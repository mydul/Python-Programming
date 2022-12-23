# Programmer Biodata

name = "John Smith"
age = 35
skills = ["Python", "JavaScript", "C++", "HTML/CSS"]
education = "Bachelor's degree in Computer Science"
experience = "5 years of software development experience"

def print_biodata():
  print("Name:", name)
  print("Age:", age)
  print("Skills:", ", ".join(skills))
  print("Education:", education)
  print("Experience:", experience)

print_biodata()

"""
Name: John Smith
Age: 35
Skills: Python, JavaScript, C++, HTML/CSS
Education: Bachelor's degree in Computer Science
Experience: 5 years of software development experience
"""

name = "John Smith"
age = 30
education = "Bachelor's degree in Computer Science"
skills = ["Python", "Java", "C++", "HTML/CSS", "JavaScript"]
experience = ["Software Developer at XYZ Company", "Intern at ABC Company"]

def print_biodata(name, age, education, skills, experience):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Education: {education}")
    print("Skills:")
    for skill in skills:
        print(f"- {skill}")
    print("Experience:")
    for exp in experience:
        print(f"- {exp}")

print_biodata(name, age, education, skills, experience)

"""
Name: John Smith
Age: 30
Education: Bachelor's degree in Computer Science
Skills:
- Python
- Java
- C++
- HTML/CSS
- JavaScript
Experience:
- Software Developer at XYZ Company
- Intern at ABC Company
"""

class Programmer:
  def __init__(self, name, age, language):
    self.name = name
    self.age = age
    self.language = language

  def bio(self):
    print(f"Hi, my name is {self.name} and I am a programmer.")
    print(f"I am {self.age} years old and I am proficient in {self.language}.")

programmer = Programmer("John Doe", 30, "Python")
programmer.bio()

"""
Hi, my name is John Doe and I am a programmer.
I am 30 years old and I am proficient in Python.

"""