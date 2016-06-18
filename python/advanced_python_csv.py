import csv

outfile = open("/Users/christieli/Desktop/pre-work/emails.csv", "w")
with open("/Users/christieli/Desktop/pre-work/dsp/python/faculty.csv", "rb") as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    email = row[" email"]
    outfile.write(email + "\n")
outfile.close()

