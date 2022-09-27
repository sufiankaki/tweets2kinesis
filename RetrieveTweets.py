import boto3
import json
import tweepy
import uuid

bearer_key = 'INSERT YOUR BEARER KEY HERE'

kinesis_stream_name = 'kds-twitter-sda'
twitter_filter_tag = '#sports lang:en'


class StreamingTweets(tweepy.StreamingClient):
    def on_tweet(self, status):
        pass
        
    
    def on_data(self, data):
        status = json.loads(data.decode("utf-8"))
        #print(json.dumps(status, indent=4, sort_keys=True))
        data = {
            'tweet_id': status['data']['id'],
            'tweet_text': status['data']['text'],
            'user_id': status['includes']['users'][0]['id'],
            'user_name': status['includes']['users'][0]['name'],
            'user_username': status['includes']['users'][0]['username']
        }
        #print(json.dumps(data, indent=4, sort_keys=True))
        
        response = kinesis_client.put_record(
            StreamName=kinesis_stream_name,
            Data=json.dumps(data),
            PartitionKey=partition_key)

        print('Status: ' +
              json.dumps(response['ResponseMetadata']['HTTPStatusCode']))
        
        
    def on_error(self, status):
        print(status)


session = boto3.Session()
kinesis_client = session.client('kinesis')
partition_key = str(uuid.uuid4())

stream = StreamingTweets(bearer_key)
stream.add_rules(tweepy.StreamRule(twitter_filter_tag))
stream.filter(expansions=['author_id', 'in_reply_to_user_id', 'geo.place_id'])

