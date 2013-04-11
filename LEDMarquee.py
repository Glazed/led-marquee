from inputs import InputClock
from inputs import InputConsole
from inputs import InputWeather
from inputs import InputMomentum
from inputs import InputEmail
from filters import profanityfilter
import time

def ledMarquee():
  """
  Main function for LEDMarquee. Sends properly formatted
  text to hardware for display on the Marquee.

  Current state: Printing as simulation.
  """
  printList = [InputConsole, InputClock, InputWeather, InputMomentum, InputEmail]

  pro = profanityfilter.ProfanityFilter()

  while(True):
    #Iterates through all given commands, printing .get() statements.
    for i in printList:
      printStr = i.get()
      if (printStr):
        time.sleep(2)
        if (i.isFiltered()):
          printStr = pro.replaceProfanity(printStr)
        print(printStr)


ledMarquee()
