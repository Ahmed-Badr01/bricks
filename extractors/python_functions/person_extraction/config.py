from util.configs import build_extractor_function_config
from util.enums import State
from . import person_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=person_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=34,
        tabler_icon="User",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )
