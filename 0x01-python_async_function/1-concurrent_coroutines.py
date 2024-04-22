#!/usr/bin/python3

import time

def task(id):
    print(f'Task {id} started')
    time.sleep(1)  # Simulating a blocking I/O-bound task (e.g., network call)
    print(f'Task {id} finished')

def main():
    task(1)
    task(2)
    task(3)

main()