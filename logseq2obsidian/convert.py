import re


def is_markdown_heading(potential_heading) -> bool:
    if re.match(r"^(#+)\s*(.*)+", potential_heading):
        return True
    else:
        return False


def is_orgmode_heading(potential_heading) -> bool:
    # TODO complete implementation
    return potential_heading == """# test
            :PROPERTIES:
            :heading: true
            :END:
            """


def convert_orgmode_to_markdown_heading(heading) -> str:
    raise NotImplementedError

