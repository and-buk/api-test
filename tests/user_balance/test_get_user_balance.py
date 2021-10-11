import pytest

from fixtures.balance.model import BalanceResponse
from fixtures.common_models import MessageResponse
from fixtures.constants import ResponseText


class TestUserBalance:

    @pytest.mark.positive
    def test_get_user_balance(self, app, balance):
        """
        Steps.
            1. Register new user
            2. Access to store with valid data
            3. Add user info
            4. Add new store
            5. Add new item
            6. Add user balance
            7. Try to get user balance
            8. Check that status code is 200
            9. Check response
        """
        fixture_data = balance()
        res = app.operations_with_user_balance.get_user_balance(
            user_id=fixture_data.user_uuid,
            header=fixture_data.header,
            type_response=BalanceResponse,
        )
        assert res.status_code == 200

    @pytest.mark.negative
    def test_get_balance_of_non_existent_user(self, app, balance):
        """
        Steps.
            1. Register new user
            2. Access to store with valid data
            3. Add user info
            4. Add new store
            5. Add new item
            6. Add user balance
            7. Try to get balance of non-existent user
            8. Check that status code is 404
            9. Check response
        """
        fixture_data = balance()
        res = app.operations_with_user_balance.get_user_balance(
            user_id=2000,
            header=fixture_data.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 404
        assert res.data.message == ResponseText.MESSAGE_BALANCE_NOT_FOUND
