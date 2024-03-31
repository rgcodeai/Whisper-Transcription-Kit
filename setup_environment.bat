@echo off
cd /d %~dp0
rem Creates a new virtual environment for this project
echo Creating virtual environment...
python -m venv venv
rem Check if the virtual environment was created successfully
if %errorlevel% neq 0 (
    echo Error creating the virtual environment.
    goto end
)

rem Activates the newly created virtual environment
echo Activating virtual environment...
call venv/Scripts/activate.bat
rem Checks if the dependencies were installed correctly
if %errorlevel% neq 0 (
    echo Error activating the virtual environment.
    goto end
)

rem Updates pip to the latest version
echo Updating pip...
python -m pip install --upgrade pip
rem Check if pip was updated correctly
if %errorlevel% neq 0 (
    echo Error updating pip.
    goto end
)

rem Install FFmpeg using Chocolatey
echo Installing FFmpeg...
choco install ffmpeg -y
rem Check if FFmpeg was installed correctly
if %errorlevel% neq 0 (
    echo Error installing FFmpeg.
    goto end
)

rem Installs torch, torchvision, and torchaudio with the specific index URL
echo Installing torch, torchvision, and torchaudio...
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
rem Checks if the specific dependencies were installed correctly
if %errorlevel% neq 0 (
    echo Error installing torch, torchvision, and torchaudio.
    goto end
)

rem Installs the necessary dependencies for the project from requirements.txt
echo Installing remaining dependencies from requirements.txt...
pip install -r requirements.txt
rem Check if the dependencies were installed correctly
if %errorlevel% neq 0 (
    echo Error installing remaining dependencies.
    goto end
)

rem Confirms that the environment is ready to be used
echo.
echo Development environment ready.

:end
rem Label to jump to if there is an error in any of the previous operations or at the end of the script
echo Press any key to close....
pause > nul