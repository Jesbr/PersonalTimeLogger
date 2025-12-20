from datetime import timedelta

def make_time(d, h, m, s):
    return timedelta(days=d, hours=h, minutes=m, seconds=s)

def add_time(d1, h1, m1, s1, d2, h2, m2, s2):
    time1 = make_time(d1, h1, m1, s1)
    time2 = make_time(d2, h2, m2, s2)
    totalSeconds = time1 + time2
    total = int(totalSeconds.total_seconds())

    d = total // 86400
    h = (total % 86400) // 3600
    m = (total % 3600) // 60
    s = total % 60

    return d, h, m, s

def subtract_time(d1, h1, m1, s1, d2, h2, m2, s2):
    time1 = make_time(d1, h1, m1, s1)
    time2 = make_time(d2, h2, m2, s2)
    totalSeconds = time1 - time2
    total = int(totalSeconds.total_seconds())

    sign = "-" if total < 0 else ""
    total = abs(total)

    d = total // 86400
    h = (total % 86400) // 3600
    m = (total % 3600) // 60
    s = total % 60

    return sign, d, h, m, s