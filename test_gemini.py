import os
import google.generativeai as genai

# Hardcoded API key from chatbot_engine.py
API_KEY = "AIzaSyBPGMn9EHpFI0xWUaFWpYt9i3rPF_I6KZ4"
genai.configure(api_key=API_KEY)

def test_model(model_name):
    print(f"\n--- Testing Model: {model_name} ---")
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(
            "What is TCP/IP? Give a medium length explanation.",
            generation_config={"max_output_tokens": 1024}
        )
        print("Response received:")
        print(response.text)
        print(f"Total characters: {len(response.text)}")
    except Exception as e:
        print(f"Error with model {model_name}: {e}")

# Try current model
test_model("gemini-2.5-flash")

# Try recommended model
test_model("gemini-1.5-flash")
