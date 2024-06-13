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
            """# test
            :PROPERTIES:
            :heading: true
            :END:
            """,
            True
        )
    ]
)
def test_is_orgmode_heading(string, expected):
    result = convert.is_orgmode_heading(string)

    assert result == expected
