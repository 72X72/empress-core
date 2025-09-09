#!/data/data/com.termux/files/usr/bin/bash

# EMPRESS Affiliate Recon Soldier (Self-healing)

mkdir -p ~/empress/soldiers/affiliate
mkdir -p ~/empress/narration

# Pull raw response
curl -s "https://api.clickbank.com/public/products/list?sort=gravity" > offers.json

# Check if response is JSON
if jq empty offers.json 2>/dev/null; then
  jq '.products[0:5] | .[] | {title: .title, link: .affiliate_link}' offers.json > top_links.json
  echo "EMPRESS pulled $(jq length top_links.json) high-commission links." > log.txt
else
  echo "EMPRESS: Invalid response format. Mutation blocked." > log.txt
fi

cp log.txt ~/empress/narration/affiliate_log_$(date +%s).txt
