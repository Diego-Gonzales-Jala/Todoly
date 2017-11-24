import yaml

global generic_data
generic_data = yaml.load(open('configuration/config.yml'))

def before_all(context):
    print("_____________Init before all_______________")
    context.host          = generic_data['host']
    context.rootPath      = generic_data['rootPath']
    context.token         = generic_data['token']
    context.tokentoupdate = generic_data['tokentoupdate']
    context.tokentodelete = generic_data['tokentodelete']


def after_feature(context, feature):
    if 'smoke' in feature.tags:
        print("__________ After feature______________")

def before_feature(context, feature):
    if 'smoke' in feature.tags:
        print("___________Init before feature_____________")

def before_scenario(context, scenario):
    if 'smoke' in scenario.tags:
        print("_________Init test cases for smoke___________")
    if 'crud' in scenario.tags:
        print("_________Init test cases for crud___________")
'''
def before_step(context, step):
    print("STEP: ", step.name)
    print("KEYWORD: ", step.keyword)
    print("STATUS: ", step.status)
'''