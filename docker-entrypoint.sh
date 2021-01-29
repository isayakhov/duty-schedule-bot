#!/usr/bin/env sh

case "$1" in
    "help")
        echo "Duty Schedule Bot"
        echo "Please use of next parameters to start: "
        echo "  > bot: Run bot"
        echo "  > scheduler: Run scheduler for cron tasks"
        ;;
    "bot")
        echo "Running bot ..."
        python -m app.telegram.run_bot
        ;;
    "scheduler")
        echo "Running scheduler"
        python -m app.telegram.run_scheduler
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
