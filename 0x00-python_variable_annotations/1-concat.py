#!/usr/bin/env python3
def show(value: str, excitement: int = 10) -> None:
    print(value + value[-1] * excitement)


show("Hello World")