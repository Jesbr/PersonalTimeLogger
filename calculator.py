from datetime import timedelta

def make_time(d, h, m, s):
    return timedelta(days=d, hours=h, minutes=m, seconds=s)

def format_timedelta(td):
    total_seconds = int(td.total_seconds())
    total_seconds = abs(total_seconds)

    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    dSpace = ""
    if (days < 10):
        dSpace = "  "
    elif (days < 100):
        dSpace = " "
    hSpace = ""
    if (hours < 10):
        hSpace = " "
    mSpace = ""
    if (minutes < 10):
        mSpace = " "
    sSpace = ""
    if (seconds < 10):
        sSpace = " "

    return f"{dSpace}{days}d {hSpace}{hours}h {mSpace}{minutes}m {sSpace}{seconds}s"

def add_time(d1, h1, m1, s1, d2, h2, m2, s2):
    time1 = make_time(d1, h1, m1, s1)
    time2 = make_time(d2, h2, m2, s2)
    totalSeconds = time1 + time2

    formatTime1 = format_timedelta(time1)
    formatTime2 = format_timedelta(time2)
    formatTime3 = format_timedelta(totalSeconds)
    resultTime = f"({formatTime1}) + ({formatTime2}) = ({formatTime3})"

    total = int(totalSeconds.total_seconds())

    d = total // 86400
    h = (total % 86400) // 3600
    m = (total % 3600) // 60
    s = total % 60

    return resultTime, d, h, m, s

def subtract_time(d1, h1, m1, s1, d2, h2, m2, s2):
    time1 = make_time(d1, h1, m1, s1)
    time2 = make_time(d2, h2, m2, s2)
    totalSeconds = time1 - time2

    formatTime1 = format_timedelta(time1)
    formatTime2 = format_timedelta(time2)
    formatTime3 = format_timedelta(totalSeconds)
    resultTime = f"({formatTime1}) - ({formatTime2}) = -({formatTime3})"

    total = int(totalSeconds.total_seconds())

    sign = "-" if total < 0 else ""
    total = abs(total)

    d = total // 86400
    h = (total % 86400) // 3600
    m = (total % 3600) // 60
    s = total % 60

    return resultTime, sign, d, h, m, s