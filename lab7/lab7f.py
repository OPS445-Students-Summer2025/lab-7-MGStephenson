#!/usr/bin/env python3
# Student ID: MGStephenson

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
       function attributes: __init__, format_time, valid_time,
                            change_time, sum_times, time_to_sec
    """

    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second
   
    def __str__(self):
        """Return a user-friendly string version of the Time object"""
        return self.format_time()

    def __repr__(self):
        '''return a string representation for the object self'''
        '''just instead of ':', you are required use the '.'  in the formatting string.'''
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def __add__(self, t2):
        """return the result by using sum_times() method"""
        return self.sum_times(t2)

    def format_time(self):
        """Return time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def valid_time(self):
        """Check for the validity of the time object attributes:
        24 > hour >= 0, 60 > minute >= 0, 60 > second >= 0
        """
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

    def time_to_sec(self):
        """Convert the time object to a single integer representing
        the number of seconds since midnight"""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def change_time(self, seconds):
        """Change the time object by adding the given number of seconds"""
        total_seconds = self.time_to_sec() + seconds
        new_time = sec_to_time(total_seconds)
        self.hour = new_time.hour
        self.minute = new_time.minute
        self.second = new_time.second
        return None

    def sum_times(self, t2):
        """Add this time object with another time object and return the result"""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)


# Standalone function to convert seconds into a Time object
def sec_to_time(seconds):
    """Convert a given number of seconds to a Time object"""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


# Optional: test block
if __name__ == '__main__':
    t1 = Time(1, 30, 0)
    t2 = Time(2, 45, 30)
    print("Time 1:", t1.format_time())
    print("Time 2:", t2.format_time())

    print("Valid Time 1:", t1.valid_time())
    print("Valid Time 2:", t2.valid_time())

    total = t1.sum_times(t2)
    print("Sum of Time 1 and Time 2:", total.format_time())

    t1.change_time(500)
    print("Time 1 after adding 500 seconds:", t1.format_time())
