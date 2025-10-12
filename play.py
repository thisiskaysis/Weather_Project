from datetime import datetime
import csv

# #FUNCTION FIND_MIN
# weather_data = [10.4, 14.5, 12.9, 8.9, 10.5, 11.7]
# minimum = min(weather_data)
# index = weather_data.index(minimum)
# print(minimum, index)

# #FUNCTION CONVERT DATE
# iso_string = "2021-07-05T07:00:00+08:00"
# formatted_date = datetime.fromisoformat(iso_string)
# date = datetime.strftime(formatted_date, "%A %d %B %Y")
# print(date)

# #FUNCTION LOAD_DATA_FROM_CSV
# data = []
# with open('./test.csv', 'r') as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         date = row[0]
#         min = int(row[1])
#         max = int(row[2])
#         output = [date, min, max]
#         data.append(output)
# print(data)

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

for i in nested_list:  # Outer loop iterates through indices of sublists
    print(i)