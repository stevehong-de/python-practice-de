from datetime import datetime
from datetime import timedelta
import time

# go through this in command line (python3)

# Generate datetime now
datetime_now = datetime.now()
print(datetime_now)

# Modify datetime now minus one hour
datetime_now_minus_one_hour = datetime_now - timedelta(hours=1)
print(datetime_now_minus_one_hour)

# delete the decimals from the timestamp
datetime_minus_one_reformatted = datetime_now_minus_one_hour.strftime("%d/%m/%Y %H:%M:%S")
print(datetime_minus_one_reformatted)

# Convert datetime to epoch using timestamp()
epoch = datetime_now.timestamp()
print(epoch)

# turn epoch into custom datetime and format
ts_from_epoch = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))
print(ts_from_epoch)
print(datetime.utcfromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S'))
