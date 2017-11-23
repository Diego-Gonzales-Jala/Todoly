from behave import when
from utils.module_rest import *

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

