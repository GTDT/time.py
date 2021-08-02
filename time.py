from datetime import datetime
from time import sleep
print("\033c")
try:
  while True:
    sleep(0.1)
    print('\x1b[H\n ',datetime.now(), end='')
except:
  print('\n  exited...\n')
