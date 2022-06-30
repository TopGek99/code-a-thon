#for any number of companies, 4 factor ratings can be inputed. 
#the program will keep asking for 4 factor ratings unless a N is inouted. 
#for all the inputed data. Program will outout the following
#-----number of start-ups
#-----start-up progression rate = ((total number of P1s) + (total number of P2s) + (total number of P3s)) / (total number of startups)
#-----Average rating for Factor 1 
#-----Average rating for Factor 2 
#-----Average rating for Factor 3
#-----Average rating for Factor 4
#-----Average final rating
#-----Number of P1s
#-----Number of P2s
#-----Number of P3s
#-----Number of Rs

num_start_up = 0
weighting = [0.3, 0.3, 0.35, 0.05]
factor_totals = [0, 0, 0, 0]
num_categories = [0, 0, 0, 0]
num_p = 0
result_total = 0
p1_names = []
p2_names = []
p3_names = []
r_names = []
data = input("Enter a Start-up’s factor ratings (separated by comma), type in letter N to finish:\n")
while data != 'N':
    num_start_up += 1
    dataset = data.split(',')
    start_up = dataset[0]
    dataset.remove(dataset[0])
    result = 0
    i = 0
    while i < len(dataset):
        result += float(dataset[i])*weighting[i]
        factor_totals[i] += float(dataset[i])
        i += 1
    result_total += result
    if result >= 4.0:
        num_categories[0] += 1
        num_p += 1
        p1_names.append(start_up)
    elif result >= 2.5:
        num_categories[1] += 1
        num_p += 1
        p2_names.append(start_up)
    elif result >= 1.0:
        num_categories[2] += 1
        num_p += 1
        p3_names.append(start_up)
    elif result >= 0:
        num_categories[3] += 1
        r_names.append(start_up)
    data = input("Enter a Start-up’s factor ratings (separated by comma), type in letter N to finish:\n")
p_ratio = num_p/num_start_up * 100
result_avg = result_total/num_start_up
task2file = open("task2.txt","w")
task2file.write("p1_names = " + str(p1_names) + "\np2_names = " + str(p2_names) + "\np3_names = " + str(p3_names) + "\nr_names = " + str(r_names) + "\n")
print("Number of Start-ups:",num_start_up)
print("Start-up progression rate: ",round(p_ratio),'%', sep='')
print("Average rating for factor 1(Founder):",round(factor_totals[0]/num_start_up, 2))
print("Average rating for factor 2(Industry):",round(factor_totals[1]/num_start_up, 2))
print("Average rating for factor 3(Traction):",round(factor_totals[2]/num_start_up, 2))
print("Average rating for factor 4(Gut):",round(factor_totals[3]/num_start_up, 2))
print("Number of P1s:", end=' ')
print(num_categories[0], *p1_names, sep=',')
print("Number of P2s:", end=' ')
print(num_categories[1], *p2_names, sep=',')
print("Number of P3s:", end=' ')
print(num_categories[2], *p3_names, sep=',')
print("Number of Rs:", end=' ')
print(num_categories[3], *r_names, sep=',')
