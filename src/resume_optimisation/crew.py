from crewai.project import CrewBase, agent, task, crew
from crewai import Agent, Process, Task, Crew, LLM
from dotenv import load_dotenv
import os
from resume_optimisation.models import JobDescription, OptimisedResume, ParsedResume, RecommendedCourses
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

load_dotenv()

@CrewBase
class ResumeCrew():
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    llm_model = os.getenv("LLM_MODEL")
    llm_base_url = os.getenv("LLM_API_BASE")
    serper_api_key = os.getenv("SERPER_API_KEY")
    os.environ["SERPER_API_KEY"] = serper_api_key

    def __init__(self) -> None:
        self.llm = LLM(model=self.llm_model, base_url=self.llm_base_url)
        self.serper_search = SerperDevTool()
        self.scrape_website = ScrapeWebsiteTool()

    #Resume Analyser
    @agent
    def resume_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_analyzer'],
            verbose=True,
            llm=self.llm
        )
    
    @task
    def resume_analysis(self) ->Task:
        return Task(
            config=self.tasks_config['resume_analysis'],
            output_pydantic=ParsedResume,
            output_file='output/parsed_resume.json'
        )
    
    #Job Description Analyser
    @agent
    def job_description_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['job_description_analyzer'],
            verbose=True,
            llm=self.llm
        )
    
    @task
    def job_description_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['job_description_analysis'],
            output_pydantic=JobDescription,
            output_file='output/parsed_jd.json'

        )
    
    #Resume Validator
    @agent
    def resume_validator(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_validator'],
            verbose=True,
            tools=[self.serper_search],
            llm=self.llm
        )
    
    @task 
    def validate_resume(self) -> Task:
        return Task(
            config=self.tasks_config['validate_resume'],
            context=[self.resume_analysis(), self.job_description_analysis()],
            output_pydantic=OptimisedResume,
            output_file='output/optimised_resume.json'
        )

    #Course Recommender
    @agent
    def course_recommender(self) -> Agent:
        return Agent(
            config=self.agents_config['course_recommender'],
            verbose=True,
            tools=[self.serper_search, self.scrape_website],
            llm=self.llm
        )
    
    @task
    def course_recommendation(self) -> Task:
        return Task(
            config=self.tasks_config['course_recommendation'],
            context=[self.validate_resume()],
            output_pydantic=RecommendedCourses,
            output_file='output/recommended_courses.json'
        )
    
    @crew
    def resume_optimisation_crew(self) -> Crew:
        return Crew(
            agents= [self.resume_analyzer(), self.job_description_analyzer(), self.resume_validator(), self.course_recommender()],
            tasks= [self.resume_analysis(), self.job_description_analysis(), self.validate_resume(), self.course_recommendation()],
            process=Process.sequential,
            verbose=True
        )