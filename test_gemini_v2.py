import google.generativeai as genai

# Hardcoded API key from chatbot_engine.py
API_KEY = "AIzaSyBPGMn9EHpFI0xWUaFWpYt9i3rPF_I6KZ4"
genai.configure(api_key=API_KEY)

def test_model(model_name):
    print(f"\n--- Testing Model: {model_name} ---")
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(
            "What is TCP/IP? Give a long, detailed explanation in 3 paragraphs.",
            generation_config={"max_output_tokens": 1024}
        )
        print("Response text:")
        print(response.text)
        print(f"Total characters: {len(response.text)}")
        
        # Check finish reason
        for candidate in response.candidates:
            print(f"Finish Reason: {candidate.finish_reason}")
            
    except Exception as e:
        print(f"Error with model {model_name}: {e}")

# test_model("models/gemini-2.5-flash") # The SDK likes full names
test_model("gemini-2.5-flash")
test_model("gemini-1.5-flash")
