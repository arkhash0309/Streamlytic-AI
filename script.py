import openai
import streamlit as st

# Ensure to keep your API key secure
openai.api_key = "your_openai_api_key"

# Function to chat with GPT-3.5-turbo
def chat_with_gpt(conversation_history):
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=conversation_history
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit application
def main():
    st.title("GPT-3.5 Chatbot")
    
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = [{"role": "system", "content": "You are a helpful assistant."}]
    
    user_input = st.text_input("You: ", "")
    
    if st.button("Send"):
        if user_input.lower() in ["quit", "exit", "bye"]:
            st.write("Chatbot: Goodbye!")
            st.stop()
        
        st.session_state.conversation_history.append({"role": "user", "content": user_input})
        
        response = chat_with_gpt(st.session_state.conversation_history)
        st.session_state.conversation_history.append({"role": "assistant", "content": response})
        
        st.write(f"**You:** {user_input}")
        st.write(f"**Chatbot:** {response}")

    st.write("---")
    st.write("Conversation History:")
    for message in st.session_state.conversation_history:
        if message["role"] == "user":
            st.write(f"**You:** {message['content']}")
        elif message["role"] == "assistant":
            st.write(f"**Chatbot:** {message['content']}")

if __name__ == "__main__":
    main()
