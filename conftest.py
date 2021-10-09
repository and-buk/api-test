import logging

import pytest

from fixtures.app import Application
from fixtures.auth.model import AuthUserResponse
from fixtures.balance.model import Balance, BalanceResponse
from fixtures.common_models import UserStore
from fixtures.magazine.model import Store
from fixtures.magazine.model import StoreResponse
from fixtures.register.model import RegisterUser
from fixtures.register.model import RegisterUserResponse
from fixtures.store_item.model import Item
from fixtures.store_item.model import ItemResponse
from fixtures.userInfo.model import AddUserInfo

logger = logging.getLogger("api")


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://stores-tests-api.herokuapp.com",
    ),


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--api-url")
    logger.info(f"Start api tests, url is {url}")
    return Application(url)


@pytest.fixture
def register_user(app) -> UserStore:
    """
    Register new user
    """
    data = RegisterUser.random()
    res = app.register.register(data=data, type_response=RegisterUserResponse)
    data = UserStore(user=data, user_uuid=res.data.uuid)
    return data


@pytest.fixture
def auth_user(app, register_user) -> UserStore:
    """
    Login user
    """
    res = app.auth.login(data=register_user.user, type_response=AuthUserResponse)
    token = res.data.access_token
    header = {"Authorization": f"JWT {token}"}
    data = UserStore(**register_user.to_dict())
    data.header = header
    return data


@pytest.fixture
def user_info_(app, auth_user) -> UserStore:
    """
    Add user info
    """
    data = AddUserInfo.random()
    app.user_info.add_user_info(
        user_id=auth_user.user_uuid, data=data, header=auth_user.header
    )
    data_user = UserStore(**auth_user.to_dict())
    data_user.user_info = data
    return data_user


@pytest.fixture
def store(app, user_info_) -> UserStore:
    """
    Add store
    """
    name_store = Store.random()
    res = app.operations_with_store.add_new_store(
        name_store=name_store,
        header=user_info_.header,
        type_response=StoreResponse,
    )
    data_store = UserStore(**user_info_.to_dict())
    data_store.store = name_store
    data_store.store_uuid = res.data.uuid
    return data_store


@pytest.fixture
def item(app, store) -> UserStore:
    """
    Add item
    """
    data = Item.random(store_id=store.store_uuid)
    res = app.operations_with_store_item.add_item(
        name_item=data.name,
        data=data,
        header=store.header,
        type_response=ItemResponse,
    )
    data_item = UserStore(**store.to_dict())
    data_item.item = data.name
    data_item.price = data.price
    data_item.item_uuid = res.data.itemID
    return data_item


@pytest.fixture
def balance(app, item):
    """
    Add and set user balance
    """
    def _set_balance(set_amount=None) -> UserStore:
        if set_amount is not None:
            data = Balance.random(value=set_amount)
        else:
            data = Balance.random()
        app.operations_with_user_balance.add_user_balance(
            user_id=item.user_uuid,
            data=data,
            header=item.header,
            type_response=BalanceResponse,
        )
        data_balance = UserStore(**item.to_dict())
        data_balance.user_balance = data
        return data_balance
    return _set_balance
