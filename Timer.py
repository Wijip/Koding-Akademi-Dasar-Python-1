import time

# function to display time
def display_time(time_str):
    print("\r", time_str, end="", flush=True)

# function to get timer input from user
def get_timer():
    timer_input = input("\nEnter timer value in minutes: ")
    try:
        timer_val = int(timer_input)
        return timer_val
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return get_timer()

# get timer value from user
timer = get_timer()
end_time = time.time() + timer * 60

# display current time and countdown timer
while time.time() < end_time:
    current_time = time.strftime("%H:%M:%S", time.localtime())
    time_left = int(end_time - time.time())
    timer_str = "Timer: {:02d}:{:02d}".format(time_left // 60, time_left % 60)
    display_time(current_time + " " + timer_str)
    time.sleep(1)

# display timer ended message
display_time("Timer ended!")
