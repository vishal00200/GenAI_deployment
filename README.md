# GenAI Assistant

A Streamlit chat application powered by a Groq/OpenAI-compatible chat completion API.

## Run locally

```bash
pip install -r requirements.txt
set GROQ_API_KEY=your_api_key
streamlit run app.py
```

## Streamlit Community Cloud

1. Push this project to GitHub.
2. Open https://share.streamlit.io/.
3. Connect the repository and select `app.py`.
4. Add `GROQ_API_KEY` in App settings under Secrets.
5. Deploy and test the generated URL.

## Hugging Face Spaces

1. Create a new Streamlit Space.
2. Connect the GitHub repository or upload `app.py`, `requirements.txt`, and `README.md`.
3. Add `GROQ_API_KEY` under Space settings > Variables and secrets.
4. Build, open the Space, and test it in a browser.
