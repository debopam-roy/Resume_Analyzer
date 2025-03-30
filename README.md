# AI-Powered Resume Optimization System

An intelligent system that analyzes resumes against job descriptions, providing optimization suggestions and skill gap analysis using AI.

## 🌟 Features

- **Resume Analysis**: Parses and analyzes resume content
- **Job Description Matching**: Compares resume against job requirements
- **Skill Gap Analysis**: Identifies missing skills and provides learning paths
- **Experience Analysis**: Evaluates work experience relevance
- **Course Recommendations**: Suggests relevant courses for skill improvement
- **API Integration**: RESTful API for easy integration

## 🛠️ Technology Stack

- Python 3.12
- FastAPI
- Pydantic
- CrewAI
- PDF Text Extraction Tools

## 📋 Prerequisites

```bash
- Python 3.8 or higher
- pip (Python package manager)
```

## 🚀 Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/resume-optimization-system.git
cd resume-optimization-system
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

## 📚 Project Structure

# ResumeOptimisation Crew

Welcome to the ResumeOptimisation Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/resume_optimisation/config/agents.yaml` to define your agents
- Modify `src/resume_optimisation/config/tasks.yaml` to define your tasks
- Modify `src/resume_optimisation/crew.py` to add your own logic, tools and specific args
- Modify `src/resume_optimisation/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the resume_optimisation Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The resume_optimisation Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the ResumeOptimisation Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
