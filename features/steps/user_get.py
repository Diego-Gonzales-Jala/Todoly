from compare import *
from utils.module_rest import *
from behave import given, when, then

@given(u'My service for "{methodgetuser}" for user')
def step_impl(context,methodgetuser ):
    context.methodgetuser = methodgetuser

@when(u'I send {method} user request to get user information')
def step_impl(context, method):
    context.method   = method
    context.url      = context.host + context.rootPath + context.methodgetuser
    context.headers  = context.token
    context.response = perform_request(context.method, context.url, context.headers)
    generateFileJson("data/", "User_GET", context.response.json())

@then(u'I receive status code {status_code} for the response')
def step_impl(context, status_code):
    expect(context.response.status_code).to_equal(int(status_code))



