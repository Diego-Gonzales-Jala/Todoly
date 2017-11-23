from compare import *
from utils.module_rest import *
from behave import given, when, then
import json

@given(u'I have a service for "{updateone}" for update my existing user')
def step_impl(context, updateone):
    context.updateone = updateone

@given(u'I have a payload to update')
def step_impl(context):
    context.payloadupdate = json.loads(context.text)

@when(u'I send {updmethod} user update request to update user in database')
def step_impl(context, updmethod):
    context.updmethod  = updmethod
    context.url  = context.host + context.rootPath + context.updateone
    context.headers = context.tokentoupdate
    context.response = perform_request(context.updmethod, context.url, context.headers, context.payloadupdate)
    generateFileJson("data/", "User_PUT", context.response.json())

@then(u'I receive status code {status_code} for the response after update')
def step_impl(context, status_code):
    expect(context.response.status_code).to_equal(int(status_code))


