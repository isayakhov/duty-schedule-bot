#!/usr/bin/env sh

case "$1" in
    "help")
        echo "Duty Schedule Bot"
        echo "Please use of next parameters to start: "
        echo "  > bot: Run bot"
        echo "  > scheduler: Run scheduler for cron tasks"
        ;;
    "tg-bot")
        echo "Running bot ..."
        python -m app.telegram.run_bot
        ;;
    "tg-scheduler")
        echo "Running scheduler"
        python -m app.telegram.run_scheduler
        ;;
    "slack-bot")
        echo "Running bot ..."
        python -m app.slack.run_bot
        ;;
    "slack-scheduler")
        echo "Running scheduler"
        python -m app.slack.run_scheduler
        ;;
    "")
        echo "No run parameter passed please use one of: [bot, scheduler, help]"
        exit 1
        ;;
    *)
        echo "Unknown command '$1'. please use one of: [bot, scheduler, help]"
        exit 1
        ;;
esac
