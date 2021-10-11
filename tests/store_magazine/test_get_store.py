import pytest

from fixtures.common_models import MessageResponse
from fixtures.constants import ResponseText
from fixtures.magazine.model import StoreResponse


class TestStore:

    @pytest.mark.positive
    def test_get_store_info(self, app, store):
        """
        Steps.
            1. Register new user
            2. Access to store with valid data
            3. Add user info
            4. Add store
            5. Try to get info about created store
            6. Check that status code is 200
            7. Check response
        """
        res = app.operations_with_store.get_store(
            name_store=store.store,
            header=store.header,
            type_response=StoreResponse,
        )
        assert res.status_code == 200, "Check status code"

    @pytest.mark.negative
    def test_get_info_about_non_existent_store(self, app, store):
        """
        Steps.
            1. Register new user
            2. Access to store with valid data
            3. Add user info
            4. Add store
            5. Try to get info about non-existent store
            6. Check that status code is 404
            7. Check response
        """
        res = app.operations_with_store.get_store(
            name_store=1000,
            header=store.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 404, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_STORE_NOT_FOUND
