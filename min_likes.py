import requests
import urllib
from constants import APP_ACCESS_TOKEN, BASE_URL
from get_user_id import get_user_id
posts_likes = []
def min_likes(insta_username):
    #function logic
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()

    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url for user post : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            for post in user_media['data']:
                posts_likes.append(post['likes']['count'])
            index = posts_likes.index(min(posts_likes))
            print ("Post with id %s has minimum likes. \n This post has %d likes") % (user_media['data'][index]['id'],user_media['data'][index]['likes']['count'])

        else:
            print "There is no recent post!"
    else:
        print 'Status code other than 200 received!'
