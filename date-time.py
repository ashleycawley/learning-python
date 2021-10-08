from datetime import datetime

# Today's date and time
today = datetime.now()
print(today)

# How to work out the time between a point in the past and now (Delta Time)
first_of_the_year = datetime(2020, 1, 1)
how_many_days = today - first_of_the_year
print(how_many_days)