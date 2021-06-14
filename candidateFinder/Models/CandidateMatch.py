class CandidateMatch:
    candidate_id: int
    title_ratio: float
    skill_ratio: float
    has_skill: bool
    total_ratio: float

    def __init__(self, id, title_ratio,skill_ratio ,has_skill):
        self.candidate_id = id
        self.title_ratio = title_ratio
        self.skill_ratio = skill_ratio
        self.has_skill = has_skill
        #self.total_ratio = title_ratio + skill_ratio
        self.total_ratio = title_ratio

    # Needed for the sort function
    def __eq__(self, other):
        return self.total_ratio == other.total_ratio and self.has_skill == other.has_skill

    def __lt__(self, other):
        return self.total_ratio < other.total_ratio or (self.total_ratio == other.total_ratio and self.has_skill == False)
