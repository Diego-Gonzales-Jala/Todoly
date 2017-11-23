import yaml

global generic_data
generic_data = yaml.load(open('configuration/config.yml'))

def before_all(context):
    print("_____________Init Before all_______________")
    context.host          = generic_data['host']
    context.rootPath      = generic_data['rootPath']
    context.token         = generic_data['token']
    context.tokentodelete = generic_data['tokentodelete']
    context.tokentoupdate = generic_data['tokentoupdate']
    #print(context.tokentoupdate)

def after_feature(context, feature):
    if 'smoke' in feature.tags:
        print("__________After feature______________")

def before_feature(context, feature):
    if 'smoke' in feature.tags:
        print("___________Before feature_____________")
'''
def before_scenario(context, scenario):
    if 'getuser' in scenario.tags:
        print("_________Before Scenario___________")

def before_step(context, step):
    print("STEP: ", step.name)
    print("KEYWORD: ", step.keyword)
    print("STATUS: ", step.status)
'''