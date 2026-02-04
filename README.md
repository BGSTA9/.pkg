# ML Package Offline Cache

A local cache of machine learning and deep learning packages for offline installation.

## Quick Start

### Install a Package

```bash
# Install latest version
python install_offline.py torch numpy pandas

# Install specific version
python install_offline.py torch==2.4.0

# List all available packages
python install_offline.py --list

# Search for packages
python install_offline.py --search transformer
```

### Use with Virtual Environment

```bash
# Create and activate venv
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# or: .venv\Scripts\activate  # Windows

# Install from offline cache
python install_offline.py torch torchvision numpy pandas matplotlib jupyter
```

## Available Packages

### Deep Learning Frameworks
- **PyTorch** (with CUDA 11.8, 12.1, 12.4)
- **TensorFlow** (with GPU support)
- **JAX**

### Core Scientific Stack
- NumPy, SciPy, Pandas, Matplotlib, scikit-learn, OpenCV, Pillow

### NLP & Transformers
- transformers, tokenizers, datasets, accelerate, spacy

### Training Tools
- tensorboard, wandb, mlflow, optuna, lightning

### Jupyter
- jupyter, jupyterlab, notebook, ipykernel

## Structure

```
ml_packages/
├── install_offline.py    # Install packages from cache
├── download_packages.py  # Download/update packages
├── packages/             # Downloaded wheels
│   └── {package}/{version}/
└── index/
    └── package_index.json
```

## Updating the Cache

```bash
# Download all packages
python download_packages.py --output-dir ./ml_packages

# Sync to Google Drive
python download_packages.py --output-dir ./ml_packages --sync-to-gdrive
```

## Supported Platforms

| Platform | Tag |
|----------|-----|
| macOS Intel | macosx_10_9_x86_64 |
| macOS Apple Silicon | macosx_11_0_arm64 |
| Linux x86_64 | manylinux_x86_64 |
| Windows x64 | win_amd64 |

## Python Versions

- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12
