# main file.
from get_own_post import get_own_post
from get_user_id import get_user_id
from get_user_info import get_user_info
from get_users_post import get_users_post
from self_info import self_info
from constants import APP_ACCESS_TOKEN, BASE_URL
from like_a_post import like_a_post
from post_a_comment import post_a_comment
from delete_negative_comments import delete_negative_comment

#main program
insta_username = raw_input("Enter the username of the user: ")
while True:
    choice = raw_input("Enter you choice:\n1.gey self information \n2.get own post \n3.get user's information \n4.get user's id \n5.get user's post \n6.like the post \n7.post a comment \n8.delete negative comments")
    choice = int(choice)
    if choice == 1:
        self_info()
    elif choice == 2:
        get_own_post()
    elif choice == 3:
        get_user_info(insta_username)
    elif choice == 4:
        get_user_id(insta_username)
    elif choice == 5:
        get_users_post(insta_username)
    elif choice == 6:
        like_a_post(insta_username)
    elif choice == 7:
        post_a_comment(insta_username)
    elif choice == 8:
        delete_negative_comment(insta_username)
    else:
        print("wrong choice")
        exit()