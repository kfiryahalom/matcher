class Candidate:
    id: int
    title: str
    skills: list ## better skill ids

    def __init__(self, id, title, skills):
        self.id = id
        self.title = title
        self.skills = skills
