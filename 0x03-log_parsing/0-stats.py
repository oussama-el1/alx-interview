#!/usr/bin/python3
"""
parse log
"""
import sys
import signal
import re

data = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0, 'filesize': 0}
line_count = 0


def print_data(data):
    """ print data """
    print(f"File size: {data['filesize']}")
    for k in sorted(data.keys()):
        if isinstance(k, int) and data[k] != 0:
            print(f"{k}: {data[k]}")

def signal_handler(sig, frame):
    """ signale handler """
    print_data(data)
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

def get_data():
    """ get data """
    global line_count
    possible_status = {200, 301, 400, 401, 403, 404, 405, 500}

    for line in sys.stdin:
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

    if line_count > 0:
        print_data(data)
    elif line_count == 0:
        print(f"File size: 0")

if __name__ == "__main__":
    get_data()

