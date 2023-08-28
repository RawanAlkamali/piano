#  CV Program | By: Rawan Alkamali 

class Experience:
    def __init__(self, company, job_title, start_date, end_date):
        self.company = company
        self.job_title = job_title
        self.start_date = start_date
        self.end_date = end_date

    def display_experience(self):
        print(f"\n[=] Company: {self.company}")
        print(f"[=] Job Title: {self.job_title}")
        print(f"[=] Start Date: {self.start_date}")
        print(f"[=] End Date: {self.end_date}")
        

class Education:
    def __init__(self, degree, institution, completion_date):
        self.degree = degree
        self.institution = institution
        self.completion_date = completion_date

    def display_education(self):
        print(f"\n[=] Degree: {self.degree}")
        print(f"[=] Institution: {self.institution}")
        print(f"[=] Completion Date: {self.completion_date}")
        

class Skill:
    def __init__(self, skill, percentage):
        self.skill = skill
        self.percentage = percentage
		
    def display_skill(self):
        print(f"\n[=] Skill: {self.skill}")
        print(f"[=] Percentage: {self.percentage}")
   


class CV:
    def __init__(self, name):
        self.name = name
        self.experiences = []
        self.education = []
        self.skills = []

    def add_experience(self):
        print("\n[--- Add Experience ---]")       
        company = input("\n  [>>] Enter Company Name: ")
        job_title = input("\n  [>>] Enter Job Title: ")
        start_date = input("\n  [>>] Enter Start Date: ")
        end_date = input("\n  [>>] Enter End Date: ")

        experience = Experience(company, job_title, start_date, end_date)
        self.experiences.append(experience)

        choice = input("\n  [!?] Do You Want to Add Another Experience ? (yes/no): ")
        if choice.lower() == "yes":
            self.add_experience()

    def add_education(self):
        print("\n[--- Add Education ---]")
        degree = input("\n  [>>] Enter Degree: ")
        institution = input("\n  [>>] Enter Institution: ")
        completion_date = input("\n  [>>] Enter Completion Date: ")

        education = Education(degree, institution, completion_date)
        self.education.append(education)

        choice = input("\n  [!?]  Do You Eant to Add Another Education ? (yes/no): ")
        if choice.lower() == "yes":
            self.add_education()

    def add_skill(self):
        print("\n[--- Add Skills ---]")
        skill = input("\n  [>>] Enter Skill: ")
        percentage = input("\n  [>>] Enter Percentage: ")

        skill = Skill(skill, percentage)
        self.skills.append(skill)

        choice = input("\n  [!?] Do You Want to Add Another Skill ? (yes/no): ")
        if choice.lower() == "yes":
            self.add_skill()

    def display_cv(self):
        print("\n\n-----------------------------------")
        print("\n  -----------\n  | YOUR CV |\n  -----------")
        print(f"\n  [=] Name: {self.name}")

        print("\n  Experiences:\n  ------------")
        for experience in self.experiences:
            experience.display_experience()

        print("\n  Education:\n  ----------")
        for education in self.education:
            education.display_education()

        print("\n  Skills:\n  ------- ")
        for skill in self.skills:
            skill.display_skill()





print("\n\t -----------------------------------\n\t | CV Program | By: Rawan Alkamali |\n\t -----------------------------------\n")

name = input("\t [>>] Enter Your Name: ")
cv = CV(name)

choice = input("\n   [!?] Do You Want to Add Skills ? (yes/no): ")
if choice.lower() == "yes":
    cv.add_skill()
    
cv.add_education()

cv.add_experience()

cv.display_cv()