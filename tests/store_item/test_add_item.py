import pytest

from fixtures.common_models import MessageResponse
from fixtures.constants import ResponseText
from fixtures.store_item.model import Item
from fixtures.store_item.model import ItemResponse


class TestStoreItem:

    @pytest.mark.positive
    def test_add_new_item(self, app, store):
        """
        Steps.
            1. Register new user
            2. Access to store with valid data
            3. Add user info
            4. Add store
            5. Try to add item
            6. Check that status code is 201
            7. Check response
        """
        data = Item.random(store.store_uuid)
        res = app.operations_with_store_item.add_item(
            name_item=data.name,
            data=data,
            header=store.header,
            type_response=ItemResponse,
        )
        assert res.status_code == 201

    @pytest.mark.negative
    def test_add_already_existing_item(self, app, store):
        """
        Steps.
            1. Register new user
            2. Access to store with valid data
            3. Add user info
            4. Add store
            5. Add new item
            5. Try to add an existing item
            6. Check that status code is 400
            7. Check response
        """
        data = Item.random(store.store_uuid)
        app.operations_with_store_item.add_item(
            name_item=data.name,
            data=data,
            header=store.header,
            type_response=ItemResponse,
        )
        res = app.operations_with_store_item.add_item(
            name_item=data.name,
            data=data,
            header=store.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 400
        assert res.data.message == ResponseText.MESSAGE_ITEM_EXIST.format(data.name)
