class Counter:
    # Class variable to track number of objects created
    count = 0

    def __init__(self):
        # Increment count whenever a new object is created
        Counter.count += 1

    @classmethod
    def show_count(cls):
        # Display the current object count using cls
        print("Number of objects created:", cls.count)

# Example usage
c1 = Counter()
c2 = Counter()
c3 = Counter()

Counter.show_count()  # Output: Number of objects created: 3
