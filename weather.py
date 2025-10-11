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
    
    with open(csv_file, 'r', newline='') as csv_data:
        reader = csv.reader(csv_data)
        for row in reader:
            data.append(row)
    return data
    # NOT WORKING

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
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
