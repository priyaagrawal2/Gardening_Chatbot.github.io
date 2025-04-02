import google.generativeai as genai
import config

# Set up API key
genai.configure(api_key=config.GEMINI_API_KEY)

def chatbot(input_text):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        
        # Proper system message format
        system_instruction = "You are a Gardening and Agriculture expert. Only answer questions related to Gardening and Agriculture. If a question is not related, say: 'Sorry, I can only help with Gardening and Agriculture-related questions.'"

        response = model.generate_content([
            {"text": system_instruction},  # System instruction
            {"text": input_text}  # User query
        ])
        
        return response.text.strip() if response and response.text else "Sorry, I can only help with Gardening and Agriculture-related questions."
    
    except Exception as e:
        return f"Error: {str(e)}"
