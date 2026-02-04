#!/usr/bin/env python3
"""
Offline Package Installer
Install packages from the local ML package cache.

Usage:
    python install_offline.py torch numpy pandas
    python install_offline.py torch==2.4.0 --python-version 3.11
    python install_offline.py --list
    python install_offline.py --search transformer
"""

import os
import sys
import json
import platform
import subprocess
import argparse
from pathlib import Path
from typing import Optional, List


def get_platform_tag() -> str:
    """Detect the current platform and return the wheel platform tag."""
    system = platform.system().lower()
    machine = platform.machine().lower()
    
    if system == "darwin":
        if machine == "arm64":
            return "macosx_11_0_arm64"
        else:
            return "macosx_10_9_x86_64"
    elif system == "linux":
        return "manylinux"  # Will match manylinux1, manylinux2014, etc.
    elif system == "windows":
        return "win_amd64"
    else:
        return "any"


def get_python_version_tag() -> str:
    """Get the current Python version as a wheel tag."""
    major = sys.version_info.major
    minor = sys.version_info.minor
    return f"cp{major}{minor}"


def find_package_cache(start_path: Optional[Path] = None) -> Optional[Path]:
    """Find the ml_packages directory."""
    # Check common locations
    search_paths = [
        start_path,
        Path.cwd() / "ml_packages",
        Path.home() / "ml_packages",
        Path("/Volumes/GoogleDrive/My Drive/ml_packages"),  # macOS Google Drive
        Path.home() / "Google Drive/ml_packages",
        Path.home() / "Library/CloudStorage/GoogleDrive-*/My Drive/ml_packages",
    ]
    
    for path in search_paths:
        if path and path.exists() and (path / "packages").exists():
            return path
            
    return None


class OfflineInstaller:
    def __init__(self, cache_dir: Path):
        self.cache_dir = cache_dir
        self.packages_dir = cache_dir / "packages"
        self.index_file = cache_dir / "index" / "package_index.json"
        self.platform_tag = get_platform_tag()
        self.python_tag = get_python_version_tag()
        self.index = self._load_index()
        
    def _load_index(self) -> dict:
        """Load the package index."""
        if self.index_file.exists():
            with open(self.index_file) as f:
                return json.load(f)
        return {"packages": {}}
        
    def list_packages(self):
        """List all available packages."""
        print("\n📦 Available Packages:\n")
        print(f"{'Package':<25} {'Versions':<50}")
        print("-" * 75)
        
        for pkg_name, pkg_data in sorted(self.index.get("packages", {}).items()):
            versions = list(pkg_data.get("versions", {}).keys())
            versions_str = ", ".join(sorted(versions, reverse=True)[:5])
            if len(versions) > 5:
                versions_str += f" (+{len(versions) - 5} more)"
            print(f"{pkg_name:<25} {versions_str:<50}")
            
    def search_packages(self, query: str):
        """Search for packages matching a query."""
        print(f"\n🔍 Searching for '{query}'...\n")
        
        matches = []
        for pkg_name in self.index.get("packages", {}).keys():
            if query.lower() in pkg_name.lower():
                matches.append(pkg_name)
                
        if matches:
            for pkg in sorted(matches):
                versions = list(self.index["packages"][pkg].get("versions", {}).keys())
                print(f"  • {pkg}: {', '.join(sorted(versions, reverse=True)[:3])}")
        else:
            print("  No packages found.")
            
    def find_wheel(self, package_name: str, version: str) -> Optional[Path]:
        """Find the best matching wheel for the current system."""
        pkg_dir = self.packages_dir / package_name / version
        
        if not pkg_dir.exists():
            # Try CUDA versions for torch
            if package_name == "torch":
                for cuda_suffix in ["+cu124", "+cu121", "+cu118"]:
                    cuda_dir = self.packages_dir / package_name / f"{version}{cuda_suffix}"
                    if cuda_dir.exists():
                        pkg_dir = cuda_dir
                        break
                        
        if not pkg_dir.exists():
            return None
            
        # Score each wheel file by compatibility
        candidates = []
        
        for f in pkg_dir.iterdir():
            if not f.suffix == ".whl":
                continue
                
            name = f.name
            score = 0
            
            # Check Python version compatibility
            if self.python_tag in name or "py3-" in name or "py2.py3-" in name:
                score += 10
                
            # Check platform compatibility  
            if self.platform_tag in name:
                score += 20
            elif "any" in name or "none-any" in name:
                score += 5
                
            # Prefer manylinux on Linux
            if "linux" in self.platform_tag and "manylinux" in name:
                score += 15
                
            if score > 0:
                candidates.append((score, f))
                
        # Also check for source distributions
        for f in pkg_dir.iterdir():
            if f.suffix in [".tar.gz", ".zip"] and ".whl" not in f.name:
                candidates.append((1, f))  # Low priority
                
        if not candidates:
            return None
            
        # Return highest scoring candidate
        candidates.sort(key=lambda x: x[0], reverse=True)
        return candidates[0][1]
        
    def install_package(self, package_spec: str, upgrade: bool = False) -> bool:
        """Install a package from the cache."""
        # Parse package spec (e.g., "torch==2.4.0" or "numpy")
        if "==" in package_spec:
            package_name, version = package_spec.split("==")
        else:
            package_name = package_spec
            # Find latest version
            pkg_data = self.index.get("packages", {}).get(package_name, {})
            versions = list(pkg_data.get("versions", {}).keys())
            if not versions:
                print(f"❌ Package '{package_name}' not found in cache")
                return False
            version = sorted(versions, reverse=True)[0]
            
        wheel_path = self.find_wheel(package_name, version)
        
        if not wheel_path:
            print(f"❌ No compatible wheel found for {package_name}=={version}")
            print(f"   Platform: {self.platform_tag}, Python: {self.python_tag}")
            return False
            
        print(f"📦 Installing {package_name}=={version} from {wheel_path.name}...")
        
        cmd = [sys.executable, "-m", "pip", "install", str(wheel_path)]
        if upgrade:
            cmd.append("--upgrade")
            
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ Successfully installed {package_name}=={version}")
                return True
            else:
                print(f"❌ Installation failed: {result.stderr[:200]}")
                return False
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
            
    def install_packages(self, packages: List[str], upgrade: bool = False):
        """Install multiple packages."""
        success = 0
        failed = 0
        
        for pkg in packages:
            if self.install_package(pkg, upgrade):
                success += 1
            else:
                failed += 1
                
        print(f"\n📊 Results: {success} succeeded, {failed} failed")


def main():
    parser = argparse.ArgumentParser(
        description="Install packages from offline cache",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python install_offline.py torch numpy pandas
    python install_offline.py torch==2.4.0
    python install_offline.py --list
    python install_offline.py --search transformer
        """
    )
    parser.add_argument(
        "packages",
        nargs="*",
        help="Packages to install (e.g., 'torch' or 'torch==2.4.0')"
    )
    parser.add_argument(
        "--cache-dir", "-c",
        type=Path,
        help="Path to the ml_packages cache directory"
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List all available packages"
    )
    parser.add_argument(
        "--search", "-s",
        type=str,
        help="Search for packages"
    )
    parser.add_argument(
        "--upgrade", "-U",
        action="store_true",
        help="Upgrade packages"
    )
    
    args = parser.parse_args()
    
    # Find cache directory
    cache_dir = args.cache_dir or find_package_cache()
    
    if not cache_dir:
        print("❌ Could not find ml_packages directory.")
        print("   Please specify with --cache-dir or ensure it exists in a standard location.")
        sys.exit(1)
        
    print(f"📂 Using cache: {cache_dir}")
    print(f"🖥️  Platform: {get_platform_tag()}, Python: {get_python_version_tag()}")
    
    installer = OfflineInstaller(cache_dir)
    
    if args.list:
        installer.list_packages()
    elif args.search:
        installer.search_packages(args.search)
    elif args.packages:
        installer.install_packages(args.packages, args.upgrade)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
