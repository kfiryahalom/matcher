class Job:
    title:str
    skill: str # better skill id?
    
    def __init__(self):
        return self
    
    def __init__(self, title, skill):
        self.title = title
        self.skill = skill

    
    # I guess there is some autoMapper?
    def convert_to_job(request):
        
        title = request['title']
        skill = request['skill']
        job = Job(title,skill )
        return job