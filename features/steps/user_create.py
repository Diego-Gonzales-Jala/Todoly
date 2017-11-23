from compare import *
from utils.module_rest import *
from behave import given, when, then
import requests
import json

@given(u'I have create request {payload}')
def step_impl(context, payload):
    context.payload = payload

@when(u'I send a {methodpost} request to create a new user')
def step_impl(context, methodpost):
    context.methodpost = methodpost
    context.url      = context.host + context.rootPath + context.servicemethod
    context.createParams2 = {"Email":"test.tes@jalasoft.com", "FullName": "Irina Torrico","Password": "123456"}
    context.response = requests.post(context.url, json=context.createParams2)
    generateFileJson("data/", "data_create_user", context.response.json())


@then(u'I receive status code {status_code} for the response create user')
def step_impl(context, status_code):
    expect(context.response.status_code).to_equal(int(status_code))