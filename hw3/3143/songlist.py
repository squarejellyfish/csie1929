def practice(dct: dict, song: str, writer: str) -> dict:
    dct[song] = writer

    return dct

def query(dct: dict, song: str) -> bool:
    if (song in dct):
        return dct[song]
    return False

