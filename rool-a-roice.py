import random

response = "y"

while response == "y":
    no = random.randint(1, 6)
    if no == 1:
        print("[---------]")
        print("[           ]")
        print("[     O     ]")
        print("[           ]")
        print("[---------]")
    elif no == 2:
        print("[---------]")
        print("[           ]")
        print("[   O   O   ]")
        print("[           ]")
        print("[---------]")
    elif no == 3:
        print("[---------]")
        print("[     O     ]")
        print("[     O     ]")
        print("[     O     ]")
        print("[---------]")
    elif no == 4:
        print("[---------]")
        print("[   O   O   ]")
        print("[           ]")
        print("[   O   O   ]")
        print("[---------]")
    elif no == 5:
        print("[---------]")
        print("[   O   O   ]")
        print("[     O     ]")
        print("[   O   O   ]")
        print("[---------]")
    else:
        print("[---------]")
        print("[   O   O   ]")
        print("[   O   O   ]")
        print("[   O   O   ]")
        print("[---------]")
    response = input("Você quer jogar o dado novamente? (y/n)")

print("Obrigado por jogar!")
