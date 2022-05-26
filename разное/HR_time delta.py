
from datetime import datetime

t1 = "Fri 11 Feb 2078 00:05:21 +0400"
t2 = "Mon 29 Dec 2064 03:33:48 -1100"
    
t1_time = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
t2_time = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')

time_sec = (t1_time-t2_time).total_seconds()

print(round(abs(time_sec)))
