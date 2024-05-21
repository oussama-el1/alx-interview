import re
import random
import datetime



for i in range(5):
    line = "{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0000"),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    )
    if not validate_line(line):
        print("Invalid line:", line)
        # Add any action you want to take if the line is invalid
    else:
        print("valid line:", line)
