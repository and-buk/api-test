from requests import Response

from common.deco import logging as log
from fixtures.store_item.model import Item
from fixtures.validator import Validator


class StoreItem(Validator):
    def __init__(self, app):
        self.app = app

    POST_ITEM = "/item/{}"
    PUT_ITEM = "/item/{}"
    GET_ITEM = "/item/{}"

    @log("Add new item")
    def add_item(
        self, name_item: str, data: Item, header=None, type_response=None
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/storeItem/itemAdd
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_ITEM.format(name_item)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    @log("Change item")
    def change_item(
        self, name_item: str, data: Item, header=None, type_response=None
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/storeItem/itemChange
        """
        response = self.app.client.request(
            method="PUT",
            url=f"{self.app.url}{self.PUT_ITEM.format(name_item)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    @log("Get item")
    def get_item(self, name_item: str, header=None, type_response=None) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/storeMagazine/storeGet
        """
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.GET_ITEM.format(name_item)}",
            headers=header,
        )
        return self.structure(response, type_response=type_response)
