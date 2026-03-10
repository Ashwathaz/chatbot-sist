import google.generativeai as genai

# Hardcoded API key from chatbot_engine.py
API_KEY = "AIzaSyBPGMn9EHpFI0xWUaFWpYt9i3rPF_I6KZ4"
genai.configure(api_key=API_KEY)

def test_chat_session(model_name):
    print(f"\n--- Testing Chat Session: {model_name} ---")
    try:
        model = genai.GenerativeModel(model_name)
        chat = model.start_chat()
        
        # turn
        r = chat.send_message("What is TCP/IP? Explain in detail.", 
                               generation_config={"max_output_tokens": 1024})
        print(f"Turn: {r.text}")
        print(f"Length: {len(r.text)}")
        
    except Exception as e:
        print(f"Error: {e}")

test_chat_session("gemini-1.5-flash")
