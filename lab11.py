def cheat_sort(seq):
    seq.sort()

def cheat_merge(left, right):
    return sorted(left + right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(seq):
    if len(seq) <= 1:
        return

    mid = len(seq) // 2
    left = seq[:mid]
    right = seq[mid:]

    merge_sort(left)
    merge_sort(right)

    merged = merge(left, right)

   
    for i in range(len(seq)):
        seq[i] = merged[i]


