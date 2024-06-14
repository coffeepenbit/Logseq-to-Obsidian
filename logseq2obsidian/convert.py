import re

RE_ORGMODE_HEADING = re.compile(r'\*\s+(.+)\n:PROPERTIES:\n:heading:\s+true\n:END:', re.MULTILINE)


def is_markdown_heading(potential_heading) -> bool:
    return bool(re.match(r"^(#+)\s*(.*)+", potential_heading))


def is_orgmode_heading(potential_heading) -> bool:
    return bool(re.match(RE_ORGMODE_HEADING, potential_heading))


def convert_orgmode_to_markdown_heading(heading) -> str:
    raise NotImplementedError

def convert_org_to_markdown(org_text):
    """Convert org-mode formatted text with specific header properties to Markdown."""
    # Regex to find eligible headers with 'heading: true' property
    header_pattern = r"^(\*+)\s+(.*?)\s+:PROPERTIES:\n:heading:\s+true\n:END:"
    # Replace matched headers using parse_header function
    markdown_text = re.sub(header_pattern, parse_header, org_text, flags=re.MULTILINE)
    return markdown_text

def parse_header(match):
    """Convert org-mode header syntax to Markdown based on match from regex."""
    level = len(match.group(1))  # Number of stars indicates header level
    header_text = match.group(2).strip()
    return f"{'#' * level} {header_text}"
