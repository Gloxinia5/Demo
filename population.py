start_size = 0
end_size = 0
n = 0

while start_size < 9:
    start_size = int(input("Population start size: "))

currPopulation = start_size

while end_size < start_size:
    end_size = int(input("Population end size: "))

while currPopulation < end_size:
    currPopulation = (currPopulation + (currPopulation / 3) - (currPopulation/4))
    n += 1

print(f"years: {n}")