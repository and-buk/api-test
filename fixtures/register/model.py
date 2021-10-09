import attr
from faker import Faker

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class RegisterUser(BaseClass):
    username: str = attr.ib(default=None)
    password: str = attr.ib(default=None)

    @staticmethod
    def random():
        return RegisterUser(username=fake.email(), password=fake.password())


@attr.s
class RegisterUserResponse:
    message: str = attr.ib(validator=attr.validators.instance_of(str))
    uuid: int = attr.ib(validator=attr.validators.instance_of(int))
