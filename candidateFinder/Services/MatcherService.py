from candidateFinder.Models.CandidateMatch import CandidateMatch
from candidateFinder.Utils.RegexUtil import RegexUtil
from candidateFinder.Models.Job import Job
from candidateFinder.Data.Repository.CandidateRepository import CandidateRepository


# jods = [Job('job1','skill1'),Job('job2','skill2'),Job('job3','skill1')]
# candidates = [Candidate(1,'job2',['software','dfg','software engineer','dfs']),Candidate(2,'jofdgdf',['skill2','engineer']),Candidate(3,'job2',['software engineer'])]

class MatcherService:
    __candidateRepository: CandidateRepository

    def __init__(self):
        self.__candidateRepository = CandidateRepository()

    @staticmethod
    def __get_candidate_match(job, candidate):
        skill_score = 0  # => Part of second Option
        has_skill = False
        job_score = RegexUtil.get_top_match_ratio([candidate.title], job.title)
        if len(candidate.skills) > 0:
            # skill_score = RegexUtil.get_top_match_ratio(candidate.skills,job.skill) # => Part of second Option
            if job.skill in candidate.skills:
                has_skill = True
        candidateMatch = CandidateMatch(candidate.id, job_score, skill_score, has_skill)
        return candidateMatch

    def candidate_finder(self, request):
        # convert job to Job
        job = Job.convert_to_job(request)

        candidates = self.__candidateRepository.get_all_candidates()
        candidateMatchList = []

        for candidate in candidates:
            candidateMatchList.append(self.__get_candidate_match(job, candidate))

        # sort logic can be found in CandidateMatch class, functions (__eq__, __it__)
        candidateMatchList = [c.__dict__ for c in sorted(candidateMatchList, reverse=True)]
        return candidateMatchList
