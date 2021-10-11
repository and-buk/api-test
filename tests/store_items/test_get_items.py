import pytest

from fixtures.store_items.model import ItemsResponse


class TestStoreItem:

    @pytest.mark.positive
    def test_get_all_item(self, app, item):
        """
        Steps.
            1. Register new user
            2. Access to store with valid data
            3. Add user info
            4. Add store
            5. Add item
            6. Try to get all items
            7. Check that status code is 200
            8. Check response
        """
        res = app.store_items.get_all_items(
            header=item.header,
            type_response=ItemsResponse,
        )
        assert res.status_code == 200
