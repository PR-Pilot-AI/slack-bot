from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app_token = "xapp-app_token"
bot_token = "xoxb-bot_token"


app = App(token=bot_token)


@app.command("/pilot")
def custom_command_function(ack, respond, command):
    ack()
    #TODO implement the logic 
    respond("your message") # if it is needed


if __name__ == '__main__':
    handler = SocketModeHandler(app, app_token)
    handler.start()