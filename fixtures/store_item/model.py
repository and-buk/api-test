import random

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
    def random(store_id, name=None):
        if name is None:
            name = fake.catch_phrase()
        return Item(name=name, price=random.randint(100, 100000), store_id=store_id)


@attr.s
class ItemResponse:
    name: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    price: int = attr.ib(default=None, validator=attr.validators.instance_of(int))
    itemID: int = attr.ib(default=None, validator=attr.validators.instance_of(int))
