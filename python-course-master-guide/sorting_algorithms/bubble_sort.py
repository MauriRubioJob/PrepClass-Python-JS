
def bubble(data, printer=None):
    for i in range(len(data) - 1):
        swapped = False
        for j in range(len(data) - 1 - i):
            if printer:
                printer(data, highlight=(j, ))
            a = data[j]
            b = data[j + 1]
            if a > b:
                data[j] = b
                data[j + 1] = a
                swapped = True
        if not swapped:
            break
    if printer:
        printer(data)
