#!/bin/bash
set -o errexit  # Exit script on error

echo "Updating system and installing dependencies..."
apt-get update && apt-get install -y wget curl unzip

# Install Google Chrome
echo "Installing Google Chrome..."
wget -q -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i /tmp/chrome.deb || apt-get -fy install

# Ensure Chrome is correctly linked
ln -sf /usr/bin/google-chrome-stable /usr/bin/google-chrome
export CHROME_PATH="/usr/bin/google-chrome"

# Install ChromeDriver (Ensure it matches Chrome)
echo "Installing ChromeDriver..."
CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d '.' -f 1)
CHROMEDRIVER_VERSION=$(curl -sS "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION")
wget -q -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip"
unzip /tmp/chromedriver.zip -d /usr/local/bin/
chmod +x /usr/local/bin/chromedriver
export CHROMEDRIVER_PATH="/usr/local/bin/chromedriver"

# Verify installations
if ! command -v google-chrome &> /dev/null
then
    echo "Google Chrome installation failed!"
    exit 1
fi

if ! command -v chromedriver &> /dev/null
then
    echo "ChromeDriver installation failed!"
    exit 1
fi

echo "✅ Chrome and ChromeDriver installed successfully!"

# Install Python dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Build completed successfully."


