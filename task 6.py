# Please enter your code here for implementing the function.
def preprocess_string(string, delimiter):

    string = string.split(delimiter[0])
    print(string)
    new_str = []
    a = 0
    while a < len(delimiter):
        for n in range(len(string)):
            string[n] = string[n].replace(delimiter[a],)

        for sentence in string:
            new_str.append(sentence)
        print(new_str)
        string = new_str
        new_str = []

        a += 1
        print(string)

    print(string)

    return string


string = "Python is fun and tsssss; what a language to learn, waow :)"
delimiter = [',', ' ', ';', ':)']
preprocess_string(string, delimiter)