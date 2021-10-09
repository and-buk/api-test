import attr
from faker import Faker

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class Auth(BaseClass):
    username: str = attr.ib(default=None)
    password: str = attr.ib(default=None)

    @staticmethod
    def random():
        return Auth(username=fake.email(), password=fake.password())


@attr.s
class AuthUserResponse:
    access_token: str = attr.ib(validator=attr.validators.instance_of(str))
