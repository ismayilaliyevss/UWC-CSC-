import random 
# ● ┌ ─ ┐ │ └ ┘
"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),  
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")         
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))


for d in range (num_of_dice) :
    dice.append(random.randint(1, 6))

#for d in range(num_of_dice) :
#    for line in dice_art.get(dice[d]) :
#        print(line )

for line in range (5) :
    for d in dice : 
        print(dice_art.get(d)[line], end= "")            #printing every line st dice of collection
    print()    


for d in dice :
    total+=d

print(total)
