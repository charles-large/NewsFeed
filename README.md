# NewsFeed
RSS News Feed for AWS service features and updates

1. Daily invocation of Eventbridge rule that triggers Lambda function
2. Checks RSS Feed for AWS News Announcements and compares with latest entry in DynamoDB
3. DynamoDB will store new events in table
4. DynamoDB Streams detects new entries. Lambda is watching Streams and invokes SNS event.
5. SNS sends out email with service update/announcement

![newsfeed drawio](https://github.com/charles-large/NewsFeed/assets/70664028/dffd0cc1-20c6-4f88-ba8c-c34d6483e3ce)
