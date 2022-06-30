# There are four factors with weighting, eg Founder(0.3), Industry(0.3),
# Traction(0.35) and Gut (0.05) for start-ups
# final rating(eg; P1, P2, P3, P4) is sum of all the factors multiplied with it's respective weighting. 
# 4.0 - 5.0 = P1
# 2.5 - 4.0 = P2
# 1.0 - 2.5 = P3
# 0.0 - R   = P4 
# So a start-up's four factor rating can be inputed. Program will output the final rating 
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
    print( "The start-up has a final rating of P1")
elif result >= 2.5:
    print('The start-up has a final rating of P2')
elif result >= 1.0:
    print('The start-up has a final rating of P3')
elif result >= 0:
    print('The start-up has a final rating of R')

