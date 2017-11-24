from utils.module_rest import *
from behave import given, when, then
from compare import *


@given(u'I have a service for "{servicedelete}" to delete a user')
def step_impl(context, servicedelete):
    context.servicedelete = servicedelete

@when(u'I send {methoddelete} items request to delete an exsiting user')
def step_impl(context, methoddelete):
    context.method  = methoddelete
    context.url     = context.host + context.rootPath + context.servicedelete
    context.headers = context.tokentodelete
    context.response = perform_request(context.method, context.url, context.headers)
    generateFileJson("data/", "User_DELETE", context.response.json())


@then(u'I receive status code {status_code} for the response after delete')
def step_impl(context, status_code):
    expect(context.response.status_code).to_equal(int(status_code))