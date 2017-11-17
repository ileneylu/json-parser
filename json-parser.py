# Description: python script for parsing patient.json and create output.html
# Author: Ilene Lu

#! /usr/bin/python

import json

with open('patient.json', 'r') as fp:
    obj = json.load(fp)

givenName = obj["name"][0]["given"][0]
familyName = obj["name"][0]["family"][0]
ogName = obj["managingOrganization"]["display"]
gender = obj["gender"]
numCond = 0
conditions = obj["conditions"]
for condition in conditions:
    numCond += 1

with open("output.html", "w") as output:
  output.write("<html><head></head><body>")
  output.write("<p>"),
  output.write("Name of Patient: " + givenName + " " + familyName),
  output.write("</p>")
  output.write("<p>"),
  output.write("Organization name: " + ogName),
  output.write("</p>")
  output.write("<p>"),
  output.write("Gender: " + gender),
  output.write("</p>")
  output.write("<p>"),
  output.write("Number of conditions they have: " + str(numCond)),
  output.write("</p>")
  output.write("<p>"),
  output.write("List of all conditions:"),
  output.write("</p>")
  for condition in conditions:
      output.write("<p>"),
      output.write("- " + condition),
      output.write("</p>")

  output.write("</body></html>")

output.close()
