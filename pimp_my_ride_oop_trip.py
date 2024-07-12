from dataclasses import dataclass

class Trip:
    client = str
    start = int
    duration = int
    price = int

    def __init__(self):
