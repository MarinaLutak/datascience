import re

pattern_provider_id=re.compile(r"\d+$")
pattern_city=re.compile(r"[a-zA-Z -]+$")
pattern_total_lupa_episodes=re.compile(r"\d+$")
pattern_average_age=re.compile(r"\d+$")

def provider_id_validator(pattern_provider_id, prompt):
	number=int(validator(pattern_provider_id, prompt))
	while number<=0:
		number=int(validator(pattern_provider_id, prompt))
	return number

def validator(pattern, prompt):
	data=input(prompt)	
	while not bool (pattern.match(data)):
		data=input(prompt)
	return data

def city_validator(pattern_city, prompt):
	name=(validator(pattern_city, prompt))
	return name

def total_lupa_episodes_validator(pattern_total_lupa_episodes, prompt):
	number=int(validator(pattern_total_lupa_episodes, prompt))
	while number<=0:
		number=int(validator(pattern_total_lupa_episodes, prompt))
	return number

def average_age_validator(pattern_average_age, prompt):
	age=int(validator(pattern_average_age, prompt))
	while age<=0:
		age=int(validator(pattern_average_age, prompt))
	return age










