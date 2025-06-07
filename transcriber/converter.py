import subprocess

def convert_opus_to_wav(input_path, output_path):
    command = ["ffmpeg", "-y", "-i", input_path, output_path]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg conversion failed: {result.stderr}")