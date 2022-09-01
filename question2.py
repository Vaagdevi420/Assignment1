dog = dict () 
dog["name"] = "chotu",
dog["color"] = "brown",
dog["breed"] ="lab",
dog["legs"] = "4",
dog["age"]  = "2"
student = {
"first_name" : "Vaagdevi",
"last_name" : "Suryadevara",
"gender" : "Female",
"age" : "23",
"marital status": "Single" ,
"skills" : ["reading","writing","eating"],
"country":"India",
"city" : "Guntur",
"address" : "**"
}
print(len(student))
x = student.get("skills")
print(x)
print(type(x))
student['skills']+=['singing']
print(student)
print(list(student.keys()))
print(list(student.values()))
