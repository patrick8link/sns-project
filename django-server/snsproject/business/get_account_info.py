# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 17:33:59 2020
@author: Patrick
"""

import mysql.connector
import json

            
#GET ACCOUNT INFORMATION FROM TABLE <DATABASE NAME = snsDB, TABLE NAME = business_discovery>
def getAccountFromTable(key,value):
    try:
        connection = mysql.connector.connect(
                host="10.0.0.35",
                user="root",
                password="123456qwer!",
                database="snsDB"
            )
        cursor = connection.cursor()
        #print ("SELECT %s FROM business_discovery WHERE username = '%s'" % (key, value))
        cursor.execute("SELECT %s FROM business_discovery WHERE ig_id = '%s'" % (key, value))
        result = cursor.fetchone()
        return result
    except mysql.connector.Error as error:
        print("Failed to connect to MySQL {}".format(error))
    finally:
         if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            

def getMediaFromTable(key,value):
    try:
        connection = mysql.connector.connect(
                host="10.0.0.35",
                user="root",
                password="123456qwer!",
                database="snsDB"
            )
        cursor = connection.cursor()
        #print ("SELECT %s FROM media WHERE username = '%s'" % (key, value))
        cursor.execute("SELECT %s FROM media WHERE ig_id = '%s'" % (key, value))
        result = cursor.fetchone()
        return result
    except mysql.connector.Error as error:
        print("Failed to connect to MySQL {}".format(error))
    finally:
         if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            
def getHighestLikeFromMedia(key,value):
    try:
        connection = mysql.connector.connect(
                host="10.0.0.35",
                user="root",
                password="123456qwer!",
                database="snsDB"
            )
        cursor = connection.cursor()
        #print ("SELECT %s FROM media WHERE username = '%s'" % (key, value))
        cursor.execute("SELECT %s FROM media WHERE ig_id = '%s' ORDER BY like_count DESC LIMIT 3" % (key, value))
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as error:
        print("Failed to connect to MySQL {}".format(error))
    finally:
         if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
