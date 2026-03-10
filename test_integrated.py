from chatbot_engine import generate_response

print("Test Turn 1: define TCP/IP")
resp1 = generate_response("define TCP/IP")
print(f"Response: {resp1[:100]}...")
print(f"Total length: {len(resp1)}")

print("\nTest Turn 2: what is ryzen 9950")
resp2 = generate_response("what is ryzen 9950")
print(f"Response: {resp2[:100]}...")
print(f"Total length: {len(resp2)}")
