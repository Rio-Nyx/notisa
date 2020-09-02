import json
def jsonload(key,value):
	with open("config.json", "r") as files:
		json_data = json.load(files)
		print(json_data[key])
		json_data[key]=value				
	with open('config.json', 'w') as file:
		json.dump(json_data, file, indent=2)
def jsonread():
	with open("config.json", "r") as files:
		json_data = json.load(files)
	return json_data
def jsonchange(settings):
	with open('config.json', 'w') as files:			
		#json.dump(settings, file, indent=2)
		json.dump(settings, files)
#jsonload("background","red")
