""" 
  Character, a shell class 
  It is used for generating totally new characters,
  updating partially completed characters,
  or as a standard interface for existing characters.
"""

import random
import sys
sys.path.append("lib")
from character_tools import *

class Character(object):

  def __init__(self, my_data = None):
    self.create_framework()

    if my_data == None:
      self.generate_basic()
    else:
      for k,v in my_data.items():
        setattr(self, k, v)
      self.fill_out_char(my_data)
  
  def create_framework(self):
    self.name     = ""
    self.upp      = []
    self.age      = 0
    self.gender   = ""
    self.careers  = {}
    self.skills   = {}
 
  def fill_out_char(self, my_data):
    self.gender   = my_data.get('gender', set_gender())
    self.upp      = my_data.get('upp', roll_upp())
    self.name     = my_data.get('name', set_name(self.gender))
    self.age      = my_data.get('age', 18)
    self.careers  = my_data.get('careers', {})
    self.skills   = my_data.get('skills', {})
 
  def generate_basic(self):
    self.gender   = set_gender()
    self.name     = set_name(self.gender)
    self.upp      = roll_upp()

  def run_career(self, career, terms = 0):
    """ Run a single career """
    self.career   = career
    if terms == 0:
      self.terms    = roll_terms()
    else:
      self.terms    = terms
    self.careers  = {self.career : self.terms}
    if hasattr(self, 'age'):
      pass
    else:
      self.age      = set_age(self.terms)
    self.skills   = set_skills(self.career, self.terms)

  def __str__(self):
    name    = self.name
    gender  = self.gender
    upp     = show_upp(self.upp)
    career_string = self.string_careers()
    skill_string  = self.string_skills()
    return ("%-20s %-10s [%s]\n  %s \n  %s" % 
      (name, upp, gender, career_string, skill_string))

  def display(self):
    print("%-15s %s [%s] Age: %d " % 
      (self.name, show_upp(self.upp), self.gender, self.age))
    career_line = self.string_careers()
    print(career_line)
    skill_line = self.string_skills()
    print(skill_line)
    print("")
  
  def string_careers(self):
    career_line   = ''
    career_keys   = list(self.careers.keys())
    career_keys.sort()
    for c in career_keys:
      career_line += c + " (" + str(self.careers[c]) + " terms) "
    return career_line
 
  def string_skills(self):
    skill_line = ''
    skill_keys = list(self.skills.keys())
    skill_keys.sort()
    for s in skill_keys:
      skill_line += s + '-' + str(self.skills[s]) + " "
    return skill_line

  def display_string(self):
    c_string = self.name + (" " * (20 - len(self.name)))
    c_string += show_upp(self.upp) + " "
    c_string += '[' + self.gender +']' + " Age: " + str(self.age)
    c_string += "\n  " + self.string_careers()
    c_string += "\n  " + self.string_skills()
    return c_string
