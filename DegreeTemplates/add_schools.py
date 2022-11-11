import json

with open("Data/DegreeTemplatesFormatted.json", "r") as read_file:
    data = json.load(read_file)

with open("Data/schools.json", "r") as read_file:
	schools = json.load(read_file)

output = []

# iterate through
for school in schools:
	schoolObj = {}
	schoolObj["School Name"] = school["School Name"]
	schoolObj["Majors"] = []
	for school_major in school["Majors"]:
		for major in data:
			if major["Major"].find(school_major) != -1: #found the major
				schoolObj["Majors"].append(major)
	output.append(schoolObj)

with open("Data/SchoolDegreeTemplates.json", "w") as write_file:
	json.dump(output, write_file, sort_keys=False, indent=2, ensure_ascii=False)

# issue with repeated majors in DegreeTemplates.json
# could look for repeated names and not do it or just repeat for multiple schools
# Specifically Design, Innovation, and Society/Mechanical Engineering template repeats
# Should be okay since this is a dual major between SoE and HASS