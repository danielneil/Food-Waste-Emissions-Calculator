#!/usr/bin/python

# Calculate the emissions from a specific amount of food waste entered as an argument on the command line.

import sys, getopt

def main(argv):
   
   foodWasteKg = 0

   helpString = 'Food_Waste_Emissions_Calculator.py -i <foodWasteInKG>'
   
   try:
      opts, args = getopt.getopt(argv,"hi:",["foodWasteKg="])
      
   except getopt.GetoptError:
      
      print helpString
      
      sys.exit(2)
      
   for opt, arg in opts:
      
      if opt == '-h':
         
         print helpString
         sys.exit()

   print foodWasteKg
         
if __name__ == "__main__":
   
   main(sys.argv[1:])
