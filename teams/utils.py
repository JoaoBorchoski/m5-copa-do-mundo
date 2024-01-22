from .exceptions import (
    negative_titles_error,
    invalid_year_cup_error,
    impossible_titles_error,
)


def data_processing(data):
    negative_titles_error(**data)
    invalid_year_cup_error(**data)
    impossible_titles_error(**data)


data = {
    "name": "França",
    "titles": -2,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "2002-10-18",
}
