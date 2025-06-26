"""
elef = 1
print(f"{elef} elefante incomoda muita gente...")
incomoda = input("Os elefantes já estão incomodando?").lower()
while incomoda == "n":
    print(f"{elef} elefante incomodam muita gente...")
    elef += 1
    print(f"{elef} elefantes {elef*"incomodam "}muito mais...")
    incomoda = input("Os elefantes já estão incomodando?").lower()
"""

elef = 1
maxelef = int(input("Quantos elefantes te incomodam?"))
while elef != maxelef+1:
    if elef == 1:
        print(f"{elef} elefante incomoda muita gente...")
    else:
        print(f"{elef} elefantes incomodam muita gente...")
    elef += 1
    print(f"{elef} elefantes {elef*"incomodam "}muito mais...")

