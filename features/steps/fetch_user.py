from behave import when, then


@when('Get call for all user is requested')
def step_impl(context):
    context.response = context.api_operations.get_request()


@then('All users should be returned in the response')
def step_impl(context):
    response = context.response
    assert response[0] == 200


@when('Get call for user_id is requested')
def step_impl(context):
    context.response = context.api_operations.get_request(3770510)


@then('User with user_id should be returned in the response')
def step_impl(context):
    response = context.response
    assert response[0] == 200
    data = response[1]
    assert data["id"] == 3770510
