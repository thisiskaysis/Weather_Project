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

min_list = []
max_list = []
date = len(weather_data)

#ADD LOW AND HIGH TEMP DATA TO NEW, SEPERATE LISTS
for data in weather_data:
    if data and len(data) == 3:
        min_list.append(data[1]) #add low temps to new list
        max_list.append(data[2]) #add high temps to new list

#FIND MEAN HIGH AND LOW TEMPS
mean_low = weather.calculate_mean(min_list) #find mean temp
mean_low_celcius = weather.convert_f_to_c(mean_low) #convert to celcius
avg_low = weather.format_temperature(mean_low_celcius) #format degrees symbol
mean_high = weather.calculate_mean(max_list) #find mean temp
mean_high_celcius = weather.convert_f_to_c(mean_high) #convert to celcius
avg_high = weather.format_temperature(mean_high_celcius) #format degrees symbol

#FIND MIN TEMP AND ADD TO LIST, THEN CONVERT AND FORMAT
min = weather.find_min(min_list)
min_list.extend(min) #Add min temp and index to min_list
min_index = min_list[-1] #index for date is now last number of min_list
min_farenheit = min_list[-2] #get temp inside min_list
min_celcius = weather.convert_f_to_c(min_farenheit) #convert to celcius
min_temp = weather.format_temperature(min_celcius) #format degrees symbol

#FIND MAX TEMP AND ADD TO LIST, THEN CONVERT AND FORMAT
max = weather.find_max(max_list)
max_list.extend(max) #add max temp and index to max_list
max_index = max_list[-1] #index for date is now last number of max_list
max_farenheit = max_list[-2] #get temp inside max_list
max_celcius = weather.convert_f_to_c(max_farenheit) #convert to celcius
max_temp = weather.format_temperature(max_celcius) #format degrees symbol

#PULL DATE FROM ORIGINAL LIST FOR HIGHEST AND LOWEST TEMPS
min_data = weather_data[min_index][0] #min_index grabs index no. to access date of min temp inside original weather_data
min_date = weather.convert_date(min_data) #convert date from ISO date
max_data = weather_data[max_index][0] #max_index grabs index no. to access date of max temp inside original weather_data
max_date = weather.convert_date(max_data) #convert date from ISO date

print(f"{date} Day Overview")
print(f"The lowest temperature will be {min_temp}, and will occur on {min_date}.")
print(f"The highest temperature will be {max_temp}, and will occur on {max_date}.")
print(f"The average low this week is {avg_low}.")
print(f"The average high this week is {avg_high}.")