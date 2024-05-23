# Slack Bot for PR Pilot

This repository contains the implementation of a Slack bot designed to integrate with PR Pilot, facilitating automated interactions and task management within Slack.

## Features

- **Command Handling**: Processes commands sent via Slack to interact with the PR Pilot system.
- **Task Tracking**: Provides updates and results of tasks initiated through Slack commands.

## Installation

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up the necessary environment variables (`SLACK_SIGNING_SECRET`, `SLACK_BOT_TOKEN`, `SLACK_APP_TOKEN`).
4. Run the bot using `python app.py`.

## Usage

Use the `/pilot` command in Slack to interact with the PR Pilot system. The bot will handle the command and provide feedback directly in Slack.

## Contributing

Contributions are welcome! Please read the CONTRIBUTING.md for guidelines on how to contribute to this project.

## License

Distributed under the MIT License. See `LICENSE` file for more information.