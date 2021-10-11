import pytest

from fixtures.store_item.model import Item
from fixtures.store_item.model import ItemResponse


class TestStoreItem:

    @pytest.mark.positive
    def test_change_item(self, app, item):
        """
        Steps.
            1. Register new user
            2. Access to store with valid data
            3. Add user info
            4. Add store
            5. Add item
            6. Try to change item price
            7. Check that status code is 200
            8. Check response
        """
        data = Item.random(item.store_uuid, name=item.item)
        res = app.operations_with_store_item.change_item(
            name_item=item.item,
            data=data,
            header=item.header,
            type_response=ItemResponse,
        )
        assert res.status_code == 200
