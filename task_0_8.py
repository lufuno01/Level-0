def convert(number):
    hours = number // 60
    minutes = number - hours * 60
    string_hours = " hours"
    string_min = " minutes"

    if (hours == 1):
        string_hours = " hour"

    if (minutes == 1):
        string_min = " minute"

    if (minutes > 0 and hours > 0):
        return str(hours) + string_hours + ", " + str(minutes) + string_min
    if (hours > 1 and minutes > 1):
        return str(hours) + string_hours + ", " + str(minutes) + string_min
    if (minutes == 0):
        return str(hours) + string_hours + ", " + str(minutes) + string_min
    elif (hours == 0):
        return str(hours) + string_hours + ", " + str(minutes) + string_min

    return str(hours) + string_hours


print(convert(120))

