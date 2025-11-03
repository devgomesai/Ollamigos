# Ollamigos: CrewAI Research Assistant

> 🚀 **CrewAI + Ollama: The Ultimate AI Agent Development Combination**

A powerful AI research assistant that harnesses the synergistic power of **CrewAI** and **Ollama** to provide local, private, and efficient AI research capabilities. This project demonstrates how combining these two technologies creates the best possible setup for building multi-agent AI systems.

## 🌟 Features

- 🤖 **Multi-Agent AI Research**: Leverages CrewAI's powerful multi-agent framework for intelligent research tasks
- 🔒 **Local LLM Processing**: Uses Ollama for privacy-focused, local execution of large language models
- 📊 **Intelligent Research Workflow**: Research agent gathers data, reporting analyst creates detailed reports
- 💻 **Modern Web Interface**: Sleek, intuitive UI with a vibrant blue/turquoise color scheme and real-time progress indicators
- 🔍 **Advanced Tools**: Web search, website browsing, and utility tools for comprehensive research
- 📄 **Markdown Reports**: Generates clean, formatted research reports in markdown format
- ⚡ **Configurable Architecture**: YAML-based agent and task configuration for easy customization
- 🌐 **Web Integration**: DuckDuckGo search, website browsing, and current time tools

## 🛠 Tech Stack

- [**CrewAI**](https://crewai.com): Multi-agent framework for orchestrating autonomous AI agents
- [**Ollama**](https://ollama.ai): Tool for running large language models locally
- [**Python 3.13**](https://python.org): Core programming language
- [**FastAPI**](https://fastapi.tiangolo.com): Web framework for the API and serving the web interface
- [**Jinja2**](https://jinja.palletsprojects.com): Template engine for the web UI
- [**LangChain**](https://langchain.com): For LLM integration and utilities
- [**Pydantic**](https://pydantic.dev): Data validation and settings management
- [**Requests/BeautifulSoup**](https://requests.readthedocs.io/): Web scraping and browsing tools
- [**uv**](https://github.com/astral-sh/uv): Fast Python package installer and resolver

## 📦 Installation

### Prerequisites

- Python 3.13 or higher
- [Ollama](https://ollama.ai) installed and running
- Compatible LLM model (recommended: glm-4.6:cloud or similar)

### Step-by-Step Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/ollama-cloud.git
   cd ollama-cloud
   ```

## 🚀 Usage

### Quick Start

After installation, simply run:

```bash
.\setup.ps1
```

This will:
1. Install the uv package manager if needed
2. Install dependencies using uv
3. Activate the virtual environment
4. Pull the required Ollama model (glm-4.6:cloud)
5. Set up environment variables
6. Launch the API server

The application launches a web interface where you can:

- Enter research topics in the intuitive web UI
- Monitor the research process in real-time
- View detailed reports with rich formatting
- Download generated reports

### Direct Usage

You can also integrate the research crew directly in your code:

```python
from src.agent.src.agent.crew import ResearchCrew

# Initialize the crew
crew = ResearchCrew()

# Define your inputs
inputs = {'topic': 'Improving personal productivity in the workplace'}

# Kickoff the process
result = crew.crew().kickoff(inputs=inputs)

print(result)
```

Alternatively, you can interact with the API directly:

```bash
# Health check
curl http://localhost:8000/health

# Start a research task
curl -X POST http://localhost:8000/kickoff \
  -H "Content-Type: application/json" \
  -d '{"topic": "Your research topic here"}'
```

## 🌐 API Endpoints

The application provides several API endpoints for interaction:

- `GET /` - Home page with the web interface
- `GET /health` - Health check endpoint to verify the API is running
- `POST /kickoff` - Start the research crew with a specific topic
- `GET /docs` - Interactive API documentation (Swagger UI)

## ⚙️ Configuration

### Environment Variables

The application uses a `.env` file for configuration:

- `LLM_CHOICE`: The model to use (e.g., `ollama/glm-4.6:cloud`)
- `BASE_URL`: The Ollama server URL (default: `http://localhost:11434`)

### Agent Configuration

Agents and tasks are configured through YAML files in the `src/agent/src/agent/config/` directory:

- `agents.yaml`: Defines agent roles, goals, and backstories
- `tasks.yaml`: Defines research and reporting tasks with descriptions and expected outputs

### Custom Models

To use a different Ollama model:

1. Pull the model: `ollama pull your-model-name`
2. Update `LLM_CHOICE` in your `.env` file
3. Adjust temperature settings as needed

## 📁 Project Structure

```
ollama-cloud/
├── .env                   # Environment variables
├── .gitignore             # Git ignore rules
├── pyproject.toml         # Project dependencies and metadata
├── README.md              # This file
├── setup.ps1              # Setup script for Windows
├── trace.png              # Architecture diagram
├── uv.lock                # Dependency lock file
├── output/                # Generated research reports
│   └── research_report.md
└── src/
    ├── agent/             # CrewAI agent implementation
    │   ├── src/
    │   │   └── agent/
    │   │       ├── __init__.py
    │   │       ├── crew.py         # CrewAI implementation
    │   │       ├── config/
    │   │       │   ├── agents.yaml # Agent configurations
    │   │       │   └── tasks.yaml  # Task configurations
    │   │       └── tools/
    │   │           ├── __init__.py
    │   │           └── tools.py    # Custom tools implementation
    ├── api/               # FastAPI application
    │   ├── __init__.py
    │   └── api.py         # API endpoints and web interface
    ├── static/            # Static assets (CSS, JS, images)
    │   ├── crew_ai.png
    │   ├── ollama.png
    │   └── x.svg
    ├── templates/         # HTML templates for web interface
    │   └── index.html     # Main web interface template
    └── tests/             # Test files
```

## 🔍 How It Works

### Web Application Architecture

The system is built as a web application with the following components:

1. **FastAPI Backend**: Provides RESTful API endpoints for research tasks
2. **Modern Web Interface**: User-friendly UI built with Jinja2 templates
3. **CrewAI Framework**: Orchestrates the multi-agent research workflow

### Multi-Agent Architecture

The system implements a two-agent research workflow:

1. **Research Agent**:
   - Gathers information using search and browsing tools
   - Focuses on collecting relevant data about the specified topic
   - Operates with a temperature setting of 0.1 for consistent results

2. **Reporting Analyst Agent**:
   - Synthesizes research findings into a comprehensive report
   - Expands bullet points into detailed sections
   - Formats output in markdown for easy reading

### Tool Integration

The system includes several custom tools:

- **DuckDuckGo Search**: For finding general information
- **Website Browser**: For extracting content from specific URLs
- **Current Time Tool**: For time-sensitive queries

### Process Flow

1. User enters a research topic via the web interface
2. The API receives the request and initializes the CrewAI workflow
3. CrewAI orchestrates the agents in sequential order
4. Research agent performs initial investigation
5. Reporting analyst creates the final report
6. Results are saved to a timestamped markdown file in the output directory
7. The completed report is returned to the web interface for display and download

## 🙏 Acknowledgments

- [CrewAI](https://crewai.com) for their powerful multi-agent framework
- [Ollama](https://ollama.ai) for making local LLM execution accessible
- The open-source community for providing the tools and libraries that make this project possible

## 🚀 Why CrewAI + Ollama is the Best Combination

The combination of CrewAI and Ollama provides unparalleled advantages for AI development:

- **Privacy First**: All processing happens locally with Ollama, ensuring your data never leaves your machine
- **Cost Effective**: No API costs or rate limits when running local models
- **Flexibility**: CrewAI allows for complex agent workflows while Ollama supports diverse models
- **Performance**: Local execution provides consistent response times
- **Customization**: Full control over both agent behavior and model parameters

This project exemplifies how these two technologies work together to create powerful, private, and efficient AI solutions.