import csv

faculty_dict = {}
with open("/Users/christieli/Desktop/pre-work/dsp/python/faculty.csv", "rb") as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    name = row["name"]
    tokens = name.split()

    last_name = tokens[-1]
    if last_name not in faculty_dict:
      faculty_dict[last_name] = []
    
    faculty_dict[last_name].append([
      row[" degree"].strip(),
      row[" title"].strip(),
      row[" email"].strip()
    ])
keys = faculty_dict.keys()
for key in keys[:3]:
  print key, faculty_dict[key]
print

professor_dict = {}
with open("/Users/christieli/Desktop/pre-work/dsp/python/faculty.csv", "rb") as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    name = row["name"]
    tokens = name.split()

    first_name = tokens[0]
    last_name = tokens[-1]
    key = (first_name, last_name)
    if key not in faculty_dict:
      professor_dict[key] = []
    
    professor_dict[key].append([
      row[" degree"].strip(),
      row[" title"].strip(),
      row[" email"].strip()
    ])
keys = professor_dict.keys()
for key in keys[:3]:
  print key, professor_dict[key]
print

keys = professor_dict.keys()
keys.sort(key=lambda name: name[1])
for key in keys[:3]:
  print key, professor_dict[key]
print
