from datetime import date, timedelta

def meetup(year, month, week, day_of_week):
    convert_weekday = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
                       'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    weekday = convert_weekday[day_of_week]

    d = date(year, month, 1)  # first day of given month
    d += timedelta(days = weekday - d.weekday())
    if d.month < month:
        d += timedelta(days = 7)

    counter = 1
    while d.month == month:
        if week == "teenth" and d.day > 12 and d.day < 20:
            return d
        if week == '1st' and counter == 1:
            return d
        if week == '2nd' and counter == 2:
            return d
        if week == '3rd' and counter == 3:
            return d
        if week == '4th' and counter == 4:
            return d
        if week == '5th' and counter == 5:
            return d
        d += timedelta(days = 7)
        counter += 1
    if week == 'last':
        if d.month != month:
            d += timedelta(days = -7)
        return d
    raise MeetupDayException('Date does not exist.')

class MeetupDayException(Exception):
    "Raised if made it all the way through the dates"
    pass
