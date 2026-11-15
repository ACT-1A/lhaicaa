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

qty = int(input("enter quantity:"))

if qty <= 0:
    print("invalid quantity!")
    exit()

subtotal = price * qty

if subtotal >= 1000:
    discount_rate = 0.10

elif subtotal >= 500:
    discount_rate = 0.05

else:
    discount_rate = 0

discount = subtotal * discount_rate
discount_amt = subtotal - discount
tax = discount_amt * 0.12
final_total = discount_amt + tax

print("\n=========================================================")
print("                        RECEIPT")
print("=========================================================")

print(f"Product code: {code}")
print(f"Price: P{price:.2f}")
print(f"Quantity: P{qty:.0f}")

print("=========================================================")

print(f"subtotal: P{subtotal:.2f}")
print(f"discount: P{discount:.2f}")
print(f"tax: P{tax:.2f}")

print("=========================================================")

print(f"total: P{final_total:.2f}")

print("=========================================================")

payment = float(input("enter payment: P"))
if payment >= final_total:
    change = payment - final_total
    print(f"payment :P {payment:.2f}")
    print(f"change :P{change:.2f}")
else:
    balance = final_total - payment
    print("insufficient payment!")
    print(f"balance :P{balance:.2f}")

print("=========================================================")
print("                  THANK YOU FOR SHOPPING")
print("=========================================================")
