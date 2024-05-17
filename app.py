from slack_sdk import WebClient
from slack_sdk.rtm import RTMClient

# Initialize the Slack client with your bot's token
token = 'YOUR_BOT_USER_OAUTH_TOKEN'
client = WebClient(token=token)

# Define an event handler for messages
def handle_message(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']

    if 'text' in data and 'Hello' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        web_client.chat_postMessage(channel=channel_id, text=f"Hello <@{user}>!", thread_ts=thread_ts)

# Start the RTM client
def main():
    rtm_client = RTMClient(token=token)
    rtm_client.start()

if __name__ == '__main__':
    main()