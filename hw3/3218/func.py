def flame_breathing(train: list, *num):
    for n in num:
        if (train[n - 1] != 0): continue

        train[n - 1] = -1

    return train
