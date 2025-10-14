import csv
from datetime import datetime
import weather

weather_data = [
    ["2020-06-19T07:00:00+08:00", 47, 46],
    ["2020-06-20T07:00:00+08:00", 51, 67],
    ["2020-06-21T07:00:00+08:00", 58, 72],
    ["2020-06-22T07:00:00+08:00", 59, 71],
    ["2020-06-23T07:00:00+08:00", 52, 71],
    ["2020-06-24T07:00:00+08:00", 52, 67],
    ["2020-06-25T07:00:00+08:00", 48, 66],
    ["2020-06-26T07:00:00+08:00", 53, 66],
    ]

min_list = [] #empty list for low temps
max_list = [] #empty list for high temps
date = len(weather_data) #number of days in dataset

#ADD LOW AND HIGH TEMP DATA TO NEW, SEPERATE LISTS
for data in weather_data:
    if data and len(data) == 3:
        min_list.append(data[1]) #add low temps to min_list
        max_list.append(data[2]) #add high temps to max_list

#FIND MEAN (AVG) LOW TEMP
mean_low_f = weather.calculate_mean(min_list) #find mean temp (farenheit)
mean_low_c = weather.convert_f_to_c(mean_low_f) #convert farenheit to celcius
avg_low = weather.format_temperature(mean_low_c) #format degrees symbol (e.g. 23°C)

#FIND MEAN (AVG) HIGH TEMP
mean_high_f = weather.calculate_mean(max_list) #find mean temp (fanrenheit)
mean_high_c = weather.convert_f_to_c(mean_high_f) #convert farenheit to celcius
avg_high = weather.format_temperature(mean_high_c) #format degrees symbol (e.g. 23°C)

#FIND MIN TEMP, CONVERT & FORMAT
min_temp_f, min_index = weather.find_min(min_list) #this function returns a tuple (temp, index), so we are defining both here.
min_temp_c = weather.convert_f_to_c(min_temp_f) #convert to celcius
min_temp = weather.format_temperature(min_temp_c) #format degrees symbol

#FIND MAX TEMP, CONVERT & FORMAT
max_temp_f, max_index = weather.find_max(max_list) #this function returns a tuple (temp, index), so we are defining both here.
max_temp_c = weather.convert_f_to_c(max_temp_f) #convert to celcius
max_temp = weather.format_temperature(max_temp_c) #format degrees symbol

#DAY OF LOWEST TEMP
#Finding the DAY that the lowest temp occurs on, using the index value from find_min function
min_isodate = weather_data[min_index][0] #targeting weather_data list, [min_index] grabs the correct DAY sublist, [0] targets the FIRST ROW which is isodate string
min_date = weather.convert_date(min_isodate) #convert date from ISO date

#DAY OF HIGHEST TEMP
max_isodate = weather_data[max_index][0] #targeting weather_data list, [max_index] grabs the correct DAY sublist, [0] targets the FIRST ROW which is isodate string
max_date = weather.convert_date(max_isodate) #convert date from ISO date

print(f"{date} Day Overview")
print(f"The lowest temperature will be {min_temp}, and will occur on {min_date}.")
print(f"The highest temperature will be {max_temp}, and will occur on {max_date}.")
print(f"The average low this week is {avg_low}.")
print(f"The average high this week is {avg_high}.")