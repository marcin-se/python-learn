import os, sys, pickle, json, sys, pathlib
from library.py11pliki import Mod

# file_content.encode("utf-8")
# file_content.decode("utf-8")


working_list =

with open("fort_escort.csv") as file:
	reader = csv.reader(file)
	for line in reader:
		file_content.append(line)


file_content[2][1] = 27

print(file_content)

with open("fort_escort_2.csv", "w", newline="") as file:
	writer = csv.writer(file)
	for line in file_content:
		writer.writerow(line)
		
line_count = 0




# BARTEK - python reader.py deniro.csv deniro2.csv

# zadanie - python reader.py deniro.csv deniro2.csv 10,1,2030 11,1,2040

with open(argv[1]) as file:
	reader = csv.reader(file)
	for line in reader:
		file_content.append(line)
		
print(file_content)

with open(argv[2], "w", newline="") as file:
	writer = csv.writer(file)
	for line in file_content:
		writer.writerow(line)

for param in argv[3:]:
	param_list = param.split(",")
	file_content[int(param_list[0])-1][int(param_list[1])-1] = int(param_list[2])


with open(argv[2], "w") as file:
	print(json.dumps(file_content))
	file_content_json = json.dumps(file_content)
	file.write(file_content_json)
