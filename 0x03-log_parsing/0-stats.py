#!/usr/bin/python3
"""
parse log
"""
import sys
import signal
import re

data = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0,
        500: 0, 'filesize': 0}
line_count = 0


def validate_line(line):
    """ Updated regex pattern to match the datetime format in the log lines """
    pattern = (r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
               r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] '
               r'"GET /projects/260 HTTP/1\.1" [2345]\d{2} \d+$')
    return re.match(pattern, line) is not None


def print_data(data):
    """ print data """
    print(f"File size: {data['filesize']}")
    for k in data.keys():
        if isinstance(k, int) and data[k] != 0:
            print(f"{k}: {data[k]}")


def signal_handler(sig, frame):
    """ signal handler """
    print_data(data)
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)


def get_data():
    """ get data """
    global line_count
    possible_status = {200, 301, 400, 401, 403, 404, 405, 500}

    for line in sys.stdin:
        if validate_line(line):
            parts = line.split(' ')
            filesize = parts[-1]
            status = parts[-2]

            try:
                status = int(status)
            except ValueError:
                continue

            if status not in possible_status:
                continue

            data[status] += 1
            data['filesize'] += int(filesize)
            line_count += 1

            if line_count == 10:
                print_data(data)
                line_count = 0
        else:
            continue


if __name__ == "__main__":
    get_data()
