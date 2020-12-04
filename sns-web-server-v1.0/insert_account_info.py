# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 18:10:45 2020

@author: Patrick
"""
import mysql.connector
import json

#INSERT ACCOUNT INFORMATION TO TABLE <DATABASE NAME = snsDB, TABLE NAME = business_discovery>
def insertAccountIntoTable(username, name, ig_id, profile_picture_url, follows_count, followers_count, media_count, id):
    try:
        connection = mysql.connector.connect(
                host="115.145.178.15",
                port="8081",
                user="root",
                password="123456qwer!",
                database="snsDB",
                use_unicode=True,
                charset="utf8mb4"
            )
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO business_discovery 
                                    (username, name, ig_id, profile_picture_url, follows_count, followers_count, media_count, id) 
                                VALUES 
                                    (%s,%s,%s,%s,%s,%s,%s,%s)
                                 ON DUPLICATE KEY UPDATE
                                    profile_picture_url = %s, follows_count = %s, followers_count = %s, media_count = %s
                                """
        mySql_data = (username, name, ig_id, profile_picture_url, follows_count, followers_count, media_count, id, profile_picture_url, follows_count, followers_count, media_count)
        cursor.execute(mySql_insert_query,mySql_data)
        connection.commit()
        print("Record inserted successfully into business_discovery table")
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
        
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def insertMediaIntoTable(id, comments_count, like_count, media_url, permalink, timestamp, username, ig_id):
    try:
        connection = mysql.connector.connect(
                host="115.145.178.15",
                port="8081",
                user="root",
                password="123456qwer!",
                database="snsDB",
                use_unicode=True,
                charset="utf8mb4"
            )
        cursor = connection.cursor()
        mySql_insert_query = """INSERT IGNORE INTO media (id, comments_count, like_count, media_url, permalink, timestamp, username, ig_id) VALUES (
                                  %s,%s,%s,%s,%s,%s,%s,%s);
                                """
        mySql_data = (id, comments_count, like_count, media_url, permalink, timestamp, username, ig_id)
        cursor.execute(mySql_insert_query,mySql_data)
        connection.commit()
        print("Record inserted successfully into media table")
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
        
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            

    
def insertHistoryintoTable(date, followers_count, follows_count, media_count, username):
    try:
        connection = mysql.connector.connect(
                host="115.145.178.15",
                port="8081",
                user="root",
                password="123456qwer!",
                database="snsDB",
                use_unicode=True,
                charset="utf8mb4"
            )
        cursor = connection.cursor()
        mySql_insert_query = """INSERT IGNORE INTO followers_history (date, followers_count, follows_count, media_count, username) VALUES (
                                  %s,%s,%s,%s,%s);
                                """
        mySql_data = (date, followers_count, follows_count, media_count, username)       
        cursor.execute(mySql_insert_query,mySql_data)
        connection.commit()
        print("Record inserted successfully into history table")
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
        
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")   

with open('19.json') as f:
    data = json.load(f)

# =============================================================================
# datajson=open("awesome-haeun.json","w")
# datajson.write(json.dumps(data, indent=4, sort_keys=True))
# datajson.close()
#     
# =============================================================================
#print (json.dumps(data,sort_keys=True,indent=4))

username = data["business_discovery"]["username"]
name = data["business_discovery"]["name"]
ig_id = data["business_discovery"]["ig_id"]
profile_picture_url = data["business_discovery"]["profile_picture_url"]
follows_count = data["business_discovery"]["follows_count"]
followers_count = data["business_discovery"]["followers_count"]
media_count = data["business_discovery"]["media_count"]
id = data["business_discovery"]["id"]
insertAccountIntoTable(username, name, ig_id, profile_picture_url, follows_count, followers_count, media_count, id)

media = data["business_discovery"]["media"]["data"]
for mediaData in media:
    media_id = mediaData["id"]
    comments_count = mediaData["comments_count"]
    like_count = mediaData["like_count"]
    media_url = mediaData["media_url"]
    permalink = mediaData["permalink"]
    timestamp = mediaData["timestamp"]
    media_username = mediaData["username"]
    insertMediaIntoTable(media_id, comments_count, like_count, media_url, permalink, timestamp, media_username, ig_id)

history = data["business_discovery"]["followers_history"]
for historyData in history:
    hist_followers_count = historyData["followers_count"]
    hist_date = historyData["date"]
    hist_follows_count = historyData["follows_count"]
    hist_media_count = historyData["media_count"]
    hist_username = username
    insertHistoryintoTable(hist_date, hist_followers_count, hist_follows_count, hist_media_count, username)



