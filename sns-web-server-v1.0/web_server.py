# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:42:55 2020

@author: Patrick
"""

from flask import Flask, request, render_template, redirect, url_for, jsonify, send_file
import requests
import json
import get_account_info as getAcc

app = Flask(__name__)

@app.route("/")
def form():
	return render_template('my-form.html')

@app.route("/",methods=['POST'])
def form_post():
    usernameText = request.form['usernameText']
    return redirect(url_for('get_account_data',username=usernameText))

@app.route("/account/<username>", methods=['GET'])
def get_account_data(username):
    try:
        resultURL=[]
        resultLike=[]
        resultPerma=[]
        for data in getAcc.getHighestLikeFromMedia("media_url,like_count,permalink",username):
            media_url,like,permalink = data
            resultURL.append(media_url)
            resultLike.append(like)
            resultPerma.append(permalink)
        name,profile_picture_url,follows_count,followers_count=getAcc.getAccountFromTable("name,profile_picture_url,follows_count,followers_count",username)
        return render_template('account_data.html',
                                profile_picture_url=profile_picture_url,
                                username=username, 
                                name=name,
                                followers_count=followers_count,
                                follows_count=follows_count,
                                like_count=resultLike,
                                mediaURL=resultURL,
                                permalink=resultPerma
                                )
    except:
        return render_template('error.html')
    
@app.route("/account/<username>",methods=['POST'])
def go_home():
    return redirect(url_for('my-form.html'))
    
@app.route('/favicon.ico') 
def favicon(): 
    return render_template('my-form.html')

@app.route("/accountImg", methods=['GET'])
def get_avatar():
    return send_file('img_avatar.png', mimetype='image/gif')

@app.route("/test/<username>", methods=['GET'])
def multiple_pic(username):
    resultURL=[]
    resultLike=[]
    for data in getAcc.getHighestLikeFromMedia("media_url,like_count"):
        media_url,like = data
        resultURL.append(media_url)
        resultLike.append(like)
    return render_template('multi-pic.html', like_count=resultLike, mediaURL=resultURL)

if __name__ == '__main__':
	app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
	app.run(host='10.0.0.26',port=80)

