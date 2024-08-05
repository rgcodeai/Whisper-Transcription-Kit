# Whisper Transcription Kit

## Description

This project uses the OpenAI Whisper model to transcribe audio and video files into text. It is designed to be easy to use, allowing users to convert their multimedia files into written content using advanced machine learning technologies.

## Requirements

- Python 3.8 3.11.
- Chocolatey
- CUDA (for users with NVIDIA GPUs)

## File Description

- **`requirements.txt`**: Contains a list of the Python packages required to run the transcription scripts, including the Whisper model for handling multimedia files.
- **`setup_environment.bat`**: This batch script is designed to set up the required Python environment for the project. Its main function is to automate various processes, including the creation of a virtual environment and the installation of the dependencies specified in **`requirements.txt`**. It also handles the installation of FFmpeg through Chocolatey and PyTorch version 12.1.
- **`run_script.bat`**: This batch file is used to start the transcription process. It provides a simple way to initiate the transcription with a double-click.
- **`transcribe.py`**: The main Python script that uses the Whisper model to transcribe audio and video files. It includes the logic for processing multimedia files and generating the transcriptions.

## Folder Structure

- **`input/`**: Folder where users should place the audio or video files they want to transcribe.
- **`output/`**: Folder where the generated transcriptions will be saved. Each transcription is named according to its source file. The transcriptions are saved in (srt, tsv, txt, vtt) formats.

## Installation

1. **Clone the Project**: Start by cloning the repository or downloading the project files to your local machine.
2. **Set up the Environment**:
    - Navigate to the project directory.
    - Run **`setup_environment.bat`** as an administrator. This script will create a Python virtual environment and install the necessary dependencies.

Refer to our detailed guide for [installing Whisper on Windows](https://mistercontenidos.com/en/how-to-install-whisper-on-windows-a-simple-step-by-step-guide/).

## Usage

1. **Prepare Your Multimedia Files**: Place the audio or video files you want to transcribe in the **`input/`** folder.
2. **Run the Transcription**:
    - Double-click on **`run_script.bat`** to start the transcription process.
    - The script will automatically process all the files present in the **`input/`** folder and generate the transcriptions in the **`output/`** folder.
3. **Access the Transcriptions**: Once the transcription process is complete, you can find the resulting texts in the **`output/`** folder. Each transcription file will be named after the original file for easy identification.

## Change Log

- **March 30, 2024**: Project published.
- **August 4, 2024**: Automatically selects the device on which the models should be loaded, either CUDA or CPU. If CUDA is not available, it will run on CPU. It also makes it easy to change models, the "medium" model is used by default. If you want to change models just replace the word "medium" with (tiny, base, small, or large).

## Languages

- [Español](docs/es/README_ES.md)
- [Português](docs/pt/README_PT.md)
