import json
from behave import when, then
from compare import expect
from utils.module_rest import *
#Smoke testing

@when(u'I send "{method}" project request')
def step_impl(context,method):
    context.method   = method
    context.url      = context.host + context.rootPath + context.servicemethod
    context.headers  = context.token
    context.response = perform_request(context.method, context.url, context.headers)
    generateFileJson("data/", "Project_GETAllProyects", context.response.json())


@when(u'I send "{method}" project request to see a proyect')
def step_impl(context,method):
    context.method   = method
    context.url      = context.host + context.rootPath + context.servicemethod
    context.headers  = context.token
    context.response = perform_request(context.method, context.url, context.headers)
    generateFileJson("data/", "Project_GETProyectsByID", context.response.json())


@when(u'I send "{method}" project request to see the items in a proyect')
def step_impl(context,method):
    context.method   = method
    context.url      = context.host + context.rootPath + context.servicemethod
    context.headers  = context.token
    context.response = perform_request(context.method, context.url, context.headers)
    generateFileJson("data/", "Project_GETItemsInAProject", context.response.json())

@when(u'I send "{method}" project request to see the done items in a proyect')
def step_impl(context,method):
    context.method   = method
    context.url      = context.host + context.rootPath + context.servicemethod
    context.headers  = context.token
    context.response = perform_request(context.method, context.url, context.headers)
    generateFileJson("data/", "Project_GETDoneItemsInAProject", context.response.json())


#***************POST*********************************
@when(u'I send "{method}" project request with generic body.json')
def step_impl(context,method):
    context.pyloadBody = json.loads(context.text)
    context.method   = method
    context.url      = context.host + context.rootPath + context.servicemethod
    context.headers  = context.token
    context.pyloadrequest = context.pyloadBody
    #context.pyloadrequest = {"Content": "My New GenericProject-Alex", "Icon": 4}
    context.response = perform_request(context.method, context.url, context.headers, context.pyloadrequest)
    generateFileJson("data/", "Project_POSTCreateProyect", context.response.json())


#***************PUT*********************************
@when(u'I send "{method}" project request with generic body.json to update a proyect')
def step_impl(context,method):
    context.method   = method
    context.url      = context.host + context.rootPath + context.servicemethod
    context.headers  = context.token
    context.pyloadBody = json.loads(context.text)
    context.pyloadrequest = context.pyloadBody
    #context.pyloadrequest = {"Content": "My Update GenericProject-Alex", "Icon": 1}
    context.response = perform_request(context.method, context.url, context.headers, context.pyloadrequest)
    generateFileJson("data/", "Project_PUTUpdateProyect", context.response.json())


@when(u'I send "{method}" project request to remove a proyect')
def step_impl(context,method):
    context.method   = method
    context.url      = context.host + context.rootPath + context.servicemethod
    context.headers  = context.token
    context.response = perform_request(context.method, context.url, context.headers)
    generateFileJson("data/", "Project_DELETEAProject", context.response.json())




@then(u'I receive the status code "{statusCode}" in the response')
def step_impl(context, statusCode):
    expect(context.response.status_code).to_equal(int(statusCode))
