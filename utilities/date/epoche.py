""" Working with epoche time"""
import time
import datetime

# epoche to datetime
current_epoch_time = int(time.time())
cur_date_time = datetime.datetime.fromtimestamp(current_epoch_time)

# datetime to epoche
today_date_time = datetime.datetime.today()
today_epoch = today_date_time.timestamp()

new_date_time = cur_date_time + datetime.timedelta(days=30)
new_epoch_time = new_date_time.timestamp()

print('epoch to datetime:')
print('Today in epoche: {}'.format(current_epoch_time))
print('In date_time:    {}'.format(cur_date_time))

print('\ndatetime to epoch:')
print('Today in epoche: {}'.format(today_date_time))
print('In date_time:    {}'.format(int(today_epoch)))

print('\nAdd 30 days:     {}'.format(new_date_time))
print('In  epoche:      {}'.format(int(new_epoch_time)))

print()

