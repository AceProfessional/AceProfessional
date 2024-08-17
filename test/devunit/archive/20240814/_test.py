# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-08-14 17:13:15 UTC+08:00
"""

from fairylandfuture.structures.general.api import ResponseStructure


if __name__ == "__main__":
    data = {"key": '["asdsa"]'}
    response = ResponseStructure(code=200, data=data)
    d = response.asdict
    d.update(code=2000)
    print(repr(response), repr(response.to_dict(ignorenone=True)), repr(d))
