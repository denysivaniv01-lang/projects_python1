vov={"name": "Adam","age": 15}
print(vov["name"])
print(vov.get("age"))
vov.update({"food":"Apple"})
print(vov)


for key,values in vov.items():
    print(key,values,sep="-")
print("\n")
for val in vov.values():
    print(val)

