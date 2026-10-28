import threading
import time

# Task 1: Display numbers
def display_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)

# Task 2: Display squares of numbers
def display_squares():
    for i in range(1, 6):
        print(f"Square of {i} = {i * i}")
        time.sleep(1)

# Task 3: Display messages
def display_messages():
    for i in range(1, 6):
        print(f"Python Thread Message {i}")
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=display_numbers)
t2 = threading.Thread(target=display_squares)
t3 = threading.Thread(target=display_messages)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to finish
t1.join()
t2.join()
t3.join()

print("\nAll threads have completed execution.")
