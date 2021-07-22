#!/usr/bin/python

# Calculate the emissions from a specific amount of food waste entered as an argument on the command line.

import sys, getopt

def main(argv):
   
   foodWasteKg = 0
   
   # For every kilo of food waste that ends up in land 
   # fill, 1.9kg of methane is released into the atmosphere.
   methaneKG = 1.9

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

      elif opt in ("-i", "--foodWasteKg"):
         foodWasteKg = int(arg)
   
         methaneEmissions = foodWasteKg * methaneKG
   
         print 'Food Waste (KG): ' + str(foodWasteKg) + ' kg'
         print 'Released Methane: ' + str(methaneEmissions) + ' kg'      
      
if __name__ == "__main__":
   
   main(sys.argv[1:])
