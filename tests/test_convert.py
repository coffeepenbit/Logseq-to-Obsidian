import pytest

from logseq2obsidian import convert


@pytest.mark.parametrize(
    "string, expected", [
        (
            "",
            False
        ),
        (
            "",
            False
        ),
        (
            "* test",
            False
        ),
        (
            "# test",
            True
        ),
        (
            "## test",
            True
        ),
        (
            "## *test* ==#![[heading]]==",
            True
        )
    ]
)
def test_is_markdown_heading(string, expected):
    result = convert.is_markdown_heading(string)

    assert result == expected


@pytest.mark.parametrize(
    "string, expected", [
        (
            "",
            False
        ),
        (
            " ",
            False
        ),
        (
            "* test",
            False
        ),
        (
            "# test",
            False
        ),
        (
            "\n".join(
                [
                    "## test",
                    ":PROPERTIES:",
                    ":heading: true",
                    ":END:"
                ]
            ),
            True
        )
    ]
)
def test_is_orgmode_heading(string, expected):
    print(f"{string=}")
    result = convert.is_orgmode_heading(string)

    assert result == expected


def test_simple_header_conversion():
    org_text = """
** Test Header :PROPERTIES:
:heading: true
:END:
"""
    expected_output = "\n## Test Header\n"
    assert convert.convert_org_to_markdown(org_text) == expected_output

def test_non_header():
    org_text = """
* Not a Header :PROPERTIES:
:heading: false
:END:
"""
    expected_output = "\n* Not a Header :PROPERTIES:\n:heading: false\n:END:\n"
    assert convert.convert_org_to_markdown(org_text) == expected_output

def test_multiple_headers():
    org_text = """
* Overview :PROPERTIES:
:heading: true
:END:
** Details :PROPERTIES:
:heading: true
:END:
"""
    expected_output = "\n# Overview\n## Details\n"
    assert convert.convert_org_to_markdown(org_text) == expected_output

def test_mixed_content():
    org_text = """
** Valid Header :PROPERTIES:
:heading: true
:END:
Content under header
* Ignored Header :PROPERTIES:
:heading: false
:END:
"""
    expected_output = "\n## Valid Header\nContent under header\n* Ignored Header :PROPERTIES:\n:heading: false\n:END:\n"
    assert convert.convert_org_to_markdown(org_text) == expected_output

def test_no_properties_block():
    org_text = """
** Missing Properties
"""
    expected_output = "\n** Missing Properties\n"
    assert convert.convert_org_to_markdown(org_text) == expected_output