#! /usr/bin/python3

import threading


def simple_func():
	print("Entered sample function for testing threading")


if __name__ == "__main__":
	for _ in range(3):
		t = threading.Thread(target=simple_func)
		t.start()
