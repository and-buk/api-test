from requests import Response

from common.deco import logging as log
from fixtures.balance.model import Balance
from fixtures.validator import Validator


class UserBalance(Validator):
    def __init__(self, app):
        self.app = app

    POST_BALANCE = "/balance/{}"
    GET_BALANCE = "/balance/{}"

    @log("Add user balance")
    def add_user_balance(
        self, user_id: int, data: Balance, header=None, type_response=None
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/userBalance/balanceAdd
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_BALANCE.format(user_id)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    @log("Get user balance")
    def get_user_balance(
        self, user_id: int, header=None, type_response=None
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/userBalance/balanceGet
        """
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.GET_BALANCE.format(user_id)}",
            headers=header,
        )
        return self.structure(response, type_response=type_response)
