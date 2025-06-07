# main.py

import whisper
from recipe_parser import extract_recipe_info  # Importing from new file

# Load model
model = whisper.load_model("large")

# Transcribe and translate
result = model.transcribe("audio/converted.wav", task="translate")
translated_text = result["text"]

# Print translated text
print("\n🔤 Translated English Text:\n", translated_text)

# Extract ingredients and steps
recipe_data = extract_recipe_info(translated_text)

# Print nicely
print("\n📌 Ingredients:")
for ing in recipe_data["ingredients"]:
    print(f"- {ing}")

print("\n📋 Steps:")
for i, step in enumerate(recipe_data["steps"], 1):
    print(f"{i}. {step}")

# Optional: Save to file
with open("extracted_recipe.txt", "w") as f:
    f.write("Ingredients:\n")
    for ing in recipe_data["ingredients"]:
        f.write(f"- {ing}\n")
    f.write("\nSteps:\n")
    for i, step in enumerate(recipe_data["steps"], 1):
        f.write(f"{i}. {step}\n")