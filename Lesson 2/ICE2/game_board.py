
def hori(x):
    for j in range(x):
        print("-" * x,' ',end="")

def ver(x):
    for j in range(x+1):
        print("|"," "*(x-1),end="")


def board_draw(x,y):

    for k in range(y):
        hori(x)
        print()
        ver(y)
        print()
    hori(x)

heightinp = int(input("Enter the height of the board:"))
widthinp = int(input("Enter the width of the board:"))

for i in range(heightinp):
    print("--- "*heightinp)
    print("|  " * (heightinp+1))

print("--- "*heightinp)

