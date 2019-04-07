from datetime import timedelta, datetime

def add_gigasecond(moment):
    return moment + timedelta(seconds=10**9)
