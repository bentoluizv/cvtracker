from ulid import ULID


def get_new_ulid_as_str():
    return str(ULID())
