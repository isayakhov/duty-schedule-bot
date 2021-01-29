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

1. First you need to create your own bot in telegram and add it to your group
2. Next you need to pass to environment variables your bot's token into `TELEGRAM_TOKEN` variable
3. The last part is to type: `docker-compose up`
4. That's all :)

## Environment variables

|Name     | Required | Default | Description|
|:--------|:-------- |:------- |:-----------|
| REDIS_HOST        | - | redis    | Redis host address        |
| REDIS_PORT        | - | 6379     | Redis port number         |
| REDIS_DB          | - | 0        | Redis database number     |
| TELEGRAM_TOKEN    | - | -        | Telegram bot token        |
| DAYS_OF_DUTY      |   | 5        | Total duty days           |
| PLATFORM          | - | telegram | Platform (for the future) |

## Future plans

* Add Slack support
