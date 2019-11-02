import datetime

def get_time():
    now = datetime.datetime.now()
    current_time = int(now.strftime("%H"))

    if current_time < 12:
        return "Good morning, "
    elif current_time < 18:
        return "Good afternoon, "
    else:
        return "Good night, "

def get_color(level):
    if level == "high":
        return "red"
    elif level == "normal":
        return "yellow"
    elif level == "low":
        return "green"
