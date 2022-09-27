# Filter Tweets and Put them to AWS Kinesis Data Streams

This project deals with how you can retrieve tweets using Twitter API v2 using Tweepy and insert them into a Kinesis Data Stream. This work is built over the work you may find [here](https://towardsdatascience.com/how-to-create-a-dataset-with-twitter-and-cloud-computing-fcd82837d313)

While going through this above link, I realised it does not support Twitter API v2 so I made some changes to the code that you can find in `RetrieveTweets.py`

Additionally I also created a script to get the Stream records `GetRecords.py`

I executed these scripts on an EC2 instance to which I attached an **IAM Role** allowing it to have the following permissions
Kinesis
- Write
  - Put Records
- Read
  - Get Records
  - Describe Stream
  - Get Shard Iterator
  
You may find the video walkthrough of this implementation [here]()
