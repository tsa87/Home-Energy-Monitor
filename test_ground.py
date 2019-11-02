import datetime


def get_time():
    now = datetime.datetime.now()
    current_time = int(now.strftime("%H"))


    if current_time < 12:
        return "Good morning, "
    elif current_time < 18:
        return "Good evening, "
    else:
        return "Good night, "
