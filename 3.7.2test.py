import time
StartTime = time.time()
for i in range(1000000):
    i**2
print(time.time()-StartTime)