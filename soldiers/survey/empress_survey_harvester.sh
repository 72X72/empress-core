#!/data/data/com.termux/files/usr/bin/bash

# EMPRESS Survey Harvester Soldier
mkdir -p ~/empress/narration
curl -s https://api.swagbucks.com/tasks > tasks.json
jq '.[] | select(.reward > 5)' tasks.json > high_value.json
echo "EMPRESS found $(jq length high_value.json) high-value tasks." > log.txt
cp log.txt ~/empress/narration/survey_log_$(date +%s).txt
