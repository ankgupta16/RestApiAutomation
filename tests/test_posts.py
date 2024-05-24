import pytest

from utilities.base import Base
from utilities import urls
import requests
from test_data import schemas
from utilities.validations import general_validations, posts_validations


class TestPosts(Base):

    se = requests.session()
    se.headers.update({'Authorization': f'Bearer {Base.access_token}'})

    @pytest.mark.positive
    def test_create_new_post_positive(self, get_create_post_data):
        logs = self.get_logger()
        random_user_response = self.get_a_random_user()
        post_data = {
            "user_id": random_user_response['id'],
            "title": get_create_post_data['title'],
            "body": get_create_post_data['body'],
        }
        expected_schema = schemas.single_post_schema()
        response = TestPosts.se.post(Base.base_url + urls.common_post_url(), data=post_data)
        try:
            general_validations.validate_status_code(response, 201)
            logs.info("created new post successfully: status 201")
            data = response.json()
            general_validations.validate_content_type(response)
            general_validations.validate_auth_token(response, Base.access_token)
            general_validations.validate_response_is_a_dictionary(data)
            general_validations.validate_response_time(response, 1)
            logs.info("response time taken: " + str(round(response.elapsed.total_seconds(), 1)))
            general_validations.validate_single_object_schema(data, expected_schema)
            posts_validations.validate_post_response_body(post_data, data)
            logs.info("validated post data successfully")
        except AssertionError as ae:
            logs.error(f"Test Failed while creating new post {ae}")
            pytest.fail(f"Test Failed while creating new post {ae}")

    @pytest.mark.positive
    def test_get_post_by_id_positive(self):
        logs = self.get_logger()
        random_post_response = self.get_a_random_post()
        post_id = random_post_response['id']
        expected_schema = schemas.single_post_schema()
        response = TestPosts.se.get(Base.base_url + urls.single_post_url(post_id))
        try:
            general_validations.validate_status_code(response, 200)
            logs.info(f"getting single post by id {post_id} successfully")
            data = response.json()
            assert data['id'] == post_id, "Unexpected data is returned" + data
            logs.info("validated post data successfully")
            general_validations.validate_content_type(response)
            general_validations.validate_auth_token(response, Base.access_token)
            general_validations.validate_response_is_a_dictionary(data)
            general_validations.validate_response_time(response, 2.0)
            general_validations.validate_single_object_schema(data, expected_schema)
        except AssertionError as ae:
            logs.error(f"Test Failed while getting post by id {ae}")
            pytest.fail(f"Test Failed while getting post by id {ae}")

    @pytest.mark.positive
    def test_get_all_posts_positive(self):
        logs = self.get_logger()
        expected_schema = schemas.single_post_schema()
        response = TestPosts.se.get(Base.base_url + urls.common_post_url())
        try:
            general_validations.validate_status_code(response, 200)
            data = response.json()
            logs.info("getting all the posts successfully: status 200")
            general_validations.validate_content_type(response)
            general_validations.validate_auth_token(response, Base.access_token)
            general_validations.validate_response_is_a_list(data)
            general_validations.validate_response_time(response, 1.0)
            general_validations.validate_multiple_object_schema(data, expected_schema)
        except AssertionError as ae:
            logs.error(f"Test Failed while getting all posts {ae}")
            pytest.fail(f"Test Failed while getting all posts {ae}")

    @pytest.mark.positive
    def test_search_post_by_title_positive(self):
        logs = self.get_logger()
        expected_schema = schemas.single_post_schema()
        random_post_response = self.get_a_random_post()
        post_title = random_post_response['title'][0:5].lower()
        response = TestPosts.se.get(Base.base_url + urls.search_post_by_title_url(post_title))
        try:
            general_validations.validate_status_code(response, 200)
            data = response.json()
            logs.info(f"searched post by title {post_title} successfully: status 200")
            posts_validations.validate_searched_post_by_title(data, post_title)
            logs.info("validated searched post successfully")
            general_validations.validate_content_type(response)
            general_validations.validate_auth_token(response, Base.access_token)
            general_validations.validate_response_is_a_list(data)
            general_validations.validate_response_time(response, 1.0)
            general_validations.validate_multiple_object_schema(data, expected_schema)
        except AssertionError as ae:
            logs.error(f"Test Failed while searching post by title positive {ae}")
            pytest.fail(f"Test Failed while searching post by title positive {ae}")

    @pytest.mark.positive
    def test_search_post_by_body_positive(self):
        logs = self.get_logger()
        expected_schema = schemas.single_post_schema()
        random_post_response = self.get_a_random_post()
        post_body = random_post_response['body'][0:5].lower()
        response = TestPosts.se.get(Base.base_url + urls.search_post_by_body_url(post_body))
        try:
            general_validations.validate_status_code(response, 200)
            data = response.json()
            logs.info(f"searched post by body {post_body} successfully: status 200")
            posts_validations.validate_searched_post_by_body(data, post_body)
            logs.info("validated searched post successfully")
            general_validations.validate_content_type(response)
            general_validations.validate_auth_token(response, Base.access_token)
            general_validations.validate_response_is_a_list(data)
            general_validations.validate_response_time(response, 1.0)
            general_validations.validate_multiple_object_schema(data, expected_schema)
        except AssertionError as ae:
            logs.error(f"Test Failed while searching post by body positive {ae}")
            pytest.fail(f"Test Failed while searching post by body positive {ae}")

    @pytest.mark.positive
    def test_search_post_by_user_id_positive(self):
        logs = self.get_logger()
        expected_schema = schemas.single_post_schema()
        random_user_response = self.get_a_random_user()
        user_id = random_user_response['id']
        response = TestPosts.se.get(Base.base_url + urls.search_post_by_user_id_url(user_id))
        try:
            general_validations.validate_status_code(response, 200)
            data = response.json()
            logs.info(f"searched post by user_id {user_id} successfully: status 200")
            posts_validations.validate_searched_post_by_user_id(data, user_id)
            logs.info("validated searched post using user_id successfully")
            general_validations.validate_content_type(response)
            general_validations.validate_auth_token(response, Base.access_token)
            general_validations.validate_response_is_a_list(data)
            general_validations.validate_response_time(response, 1.0)
            general_validations.validate_multiple_object_schema(data, expected_schema)
        except AssertionError as ae:
            logs.error(f"Test Failed while searching post by user_id positive {ae}")
            pytest.fail(f"Test Failed while searching post by user_id positive {ae}")


    @pytest.mark.positive
    def test_update_post_positive(self, get_create_post_data):
        logs = self.get_logger()
        random_post_response = self.get_a_random_post()
        user_id = random_post_response['user_id']
        post_id = random_post_response['id']
        post_update_data = {
            "user_id": user_id,
            "title": get_create_post_data['title'],
            "body": get_create_post_data['body'],
        }
        response = TestPosts.se.put(Base.base_url + urls.single_post_url(post_id), data=post_update_data)
        expected_schema = schemas.single_post_schema()
        try:
            general_validations.validate_status_code(response, 200)
            data = response.json()
            logs.info("updated existing post successfully: status 200")
            general_validations.validate_content_type(response)
            general_validations.validate_auth_token(response, Base.access_token)
            general_validations.validate_response_is_a_dictionary(data)
            general_validations.validate_response_time(response, 2.0)
            general_validations.validate_single_object_schema(data, expected_schema)
            posts_validations.validate_post_response_body(post_update_data, data)
            logs.info("validated updated body response")
        except AssertionError as ae:
            logs.error(f"Test Failed while updating post positive {ae}")
            pytest.fail(f"Test Failed while updating post positive {ae}")

    @pytest.mark.positive
    def test_delete_post_positive(self):
        logs = self.get_logger()
        random_post_response = self.get_a_random_post()
        post_id = random_post_response['id']
        response = TestPosts.se.delete(Base.base_url + urls.single_post_url(post_id))
        try:
            general_validations.validate_status_code(response, 204)
            logs.info("deleted existing post successfully: status 204")
            general_validations.validate_none_content_type(response)
            general_validations.validate_auth_token(response, Base.access_token)
            general_validations.validate_response_time(response, 1.0)
        except AssertionError as ae:
            logs.error(f"Test Failed while deleting post positive {ae}")
            pytest.fail(f"Test Failed while deleting post positive {ae}")



    @pytest.mark.negative
    def test_create_new_post_negative(self):
        logs = self.get_logger()
        # Unauthenticated user
        try:
            post_data = {
                "title": "random post",
                "body": "post description",
                "user_id": 1
            }
            response = requests.post(Base.base_url + urls.common_post_url(), data=post_data)
            general_validations.validate_status_code(response, 401)
            general_validations.validate_unauthenticated_user_message(response)
            logs.info("[for unauthenticated user] Expected status code and messages are returned")
        except AssertionError as ae:
            logs.error(f"Test Failed for creating new post negative[Unauthenticated user] {ae}")
            pytest.fail(f"Test Failed for creating new post negative[Unauthenticated user] {ae}")

        # sending blank data validation
        try:
            post_data = {
                "title": "",
                "body": "",
                "user_id": ""
            }
            response = TestPosts.se.post(Base.base_url + urls.common_post_url(), data=post_data)
            general_validations.validate_status_code(response, 422)
            data = response.json()
            posts_validations.validate_sending_blank_data(data)
        except AssertionError as ae:
            logs.error(f"Test Failed for creating new post negative[Blank data] {ae}")
            pytest.fail(f"Test Failed for creating new post negative[Blank data] {ae}")

        # non-existent user_id [string, special characters]
        try:
            post_data = {
                "title": "",
                "body": "",
                "user_id": 1
            }
            response = TestPosts.se.post(Base.base_url + urls.common_post_url(), data=post_data)
            general_validations.validate_status_code(response, 422)
            logs.info(f"[for non-existent user_id 1] Expected status code and messages are returned ")
            data = response.json()
            posts_validations.validate_sending_blank_data(data)
        except AssertionError as ae:
            logs.error(f"Test Failed for creating new post negative[non-existent user] {ae}")
            pytest.fail(f"Test Failed for creating new post negative[non-existent user] {ae}")

    @pytest.mark.negative
    @pytest.mark.parametrize('invalid_post_id', [-123, "%$#@!", " "])
    def test_get_post_by_id_negative(self, invalid_post_id):
        logs = self.get_logger()
        response = TestPosts.se.get(Base.base_url + urls.single_post_url(invalid_post_id))
        try:
            general_validations.validate_status_code(response, 404)
            general_validations.validate_resource_not_found_message(response)
            logs.info(f"[for invalid post_id {invalid_post_id}] Expected status code and messages are returned ")
        except AssertionError as ae:
            logs.error(f"Test Failed for getting post by id negative{ae}")
            pytest.fail(f"Test Failed for getting post by id negative{ae}")

    @pytest.mark.negative
    def test_update_post_negative(self):
        logs = self.get_logger()
        # Unauthenticated user
        random_post_response = self.get_a_random_post()
        post_id = random_post_response['id']
        try:
            post_data = {
                "title": "random post",
                "body": "post description",
                "user_id": 1
            }
            response = requests.put(Base.base_url + urls.single_post_url(post_id), data=post_data)
            general_validations.validate_status_code(response, 401)
            general_validations.validate_unauthenticated_user_message(response)
            logs.info("[for updating post with unauthenticated user] Expected status code and messages are returned")
        except AssertionError as ae:
            logs.error(f"Test Failed for creating new post negative[Unautneticated user] {ae}")
            pytest.fail(f"Test Failed for creating new post negative[Unautneticated user] {ae}")

        # sending blank data validation
        try:
            post_data = {
                "title": "",
                "body": "",
                "user_id": ""
            }
            response = TestPosts.se.put(Base.base_url + urls.single_post_url(post_id), data=post_data)
            general_validations.validate_status_code(response, 422)
            data = response.json()
            posts_validations.validate_sending_blank_data(data)
            logs.info("[for updating with blank data] Expected status code and messages are returned")
        except AssertionError as ae:
            logs.error(f"Test Failed for updating post negative[Blank data] {ae}")
            pytest.fail(f"Test Failed for updating post negative[Blank data] {ae}")

        # non-existent user_id [string, special characters]
        try:
            post_data = {
                "title": "",
                "body": "",
                "user_id": 1
            }
            response = TestPosts.se.put(Base.base_url + urls.single_post_url(post_id), data=post_data)
            general_validations.validate_status_code(response, 422)
            data = response.json()
            posts_validations.validate_sending_blank_data(data)
            logs.info(f"[for updating post with invalid user_id] Expected status code and messages are returned")
        except AssertionError as ae:
            logs.error(f"Test Failed for creating new post negative[non-existent user] {ae}")
            pytest.fail(f"Test Failed for creating new post negative[non-existent user] {ae}")

    @pytest.mark.negative
    @pytest.mark.parametrize('invalid_data', [-123, "!@#$"])
    def test_delete_post_negative(self, invalid_data):
        logs = self.get_logger()
        # unauthenticated user validation
        random_post_response = self.get_a_random_post()
        try:
            post_id = random_post_response['id']
            response = requests.delete(Base.base_url + urls.single_post_url(post_id))
            general_validations.validate_status_code(response, 401)
            general_validations.validate_unauthenticated_user_message(response)
            logs.info("[for deleting post with unauthenticated user] Expected status code and messages are returned")
        except AssertionError as ae:
            logs.error(f"Test Failed for deleting post negative[Unautneticated user] {ae}")
            pytest.fail(f"Test Failed for deleting post negative[Unautneticated user] {ae}")

        # invalid user id
        try:
            response = TestPosts.se.delete(Base.base_url + urls.single_post_url(invalid_data))
            general_validations.validate_status_code(response, 404)
            general_validations.validate_resource_not_found_message(response)
            logs.info("[for deleting post with invalid user_id] Expected status code and messages are returned")
        except AssertionError as ae:
            logs.error(f"Test Failed for creating new post negative[Invalid user] {ae}")
            pytest.fail(f"Test Failed for creating new post negative[Invalid user] {ae}")
