@echo off

REM to install Chocolatey from the command line on Windows
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

echo Installing Python...
powershell.exe -Command "Start-Process cmd -Verb RunAs -ArgumentList '/c choco install python3 -y'"

echo Setting Python in PATH...
setx PATH "%PATH%;C:\Python38\Scripts;C:\Python38"


REM Install package
echo Installing required packages...
pip install requests wget
wget https://github.com/nomic-ai/gpt4all/archive/refs/heads/main.zip
tar -xvf gpt4all-main.zip
cd gpt4all-main
cd chat
wget https://the-eye.eu/public/AI/models/nomic-ai/gpt4all/gpt4all-lora-quantized.bin


REM torch the cpu version
pip install torch
REM If you want to install the GPU version, you need to use the following command instead:
REM pip install torch torchvision torchaudio -f https://download.pytorch.org/whl/cu111/torch_stable.html


pip install accelerate datasets torchmetrics evaluate transformers wandb peft nodelist-inflator sentencepiece jsonlines

echo Installing Microsoft Build Tools 2019...
choco install visualstudio2019buildtools -y

REM Download file
REM wget https://example.com/file.zip -O C:\path\to\save\file.zip

REM now there is a .exe file in your folder. Run and Enjoy it!


echo ALL Done.
