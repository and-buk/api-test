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
    name: str = attr.ib(default=None)
    uuid: str = attr.ib(default=None)
    items: List[str] = attr.ib(default=None)
