colors = ["red", "blue", "yellow", "black"]
symbols = []

for i in range(4):
    for c in colors:
        symbols.append(f"{c}{i}")
        
print(symbols)