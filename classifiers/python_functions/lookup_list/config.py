from util.configs import build_classifier_function_config
from util.enums import State
from . import lookup_list, INPUT_EXAMPLE

def get_config():
    return build_classifier_function_config(
        function=lookup_list,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=26,
        tabler_icon="ClipboardList",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )
