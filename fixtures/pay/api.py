from requests import Response

from common.deco import logging as log
from fixtures.pay.model import PayRequest
from fixtures.validator import Validator


class BuyItem(Validator):
    def __init__(self, app):
        self.app = app

    POST_PAY = "/pay/{}"

    @log("Pay item")
    def pay_for_item(
        self, user_id: int, data: PayRequest, header=None, type_response=None
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/pay/pay
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_PAY.format(user_id)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)
