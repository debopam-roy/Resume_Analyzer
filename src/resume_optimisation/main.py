#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from resume_optimisation.crew import ResumeCrew
from resume_optimisation.utils.extract_document import extract_text
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

resume_content = extract_text('/Users/mapobed/Documents/metasage.ai_interview/knowledge/resume.pdf')  #input("Input the resume file path: ").strip()
job_description_content = extract_text('/Users/mapobed/Documents/metasage.ai_interview/knowledge/jd.pdf') #input("Input the job description file path: ").strip()


def train():
    """
    Train the crew for a given number of iterations.
    """
    try:
        ResumeCrew().resume_optimisation_crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs={"resume_content": resume_content, "job_description_content": job_description_content})

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ResumeCrew().resume_optimisation_crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """

    try:
        ResumeCrew().resume_optimisation_crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs={"resume_content": resume_content, "job_description_content": job_description_content})

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run():
    """
    Run the crew with user inputs.
    """
    
    try:

        ResumeCrew().resume_optimisation_crew().kickoff(inputs={"resume_content": resume_content, "job_description_content": job_description_content})

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()
