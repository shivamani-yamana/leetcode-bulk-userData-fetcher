import requests
import csv

def getProfile(username):
    url = f'https://alfa-leetcode-api.onrender.com/userProfile/{username}'
    response = requests.get(url)
    return response.json()
    
def getBadges(username):
    url = f'https://alfa-leetcode-api.onrender.com/{username}/badges'
    response = requests.get(url)
    return response.json()
    
usernames = []
usersData = []
with open("users_list.txt","r") as fileInput :
    for line in fileInput:
        usernames.append(line.rstrip('\n'))
print(usernames)

for user in usernames:
    profileData = getProfile(user)
    badgesData = getBadges(user)
    record = {}
    record["Username"] = user
    record["Rating"] = profileData["ranking"]
    record["Problems Solved"] = profileData["totalSolved"]
    badges = ",".join([i["displayName"] for i in badgesData["badges"]])
    record["Badges"]=badges
    usersData.append(record)

with open('user_data.csv','w',newline='') as csvFile:
    fieldNames = ["Username","Rating","Problems Solved","Badges"]
    writer = csv.DictWriter(csvFile,fieldnames=fieldNames)
    writer.writeheader()
    writer.writerows(usersData)