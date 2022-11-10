import json

with open("Data/DegreeTemplatesFormatted.json", "r") as read_file:
    data = json.load(read_file)

with open("Data/schools.json", "r") as read_file:
	schools = json.load(read_file)

output = []

# iterate through
for school in schools:
	for school_major in school["Majors"]:
		for major in data:
			if major["Major"].find(school_major) != -1: #found the major
				major["School"] = school["School Name"]
				output.append(major)

with open("Data/SchoolDegreeTemplates.json", "w") as write_file:
	json.dump(output, write_file, sort_keys=False, indent=2, ensure_ascii=False)
