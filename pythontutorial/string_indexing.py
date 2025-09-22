card_number = "1234-5678-9012-3456"
print(card_number[0])
print(card_number[:4])
print(card_number[7:11])
print(card_number[6:])
print(card_number[-1])
print(card_number[-4:-9:-1])
print(card_number[::4])

#exercise 1
last_digits = card_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

#exercise 2
reversed_version = card_number[::-1]
print(reversed_version)

