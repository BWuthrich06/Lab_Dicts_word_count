"""Count words in file."""

def load_data(file_name):
    result = []
    test_file= open(file_name)
    for row in test_file:
        data = row.rstrip().split(" ")
        data_tuple = tuple(data)
        result.append(data_tuple)
    test_file.close()

    return result


def count_words():
    count = {}
    data = load_data("test.txt")
    for row in data:
        for word in row:
            if word in count:
                count[word]+=1
            else:
                count[word] = 1
    
    for item in count.items():
        print(item)
        
print(count_words())
    
    

