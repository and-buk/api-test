from fixtures.auth.api import AuthUser
from fixtures.magazine.api import StoreMagazine
from fixtures.register.api import Register
from fixtures.requests import Client
from fixtures.store_item.api import StoreItem
from fixtures.userInfo.api import UserInfo


class Application:
    def __init__(self, url):
        self.url = url

        # В качестве параметра объекта конструктор HTTP-запроса
        self.client = Client

        self.register = Register(self)
        self.auth = AuthUser(self)
        self.user_info = UserInfo(self)
        self.operations_with_store = StoreMagazine(self)
        self.operations_with_store_item = StoreItem(self)
