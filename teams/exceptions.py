def cup_generator(start):
    cup = [start]
    for year in cup:
        if cup[-1] < "2022":
            cup.append(str(int(cup[-1]) + 4))
    return cup


cup_years = cup_generator("1930")


class ImpossibleTitlesError(Exception):
    default_message = "impossible to have more titles than disputed cups"

    def __init__(self, message=None):
        self.message = message or self.default_message


class InvalidYearCupError(Exception):
    default_message = "there was no world cup this year"

    def __init__(self, message=None):
        self.message = message or self.default_message


class NegativeTitlesError(Exception):
    default_message = "titles cannot be negative"

    def __init__(self, message=None):
        self.message = message or self.default_message


def negative_titles_error(**data):
    if data["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")


def invalid_year_cup_error(**data):
    data["first_cup"] = data["first_cup"][:4]

    if int(data["first_cup"]) % 2:
        raise InvalidYearCupError("there was no world cup this year")
    if data["first_cup"] not in cup_years:
        raise InvalidYearCupError("there was no world cup this year")


def impossible_titles_error(**data):
    cup_impossible = cup_generator(data["first_cup"][:4])
    if data["titles"] > len(cup_impossible):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
