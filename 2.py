import time
timestamp= time.strftime('%H:%M:%S')
print(timestamp)

timestamp= time.strftime('%H')
print(timestamp)

timestamp= time.strftime('%M')
print(timestamp)

timestamp= time.strftime('%S')
print(timestamp)
if(timestamp > 15):
    print("Good DAY")
else:
    PRINT("HELLO")
