#!/usr/bin/python

import password_policy_checker as checker


def run(filename, length, uppercase, lowercase, special, digit, c8, s_u_e_d, start_upper, end_digit, encoding="utf-8"):
    print("[+] Starting program...")

    file_content = checker.get_file_content(filename, encoding)
    result_from_analysis = checker.password_policy_checker(file_content, length, uppercase, lowercase, special, digit, c8, s_u_e_d, start_upper, end_digit)
    checker.find_percentage(len(file_content), result_from_analysis)

    print("[+] Program finished...")

