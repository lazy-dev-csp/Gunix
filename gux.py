#!/usr/bin/python3


#### Imports ####


import os
import argparse
from datetime import datetime

#### Define Sizes ####

def size_KiB(file):
   return os.path.getsize(file) /  1024
def size_MiB(file):
   return os.path.getsize(file) / (1024**2)
def size_GiB(file):
   return os.path.getsize(file) / (1024**3)


#### Define Arguments ####


parser = argparse.ArgumentParser(prog='gux')
parser.add_argument("file", help="Path to the file")
parser.add_argument("-u", "--unix", action="store_true", help="Print only the Unix timestamp")
parser.add_argument("-d","--date", action="store_true", help="Print only the Creation Dateof the file")
parser.add_argument("-s","--size", choices=["KiB","MiB","GiB"], help="Unit to display size in")

### Define  Things ####

args = parser.parse_args()
file = args.file

#### Main Program Block  ####

if not os.path.exists(file):
         print("File Not Found Bozo")

if  os.path.exists(file):
    size = os.path.getsize(file)
    timestamp = os.path.getmtime(file)
    date = datetime.fromtimestamp(timestamp)
    formatted = date.strftime("%m/%d/%y")


    #### Print Info ####

    units = {
    "KiB": size_KiB,
    "MiB": size_MiB,
    "GiB": size_GiB
    }

    if   args.unix and args.date:
        print(f"Unix: {timestamp} Date: {formatted}")
    elif args.unix:
        print(f"Unix Timestamp: {int(timestamp)}")
    elif args.date:
        print(f"File Creation Date: {formatted}")

    #### Print File Sizes ####

    if  args.size == "KiB":
        size = size_KiB(file)
    elif args.size == "MiB":
        size = size_MiB(file)
    elif args.size == "GiB":
        size = size_GiB(file)

    unit = args.size

    if args.size:
        print(f"File Is: {size:.2f} {args.size}")

    if not (args.unix and not  args.date and not args.size):
       print(f"File: {os.path.basename(file)}")
       print(f"  Modified: {formatted}")
       print(f"  Size: {size / 1024:.2f} KiB")
