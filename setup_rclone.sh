#!/bin/bash
# =============================================================================
# rclone Setup Script for Google Drive
# =============================================================================
# This script helps you configure rclone to sync with Google Drive.
# Run this once before using the download script's --sync-to-gdrive option.
# =============================================================================

set -e

echo "🔧 rclone Setup for Google Drive"
echo "================================="
echo ""

# Check if rclone is installed
if ! command -v rclone &> /dev/null; then
    echo "📦 rclone not found. Installing..."
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        if command -v brew &> /dev/null; then
            brew install rclone
        else
            echo "❌ Homebrew not found. Please install rclone manually:"
            echo "   https://rclone.org/downloads/"
            exit 1
        fi
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        curl https://rclone.org/install.sh | sudo bash
    else
        echo "❌ Please install rclone manually:"
        echo "   https://rclone.org/downloads/"
        exit 1
    fi
fi

echo "✅ rclone is installed: $(rclone version | head -1)"
echo ""

# Check if gdrive remote already exists
if rclone listremotes | grep -q "^gdrive:"; then
    echo "✅ 'gdrive' remote already configured."
    echo ""
    echo "Testing connection..."
    if rclone lsd gdrive: --max-depth 1 2>/dev/null; then
        echo "✅ Connection successful!"
    else
        echo "⚠️  Connection test failed. You may need to reconfigure."
        echo "   Run: rclone config delete gdrive"
        echo "   Then run this script again."
    fi
else
    echo "📝 Setting up Google Drive remote..."
    echo ""
    echo "This will open a browser window for Google authentication."
    echo "Please follow the prompts to authorize rclone."
    echo ""
    read -p "Press Enter to continue..."
    
    # Configure gdrive remote
    rclone config create gdrive drive \
        scope=drive \
        --drive-acknowledge-abuse
        
    echo ""
    echo "✅ Google Drive remote 'gdrive' configured!"
fi

echo ""
echo "================================="
echo "🎉 Setup Complete!"
echo "================================="
echo ""
echo "You can now use the download script with Google Drive sync:"
echo ""
echo "  python download_packages.py --output-dir ./ml_packages --sync-to-gdrive"
echo ""
echo "Or manually sync with:"
echo ""
echo "  rclone sync ./ml_packages gdrive:ml_packages --progress"
echo ""
