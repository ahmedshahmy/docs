import pyrebase
import csv

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
auth=firebase.auth()
usr="maa.shahmy@gmail.com"
passwd="19880113"
user = auth.sign_in_with_email_and_password(usr, passwd)

#db.child("Creat").remove(user['idToken'])

power = input("Enter RU to remove duplicates:")

patients = db.child("Creat").order_by_child(
        "RU").equal_to(power).get(user['idToken'])
i=0
for p in patients.each():
    i+=1
    ikey=p.key()
    if i>1:
        db.child("Creat").child(ikey).remove(user['idToken'])
        print("data removed")
    else:
        print("No duplicates")