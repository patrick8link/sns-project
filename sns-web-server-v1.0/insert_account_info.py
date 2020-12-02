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
                host="10.0.0.35",
                user="root",
                password="123456qwer!",
                database="snsDB",
                use_unicode=True,
                charset="utf8mb4"
            )
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO business_discovery (username, name, ig_id, profile_picture_url, follows_count, followers_count, media_count, id) VALUES (
                                  %s,%s,%s,%s,%s,%s,%s,%s);
                                """
        mySql_data = (username, name, ig_id, profile_picture_url, follows_count, followers_count, media_count, id)
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
                host="10.0.0.35",
                user="root",
                password="123456qwer!",
                database="snsDB",
                use_unicode=True,
                charset="utf8mb4"
            )
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO media (id, comments_count, like_count, media_url, permalink, timestamp, username, ig_id) VALUES (
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
            
with open('awesomehaeun-data.json') as f:
    data = json.load(f)
    
# =============================================================================
# datajson=open("data.json","w")
# datajson.write(json.dumps(data, indent=4, sort_keys=True))
# datajson.close()
#     
# print (json.dumps(data,sort_keys=True,indent=4))
# =============================================================================

username = data["business_discovery"]["username"]
name = data["business_discovery"]["name"]
ig_id = data["business_discovery"]["ig_id"]
profile_picture_url = data["business_discovery"]["profile_picture_url"]
follows_count = data["business_discovery"]["follows_count"]
followers_count = data["business_discovery"]["followers_count"]
media_count = data["business_discovery"]["media_count"]
id = data["business_discovery"]["id"]



#insertAccountIntoTable(username, name, ig_id, profile_picture_url, follows_count, followers_count, media_count, id)

