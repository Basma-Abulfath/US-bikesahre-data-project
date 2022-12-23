import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    cities = ["chicago", "new_york_city", "washington"]
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december", "all"]
    days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]

    city = input(f"Enter the city name to start explore it's data from {str(cities)}:")
    city = city.lower()
    while not(city in cities):
        city = input(f"You entered uncorrect city enter it from{str(cities)}")
        city = city.lower()

    day = input(f"Enter the day you want to explore{str(days)} or all if you want to select them all:")
    day = day.lower()
    while not(day in days):
        day = input(f"You entered uncorrect day enter it from{str(days)}")
        day = day.lower()

    month = input(f"Enter the month you want to explore{str(months)} or all if you want to select them all:")
    month = month.lower() 
    while not(month in months):
        month = input(f"You entered uncorrect month enter it from{str(months)}:")
        month = month.lower() 
   
    else:
        print('-'*40)
        return city, month.title(), day.title()

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(r"C:\Users\hp\Desktop\US Bike share project\{}.csv".format(city))
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    df = df.dropna()

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])
    df["day"] = df["Start Time"].dt.day_name()
    df["month"] = df["Start Time"].dt.month_name()
    

    if day == "All":
        pass
    else:
        df = df.set_index(['day'], drop = False)
        df = df.loc[day]

    if month == "All":
        pass
    else:
        df = df.set_index(['month'], append = True, drop= False)
        df = df.loc[month]

    print(df.columns)
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is: {} "
    .format(df["month"].mode()[0]))

    # display the most common day of week
    print("The most common day is: {}"
    .format(df["day"].mode()[0]))

    # display the most common start hour
    print("The most common start hour is: {}"
    .format(df["Start Time"].dt.hour.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    combination_of_staions = df["Start Station"] + df["End Station"]

    # display most commonly used start station
    print("the most common station is: {}"
    .format(df["Start Station"].mode()[0]))

    # display most commonly used end station
    print("the most common end station is: {}"
    .format(df["End Station"].mode()[0]))

    # display most frequent combination of start station and end station trip
    print("the most common combination of start station and end station is: {}"
    .format(combination_of_staions.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    time_period = df["End Time"] - df["Start Time"]

    # display total travel time
    print("Total travel times in the data in hours: {:10.3f}"
    .format(time_period.sum() / pd.Timedelta('1 hour')))

    # display mean travel time
    print("Mean travel time in hours: {:10.3f}"
    .format(time_period.mean() / pd.Timedelta('1 hour')))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Count of subrescribers: {}\nCount of costumers: {}"
    .format(len(df[df["User Type"] == "Subscriber"]),
            len(df[df["User Type"] == "Customer"])))

    # Display counts of gender
    print("\nCount of males: {}\nCount of females: {}"
    .format(len(df[df["Gender"] == "Male"]),
            len(df[df["Gender"] == "Female"])))

    # Display earliest, most recent, and most common year of birth
    print("\nThe earliest brith year: {}\nThe most recent brith year: {}\nThe most common brith year: {}"
    .format(int(df["Birth Year"].min()),
            int(df["Birth Year"].max()),
            int(df["Birth Year"].mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
