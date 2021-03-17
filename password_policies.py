#!/usr/bin/python

# This script contains different characteristics of password policies

import re


# Checks if string ends with a digit
def end_with_digit(string):
    if string[-1].isdigit():
        return True
    else:
        return False


# Checks if string starts with an uppercase character
def start_with_uppercase(string):
    if string[0].isupper():
        return True
    else:
        return False


# Takes a regex and string as inputs and check if there is a match
def check_regex_matches(regex, string):
    if regex.search(string):
        return True
    else:
        return False


# Checks is password start with uppercase and end with digit
def start_with_uppercase_end_with_digit(string):
    regex = re.compile(r"^[A-Z].+\d$")
    return check_regex_matches(regex, string)


# Checks if password contain digit, contain lowercase and uppercase characters, and contain special character
def contain_all_classes(string):
    if contain_digit(string) and contain_lowercase(string) and contain_uppercase(string) and contain_special_character(string):
        return True
    else:
        return False


# Extract hash from string
def get_hash(string):
    match_obj = re.search(r"(.*):", string)
    return match_obj.group(1)


# Checks if a string contains any special characters from a set of 33 characters " !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
def contain_special_character(string):
    if isinstance(string, str) and len(string) > 0:
        regex = re.compile("[\s!\"#$%&'()*+,-./:;<=>?@\[\]^_`{|}~]")
        return check_regex_matches(regex, string)
    else:
        print("[-] Invalid string value in function 'contain_special_character'")
        exit()


# Checks if a string contains any digits ranging from 0-9
def contain_digit(string):
    regex = re.compile("[0-9]")
    return check_regex_matches(regex, string)


# Checks if a string contains any uppercase letters between A-Z
def contain_uppercase(string):
    regex = re.compile("[A-Z]")
    return check_regex_matches(regex, string)


# Checks if a string contains any lowercase letters between A-Z
def contain_lowercase(string):
    regex = re.compile("[a-z]")
    return check_regex_matches(regex, string)