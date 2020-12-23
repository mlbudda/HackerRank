# Time Conversion

def timeConversion(s):
    """ Converts to military (24-hour) time """
    new_s = ''
    if s[-2:] == 'PM' and s[:2] != '12':
        new_s = str(int(s[:2]) + 12) + s[2:-2]
    elif s[-2:] == 'AM' and s[:2] == '12':
        new_s = '0' + str(int(s[:2]) - 12) + s[2:-2]
    else:
        new_s = s[:-2]
    return new_s


# Running some tests..
print(timeConversion('07:05:45PM') == '19:05:45')