import pytest
from src.processing import filter_by_state, sort_by_date


# Модуль processing
@pytest.mark.parametrize(
    "transactions, state, expected",
    [
        (
            [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "PENDING"}, {"id": 3, "state": "EXECUTED"}],
            "EXECUTED",
            [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}],
        ),
        (
            [
                {"id": 1, "state": "PENDING"},
                {"id": 2, "state": "PENDING"},
            ],
            "EXECUTED",
            [],
        ),  # Нет словарей с состоянием EXECUTED
        (
            [
                {"id": 1, "state": "EXECUTED"},
                {"id": 2, "state": "PENDING"},
            ],
            "PENDING",
            [{"id": 2, "state": "PENDING"}],
        ),
        ([], "EXECUTED", []),  # Пустой список
    ],
)
def test_filter_by_state(transactions, state, expected):
    assert filter_by_state(transactions, state) == expected


@pytest.mark.parametrize(
    "transactions, fun_sorted, expected",
    [
        (
            [{"id": 1, "date": "/1999-01-20"}, {"id": 2, "date": "/1999-01-21"}, {"id": 3, "date": "/1999-01-22"}],
            True,
            [{"id": 1, "date": "/1999-01-20"}, {"id": 2, "date": "/1999-01-21"}, {"id": 3, "date": "/1999-01-22"}],
        ),
        (
            [{"id": 1, "date": "/1999-01-20"}, {"id": 2, "date": "/1999-01-21"}, {"id": 3, "date": "/1999-01-22"}],
            False,
            [{"id": 3, "date": "/1999-01-22"}, {"id": 2, "date": "/1999-01-21"}, {"id": 1, "date": "/1999-01-20"}],
        ),
        (
            [{"id": 1, "date": ""}, {"id": 2, "date": "/1999-01-21"}, {"id": 3, "date": "/1999-01-22"}],
            True,
            [{"id": 2, "date": "/1999-01-21"}, {"id": 3, "date": "/1999-01-22"}],
        ),
        (
            [{"id": 1, "date": ""}, {"id": 2, "date": "/1999-01-21"}, {"id": 3, "date": "/1999-01-22"}],
            False,
            [{"id": 3, "date": "/1999-01-22"}, {"id": 2, "date": "/1999-01-21"}],
        ),
    ]
)
def test_sort_by_date(transactions, fun_sorted, expected):
    assert sort_by_date(transactions, fun_sorted) == expected
