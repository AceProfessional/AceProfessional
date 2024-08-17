# coding: utf8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-03 21:45:41 UTC+08:00
"""

from fairylandfuture.modules.datetimes import DateTimeModule
from fairylandfuture.enums.datetimes import DateTimeEnum

a = DateTimeModule.datetime_to_timestamp("2024-01-01", _format=DateTimeEnum.date)
a = DateTimeModule.datetime_to_timestamp("2024/01/01", _format="%Y/%m/%d")
a = DateTimeModule.datetime_to_timestamp("2024--01--01", _format="%Y--%m--%d")

print(a)
