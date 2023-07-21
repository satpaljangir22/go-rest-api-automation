from utils import api_calls


def before_all(context):
    print("******** Initiating Suite ********")
    api_calls.config_context(context)


def after_all(context):
    print("******** Tearing Down Suite ********")
    api_calls.tear_down(context)
