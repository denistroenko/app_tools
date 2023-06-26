def human_space(bytes: int, digits: int=1) -> str:
    sizes = {4: 'T', 3: 'G', 2: 'M', 1: 'K', 0: 'b'}

    e = 0
    while bytes >= 1024:
        bytes /= 1024
        e += 1

    return str(f'{round(bytes, digits)}{sizes[e]}')
