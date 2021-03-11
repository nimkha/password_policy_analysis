#!/usr/bin/python

import password_policy_checker as checker


def run(filename, length, uppercase, lowercase, special, digit, c8, s_u_e_d):
    print("[+] Starting program...")

    file_content = checker.get_file_content(filename)
    result_from_analysis = checker.password_policy_checker(file_content, length, uppercase, lowercase, special, digit, c8, s_u_e_d)
    checker.find_percentage(len(file_content), result_from_analysis)

    print("[+] Program finished...")

