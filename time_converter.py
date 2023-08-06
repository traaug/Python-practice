def format_duration(second):
    if second == 0:
        return "Now"
    minute = second // 60
    second %= 60
    hour = minute // 60
    minute %= 60
    if hour != 0:
        if hour == 1:
            print(hour, "hour", end=' ')
        else:
            print(hour, "hours", end=' ')

    if minute != 0:
        if minute == 1:
            print(minute, "minute", end=' ')
        else:
            print(minute, "minutes", end=' ')

    if second != 0:
        if second == 1:
            print(second, "second", end=' ')
        else:
            print(second, "seconds", end=' ')


format_duration(68)
