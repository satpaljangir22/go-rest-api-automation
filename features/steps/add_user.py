from behave import given, when, then
from utils.utilities import Utilities


@when('Post call to add user is requested')
def step_impl(context):
    user_data = {
        "name": "Satpal Jangir",
        "email": Utilities.generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    context.response = context.api_operations.post_request(user_data)


@then('User details should be returned in the response')
def step_impl(context):
    response = context.response
    assert response[0] == 201
    content = response[1]
    assert "id" in content
    assert content["name"] == "Satpal Jangir"
