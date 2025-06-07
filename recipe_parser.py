# recipe_parser.py

import re

def extract_recipe_info(translated_text):
    # Extract ingredients based on common cooking terms
    ingredients = re.findall(
        r"(?:add|use|take|mix|combine|include)\s+(.*?)\b(?:and|to|with|for|in|then|\.|,)",
        translated_text, re.IGNORECASE
    )
    
    # Extract steps based on transition keywords
    steps = re.split(
        r"(?:then|next|after that|now|first|second|third|finally|step\s+\d+)",
        translated_text, flags=re.IGNORECASE
    )

    # Clean up
    ingredients_clean = list(set([i.strip().lower() for i in ingredients if len(i.strip()) > 2]))
    steps_clean = [step.strip().capitalize() for step in steps if len(step.strip()) > 10]

    return {
        "ingredients": ingredients_clean,
        "steps": steps_clean
    }