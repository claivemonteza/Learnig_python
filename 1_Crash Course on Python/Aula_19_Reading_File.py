file = open("spider.txt")
print(file.readline())

print(file.read())
file.close()

##when use with no need to write file.close will close when is finish
with open("spider.txt") as file:
    print(file.readline())


with open("spider.txt") as file:
    for line in file:
        print(line.upper())

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())


## r for read only
## w write only
## a append
## r+ read-write
with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")


 import os
 os.remove("novel.txt")


os.rename("first_draft.txt", "finished_masterpiece.txt")

 os.path.exists("finished_masterpiece.txt")
 os.path.exists("userlist.txt")

os.path.getmtime("spider.txt")
#This code will provide a unix timestamp for the file

import datetime
timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)
#This code will provide the date and time for the file in an 
#easy-to-understand format

os.path.abspath("spider.txt")
#This code takes the file name and turns it into an absolute path

#Read on csv file
import csv
 f = open("csv_file.txt")
 csv_f = csv.reader(f)
 for row in csv_f:
     name, phone, role = row
     print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()

#Write on csv file
import csv

hosts = [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

#the following command should be used in the terminal
cat software.csv 
#Output name,version,status,users
#MailTree,5.34,production,324
#CalDoor,1.25.1,beta,22
#Chatty Chicken,0.34,alpha,4

with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
      print(("{} has {} users").format(row["name"], row["users"]))


users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)      