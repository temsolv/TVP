def reduce_noise(arr: list, factor):
    """Function that reduces noise value by multiplyng on given factor"""
    for i in range(len(arr)):
        arr[i] = arr[i] * factor