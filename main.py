#Max Onkst
import const
import tweepy
from tweepy import Stream


# A listener handles tweets that are received from the stream.
# This is a basic listener that prints recieved tweets to standard output
class TweetListener(Stream):
    def onData(self, data):  # return data
        print(data)
        return True

    def onError(self, status):  # return status on error
        print(status)


def main():
    auth = tweepy.OAuthHandler(const.CONSUMER_KEY, const.CONSUMER_SECRET)
    auth.set_access_token(const.ACCESS_TOKEN, const.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    try:
        api.verify_credentials()
        print('Verification Successful.')
    except:
        print('Authentication Error.')
    twitterStream = Stream(const.CONSUMER_KEY, const.CONSUMER_SECRET, const.ACCESS_TOKEN, const.ACCESS_TOKEN_SECRET)
    users = api.lookup_users(screen_name={"Youtube", "Meta"})

    print("\nTask 1:")
    for user in users:
        print("\nUser name: ", user.name)
        print("Screen name: ", user.screen_name)
        print("User ID: ", user.id)
        print("Location: ", user.location)
        print("User description: ", user.description)
        print("Follower count: ", user.followers_count)
        print("Friend count: ", user.friends_count)
        print("Tweet count: ", user.statuses_count)
        print("url: ", user.url)
    print("------------------------------------------------------")
    print("Task 2\n")
    #To crawl through more users, add them to the 'names' list below
    names = {"juicyfruitsnacc"}
    for name in names:
        counter1 = 0
        counter2 = 0
        print("\nScreen name: ", name)
        for user in tweepy.Cursor(api.get_friends, screen_name=name).items():
            if(counter1 == 0):
                print("\nFriends:\n")
            counter1 = counter1 + 1
            print(user.screen_name)
            if counter1 >= 20:
                break

        for user in tweepy.Cursor(api.get_followers, screen_name=name).items():
            if(counter2 == 0):
                print("\nFollowers:")
            counter2 = counter2 + 1
            print(counter2,': ', user.screen_name)
            if counter2 >= 20:
                break
    print("--------------------------------------------------")
    print("Task 3a")
    counter4 = 0
    for tweet in tweepy.Cursor(api.search_tweets, q = ["Ohio", "weather"]).items():
        counter4 = counter4 + 1
        print("\nTweet ",counter4,":\n")
        print(tweet.text)
        if(counter4 == 50):
            break

    print("-------------------------------------------------------")
    print("Task 3b\n")
    counter5 = 0
    for tweet in tweepy.Cursor(api.search_tweets, q="",geocode='39.758949,-84.191605,25mi').items():
        counter5 = counter5 + 1
        print("\nTweet ",counter5,":\n")
        print(tweet.text)
        if(counter5 == 50):
            break

    print("-------------------------------------------------------")
    print("Task 4\n")

    test = {"nevabraxt", "ricklevr", "sauceddie", "Meta", "Youtube", "Nasa"}
    counter6 = 0
    list = []
    avglist = []
    accounts = api.lookup_users(screen_name=test)
    for account in accounts:
        tweets = account.statuses_count
        followers = account.followers_count
        avg = round(followers/tweets, 1)
        list.append(account.name + ": " + str(avg))
        avglist.append(avg)
        counter6 = counter6 + 1

    max = 0
    maxindex = 0
    score = 1
    print("Followers Per Tweet:\n")
    while len(avglist) > 0:
        for obj in avglist:
            if obj > max:
                max = obj
                maxindex = avglist.index(max)
        print(score, ". ",list[maxindex])
        del list[maxindex]
        del avglist[maxindex]
        max = 0
        score = score + 1

    return  # end main


# call main()
if __name__ == '__main__':
    main()
