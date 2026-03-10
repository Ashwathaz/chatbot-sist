import google.generativeai as genai

# Hardcoded API key from chatbot_engine.py
API_KEY = "AIzaSyBPGMn9EHpFI0xWUaFWpYt9i3rPF_I6KZ4"
genai.configure(api_key=API_KEY)

def test_chat_session(model_name):
    print(f"\n--- Testing Chat Session: {model_name} ---")
    try:
        model = genai.GenerativeModel(model_name)
        chat = model.start_chat()
        
        # 1st turn
        r1 = chat.send_message("Define TCP/IP in 1 word.")
        print(f"Turn 1: {r1.text}")
        
        # 2nd turn
        r2 = chat.send_message("Now explain it in detail.", 
                               generation_config={"max_output_tokens": 1024})
        print(f"Turn 2: {r2.text}")
        print(f"Length of turn 2: {len(r2.text)}")
        
    except Exception as e:
        print(f"Error: {e}")

test_chat_session("gemini-2.5-flash")
