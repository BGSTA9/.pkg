#!/usr/bin/env python3
"""
ML Package Downloader - Direct to Google Drive
Downloads ML/DL packages and immediately uploads to Google Drive.
Minimal local storage required (~2GB temp space max).

Usage:
    python download_packages.py
    python download_packages.py --start-from 5   # Resume from package 5
"""

import os
import sys
import json
import subprocess
import shutil
import tempfile
import argparse
from pathlib import Path
from datetime import datetime

# =============================================================================
# CONFIGURATION
# =============================================================================

PYTHON_VERSIONS = ["3.9", "3.10", "3.11", "3.12"]

PLATFORMS = {
    "linux": "manylinux2014_x86_64",
    "macos_intel": "macosx_10_9_x86_64",
    "macos_arm": "macosx_11_0_arm64", 
    "windows": "win_amd64"
}

# PyTorch CUDA index URLs
PYTORCH_INDEX_URLS = {
    "cu118": "https://download.pytorch.org/whl/cu118",
    "cu121": "https://download.pytorch.org/whl/cu121",
    "cu124": "https://download.pytorch.org/whl/cu124",
}

# Google Drive settings
GDRIVE_REMOTE = "gdrive"
GDRIVE_PATH = "ml_packages"

# Package definitions
PACKAGES = {
    # Tier 1: Deep Learning Frameworks
    "torch": {
        "versions": ["2.0.0", "2.1.0", "2.2.0", "2.3.0", "2.4.0"],
        "cuda": True,
    },
    "torchvision": {
        "versions": ["0.15.0", "0.16.0", "0.17.0", "0.18.0", "0.19.0"],
    },
    "torchaudio": {
        "versions": ["2.0.0", "2.1.0", "2.2.0", "2.3.0", "2.4.0"],
    },
    "tensorflow": {
        "versions": ["2.13.0", "2.14.0", "2.15.0"],
    },
    
    # Tier 2: Core Scientific Stack
    "numpy": {"versions": ["1.24.0", "1.25.0", "1.26.0", "2.0.0"]},
    "scipy": {"versions": ["1.11.0", "1.12.0", "1.13.0", "1.14.0"]},
    "pandas": {"versions": ["2.0.0", "2.1.0", "2.2.0"]},
    "matplotlib": {"versions": ["3.7.0", "3.8.0", "3.9.0"]},
    "scikit-learn": {"versions": ["1.3.0", "1.4.0", "1.5.0"]},
    "opencv-python": {"versions": ["4.9.0.80", "4.10.0.84"]},
    "Pillow": {"versions": ["10.2.0", "10.3.0", "10.4.0"]},
    
    # Tier 3: NLP & Transformers
    "transformers": {"versions": ["4.38.0", "4.39.0", "4.40.0"]},
    "tokenizers": {"versions": ["0.19.0", "0.20.0"]},
    "datasets": {"versions": ["2.18.0", "2.19.0", "2.20.0"]},
    "accelerate": {"versions": ["0.27.0", "0.28.0"]},
    "safetensors": {"versions": ["0.4.2", "0.4.3"]},
    
    # Tier 4: Training Tools
    "tensorboard": {"versions": ["2.15.0", "2.16.0", "2.17.0"]},
    "lightning": {"versions": ["2.2.0", "2.3.0", "2.4.0"]},
    "wandb": {"versions": ["0.17.0", "0.18.0"]},
    "optuna": {"versions": ["3.6.0", "4.0.0"]},
    
    # Tier 5: Jupyter
    "jupyterlab": {"versions": ["4.1.0", "4.2.0"]},
    "notebook": {"versions": ["7.1.0", "7.2.0"]},
    "ipykernel": {"versions": ["6.28.0", "6.29.0"]},
    
    # Tier 6: Utilities
    "tqdm": {"versions": ["4.66.0"]},
    "pyyaml": {"versions": ["6.0.1"]},
    "rich": {"versions": ["13.7.0"]},
    "h5py": {"versions": ["3.10.0", "3.11.0"]},
    "onnx": {"versions": ["1.15.0", "1.16.0"]},
    "onnxruntime": {"versions": ["1.17.0", "1.18.0"]},
    "einops": {"versions": ["0.7.0", "0.8.0"]},
}


def log(message: str):
    """Print timestamped log message."""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")


def upload_to_gdrive(local_path: Path, remote_subpath: str) -> bool:
    """Upload a file to Google Drive using rclone."""
    remote_full = f"{GDRIVE_REMOTE}:{GDRIVE_PATH}/{remote_subpath}"
    
    cmd = ["rclone", "copy", str(local_path), remote_full, "--progress"]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        return result.returncode == 0
    except Exception as e:
        log(f"    Upload error: {e}")
        return False


def check_exists_on_gdrive(remote_subpath: str, filename: str) -> bool:
    """Check if a file already exists on Google Drive."""
    remote_full = f"{GDRIVE_REMOTE}:{GDRIVE_PATH}/{remote_subpath}/{filename}"
    
    cmd = ["rclone", "lsf", remote_full]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return result.returncode == 0 and filename in result.stdout
    except:
        return False


def download_and_upload_package(pkg_name: str, version: str, 
                                temp_dir: Path,
                                python_version: str = None, 
                                platform: str = None,
                                extra_index_url: str = None) -> int:
    """Download a package and immediately upload to Google Drive."""
    
    # Clear temp dir
    for f in temp_dir.iterdir():
        if f.is_file():
            f.unlink()
    
    cmd = [
        sys.executable, "-m", "pip", "download",
        f"{pkg_name}=={version}",
        "--dest", str(temp_dir),
        "--no-deps",
    ]
    
    if python_version:
        cmd.extend(["--python-version", python_version])
    if platform:
        cmd.extend(["--platform", platform])
    if extra_index_url:
        cmd.extend(["--extra-index-url", extra_index_url])
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        if result.returncode != 0:
            return 0
            
        # Upload downloaded files
        uploaded = 0
        remote_subpath = f"packages/{pkg_name}/{version}"
        
        for f in temp_dir.iterdir():
            if f.suffix in [".whl", ".tar.gz", ".zip"]:
                if upload_to_gdrive(f, remote_subpath):
                    uploaded += 1
                    log(f"    ✓ Uploaded: {f.name}")
                f.unlink()  # Delete local file
                
        return uploaded
        
    except subprocess.TimeoutExpired:
        return 0
    except Exception as e:
        log(f"    Error: {e}")
        return 0


def download_pytorch_cuda(version: str, cuda_version: str, temp_dir: Path):
    """Download PyTorch with CUDA support."""
    index_url = PYTORCH_INDEX_URLS.get(cuda_version)
    if not index_url:
        return
    
    packages = ["torch", "torchvision", "torchaudio"]
    
    for py_ver in PYTHON_VERSIONS:
        for pkg in packages:
            # Clear temp dir
            for f in temp_dir.iterdir():
                if f.is_file():
                    f.unlink()
                    
            cmd = [
                sys.executable, "-m", "pip", "download",
                pkg,
                "--dest", str(temp_dir),
                "--index-url", index_url,
                "--python-version", py_ver,
                "--no-deps",
            ]
            
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
                
                if result.returncode == 0:
                    remote_subpath = f"packages/torch/{version}+{cuda_version}"
                    for f in temp_dir.iterdir():
                        if f.suffix == ".whl":
                            if upload_to_gdrive(f, remote_subpath):
                                log(f"    ✓ {pkg} (CUDA {cuda_version}, py{py_ver})")
                            f.unlink()
            except Exception as e:
                log(f"    ✗ {pkg}: {e}")


def main():
    parser = argparse.ArgumentParser(description="ML Package Downloader - Direct to Google Drive")
    parser.add_argument("--start-from", type=int, default=1,
                        help="Resume from package number (1-indexed, matches [X/79] output)")
    args = parser.parse_args()
    start_from = args.start_from
    
    log("=" * 60)
    log("ML Package Downloader - Direct to Google Drive")
    log("=" * 60)
    log("")
    
    # Check rclone is configured
    result = subprocess.run(["rclone", "listremotes"], capture_output=True, text=True)
    if "gdrive:" not in result.stdout:
        log("❌ Error: 'gdrive' remote not configured in rclone")
        log("   Run: ./setup_rclone.sh")
        sys.exit(1)
    
    log(f"✓ Using rclone remote: {GDRIVE_REMOTE}:{GDRIVE_PATH}")
    if start_from > 1:
        log(f"⏩ Resuming from package #{start_from}")
    log("")
    
    # Create temp directory for downloads
    temp_dir = Path(tempfile.mkdtemp(prefix="ml_packages_"))
    log(f"📁 Temp directory: {temp_dir}")
    log("")
    
    total_packages = sum(len(pkg.get("versions", [])) for pkg in PACKAGES.values())
    current = 0
    total_uploaded = 0
    
    try:
        for pkg_name, pkg_config in PACKAGES.items():
            versions = pkg_config.get("versions", [])
            is_cuda = pkg_config.get("cuda", False)
            
            log(f"📦 {pkg_name} ({len(versions)} versions)")
            
            for version in versions:
                current += 1
                
                # Skip if before start_from
                if current < start_from:
                    log(f"  [{current}/{total_packages}] {pkg_name}=={version} (skipped)")
                    continue
                
                log(f"  [{current}/{total_packages}] {pkg_name}=={version}")
                
                # Download for each Python version and platform
                for py_ver in PYTHON_VERSIONS:
                    for plat_name, plat_tag in PLATFORMS.items():
                        count = download_and_upload_package(
                            pkg_name, version, temp_dir,
                            python_version=py_ver,
                            platform=plat_tag
                        )
                        total_uploaded += count
                
                # Handle CUDA builds for PyTorch
                if pkg_name == "torch" and is_cuda:
                    for cuda_ver in ["cu118", "cu121", "cu124"]:
                        log(f"    → CUDA {cuda_ver}...")
                        download_pytorch_cuda(version, cuda_ver, temp_dir)
                        
        log("")
        log("=" * 60)
        log(f"✅ Complete! Uploaded {total_uploaded} files to Google Drive")
        log("=" * 60)
        
    finally:
        # Cleanup temp directory
        shutil.rmtree(temp_dir, ignore_errors=True)
        log(f"🧹 Cleaned up temp directory")


if __name__ == "__main__":
    main()
