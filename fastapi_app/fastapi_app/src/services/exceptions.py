from pydantic.errors import PydanticUserError

class ExistsError(PydanticUserError):
    pass

