import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts an ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # date = datetime.strftime(iso_string, "%A %d %m %Y")
    
    iso_date = datetime.fromisoformat(iso_string)
    formatted_date = datetime.strftime(iso_date, "%A %d %B %Y")
    return formatted_date


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    fahrenheit = float(temp_in_fahrenheit)
    celcius = float(fahrenheit - 32) * 5 / 9
    return round(celcius, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    weather_data = [float(data) for data in weather_data]
    total = sum(weather_data)
    length = len(weather_data)
    return total/length

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    
    data = []
    
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row and len(row) == 3:
                date = row[0]
                min = int(row[1])
                max = int(row[2])
                output = [date, min, max]
                data.append(output)
    
    return data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    
    if not weather_data:
        return ()
    
    min_value = min(weather_data)
    last_index = 0

    for index, number in enumerate(weather_data):
        if number > min_value:
            continue
        if number == min_value:
            last_index = index
    
    float_value = float(min_value)
    
    return float_value, last_index



def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    
    max_value = max(weather_data)
    max_index = 0

    for index, value in enumerate(weather_data):
        if value < max_value:
            continue
        if value == max_value:
            max_index = index
    
    float_value = float(max_value)
    return float_value, max_index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
    min_list = []
    max_list = []
    date = len(weather_data)

    #ADD LOW AND HIGH TEMP DATA TO NEW, SEPERATE LISTS
    for data in weather_data:
        if data and len(data) == 3:
            min_list.append(data[1])
            max_list.append(data[2])

    #FIND MEAN (AVG) LOW TEMP
    mean_low_f = calculate_mean(min_list)
    mean_low_c = convert_f_to_c(mean_low_f)
    avg_low = format_temperature(mean_low_c)

    #FIND MEAN (AVG) HIGH TEMP
    mean_high_f = calculate_mean(max_list)
    mean_high_c = convert_f_to_c(mean_high_f)
    avg_high = format_temperature(mean_high_c)

    #FIND MIN TEMP, CONVERT & FORMAT
    min_temp_f, min_index = find_min(min_list)
    min_temp_c = convert_f_to_c(min_temp_f)
    min_temp = format_temperature(min_temp_c)

    #FIND MAX TEMP, CONVERT & FORMAT
    max_temp_f, max_index = find_max(max_list)
    max_temp_c = convert_f_to_c(max_temp_f)
    max_temp = format_temperature(max_temp_c)

    #DAY OF LOWEST TEMP
    min_isodate = weather_data[min_index][0]
    min_date = convert_date(min_isodate)

    #DAY OF HIGHEST TEMP
    max_isodate = weather_data[max_index][0]
    max_date = convert_date(max_isodate)

    return f"""{date} Day Overview
  The lowest temperature will be {min_temp}, and will occur on {min_date}.
  The highest temperature will be {max_temp}, and will occur on {max_date}.
  The average low this week is {avg_low}.
  The average high this week is {avg_high}.
"""


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    daily_summary = ""

    for data in weather_data:
        if data and len(data) == 3:
            iso_date = data[0]
            date = convert_date(iso_date)
            min_temp_c = convert_f_to_c(data[1])
            max_temp_c = convert_f_to_c(data[2])
            min_temp = format_temperature(min_temp_c)
            max_temp = format_temperature(max_temp_c)

            daily_summary += f"---- {date} ----\n  Minimum Temperature: {min_temp}\n  Maximum Temperature: {max_temp}\n\n"
            
    return daily_summary