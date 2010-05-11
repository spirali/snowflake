import datetime
import glob

@tag
def today(sections):
    DATE_FORMAT = "%Y-%m-%d"
    return datetime.datetime.now().strftime(DATE_FORMAT)

@tag
def now(sections):
    TIME_FORMAT = "%H:%M:%S"
    return datetime.datetime.now().strftime(TIME_FORMAT)
