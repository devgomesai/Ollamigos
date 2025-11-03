from crewai import LLM, Agent, Task, Crew
from crewai.project import CrewBase, agent, task, crew
from dotenv import load_dotenv
from textwrap import dedent
from datetime import datetime
import os
from .tools import search_tool, browse_tool, time_tool
load_dotenv()


@CrewBase
class ResearchCrew:
    """Research crew for conducting comprehensive research and generating reports"""
    
    # Define configuration file paths
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self, topic=None):
        # Centralized LLM configuration
        self.model = LLM(
            model=os.getenv("LLM_CHOICE"),
            base_url=os.getenv("BASE_URL"),
            temperature=0.1
        )
        
        # Create output directory if it doesn't exist
        self.output_dir = 'output'
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Generate dynamic filename
        self.output_file = self._generate_output_filename(topic)

    def _generate_output_filename(self, topic=None):
        """Generate a unique filename for the research report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if topic:
            safe_topic = "".join(c if c.isalnum() or c in (' ', '_', '-') else '_' for c in topic)
            safe_topic = safe_topic.strip().replace(' ', '_')[:50]  
            filename = f"research_report_{safe_topic}_{timestamp}.md"
        else:
            filename = f"research_report_{timestamp}.md"
        
        return os.path.join(self.output_dir, filename)

    @agent
    def researcher(self) -> Agent:
        """Research agent responsible for gathering and analyzing information"""
        return Agent(
            config=self.agents_config['researcher'],
            llm=self.model,
            tools=[search_tool, browse_tool],
            verbose=True,
            max_iter=15, 
            allow_delegation=False 
        )

    @agent
    def reporting_analyst(self) -> Agent:
        """Analyst agent responsible for synthesizing research into reports"""
        return Agent(
            config=self.agents_config['reporting_analyst'],
            llm=self.model,
            tools=[search_tool, browse_tool, time_tool],
            verbose=True,
            max_iter=15,
            allow_delegation=False
        )

    @task
    def research_task(self) -> Task:
        """Task for conducting initial research"""
        return Task(
            config=self.tasks_config['research_task'],
            agent=self.researcher(),  
            tools=[search_tool, browse_tool]
        )

    @task
    def reporting_task(self) -> Task:
        """Task for generating final report"""
        return Task(
            config=self.tasks_config['reporting_task'],
            agent=self.reporting_analyst(),  
            tools=[search_tool, browse_tool, time_tool],
            context=[self.research_task()],  
            output_file=self.output_file  
        )

    @crew
    def crew(self) -> Crew:
        """Creates a research crew with defined workflow"""
        return Crew(
            name="Ollamigos",
            agents=self.agents,  
            tasks=self.tasks,    
            verbose=True,
            process='sequential',  
            memory=False,  
        )