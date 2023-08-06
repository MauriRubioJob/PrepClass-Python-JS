
def merge_inplace(data, printer=None, offset=0):
    length = len(data)
    if length > 1:
        mid = length // 2
        left = data[:mid]
        right = data[mid:]

        if printer:
            printer(data, offset=offset)

        merge_inplace(left, printer=printer, offset=offset)
        merge_inplace(right, printer=printer, offset=offset+mid)

        if printer:
            printer(left+right, highlight=range(length), offset=offset)

        left_index, right_index = 0, 0
        data_index = 0

        left_length = len(left)
        right_length = len(right)

        while left_index < left_length and right_index < right_length:
            if left[left_index] < right[right_index]:
                data[data_index] = left[left_index]
                left_index += 1
            else:
                data[data_index] = right[right_index]
                right_index += 1
            data_index += 1
            if printer:
                printer(data[:data_index], highlight=range(length),
                        colour=(data_index-1, ), offset=offset)

        while left_index < left_length:
            data[data_index] = left[left_index]
            left_index += 1
            data_index += 1
            if printer:
                printer(data[:data_index], highlight=range(length),
                        colour=(data_index-1, ), offset=offset)

        while right_index < right_length:
            data[data_index] = right[right_index]
            right_index += 1
            data_index += 1
            if printer:
                printer(data[:data_index], highlight=range(length),
                        colour=(data_index-1, ), offset=offset)

        printer(data, offset=offset)


def merge_pure(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        left = merge_pure(left)
        right = merge_pure(right)

        _data = []
        while left and right:
            if left[0] < right[0]:
                _data.append(left.pop(0))
            else:
                _data.append(right.pop(0))

        _data.extend(left)
        _data.extend(right)

        return _data
    return data
