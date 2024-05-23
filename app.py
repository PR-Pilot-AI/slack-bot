import os
import re

from pr_pilot.util import create_task, wait_for_result
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient

signing_secret = os.getenv('SLACK_SIGNING_SECRET')
bot_token = os.getenv('SLACK_BOT_TOKEN')
app_token = os.getenv('SLACK_APP_TOKEN')
github_repo = 'PR-Pilot-AI/pr-pilot'
app = App(token=bot_token, signing_secret=signing_secret)

def translate_markdown(markdown):
    # Translate Markdown into Slack-compatible format
    regex = r"\[([^\]]+)\]\(([^)]+)\)"
    return re.sub(regex, r"<\2|\1>", markdown).replace("**", "*")


@app.command("/pilot")
def custom_command_function(ack, respond, command):
    ack()
    # Pass on slash command to PR Pilot
    task = create_task(github_repo, command['text'])
    dashboard_url = f"https://app.pr-pilot.ai/dashboard/tasks/{task.id}/"
    respond(f"Working on it! You can track my progress in the <{dashboard_url}|dashboard>, "
            f"I will send you the result as a message.")
    result = wait_for_result(task)

    # Send the result as a message to the user
    client = WebClient(token=bot_token)
    client.chat_postMessage(channel=command["user_id"], text=translate_markdown(result))


if __name__ == '__main__':
    SocketModeHandler(app, app_token).start()