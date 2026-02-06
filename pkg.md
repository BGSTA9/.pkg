(base) soheilsanati@Soheils-MacBook-Pro pkg % ./setup_rclone.sh

🔧 rclone Setup for Google Drive
=================================

✅ rclone is installed: rclone v1.73.0

✅ 'gdrive' remote already configured.

Testing connection...
           0 2026-02-04 16:47:25        -1 .pkg
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
[19:14:04]     ✓ Uploaded: torch-2.2.0-cp312-cp312-manylinux1_x86_64.whl
[19:14:58]     ✓ Uploaded: torch-2.2.0-cp312-none-macosx_10_9_x86_64.whl
[19:15:39]     ✓ Uploaded: torch-2.2.0-cp312-none-macosx_11_0_arm64.whl
[19:17:00]     ✓ Uploaded: torch-2.2.0-cp312-cp312-win_amd64.whl
[19:17:00]     → CUDA cu118...
[19:17:10]     ✓ torchvision (CUDA cu118, py3.9)
[19:17:16]     ✓ torchaudio (CUDA cu118, py3.9)
[19:17:23]     ✓ torchvision (CUDA cu118, py3.10)
[19:17:30]     ✓ torchaudio (CUDA cu118, py3.10)
[19:17:36]     ✓ torchvision (CUDA cu118, py3.11)
[19:17:44]     ✓ torchvision (CUDA cu118, py3.12)
[19:17:45]     → CUDA cu121...
[19:17:54]     ✓ torchvision (CUDA cu121, py3.9)
[19:18:01]     ✓ torchaudio (CUDA cu121, py3.9)
[19:18:08]     ✓ torchvision (CUDA cu121, py3.10)
[19:18:15]     ✓ torchaudio (CUDA cu121, py3.10)
[19:18:21]     ✓ torchvision (CUDA cu121, py3.11)
[19:18:28]     ✓ torchvision (CUDA cu121, py3.12)
[19:18:29]     → CUDA cu124...
[19:18:39]     ✓ torchvision (CUDA cu124, py3.9)
[19:18:44]     ✓ torchaudio (CUDA cu124, py3.9)
[19:18:51]     ✓ torchvision (CUDA cu124, py3.10)
[19:18:57]     ✓ torchaudio (CUDA cu124, py3.10)
[19:19:04]     ✓ torchvision (CUDA cu124, py3.11)
[19:19:14]     ✓ torchvision (CUDA cu124, py3.12)
[19:19:15]   [4/79] torch==2.3.0
[19:25:20]     ✓ Uploaded: torch-2.3.0-cp39-none-macosx_11_0_arm64.whl
[19:27:11]     ✓ Uploaded: torch-2.3.0-cp39-cp39-win_amd64.whl
[19:32:36]     ✓ Uploaded: torch-2.3.0-cp310-none-macosx_11_0_arm64.whl
[19:33:23]     ✓ Uploaded: torch-2.3.0-cp310-cp310-win_amd64.whl
[19:38:10]     ✓ Uploaded: torch-2.3.0-cp311-cp311-manylinux1_x86_64.whl
[19:38:57]     ✓ Uploaded: torch-2.3.0-cp311-none-macosx_11_0_arm64.whl
[19:40:16]     ✓ Uploaded: torch-2.3.0-cp311-cp311-win_amd64.whl
[19:45:52]     ✓ Uploaded: torch-2.3.0-cp312-none-macosx_11_0_arm64.whl
[19:47:15]     ✓ Uploaded: torch-2.3.0-cp312-cp312-win_amd64.whl
[19:47:15]     → CUDA cu118...
[19:47:26]     ✓ torchvision (CUDA cu118, py3.9)
[19:47:34]     ✓ torchaudio (CUDA cu118, py3.9)
[19:47:41]     ✓ torchvision (CUDA cu118, py3.10)
[19:47:48]     ✓ torchaudio (CUDA cu118, py3.10)
[19:47:55]     ✓ torchvision (CUDA cu118, py3.11)
[19:48:02]     ✓ torchvision (CUDA cu118, py3.12)
[19:48:03]     → CUDA cu121...
[19:48:12]     ✓ torchvision (CUDA cu121, py3.9)
[19:48:20]     ✓ torchaudio (CUDA cu121, py3.9)
[19:48:28]     ✓ torchvision (CUDA cu121, py3.10)
[19:48:33]     ✓ torchaudio (CUDA cu121, py3.10)
[19:48:40]     ✓ torchvision (CUDA cu121, py3.11)
[19:48:46]     ✓ torchvision (CUDA cu121, py3.12)
[19:48:47]     → CUDA cu124...
[19:48:57]     ✓ torchvision (CUDA cu124, py3.9)
[19:49:04]     ✓ torchaudio (CUDA cu124, py3.9)
[19:49:11]     ✓ torchvision (CUDA cu124, py3.10)
[19:49:17]     ✓ torchaudio (CUDA cu124, py3.10)
[19:49:25]     ✓ torchvision (CUDA cu124, py3.11)
[19:49:34]     ✓ torchvision (CUDA cu124, py3.12)
[19:49:35]   [5/79] torch==2.4.0
[20:10:04]     ✓ Uploaded: torch-2.4.0-cp39-none-macosx_11_0_arm64.whl
[20:11:23]     ✓ Uploaded: torch-2.4.0-cp39-cp39-win_amd64.whl
[20:14:23]     ✓ Uploaded: torch-2.4.0-cp310-cp310-manylinux1_x86_64.whl
[20:14:59]     ✓ Uploaded: torch-2.4.0-cp310-none-macosx_11_0_arm64.whl
>>> Continue from here ...
[15:23:45] ============================================================
[15:23:45] ML Package Downloader - Direct to Google Drive
[15:23:45] ============================================================
[15:23:45] 
[15:23:45] ✓ Using rclone remote: gdrive:ml_packages
[15:23:45] ⏩ Resuming from package #6
[15:23:45] 
[15:23:45] 📁 Temp directory: /var/folders/j1/9fxjp53j61vcxxw21brhmtyr0000gn/T/ml_packages_qai8qqza
[15:23:45] 
[15:23:45] 📦 torch (5 versions)
[15:23:45]   [1/79] torch==2.0.0 (skipped)
[15:23:45]   [2/79] torch==2.1.0 (skipped)
[15:23:45]   [3/79] torch==2.2.0 (skipped)
[15:23:45]   [4/79] torch==2.3.0 (skipped)
[15:23:45]   [5/79] torch==2.4.0 (skipped)
[15:23:45] 📦 torchvision (5 versions)
[15:23:45]   [6/79] torchvision==0.15.0
[15:23:58]     ✓ Uploaded: torchvision-0.15.0-cp39-cp39-manylinux1_x86_64.whl
[15:24:04]     ✓ Uploaded: torchvision-0.15.0-cp39-cp39-macosx_10_9_x86_64.whl
[15:24:11]     ✓ Uploaded: torchvision-0.15.0-cp39-cp39-macosx_11_0_arm64.whl
[15:24:17]     ✓ Uploaded: torchvision-0.15.0-cp39-cp39-win_amd64.whl
[15:24:27]     ✓ Uploaded: torchvision-0.15.0-cp310-cp310-manylinux1_x86_64.whl
[15:24:33]     ✓ Uploaded: torchvision-0.15.0-cp310-cp310-macosx_10_9_x86_64.whl
[15:24:39]     ✓ Uploaded: torchvision-0.15.0-cp310-cp310-macosx_11_0_arm64.whl
[15:24:45]     ✓ Uploaded: torchvision-0.15.0-cp310-cp310-win_amd64.whl
[15:24:51]     ✓ Uploaded: torchvision-0.15.0-cp311-cp311-manylinux1_x86_64.whl
[15:24:59]     ✓ Uploaded: torchvision-0.15.0-cp311-cp311-macosx_10_9_x86_64.whl
[15:25:06]     ✓ Uploaded: torchvision-0.15.0-cp311-cp311-macosx_11_0_arm64.whl
[15:25:12]     ✓ Uploaded: torchvision-0.15.0-cp311-cp311-win_amd64.whl
[15:25:15]   [7/79] torchvision==0.16.0
[15:25:25]     ✓ Uploaded: torchvision-0.16.0-cp39-cp39-manylinux1_x86_64.whl
[15:25:32]     ✓ Uploaded: torchvision-0.16.0-cp39-cp39-macosx_11_0_arm64.whl
[15:25:37]     ✓ Uploaded: torchvision-0.16.0-cp39-cp39-win_amd64.whl
[15:25:43]     ✓ Uploaded: torchvision-0.16.0-cp310-cp310-manylinux1_x86_64.whl
[15:25:48]     ✓ Uploaded: torchvision-0.16.0-cp310-cp310-macosx_11_0_arm64.whl
[15:25:54]     ✓ Uploaded: torchvision-0.16.0-cp310-cp310-win_amd64.whl
[15:25:59]     ✓ Uploaded: torchvision-0.16.0-cp311-cp311-manylinux1_x86_64.whl
[15:26:05]     ✓ Uploaded: torchvision-0.16.0-cp311-cp311-macosx_11_0_arm64.whl
[15:26:11]     ✓ Uploaded: torchvision-0.16.0-cp311-cp311-win_amd64.whl
[15:26:14]   [8/79] torchvision==0.17.0
[15:26:27]     ✓ Uploaded: torchvision-0.17.0-cp39-cp39-manylinux1_x86_64.whl
[15:26:34]     ✓ Uploaded: torchvision-0.17.0-cp39-cp39-macosx_11_0_arm64.whl
[15:26:39]     ✓ Uploaded: torchvision-0.17.0-cp39-cp39-win_amd64.whl
[15:26:47]     ✓ Uploaded: torchvision-0.17.0-cp310-cp310-manylinux1_x86_64.whl
[15:26:53]     ✓ Uploaded: torchvision-0.17.0-cp310-cp310-macosx_11_0_arm64.whl
[15:26:59]     ✓ Uploaded: torchvision-0.17.0-cp310-cp310-win_amd64.whl
[15:27:07]     ✓ Uploaded: torchvision-0.17.0-cp311-cp311-manylinux1_x86_64.whl
[15:27:14]     ✓ Uploaded: torchvision-0.17.0-cp311-cp311-macosx_11_0_arm64.whl
[15:27:20]     ✓ Uploaded: torchvision-0.17.0-cp311-cp311-win_amd64.whl
[15:27:31]     ✓ Uploaded: torchvision-0.17.0-cp312-cp312-manylinux1_x86_64.whl
[15:27:38]     ✓ Uploaded: torchvision-0.17.0-cp312-cp312-macosx_11_0_arm64.whl
[15:27:45]     ✓ Uploaded: torchvision-0.17.0-cp312-cp312-win_amd64.whl
[15:27:45]   [9/79] torchvision==0.18.0
[15:27:55]     ✓ Uploaded: torchvision-0.18.0-cp39-cp39-manylinux1_x86_64.whl
[15:28:01]     ✓ Uploaded: torchvision-0.18.0-cp39-cp39-macosx_11_0_arm64.whl
[15:28:08]     ✓ Uploaded: torchvision-0.18.0-cp39-cp39-win_amd64.whl
[15:28:16]     ✓ Uploaded: torchvision-0.18.0-cp310-cp310-manylinux1_x86_64.whl
[15:28:21]     ✓ Uploaded: torchvision-0.18.0-cp310-cp310-macosx_11_0_arm64.whl
[15:28:28]     ✓ Uploaded: torchvision-0.18.0-cp310-cp310-win_amd64.whl
[15:28:36]     ✓ Uploaded: torchvision-0.18.0-cp311-cp311-manylinux1_x86_64.whl
[15:28:41]     ✓ Uploaded: torchvision-0.18.0-cp311-cp311-macosx_11_0_arm64.whl
[15:28:49]     ✓ Uploaded: torchvision-0.18.0-cp311-cp311-win_amd64.whl
[15:28:59]     ✓ Uploaded: torchvision-0.18.0-cp312-cp312-manylinux1_x86_64.whl
[15:29:06]     ✓ Uploaded: torchvision-0.18.0-cp312-cp312-macosx_11_0_arm64.whl
[15:29:12]     ✓ Uploaded: torchvision-0.18.0-cp312-cp312-win_amd64.whl
[15:29:12]   [10/79] torchvision==0.19.0
[15:29:22]     ✓ Uploaded: torchvision-0.19.0-cp39-cp39-manylinux1_x86_64.whl
[15:29:29]     ✓ Uploaded: torchvision-0.19.0-cp39-cp39-macosx_11_0_arm64.whl
[15:29:35]     ✓ Uploaded: torchvision-0.19.0-1-cp39-cp39-win_amd64.whl
[15:29:42]     ✓ Uploaded: torchvision-0.19.0-cp310-cp310-manylinux1_x86_64.whl
[15:29:47]     ✓ Uploaded: torchvision-0.19.0-cp310-cp310-macosx_11_0_arm64.whl
[15:29:53]     ✓ Uploaded: torchvision-0.19.0-1-cp310-cp310-win_amd64.whl
[15:30:02]     ✓ Uploaded: torchvision-0.19.0-cp311-cp311-manylinux1_x86_64.whl
[15:30:10]     ✓ Uploaded: torchvision-0.19.0-cp311-cp311-macosx_11_0_arm64.whl
[15:30:16]     ✓ Uploaded: torchvision-0.19.0-1-cp311-cp311-win_amd64.whl
[15:30:29]     ✓ Uploaded: torchvision-0.19.0-cp312-cp312-manylinux1_x86_64.whl
[15:30:36]     ✓ Uploaded: torchvision-0.19.0-cp312-cp312-macosx_11_0_arm64.whl
[15:30:42]     ✓ Uploaded: torchvision-0.19.0-1-cp312-cp312-win_amd64.whl
[15:30:42] 📦 torchaudio (5 versions)
[15:30:42]   [11/79] torchaudio==2.0.0
[15:30:53]     ✓ Uploaded: torchaudio-2.0.0-cp39-cp39-manylinux1_x86_64.whl
[15:31:00]     ✓ Uploaded: torchaudio-2.0.0-cp39-cp39-macosx_10_9_x86_64.whl
[15:31:07]     ✓ Uploaded: torchaudio-2.0.0-cp39-cp39-macosx_11_0_arm64.whl
[15:31:14]     ✓ Uploaded: torchaudio-2.0.0-cp39-cp39-win_amd64.whl
[15:31:23]     ✓ Uploaded: torchaudio-2.0.0-cp310-cp310-manylinux1_x86_64.whl
[15:31:32]     ✓ Uploaded: torchaudio-2.0.0-cp310-cp310-macosx_10_9_x86_64.whl
[15:31:38]     ✓ Uploaded: torchaudio-2.0.0-cp310-cp310-macosx_11_0_arm64.whl
[15:31:43]     ✓ Uploaded: torchaudio-2.0.0-cp310-cp310-win_amd64.whl
[15:31:49]     ✓ Uploaded: torchaudio-2.0.0-cp311-cp311-manylinux1_x86_64.whl
[15:31:57]     ✓ Uploaded: torchaudio-2.0.0-cp311-cp311-macosx_10_9_x86_64.whl
[15:32:06]     ✓ Uploaded: torchaudio-2.0.0-cp311-cp311-macosx_11_0_arm64.whl
[15:32:13]     ✓ Uploaded: torchaudio-2.0.0-cp311-cp311-win_amd64.whl
[15:32:15]   [12/79] torchaudio==2.1.0
[15:32:25]     ✓ Uploaded: torchaudio-2.1.0-cp39-cp39-manylinux1_x86_64.whl
[15:32:32]     ✓ Uploaded: torchaudio-2.1.0-cp39-cp39-macosx_11_0_arm64.whl
[15:32:37]     ✓ Uploaded: torchaudio-2.1.0-cp39-cp39-win_amd64.whl
[15:32:45]     ✓ Uploaded: torchaudio-2.1.0-cp310-cp310-manylinux1_x86_64.whl
[15:32:51]     ✓ Uploaded: torchaudio-2.1.0-cp310-cp310-macosx_11_0_arm64.whl
[15:32:57]     ✓ Uploaded: torchaudio-2.1.0-cp310-cp310-win_amd64.whl
[15:33:04]     ✓ Uploaded: torchaudio-2.1.0-cp311-cp311-manylinux1_x86_64.whl
[15:33:10]     ✓ Uploaded: torchaudio-2.1.0-cp311-cp311-macosx_11_0_arm64.whl
[15:33:15]     ✓ Uploaded: torchaudio-2.1.0-cp311-cp311-win_amd64.whl
[15:33:18]   [13/79] torchaudio==2.2.0
[15:33:27]     ✓ Uploaded: torchaudio-2.2.0-cp39-cp39-manylinux1_x86_64.whl
[15:33:34]     ✓ Uploaded: torchaudio-2.2.0-cp39-cp39-macosx_11_0_arm64.whl
[15:33:41]     ✓ Uploaded: torchaudio-2.2.0-cp39-cp39-win_amd64.whl
[15:33:47]     ✓ Uploaded: torchaudio-2.2.0-cp310-cp310-manylinux1_x86_64.whl
[15:33:55]     ✓ Uploaded: torchaudio-2.2.0-cp310-cp310-macosx_11_0_arm64.whl
[15:34:03]     ✓ Uploaded: torchaudio-2.2.0-cp310-cp310-win_amd64.whl
[15:34:12]     ✓ Uploaded: torchaudio-2.2.0-cp311-cp311-manylinux1_x86_64.whl
[15:34:19]     ✓ Uploaded: torchaudio-2.2.0-cp311-cp311-macosx_11_0_arm64.whl
[15:34:25]     ✓ Uploaded: torchaudio-2.2.0-cp311-cp311-win_amd64.whl
[15:34:35]     ✓ Uploaded: torchaudio-2.2.0-cp312-cp312-manylinux1_x86_64.whl
[15:34:43]     ✓ Uploaded: torchaudio-2.2.0-cp312-cp312-macosx_11_0_arm64.whl
[15:34:50]     ✓ Uploaded: torchaudio-2.2.0-cp312-cp312-win_amd64.whl
[15:34:50]   [14/79] torchaudio==2.3.0
[15:34:59]     ✓ Uploaded: torchaudio-2.3.0-cp39-cp39-manylinux1_x86_64.whl
[15:35:06]     ✓ Uploaded: torchaudio-2.3.0-cp39-cp39-macosx_11_0_arm64.whl
[15:35:13]     ✓ Uploaded: torchaudio-2.3.0-cp39-cp39-win_amd64.whl
[15:35:21]     ✓ Uploaded: torchaudio-2.3.0-cp310-cp310-manylinux1_x86_64.whl
[15:35:28]     ✓ Uploaded: torchaudio-2.3.0-cp310-cp310-macosx_11_0_arm64.whl
[15:35:36]     ✓ Uploaded: torchaudio-2.3.0-cp310-cp310-win_amd64.whl
[15:35:42]     ✓ Uploaded: torchaudio-2.3.0-cp311-cp311-manylinux1_x86_64.whl
[15:35:49]     ✓ Uploaded: torchaudio-2.3.0-cp311-cp311-macosx_11_0_arm64.whl
[15:35:55]     ✓ Uploaded: torchaudio-2.3.0-cp311-cp311-win_amd64.whl
[15:36:03]     ✓ Uploaded: torchaudio-2.3.0-cp312-cp312-manylinux1_x86_64.whl
[15:36:10]     ✓ Uploaded: torchaudio-2.3.0-cp312-cp312-macosx_11_0_arm64.whl
[15:36:17]     ✓ Uploaded: torchaudio-2.3.0-cp312-cp312-win_amd64.whl
[15:36:17]   [15/79] torchaudio==2.4.0
[15:36:27]     ✓ Uploaded: torchaudio-2.4.0-cp39-cp39-manylinux1_x86_64.whl
[15:36:34]     ✓ Uploaded: torchaudio-2.4.0-cp39-cp39-macosx_11_0_arm64.whl
[15:36:42]     ✓ Uploaded: torchaudio-2.4.0-cp39-cp39-win_amd64.whl
[15:36:48]     ✓ Uploaded: torchaudio-2.4.0-cp310-cp310-manylinux1_x86_64.whl
[15:36:55]     ✓ Uploaded: torchaudio-2.4.0-cp310-cp310-macosx_11_0_arm64.whl
[15:37:01]     ✓ Uploaded: torchaudio-2.4.0-cp310-cp310-win_amd64.whl
[15:37:09]     ✓ Uploaded: torchaudio-2.4.0-cp311-cp311-manylinux1_x86_64.whl
[15:37:17]     ✓ Uploaded: torchaudio-2.4.0-cp311-cp311-macosx_11_0_arm64.whl
[15:37:23]     ✓ Uploaded: torchaudio-2.4.0-cp311-cp311-win_amd64.whl
[15:37:29]     ✓ Uploaded: torchaudio-2.4.0-cp312-cp312-manylinux1_x86_64.whl
[15:37:35]     ✓ Uploaded: torchaudio-2.4.0-cp312-cp312-macosx_11_0_arm64.whl
[15:37:43]     ✓ Uploaded: torchaudio-2.4.0-cp312-cp312-win_amd64.whl
[15:37:43] 📦 tensorflow (3 versions)
[15:37:43]   [16/79] tensorflow==2.13.0
[15:41:27]     ✓ Uploaded: tensorflow-2.13.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[15:41:34]     ✓ Uploaded: tensorflow-2.13.0-cp39-cp39-win_amd64.whl
[15:46:13]     ✓ Uploaded: tensorflow-2.13.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[15:46:19]     ✓ Uploaded: tensorflow-2.13.0-cp310-cp310-win_amd64.whl
[15:47:50]     ✓ Uploaded: tensorflow-2.13.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[15:47:57]     ✓ Uploaded: tensorflow-2.13.0-cp311-cp311-win_amd64.whl
[15:47:59]   [17/79] tensorflow==2.14.0
[15:49:54]     ✓ Uploaded: tensorflow-2.14.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[15:50:00]     ✓ Uploaded: tensorflow-2.14.0-cp39-cp39-win_amd64.whl
[15:52:44]     ✓ Uploaded: tensorflow-2.14.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[15:52:53]     ✓ Uploaded: tensorflow-2.14.0-cp310-cp310-win_amd64.whl
[15:54:50]     ✓ Uploaded: tensorflow-2.14.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[15:54:56]     ✓ Uploaded: tensorflow-2.14.0-cp311-cp311-win_amd64.whl
[15:54:59]   [18/79] tensorflow==2.15.0
[15:57:29]     ✓ Uploaded: tensorflow-2.15.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[15:57:35]     ✓ Uploaded: tensorflow-2.15.0-cp39-cp39-win_amd64.whl
[15:59:34]     ✓ Uploaded: tensorflow-2.15.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[15:59:40]     ✓ Uploaded: tensorflow-2.15.0-cp310-cp310-win_amd64.whl
[16:01:49]     ✓ Uploaded: tensorflow-2.15.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:01:59]     ✓ Uploaded: tensorflow-2.15.0-cp311-cp311-win_amd64.whl
[16:02:01] 📦 numpy (4 versions)
[16:02:01]   [19/79] numpy==1.24.0
[16:02:18]     ✓ Uploaded: numpy-1.24.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:02:32]     ✓ Uploaded: numpy-1.24.0-cp39-cp39-macosx_10_9_x86_64.whl
[16:02:48]     ✓ Uploaded: numpy-1.24.0-cp39-cp39-macosx_11_0_arm64.whl
[16:03:00]     ✓ Uploaded: numpy-1.24.0-cp39-cp39-win_amd64.whl
[16:03:12]     ✓ Uploaded: numpy-1.24.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:05:20]     ✓ Uploaded: numpy-1.24.0-cp310-cp310-macosx_10_9_x86_64.whl
[16:05:34]     ✓ Uploaded: numpy-1.24.0-cp310-cp310-macosx_11_0_arm64.whl
[16:05:44]     ✓ Uploaded: numpy-1.24.0-cp310-cp310-win_amd64.whl
[16:05:57]     ✓ Uploaded: numpy-1.24.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:06:14]     ✓ Uploaded: numpy-1.24.0-cp311-cp311-macosx_10_9_x86_64.whl
[16:06:26]     ✓ Uploaded: numpy-1.24.0-cp311-cp311-macosx_11_0_arm64.whl
[16:06:38]     ✓ Uploaded: numpy-1.24.0-cp311-cp311-win_amd64.whl
[16:06:53]   [20/79] numpy==1.25.0
[16:07:16]     ✓ Uploaded: numpy-1.25.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:07:30]     ✓ Uploaded: numpy-1.25.0-cp39-cp39-macosx_10_9_x86_64.whl
[16:07:42]     ✓ Uploaded: numpy-1.25.0-cp39-cp39-macosx_11_0_arm64.whl
[16:07:54]     ✓ Uploaded: numpy-1.25.0-cp39-cp39-win_amd64.whl
[16:08:08]     ✓ Uploaded: numpy-1.25.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:08:22]     ✓ Uploaded: numpy-1.25.0-cp310-cp310-macosx_10_9_x86_64.whl
[16:08:34]     ✓ Uploaded: numpy-1.25.0-cp310-cp310-macosx_11_0_arm64.whl
[16:08:44]     ✓ Uploaded: numpy-1.25.0-cp310-cp310-win_amd64.whl
[16:08:56]     ✓ Uploaded: numpy-1.25.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:09:05]     ✓ Uploaded: numpy-1.25.0-cp311-cp311-macosx_10_9_x86_64.whl
[16:09:20]     ✓ Uploaded: numpy-1.25.0-cp311-cp311-macosx_11_0_arm64.whl
[16:09:32]     ✓ Uploaded: numpy-1.25.0-cp311-cp311-win_amd64.whl
[16:09:45]   [21/79] numpy==1.26.0
[16:10:01]     ✓ Uploaded: numpy-1.26.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:10:13]     ✓ Uploaded: numpy-1.26.0-cp39-cp39-macosx_10_9_x86_64.whl
[16:10:25]     ✓ Uploaded: numpy-1.26.0-cp39-cp39-macosx_11_0_arm64.whl
[16:10:37]     ✓ Uploaded: numpy-1.26.0-cp39-cp39-win_amd64.whl
[16:10:49]     ✓ Uploaded: numpy-1.26.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:11:01]     ✓ Uploaded: numpy-1.26.0-cp310-cp310-macosx_10_9_x86_64.whl
[16:11:11]     ✓ Uploaded: numpy-1.26.0-cp310-cp310-macosx_11_0_arm64.whl
[16:11:23]     ✓ Uploaded: numpy-1.26.0-cp310-cp310-win_amd64.whl
[16:11:34]     ✓ Uploaded: numpy-1.26.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:11:48]     ✓ Uploaded: numpy-1.26.0-cp311-cp311-macosx_10_9_x86_64.whl
[16:12:00]     ✓ Uploaded: numpy-1.26.0-cp311-cp311-macosx_11_0_arm64.whl
[16:12:11]     ✓ Uploaded: numpy-1.26.0-cp311-cp311-win_amd64.whl
[16:12:19]     ✓ Uploaded: numpy-1.26.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:12:31]     ✓ Uploaded: numpy-1.26.0-cp312-cp312-macosx_10_9_x86_64.whl
[16:12:39]     ✓ Uploaded: numpy-1.26.0-cp312-cp312-macosx_11_0_arm64.whl
[16:12:51]     ✓ Uploaded: numpy-1.26.0-cp312-cp312-win_amd64.whl
[16:12:51]   [22/79] numpy==2.0.0
[16:13:06]     ✓ Uploaded: numpy-2.0.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:13:16]     ✓ Uploaded: numpy-2.0.0-cp39-cp39-macosx_10_9_x86_64.whl
[16:13:28]     ✓ Uploaded: numpy-2.0.0-cp39-cp39-macosx_11_0_arm64.whl
[16:13:40]     ✓ Uploaded: numpy-2.0.0-cp39-cp39-win_amd64.whl
[16:13:52]     ✓ Uploaded: numpy-2.0.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:14:05]     ✓ Uploaded: numpy-2.0.0-cp310-cp310-macosx_10_9_x86_64.whl
[16:14:21]     ✓ Uploaded: numpy-2.0.0-cp310-cp310-macosx_11_0_arm64.whl
[16:14:29]     ✓ Uploaded: numpy-2.0.0-cp310-cp310-win_amd64.whl
[16:14:37]     ✓ Uploaded: numpy-2.0.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:14:51]     ✓ Uploaded: numpy-2.0.0-cp311-cp311-macosx_10_9_x86_64.whl
[16:15:03]     ✓ Uploaded: numpy-2.0.0-cp311-cp311-macosx_11_0_arm64.whl
[16:15:10]     ✓ Uploaded: numpy-2.0.0-cp311-cp311-win_amd64.whl
[16:15:23]     ✓ Uploaded: numpy-2.0.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:15:38]     ✓ Uploaded: numpy-2.0.0-cp312-cp312-macosx_10_9_x86_64.whl
[16:15:49]     ✓ Uploaded: numpy-2.0.0-cp312-cp312-macosx_11_0_arm64.whl
[16:16:00]     ✓ Uploaded: numpy-2.0.0-cp312-cp312-win_amd64.whl
[16:16:00] 📦 scipy (4 versions)
[16:16:00]   [23/79] scipy==1.11.0
[16:16:17]     ✓ Uploaded: scipy-1.11.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:16:37]     ✓ Uploaded: scipy-1.11.0-cp39-cp39-macosx_10_9_x86_64.whl
[16:18:17]     ✓ Uploaded: scipy-1.11.0-cp39-cp39-win_amd64.whl
[16:18:35]     ✓ Uploaded: scipy-1.11.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:18:51]     ✓ Uploaded: scipy-1.11.0-cp310-cp310-macosx_10_9_x86_64.whl
[16:19:43]     ✓ Uploaded: scipy-1.11.0-cp310-cp310-win_amd64.whl
[16:20:01]     ✓ Uploaded: scipy-1.11.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:20:20]     ✓ Uploaded: scipy-1.11.0-cp311-cp311-macosx_10_9_x86_64.whl
[16:21:17]     ✓ Uploaded: scipy-1.11.0-cp311-cp311-win_amd64.whl
[16:23:39]   [24/79] scipy==1.12.0
[16:24:01]     ✓ Uploaded: scipy-1.12.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:24:21]     ✓ Uploaded: scipy-1.12.0-cp39-cp39-macosx_10_9_x86_64.whl
[16:25:17]     ✓ Uploaded: scipy-1.12.0-cp39-cp39-win_amd64.whl
[16:25:33]     ✓ Uploaded: scipy-1.12.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:25:53]     ✓ Uploaded: scipy-1.12.0-cp310-cp310-macosx_10_9_x86_64.whl
[16:26:45]     ✓ Uploaded: scipy-1.12.0-cp310-cp310-win_amd64.whl
[16:27:05]     ✓ Uploaded: scipy-1.12.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:27:24]     ✓ Uploaded: scipy-1.12.0-cp311-cp311-macosx_10_9_x86_64.whl
[16:28:37]     ✓ Uploaded: scipy-1.12.0-cp311-cp311-win_amd64.whl
[16:28:53]     ✓ Uploaded: scipy-1.12.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:29:11]     ✓ Uploaded: scipy-1.12.0-cp312-cp312-macosx_10_9_x86_64.whl
[16:30:00]     ✓ Uploaded: scipy-1.12.0-cp312-cp312-win_amd64.whl
[16:30:00]   [25/79] scipy==1.13.0
[16:30:18]     ✓ Uploaded: scipy-1.13.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:30:39]     ✓ Uploaded: scipy-1.13.0-cp39-cp39-macosx_10_9_x86_64.whl
[16:31:39]     ✓ Uploaded: scipy-1.13.0-cp39-cp39-win_amd64.whl
[16:31:54]     ✓ Uploaded: scipy-1.13.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:32:08]     ✓ Uploaded: scipy-1.13.0-cp310-cp310-macosx_10_9_x86_64.whl
[16:32:56]     ✓ Uploaded: scipy-1.13.0-cp310-cp310-win_amd64.whl
[16:33:13]     ✓ Uploaded: scipy-1.13.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:33:34]     ✓ Uploaded: scipy-1.13.0-cp311-cp311-macosx_10_9_x86_64.whl
[16:34:55]     ✓ Uploaded: scipy-1.13.0-cp311-cp311-win_amd64.whl
[16:35:12]     ✓ Uploaded: scipy-1.13.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:35:29]     ✓ Uploaded: scipy-1.13.0-cp312-cp312-macosx_10_9_x86_64.whl
[16:36:20]     ✓ Uploaded: scipy-1.13.0-cp312-cp312-win_amd64.whl
[16:36:20]   [26/79] scipy==1.14.0
[16:36:41]     ✓ Uploaded: scipy-1.14.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:36:54]     ✓ Uploaded: scipy-1.14.0-cp310-cp310-macosx_10_9_x86_64.whl
[16:38:02]     ✓ Uploaded: scipy-1.14.0-cp310-cp310-win_amd64.whl
[16:38:22]     ✓ Uploaded: scipy-1.14.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:38:42]     ✓ Uploaded: scipy-1.14.0-cp311-cp311-macosx_10_9_x86_64.whl
[16:40:02]     ✓ Uploaded: scipy-1.14.0-cp311-cp311-win_amd64.whl
[16:40:14]     ✓ Uploaded: scipy-1.14.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:40:29]     ✓ Uploaded: scipy-1.14.0-cp312-cp312-macosx_10_9_x86_64.whl
[16:41:13]     ✓ Uploaded: scipy-1.14.0-cp312-cp312-win_amd64.whl
[16:41:13] 📦 pandas (3 versions)
[16:41:13]   [27/79] pandas==2.0.0
[16:41:26]     ✓ Uploaded: pandas-2.0.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:41:37]     ✓ Uploaded: pandas-2.0.0-cp39-cp39-macosx_10_9_x86_64.whl
[16:41:49]     ✓ Uploaded: pandas-2.0.0-cp39-cp39-macosx_11_0_arm64.whl
[16:41:58]     ✓ Uploaded: pandas-2.0.0-cp39-cp39-win_amd64.whl
[16:42:10]     ✓ Uploaded: pandas-2.0.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:42:18]     ✓ Uploaded: pandas-2.0.0-cp310-cp310-macosx_10_9_x86_64.whl
[16:42:32]     ✓ Uploaded: pandas-2.0.0-cp310-cp310-macosx_11_0_arm64.whl
[16:42:46]     ✓ Uploaded: pandas-2.0.0-cp310-cp310-win_amd64.whl
[16:42:56]     ✓ Uploaded: pandas-2.0.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:43:08]     ✓ Uploaded: pandas-2.0.0-cp311-cp311-macosx_10_9_x86_64.whl
[16:43:19]     ✓ Uploaded: pandas-2.0.0-cp311-cp311-macosx_11_0_arm64.whl
[16:43:29]     ✓ Uploaded: pandas-2.0.0-cp311-cp311-win_amd64.whl
[16:47:05]   [28/79] pandas==2.1.0
[16:47:18]     ✓ Uploaded: pandas-2.1.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:47:30]     ✓ Uploaded: pandas-2.1.0-cp39-cp39-macosx_10_9_x86_64.whl
[16:47:40]     ✓ Uploaded: pandas-2.1.0-cp39-cp39-macosx_11_0_arm64.whl
[16:47:53]     ✓ Uploaded: pandas-2.1.0-cp39-cp39-win_amd64.whl
[16:48:03]     ✓ Uploaded: pandas-2.1.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:48:15]     ✓ Uploaded: pandas-2.1.0-cp310-cp310-macosx_10_9_x86_64.whl
[16:48:27]     ✓ Uploaded: pandas-2.1.0-cp310-cp310-macosx_11_0_arm64.whl
[16:48:36]     ✓ Uploaded: pandas-2.1.0-cp310-cp310-win_amd64.whl
[16:48:47]     ✓ Uploaded: pandas-2.1.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:48:55]     ✓ Uploaded: pandas-2.1.0-cp311-cp311-macosx_10_9_x86_64.whl
[16:49:06]     ✓ Uploaded: pandas-2.1.0-cp311-cp311-macosx_11_0_arm64.whl
[16:49:13]     ✓ Uploaded: pandas-2.1.0-cp311-cp311-win_amd64.whl
[16:51:08]   [29/79] pandas==2.2.0
[16:51:21]     ✓ Uploaded: pandas-2.2.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:51:32]     ✓ Uploaded: pandas-2.2.0-cp39-cp39-macosx_10_9_x86_64.whl
[16:51:43]     ✓ Uploaded: pandas-2.2.0-cp39-cp39-macosx_11_0_arm64.whl
[16:51:52]     ✓ Uploaded: pandas-2.2.0-cp39-cp39-win_amd64.whl
[16:52:02]     ✓ Uploaded: pandas-2.2.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:52:13]     ✓ Uploaded: pandas-2.2.0-cp310-cp310-macosx_10_9_x86_64.whl
[16:52:22]     ✓ Uploaded: pandas-2.2.0-cp310-cp310-macosx_11_0_arm64.whl
[16:52:33]     ✓ Uploaded: pandas-2.2.0-cp310-cp310-win_amd64.whl
[16:52:43]     ✓ Uploaded: pandas-2.2.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:52:55]     ✓ Uploaded: pandas-2.2.0-cp311-cp311-macosx_10_9_x86_64.whl
[16:53:06]     ✓ Uploaded: pandas-2.2.0-cp311-cp311-macosx_11_0_arm64.whl
[16:53:16]     ✓ Uploaded: pandas-2.2.0-cp311-cp311-win_amd64.whl
[16:53:28]     ✓ Uploaded: pandas-2.2.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:53:39]     ✓ Uploaded: pandas-2.2.0-cp312-cp312-macosx_10_9_x86_64.whl
[16:53:49]     ✓ Uploaded: pandas-2.2.0-cp312-cp312-macosx_11_0_arm64.whl
[16:53:59]     ✓ Uploaded: pandas-2.2.0-cp312-cp312-win_amd64.whl
[16:53:59] 📦 matplotlib (3 versions)
[16:53:59]   [30/79] matplotlib==3.7.0
[16:54:13]     ✓ Uploaded: matplotlib-3.7.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:54:34]     ✓ Uploaded: matplotlib-3.7.0-cp39-cp39-macosx_11_0_arm64.whl
[16:54:40]     ✓ Uploaded: matplotlib-3.7.0-cp39-cp39-win_amd64.whl
[16:54:50]     ✓ Uploaded: matplotlib-3.7.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:55:07]     ✓ Uploaded: matplotlib-3.7.0-cp310-cp310-macosx_11_0_arm64.whl
[16:55:15]     ✓ Uploaded: matplotlib-3.7.0-cp310-cp310-win_amd64.whl
[16:55:28]     ✓ Uploaded: matplotlib-3.7.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:55:45]     ✓ Uploaded: matplotlib-3.7.0-cp311-cp311-macosx_11_0_arm64.whl
[16:55:53]     ✓ Uploaded: matplotlib-3.7.0-cp311-cp311-win_amd64.whl
[16:56:24]   [31/79] matplotlib==3.8.0
[16:56:38]     ✓ Uploaded: matplotlib-3.8.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:57:00]     ✓ Uploaded: matplotlib-3.8.0-cp39-cp39-macosx_11_0_arm64.whl
[16:57:09]     ✓ Uploaded: matplotlib-3.8.0-cp39-cp39-win_amd64.whl
[16:57:20]     ✓ Uploaded: matplotlib-3.8.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:57:36]     ✓ Uploaded: matplotlib-3.8.0-cp310-cp310-macosx_11_0_arm64.whl
[16:57:45]     ✓ Uploaded: matplotlib-3.8.0-cp310-cp310-win_amd64.whl
[16:57:52]     ✓ Uploaded: matplotlib-3.8.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:58:11]     ✓ Uploaded: matplotlib-3.8.0-cp311-cp311-macosx_11_0_arm64.whl
[16:58:19]     ✓ Uploaded: matplotlib-3.8.0-cp311-cp311-win_amd64.whl
[16:58:31]     ✓ Uploaded: matplotlib-3.8.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[16:58:47]     ✓ Uploaded: matplotlib-3.8.0-cp312-cp312-macosx_11_0_arm64.whl
[16:58:56]     ✓ Uploaded: matplotlib-3.8.0-cp312-cp312-win_amd64.whl
[16:58:56]   [32/79] matplotlib==3.9.0
[16:59:06]     ✓ Uploaded: matplotlib-3.9.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:00:39]     ✓ Uploaded: matplotlib-3.9.0-cp39-cp39-macosx_11_0_arm64.whl
[17:00:50]     ✓ Uploaded: matplotlib-3.9.0-cp39-cp39-win_amd64.whl
[17:00:58]     ✓ Uploaded: matplotlib-3.9.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:02:09]     ✓ Uploaded: matplotlib-3.9.0-cp310-cp310-macosx_11_0_arm64.whl
[17:02:17]     ✓ Uploaded: matplotlib-3.9.0-cp310-cp310-win_amd64.whl
[17:02:25]     ✓ Uploaded: matplotlib-3.9.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:03:08]     ✓ Uploaded: matplotlib-3.9.0-cp311-cp311-macosx_11_0_arm64.whl
[17:03:17]     ✓ Uploaded: matplotlib-3.9.0-cp311-cp311-win_amd64.whl
[17:03:25]     ✓ Uploaded: matplotlib-3.9.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:04:31]     ✓ Uploaded: matplotlib-3.9.0-cp312-cp312-macosx_11_0_arm64.whl
[17:04:40]     ✓ Uploaded: matplotlib-3.9.0-cp312-cp312-win_amd64.whl
[17:04:40] 📦 scikit-learn (3 versions)
[17:04:40]   [33/79] scikit-learn==1.3.0
[17:04:52]     ✓ Uploaded: scikit_learn-1.3.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:05:03]     ✓ Uploaded: scikit_learn-1.3.0-cp39-cp39-macosx_10_9_x86_64.whl
[17:05:50]     ✓ Uploaded: scikit_learn-1.3.0-cp39-cp39-win_amd64.whl
[17:06:00]     ✓ Uploaded: scikit_learn-1.3.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:06:09]     ✓ Uploaded: scikit_learn-1.3.0-cp310-cp310-macosx_10_9_x86_64.whl
[17:06:53]     ✓ Uploaded: scikit_learn-1.3.0-cp310-cp310-win_amd64.whl
[17:07:06]     ✓ Uploaded: scikit_learn-1.3.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:07:17]     ✓ Uploaded: scikit_learn-1.3.0-cp311-cp311-macosx_10_9_x86_64.whl
[17:08:29]     ✓ Uploaded: scikit_learn-1.3.0-cp311-cp311-win_amd64.whl
[17:10:51]   [34/79] scikit-learn==1.4.0
[17:11:07]     ✓ Uploaded: scikit_learn-1.4.0-1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:11:18]     ✓ Uploaded: scikit_learn-1.4.0-1-cp39-cp39-macosx_10_9_x86_64.whl
[17:12:36]     ✓ Uploaded: scikit_learn-1.4.0-1-cp39-cp39-win_amd64.whl
[17:12:47]     ✓ Uploaded: scikit_learn-1.4.0-1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:12:57]     ✓ Uploaded: scikit_learn-1.4.0-1-cp310-cp310-macosx_10_9_x86_64.whl
[17:14:39]     ✓ Uploaded: scikit_learn-1.4.0-1-cp310-cp310-win_amd64.whl
[17:14:47]     ✓ Uploaded: scikit_learn-1.4.0-1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:14:57]     ✓ Uploaded: scikit_learn-1.4.0-1-cp311-cp311-macosx_10_9_x86_64.whl
[17:16:14]     ✓ Uploaded: scikit_learn-1.4.0-1-cp311-cp311-win_amd64.whl
[17:16:24]     ✓ Uploaded: scikit_learn-1.4.0-1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:16:35]     ✓ Uploaded: scikit_learn-1.4.0-1-cp312-cp312-macosx_10_9_x86_64.whl
[17:17:53]     ✓ Uploaded: scikit_learn-1.4.0-1-cp312-cp312-win_amd64.whl
[17:17:53]   [35/79] scikit-learn==1.5.0
[17:18:06]     ✓ Uploaded: scikit_learn-1.5.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:18:20]     ✓ Uploaded: scikit_learn-1.5.0-cp39-cp39-macosx_10_9_x86_64.whl
[17:21:43]     ✓ Uploaded: scikit_learn-1.5.0-cp39-cp39-win_amd64.whl
[17:21:53]     ✓ Uploaded: scikit_learn-1.5.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:22:05]     ✓ Uploaded: scikit_learn-1.5.0-cp310-cp310-macosx_10_9_x86_64.whl
[17:24:53]     ✓ Uploaded: scikit_learn-1.5.0-cp310-cp310-win_amd64.whl
[17:25:04]     ✓ Uploaded: scikit_learn-1.5.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:25:16]     ✓ Uploaded: scikit_learn-1.5.0-cp311-cp311-macosx_10_9_x86_64.whl
[17:28:06]     ✓ Uploaded: scikit_learn-1.5.0-cp311-cp311-win_amd64.whl
[17:28:13]     ✓ Uploaded: scikit_learn-1.5.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:28:26]     ✓ Uploaded: scikit_learn-1.5.0-cp312-cp312-macosx_10_9_x86_64.whl
[17:31:09]     ✓ Uploaded: scikit_learn-1.5.0-cp312-cp312-win_amd64.whl
[17:31:09] 📦 opencv-python (2 versions)
[17:31:09]   [36/79] opencv-python==4.9.0.80
[17:31:37]     ✓ Uploaded: opencv_python-4.9.0.80-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:32:18]     ✓ Uploaded: opencv_python-4.9.0.80-cp37-abi3-macosx_11_0_arm64.whl
[17:32:35]     ✓ Uploaded: opencv_python-4.9.0.80-cp37-abi3-win_amd64.whl
[17:32:40]     ✓ Uploaded: opencv_python-4.9.0.80-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:32:53]     ✓ Uploaded: opencv_python-4.9.0.80-cp37-abi3-macosx_11_0_arm64.whl
[17:32:57]     ✓ Uploaded: opencv_python-4.9.0.80-cp37-abi3-win_amd64.whl
[17:33:02]     ✓ Uploaded: opencv_python-4.9.0.80-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:33:15]     ✓ Uploaded: opencv_python-4.9.0.80-cp37-abi3-macosx_11_0_arm64.whl
[17:33:19]     ✓ Uploaded: opencv_python-4.9.0.80-cp37-abi3-win_amd64.whl
[17:33:23]     ✓ Uploaded: opencv_python-4.9.0.80-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:33:36]     ✓ Uploaded: opencv_python-4.9.0.80-cp37-abi3-macosx_11_0_arm64.whl
[17:33:40]     ✓ Uploaded: opencv_python-4.9.0.80-cp37-abi3-win_amd64.whl
[17:33:40]   [37/79] opencv-python==4.10.0.84
[17:34:03]     ✓ Uploaded: opencv_python-4.10.0.84-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:34:46]     ✓ Uploaded: opencv_python-4.10.0.84-cp37-abi3-macosx_11_0_arm64.whl
[17:35:04]     ✓ Uploaded: opencv_python-4.10.0.84-cp37-abi3-win_amd64.whl
[17:35:08]     ✓ Uploaded: opencv_python-4.10.0.84-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:35:21]     ✓ Uploaded: opencv_python-4.10.0.84-cp37-abi3-macosx_11_0_arm64.whl
[17:35:25]     ✓ Uploaded: opencv_python-4.10.0.84-cp37-abi3-win_amd64.whl
[17:35:29]     ✓ Uploaded: opencv_python-4.10.0.84-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:35:43]     ✓ Uploaded: opencv_python-4.10.0.84-cp37-abi3-macosx_11_0_arm64.whl
[17:35:47]     ✓ Uploaded: opencv_python-4.10.0.84-cp37-abi3-win_amd64.whl
[17:35:51]     ✓ Uploaded: opencv_python-4.10.0.84-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:36:04]     ✓ Uploaded: opencv_python-4.10.0.84-cp37-abi3-macosx_11_0_arm64.whl
[17:36:08]     ✓ Uploaded: opencv_python-4.10.0.84-cp37-abi3-win_amd64.whl
[17:36:08] 📦 Pillow (3 versions)
[17:36:08]   [38/79] Pillow==10.2.0
[17:36:19]     ✓ Uploaded: pillow-10.2.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:36:31]     ✓ Uploaded: pillow-10.2.0-cp39-cp39-macosx_11_0_arm64.whl
[17:36:37]     ✓ Uploaded: pillow-10.2.0-cp39-cp39-win_amd64.whl
[17:36:44]     ✓ Uploaded: pillow-10.2.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:36:53]     ✓ Uploaded: pillow-10.2.0-cp310-cp310-macosx_11_0_arm64.whl
[17:37:01]     ✓ Uploaded: pillow-10.2.0-cp310-cp310-win_amd64.whl
[17:37:08]     ✓ Uploaded: pillow-10.2.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:37:16]     ✓ Uploaded: pillow-10.2.0-cp311-cp311-macosx_11_0_arm64.whl
[17:37:24]     ✓ Uploaded: pillow-10.2.0-cp311-cp311-win_amd64.whl
[17:37:33]     ✓ Uploaded: pillow-10.2.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:37:43]     ✓ Uploaded: pillow-10.2.0-cp312-cp312-macosx_11_0_arm64.whl
[17:37:51]     ✓ Uploaded: pillow-10.2.0-cp312-cp312-win_amd64.whl
[17:37:51]   [39/79] Pillow==10.3.0
[17:38:01]     ✓ Uploaded: pillow-10.3.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:38:22]     ✓ Uploaded: pillow-10.3.0-cp39-cp39-macosx_11_0_arm64.whl
[17:38:28]     ✓ Uploaded: pillow-10.3.0-cp39-cp39-win_amd64.whl
[17:38:36]     ✓ Uploaded: pillow-10.3.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:38:48]     ✓ Uploaded: pillow-10.3.0-cp310-cp310-macosx_11_0_arm64.whl
[17:38:55]     ✓ Uploaded: pillow-10.3.0-cp310-cp310-win_amd64.whl
[17:39:02]     ✓ Uploaded: pillow-10.3.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:39:14]     ✓ Uploaded: pillow-10.3.0-cp311-cp311-macosx_11_0_arm64.whl
[17:39:20]     ✓ Uploaded: pillow-10.3.0-cp311-cp311-win_amd64.whl
[17:39:27]     ✓ Uploaded: pillow-10.3.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:39:37]     ✓ Uploaded: pillow-10.3.0-cp312-cp312-macosx_11_0_arm64.whl
[17:39:44]     ✓ Uploaded: pillow-10.3.0-cp312-cp312-win_amd64.whl
[17:39:44]   [40/79] Pillow==10.4.0
[17:39:54]     ✓ Uploaded: pillow-10.4.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:40:09]     ✓ Uploaded: pillow-10.4.0-cp39-cp39-macosx_11_0_arm64.whl
[17:40:16]     ✓ Uploaded: pillow-10.4.0-cp39-cp39-win_amd64.whl
[17:40:24]     ✓ Uploaded: pillow-10.4.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:40:35]     ✓ Uploaded: pillow-10.4.0-cp310-cp310-macosx_11_0_arm64.whl
[17:40:41]     ✓ Uploaded: pillow-10.4.0-cp310-cp310-win_amd64.whl
[17:40:48]     ✓ Uploaded: pillow-10.4.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:40:59]     ✓ Uploaded: pillow-10.4.0-cp311-cp311-macosx_11_0_arm64.whl
[17:41:06]     ✓ Uploaded: pillow-10.4.0-cp311-cp311-win_amd64.whl
[17:41:16]     ✓ Uploaded: pillow-10.4.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:41:26]     ✓ Uploaded: pillow-10.4.0-cp312-cp312-macosx_11_0_arm64.whl
[17:41:32]     ✓ Uploaded: pillow-10.4.0-cp312-cp312-win_amd64.whl
[17:41:32] 📦 transformers (3 versions)
[17:41:32]   [41/79] transformers==4.38.0
[17:41:44]     ✓ Uploaded: transformers-4.38.0-py3-none-any.whl
[17:41:47]     ✓ Uploaded: transformers-4.38.0-py3-none-any.whl
[17:41:51]     ✓ Uploaded: transformers-4.38.0-py3-none-any.whl
[17:41:54]     ✓ Uploaded: transformers-4.38.0-py3-none-any.whl
[17:41:58]     ✓ Uploaded: transformers-4.38.0-py3-none-any.whl
[17:42:03]     ✓ Uploaded: transformers-4.38.0-py3-none-any.whl
[17:42:08]     ✓ Uploaded: transformers-4.38.0-py3-none-any.whl
[17:42:12]     ✓ Uploaded: transformers-4.38.0-py3-none-any.whl
[17:42:16]     ✓ Uploaded: transformers-4.38.0-py3-none-any.whl
[17:42:20]     ✓ Uploaded: transformers-4.38.0-py3-none-any.whl
[17:42:25]     ✓ Uploaded: transformers-4.38.0-py3-none-any.whl
[17:42:30]     ✓ Uploaded: transformers-4.38.0-py3-none-any.whl
[17:42:38]     ✓ Uploaded: transformers-4.38.0-py3-none-any.whl
[17:42:42]     ✓ Uploaded: transformers-4.38.0-py3-none-any.whl
[17:42:48]     ✓ Uploaded: transformers-4.38.0-py3-none-any.whl
[17:42:52]     ✓ Uploaded: transformers-4.38.0-py3-none-any.whl
[17:42:52]   [42/79] transformers==4.39.0
[17:43:03]     ✓ Uploaded: transformers-4.39.0-py3-none-any.whl
[17:43:07]     ✓ Uploaded: transformers-4.39.0-py3-none-any.whl
[17:43:12]     ✓ Uploaded: transformers-4.39.0-py3-none-any.whl
[17:43:16]     ✓ Uploaded: transformers-4.39.0-py3-none-any.whl
[17:43:21]     ✓ Uploaded: transformers-4.39.0-py3-none-any.whl
[17:43:26]     ✓ Uploaded: transformers-4.39.0-py3-none-any.whl
[17:43:30]     ✓ Uploaded: transformers-4.39.0-py3-none-any.whl
[17:43:34]     ✓ Uploaded: transformers-4.39.0-py3-none-any.whl
[17:43:39]     ✓ Uploaded: transformers-4.39.0-py3-none-any.whl
[17:43:43]     ✓ Uploaded: transformers-4.39.0-py3-none-any.whl
[17:43:47]     ✓ Uploaded: transformers-4.39.0-py3-none-any.whl
[17:43:52]     ✓ Uploaded: transformers-4.39.0-py3-none-any.whl
[17:43:57]     ✓ Uploaded: transformers-4.39.0-py3-none-any.whl
[17:44:01]     ✓ Uploaded: transformers-4.39.0-py3-none-any.whl
[17:44:06]     ✓ Uploaded: transformers-4.39.0-py3-none-any.whl
[17:44:10]     ✓ Uploaded: transformers-4.39.0-py3-none-any.whl
[17:44:10]   [43/79] transformers==4.40.0
[17:44:22]     ✓ Uploaded: transformers-4.40.0-py3-none-any.whl
[17:44:26]     ✓ Uploaded: transformers-4.40.0-py3-none-any.whl
[17:44:29]     ✓ Uploaded: transformers-4.40.0-py3-none-any.whl
[17:44:33]     ✓ Uploaded: transformers-4.40.0-py3-none-any.whl
[17:44:37]     ✓ Uploaded: transformers-4.40.0-py3-none-any.whl
[17:44:42]     ✓ Uploaded: transformers-4.40.0-py3-none-any.whl
[17:44:49]     ✓ Uploaded: transformers-4.40.0-py3-none-any.whl
[17:44:53]     ✓ Uploaded: transformers-4.40.0-py3-none-any.whl
[17:44:58]     ✓ Uploaded: transformers-4.40.0-py3-none-any.whl
[17:45:02]     ✓ Uploaded: transformers-4.40.0-py3-none-any.whl
[17:45:06]     ✓ Uploaded: transformers-4.40.0-py3-none-any.whl
[17:45:11]     ✓ Uploaded: transformers-4.40.0-py3-none-any.whl
[17:45:16]     ✓ Uploaded: transformers-4.40.0-py3-none-any.whl
[17:45:21]     ✓ Uploaded: transformers-4.40.0-py3-none-any.whl
[17:45:25]     ✓ Uploaded: transformers-4.40.0-py3-none-any.whl
[17:45:30]     ✓ Uploaded: transformers-4.40.0-py3-none-any.whl
[17:45:30] 📦 tokenizers (2 versions)
[17:45:30]   [44/79] tokenizers==0.19.0
[17:45:41]     ✓ Uploaded: tokenizers-0.19.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:46:01]     ✓ Uploaded: tokenizers-0.19.0-cp39-cp39-macosx_11_0_arm64.whl
[17:46:08]     ✓ Uploaded: tokenizers-0.19.0-cp39-none-win_amd64.whl
[17:46:14]     ✓ Uploaded: tokenizers-0.19.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:46:27]     ✓ Uploaded: tokenizers-0.19.0-cp310-cp310-macosx_11_0_arm64.whl
[17:46:35]     ✓ Uploaded: tokenizers-0.19.0-cp310-none-win_amd64.whl
[17:46:42]     ✓ Uploaded: tokenizers-0.19.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:46:55]     ✓ Uploaded: tokenizers-0.19.0-cp311-cp311-macosx_11_0_arm64.whl
[17:47:02]     ✓ Uploaded: tokenizers-0.19.0-cp311-none-win_amd64.whl
[17:47:13]     ✓ Uploaded: tokenizers-0.19.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:47:26]     ✓ Uploaded: tokenizers-0.19.0-cp312-cp312-macosx_11_0_arm64.whl
[17:47:34]     ✓ Uploaded: tokenizers-0.19.0-cp312-none-win_amd64.whl
[17:47:34]   [45/79] tokenizers==0.20.0
[17:47:45]     ✓ Uploaded: tokenizers-0.20.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:47:59]     ✓ Uploaded: tokenizers-0.20.0-cp39-cp39-macosx_11_0_arm64.whl
[17:48:06]     ✓ Uploaded: tokenizers-0.20.0-cp39-none-win_amd64.whl
[17:48:13]     ✓ Uploaded: tokenizers-0.20.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:48:25]     ✓ Uploaded: tokenizers-0.20.0-cp310-cp310-macosx_11_0_arm64.whl
[17:48:31]     ✓ Uploaded: tokenizers-0.20.0-cp310-none-win_amd64.whl
[17:48:37]     ✓ Uploaded: tokenizers-0.20.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:48:50]     ✓ Uploaded: tokenizers-0.20.0-cp311-cp311-macosx_11_0_arm64.whl
[17:48:58]     ✓ Uploaded: tokenizers-0.20.0-cp311-none-win_amd64.whl
[17:49:05]     ✓ Uploaded: tokenizers-0.20.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:49:18]     ✓ Uploaded: tokenizers-0.20.0-cp312-cp312-macosx_11_0_arm64.whl
[17:49:25]     ✓ Uploaded: tokenizers-0.20.0-cp312-none-win_amd64.whl
[17:49:25] 📦 datasets (3 versions)
[17:49:25]   [46/79] datasets==2.18.0
[17:49:33]     ✓ Uploaded: datasets-2.18.0-py3-none-any.whl
[17:49:36]     ✓ Uploaded: datasets-2.18.0-py3-none-any.whl
[17:49:39]     ✓ Uploaded: datasets-2.18.0-py3-none-any.whl
[17:49:43]     ✓ Uploaded: datasets-2.18.0-py3-none-any.whl
[17:49:46]     ✓ Uploaded: datasets-2.18.0-py3-none-any.whl
[17:49:50]     ✓ Uploaded: datasets-2.18.0-py3-none-any.whl
[17:49:54]     ✓ Uploaded: datasets-2.18.0-py3-none-any.whl
[17:49:59]     ✓ Uploaded: datasets-2.18.0-py3-none-any.whl
[17:50:03]     ✓ Uploaded: datasets-2.18.0-py3-none-any.whl
[17:50:08]     ✓ Uploaded: datasets-2.18.0-py3-none-any.whl
[17:50:13]     ✓ Uploaded: datasets-2.18.0-py3-none-any.whl
[17:50:18]     ✓ Uploaded: datasets-2.18.0-py3-none-any.whl
[17:50:23]     ✓ Uploaded: datasets-2.18.0-py3-none-any.whl
[17:50:27]     ✓ Uploaded: datasets-2.18.0-py3-none-any.whl
[17:50:31]     ✓ Uploaded: datasets-2.18.0-py3-none-any.whl
[17:50:36]     ✓ Uploaded: datasets-2.18.0-py3-none-any.whl
[17:50:36]   [47/79] datasets==2.19.0
[17:50:43]     ✓ Uploaded: datasets-2.19.0-py3-none-any.whl
[17:50:47]     ✓ Uploaded: datasets-2.19.0-py3-none-any.whl
[17:50:50]     ✓ Uploaded: datasets-2.19.0-py3-none-any.whl
[17:50:53]     ✓ Uploaded: datasets-2.19.0-py3-none-any.whl
[17:50:58]     ✓ Uploaded: datasets-2.19.0-py3-none-any.whl
[17:51:02]     ✓ Uploaded: datasets-2.19.0-py3-none-any.whl
[17:51:06]     ✓ Uploaded: datasets-2.19.0-py3-none-any.whl
[17:51:10]     ✓ Uploaded: datasets-2.19.0-py3-none-any.whl
[17:51:14]     ✓ Uploaded: datasets-2.19.0-py3-none-any.whl
[17:51:20]     ✓ Uploaded: datasets-2.19.0-py3-none-any.whl
[17:51:24]     ✓ Uploaded: datasets-2.19.0-py3-none-any.whl
[17:51:29]     ✓ Uploaded: datasets-2.19.0-py3-none-any.whl
[17:51:33]     ✓ Uploaded: datasets-2.19.0-py3-none-any.whl
[17:51:37]     ✓ Uploaded: datasets-2.19.0-py3-none-any.whl
[17:51:42]     ✓ Uploaded: datasets-2.19.0-py3-none-any.whl
[17:51:46]     ✓ Uploaded: datasets-2.19.0-py3-none-any.whl
[17:51:46]   [48/79] datasets==2.20.0
[17:51:53]     ✓ Uploaded: datasets-2.20.0-py3-none-any.whl
[17:51:57]     ✓ Uploaded: datasets-2.20.0-py3-none-any.whl
[17:52:00]     ✓ Uploaded: datasets-2.20.0-py3-none-any.whl
[17:52:04]     ✓ Uploaded: datasets-2.20.0-py3-none-any.whl
[17:52:07]     ✓ Uploaded: datasets-2.20.0-py3-none-any.whl
[17:52:10]     ✓ Uploaded: datasets-2.20.0-py3-none-any.whl
[17:52:14]     ✓ Uploaded: datasets-2.20.0-py3-none-any.whl
[17:52:17]     ✓ Uploaded: datasets-2.20.0-py3-none-any.whl
[17:52:20]     ✓ Uploaded: datasets-2.20.0-py3-none-any.whl
[17:52:24]     ✓ Uploaded: datasets-2.20.0-py3-none-any.whl
[17:52:28]     ✓ Uploaded: datasets-2.20.0-py3-none-any.whl
[17:52:31]     ✓ Uploaded: datasets-2.20.0-py3-none-any.whl
[17:52:35]     ✓ Uploaded: datasets-2.20.0-py3-none-any.whl
[17:52:38]     ✓ Uploaded: datasets-2.20.0-py3-none-any.whl
[17:52:42]     ✓ Uploaded: datasets-2.20.0-py3-none-any.whl
[17:52:45]     ✓ Uploaded: datasets-2.20.0-py3-none-any.whl
[17:52:45] 📦 accelerate (2 versions)
[17:52:45]   [49/79] accelerate==0.27.0
[17:52:53]     ✓ Uploaded: accelerate-0.27.0-py3-none-any.whl
[17:52:57]     ✓ Uploaded: accelerate-0.27.0-py3-none-any.whl
[17:53:01]     ✓ Uploaded: accelerate-0.27.0-py3-none-any.whl
[17:53:09]     ✓ Uploaded: accelerate-0.27.0-py3-none-any.whl
[17:53:15]     ✓ Uploaded: accelerate-0.27.0-py3-none-any.whl
[17:53:19]     ✓ Uploaded: accelerate-0.27.0-py3-none-any.whl
[17:53:22]     ✓ Uploaded: accelerate-0.27.0-py3-none-any.whl
[17:53:27]     ✓ Uploaded: accelerate-0.27.0-py3-none-any.whl
[17:53:31]     ✓ Uploaded: accelerate-0.27.0-py3-none-any.whl
[17:53:35]     ✓ Uploaded: accelerate-0.27.0-py3-none-any.whl
[17:53:42]     ✓ Uploaded: accelerate-0.27.0-py3-none-any.whl
[17:53:46]     ✓ Uploaded: accelerate-0.27.0-py3-none-any.whl
[17:53:50]     ✓ Uploaded: accelerate-0.27.0-py3-none-any.whl
[17:53:55]     ✓ Uploaded: accelerate-0.27.0-py3-none-any.whl
[17:54:00]     ✓ Uploaded: accelerate-0.27.0-py3-none-any.whl
[17:54:05]     ✓ Uploaded: accelerate-0.27.0-py3-none-any.whl
[17:54:05]   [50/79] accelerate==0.28.0
[17:54:12]     ✓ Uploaded: accelerate-0.28.0-py3-none-any.whl
[17:54:16]     ✓ Uploaded: accelerate-0.28.0-py3-none-any.whl
[17:54:20]     ✓ Uploaded: accelerate-0.28.0-py3-none-any.whl
[17:54:23]     ✓ Uploaded: accelerate-0.28.0-py3-none-any.whl
[17:54:27]     ✓ Uploaded: accelerate-0.28.0-py3-none-any.whl
[17:54:32]     ✓ Uploaded: accelerate-0.28.0-py3-none-any.whl
[17:54:36]     ✓ Uploaded: accelerate-0.28.0-py3-none-any.whl
[17:54:40]     ✓ Uploaded: accelerate-0.28.0-py3-none-any.whl
[17:54:44]     ✓ Uploaded: accelerate-0.28.0-py3-none-any.whl
[17:54:49]     ✓ Uploaded: accelerate-0.28.0-py3-none-any.whl
[17:54:53]     ✓ Uploaded: accelerate-0.28.0-py3-none-any.whl
[17:54:57]     ✓ Uploaded: accelerate-0.28.0-py3-none-any.whl
[17:55:01]     ✓ Uploaded: accelerate-0.28.0-py3-none-any.whl
[17:55:06]     ✓ Uploaded: accelerate-0.28.0-py3-none-any.whl
[17:55:10]     ✓ Uploaded: accelerate-0.28.0-py3-none-any.whl
[17:55:15]     ✓ Uploaded: accelerate-0.28.0-py3-none-any.whl
[17:55:15] 📦 safetensors (2 versions)
[17:55:15]   [51/79] safetensors==0.4.2
[17:55:24]     ✓ Uploaded: safetensors-0.4.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:55:36]     ✓ Uploaded: safetensors-0.4.2-cp39-cp39-macosx_11_0_arm64.whl
[17:55:41]     ✓ Uploaded: safetensors-0.4.2-cp39-none-win_amd64.whl
[17:55:47]     ✓ Uploaded: safetensors-0.4.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:55:57]     ✓ Uploaded: safetensors-0.4.2-cp310-cp310-macosx_11_0_arm64.whl
[17:56:02]     ✓ Uploaded: safetensors-0.4.2-cp310-none-win_amd64.whl
[17:56:07]     ✓ Uploaded: safetensors-0.4.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:56:18]     ✓ Uploaded: safetensors-0.4.2-cp311-cp311-macosx_11_0_arm64.whl
[17:56:23]     ✓ Uploaded: safetensors-0.4.2-cp311-none-win_amd64.whl
[17:56:29]     ✓ Uploaded: safetensors-0.4.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:56:40]     ✓ Uploaded: safetensors-0.4.2-cp312-cp312-macosx_11_0_arm64.whl
[17:56:45]     ✓ Uploaded: safetensors-0.4.2-cp312-none-win_amd64.whl
[17:56:45]   [52/79] safetensors==0.4.3
[17:56:54]     ✓ Uploaded: safetensors-0.4.3-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:57:05]     ✓ Uploaded: safetensors-0.4.3-cp39-cp39-macosx_11_0_arm64.whl
[17:57:10]     ✓ Uploaded: safetensors-0.4.3-cp39-none-win_amd64.whl
[17:57:16]     ✓ Uploaded: safetensors-0.4.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:57:28]     ✓ Uploaded: safetensors-0.4.3-cp310-cp310-macosx_11_0_arm64.whl
[17:57:33]     ✓ Uploaded: safetensors-0.4.3-cp310-none-win_amd64.whl
[17:57:38]     ✓ Uploaded: safetensors-0.4.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:57:50]     ✓ Uploaded: safetensors-0.4.3-cp311-cp311-macosx_11_0_arm64.whl
[17:57:55]     ✓ Uploaded: safetensors-0.4.3-cp311-none-win_amd64.whl
[17:58:01]     ✓ Uploaded: safetensors-0.4.3-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[17:58:11]     ✓ Uploaded: safetensors-0.4.3-cp312-cp312-macosx_11_0_arm64.whl
[17:58:16]     ✓ Uploaded: safetensors-0.4.3-cp312-none-win_amd64.whl
[17:58:16] 📦 tensorboard (3 versions)
[17:58:16]   [53/79] tensorboard==2.15.0
[17:58:26]     ✓ Uploaded: tensorboard-2.15.0-py3-none-any.whl
[17:58:30]     ✓ Uploaded: tensorboard-2.15.0-py3-none-any.whl
[17:58:35]     ✓ Uploaded: tensorboard-2.15.0-py3-none-any.whl
[17:58:39]     ✓ Uploaded: tensorboard-2.15.0-py3-none-any.whl
[17:58:45]     ✓ Uploaded: tensorboard-2.15.0-py3-none-any.whl
[17:58:50]     ✓ Uploaded: tensorboard-2.15.0-py3-none-any.whl
[17:58:54]     ✓ Uploaded: tensorboard-2.15.0-py3-none-any.whl
[17:58:59]     ✓ Uploaded: tensorboard-2.15.0-py3-none-any.whl
[17:59:03]     ✓ Uploaded: tensorboard-2.15.0-py3-none-any.whl
[17:59:08]     ✓ Uploaded: tensorboard-2.15.0-py3-none-any.whl
[17:59:12]     ✓ Uploaded: tensorboard-2.15.0-py3-none-any.whl
[17:59:17]     ✓ Uploaded: tensorboard-2.15.0-py3-none-any.whl
[17:59:21]     ✓ Uploaded: tensorboard-2.15.0-py3-none-any.whl
[17:59:26]     ✓ Uploaded: tensorboard-2.15.0-py3-none-any.whl
[17:59:30]     ✓ Uploaded: tensorboard-2.15.0-py3-none-any.whl
[17:59:34]     ✓ Uploaded: tensorboard-2.15.0-py3-none-any.whl
[17:59:34]   [54/79] tensorboard==2.16.0
[17:59:44]     ✓ Uploaded: tensorboard-2.16.0-py3-none-any.whl
[17:59:48]     ✓ Uploaded: tensorboard-2.16.0-py3-none-any.whl
[17:59:52]     ✓ Uploaded: tensorboard-2.16.0-py3-none-any.whl
[17:59:56]     ✓ Uploaded: tensorboard-2.16.0-py3-none-any.whl
[18:00:00]     ✓ Uploaded: tensorboard-2.16.0-py3-none-any.whl
[18:00:05]     ✓ Uploaded: tensorboard-2.16.0-py3-none-any.whl
[18:00:10]     ✓ Uploaded: tensorboard-2.16.0-py3-none-any.whl
[18:00:14]     ✓ Uploaded: tensorboard-2.16.0-py3-none-any.whl
[18:00:36]     ✓ Uploaded: tensorboard-2.16.0-py3-none-any.whl
[18:00:42]     ✓ Uploaded: tensorboard-2.16.0-py3-none-any.whl
[18:00:48]     ✓ Uploaded: tensorboard-2.16.0-py3-none-any.whl
[18:00:54]     ✓ Uploaded: tensorboard-2.16.0-py3-none-any.whl
[18:00:58]     ✓ Uploaded: tensorboard-2.16.0-py3-none-any.whl
[18:01:04]     ✓ Uploaded: tensorboard-2.16.0-py3-none-any.whl
[18:01:08]     ✓ Uploaded: tensorboard-2.16.0-py3-none-any.whl
[18:01:13]     ✓ Uploaded: tensorboard-2.16.0-py3-none-any.whl
[18:01:13]   [55/79] tensorboard==2.17.0
[18:01:57]     ✓ Uploaded: tensorboard-2.17.0-py3-none-any.whl
[18:02:01]     ✓ Uploaded: tensorboard-2.17.0-py3-none-any.whl
[18:02:05]     ✓ Uploaded: tensorboard-2.17.0-py3-none-any.whl
[18:02:08]     ✓ Uploaded: tensorboard-2.17.0-py3-none-any.whl
[18:02:13]     ✓ Uploaded: tensorboard-2.17.0-py3-none-any.whl
[18:02:17]     ✓ Uploaded: tensorboard-2.17.0-py3-none-any.whl
[18:02:22]     ✓ Uploaded: tensorboard-2.17.0-py3-none-any.whl
[18:02:27]     ✓ Uploaded: tensorboard-2.17.0-py3-none-any.whl
[18:02:31]     ✓ Uploaded: tensorboard-2.17.0-py3-none-any.whl
[18:02:36]     ✓ Uploaded: tensorboard-2.17.0-py3-none-any.whl
[18:02:43]     ✓ Uploaded: tensorboard-2.17.0-py3-none-any.whl
[18:02:47]     ✓ Uploaded: tensorboard-2.17.0-py3-none-any.whl
[18:02:53]     ✓ Uploaded: tensorboard-2.17.0-py3-none-any.whl
[18:02:59]     ✓ Uploaded: tensorboard-2.17.0-py3-none-any.whl
[18:03:03]     ✓ Uploaded: tensorboard-2.17.0-py3-none-any.whl
[18:03:08]     ✓ Uploaded: tensorboard-2.17.0-py3-none-any.whl
[18:03:08] 📦 lightning (3 versions)
[18:03:08]   [56/79] lightning==2.2.0
[18:03:17]     ✓ Uploaded: lightning-2.2.0-py3-none-any.whl
[18:03:23]     ✓ Uploaded: lightning-2.2.0-py3-none-any.whl
[18:03:29]     ✓ Uploaded: lightning-2.2.0-py3-none-any.whl
[18:03:34]     ✓ Uploaded: lightning-2.2.0-py3-none-any.whl
[18:03:38]     ✓ Uploaded: lightning-2.2.0-py3-none-any.whl
[18:03:42]     ✓ Uploaded: lightning-2.2.0-py3-none-any.whl
[18:03:47]     ✓ Uploaded: lightning-2.2.0-py3-none-any.whl
[18:03:53]     ✓ Uploaded: lightning-2.2.0-py3-none-any.whl
[18:03:58]     ✓ Uploaded: lightning-2.2.0-py3-none-any.whl
[18:04:02]     ✓ Uploaded: lightning-2.2.0-py3-none-any.whl
[18:04:07]     ✓ Uploaded: lightning-2.2.0-py3-none-any.whl
[18:04:11]     ✓ Uploaded: lightning-2.2.0-py3-none-any.whl
[18:04:18]     ✓ Uploaded: lightning-2.2.0-py3-none-any.whl
[18:04:23]     ✓ Uploaded: lightning-2.2.0-py3-none-any.whl
[18:04:27]     ✓ Uploaded: lightning-2.2.0-py3-none-any.whl
[18:04:33]     ✓ Uploaded: lightning-2.2.0-py3-none-any.whl
[18:04:33]   [57/79] lightning==2.3.0
[18:04:41]     ✓ Uploaded: lightning-2.3.0-py3-none-any.whl
[18:04:45]     ✓ Uploaded: lightning-2.3.0-py3-none-any.whl
[18:04:49]     ✓ Uploaded: lightning-2.3.0-py3-none-any.whl
[18:04:53]     ✓ Uploaded: lightning-2.3.0-py3-none-any.whl
[18:04:57]     ✓ Uploaded: lightning-2.3.0-py3-none-any.whl
[18:05:02]     ✓ Uploaded: lightning-2.3.0-py3-none-any.whl
[18:05:06]     ✓ Uploaded: lightning-2.3.0-py3-none-any.whl
[18:05:11]     ✓ Uploaded: lightning-2.3.0-py3-none-any.whl
[18:05:19]     ✓ Uploaded: lightning-2.3.0-py3-none-any.whl
[18:05:25]     ✓ Uploaded: lightning-2.3.0-py3-none-any.whl
[18:05:30]     ✓ Uploaded: lightning-2.3.0-py3-none-any.whl
[18:05:35]     ✓ Uploaded: lightning-2.3.0-py3-none-any.whl
[18:05:40]     ✓ Uploaded: lightning-2.3.0-py3-none-any.whl
[18:05:45]     ✓ Uploaded: lightning-2.3.0-py3-none-any.whl
[18:05:49]     ✓ Uploaded: lightning-2.3.0-py3-none-any.whl
[18:05:54]     ✓ Uploaded: lightning-2.3.0-py3-none-any.whl
[18:05:54]   [58/79] lightning==2.4.0
[18:06:01]     ✓ Uploaded: lightning-2.4.0-py3-none-any.whl
[18:06:04]     ✓ Uploaded: lightning-2.4.0-py3-none-any.whl
[18:06:08]     ✓ Uploaded: lightning-2.4.0-py3-none-any.whl
[18:06:11]     ✓ Uploaded: lightning-2.4.0-py3-none-any.whl
[18:06:15]     ✓ Uploaded: lightning-2.4.0-py3-none-any.whl
[18:06:21]     ✓ Uploaded: lightning-2.4.0-py3-none-any.whl
[18:06:25]     ✓ Uploaded: lightning-2.4.0-py3-none-any.whl
[18:06:30]     ✓ Uploaded: lightning-2.4.0-py3-none-any.whl
[18:06:34]     ✓ Uploaded: lightning-2.4.0-py3-none-any.whl
[18:06:39]     ✓ Uploaded: lightning-2.4.0-py3-none-any.whl
[18:06:44]     ✓ Uploaded: lightning-2.4.0-py3-none-any.whl
[18:06:49]     ✓ Uploaded: lightning-2.4.0-py3-none-any.whl
[18:06:53]     ✓ Uploaded: lightning-2.4.0-py3-none-any.whl
[18:06:58]     ✓ Uploaded: lightning-2.4.0-py3-none-any.whl
[18:07:05]     ✓ Uploaded: lightning-2.4.0-py3-none-any.whl
[18:07:09]     ✓ Uploaded: lightning-2.4.0-py3-none-any.whl
[18:07:09] 📦 wandb (2 versions)
[18:07:09]   [59/79] wandb==0.17.0
[18:07:20]     ✓ Uploaded: wandb-0.17.0-py3-none-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:07:30]     ✓ Uploaded: wandb-0.17.0-py3-none-macosx_10_9_x86_64.whl
[18:07:40]     ✓ Uploaded: wandb-0.17.0-py3-none-macosx_11_0_arm64.whl
[18:07:53]     ✓ Uploaded: wandb-0.17.0-py3-none-win_amd64.whl
[18:08:01]     ✓ Uploaded: wandb-0.17.0-py3-none-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:08:06]     ✓ Uploaded: wandb-0.17.0-py3-none-macosx_10_9_x86_64.whl
[18:08:11]     ✓ Uploaded: wandb-0.17.0-py3-none-macosx_11_0_arm64.whl
[18:08:15]     ✓ Uploaded: wandb-0.17.0-py3-none-win_amd64.whl
[18:08:21]     ✓ Uploaded: wandb-0.17.0-py3-none-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:08:25]     ✓ Uploaded: wandb-0.17.0-py3-none-macosx_10_9_x86_64.whl
[18:08:30]     ✓ Uploaded: wandb-0.17.0-py3-none-macosx_11_0_arm64.whl
[18:08:33]     ✓ Uploaded: wandb-0.17.0-py3-none-win_amd64.whl
[18:08:38]     ✓ Uploaded: wandb-0.17.0-py3-none-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:08:42]     ✓ Uploaded: wandb-0.17.0-py3-none-macosx_10_9_x86_64.whl
[18:08:46]     ✓ Uploaded: wandb-0.17.0-py3-none-macosx_11_0_arm64.whl
[18:08:49]     ✓ Uploaded: wandb-0.17.0-py3-none-win_amd64.whl
[18:08:49]   [60/79] wandb==0.18.0
[18:09:01]     ✓ Uploaded: wandb-0.18.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:09:10]     ✓ Uploaded: wandb-0.18.0-py3-none-any.whl
[18:09:19]     ✓ Uploaded: wandb-0.18.0-py3-none-macosx_11_0_arm64.whl
[18:09:28]     ✓ Uploaded: wandb-0.18.0-py3-none-win_amd64.whl
[18:09:33]     ✓ Uploaded: wandb-0.18.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:09:38]     ✓ Uploaded: wandb-0.18.0-py3-none-any.whl
[18:09:42]     ✓ Uploaded: wandb-0.18.0-py3-none-macosx_11_0_arm64.whl
[18:09:47]     ✓ Uploaded: wandb-0.18.0-py3-none-win_amd64.whl
[18:09:52]     ✓ Uploaded: wandb-0.18.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:09:56]     ✓ Uploaded: wandb-0.18.0-py3-none-any.whl
[18:10:01]     ✓ Uploaded: wandb-0.18.0-py3-none-macosx_11_0_arm64.whl
[18:10:05]     ✓ Uploaded: wandb-0.18.0-py3-none-win_amd64.whl
[18:10:10]     ✓ Uploaded: wandb-0.18.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:10:15]     ✓ Uploaded: wandb-0.18.0-py3-none-any.whl
[18:10:19]     ✓ Uploaded: wandb-0.18.0-py3-none-macosx_11_0_arm64.whl
[18:10:24]     ✓ Uploaded: wandb-0.18.0-py3-none-win_amd64.whl
[18:10:24] 📦 optuna (2 versions)
[18:10:24]   [61/79] optuna==3.6.0
[18:10:32]     ✓ Uploaded: optuna-3.6.0-py3-none-any.whl
[18:10:35]     ✓ Uploaded: optuna-3.6.0-py3-none-any.whl
[18:10:39]     ✓ Uploaded: optuna-3.6.0-py3-none-any.whl
[18:10:44]     ✓ Uploaded: optuna-3.6.0-py3-none-any.whl
[18:10:48]     ✓ Uploaded: optuna-3.6.0-py3-none-any.whl
[18:10:53]     ✓ Uploaded: optuna-3.6.0-py3-none-any.whl
[18:10:57]     ✓ Uploaded: optuna-3.6.0-py3-none-any.whl
[18:11:01]     ✓ Uploaded: optuna-3.6.0-py3-none-any.whl
[18:11:06]     ✓ Uploaded: optuna-3.6.0-py3-none-any.whl
[18:11:11]     ✓ Uploaded: optuna-3.6.0-py3-none-any.whl
[18:11:16]     ✓ Uploaded: optuna-3.6.0-py3-none-any.whl
[18:11:21]     ✓ Uploaded: optuna-3.6.0-py3-none-any.whl
[18:11:25]     ✓ Uploaded: optuna-3.6.0-py3-none-any.whl
[18:11:30]     ✓ Uploaded: optuna-3.6.0-py3-none-any.whl
[18:11:34]     ✓ Uploaded: optuna-3.6.0-py3-none-any.whl
[18:11:38]     ✓ Uploaded: optuna-3.6.0-py3-none-any.whl
[18:11:38]   [62/79] optuna==4.0.0
[18:11:46]     ✓ Uploaded: optuna-4.0.0-py3-none-any.whl
[18:11:50]     ✓ Uploaded: optuna-4.0.0-py3-none-any.whl
[18:11:53]     ✓ Uploaded: optuna-4.0.0-py3-none-any.whl
[18:11:57]     ✓ Uploaded: optuna-4.0.0-py3-none-any.whl
[18:12:02]     ✓ Uploaded: optuna-4.0.0-py3-none-any.whl
[18:12:06]     ✓ Uploaded: optuna-4.0.0-py3-none-any.whl
[18:12:11]     ✓ Uploaded: optuna-4.0.0-py3-none-any.whl
[18:12:15]     ✓ Uploaded: optuna-4.0.0-py3-none-any.whl
[18:12:19]     ✓ Uploaded: optuna-4.0.0-py3-none-any.whl
[18:12:23]     ✓ Uploaded: optuna-4.0.0-py3-none-any.whl
[18:12:27]     ✓ Uploaded: optuna-4.0.0-py3-none-any.whl
[18:12:33]     ✓ Uploaded: optuna-4.0.0-py3-none-any.whl
[18:12:37]     ✓ Uploaded: optuna-4.0.0-py3-none-any.whl
[18:12:42]     ✓ Uploaded: optuna-4.0.0-py3-none-any.whl
[18:12:46]     ✓ Uploaded: optuna-4.0.0-py3-none-any.whl
[18:12:52]     ✓ Uploaded: optuna-4.0.0-py3-none-any.whl
[18:12:52] 📦 jupyterlab (2 versions)
[18:12:52]   [63/79] jupyterlab==4.1.0
[18:13:06]     ✓ Uploaded: jupyterlab-4.1.0-py3-none-any.whl
[18:13:11]     ✓ Uploaded: jupyterlab-4.1.0-py3-none-any.whl
[18:13:15]     ✓ Uploaded: jupyterlab-4.1.0-py3-none-any.whl
[18:13:18]     ✓ Uploaded: jupyterlab-4.1.0-py3-none-any.whl
[18:13:21]     ✓ Uploaded: jupyterlab-4.1.0-py3-none-any.whl
[18:13:25]     ✓ Uploaded: jupyterlab-4.1.0-py3-none-any.whl
[18:13:28]     ✓ Uploaded: jupyterlab-4.1.0-py3-none-any.whl
[18:13:32]     ✓ Uploaded: jupyterlab-4.1.0-py3-none-any.whl
[18:13:35]     ✓ Uploaded: jupyterlab-4.1.0-py3-none-any.whl
[18:13:39]     ✓ Uploaded: jupyterlab-4.1.0-py3-none-any.whl
[18:13:42]     ✓ Uploaded: jupyterlab-4.1.0-py3-none-any.whl
[18:13:46]     ✓ Uploaded: jupyterlab-4.1.0-py3-none-any.whl
[18:13:49]     ✓ Uploaded: jupyterlab-4.1.0-py3-none-any.whl
[18:13:53]     ✓ Uploaded: jupyterlab-4.1.0-py3-none-any.whl
[18:13:56]     ✓ Uploaded: jupyterlab-4.1.0-py3-none-any.whl
[18:14:00]     ✓ Uploaded: jupyterlab-4.1.0-py3-none-any.whl
[18:14:00]   [64/79] jupyterlab==4.2.0
[18:14:13]     ✓ Uploaded: jupyterlab-4.2.0-py3-none-any.whl
[18:14:17]     ✓ Uploaded: jupyterlab-4.2.0-py3-none-any.whl
[18:14:24]     ✓ Uploaded: jupyterlab-4.2.0-py3-none-any.whl
[18:14:29]     ✓ Uploaded: jupyterlab-4.2.0-py3-none-any.whl
[18:14:34]     ✓ Uploaded: jupyterlab-4.2.0-py3-none-any.whl
[18:14:39]     ✓ Uploaded: jupyterlab-4.2.0-py3-none-any.whl
[18:14:44]     ✓ Uploaded: jupyterlab-4.2.0-py3-none-any.whl
[18:14:49]     ✓ Uploaded: jupyterlab-4.2.0-py3-none-any.whl
[18:14:54]     ✓ Uploaded: jupyterlab-4.2.0-py3-none-any.whl
[18:14:58]     ✓ Uploaded: jupyterlab-4.2.0-py3-none-any.whl
[18:15:03]     ✓ Uploaded: jupyterlab-4.2.0-py3-none-any.whl
[18:15:07]     ✓ Uploaded: jupyterlab-4.2.0-py3-none-any.whl
[18:15:12]     ✓ Uploaded: jupyterlab-4.2.0-py3-none-any.whl
[18:15:17]     ✓ Uploaded: jupyterlab-4.2.0-py3-none-any.whl
[18:15:22]     ✓ Uploaded: jupyterlab-4.2.0-py3-none-any.whl
[18:15:26]     ✓ Uploaded: jupyterlab-4.2.0-py3-none-any.whl
[18:15:26] 📦 notebook (2 versions)
[18:15:26]   [65/79] notebook==7.1.0
[18:15:38]     ✓ Uploaded: notebook-7.1.0-py3-none-any.whl
[18:15:42]     ✓ Uploaded: notebook-7.1.0-py3-none-any.whl
[18:15:46]     ✓ Uploaded: notebook-7.1.0-py3-none-any.whl
[18:15:51]     ✓ Uploaded: notebook-7.1.0-py3-none-any.whl
[18:15:56]     ✓ Uploaded: notebook-7.1.0-py3-none-any.whl
[18:16:01]     ✓ Uploaded: notebook-7.1.0-py3-none-any.whl
[18:16:06]     ✓ Uploaded: notebook-7.1.0-py3-none-any.whl
[18:16:10]     ✓ Uploaded: notebook-7.1.0-py3-none-any.whl
[18:16:15]     ✓ Uploaded: notebook-7.1.0-py3-none-any.whl
[18:16:20]     ✓ Uploaded: notebook-7.1.0-py3-none-any.whl
[18:16:24]     ✓ Uploaded: notebook-7.1.0-py3-none-any.whl
[18:16:29]     ✓ Uploaded: notebook-7.1.0-py3-none-any.whl
[18:16:34]     ✓ Uploaded: notebook-7.1.0-py3-none-any.whl
[18:16:38]     ✓ Uploaded: notebook-7.1.0-py3-none-any.whl
[18:16:43]     ✓ Uploaded: notebook-7.1.0-py3-none-any.whl
[18:16:48]     ✓ Uploaded: notebook-7.1.0-py3-none-any.whl
[18:16:48]   [66/79] notebook==7.2.0
[18:16:59]     ✓ Uploaded: notebook-7.2.0-py3-none-any.whl
[18:17:03]     ✓ Uploaded: notebook-7.2.0-py3-none-any.whl
[18:17:07]     ✓ Uploaded: notebook-7.2.0-py3-none-any.whl
[18:17:10]     ✓ Uploaded: notebook-7.2.0-py3-none-any.whl
[18:17:15]     ✓ Uploaded: notebook-7.2.0-py3-none-any.whl
[18:17:20]     ✓ Uploaded: notebook-7.2.0-py3-none-any.whl
[18:17:25]     ✓ Uploaded: notebook-7.2.0-py3-none-any.whl
[18:17:30]     ✓ Uploaded: notebook-7.2.0-py3-none-any.whl
[18:17:34]     ✓ Uploaded: notebook-7.2.0-py3-none-any.whl
[18:17:38]     ✓ Uploaded: notebook-7.2.0-py3-none-any.whl
[18:17:43]     ✓ Uploaded: notebook-7.2.0-py3-none-any.whl
[18:17:48]     ✓ Uploaded: notebook-7.2.0-py3-none-any.whl
[18:17:53]     ✓ Uploaded: notebook-7.2.0-py3-none-any.whl
[18:17:57]     ✓ Uploaded: notebook-7.2.0-py3-none-any.whl
[18:18:02]     ✓ Uploaded: notebook-7.2.0-py3-none-any.whl
[18:18:07]     ✓ Uploaded: notebook-7.2.0-py3-none-any.whl
[18:18:07] 📦 ipykernel (2 versions)
[18:18:07]   [67/79] ipykernel==6.28.0
[18:18:15]     ✓ Uploaded: ipykernel-6.28.0-py3-none-any.whl
[18:18:18]     ✓ Uploaded: ipykernel-6.28.0-py3-none-any.whl
[18:18:22]     ✓ Uploaded: ipykernel-6.28.0-py3-none-any.whl
[18:18:26]     ✓ Uploaded: ipykernel-6.28.0-py3-none-any.whl
[18:18:29]     ✓ Uploaded: ipykernel-6.28.0-py3-none-any.whl
[18:18:33]     ✓ Uploaded: ipykernel-6.28.0-py3-none-any.whl
[18:18:37]     ✓ Uploaded: ipykernel-6.28.0-py3-none-any.whl
[18:18:41]     ✓ Uploaded: ipykernel-6.28.0-py3-none-any.whl
[18:18:46]     ✓ Uploaded: ipykernel-6.28.0-py3-none-any.whl
[18:18:49]     ✓ Uploaded: ipykernel-6.28.0-py3-none-any.whl
[18:18:53]     ✓ Uploaded: ipykernel-6.28.0-py3-none-any.whl
[18:18:57]     ✓ Uploaded: ipykernel-6.28.0-py3-none-any.whl
[18:19:01]     ✓ Uploaded: ipykernel-6.28.0-py3-none-any.whl
[18:19:05]     ✓ Uploaded: ipykernel-6.28.0-py3-none-any.whl
[18:19:09]     ✓ Uploaded: ipykernel-6.28.0-py3-none-any.whl
[18:19:12]     ✓ Uploaded: ipykernel-6.28.0-py3-none-any.whl
[18:19:12]   [68/79] ipykernel==6.29.0
[18:19:19]     ✓ Uploaded: ipykernel-6.29.0-py3-none-any.whl
[18:19:23]     ✓ Uploaded: ipykernel-6.29.0-py3-none-any.whl
[18:19:27]     ✓ Uploaded: ipykernel-6.29.0-py3-none-any.whl
[18:19:31]     ✓ Uploaded: ipykernel-6.29.0-py3-none-any.whl
[18:19:35]     ✓ Uploaded: ipykernel-6.29.0-py3-none-any.whl
[18:19:42]     ✓ Uploaded: ipykernel-6.29.0-py3-none-any.whl
[18:19:46]     ✓ Uploaded: ipykernel-6.29.0-py3-none-any.whl
[18:19:49]     ✓ Uploaded: ipykernel-6.29.0-py3-none-any.whl
[18:19:53]     ✓ Uploaded: ipykernel-6.29.0-py3-none-any.whl
[18:19:57]     ✓ Uploaded: ipykernel-6.29.0-py3-none-any.whl
[18:20:02]     ✓ Uploaded: ipykernel-6.29.0-py3-none-any.whl
[18:20:07]     ✓ Uploaded: ipykernel-6.29.0-py3-none-any.whl
[18:20:10]     ✓ Uploaded: ipykernel-6.29.0-py3-none-any.whl
[18:20:15]     ✓ Uploaded: ipykernel-6.29.0-py3-none-any.whl
[18:20:18]     ✓ Uploaded: ipykernel-6.29.0-py3-none-any.whl
[18:20:22]     ✓ Uploaded: ipykernel-6.29.0-py3-none-any.whl
[18:20:22] 📦 tqdm (1 versions)
[18:20:22]   [69/79] tqdm==4.66.0
[18:20:30]     ✓ Uploaded: tqdm-4.66.0-py3-none-any.whl
[18:20:34]     ✓ Uploaded: tqdm-4.66.0-py3-none-any.whl
[18:20:38]     ✓ Uploaded: tqdm-4.66.0-py3-none-any.whl
[18:20:42]     ✓ Uploaded: tqdm-4.66.0-py3-none-any.whl
[18:20:46]     ✓ Uploaded: tqdm-4.66.0-py3-none-any.whl
[18:20:51]     ✓ Uploaded: tqdm-4.66.0-py3-none-any.whl
[18:20:54]     ✓ Uploaded: tqdm-4.66.0-py3-none-any.whl
[18:20:58]     ✓ Uploaded: tqdm-4.66.0-py3-none-any.whl
[18:21:02]     ✓ Uploaded: tqdm-4.66.0-py3-none-any.whl
[18:21:05]     ✓ Uploaded: tqdm-4.66.0-py3-none-any.whl
[18:21:09]     ✓ Uploaded: tqdm-4.66.0-py3-none-any.whl
[18:21:14]     ✓ Uploaded: tqdm-4.66.0-py3-none-any.whl
[18:21:17]     ✓ Uploaded: tqdm-4.66.0-py3-none-any.whl
[18:21:21]     ✓ Uploaded: tqdm-4.66.0-py3-none-any.whl
[18:21:25]     ✓ Uploaded: tqdm-4.66.0-py3-none-any.whl
[18:21:29]     ✓ Uploaded: tqdm-4.66.0-py3-none-any.whl
[18:21:29] 📦 pyyaml (1 versions)
[18:21:29]   [70/79] pyyaml==6.0.1
[18:21:37]     ✓ Uploaded: PyYAML-6.0.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:21:42]     ✓ Uploaded: PyYAML-6.0.1-cp39-cp39-macosx_10_9_x86_64.whl
[18:21:47]     ✓ Uploaded: PyYAML-6.0.1-cp39-cp39-macosx_11_0_arm64.whl
[18:21:52]     ✓ Uploaded: PyYAML-6.0.1-cp39-cp39-win_amd64.whl
[18:21:57]     ✓ Uploaded: PyYAML-6.0.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:22:03]     ✓ Uploaded: PyYAML-6.0.1-cp310-cp310-macosx_10_9_x86_64.whl
[18:22:09]     ✓ Uploaded: PyYAML-6.0.1-cp310-cp310-macosx_11_0_arm64.whl
[18:22:14]     ✓ Uploaded: PyYAML-6.0.1-cp310-cp310-win_amd64.whl
[18:22:19]     ✓ Uploaded: PyYAML-6.0.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:22:24]     ✓ Uploaded: PyYAML-6.0.1-cp311-cp311-macosx_10_9_x86_64.whl
[18:22:30]     ✓ Uploaded: PyYAML-6.0.1-cp311-cp311-macosx_11_0_arm64.whl
[18:22:35]     ✓ Uploaded: PyYAML-6.0.1-cp311-cp311-win_amd64.whl
[18:22:41]     ✓ Uploaded: PyYAML-6.0.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:22:46]     ✓ Uploaded: PyYAML-6.0.1-cp312-cp312-macosx_10_9_x86_64.whl
[18:22:52]     ✓ Uploaded: PyYAML-6.0.1-cp312-cp312-macosx_11_0_arm64.whl
[18:22:56]     ✓ Uploaded: PyYAML-6.0.1-cp312-cp312-win_amd64.whl
[18:22:56] 📦 rich (1 versions)
[18:22:56]   [71/79] rich==13.7.0
[18:23:04]     ✓ Uploaded: rich-13.7.0-py3-none-any.whl
[18:23:07]     ✓ Uploaded: rich-13.7.0-py3-none-any.whl
[18:23:11]     ✓ Uploaded: rich-13.7.0-py3-none-any.whl
[18:23:15]     ✓ Uploaded: rich-13.7.0-py3-none-any.whl
[18:23:20]     ✓ Uploaded: rich-13.7.0-py3-none-any.whl
[18:23:25]     ✓ Uploaded: rich-13.7.0-py3-none-any.whl
[18:23:29]     ✓ Uploaded: rich-13.7.0-py3-none-any.whl
[18:23:33]     ✓ Uploaded: rich-13.7.0-py3-none-any.whl
[18:23:38]     ✓ Uploaded: rich-13.7.0-py3-none-any.whl
[18:23:43]     ✓ Uploaded: rich-13.7.0-py3-none-any.whl
[18:23:47]     ✓ Uploaded: rich-13.7.0-py3-none-any.whl
[18:23:51]     ✓ Uploaded: rich-13.7.0-py3-none-any.whl
[18:23:56]     ✓ Uploaded: rich-13.7.0-py3-none-any.whl
[18:24:00]     ✓ Uploaded: rich-13.7.0-py3-none-any.whl
[18:24:04]     ✓ Uploaded: rich-13.7.0-py3-none-any.whl
[18:24:08]     ✓ Uploaded: rich-13.7.0-py3-none-any.whl
[18:24:08] 📦 h5py (2 versions)
[18:24:08]   [72/79] h5py==3.10.0
[18:24:18]     ✓ Uploaded: h5py-3.10.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:24:26]     ✓ Uploaded: h5py-3.10.0-cp39-cp39-macosx_10_9_x86_64.whl
[18:24:32]     ✓ Uploaded: h5py-3.10.0-cp39-cp39-macosx_11_0_arm64.whl
[18:24:38]     ✓ Uploaded: h5py-3.10.0-cp39-cp39-win_amd64.whl
[18:24:46]     ✓ Uploaded: h5py-3.10.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:24:53]     ✓ Uploaded: h5py-3.10.0-cp310-cp310-macosx_10_9_x86_64.whl
[18:25:00]     ✓ Uploaded: h5py-3.10.0-cp310-cp310-macosx_11_0_arm64.whl
[18:25:06]     ✓ Uploaded: h5py-3.10.0-cp310-cp310-win_amd64.whl
[18:25:13]     ✓ Uploaded: h5py-3.10.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:25:22]     ✓ Uploaded: h5py-3.10.0-cp311-cp311-macosx_10_9_x86_64.whl
[18:25:29]     ✓ Uploaded: h5py-3.10.0-cp311-cp311-macosx_11_0_arm64.whl
[18:25:35]     ✓ Uploaded: h5py-3.10.0-cp311-cp311-win_amd64.whl
[18:25:42]     ✓ Uploaded: h5py-3.10.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:25:51]     ✓ Uploaded: h5py-3.10.0-cp312-cp312-macosx_10_9_x86_64.whl
[18:25:58]     ✓ Uploaded: h5py-3.10.0-cp312-cp312-macosx_11_0_arm64.whl
[18:26:05]     ✓ Uploaded: h5py-3.10.0-cp312-cp312-win_amd64.whl
[18:26:05]   [73/79] h5py==3.11.0
[18:26:16]     ✓ Uploaded: h5py-3.11.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:26:23]     ✓ Uploaded: h5py-3.11.0-cp39-cp39-macosx_10_9_x86_64.whl
[18:26:31]     ✓ Uploaded: h5py-3.11.0-cp39-cp39-macosx_11_0_arm64.whl
[18:26:39]     ✓ Uploaded: h5py-3.11.0-cp39-cp39-win_amd64.whl
[18:26:47]     ✓ Uploaded: h5py-3.11.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:26:54]     ✓ Uploaded: h5py-3.11.0-cp310-cp310-macosx_10_9_x86_64.whl
[18:27:01]     ✓ Uploaded: h5py-3.11.0-cp310-cp310-macosx_11_0_arm64.whl
[18:27:10]     ✓ Uploaded: h5py-3.11.0-cp310-cp310-win_amd64.whl
[18:27:19]     ✓ Uploaded: h5py-3.11.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:27:26]     ✓ Uploaded: h5py-3.11.0-cp311-cp311-macosx_10_9_x86_64.whl
[18:27:33]     ✓ Uploaded: h5py-3.11.0-cp311-cp311-macosx_11_0_arm64.whl
[18:27:40]     ✓ Uploaded: h5py-3.11.0-cp311-cp311-win_amd64.whl
[18:27:48]     ✓ Uploaded: h5py-3.11.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:27:56]     ✓ Uploaded: h5py-3.11.0-cp312-cp312-macosx_10_9_x86_64.whl
[18:28:02]     ✓ Uploaded: h5py-3.11.0-cp312-cp312-macosx_11_0_arm64.whl
[18:28:10]     ✓ Uploaded: h5py-3.11.0-cp312-cp312-win_amd64.whl
[18:28:10] 📦 onnx (2 versions)
[18:28:10]   [74/79] onnx==1.15.0
[18:28:28]     ✓ Uploaded: onnx-1.15.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:28:54]     ✓ Uploaded: onnx-1.15.0-cp39-cp39-macosx_10_12_universal2.whl
[18:29:06]     ✓ Uploaded: onnx-1.15.0-cp39-cp39-win_amd64.whl
[18:29:17]     ✓ Uploaded: onnx-1.15.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:29:39]     ✓ Uploaded: onnx-1.15.0-cp310-cp310-macosx_10_12_universal2.whl
[18:29:52]     ✓ Uploaded: onnx-1.15.0-cp310-cp310-win_amd64.whl
[18:30:12]     ✓ Uploaded: onnx-1.15.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:30:33]     ✓ Uploaded: onnx-1.15.0-cp311-cp311-macosx_10_12_universal2.whl
[18:30:45]     ✓ Uploaded: onnx-1.15.0-cp311-cp311-win_amd64.whl
[18:31:19]   [75/79] onnx==1.16.0
[18:31:37]     ✓ Uploaded: onnx-1.16.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:32:17]     ✓ Uploaded: onnx-1.16.0-cp39-cp39-macosx_10_15_universal2.whl
[18:32:25]     ✓ Uploaded: onnx-1.16.0-cp39-cp39-win_amd64.whl
[18:32:37]     ✓ Uploaded: onnx-1.16.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:33:00]     ✓ Uploaded: onnx-1.16.0-cp310-cp310-macosx_10_15_universal2.whl
[18:33:12]     ✓ Uploaded: onnx-1.16.0-cp310-cp310-win_amd64.whl
[18:33:20]     ✓ Uploaded: onnx-1.16.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:33:41]     ✓ Uploaded: onnx-1.16.0-cp311-cp311-macosx_10_15_universal2.whl
[18:33:52]     ✓ Uploaded: onnx-1.16.0-cp311-cp311-win_amd64.whl
[18:34:00]     ✓ Uploaded: onnx-1.16.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
[18:34:18]     ✓ Uploaded: onnx-1.16.0-cp312-cp312-macosx_10_15_universal2.whl
[18:34:28]     ✓ Uploaded: onnx-1.16.0-cp312-cp312-win_amd64.whl
[18:34:28] 📦 onnxruntime (2 versions)
[18:34:28]   [76/79] onnxruntime==1.17.0
[18:34:46]     ✓ Uploaded: onnxruntime-1.17.0-cp39-cp39-macosx_11_0_universal2.whl
[18:34:56]     ✓ Uploaded: onnxruntime-1.17.0-cp39-cp39-win_amd64.whl
[18:35:05]     ✓ Uploaded: onnxruntime-1.17.0-cp310-cp310-macosx_11_0_universal2.whl
[18:35:14]     ✓ Uploaded: onnxruntime-1.17.0-cp310-cp310-win_amd64.whl
[18:35:28]     ✓ Uploaded: onnxruntime-1.17.0-cp311-cp311-macosx_11_0_universal2.whl
[18:35:37]     ✓ Uploaded: onnxruntime-1.17.0-cp311-cp311-win_amd64.whl
[18:35:52]     ✓ Uploaded: onnxruntime-1.17.0-cp312-cp312-macosx_11_0_universal2.whl
[18:35:58]     ✓ Uploaded: onnxruntime-1.17.0-cp312-cp312-win_amd64.whl
[18:35:58]   [77/79] onnxruntime==1.18.0
[18:36:14]     ✓ Uploaded: onnxruntime-1.18.0-cp39-cp39-macosx_11_0_universal2.whl
[18:36:28]     ✓ Uploaded: onnxruntime-1.18.0-cp39-cp39-win_amd64.whl
[18:36:42]     ✓ Uploaded: onnxruntime-1.18.0-cp310-cp310-macosx_11_0_universal2.whl
[18:36:49]     ✓ Uploaded: onnxruntime-1.18.0-cp310-cp310-win_amd64.whl
[18:37:07]     ✓ Uploaded: onnxruntime-1.18.0-cp311-cp311-macosx_11_0_universal2.whl
[18:37:18]     ✓ Uploaded: onnxruntime-1.18.0-cp311-cp311-win_amd64.whl
[18:37:34]     ✓ Uploaded: onnxruntime-1.18.0-cp312-cp312-macosx_11_0_universal2.whl
[18:37:51]     ✓ Uploaded: onnxruntime-1.18.0-cp312-cp312-win_amd64.whl
[18:37:51] 📦 einops (2 versions)
[18:37:51]   [78/79] einops==0.7.0
[18:37:59]     ✓ Uploaded: einops-0.7.0-py3-none-any.whl
[18:38:03]     ✓ Uploaded: einops-0.7.0-py3-none-any.whl
[18:38:07]     ✓ Uploaded: einops-0.7.0-py3-none-any.whl
[18:38:11]     ✓ Uploaded: einops-0.7.0-py3-none-any.whl
[18:38:15]     ✓ Uploaded: einops-0.7.0-py3-none-any.whl
[18:38:19]     ✓ Uploaded: einops-0.7.0-py3-none-any.whl
[18:38:23]     ✓ Uploaded: einops-0.7.0-py3-none-any.whl
[18:38:26]     ✓ Uploaded: einops-0.7.0-py3-none-any.whl
[18:38:30]     ✓ Uploaded: einops-0.7.0-py3-none-any.whl
[18:38:34]     ✓ Uploaded: einops-0.7.0-py3-none-any.whl
[18:38:38]     ✓ Uploaded: einops-0.7.0-py3-none-any.whl
[18:38:41]     ✓ Uploaded: einops-0.7.0-py3-none-any.whl
[18:38:45]     ✓ Uploaded: einops-0.7.0-py3-none-any.whl
[18:38:49]     ✓ Uploaded: einops-0.7.0-py3-none-any.whl
[18:38:53]     ✓ Uploaded: einops-0.7.0-py3-none-any.whl
[18:38:56]     ✓ Uploaded: einops-0.7.0-py3-none-any.whl
[18:38:56]   [79/79] einops==0.8.0
[18:39:03]     ✓ Uploaded: einops-0.8.0-py3-none-any.whl
[18:39:07]     ✓ Uploaded: einops-0.8.0-py3-none-any.whl
[18:39:11]     ✓ Uploaded: einops-0.8.0-py3-none-any.whl
[18:39:14]     ✓ Uploaded: einops-0.8.0-py3-none-any.whl
[18:39:18]     ✓ Uploaded: einops-0.8.0-py3-none-any.whl
[18:39:22]     ✓ Uploaded: einops-0.8.0-py3-none-any.whl
[18:39:25]     ✓ Uploaded: einops-0.8.0-py3-none-any.whl
[18:39:29]     ✓ Uploaded: einops-0.8.0-py3-none-any.whl
[18:39:32]     ✓ Uploaded: einops-0.8.0-py3-none-any.whl
[18:39:36]     ✓ Uploaded: einops-0.8.0-py3-none-any.whl
[18:39:40]     ✓ Uploaded: einops-0.8.0-py3-none-any.whl
[18:39:44]     ✓ Uploaded: einops-0.8.0-py3-none-any.whl
[18:39:48]     ✓ Uploaded: einops-0.8.0-py3-none-any.whl
[18:39:52]     ✓ Uploaded: einops-0.8.0-py3-none-any.whl
[18:39:56]     ✓ Uploaded: einops-0.8.0-py3-none-any.whl
[18:40:01]     ✓ Uploaded: einops-0.8.0-py3-none-any.whl
[18:40:01] 
[18:40:01] ============================================================
[18:40:01] ✅ Complete! Uploaded 977 files to Google Drive
[18:40:01] ============================================================
[18:40:01] 🧹 Cleaned up temp directory