# Account should have Two-factor authentication off in account which you want to access

import getpass
import instaloader

def do_process(username, password):
    loader = instaloader.Instaloader()

    # Login
    loader.login(username, r"{}".format(password))

    # Obtain profile metadata
    profile = instaloader.Profile.from_username(loader.context, username)

    # List of followers
    followers = profile.get_followers()

    # List of followees
    followees = profile.get_followees()

    # List of accounts which you are following but didn't get follow-back
    list_of_followees_objects = list(set(followees) - set(followers))
    list_of_followees = [followee.username for followee in list_of_followees_objects]

    with open('followees.txt', 'w') as f:
        followees_count = 0
        for followee in list_of_followees:
            f.write("%s\n" % followee)
            followees_count += 1

    print("Total followees which are not following back to this account: ", followees_count)

def main():
    USER_NAME = input("Please enter your Instagram account's user name: ")
    PASSWORD = getpass.getpass(prompt="Please enter your Instagram account's password: ")
    do_process(USER_NAME, PASSWORD)

try:
    main()
except Exception:
    print("Something went wrong! Please try again with valid credentials.")
