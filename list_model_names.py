import google.generativeai as genai

# Hardcoded API key from chatbot_engine.py
API_KEY = "AIzaSyBPGMn9EHpFI0xWUaFWpYt9i3rPF_I6KZ4"
genai.configure(api_key=API_KEY)

print("Listing available model names:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")
