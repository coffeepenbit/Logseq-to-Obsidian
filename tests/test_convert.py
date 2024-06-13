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
            True
        ),
        (
            "* ",
            False
        )
    ]
)
def test_is_markdown_heading(string, expected):
    result = convert.is_markdown_heading(string)

    assert result == expected
