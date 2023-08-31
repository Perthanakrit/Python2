import math

def read_hour():
    return int(input("Enter hour: "))

def read_minute():
    return int(input("Enter minute: "))

def read_second():
    return int(input("Enter second: "))

def to_seconds(h, m, s):
    return (h * 3600) + (m * 60) + s

def time_elapsed(start, finish):
    elapse_time = math.fabs(finish - start)
    hr = elapse_time // 3600
    elapse_time -= hr * 3600
    
    minute = elapse_time // 60
    elapse_time -= minute * 60
    
    sec = elapse_time
    return f"{int(hr)} hours {int(minute)} minutes {int(sec)} seconds."                       

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))
