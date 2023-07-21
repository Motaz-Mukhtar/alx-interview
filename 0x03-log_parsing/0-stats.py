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
    try:
        for request in sys.stdin:
            request_list = request.split(' ')
            if len(request_list) > 2:
                if request_list[-2] in code_stats_dict:
                    code_stats_dict[request_list[-2]] += 1
            total_size += int(request_list[-1])
            count_lines += 1
            if count_lines == 10:
                print("File size: {}".format(total_size))
                {print("{}: {}".format(key, value)) for key, value in
                 sorted(code_stats_dict.items()) if value != 0}
                count_lines = 0
    except Exception:
        pass
    finally:
        print("File size: {}".format(total_size))
        {print("{}: {}".format(key, value)) for key, value in
         sorted(code_stats_dict.items()) if value != 0}
