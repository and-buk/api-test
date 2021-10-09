import attr

from fixtures.base import BaseClass


@attr.s
class PayRequest(BaseClass):
    itemId: int = attr.ib(default=None)

    @staticmethod
    def select_item(item_id):
        return PayRequest(itemId=item_id)


@attr.s
class PayResponse(BaseClass):
    message: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    balance: float = attr.ib(default=None, validator=attr.validators.instance_of(float))
    name: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    price: float = attr.ib(default=None, validator=attr.validators.instance_of(float))
