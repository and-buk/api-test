import pytest

from fixtures.common_models import MessageResponse
from fixtures.constants import ResponseText
from fixtures.pay.model import PayRequest, PayResponse


class TestPayItem:

    @pytest.mark.positive
    def test_pay_item(self, app, balance):
        """
        Steps.
            1. Register new user
            2. Access to store with valid data
            3. Add user info
            4. Add new store
            5. Add new item info
            6. Add user balance
            7. Try to pay for item
            8. Check that status code is 200
            9. Check response
        """
        fixture_data = balance()
        req_data = PayRequest.select_item(item_id=fixture_data.item_uuid)
        res = app.buying_product.pay_for_item(
            user_id=fixture_data.user_uuid,
            data=req_data,
            header=fixture_data.header,
            type_response=PayResponse,
        )
        assert res.status_code == 200, "Check status code"

    @pytest.mark.negative
    def test_pay_for_non_existetnt_item(self, app, balance):
        """
        Steps.
            1. Register new user
            2. Access to store with valid data
            3. Add user info
            4. Add new store
            5. Add new item info
            6. Add user balance
            7. Try to pay for item
            8. Check that status code is 404
            9. Check response
        """
        fixture_data = balance()
        req_data = PayRequest.select_item(item_id=2000)
        res = app.buying_product.pay_for_item(
            user_id=fixture_data.user_uuid,
            data=req_data,
            header=fixture_data.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 404, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_ITEM_NOT_FOUND

    @pytest.mark.negative
    def test_pay_for_item_with_no_money(self, app, balance):
        """
        Steps.
            1. Register new user
            2. Access to store with valid data
            3. Add user info
            4. Add new store
            5. Add new item info
            6. Add user balance
            7. Try to pay for item
            8. Check that status code is 400
            9. Check response
        """
        fixture_data = balance(set_amount=0)
        req_data = PayRequest.select_item(item_id=fixture_data.item_uuid)
        res = app.buying_product.pay_for_item(
            user_id=fixture_data.user_uuid,
            data=req_data,
            header=fixture_data.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 400, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_NO_MONEY.format(float(fixture_data.user_balance.balance),
                                                                        float(fixture_data.price))


