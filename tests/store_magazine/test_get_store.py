from fixtures.magazine.model import StoreResponse


class TestStore:
    def test_get_store_info(self, app, store):
        """
        Steps.
            1. Try to login user with valid data
            2. Check that status code is 200
            3. Check response
        """
        res = app.operations_with_store.get_store(
            name_store=store.store,
            header=store.header,
            type_response=StoreResponse,
        )
        assert res.status_code == 200
