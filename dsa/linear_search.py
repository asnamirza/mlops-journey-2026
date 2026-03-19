# 1. The Data Structure: A simple list of numbers
my_drawer = [10, 42, 7, 99, 3]

# 2. The Algorithm: Checking them one by one
for ball in my_drawer:
    print(f"Checking: {ball}")
    
    # If the ball is exactly 99, we found it!
    if ball == 99:
        print("🎉 We found 99! Stop looking.")
        break # This tells the computer to stop searching