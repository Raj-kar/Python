import random
from find_day import find_date
from datetime import date


def valid_date(_date, _month, _year):
    _today = date.today()
    current_year, current_month, current_date = map(
        int, str(_today).split('-'))

    if _year == current_year and _month > current_month or _date > current_date:
        random_date()


def is_leapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def random_year():
    return random.randint(1993, 2020)


def random_month():
    days_31 = [1, 3, 5, 7, 8, 10, 12]
    rand = random.randint(1, 12)
    year = random_year()

    if rand == 2:
        return [29, rand, year] if is_leapYear(year) else [28, rand, year]
    return [31, rand, year] if rand in days_31 else [30, rand, year]


def random_date():
    days_in_month, month, year = random_month()
    rand_date = random.randint(1, days_in_month)
    valid_date(rand_date, month, year)
    return f"{rand_date} / {month} / {year}"


def same_birthday():
    birth_data = {}
    same_birthdate = None
    while True:
        date = random_date()
        same_birthdate = date
        if date in birth_data.keys():
            break
        birth_data[date] = True

    decorate("Same birthdate found !!! ")
    decorate(f"The dd/mm/year is {same_birthdate}")
    date, month, year = map(int, same_birthdate.split('/'))
    decorate(f"And the day was {find_date(date, month, year)}")


same_birthday()
