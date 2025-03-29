from pydantic import BaseModel

class ParsedResume(BaseModel):
    summary: str = ""
    objective: str = ""
    work_experience: list[dict[str, str]] = []  # Specify dict types
    education: list[dict[str, str]] = []
    technical_skills: list[str] = []
    soft_skills: list[str] = []
    projects: list[dict[str, str]] = []
    
    # Additional Information
    certifications: list[dict[str, str]] = []
    publications: list[dict[str, str]] = []
    awards: list[dict[str, str]] = []
    professional_activities: list[str] = []
    interests: list[str] = []
    
    # Optional fields
    languages: list[dict[str, str]] = []
    references: list[dict[str, str]] = []

class JobDescription(BaseModel):
    job_title: str = ""
    job_description: str = ""
    key_requirements: list[str] = []
    preferred_qualifications: list[str] = []
    preferred_experience: list[str] = []

class SkillAnalysis(BaseModel):
    direct_matches: list[str]
    indirect_matches: list[dict[str, str]]  # {required_skill: related_candidate_skill}
    missing_skills: list[str]
    skill_score: float

class ExperienceAnalysis(BaseModel):
    years_match: bool
    relevance_score: float
    role_similarity: str
    experience_score: float

class PreferenceAnalysis(BaseModel):
    alignment_points: list[str]
    potential_conflicts: list[str]
    preference_score: float

class SkillGapAnalysis(BaseModel):
    skill_name: str
    key_concepts: list[str]
    learning_path: list[str]
    estimated_time: str

class OptimisedResume(BaseModel):
    skill_analysis: SkillAnalysis
    experience_analysis: ExperienceAnalysis
    preference_analysis: PreferenceAnalysis
    skill_gaps: list[SkillGapAnalysis]
    overall_score: float
    detailed_feedback: str
    
class Course(BaseModel):
    course_name: str = ""
    course_description: str = ""
    course_link: str = ""

class RecommendedCourses(BaseModel):
    recommended_courses: list[Course] = []

