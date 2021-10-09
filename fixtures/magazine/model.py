from typing import List

import attr
from faker import Faker

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class Store(BaseClass):
    name: str = attr.ib(default=None)

    @staticmethod
    def random():
        name = fake.company()
        return name


@attr.s
class StoreResponse:
    name: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    uuid: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    items: List[str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(str),
            iterable_validator=attr.validators.instance_of(list),
        ),
    )
