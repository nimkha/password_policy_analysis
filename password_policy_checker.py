#!/usr/bin/python

# This script is made to calculate the percentage of passwords in a given policy

import password_policies as policies
# from charset_normalizer import CharsetNormalizerMatches as CnM
# from charset_normalizer import detect


# Returns file content from a file as a list using encoding="utf-8" as default
# Be aware some files are encoded with iso-8859-15
def get_file_content(filename, encoding="utf-8"):
    print("[+] Getting content from file " + filename)

    try:
        with open(filename, "r", encoding=encoding) as f:
            file_content = [line.strip() for line in f]
        return file_content

    except (UnicodeDecodeError, FileNotFoundError) as error:
        if type(error) == UnicodeDecodeError:
            print("[-] A unicode decode error found => " + str(error))
        elif type(error) == FileNotFoundError:
            print("[-] File not found")
        else:
            print("[-] Unknown error detected => " + str(error))


# Removes duplicates from list one by one. This can also be done by using sets
def remove_duplicates(list_with_duplicates):
    print("[+] Removing duplicates")
    new_list = []
    counter = 0
    for i in list_with_duplicates:
        if i not in new_list:
            new_list.append(i)
            print("\r[+] Number of passwords added to list " + str(counter), end="")
    return new_list


# Takes two numbers and calculates the percentage of the total argument to get the result argument
# Ex => if the total is 100 and result is 50 then the return value is 50(%)
def find_percentage(total, result):
    y = total / 100
    x = result / y
    print(
        "[+] The percentage of the total " + "number of " + str(total) + " passwords matching policy is %.2f" % x + "%")
    return x


# Is specifically made to iterate over list of functions to check if a condition is false
def is_list_true(policy_list, arg):
    for element in policy_list:
        if not element(arg):
            return False

    return True


# Gathers all criteria in list
def get_criteria(uppercase, lowercase, special, digit, all_classes, s_u_e_d, start_upper, end_digit):
    criteria_list = []

    if uppercase:
        criteria_list.append(policies.contain_uppercase)
    if lowercase:
        criteria_list.append(policies.contain_lowercase)
    if special:
        criteria_list.append(policies.contain_special_character)
    if digit:
        criteria_list.append(policies.contain_digit)
    if all_classes:
        criteria_list.append(policies.contain_all_classes)
    if s_u_e_d:
        criteria_list.append(policies.start_with_uppercase_end_with_digit)
    if start_upper:
        criteria_list.append(policies.start_with_uppercase)
    if end_digit:
        criteria_list.append(policies.end_with_digit)

    return criteria_list


# Takes a password list and checks how many passwords matches the given policy
# Function argument all_classes = all character classes, s_u_e_d = start with uppercase and en with digit
def password_policy_checker(password_list, length, uppercase, lowercase, special, digit, all_classes, s_u_e_d, start_upper, end_digit):
    print("[+] Checking passwords against criteria")

    criteria_list = get_criteria(uppercase, lowercase, special, digit, all_classes, s_u_e_d, start_upper, end_digit)

    number_of_password_matches = 0
    for password in password_list:
        if len(criteria_list) >= 1:
            if len(password) >= length and is_list_true(criteria_list, password):
                number_of_password_matches = number_of_password_matches + 1
                print("\r[+] Number of password hits " + str(number_of_password_matches), end="")
        else:
            if len(password) >= length:
                number_of_password_matches = number_of_password_matches + 1
                print("\r[+] Number of password hits " + str(number_of_password_matches), end="")
    print()
    return number_of_password_matches


# Takes a list and filename as argument writes content to file (encoding iso-8859-15 or utf-8)
def write_list_to_file(list_to_write, filename, encoding="utf-8"):
    counter = 0
    with open(filename, "a", encoding=encoding) as f:
        for line in list_to_write:
            f.write(line)
            f.write("\n")
            counter = counter + 1
            print("\r[+] Number of lines written to file " + str(counter), end="")
    print("\n[+] Done writing list to file " + filename)


# Prints the total length of a list
def print_total_len_list(password_list, list_name="default value"):
    if isinstance(password_list, list):
        print("[+] Total number of passwords in " + list_name + " is " + str(len(password_list)))
    else:
        print("[-] List is empty or wrong type " + str(type(password_list)))


# Specifically made to extract hashes downloaded from https://haveibeenpwned.com/ and writes result to .txt file
def get_hash_from_file(file_name):
    hashes = []
    hits = 0
    file_content = get_file_content(file_name)
    for i in file_content:
        hashes.append(policies.get_hash(i))
        hits = hits + 1
        print("\r[+] Number of password hits " + str(hits), end="")

    write_list_to_file(hashes, file_name + "_only_hashes.txt")


# Tries to find correct encoding for a text file and writes new file if found using utf-8
# def normalize(text_file):
#     try:
#         CnM.normalize(text_file)  # should write to disk my_subtitle-***.srt
#     except IOError as e:
#         print('Sadly, we are unable to perform charset normalization.', str(e))

# ======================================================================================

if __name__ == "__main__":

    print("[+] Starting program...")
    # ==============================================================================================================

    # crackstation_passwords = get_file_content("crackstation-human-only.txt")

    # passwords = get_file_content("Passwords_without_duplicates/passwords_without_duplicates.txt")
    # linkedin_passwords = get_file_content("Passwords_without_duplicates/linkedin_passwords_without_duplicates_utf8.txt")
    # seclist_passwords = get_file_content("Passwords_without_duplicates/seclist_passwords_without_duplicates_utf8.txt")
    # rockyou_passwords_without_duplicates = get_file_content("Passwords/RockYou/rockyou-cp1125.txt")

    # rockyou_passwords = get_file_content("Passwords/RockYou/rockyou-cp1125.txt")
    # linkedin1_passwords = get_file_content("Passwords/LinkedIn/linkedin.txt")
    # linkedin2_passwords = get_file_content("Passwords/LinkedIn/linked2.txt")
    # all_passwords_with_duplicates = get_file_content("all_passwords_with_duplicates.txt")

    # webost_passwords = get_file_content("Passwords/SecLists/000webhost.txt")
    # top_10_million_passwords = get_file_content("Passwords/SecLists/10-million-password-list-top-1000000.txt")
    # gmail_passwords = get_file_content("Passwords/SecLists/alleged-gmail-passwords.txt")
    # bt4_passwords = get_file_content("Passwords/SecLists/bt4-password.txt")
    # darkcode_passwords = get_file_content("Passwords/SecLists/darkc0de.txt")
    # darkweb_passwords = get_file_content("Passwords/SecLists/darkweb2017-top10000.txt")
    # md5_passwords = get_file_content("Passwords/SecLists/md5decryptor-uk.txt")
    # openwall_passwords = get_file_content("Passwords/SecLists/openwall.net-all.txt")
    # xato_passwords = get_file_content("Passwords/SecLists/xato-net-10-million-passwords-1000000.txt")
    # xato_passwords_dup = get_file_content("Passwords/SecLists/xato-net-10-million-passwords-dup.txt")
    check_list = ["Passw0rd!", "Password1", "password", "P@ssw0rd!1", "passWd"]

    # ==============================================================================================================

    # passwords = seclist_passwords + linkedin_passwords + rockyou_passwords_without_duplicates
    # write_list_to_file(without, "Passwords_without_duplicates/passwords_without_duplicates_utf8.txt")

    # ==============================================================================================================

    passwords_matching_policy = password_policy_checker(check_list, 7, False, False, False, False, False, False, True, True)
    find_percentage(len(check_list), passwords_matching_policy)

    # ==============================================================================================================

    print("[+] Program finished...")
