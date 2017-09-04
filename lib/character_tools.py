import random

from base_tools import *

def roll_upp():
  return [roll_2d6() for _ in range(6)]

def set_gender():
  return random.choice(['M', 'F'])

def set_age(terms):
  return 18 + (terms * 4) + int((roll_1d6() / 2))

def set_career():
  return random.choice(['Army', 'Navy', 'Marines', 'Scouts',
    'Agent', 'Merchant', 'Citizen', 'Rogue'])

def roll_terms():
  return roll_1d6()

def set_name(gender):
  if gender == 'F':
    f_names = ['Vega', 'Gabbie', 'Giselle', 'Lanny', 'Ilana', 'Alba', 'Irene']
  else:
    f_names = ['Marco', 'Ian', 'Akil', 'Alan', 'Wilbur']
  f_name = random.choice(f_names)
  l_names = ['Domici', 'Stranger', 'Smith', 'Jones', 'Patterson']
  l_name = random.choice(l_names)
  return f_name + " " + l_name

def show_upp(upp):
  return ''.join('%X' % u for u in upp)

def set_skills(career, terms):
  skills = {}
  if career in ['Army', 'Marines']:
    skill_list = ['GunCbt', 'VaccSuit', 'Leadership', 'Vehicle']
  elif career in ['Merchant', 'Navy', 'Scout']:
    skill_list = ['Navigation', 'Pilot', 'Engineering', 'Computer']
  else:
    skill_list = ['Blade', 'GunCbt', 'Admin', 'Streetwise']

  for add_skill in range(terms * 2): 
    new_skill = random.choice(skill_list)
    if new_skill in skills:
      skills[new_skill] += 1
    else:
      skills[new_skill] = 1 

  return skills
    

