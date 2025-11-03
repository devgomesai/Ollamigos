# Install uv package manager
pip install uv

# Install dependencies using uv
uv sync

# Activate the virtual environment
.venv\Scripts\activate

# Pull the required Ollama model
ollama pull gpt-oss:120b-cloud 

# Set up environment variables
@"
LLM_CHOICE="ollama/gpt-oss:120b-cloud"
BASE_URL="http://localhost:11434"
"@ | Set-Content .env

# Run the API
uvicorn src.api.api:app