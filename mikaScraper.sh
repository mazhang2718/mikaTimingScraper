#!/bin/bash
# MikaTiming Scraper



while true; do
  echo "starting scraper..."
  python scraper.py
  echo "pushing csv to server..."
  sshpass -p PASSWORD scp mikaTiming.csv mikaTimingHalf.csv mikaTimingFull.csv numarathon@marathon.iems.northwestern.edu:/var/www/html/houston2017/data
  echo "sleeping for 2 minutes..."
  sleep 120
  echo
done



