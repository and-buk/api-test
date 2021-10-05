from fixtures.common_models import MessageResponse
from fixtures.constants import ResponseText
from fixtures.userInfo.model import AddUserInfo


class TestUserInfo:
    def test_update_user_info(self, app, user_info_):
        """
        Steps.
            1. Try to login user with valid data
            2. Check that status code is 200
            3. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.update_user_info(
            user_id=user_info_.user_uuid,
            data=data,
            header=user_info_.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 200
        assert res.data.message == ResponseText.MESSAGE_UPDATE_USER_INFO
