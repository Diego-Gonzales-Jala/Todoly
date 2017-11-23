from compare import *
from utils.module_rest import *
from behave import given, when, then
import json

@given(u'I have a service for "{servicemethodpost}" to create user')
def step_impl(context,servicemethodpost ):
    context.servicemethodpost = servicemethodpost

@given(u'I have create request payload')
def step_impl(context):
    context.payloaduser = json.loads(context.text)

@when(u'I send a {methodpost} request to create a new user')
def step_impl(context, methodpost):
    context.method   = methodpost
    context.url      = context.host + context.rootPath + context.servicemethodpost
    context.pyloadrequest = context.payloaduser
    context.response = requests.post(context.url, json=context.pyloadrequest)
    generateFileJson("data/", "data_create_user", context.response.json())


@then(u'I receive status code {status_code} for the response create user')
def step_impl(context, status_code):
    expect(context.response.status_code).to_equal(int(status_code))