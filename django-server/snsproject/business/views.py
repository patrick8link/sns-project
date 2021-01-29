from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template import loader
from django.urls import reverse

import mysql.connector
from . import get_account_info as getAcc
# Create your views here.

def search_id(request,search_id):
        try:
                resultURL=[]
                resultLike=[]
                resultPerma=[]
                for data in getAcc.getHighestLikeFromMedia("media_url,like_count,permalink",search_id):
                        media_url,like,permalink = data
                        resultURL.append(media_url)
                        resultLike.append(like)
                        resultPerma.append(permalink)
                username, name,profile_picture_url,follows_count,followers_count=getAcc.getAccountFromTable("username, name,profile_picture_url,follows_count,followers_count",search_id)
                context = {
                        'username': username,
                        'name': name,
                        'profile_picture_url': profile_picture_url,
                        'follows_count': follows_count,
                        'followers_count': followers_count,
                        'like_count': resultLike,
                        'mediaURL': resultURL,
                        'permalink': resultPerma
                }
                return HttpResponse(render(request,'account_data.html',context))
        except:
                return HttpResponseNotFound("Error 404 Not Found for {}".format(search_id))
