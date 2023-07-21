#!/usr/bin/python3
"""
    Log Parsing.
"""
import sys
import asyncio


if __name__ == "__main__":

    code_stats_dict = {'200': 0, '301': 0, '400': 0, '401': 0,
                       '403': 0, '404': 0, '405': 0, '500': 0}
    total_size = 0
    count_lines = 0

    for response in sys.stdin:
        try:
            response_list = response.split(' ')
            code_stats_dict[response_list[7]] += 1
            total_size += int(response_list[-1])
            count_lines += 1
            if count_lines == 10:
                print("File size: {}".format(total_size))
                {print("{}: {}".format(key, value)) for key, value in
                 code_stats_dict.items() if value != 0}
                count_lines = 0
        except Exception:
            print("File size: {}".format(total_size))
            {print("{}: {}".format(key, value)) for key, value in
             code_stats_dict.items() if value != 0}
