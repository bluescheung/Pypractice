#!usr/bin/env python3

import re
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str,tz_str):
    dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    t=re.match(r'UTC([+-]\d+)\:00$',tz_str)
    tr=int(t.group(1))
    print(tr)
    tz_utc=timezone(timedelta(hours=tr))
    dt=dt.replace(tzinfo=tz_utc)
    dt=dt.timestamp()
    return dt


if __name__=='__main__':
    t1=to_timestamp('2015-6-1 08:10:30','UTC+7:00')
    assert t1 == 1433121030.0,t1
    print('Pass')
