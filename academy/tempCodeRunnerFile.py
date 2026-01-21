from datetime import timedelta
from datetime import date

today = date.today()
yesterday = today - timedelta(days = 1)
sevenDay = today - timedelta(days=6)
print(sevenDay)