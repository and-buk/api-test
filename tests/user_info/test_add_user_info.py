import pytest

from fixtures.common_models import MessageResponse, AuthInvalidResponse
from fixtures.constants import ResponseText
from fixtures.userInfo.model import AddUserInfo


class TestUserInfo:

    @pytest.mark.positive
    def test_add_user_info(self, app, auth_user):
        """
        Steps.
            1. Register new user
            2. Get access to store
            3. Try to add user info
            4. Check that status code is 200
            5. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.add_user_info(
            user_id=auth_user.user_uuid,
            data=data,
            header=auth_user.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 200, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_ADD_USER_INFO

    @pytest.mark.negative
    def test_add_info_of_non_existent_user(self, app, auth_user):
        """
        Steps.
            1. Register new user
            2. Get access to store
            3. Try to add info about non-existent user
            4. Check that status code is 404
            5. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.add_user_info(
            user_id=1000,
            data=data,
            header=auth_user.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 404, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_USER_NOT_FOUND

    @pytest.mark.negative
    def test_add_already_existing_info_of_user(self, app, auth_user):
        """
        Steps.
            1. Register new user
            2. Get access to store
            3. Add user info
            4. Try to add the same info about user
            5. Check that status code is 400
            6. Check response
        """
        data = AddUserInfo.random()
        app.user_info.add_user_info(
            user_id=auth_user.user_uuid,
            data=data,
            header=auth_user.header,
            type_response=MessageResponse,
        )
        res = app.user_info.add_user_info(
            user_id=auth_user.user_uuid,
            data=data,
            header=auth_user.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 400, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_INFO_ALREADY_EXIST

    @pytest.mark.negative
    def test_add_user_info_without_auth_header(self, app, auth_user):
        """
        Steps.
            1. Register new user
            2. Get access to store
            3. Try to add info without access token
            4. Check that status code is 401
            5. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.add_user_info(
            user_id=auth_user.user_uuid,
            data=data,
            header=None,
            type_response=AuthInvalidResponse,
        )
        assert res.status_code == 401, "Check status code"
        assert res.data.description == ResponseText.DESCRIPTION_AUTH_ERROR
        assert res.data.error == ResponseText.ERROR_AUTH_TEXT
        assert res.data.status_code == 401, "Check status code"
