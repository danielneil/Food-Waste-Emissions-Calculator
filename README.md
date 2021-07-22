# Food Waste Emissions Calculator

Calculate the emissions from a specific amount of food waste entered as an argument on the command line. 

(https://github.com/danielneil/Food-Waste-Emissions-Calculator/blob/main/Food_Waste_Emissions_Calculator.py)[Food_Waste_Emissions_Calculator.py]

# Setup (Builds the dependencies)

1. Prepare a vanilla Debian Server with VirtualBox ([help](https://linuxhint.com/install_debian10_virtualbox/)).

2. Install ansible ([help](https://linuxhint.com/install_ansible_debian10/)).

3. Install Git ([help](https://linuxhint.com/install_git_debian_10/)).

4. Open a terminal, and run:
```
git clone https://github.com/danielneil/Food-Waste-Emissions-Calculator && cd Food-Waste-Emissions-Calculator && ./build.sh
```
5. Usage:
```
daniel@debian:~/Food-Waste-Emissions-Calculator$ ./Food_Waste_Emissions_Calculator.py -i 50
Food Waste (KG): 50 kg
Released Methane: 95.0 kg
Equivalent electricity consumption ( in days ) for one household: 8.5 days
Equivalent 50L petrol tanks consumed: 1.0 petrol tanks
```
