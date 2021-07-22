#!/usr/bin/python

# Calculate the emissions from a specific amount of food waste entered as an argument on the command line.

import sys, getopt

def main(argv):
   
   foodWasteKg = 0

   try:
      opts, args = getopt.getopt(argv,"hi:",["foodWasteKg="])
      
   except getopt.GetoptError:
      
      print 'Food_Waste_Emissions_Calculator.py -i <foodWasteInKG>'
      
      sys.exit(2)
      
   for opt, arg in opts:
      
      if opt == '-h':
         print 'Food_Waste_Emissions_Calculator.py -i <foodWasteInKG>'
         sys.exit()

if __name__ == "__main__":
   
   main(sys.argv[1:])
