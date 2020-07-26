from datetime import datetime


def get_time_zone(time=datetime.now()):
    current_time = time.strftime('%H:%M')
    if int(current_time[3:5]) < 30:
        minute = '00'
    else:
        minute = '30'

    hour = current_time[0:2]
    if current_time < '12:00':
        time_zone = '-' + hour + ':' + minute
    else:
        time_zone = '+' + hour + ':' + minute

    if time_zone == '-00:00':
        time_zone = '+00:00'

    return time_zone

