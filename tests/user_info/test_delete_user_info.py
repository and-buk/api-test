from fixtures.common_models import MessageResponse
from fixtures.constants import ResponseText


class TestGetUserInfo:
    def test_delete_user_info(self, app, user_info_):
        """
        1. Try to get user info
        2. Check that status code is 200
        3. Check response
        """
        res = app.user_info.delete_user_info(
            user_id=user_info_.user_uuid,
            header=user_info_.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 200, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_DELETE_USER_INFO
