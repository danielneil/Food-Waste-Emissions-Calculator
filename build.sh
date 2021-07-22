#/usr/bin/bash

# exit when any command fails
set -e

##################################################
# Now run the playbook.
ansible-playbook ./site.yml -i hosts  

# Running a smoke test of the code.
./Food_Waste_Emissions_Calculator.py  -i 10
