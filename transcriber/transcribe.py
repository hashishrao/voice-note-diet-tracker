import whisper

def run_transcription(wav_path):
    model = whisper.load_model("large")  # or "medium", "large"
    result = model.transcribe("audio/converted.wav", language="te")
    print("Detected Language:", result["language"])
    print("Transcription:", result["text"])