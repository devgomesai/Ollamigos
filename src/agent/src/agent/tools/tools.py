from scrapegraph_py.client import Client


from crewai.tools import BaseTool
from langchain_community.tools import DuckDuckGoSearchRun
import os
from dotenv import load_dotenv
from scrapegraph_py import Client
from datetime import datetime
from typing import Optional, ClassVar

load_dotenv('.env')

class BrowseWebsiteTool(BaseTool):
    name: str = "Browse Website"
    description: str = "Browse and extract content from a specific website URL. Use this when you need to get information from a particular site."
    
    client: ClassVar[Client] = Client(api_key=os.getenv('SGAI_API_KEY'))
    
    def _run(self, url: str) -> str:
        """Browse a website and return its content"""
        return self.client.markdownify(website_url=url)
    
class CurrentTimeTool(BaseTool):
    name: str = "Current Time"
    description: str = "Get the current time. Use this when you need to know the current date and time."
    
    def _run(self) -> str:
        """Get the current time"""
        return f"Current time is: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
class DuckDuckGoSearchTool(BaseTool):
    name: str = "DuckDuckGo Search"
    description: str = "Search for information using DuckDuckGo. Use this when you need to find general information about a topic."
    
    def _run(self, query: str) -> str:
        """Search using DuckDuckGo and return results"""
        search_func = DuckDuckGoSearchRun()
        return search_func.run(query)


# Instantiate the tools
search_tool = DuckDuckGoSearchTool()
browse_tool = BrowseWebsiteTool()
time_tool = CurrentTimeTool()

# List of all tools
ALL_TOOLS = [
    search_tool,
    browse_tool,
    time_tool
]