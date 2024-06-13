import re


def is_markdown_heading(potential_heading) -> bool:
    if re.match(r"^(#+)\s*(.*)+", potential_heading):
        return True
    else:
        return False


def is_orgmode_heading(potential_heading) -> bool:
    if re.match(r"\**\ *\w*"):
        return True
    else:
        return False