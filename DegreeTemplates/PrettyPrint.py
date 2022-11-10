import json

with open("DegreeTemplates.json", "r") as read_file:
    data = json.load(read_file)

# variable to store majors into another file
majors = []

for degree in data:
	majors.append(degree)

with open("DegreeTemplates2.json", "w") as write_file:
	json.dump(majors, write_file, sort_keys=False, indent=2, ensure_ascii=False)