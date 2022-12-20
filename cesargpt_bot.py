import tweepy
import openai

# Replace these with your own Twitter API keys and secrets
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

# Replace this with your own GPT-3 API key
openai.api_key = ""
openai.organization = ""

# Set up the Twitter API client
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_key, access_secret)
api = tweepy.API(auth)

# Fetch the user's tweets
user = "saposabao"
tweets = api.user_timeline(screen_name=user, count=1)



# Prompt the tweets at the GPT-3 API and get the responses
for tweet in tweets:
    print("Último tweet: " + tweet.text)
    last_tweet = tweet.id
    print(last_tweet)
    toprompt = tweet.text
    response = openai.Completion.create(model="text-davinci-003", prompt= "Ignorar termos iniciando com @, não usar aspas, responder de forma curta e sarcástica para a frase:" + toprompt, temperature=0, max_tokens=80, top_p=1, frequency_penalty=0.0, presence_penalty=0.0 )
    print(response["choices"][0]["text"])
    compose_tweet = response["choices"][0]["text"]
    # Post the response tweet as a reply to the original tweet
    api.update_status(status=compose_tweet, in_reply_to_status_id=last_tweet, auto_populate_reply_metadata =True)