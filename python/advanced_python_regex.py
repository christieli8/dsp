import csv

D = {}
T = {}
E = []
with open("/Users/christieli/Desktop/pre-work/dsp/python/faculty.csv", "rb") as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    degrees = row[" degree"].split()
    for d in degrees:
      key = d.lower().replace(".", "")
      if key not in D:
        D[key] = {
          "name": d,
          "count": 0
        }
      D[key]["count"] += 1
      
    title = row[" title"]
    if title not in T:
      T[title] = 0
    T[title] += 1
    
    email = row[" email"]
    E.append(email)

for key in D:
  print "%s: %d" % (D[key]["name"], D[key]["count"])
print

for key in T:
  print "%s: %d" % (key, T[key])
print

for e in E:
  print e
print

domains = set()
for e in E:
  tokens = e.split("@")
  domains.add(tokens[1])
print len(domains)
for d in domains:
  print d
print
