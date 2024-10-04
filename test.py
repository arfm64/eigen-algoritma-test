
def test1():
    word = "NEGIE1"
    stringword = []
    final_word = ""

    for char in word:
        if char.isalpha():
            stringword.append(char)
    stringword.reverse()

    j = 0
    for char in word:
        if char.isalpha(): 
            final_word += stringword[j]
            j += 1
        else:
            final_word += char

    return(final_word)

def test2():
    word = "Saya sangat senang mengerjakan soal algoritma"
    word_and_length = []
    
    for x in word.split(" "):
        word_and_length.append((x, len(x)))
    
    longest_word = max(word_and_length, key=lambda item: item[1])
    
    return longest_word

def test3():
    input_list = ['xc', 'dz', 'bbb', 'dz']
    query_list = ['bbb', 'ac', 'dz']
    
    word_count = {}
    for word in input_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    output = []
    for query in query_list:
        output.append(word_count.get(query, 0))

    return output

def test4():
    matrix = [[1, 2, 0], [4, 5, 6], [7, 8, 9]]
    n = len(matrix)
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(n):
        primary_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][n - 1 - i]

    difference = primary_diagonal_sum - secondary_diagonal_sum
    return primary_diagonal_sum, secondary_diagonal_sum

print("============= Question 1 =============")
print(f"Word Reverse: {test1()}")
print("============= Question 2 =============")
print(f"Longest word: {test2()[0]}")
print(f"length: {test2()[1]}")
print("============= Question 3 =============")
print(f"Output: {test3()}")
print("============= Question 4 =============")
diagonal1, diagonal2 = test4()
print(f"Diagonal 1: {diagonal1}")
print(f"Diagonal 2: {diagonal2}")
print(f"Diagonal1 - diagonal2 = {diagonal1 - diagonal2}")