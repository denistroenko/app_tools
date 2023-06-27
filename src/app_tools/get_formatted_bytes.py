def get_formatted_bytes(bytes: int,
                        digits: int = 1,
                        liter_len: str = 1,
                        ) -> str:

    # liter_len must be 1 or 2
    if liter_len not in [1, 2]:
        liter_len = 1

    # human sizes dict
    sizes = {4: 'Tb', 3: 'Gb', 2: 'Mb', 1: 'Kb', 0: 'b'}

    # new space in human size
    space = bytes

    e = 0  # exponent
    while space >= 1024:
        space /= 1024
        e += 1

    # if e > 4, show size in T
    if e > 4:
        space = bytes / 1024**4
        e = 4

    return str(f'{round(space, digits)}{sizes[e][:liter_len]}')
