import json

class Biodata:
  def __init__(self, name, pronouns, education, experience):
    self.name = name
    self.pronouns = pronouns
    self.education = education
    self.experience = experience
  
  def to_dict(self):
    return {
      'name': self.name,
      'pronouns': self.pronouns,
      'education': self.education,
      'experience': self.experience
    }
  
  def to_json(self):
    return json.dumps(self.to_dict())

biodata = Biodata(
  name = "Mydul Islam",
  pronouns = "He / Him",
  education = "A postgraduate student of University of Siegen",
  experience = "Research Assistant at University of Siegen",
)

print(biodata.to_json())

language = ["English", "German", "Bengali"]
programming = ["C", "C++", "Python", "HTML", "CSS", "LaTeX", "MATLAB", "VHDL", "Arduino" , "Shell script"]
tools = ["Microsoft Office", "Proteus", "PSpice", "LTSpice", "OriginPro", "MicroWind", "COMSOL Multiphysics", "Cadence"]
accustomed = ["Linux", "Windows", "Raspbian"]


def my_skills(language, programming, tools, accustomed):

    print("\n")
    print("Language:")
    for lan in language:
        print(f"- {lan}")

    print("\n")
    print("Programming:")
    for pro in programming:
        print(f"- {pro}")

    print("\n")
    print("Tools:")
    for tool in tools:
        print(f"- {tool}")

    print("\n")
    print("Accustomed:")
    for accus in accustomed:
        print(f"- {accus}")

my_skills(language, programming, tools, accustomed)

class SWOT_analysis:
  def __init__(self, strengths, weaknesses, threats, opportunities):
    self.strengths = strengths
    self.weaknesses = weaknesses
    self.threats = threats
    self.opportunities = opportunities

  def bio(self):
    print("\n")
    print("In my own personal SWOT analysis:")
    print(f"My strengths are {self.strengths} \n")
    print(f"My weaknesses are {self.weaknesses} \n")
    print(f"My threats are {self.threats} \n")
    print(f"My opportunities is {self.opportunities} \n")

mydul = SWOT_analysis("optimistic, punctuality, energetic, open to new ideas, team player", "straightforward, sensitive, impatient, introvert", "constantly growing industry, overworking", "networking")

mydul.bio()
