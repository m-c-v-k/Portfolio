#! Python3

### Sort a list ###
#list_of_words = [23, 54, 67, 78, 9, 7, 56, 34, 23]
# list_of_words = [7, 9, 23, 23, 34, 54, 56, 67, 78]
list_of_words = ["A", "a", "t", "z"]


n = len(list_of_words)

while True:

    counter = 0

    for i in range(n - 1):

        if list_of_words[i] > list_of_words[i + 1]:
            list_of_words[i], list_of_words[i +
                                            1] = list_of_words[i + 1], list_of_words[i]
            counter += 1

    if counter != 0:
        continue
    elif counter == 0:
        break


print(list_of_words)
