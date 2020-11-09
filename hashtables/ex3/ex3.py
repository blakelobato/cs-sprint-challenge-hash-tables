def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    hash = {}
    hash_compare = {}
    hash_result = {}
    result = []

    for i in range(len(arrays[0])):
        hash[arrays[0][i]] = arrays[0][i]

    for i in range(1, len(arrays)):
        for j in range(len(arrays[i])):
            hash_compare[arrays[i][j]] = arrays[i][j]
        hash_result = dict(hash.items() & hash_compare.items())
        hash = hash_result

    for key in hash_result:
        result.append(key)

    return result



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
