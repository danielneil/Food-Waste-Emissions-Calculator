#/usr/bin/bash

# exit when any command fails
set -e

##################################################
# Now run the playbook.
ansible-playbook ./site.yml -i hosts  

echo "Running a smoke test of the code with 50 kg of food waste"
./Food_Waste_Emissions_Calculator.py  -i 50
