import time

t = 1678432801
sj = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(round(t)))
print(time.localtime(t))
print(sj)
