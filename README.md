# 🗣️ Voice Note Diet Tracker 🍽️🧠  
**From voice to vision: transforming nutritionist voice notes into actionable diet steps.**

---

## 📖 Overview

Ever received a diet plan via voice message and had to **rewind 20 times** just to understand the ingredients?

**No more.**  
This AI-powered project takes any language voice note (e.g., from a nutritionist) and transforms it into:

- 📜 **Clean Transcription**
- 🌐 **English Translation**
- 📋 **Structured Steps**
- 🧾 **Key Ingredients & Methods**
- ⚡️ **Instant Summaries**

Built using OpenAI's Whisper and advanced NLP pipelines, this tool converts natural voice instructions into a **personalized, easy-to-follow digital meal guide.**

---

## 🧪 Features

| Feature | Description |
|--------|-------------|
| 🎧 Multilingual Audio Support | Accepts `.opus` audio in **any language** |
| 🔁 Converts to Text | Uses Whisper Large for precise transcription |
| 🌍 Translates to English | Makes sense of regional or mixed-language audios |
| 🧠 NLP Keyword Extractor | Identifies ingredients, cooking processes, and structure |
| 🪄 Step-by-step Output | Returns a well-formatted recipe or diet routine |
| ⚙️ Easy Integration | Modular file structure with clean Python logic |

---

## 🧰 Tech Stack

- **Python 3.11+**
- 🧠 OpenAI Whisper (`large` model)
- 🗂️ FFmpeg (for audio conversion)
- 🌍 Googletrans or Deep Translator
- 🔍 spaCy or custom NLP for extraction
- 🛠️ VS Code / Terminal

---

## 📂 Project Structure
voice-note-diet-tracker/
├── audio/
│   ├── input.opus         # Your raw voice note
│   └── converted.wav      # Converted WAV format
├── main.py                # Orchestrates the full pipeline
├── extractor.py           # Extracts keywords, steps, ingredients
├── requirements.txt       # Python dependencies
├── utils/
│   └── text_processing.py # Helper functions for text cleanup
├── .gitignore
└── README.md              # You’re reading this!



🧑‍🍳 Who’s This For?
	•	Nutritionists automating feedback
	•	Clients needing structure from audio notes
	•	AI hobbyists playing with Whisper
	•	Multilingual NLP enthusiasts

⸻

💡 Ideas for Future
	•	📱 Telegram or WhatsApp bot integration
	•	🧾 Export to PDF format with meal plan
	•	🔊 Real-time streaming transcription
	•	🧬 Integrate with health tracking APIs

⸻

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

Let’s make meal plans smarter, together. 🍜

⸻

📜 License

MIT License. Use freely, contribute generously.
