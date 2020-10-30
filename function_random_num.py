import csv



with open("random_num.csv",'r') as f:
    reader = csv.reader(f)
    data = list(reader)


result = []
for d in data[0]:
    d_int = int(d)
    result.append(3*d_int + 6)


with open("function_random_num.csv",'w') as output:
    writer = csv.writer(output)
    writer.writerow(result)

