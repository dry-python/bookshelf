class Validated:
    @classmethod
    def __get_validators__(cls):
        yield cls._validate_instance

    @classmethod
    def _validate_instance(cls, v):
        if isinstance(v, cls):
            return v
        else:
            raise ValueError(
                f"An instance of {cls.__name__!r} expected, got: {type(v).__name__!r}"
            )
