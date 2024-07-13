import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('\r', timer , end='')
        time.sleep(1)
        t -= 1
    print('\n')
    print('Timer Completed')


t = input("enter time in seconds: ")

countdown(int(t))

