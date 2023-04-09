@echo off
echo Installing Microsoft Build Tools 2019...
choco install visualstudio2019buildtools -y

echo Installing Python package via pip...
pip install torch-2.0.0+cu117-cp38-cp38-win_amd64.whl

echo Done!

REM Download file
wget https://example.com/file.zip -O C:\path\to\save\file.zip

REM Install package
echo Installing Python package via pip...
pip install torch-2.0.0+cu117-cp38-cp38-win_amd64.whl
pip install requests

REM Copy file
copy C:\path\to\source\file.txt C:\path\to\destination\file.txt

echo Done.
