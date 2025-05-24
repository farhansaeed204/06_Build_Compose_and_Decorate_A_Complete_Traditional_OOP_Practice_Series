class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # The iterator object itself

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value

# Using the Countdown class in a for-loop
for number in Countdown(5):
    print(number)
