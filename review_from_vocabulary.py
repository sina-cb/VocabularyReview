import os.path

__author__ = 'Sina Solaimanpour'

responses = {
    'MajorTests Tricky Words': 'http://www.vocabulary.com/lists/682592#view=notes',
    'Official GRE Verbal': 'http://www.vocabulary.com/lists/700826#view=notes',
    'Magoosh Tricky Words': 'http://www.vocabulary.com/lists/687078#view=notes'
}


def read_file(list):
    dictionary = {}

    f = open(list+'.txt', 'r')
    for line in f:
        splitted = line.split("\t")
        dictionary[splitted[0]] = (splitted[1], splitted[2])
    f.close()

    if os.path.isfile(list+'_index.txt'):
        f = open(list+'_index.txt', 'r')
        index = int(f.readline())
        f.close()
    else:
        index = 0

    return dictionary, index

def main():
    responses_key = responses.keys()
    list = responses_key[0]

    (dictionary, index) = read_file(list)

    keys = dictionary.keys()

    print('1. Press enter to see the definition\n2. Press c for exit\n3. Press r to reset the file and exit\n')

    i = 0
    for i in range(index, len(keys)):
        print(keys[i] + ":")
        input = raw_input('').lower()
        print('definition: ' + dictionary[keys[i]][0] + " ||| description: " + dictionary[keys[i]][1] + "\n")

        if input == 'c':
            f = open(list+'_index.txt', 'w')
            f.write('%d' % (i))
            f.close()
            break

        if input == 'r':
            f = open(list+'_index.txt', 'w')
            f.write('%d' % 0)
            f.close()
            break

if __name__ == "__main__": main()
