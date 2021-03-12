#!/usr/bin/python

# Commandline interface

import argparse
import main

# Initialize parser
parser = argparse.ArgumentParser(description="Analysing password content")

# Add positional arguments
parser.add_argument("file", help="Enter filename containing passwords")
parser.add_argument("length", help="Specify min length of password. Must be between 1 - 20 characters", type=int)

# Add optional arguments
parser.add_argument("-u", "--uppercase", help="Checks if password contain uppercase character", action="store_true")
parser.add_argument("-l", "--lowercase", help="Checks if password contain lowercase character", action="store_true")
parser.add_argument("-s", "--special", help="Checks if password contain special character", action="store_true")
parser.add_argument("-d", "--digit", help="Checks if password contain digit", action="store_true")
parser.add_argument("-a", "--all", help="Checks if password satisfy all criteria classes", action="store_true")
parser.add_argument("--startUendD", help="Checks if password starts with uppercase and end with digit", action="store_true")
parser.add_argument("--startUppercase", help="Checks if password start with uppercase", action="store_true")
parser.add_argument("--endDigit", help="Checks if password end with digit", action="store_true")

args = parser.parse_args()

if 1 <= args.length <= 20:
    main.run(args.file, args.length, args.uppercase, args.lowercase, args.special, args.digit, args.all, args.startUendD, args.startUppercase, args.endDigit)
else:
    print("wrong length value")
    exit()
