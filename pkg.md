(base) soheilsanati@Soheils-MacBook-Pro pkg % ./setup_rclone.sh

🔧 rclone Setup for Google Drive
=================================

✅ rclone is installed: rclone v1.73.0

✅ 'gdrive' remote already configured.

Testing connection...
           0 2026-02-04 16:47:25        -1 .pkg
           0 2023-07-09 23:26:56        -1 Colab Notebooks
           0 2024-09-17 11:10:49        -1 Heat-Equation (PINN)
           0 2025-04-28 17:22:56        -1 TSSF／CMAS 1*
           0 2025-04-28 17:23:11        -1 TSSF／CMAS 2**
✅ Connection successful!

=================================
🎉 Setup Complete!
=================================

You can now use the download script with Google Drive sync:

  python download_packages.py --output-dir ./ml_packages --sync-to-gdrive

Or manually sync with:

  rclone sync ./ml_packages gdrive:ml_packages --progress

(base) soheilsanati@Soheils-MacBook-Pro pkg % python download_packages.py
[17:47:46] ============================================================
[17:47:46] ML Package Downloader - Direct to Google Drive
[17:47:46] ============================================================
[17:47:46] 
[17:47:46] ✓ Using rclone remote: gdrive:ml_packages
[17:47:46] 
[17:47:46] 📁 Temp directory: /var/folders/j1/9fxjp53j61vcxxw21brhmtyr0000gn/T/ml_packages_elpdxjph
[17:47:46] 
[17:47:46] 📦 torch (5 versions)
[17:47:46]   [1/79] torch==2.0.0
[17:57:03]     ✓ Uploaded: torch-2.0.0-cp39-none-macosx_10_9_x86_64.whl
[17:59:01]     ✓ Uploaded: torch-2.0.0-cp39-none-macosx_11_0_arm64.whl
[18:03:26]     ✓ Uploaded: torch-2.0.0-cp39-cp39-win_amd64.whl
[18:11:45]     ✓ Uploaded: torch-2.0.0-cp310-none-macosx_10_9_x86_64.whl
[18:12:19]     ✓ Uploaded: torch-2.0.0-cp310-none-macosx_11_0_arm64.whl
[18:14:44]     ✓ Uploaded: torch-2.0.0-cp310-cp310-win_amd64.whl
[18:21:26]     ✓ Uploaded: torch-2.0.0-cp311-none-macosx_10_9_x86_64.whl
[18:21:49]     ✓ Uploaded: torch-2.0.0-cp311-none-macosx_11_0_arm64.whl
[18:22:55]     ✓ Uploaded: torch-2.0.0-cp311-cp311-win_amd64.whl
[18:22:57]     → CUDA cu118...
[18:23:10]     ✓ torchvision (CUDA cu118, py3.9)
[18:23:19]     ✓ torchaudio (CUDA cu118, py3.9)
[18:23:28]     ✓ torchvision (CUDA cu118, py3.10)
[18:23:36]     ✓ torchaudio (CUDA cu118, py3.10)
[18:23:43]     ✓ torchvision (CUDA cu118, py3.11)
[18:23:49]     ✓ torchvision (CUDA cu118, py3.12)
[18:23:51]     → CUDA cu121...
[18:24:01]     ✓ torchvision (CUDA cu121, py3.9)
[18:24:08]     ✓ torchaudio (CUDA cu121, py3.9)
[18:24:15]     ✓ torchvision (CUDA cu121, py3.10)
[18:24:22]     ✓ torchaudio (CUDA cu121, py3.10)
[18:24:28]     ✓ torchvision (CUDA cu121, py3.11)
[18:24:34]     ✓ torchvision (CUDA cu121, py3.12)
[18:24:35]     → CUDA cu124...
[18:24:46]     ✓ torchvision (CUDA cu124, py3.9)
[18:24:52]     ✓ torchaudio (CUDA cu124, py3.9)
[18:24:59]     ✓ torchvision (CUDA cu124, py3.10)
[18:25:07]     ✓ torchaudio (CUDA cu124, py3.10)
[18:25:14]     ✓ torchvision (CUDA cu124, py3.11)
[18:25:20]     ✓ torchvision (CUDA cu124, py3.12)
[18:25:22]   [2/79] torch==2.1.0
[18:30:03]     ✓ Uploaded: torch-2.1.0-cp39-cp39-manylinux1_x86_64.whl
[18:30:55]     ✓ Uploaded: torch-2.1.0-cp39-none-macosx_10_9_x86_64.whl
[18:31:16]     ✓ Uploaded: torch-2.1.0-cp39-none-macosx_11_0_arm64.whl
[18:32:09]     ✓ Uploaded: torch-2.1.0-cp39-cp39-win_amd64.whl
[18:35:12]     ✓ Uploaded: torch-2.1.0-cp310-cp310-manylinux1_x86_64.whl
[18:36:03]     ✓ Uploaded: torch-2.1.0-cp310-none-macosx_10_9_x86_64.whl
[18:36:24]     ✓ Uploaded: torch-2.1.0-cp310-none-macosx_11_0_arm64.whl
[18:38:05]     ✓ Uploaded: torch-2.1.0-cp310-cp310-win_amd64.whl
[18:40:29]     ✓ Uploaded: torch-2.1.0-cp311-cp311-manylinux1_x86_64.whl
[18:41:42]     ✓ Uploaded: torch-2.1.0-cp311-none-macosx_10_9_x86_64.whl
[18:42:06]     ✓ Uploaded: torch-2.1.0-cp311-none-macosx_11_0_arm64.whl
[18:43:27]     ✓ Uploaded: torch-2.1.0-cp311-cp311-win_amd64.whl
[18:43:30]     → CUDA cu118...
[18:43:39]     ✓ torchvision (CUDA cu118, py3.9)
[18:43:46]     ✓ torchaudio (CUDA cu118, py3.9)
[18:43:53]     ✓ torchvision (CUDA cu118, py3.10)
[18:44:01]     ✓ torchaudio (CUDA cu118, py3.10)
[18:44:07]     ✓ torchvision (CUDA cu118, py3.11)
[18:44:15]     ✓ torchvision (CUDA cu118, py3.12)
[18:44:16]     → CUDA cu121...
[18:44:28]     ✓ torchvision (CUDA cu121, py3.9)
[18:44:37]     ✓ torchaudio (CUDA cu121, py3.9)
[18:44:44]     ✓ torchvision (CUDA cu121, py3.10)
[18:44:51]     ✓ torchaudio (CUDA cu121, py3.10)
[18:44:58]     ✓ torchvision (CUDA cu121, py3.11)
[18:45:04]     ✓ torchvision (CUDA cu121, py3.12)
[18:45:05]     → CUDA cu124...
[18:45:15]     ✓ torchvision (CUDA cu124, py3.9)
[18:45:22]     ✓ torchaudio (CUDA cu124, py3.9)
[18:45:29]     ✓ torchvision (CUDA cu124, py3.10)
[18:45:35]     ✓ torchaudio (CUDA cu124, py3.10)
[18:45:42]     ✓ torchvision (CUDA cu124, py3.11)
[18:45:49]     ✓ torchvision (CUDA cu124, py3.12)
[18:45:50]   [3/79] torch==2.2.0
[18:52:01]     ✓ Uploaded: torch-2.2.0-cp39-cp39-manylinux1_x86_64.whl
[18:52:43]     ✓ Uploaded: torch-2.2.0-cp39-none-macosx_10_9_x86_64.whl
[18:53:02]     ✓ Uploaded: torch-2.2.0-cp39-none-macosx_11_0_arm64.whl
[18:53:58]     ✓ Uploaded: torch-2.2.0-cp39-cp39-win_amd64.whl
[18:57:52]     ✓ Uploaded: torch-2.2.0-cp310-cp310-manylinux1_x86_64.whl
[18:59:05]     ✓ Uploaded: torch-2.2.0-cp310-none-macosx_10_9_x86_64.whl
[18:59:24]     ✓ Uploaded: torch-2.2.0-cp310-none-macosx_11_0_arm64.whl
[19:00:34]     ✓ Uploaded: torch-2.2.0-cp310-cp310-win_amd64.whl
[19:06:52]     ✓ Uploaded: torch-2.2.0-cp311-none-macosx_10_9_x86_64.whl
[19:07:17]     ✓ Uploaded: torch-2.2.0-cp311-none-macosx_11_0_arm64.whl
[19:08:08]     ✓ Uploaded: torch-2.2.0-cp311-cp311-win_amd64.whl
