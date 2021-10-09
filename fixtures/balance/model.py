import random

import attr

from fixtures.base import BaseClass


@attr.s
class Balance(BaseClass):
    balance: int = attr.ib(default=None)

    @staticmethod
    def random(value: int = None):
        if value is not None:
            return Balance(balance=value)
        return Balance(balance=random.randint(100000, 200000))


@attr.s
class BalanceResponse(BaseClass):
    message: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    balance: float = attr.ib(default=None, validator=attr.validators.instance_of(float))
