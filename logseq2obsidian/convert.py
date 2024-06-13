import re

RE_ORGMODE_HEADING = re.compile(r'\*\s+(.+)\n:PROPERTIES:\n:heading:\s+true\n:END:', re.MULTILINE)


def is_markdown_heading(potential_heading) -> bool:
    return bool(re.match(r"^(#+)\s*(.*)+", potential_heading))


def is_orgmode_heading(potential_heading) -> bool:
    return bool(re.match(RE_ORGMODE_HEADING, potential_heading))


def convert_orgmode_to_markdown_heading(heading) -> str:
    raise NotImplementedError

