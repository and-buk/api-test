import random
from typing import Optional

import attr
from faker import Faker

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class Item(BaseClass):
    name: str = attr.ib(default=None)
    price: int = attr.ib(default=None)
    store_id: int = attr.ib(default=None)

    @staticmethod
    def random(store_id):
        return Item(name=fake.catch_phrase(),
                    price=random.randint(100, 100000),
                    store_id=store_id
                    )


@attr.s
class ItemResponse:
    name: str = attr.ib(default=None)
    price: int = attr.ib(default=None)
    itemID: int = attr.ib(default=None)
