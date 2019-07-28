#!/bin/bash

/home/speed/.local/bin/speedtest-cli --csv >> /var/speed/output.csv
/usr/bin/python3 /home/speed/speeds_to_spreadsheet.py
