
from datetime import *
import pytz

tz = pytz.timezone('Africa/Lagos')
berlin_now = datetime.now(tz)

print(berlin_now)