import json


with open("DegreeTemplates.json", "r") as read_file:
    data = json.load(read_file)

# variable to store majors into another file
majors = []

# parse majors from json file and store them by major

'''
What's the best way to find the school that a major belongs to?
Maybe hard code since there's no straightforward way to find this
Some weird stuff on line 2585 of json file with Physician-Scientist Major

'''
for degree in data:
	tmp = {}
	
	# keep major name
	tmp["Major"] = degree["Major"]
	
	# add courses by year and separate by fall and spring semester
	# Year 1
	tmp["First Year"] = []
	sem1 = []
	for course in degree["Y1S1"]:
		if course == "Fall":
			continue
		course_name = course.split("Course: ")
		if len(course_name) > 1:
			sem1.append(course_name[1])
		else:
			sem1.append(course)
	tmp["First Year"].append(sem1)

	sem2 = []
	for course in degree["Y1S2"]:
		if course == "Spring":
			continue
		course_name = course.split("Course: ")
		if len(course_name) > 1:
			sem2.append(course_name[1])
		else:
			sem2.append(course)
	tmp["First Year"].append(sem2)


	# Year 2
	tmp["Second Year"] = []
	sem1 = []
	for course in degree["Y2S1"]:
		if course == "Fall":
			continue
		course_name = course.split("Course: ")
		if len(course_name) > 1:
			sem1.append(course_name[1])
		else:
			sem1.append(course)
	tmp["Second Year"].append(sem1)

	sem2 = []
	if "Y2S2" in degree.keys():	
		for course in degree["Y2S2"]:
			if course == "Spring":
				continue
			course_name = course.split("Course: ")
			if len(course_name) > 1:
				sem2.append(course_name[1])
			else:
				sem2.append(course)
		tmp["Second Year"].append(sem2)
	else:
		print(degree["Major"])
		
	# Year 3
	if "Y3" in degree.keys():
		
		tmp["Third Year"] = []
		sem1 = []
		for course in degree["Y3S1"]:
			if course == "The Arch Semester" or course == "Fall":
				continue
			course_name = course.split("Course: ")
			if len(course_name) > 1:
				sem1.append(course_name[1])
			else:
				sem1.append(course)
		tmp["Third Year"].append(sem1)

		sem2 = []
		for course in degree["Y3S2"]:
			if course == "Spring":
				continue
			course_name = course.split("Course: ")
			if len(course_name) > 1:
				sem2.append(course_name[1])
			else:
				sem2.append(course)
		tmp["Third Year"].append(sem2)
	else:
		print(degree["Major"])

	# Year 4
	if "Y4" in degree.keys():
		tmp["Fourth Year"] = []
		sem1 = []
		for course in degree["Y4S1"]:
			if course == "Fall" or course == "The Arch Semester":
				continue
			course_name = course.split("Course: ")
			if len(course_name) > 1:
				sem1.append(course_name[1])
			else:
				sem1.append(course)
		tmp["Fourth Year"].append(sem1)

		sem2 = []
		for course in degree["Y4S2"]:
			if course == "Spring":
				continue
			course_name = course.split("Course: ")
			if len(course_name) > 1:
				sem2.append(course_name[1])
			else:
				sem2.append(course)
		tmp["Fourth Year"].append(sem2)
	else:
		print(degree["Major"])

	majors.append(tmp)


with open("Majors.json", "w") as write_file:
	json.dump(majors, write_file, sort_keys=False, indent=2, ensure_ascii=False)


