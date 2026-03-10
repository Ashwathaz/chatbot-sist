import google.generativeai as genai

# Hardcoded API key from chatbot_engine.py
API_KEY = "AIzaSyBPGMn9EHpFI0xWUaFWpYt9i3rPF_I6KZ4"
genai.configure(api_key=API_KEY)

print("Listing available models:")
for model in genai.list_models():
    print(f"- {model.name} : {model.supported_generation_methods}")
