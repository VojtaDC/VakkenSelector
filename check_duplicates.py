from collections import defaultdict
from courses import available_courses

# Maak een dictionary om de regels bij te houden waarop elk vak voorkomt
vak_regels = defaultdict(list)

# Vul de dictionary met vakken en hun regels
for index, course in enumerate(available_courses):
    vak_regels[str(course)].append(index + 1)  # +1 omdat regels meestal vanaf 1 worden geteld

# Zoek naar vakken die meer dan één keer voorkomen
duplicates = {vak: regels for vak, regels in vak_regels.items() if len(regels) > 1}

if duplicates:
    print("Dubbele vakken gevonden:")
    for vak, regels in duplicates.items():
        print(f"Vak: {vak}")
        print(f"Regels: {regels}")
else:
    print("Geen dubbele vakken gevonden.")