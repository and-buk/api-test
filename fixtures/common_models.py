import attr

from fixtures.balance.model import Balance
from fixtures.base import BaseClass
from fixtures.register.model import RegisterUser
from fixtures.userInfo.model import AddUserInfo


@attr.s
class MessageResponse:
    message: str = attr.ib(validator=attr.validators.instance_of(str))


@attr.s
class UserStore(BaseClass):
    user: RegisterUser = attr.ib(default=None)
    user_uuid: int = attr.ib(default=None)
    header: dict = attr.ib(default=None)
    user_info: AddUserInfo = attr.ib(default=None)
    store: str = attr.ib(default=None)
    store_uuid: int = attr.ib(default=None)
    item: str = attr.ib(default=None)
    price: int = attr.ib(default=None)
    item_uuid: int = attr.ib(default=None)
    user_balance: Balance = attr.ib(default=None)


@attr.s
class AuthInvalidResponse:
    description: str = attr.ib(validator=attr.validators.instance_of(str))
    error: str = attr.ib(validator=attr.validators.instance_of(str))
    status_code: int = attr.ib(validator=attr.validators.instance_of(int))
