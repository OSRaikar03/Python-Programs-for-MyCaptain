text = input("Enter your string : ")
def make_dict(x):
    dict = {}
    for ltr in x:
        dict[ltr] = 1 + dict.get(ltr, 0)
    return dict


def most_frequent(text):
    ltrs = [ltr.lower() for ltr in text if ltr.isalpha()]
    dict = make_dict(ltrs)
    result = []
    for key in dict:
        result.append((dict[key], key))
    result.sort(reverse=True)
    for count, ltr in result:
        print (ltr, count)

most_frequent(text)
