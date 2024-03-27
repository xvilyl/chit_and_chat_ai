import os
import streamlit as st

# Assuming `google.generativeai` is a placeholder for a real API like OpenAI's GPT.
# For demonstration, I'll adjust this to use OpenAI's API, but keep your original naming where possible.
import openai as genai

class ConstantClass:
    CHAT_GREET = "Hello fellow introvert! What can I help with today?"
    MODEL_NAME = "gpt-3.5-turbo"  # Adjusted to an actual model name from OpenAI.
    MAX_OUTPUT_TOKENS = 500  # This will be mapped to max_tokens in OpenAI's API.

class MethodClass:
    @staticmethod
    def set_key():
        # Configure the API key. Adjust this line to use OpenAI's API key configuration.
        genai.api_key = os.getenv("OPENAI_API_KEY")
    
    @staticmethod
    def create_model():
        # In the case of OpenAI, there's no need to create a model instance like this.
        # This method can be adjusted or removed. Keeping it for structural consistency.
        pass

    @staticmethod
    def create_prompt(recipient, message_type, user_input):
        prompt = ConstantClass.CHAT_GREET + "\n\n"
        prompt += f"Recipient: {recipient}\n"
        prompt += f"Message Type: {message_type}\n"
        prompt += f"User Input: {user_input}\n\n"
        prompt += "Generate a suitable message based on what other people say to user and reply back:"
        return prompt

    @staticmethod
    def generate_response(prompt):
        # Generate the response using the v1/chat/completions endpoint
        response = genai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()

def main():
    st.title("Chit & Chat AI")
    st.subheader('Hello fellow introvert! What can I help with today?', divider='rainbow')

    # Set API key
    MethodClass.set_key()

    # Create the Model - this step is adjusted as it's not necessary for OpenAI's usage pattern.
    # MethodClass.create_model()

    recipient = st.radio("Select the recipient:", ("Friend", "Family", "Formal", "Informal"))
    message_type = st.radio("Message type:", ("Reply - post what they have sent to you", "Start Conversation - Be brave!!"))
    user_input = st.text_area("Enter your message:")

    if st.button("Generate Message"):
        prompt = MethodClass.create_prompt(recipient, message_type, user_input)
        response = MethodClass.generate_response(prompt)
        st.success(response)

if __name__ == "__main__":
    main()
