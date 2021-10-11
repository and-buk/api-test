import pytest

from fixtures.balance.model import Balance
from fixtures.balance.model import BalanceResponse
from fixtures.common_models import MessageResponse
from fixtures.constants import ResponseText


class TestUserBalance:

    @pytest.mark.positive
    def test_add_user_balance(self, app, store):
        """
        Steps.
            1. Register new user
            2. Access to store with valid data
            3. Add user info
            4. Add new store
            5. Try do add user balance
            6. Check that status code is 201
            7. Check response
        """
        data = Balance.random()
        res = app.operations_with_user_balance.add_user_balance(
            user_id=store.user_uuid,
            data=data,
            header=store.header,
            type_response=BalanceResponse,
        )
        assert res.status_code == 201

    @pytest.mark.negative
    def test_add_balance_to_non_existent_user(self, app, store):
        """
        Steps.
            1. Register new user
            2. Access to store with valid data
            3. Add user info
            4. Add new store
            5. Try do add balance to non-existent user
            6. Check that status code is 404
            7. Check response
        """
        data = Balance.random()
        res = app.operations_with_user_balance.add_user_balance(
            user_id=2000,
            data=data,
            header=store.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 404
        assert res.data.message == ResponseText.MESSAGE_USER_NOT_FOUND_DOT
