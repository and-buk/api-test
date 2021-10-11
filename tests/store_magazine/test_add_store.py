import pytest

from fixtures.common_models import MessageResponse
from fixtures.constants import ResponseText
from fixtures.magazine.model import Store
from fixtures.magazine.model import StoreResponse


class TestStore:

    @pytest.mark.positive
    def test_add_store(self, app, user_info_):
        """
        Steps.
            1. Register new user
            2. Access to store with valid data
            3. Add user info
            4. Try to add new store
            5. Check that status code is 201
            6. Check response
        """
        name_store = Store.random()
        res = app.operations_with_store.add_new_store(
            name_store=name_store,
            header=user_info_.header,
            type_response=StoreResponse,
        )
        assert res.status_code == 201, "Check status code"

    @pytest.mark.negative
    def test_add_already_existing_store(self, app, user_info_):
        """
        Steps.
            1. Register new user
            2. Access to store with valid data
            3. Add user info
            4. Add new store
            5. Try to add an existing store
            6. Check that status code is 400
            7. Check response
        """
        name_store = Store.random()
        app.operations_with_store.add_new_store(
            name_store=name_store,
            header=user_info_.header,
            type_response=StoreResponse,
        )
        res = app.operations_with_store.add_new_store(
            name_store=name_store,
            header=user_info_.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 400, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_STORE_EXIST.format(name_store)
