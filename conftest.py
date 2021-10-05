import logging

import pytest

from fixtures.app import Application
from fixtures.auth.model import AuthUserResponse
from fixtures.common_models import UserStore
from fixtures.magazine.model import Store, StoreResponse
from fixtures.register.model import RegisterUser
from fixtures.register.model import RegisterUserResponse
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
    Add new store
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
