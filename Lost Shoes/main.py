# https://train.nzoi.org.nz/problems/1229

colours = {
    'G': "Green",
    'B': "Black",
    'R': "Red",
    'Bl': "Blue",
    'Br': "Brown",
    'M': "Mustard",
}

counts = {
    "Green": 0,
    "Black": 0,
    "Red": 0,
    "Blue": 0,
    "Brown": 0,
    "Mustard": 0,
}

chars = input()
shoes = []

i = 0
while i < len(chars):
    if chars[i] == 'B' and i + 1 < len(chars) and chars[i + 1].islower():
        shoes.append(chars[i] + chars[i + 1])
        i += 1
    else:
        shoes.append(chars[i])
    i += 1

for shoe in shoes:
    counts[colours[shoe]] += 1

unpaired = []

for colour, count in counts.items():
    if count % 2 == 1:
        unpaired.append(colour)

if len(unpaired) == 0:
    print("All paired up!")
else:
    for colour in unpaired:
        print(f"A {colour} shoe has no partner.")