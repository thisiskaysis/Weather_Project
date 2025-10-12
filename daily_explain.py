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

#THIS NEEDS TO RETURN A STRING! NOT A LIST

daily_summary = "" #empty string to add each iteration summary

for data in weather_data:
    if data and len(data) == 3:
        iso_date = data[0] #take date from first row
        date = convert_date(iso_date) #convert date from ISO date
        min_temp_c = convert_f_to_c(data[1]) #convert min temp to celcius
        max_temp_c = convert_f_to_c(data[2]) #convert max temp to celcius
        min_temp = format_temperature(min_temp_c) #format degrees celcius
        max_temp = format_temperature(max_temp_c) #format degrees celcius

        daily_summary += f"---- {date} ----\n  Minimum Temperature: {min_temp}\n  Maximum Temperature: {max_temp}\n\n"
        #this is the string we are adding to our empty string each iteration.
        #the \n are line breaks
        #I tried writing in triple brackets but couldn't get line breaks correct. wrote like this using \n newline breaks in order to pass test
            
print(daily_summary)