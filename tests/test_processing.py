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
