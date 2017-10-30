import time


def datetime_to_timestamp(dt):
    if not dt:
        return None
    return int(time.mktime(dt.timetuple()))