#!/bin/bash

# Start the run once job.
echo "Downloaded latest menus"

# Setup a cron schedule
echo "* * * * * /cafdl.sh >> /var/log/cron.log 2>&1
# This extra line makes it a valid cron" > scheduler.txt

crontab scheduler.txt
cron -f