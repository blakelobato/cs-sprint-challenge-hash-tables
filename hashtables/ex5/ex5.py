# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash = {}
    result = []
    final = []

    for i in range(len(files)):
        slash_loc = files[i].rfind('/')
        filename_loc = -(len(files[i]) - slash_loc - 1)
        filename = files[i][filename_loc:]
        
        if filename not in hash:
            hash[filename] = [files[i]]
        else:
            existing_value = hash[filename]
            existing_value.append(files[i])
            hash[filename] = existing_value

    for i in range(len(queries)):
        if queries[i] in hash:
            result.append(hash[queries[i]])

    for i in range(len(result)):
        for j in range(len(result[i])):
            final.append(result[i][j])

    return final


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
