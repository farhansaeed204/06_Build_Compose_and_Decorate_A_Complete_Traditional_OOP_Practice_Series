class Logger:
    def __init__(self):
        print("Logger initialized. Object created.")

    def __del__(self):
        print("Logger destroyed. Object deleted.")

# Create an object
log = Logger()

# Optionally delete it manually to trigger destructor
del log

# Or let Python handle it automatically at the end of program
