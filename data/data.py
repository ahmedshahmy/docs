import pyrebase
import matplotlib.pyplot as plt

firebasConfig={
    'apiKey': "AIzaSyAyOKsYNnwrxwgmMy-7qQsT7QiYIcWF3-I",
    'authDomain': "renal-1e0ac.firebaseapp.com",
    'databaseURL': "https://renal-1e0ac.firebaseio.com",
    'projectId': "renal-1e0ac",
    'storageBucket': "renal-1e0ac.appspot.com",
    'messagingSenderId': "39709818947",
    'appId': "1:39709818947:web:8998d016a6d9e4ffa854f6",
    'measurementId': "G-1R80GQM1G8"
}

firebase=pyrebase.initialize_app(firebasConfig)
db=firebase.database()

#data={"name":"Me","age":20,"male":True}
#
# db.push(data)

"""


while True:

    cont=input("add data?")

    if cont=="y":

        name=input("Name:")
        age=input("Age:")
        male=input("Male:")

        data={"name":name,"age":age,"male":male}
        db.push(data)

    if cont=="n":
        break
"""

global x
global y
x=[]
y=[]
"""
while True:

    cont=input("add data?")

    if cont=="y":

        name=input("Name:")
        date=input("Date:")
        cr=input("Creatinine:")

        data={"name":name,"date":date,"Creatinine":cr}
        db.child("patients").push(data)

    if cont=="n":
        break
"""

patients=db.child("patients").order_by_child("name").equal_to("das").get()

for p in patients.each():
    
    
    #print(p.val()["date"])
    x.append(p.val()["date"])
    y.append(p.val()["Creatinine"])
   

plt.plot(x,y)
#plt.yscale("log")
plt.show()


