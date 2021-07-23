#!/usr/bin/python

# Calculate the emissions from a specific amount of food waste entered as an argument on the command line.

import sys, getopt

def main(argv):
   
   foodWasteKg = 0
   
   # For every kilo of food waste that ends up in land fill the follow constants are applicable. 
   
   # Amount of methane (in kg) released into the atmosphere.
   Emissions_of_CO2_e_kg = 1.9

   # Equivalent electricity consumption ( in days ) for one household
   household_electricity_consumption_days = 0.17
   
   # Equivalent 50L petrol tanks consumed
   petrol_tanks = 0.02
   
   # Display help.
   helpString = 'Food_Waste_Emissions_Calculator.py -i <foodWasteKg>'
   
   try:
      opts, args = getopt.getopt(argv,"hi:",["Emissions_of_CO2_e_kg="])
      
   except getopt.GetoptError:
      
      print helpString
      
      sys.exit(2)
      
   for opt, arg in opts:
      
      if opt == '-h':
         
         print helpString
         sys.exit()

      elif opt in ("-i", "--foodWasteKg"):
         foodWasteKg = int(arg)
   
         methaneEmissions_calc = foodWasteKg * Emissions_of_CO2_e_kg
         household_electricity_days_calc = foodWasteKg * household_electricity_consumption_days
         petrol_tanks_calc = foodWasteKg * petrol_tanks
   
         print 'Food Waste (KG): ' + str(foodWasteKg) + ' kg'
         print 'Released Methane: ' + str(methaneEmissions_calc) + ' kg'      
         print 'Equivalent electricity consumption ( in days ) for one household: ' + str(household_electricity_days_calc) + ' days'
         print 'Equivalent 50L petrol tanks consumed: ' + str(petrol_tanks_calc) + ' petrol tanks'      
      
if __name__ == "__main__":
   
   main(sys.argv[1:])
