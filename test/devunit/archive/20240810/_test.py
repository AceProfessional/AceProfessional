# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-08-10 13:16:27 UTC+08:00
"""

from fairylandfuture.enums.enconding import EncodingEnum
from fairylandfuture.core.superclass.enumerate import BaseEnum
from fairylandfuture.modules.validations.strings import ValidateStringModule

print(EncodingEnum.default.value)

print(ValidateStringModule.valid_parentheses(""))
