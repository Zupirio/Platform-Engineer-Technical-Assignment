def flat_list(list_to_flat):
    if not isinstance(list_to_flat, list):
        yield list_to_flat
    else:
        for item in list_to_flat:
            yield from flat_list(item)
    # return(list(flat_list(list_to_flat)))


def bubbleSort(theSeq):
    # flat_list(theSeq)
    newSeq = list(flat_list(theSeq))
    newSeq = list(filter(None, newSeq))
    n = len(newSeq)
    print(n)

    if n < 10000:
        for i in range(n - 1):
            flag = 0

            for j in range(n - 1):
                if newSeq[j] > newSeq[j + 1]:
                    tmp = newSeq[j]
                    newSeq[j] = newSeq[j + 1]
                    newSeq[j + 1] = tmp
                    flag = 1
            if flag == 0:
                break
        return newSeq
    else:
        return ("Array is too big")


# el = [6, 2, [4, 3], [5, 1, 1, [2, 3]]]
# el = [6, 2, [4, 3],[[[5], null], 1]]
# el = [1,2,3,4,[100,200,300,[1000,2000,3000]]]
el = []
# el = [-1, -3, -5, -7, -9, -5]
# el = [5, 5, 7, 8, 2, 4, 1]
# el = [1, None, 1, 1]

result = bubbleSort(el)

print(result)
