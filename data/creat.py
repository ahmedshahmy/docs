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

with open('jancreat.csv') as csvfile:
    readCSV=csv.reader(csvfile,delimiter=',')
    i=0
    for row in readCSV:
        i+=1
        ru=row[0]
        creat=row[1]
        date=row[2]

        data={"RU":ru,"date":date,"Creatinine":creat}

        if(i%100==0):
            user = auth.refresh(user['refreshToken'])
        db.child("Creat").push(data,user['idToken'])
        print("added")
        print(i)