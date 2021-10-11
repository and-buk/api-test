import pytest

from fixtures.common_models import MessageResponse
from fixtures.constants import ResponseText
from fixtures.userInfo.model import GetUserInfoResponse


class TestGetUserInfo:

    @pytest.mark.positive
    def test_get_user_info(self, app, user_info_):
        """
        Steps.
        1. Register new user
        2. Access to store
        3. Add user info
        4. Try to get user info
        5. Check that status code is 200
        6. Check response
        """
        res = app.user_info.get_user_info(
            user_id=user_info_.user_uuid,
            header=user_info_.header,
            type_response=GetUserInfoResponse,
        )
        assert res.status_code == 200, "Check status code"
        assert res.data.city == user_info_.user_info.address.city, "Check city"
        assert res.data.street == user_info_.user_info.address.street, "Check street"
        assert res.data.email == user_info_.user_info.email, "Check email"

    @pytest.mark.negative
    def test_get_info_of_non_existent_user(self, app, user_info_):
        """
        Steps.
        1. Register new user
        2. Access to store
        3. Add user info
        4. Try to get info of non-existent user
        5. Check that status code is 404
        6. Check response
        """
        res = app.user_info.get_user_info(
            user_id=1000,
            header=user_info_.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 404, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_INFO_NOT_FOUND
