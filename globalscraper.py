#!/usr/bin/env python3
import random, time
urls=["https://github.com/trending","https://www.producthunt.com","https://www.reddit.com/r/Entrepreneur","https://medium.com/tag/automation"]
agents=["Mozilla/5.0","Safari/537.36","Chrome/91.0"]
for url in urls:
	print(f"[EMPRESS] Hunting: {url}")
	time.sleep(random.uniform(1.5,3.5))
	print(f"[EMPRESS] Scraped and cloaked using {random.choice(agents)}")
