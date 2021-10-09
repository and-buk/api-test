from requests import Response

from common.deco import logging as log
from fixtures.validator import Validator


class StoreItems(Validator):
    def __init__(self, app):
        self.app = app

    GET_ITEM = "/items"

    @log("Get all items")
    def get_all_items(self, header=None, type_response=None) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/storeItems/itemsGet
        """
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.GET_ITEM}",
            headers=header,
        )
        return self.structure(response, type_response=type_response)
