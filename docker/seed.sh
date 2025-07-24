#!/bin/bash
set -e
while true; do
  echo "Seed $(date)" > sync_files/public/seed_$(date +%s).txt
  sleep 120          
done
