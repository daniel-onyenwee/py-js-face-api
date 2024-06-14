rem Navigate to the directory containing your Python script
cd /d %~dp0

REM Define the Nuitka command with all the necessary options
set nuitka_command="C:\Users\danie\OneDrive\Desktop\code book\open_Noonoo\py-js-face-api\Scripts\python.exe" -m nuitka --standalone --onefile --output-dir=dist --output-filename=py-js-face-api.exe --product-name=PyJsFaceAPI --file-version=1.0.0 --product-version=1.0.0 --file-description="A CLI tool for face detection and recognition." --windows-icon-from-ico=./assets/icon.ico main.py

REM Execute the Nuitka command
%nuitka_command%
