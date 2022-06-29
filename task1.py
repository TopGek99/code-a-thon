data = input("Enter a Start-up’s factor ratings (separated by comma):\n")
dataset = data.split(',')
start_up = dataset[0]
dataset.remove(dataset[0])
weighting = [0.3, 0.3, 0.35, 0.05]
result = 0
i = 0
while i < len(dataset):
    result += float(dataset[i])*weighting[i]
    i += 1
if result >= 4.0:
    print('P1')
elif result >= 2.5:
    print('P2')
elif result >= 1.0:
    print('P3')
elif result >= 0:
    print('R')

