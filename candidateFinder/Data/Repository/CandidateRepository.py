from candidateFinder.models import Candidate as DB_Candidate , Candidate_Skills,Skill
from candidateFinder.Models.Candidate import Candidate

class CandidateRepository:
    
    def __get_skills(candidate_id):
        skills = []
        skill_ids = []
        db_skill = Skill.objects.all()# improve! should had been given as part of join query :/
        db_candidate_skills = Candidate_Skills.objects.all()# improve! should had been given as part of join query :/

        candidate_skills  = list(filter(lambda candidate_skill: candidate_skill.candidate_id == candidate_id, list(db_candidate_skills)))
        skill_ids = [s.id for s in candidate_skills]
        candidate_skills_list  = list(filter(lambda candidate_skill: candidate_skill.id in skill_ids, list(db_skill)))
        skills = [s.title for s in candidate_skills_list]
        return skills

    def get_all_candidates(self):
        candidates =[]

        # Didn't had the time to figure out how exactly to performe 'Join' in django ORM
        # So did it (and aware of that!) by getting each table seperatly and combine the relevant data in loops and lambda expressions
        db_candidate = DB_Candidate.objects.all()

        for db_candidate in db_candidate:
            skills = CandidateRepository.__get_skills(db_candidate.id)
            candidates.append(Candidate(db_candidate.id,db_candidate.title, skills))
        return candidates

