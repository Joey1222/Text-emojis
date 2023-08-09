from threading import Thread
import argparse
import timeit

start = timeit.default_timer()

def main():
  print("hello, world")

stop = timeit.default_timer()

print(f'Time: {round(stop - start)}')