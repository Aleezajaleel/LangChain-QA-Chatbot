import streamlit as st  #Streamlit for UI
from dotenv import load_dotenv # load .ennv into os.environ
import os  # interacts with environment vars
from langchain_groq import ChatGroq # Groq LLM integration
from langchain.memory import ConversationBufferMemory #Memory backend for chat
from langchain.chains import ConversationChain # chain that wires LLM + memory

## Load API Key

load_dotenv() # read .ev file
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY") # set groq key

## Streamlit App setup
st.set_page_config(page_title=" 💬 Conversational Chatbot") # title in browser tab
st.title("💬 Conversational Chatbot with Message History") # app header


# Sidebar Controls
model_name = st.sidebar.selectbox( #pick a supported model
    "Select Groq Model",
    ["gemma2-9b-it","deepseek-r1-distill-llama-70b","llama3-8b-8192"]
)

temperature = st.sidebar.slider(  #fix the ranndomness of the response
    "Temperature",0.0,1.0,0.7
)

max_tokens = st.sidebar.slider(  # max response length
    "Max Tokens", 50,300,150
)

# Initialize Memory and History

if "memory" not in st.session_state:
    # persist memory across reruns
    st.session_state.memory = ConversationBufferMemory(
        return_messages=True # return as list of messages, not one big string.
    )

if "history" not in st.session_state:
    # store role/content pairs display
    st.session_state.history= []


## user input
user_input = st.chat_input("You : ") # clears itself on enter

if user_input:
    # appennd user turn to visible history
    st.session_state.history.append(("user",user_input))

    # instantiiated a freash LLM for this turn
    llm= ChatGroq(
        model_name=model_name,
        temperature=temperature,
        max_tokens=max_tokens
    )


    # build conversationchain with our memory
    conv = ConversationChain(
        llm=llm,
        memory=st.session_state.memory,
        verbose = True
    )

    # get AI response (memory is updated interally)
    ai_response = conv.predict(input=user_input)


    # append assitant turn to bisible history
    st.session_state.history.append(("assistant", ai_response))

# Reder chat bubble

for role, text in st.session_state.history:
    if role == "user":
        st.chat_message("user").write(text) # user style
    else:
        st.chat_message("assistant").write(text) # assitant style

