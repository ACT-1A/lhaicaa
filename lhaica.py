print("=========================================================")
print("                  PYTHON MINI STORE POS")
print("=========================================================")

print("PRODUCT MENU")
print("[B] BURGER        - P50")
print("[P] PIZZA         - P120")
print("[F] FRIES         - P70")
print("[S] SOFT DRINKS   - P40")
print("=========================================================")

code = input("enter product code: ").upper()

if code == 'B':
    product = "BURGER"
    price = 50

elif code == 'P':
    product = "PIZZA"
    price = 120

elif code == 'F':
    product = "FRIES"
    price = 70

elif code == 'S':
    product = "SOFT DRINKS"
    price = 40

else:
    print("invalid code!")
    exit()