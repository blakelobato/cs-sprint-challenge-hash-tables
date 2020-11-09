def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    t = {}
    
    for num in a:
        if num * -1 in t:
            result.append(abs(num))
        t[num] = None
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
