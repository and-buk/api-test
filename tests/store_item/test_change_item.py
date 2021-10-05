from fixtures.magazine.model import StoreResponse
from fixtures.store_item.model import Item


class TestStoreItem:
    def test_change_item(self, app, item):
        """
        Steps.
            1. Register new user
            2. Check that status code is 200
            3. Check response
        """
        data = Item.random(item.store_uuid, name=item.item)
        res = app.operations_with_store_item.change_item(
            name_item=item.item,
            data=data,
            header=item.header,
            type_response=StoreResponse,
        )
        assert res.status_code == 200
