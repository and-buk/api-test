import pytest

from fixtures.common_models import MessageResponse
from fixtures.constants import ResponseText
from fixtures.store_item.model import ItemResponse


class TestStoreItem:

    @pytest.mark.positive
    def test_get_item(self, app, item):
        """
        Steps.
            1. Register new user
            2. Access to store with valid data
            3. Add user info
            4. Add store
            5. Add item
            6. Try to get item
            7. Check that status code is 200
            8. Check response
        """
        res = app.operations_with_store_item.get_item(
            name_item=item.item,
            header=item.header,
            type_response=ItemResponse,
        )
        assert res.status_code == 200

    @pytest.mark.negative
    def test_get_info_about_non_existent_item(self, app, item):
        """
        Steps.
            1. Register new user
            2. Access to store with valid data
            3. Add user info
            4. Add store
            5. Add item
            6. Try to get info about non-existent item
            7. Check that status code is 404
            8. Check response
        """
        res = app.operations_with_store_item.get_item(
            name_item="MMMdnfnfnf",
            header=item.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 404
        assert res.data.message == ResponseText.MESSAGE_ITEM_NOT_FOUND
