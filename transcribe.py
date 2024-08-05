import os
import whisper
import datetime
import torch

# Definición del modelo por defecto
DEFAULT_MODEL = "medium"

def seconds_to_srt_format(seconds):
    """Converts seconds to the HH:MM:SS,MMM format required by SRT."""
    whole_seconds = int(seconds)
    milliseconds = int((seconds - whole_seconds) * 1000)
    return f"{datetime.timedelta(seconds=whole_seconds)},{milliseconds:03d}"

def transcribe_audio_to_srt(transcription_result):
    """Creates SRT content from the transcription result."""
    srt_content = []
    for i, segment in enumerate(transcription_result["segments"], start=1):
        start_time = seconds_to_srt_format(segment["start"])
        end_time = seconds_to_srt_format(segment["end"])
        text = segment["text"].replace('\n', ' ').strip()  # Remove line breaks and strip whitespace
        srt_content.append(f"{i}\n{start_time} --> {end_time}\n{text}\n")
    return "\n".join(srt_content)

def transcribe_audio_to_txt(transcription_result):
    """Creates TXT content from the transcription result."""
    return "\n".join(segment["text"].strip() for segment in transcription_result["segments"])

def transcribe_audio_to_vtt(transcription_result):
    """Creates VTT content from the transcription result."""
    vtt_content = "WEBVTT\n\n"
    for i, segment in enumerate(transcription_result["segments"], start=1):
        start_time = seconds_to_srt_format(segment["start"])
        end_time = seconds_to_srt_format(segment["end"])
        text = segment["text"].replace('\n', ' ').strip()
        
        vtt_content += f"{start_time} --> {end_time}\n{text}\n\n"
    return vtt_content

def transcribe_audio_to_tsv(transcription_result):
    """Creates TSV content from the transcription result."""
    tsv_content = "StartTime\tEndTime\tText\n"
    for segment in transcription_result["segments"]:
        start_time = seconds_to_srt_format(segment["start"])
        end_time = seconds_to_srt_format(segment["end"])
        text = segment["text"].replace('\n', ' ').strip()
        
        tsv_content += f"{start_time}\t{end_time}\t{text}\n"
    return tsv_content

def generate_transcription_files(source_dir, target_dir, model_name=DEFAULT_MODEL):
    """Generates transcription files in multiple formats for all audio and video files in the source directory."""
    # Check if CUDA is available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    
    model = whisper.load_model(model_name, device=device)
    os.makedirs(target_dir, exist_ok=True)
    supported_extensions = ('.mp3', '.wav', '.m4a', '.aac', '.mp4', '.mov', '.avi', '.mkv', '.flac')
    
    for file_name in os.listdir(source_dir):
        if not file_name.lower().endswith(supported_extensions):
            continue
        audio_path = os.path.join(source_dir, file_name)
        base_name = os.path.splitext(file_name)[0]
        
        print(f"Transcribing: {file_name}")
        transcription_result = model.transcribe(audio_path, verbose=False)
        
        # Generate each format
        formats = {
            'srt': transcribe_audio_to_srt,
            'txt': transcribe_audio_to_txt,
            'vtt': transcribe_audio_to_vtt,
            'tsv': transcribe_audio_to_tsv,
        }
        
        for ext, func in formats.items():
            content = func(transcription_result)
            file_path = os.path.join(target_dir, f"{base_name}.{ext}")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
        print(f"Finished transcribing: {file_name}")

def main():
    source_dir = "input"
    target_dir = "output"
    generate_transcription_files(source_dir, target_dir)

if __name__ == "__main__":
    main()
