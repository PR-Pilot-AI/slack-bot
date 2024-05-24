# Slack Bot for PR Pilot

This repository contains a demo implementation of a Slack bot designed to integrate with PR Pilot via the `/pilot` slash command.

For more information, check out the [blog post](https://www.pr-pilot.ai/blog/a-natural-language-interface-between-slack-and-github).


## Demo Video

[![Watch the video](https://img.youtube.com/vi/QuSsMHLqTBk/maxresdefault.jpg)](https://youtu.be/QuSsMHLqTBk)

## Prerequisites

1. Follow the [Slack Bolt Getting Started Guide](https://slack.dev/bolt-python/tutorial/getting-started) to create your Slack app
2. Create an API Key in your [PR Pilot Dashboard](https://app.pr-pilot.ai/dashboard/api-keys/)

## Installation

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up the necessary environment variables (`SLACK_SIGNING_SECRET`, `SLACK_BOT_TOKEN`, `SLACK_APP_TOKEN`, `PR_PILOT_API_KEY`).
4. Run the bot using `python app.py`.

## Usage

Use the `/pilot` command in Slack to interact with the bot. It will handle the command and provide feedback directly in Slack.
