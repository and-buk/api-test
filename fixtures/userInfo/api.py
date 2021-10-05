from requests import Response

from common.deco import logging as log
from fixtures.userInfo.model import AddUserInfo
from fixtures.validator import Validator


class UserInfo(Validator):
    def __init__(self, app):
        self.app = app

    POST_USERINFO = "/user_info/{}"
    PUT_USERINFO = "/user_info/{}"
    GET_USERINFO = "/user_info/{}"
    DELETE_USERINFO = "/user_info/{}"

    @log("Add user info")
    def add_user_info(
        self, user_id: int, data: AddUserInfo, header=None, type_response=None
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/userInfo/userInfoAdd
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_USERINFO.format(user_id)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    @log("Update user info")
    def update_user_info(
        self, user_id: int, data: AddUserInfo, header=None, type_response=None
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/userInfo/userInfoUpdate
        """
        response = self.app.client.request(
            method="PUT",
            url=f"{self.app.url}{self.PUT_USERINFO.format(user_id)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    @log("Get user info")
    def get_user_info(self, user_id: int, header=None, type_response=None) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/userInfo/userInfoGet
        """
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.GET_USERINFO.format(user_id)}",
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    @log("Delete user info")
    def delete_user_info(
        self, user_id: int, header=None, type_response=None
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/userInfo/userInfoDelete
        """
        response = self.app.client.request(
            method="DELETE",
            url=f"{self.app.url}{self.DELETE_USERINFO.format(user_id)}",
            headers=header,
        )
        return self.structure(response, type_response=type_response)
