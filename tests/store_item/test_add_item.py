from fixtures.magazine.model import StoreResponse
from fixtures.store_item.model import Item


class TestStoreItem:
    def test_add_new_item(self, app, store):
        """
        Steps.
            1. Try to login user with valid data
            2. Check that status code is 200
            3. Check response
        """
        data = Item.random(store.store_uuid)
        res = app.operations_with_store_item.add_item(
            name_item=data.name,
            data=data,
            header=store.header,
            type_response=StoreResponse,
        )
        assert res.status_code == 201
