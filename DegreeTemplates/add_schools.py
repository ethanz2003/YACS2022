import json

with open("Data/DegreeTemplatesFormatted.json", "r") as read_file:
    data = json.load(read_file)

with open("Data/schools.json", "r") as read_file:
	schools = json.load(read_file)

output = []


# change the formatting of major data
for major in data:
	for key in major.keys():
		if isinstance(major[key], list):
			for i in range(len(major[key])):
				major[key][i] = major[key][i].replace("Course: ", "")
				major[key][i] = major[key][i].replace("Credit Hours: ", "| Credits: ")

# iterate through
for school in schools:
	schoolObj = {}
	schoolObj["School Name"] = school["School Name"]
	schoolObj["Majors"] = []
	for school_major in school["Majors"]:
		for major in data:
			if major not in schoolObj["Majors"] and major["Major"].find(school_major) != -1: #found the major
				if len(schoolObj["Majors"]) == 0:
					schoolObj["Majors"].append(major)
				else:
					prev = len(schoolObj["Majors"])
					for i in range(len(schoolObj["Majors"])):
						if major["Major"] < schoolObj["Majors"][i]["Major"]:
							schoolObj["Majors"].insert(i, major)
							break;
					if len(schoolObj["Majors"]) == prev:
						schoolObj["Majors"].append(major)
	output.append(schoolObj)

with open("Data/SchoolDegreeTemplates.json", "w") as write_file:
	json.dump(output, write_file, sort_keys=False, indent=2, ensure_ascii=False)

# issue with repeated majors in DegreeTemplates.json
# could look for repeated names and not do it or just repeat for multiple schools
# Specifically Design, Innovation, and Society/Mechanical Engineering template repeats
# Should be okay since this is a dual major between SoE and HASS