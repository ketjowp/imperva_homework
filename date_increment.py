from datetime import date

DATE_DICT = {
    "day": 0,
    "month": 1,
    "year": 2
}
LAST_MONTH = 12
MONTHS_31_DAYS_LIST = [1, 3, 5, 7, 8, 10, 12]
MONTHS_30_DAYS_LIST = [4, 6, 9, 11]


def check_leap_year(year):
    """
    Function for checking if the year is a leap year

    :param year: Integer with the year to check
    :return: True if the year is a leap year, False if not
    """
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


def check_number_of_days_in_the_month(month, is_leap_year):
    """
    Function checking the number of days in the month

    :param month: Integer with a number of the month
    :param is_leap_year: Boolean if the analyzed year is a leap year or not
    :return: Integer with a number of days in the month
    """
    if month in MONTHS_31_DAYS_LIST:
        return 31
    elif month in MONTHS_30_DAYS_LIST:
        return 30
    elif month == 2 and is_leap_year:
        return 29
    elif month == 2:
        return 28
    else:
        raise WrongDateFormatException("Wrong month introduced")


def date_increment(date_to_modify, number_of_days):
    """
    Function which takes date string and returns it incremented by the
    declared number of days

    :param date_to_modify: String in format dd.mm.yyyy
    containing date to modify
    :param number_of_days: Number of days to add
    :return: String with modified date
    """

    if date_to_modify.count('.') != 2 or len(date_to_modify) != 10:
        raise WrongDateFormatException("Provide date in format dd.mm.yyy")

    date_to_modify = date_to_modify.split('.')
    day = int(date_to_modify[DATE_DICT["day"]])
    month = int(date_to_modify[DATE_DICT["month"]])
    year = int(date_to_modify[DATE_DICT["year"]])

    is_leap_year = check_leap_year(year)
    max_number_of_days = check_number_of_days_in_the_month(month, is_leap_year)

    if day > max_number_of_days:
        raise WrongDateFormatException("Wrong day introduced")

    while number_of_days:
        if number_of_days + day > max_number_of_days:
            if month != LAST_MONTH:
                month += 1
            else:
                month = 1
                year += 1
                is_leap_year = check_leap_year(year)

            number_of_days -= max_number_of_days - day + 1
            day = 1
            max_number_of_days = \
                check_number_of_days_in_the_month(month, is_leap_year)

        else:
            day += number_of_days
            number_of_days = 0

    modified_date = date(year=year, month=month, day=day)

    return modified_date.strftime("%d.%m.%Y")


class WrongDateFormatException(Exception):
    pass


if __name__ == '__main__':
    print(date_increment('31.12.2023', 1))
