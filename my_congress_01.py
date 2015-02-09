
import json

f = open("congress.json","r")
content = f.read()
jsondata = json.loads(content)

print("The type of the data is: ",type(jsondata["results"][0]["members"]))
print("And it is a list of ",type(jsondata["results"][0]["members"][0]))

members = set()

for items in jsondata["results"][0]["members"]:

    members.add(items["id"])

print("The total number of members are: ",len(members))

