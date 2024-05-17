import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.rtm_v2 import RTMClient

# Get the Slack bot token from environment variables
slack_token = os.getenv("SLACK_BOT_TOKEN")

# Initialize the Slack client
client = WebClient(token=slack_token)

@RTMClient.run_on(event="message")
def handle_message(**payload):
    data = payload['data']
    web_client = payload['web_client']
    if 'text' in data and 'bot_id' not in data:
        channel_id = data['channel']
        user = data['user']
        text = data['text']
        
        response = f"Hello <@{user}>! You said: {text}"
        
        try:
            web_client.chat_postMessage(
                channel=channel_id,
                text=response
            )
        except SlackApiError as e:
            print(f"Error posting message: {e.response['error']}")

# Initialize the RTM client
rtm_client = RTMClient(token=slack_token)
rtm_client.start()
