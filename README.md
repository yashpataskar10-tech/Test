## Streamlit Community Cloud

1. Select `streamlit_app.py` as the app file when deploying this repository.
2. In the app settings, open **Secrets** and add:

```toml
GEMINI_API_KEY = "your-gemini-api-key"
TAVILY_API_KEY = "your-tavily-api-key"
```

3. Save the secrets and reboot the app.

Never commit API keys or a `.env` file to GitHub.

