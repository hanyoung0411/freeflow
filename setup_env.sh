#!/bin/bash

set -x

# Check Python version
python310_path=$(which python3.10)
if [ -n "$python310_path" ]; then
  echo "Python 3.10 found at $python310_path"
else
  echo "Python 3.10 not found"
  exit 1
fi

# Create a virtual environment
virtualenv --python=python3.10 venv
echo 'Virtual environment created!'
source venv/bin/activate

# Install numpy first (as it seems to be missing)
pip install numpy

# Operating system specific installs
if [[ "$OSTYPE" == "darwin"* ]]; then
  # MacOS
  brew install llvm@11
  brew install ffmpeg  # Installing ffmpeg on macOS
  export LLVM_CONFIG=$(brew --prefix llvm@11)/bin/llvm-config
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
  # Linux
  sudo apt update
  sudo apt install -y llvm-11-dev
  sudo apt install -y ffmpeg  # Installing ffmpeg on Linux
  export LLVM_CONFIG=/usr/bin/llvm-config-11
elif [[ "$OSTYPE" == "msys" ]]; then
  # Windows
  echo "Please manually install LLVM and FFmpeg for Windows and set LLVM_CONFIG"
  exit 1
fi

echo "Using LLVM_CONFIG=$LLVM_CONFIG"

# Finally, install the requirements
pip install -r requirements.txt
echo 'Dependencies installation ended!'