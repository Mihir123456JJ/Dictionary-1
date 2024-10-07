student_data= {
"idi1":{
    "Name":"Dev",
    "ID":"St#$342sdfa",
    "Grade":2,
    "Student":True,
    "Course":["Math","Science 1","English 5"]   
},
"idi2":{
    "Name":"Mihir",
    "ID": "DTR#$56277dass",
    "Grade":4,
    "Student":True, 
    "Course":["Biology 2","Math 7","English 1"]
}
}
res={}
for key,value in student_data.items():
    if value not in res.values():
        res[key]=value
print(res)        
