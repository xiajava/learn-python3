#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp
import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    # dt_str转换为datetime
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # tz_str转换为timezone
    m = re.match(r'^(UTC)([+-]?)([0-9]|0[0-9]|1[0-2])\:(00)$', tz_str)
    sign = -1 if m.group(2) is '-' else 1
    tz = sign * int(m.group(3))
    # 本地时间转换为UTC时间
    tz_utc = timezone(timedelta(hours=tz))
    dt_utc = dt.replace(tzinfo=tz_utc)
    # datetime转换为timestamp
    return dt_utc.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
print(t1)
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print(t2)
print('Pass')
