class Countdown:
    def __init__(self, start):
        self.current = start + 1  # We'll decrement first in __next__

    def __iter__(self):
        return self # Return the iterator object (self)

    def __next__(self):
        self.current -= 1 # Return next value in countdown
        if self.current < 0:
            raise StopIteration  # Signals end of iteration
        return self.current

print("Countdown from 5:")
for num in Countdown(5):
    print(num, end=" ")  

print("\n\nCountdown from 3:")
for num in Countdown(3):
    print(num, end=" ")  