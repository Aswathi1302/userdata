import requests
import json
import mysql.connector
import sys
try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database=' userdatadb')
except mysql.connector.Error as e:
    sys.exit("db connection error")
mycursor=mydb.cursor() 
data=requests.get("https://reqres.in/api/users?page=1").text
data_info=json.loads(data)
print(data_info)

datainf=data_info["data"]
for i in datainf:
    id=str(i['id'])
    sql="INSERT INTO `userdata`(`id`, `email`, `first_name`, `last_name`, `avatar`)  VALUES (%s,%s,%s,%s,%s)"
    data=(i['id'],i['email'],i['first_name'],i['last_name'],i['avatar'])
    mycursor.execute(sql,data)
    mydb.commit()
    print("data inserted success",i['id'])
