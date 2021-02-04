# Duty Schedule Bot

[![build](https://github.com/isayakhov/duty-schedule-bot/workflows/Linters%20And%20Tests/badge.svg)](https://github.com/isayakhov/duty-schedule-bot/blob/main/.github/workflows/lint-and-tests.yml)
[![codecov](https://codecov.io/gh/isayakhov/duty-schedule-bot/branch/main/graph/badge.svg?token=7DVLEWCKQR)](https://codecov.io/gh/isayakhov/duty-schedule-bot)
[![code_quality](https://www.code-inspector.com/project/18495/status/svg)](https://frontend.code-inspector.com/public/project/18495/duty-schedule-bot/dashboard)
[![code_score](https://www.code-inspector.com/project/18495/score/svg)](https://frontend.code-inspector.com/public/project/18495/duty-schedule-bot/dashboard)

## What is this?

Bot sends into your Telegram group who is from your team on duty today and tomorrow, and also sends schedule for the next week.

## Why?

If your team needs to do some operation activities every day e.g. working with support chats, incidents management, bugs fixing etc.
you can share this role (Duty guy) between team members to help them to better focus on sprint goals and other team activities.

## How to run it?

1. First you need to create your own bot in Telegram / Slack and add it to your group
2. Next you need to pass to environment variables your bot's token into `TELEGRAM_TOKEN` / `SLACK_TOKEN` variable
   - For the Slack you also need to configure a public domain with SSL
   - You also need to configure slash commands on your Slack Applications page
3. Choose `docker-compose.yml` file for you (slack or telegram) and build it
4. The last part is to type: `docker-compose up`
5. Application runs two independent processes for periodic tasks and for bot interaction
6. That's all :)

## How to contribute?

1. Type: `pip install pre-commit && pre-commit install`
2. Make and commit your changes
3. Open Pull request
4. Push your changes

## Environment variables

### Common

|Name     | Required | Default | Description|
|:--------|:-------- |:------- |:-----------|
| REDIS_HOST        | - | redis    | Redis host address                |
| REDIS_PORT        | - | 6379     | Redis port number                 |
| REDIS_DB          | - | 0        | Redis database number             |
| DAYS_OF_DUTY      |   | 5        | Total duty days                   |

### Telegram

|Name     | Required | Default | Description|
|:--------|:-------- |:------- |:-----------|
| TELEGRAM_TOKEN |   | "" | Telegram bot token |

### Slack

|Name     | Required | Default | Description|
|:--------|:-------- |:------- |:-----------|
| SLACK_TOKEN |   | ""                                         | Slack bot token         |
| SLACK_URL   |   | https://slack.com/api/chat.postMessage     | Slack POST requests URL |
