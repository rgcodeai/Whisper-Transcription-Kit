@echo off
rem Activates the virtual environment required for the project
echo Activating virtual environment...
call venv/Scripts/activate.bat
rem Checks if the virtual environment was activated correctly
if %errorlevel% neq 0 (
    echo Error activating the virtual environment.
    goto end
    rem If there's an error, displays a message and jumps to the :end label
)

rem Executes the Python script that performs the desired task
echo Running Python script...
python transcribe.py
rem Checks if the Python script was executed correctly
if %errorlevel% neq 0 (
    echo Error running the Python script.
    goto end
    rem If there's an error, displays a message and jumps to the :end label
)

rem Displays a success message if the Python script executed without errors
echo.
echo Script executed successfully.

:end
rem Label to jump to if there is an error in any of the operations above or upon finishing the script
echo Press any key to close....
pause > nul