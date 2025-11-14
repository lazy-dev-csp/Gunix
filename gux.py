###########
# Imports #
###########

import os
import argparse
from datetime import datetime

###################
# Argparse Things #
###################

parser = argparse.ArgumentParser(prog='timestamp')
parser.add_argument("file", help="Path to the file")
parser.add_argument("-u", "--unix", action="store_true", help="Print only the Unix timestamp")
parser.add_argument("-d","--date", action="store_true", help="Print only the Creation Dateof the file")

args = parser.parse_args()
file = args.file

################
# Main Program #
################

if os.path.exists(file):
    timestamp = os.path.getmtime(file)
    date = datetime.fromtimestamp(timestamp)
    formatted = date.strftime("%m/%d/%y")

    if args.unix and args.date:
       print(f"Unix: {timestamp} Date: {formatted}")
    elif args.unix:
        print(f"Unix Timestamp: {int(timestamp)}")
    elif args.date:
        print(f"File Creation Date: {formatted}")
    else:
       print("Please add argumenrs to your command or use -h or --help")

else:
    print("File not found")
