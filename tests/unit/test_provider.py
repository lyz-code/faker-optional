"""Test the optional fake provider."""

import re
from datetime import datetime
from typing import Any, Dict, List, Set, Tuple

import pytest
from faker import Faker


@pytest.mark.parametrize(
    ("method", "type_"),
    [
        ("optional_int", int),
        ("optional_bool", bool),
        ("optional_str", str),
        ("optional_float", float),
        ("optional_tuple", Tuple),
        ("optional_list", List),
        ("optional_set", Set),
        ("optional_dict", Dict),
        ("optional_datetime", datetime),
        ("optional_word", str),
        ("optional_sentence", str),
        ("optional_paragraph", str),
        ("optional_text", str),
        ("optional_name", str),
        ("optional_first_name", str),
        ("optional_last_name", str),
        ("optional_name_female", str),
        ("optional_name_male", str),
        ("optional_name_nonbinary", str),
        ("optional_first_name_female", str),
        ("optional_first_name_male", str),
        ("optional_first_name_nonbinary", str),
        ("optional_last_name_female", str),
        ("optional_last_name_male", str),
        ("optional_last_name_nonbinary", str),
    ],
)
def test_optional_type(fake: Faker, method: str, type_: Any) -> None:
    """
    Given: The Optional Provider.
    When: called with the optional methods.
    Then: Half of the times it returns the desired type_, and half None.
    """
    result = [getattr(fake, method)() for i in range(0, 100)]

    assert None in result
    for item in result:
        if item is None:
            assert True
        else:
            assert isinstance(item, type_)


@pytest.mark.parametrize(
    ("method", "item_regexp"),
    [
        ("optional_date", r"(\d{2}-?){3}"),
        ("optional_time", r"(\d{2}:?){3}"),
    ],
)
def test_optional_regexp(fake: Faker, method: str, item_regexp: str) -> None:
    """
    Given: The Optional Provider.
    When: called with the optional methods.
    Then: Half of the times it returns strings that match the regular expression,
        and half None.
    """
    regexp = re.compile(item_regexp)

    result = [getattr(fake, method)() for i in range(0, 100)]

    assert None in result
    for item in result:
        if item is None:
            assert True
        else:
            assert regexp.match(item)


@pytest.mark.parametrize(
    "method",
    [
        "optional_words",
        "optional_sentences",
        "optional_paragraphs",
        "optional_texts",
    ],
)
def test_optional_list_of_strings(fake: Faker, method: str) -> None:
    """
    Given: The Optional Provider.
    When: called with the optional methods.
    Then: Half of the times it returns a list of strings, and half None.
    """
    result = [getattr(fake, method)() for i in range(0, 100)]

    assert None in result
    for items_list in result:
        if items_list is None:
            assert True
        else:
            for item in items_list:
                assert isinstance(item, str)
