from nltk.chat.util import Chat, reflections

# Define the chat pairs and patterns.
pairs = [
    [r'my name is (.*)', ['hi %1']],
    [r'hello', ['Hello! How can I assist you?']],
    [r'hi', ['Hi there! How can I help you today?']],
    [r'how are you', ['I\'m just a program, so I don\'t have feelings, but thanks for asking!']],
    [r'you are amazing', ['Thank you! How can I assist you today?']],
    [r'quit', ['Goodbye! If you have more questions, just ask.']]
]

# Create the chatbot.
chat = Chat(pairs, reflections)

# This function will start the conversation.
def start_chat():
    print("Hello! Type \"quit\" to exit.")
    chat.converse()

# Run the chatbot function.
if __name__ == "__main__":
    start_chat()
