import pytest

from logseq2obsidian import convert


@pytest.mark.parametrize(
    "string, expected", [
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
