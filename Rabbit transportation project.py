print("Welcome to place the rabbit")

field = [ ["🥬️", "🥬️", "🥬️"], ["🥬️", "🥬️", "🥬️"], ["🥬️", "🥬️", "🥬️"] ]

print(f"{field[0]} \n{field[1]} \n{field[2]}")
print("Where should the rabbit go? 🐇")

choose_r_c = input("Please choose row and column")

row = int(choose_r_c[0])
column = int(choose_r_c[1])

field[row-1][column-1] = "🐇"

print("Success! Here is your rabbit:")

print(f"{field[0]} \n{field[1]} \n{field[2]}")