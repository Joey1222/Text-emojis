import os
from sys import argv
from time import sleep
from tqdm import tqdm
from threading import Thread
import timeit

def clear_bar(secs: int):
    for i in tqdm(range(secs), desc="Going to clear in"):
        sleep(1)
    os.system("clear")

clearbarthread = Thread(target=clear_bar, args=(10,))

def main():
  try:
    if argv[1] == "--clean":
      print('Clean: true')
      clearbarthread.start()
  except:
    print('''Invaild args!

  Usage:
    --clean (y/n) to clean yes or no
    ''')
    clearbarthread.start()

mainthread = Thread(target=main)

mainthread.start()

start = timeit.default_timer()

stop = timeit.default_timer()

print('Time: ', stop - start)