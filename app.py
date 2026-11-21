import os

import streamlit as st
from openai import OpenAI


st.set_page_config(
    page_title="GenAI Assistant",
    page_icon="AI",
    layout="wide",
)


@st.cache_resource
def get_client(api_key: str) -> OpenAI:
    return OpenAI(
        api_key=api_key,
        base_url=os.getenv(
            "OPENAI_BASE_URL",
            "https://api.groq.com/openai/v1",
        ),
    )


st.title("GenAI Assistant")
st.caption("A simple generative AI chat application deployed with Streamlit")

api_key = os.getenv("GROQ_API_KEY") or st.sidebar.text_input(
    "Groq API key",
    type="password",
    help="Set GROQ_API_KEY in the platform secrets for deployment.",
)

model = st.sidebar.text_input(
    "Model",
    value=os.getenv("GENAI_MODEL", "llama-3.1-8b-instant"),
)

temperature = st.sidebar.slider("Temperature", 0.0, 1.5, 0.7, 0.1)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! Ask me a question.",
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Enter a prompt")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if not api_key:
        with st.chat_message("assistant"):
            st.error(
                "No API key found. Add GROQ_API_KEY to Streamlit secrets "
                "or enter it in the sidebar."
            )
    else:
        try:
            client = get_client(api_key)
            response = client.chat.completions.create(
                model=model,
                messages=st.session_state.messages,
                temperature=temperature,
            )
            answer = response.choices[0].message.content
            with st.chat_message("assistant"):
                st.markdown(answer)
            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )
        except Exception as exc:
            with st.chat_message("assistant"):
                st.error(f"Request failed: {exc}")
