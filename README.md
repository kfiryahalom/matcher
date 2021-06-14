# Matcher

* Short video demonstration can be found in Attachment folder

## Assumptions
* There wasn't exact instruction on how to trigger the logic so I assumed that you expected api call with Django framework(heard you are using Django and Postgres) - so I tried to learn a bit about that framework as well.
* Also there wasn't an exact explanation of what makes the match strong as there are 2 parameters (so in code you can find commented rows marked that they are part of Option 2) - explanation below
* rRegarding the best match (2.4.1) => I used regex match score regarding the title (job, candidate title)
    * Option 2 - is to do so also on skills (maybe good in case candidates not having the skill & having the same score to the title)

# Instructions to install
* Unzip the folder
* Open CMD on with the folder path
* pip install virtualenvwrapper-win
* mkvirtualenv gloat
* python manage.py runserver


# DB structure
* Created 3 tables
    * candidateFinder_candidate (id, title)
	* candidateFinder_skill (id, title (unique))
	* candidateFinder_candidate_skills (id, candidate_id,skill_id)
		* This is the mapping table between candidate to his skills
* You can find model view image in Attachment folder
			
* Connecting the postgres DB:
	* Create DB server called 'matcher' (or any name and change it in the settings.py in the DATABASES section)
		* Also make sure USER/PASSWORD are correct (is it shouldn't be exposed there in my opinion - I guess its better to set them in some config file which is not part of the repo or so)
	* in CMD:
		* python manage.py makemigrations candidateFinder
		* python manage.py sqlmigrate candidateFinder 0001 (or any other version you will get in the response)
		* python manage.py migrate
	* now the tables should be created (you can import records manually or from the files that I will attach)

# How to run the matcher
* Open postman
* After the server is running (python manage.py runserver)
* Create a POST request with ULR: http://127.0.0.1:8000/test/
* Wxample body request:
        ```
{
	"title":"Software Enginner",
	"skill": "C#"
}
        ```
* Result: candidate Mach object order from the top relevant match
	* Data contains the candidate_id, the score of the job title match, if the candidate has the job skill
	* skill_ratio is relevant for the `second Option` which has case of 2 candidates who have the same score on the title, with no exact skill, in that case, the match ratio on the candidate skills can make for an accurate match
		

# Extra what should I do to improve the project:
* As part of the lack of time to work on this proj this week and the fact that I'm not that aware (yet) of python programming, Django framework, and Django ORM
	* In the Data file - I should have made the query with Join and not separate and in memory (understood its something with `prefetch_related` or so)
* Regarding unit test - as well lake of time from today till Thursday (sorry for that)
	* I guess I should check how to do Dependency-Injection (if there something for that? in that language - can help with mocking I guess) in python and make the changes 
* In case this job is frequent called - using cache on the Get data would improve performance
* 
