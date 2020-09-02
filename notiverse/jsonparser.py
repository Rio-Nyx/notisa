import json

def jsonread():
	with open("config.json", "r") as files:
		json_data = json.load(files)
	return json_data
def jsonchange(settings):
	with open('config.json', 'w') as files:			
		json.dump(settings, files)
