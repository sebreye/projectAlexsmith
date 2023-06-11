from django_seed import Seed
from .models import Skills
def skills_run():
	seeder = Seed.seeder()
	datas = [
		{"title_skills": "html", "lvl_skills": 60},
  	    {"title_skills": "css", "lvl_skills": 30},
        {"title_skills": "js", "lvl_skills": 50},	
	]
	for data in datas:
		seeder.add_entity(Skills, 1, data)
	print(seeder.execute())