#!/usr/bin/env python3
"""
Script that reads stdin line by line and computes metrics.
"""

import sys

# Initialize total file size and status code counts
total_file_size = 0
status_code_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

def print_stats():
    """
    Function to print the statistics.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()

        # Ensure the input line matches the required format
        if len(parts) >= 7 and parts[-2].isdigit():
            status_code = parts[-2]
            file_size = parts[-1]

            # Accumulate the total file size
            try:
                total_file_size += int(file_size)
            except ValueError:
                continue

            # Increment the count for the status code
            if status_code in status_code_count:
                status_code_count[status_code] += 1

            line_count += 1

            # Every 10 lines, print the current statistics
            if line_count % 10 == 0:
                print_stats()

except KeyboardInterrupt:
    # On keyboard interruption, print statistics
    print_stats()
    raise

# Print the final stats at the end of the input
print_stats()
