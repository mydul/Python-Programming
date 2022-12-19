"""
# import module
import calendar
   
yy = 2023
mm = 01
   
# Display the calendar for 1 month
print(calendar.month(yy, mm)) # calendar() function to print calendar

# using calendar function to print calendar of year
print ("The calendar of year 2023 is :")
print (calendar.calendar(2023, 2, 1, 6))
"""

import calendar

# Prompt the user for a year
year = int(input("Enter a year: "))

# Create a calendar for the year
c = calendar.Calendar()

# Iterate over the months in the year
for month in range(1, 13):
    # Print the month name and year
    print(calendar.month_name[month], year)
    
    # Print the calendar for the month
    print(c.formatmonth(year, month))