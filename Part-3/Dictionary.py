thisdict = {"id" : 100, "name" : "Saman", "salary" : 50000.0}

print(thisdict)
print(type(thisdict))

print(thisdict["id"])
print(thisdict["name"])
print(thisdict["salary"])

 #another collection
thisdict["address"] = {"no" : 51, "street" : "1st lane", "town" : " Kandy"}
print(thisdict)

thisdict["mobile"] = ["0764534432", "0712353466"]
print(thisdict)

print(thisdict["address"])
print(thisdict["address"]["town"])

print(thisdict["mobile"][1])