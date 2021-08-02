from datetime import datetime
from time import sleep
print("\033c")               # clear console
try:                         # to display the exit message on exit
  while True: 
    print(                   # time printing
      '\x1b[H\n',            # back to the start of the line and new line
      datetime.now(),
      end=''
    );
    sleep(0.1)               # delay between the prints
except:
  print('\n  exited...\n')   # exit message
