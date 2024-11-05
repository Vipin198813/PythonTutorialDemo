import csv
data = open('MyExcelFile.csv')
csv_data = csv.reader(data)
data_lines = list(csv_data)
print(data_lines[0])
print(len(data_lines))

for line in data_lines[:len(data_lines)]:
    print(line)

file_to_output = open('to_save_file.',mode ='w',newline = '')
csv_writer = csv.writer(file_to_output,delimiter=',')
print(csv_writer.writerow(['a','b','c']))