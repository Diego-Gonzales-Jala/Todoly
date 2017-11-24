from compare import *
from utils.json_order import *
from utils.module_rest import *
from utils.file_system import *
from behave import then




@then(u'A new project should be insert in the database')
def step_impl(context):
    #retormanamos el ID del proyecto creado
    context.payload = context.response.json()
    context.Id = str(context.payload['Id'])
    #armamos el response
    context.method   = "GET"
    context.ServiceGet = '/projects/' + context.Id + '.json'
    context.url      = context.host + context.rootPath + context.ServiceGet
    context.headers  = context.token

    context.response = perform_request(context.method, context.url, context.headers)
    generateFileJson("data/", "Project_GETProyectsByID", context.response.json())

    # comparamos GET and POST
    context.rootpathDataFile = "data/Project_POSTCreateProyect.json"
    context.dataFile = "data/Project_GETProyectsByID.json"

    if context.rootpathDataFile == context.dataFile:
        bool = True
    else:
        bool = False

    assert bool != True



@then(u'The project should be updated in the database')
def step_impl(context):
    #retormanamos el ID del proyecto creado
    context.payload = context.response.json()
    context.Id = str(context.payload['Id'])
    #armamos el response
    context.method   = "GET"
    context.ServiceGet = '/projects/' + context.Id + '.json'
    context.url      = context.host + context.rootPath + context.ServiceGet
    context.headers  = context.token

    context.response = perform_request(context.method, context.url, context.headers)
    generateFileJson("data/", "Project_GETProyectsByID", context.response.json())

    # comparamos GET and POST
    context.rootpathDataFile = "data/Project_PUTUpdateProyect.json"
    context.dataFile = "data/Project_GETProyectsByID.json"

    if context.rootpathDataFile == context.dataFile:
        bool = True
    else:
        bool = False

    assert bool != True


@then(u'The project should be deleted in the database')
def step_impl(context):
    #retormanamos el ID del proyecto creado
    context.payload = context.response.json()
    context.Id = str(context.payload['Deleted'])

    expect(context.Id).to_equal("True")



