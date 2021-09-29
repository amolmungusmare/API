import json,requests,os
sr,crsnamea,Identy=[],[],[]
if os.path.exists("course.json"):
    with open('course.json') as love:
        c=json.load(love)
    for i in range(len(c["availableCourses"])):
        print(i,c["availableCourses"][i]["name"],c["availableCourses"][i]["id"])
        sr.append(i),crsnamea.append(c["availableCourses"][i]["name"]),Identy.append(c["availableCourses"][i]["id"])
else:
    a=requests.get('http://saral.navgurukul.org/api/courses')
    z=a.json()
    with open('course.json','w') as love:
        c=json.dump(z,love,indent=2)
    for i in range(len(z["availableCourses"])):
        print(i,z["availableCourses"][i]["name"],z["availableCourses"][i]["id"])
        sr.append(i),crsnamea.append(z["availableCourses"][i]["name"]),Identy.append(z["availableCourses"][i]["id"])
inputsr=int(input('enter course serial number '))
print('your parent course is ',crsnamea[inputsr])
containerofcoursename=crsnamea[inputsr]
nd_file=containerofcoursename+'.json'
love.close()
a=requests.get('http://saral.navgurukul.org/api/courses/'+Identy[inputsr]+'/exercises')
b=a.json()
with open(nd_file ,"w") as c:
    json.dump(b,c,indent=4)
incre=1 
slug={}
akash={}
for y in b["data"]:
    print(str(incre),y["name"])
    decre=1
    akash[str(incre)]=y["slug"] 
    for k2 in y["childExercises"]:
        print("    "+str(incre)+"."+str(decre)," "+k2["name"])
        slug[str(incre)+"."+str(decre)]=k2["slug"]
        akash[str(incre)+"."+str(decre)]=k2["slug"]
        decre+=1
    incre+=1
user2=input("enter the num:-")
l=requests.get(f"http://saral.navgurukul.org/api/courses/{Identy[inputsr]}/exercise/getBySlug?slug={akash[user2]}")
c=l.json()
filename=akash[user2]
file=str(filename)+'.json'
with open(file,"w") as n:
    json.dump(c,n,indent=4)
data=c["content"]
main_data=json.loads(data)
for x in main_data:
    for y in x:
        co=x["value"]
    print(co)
