# Contains Helper Function #

# Converts a QDate to a formatted string
from PyQt5.QtCore import QDate
def format_qdate(date):
    # Format would for example be Sunday 1/1/2020
    return date.longDayName(date.dayOfWeek()) + " " + \
        str(date.day()) + "/" + str(date.month()) + "/" + str(date.year())


# Converts a string date and returns it back as a a QDate Object
def converted_date(str_date):
    date = QDate()
    # If a date exists in QSettings to use then set that date to start date
    if str_date is not None:
        str_list = str_date.split('/')
        date.setDate(int(str_list[2]), int(str_list[1]), int(str_list[0]))
    # Otherwise just set it to year 2020
    else:
        date.setDate(2020, 1, 1)

    return date