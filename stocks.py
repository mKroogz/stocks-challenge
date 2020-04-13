stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak"
}

purchases = [
    ( 'GM', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GM', 200, '1-jul-1998', 56 )
]

for (key, value) in stockDict.items():
    for stocks in purchases:
        if stocks[0] == key:
            print(f"I purchased {value} stock for ${(stocks[1] * stocks[3])}")

portfolio = dict()
for ticker in purchases:
    portfolio[ticker[0]] = []
for stocks in purchases:
    portfolio[stocks[0]].append(stocks[1:])

value = 0
for (tick, buys) in portfolio.items():
    print(f"------ {tick} ------")
    for info in buys:
        print(f"{info[0]} shares at {info[2]} dollars each on {info[1]}")
        value += info[0] * info[2]
print(f"Total value of stock in portfolio: ${value}")