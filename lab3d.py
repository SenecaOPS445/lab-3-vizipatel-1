#!/usr/bin/env python3

# Author ID: vpatel325

import subprocess

def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    output, error = p.communicate()

    if error:
        return f"Error: {error.decode('utf-8').strip()}"

    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
