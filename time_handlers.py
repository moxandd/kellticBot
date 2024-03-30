from datetime import datetime, time, timedelta
import pytz

def get_time(offset): 
        positive = offset > 0
        if positive:
            time_utc = datetime.now(tz=pytz.utc) + timedelta(seconds=offset)
        else:
            time_utc = datetime.now(tz=pytz.utc) - timedelta(seconds=offset)
        print(time_utc)
        result = time_utc.strftime('%H:%M')
        
        return result