from Queue import Queue


def generate_strings(num):
    chars = ["A", "B", "C", "D"]
    all_strings = Queue()
    for item in chars:
        all_strings.put(item)

    while all_strings.qsize() != pow(4, num):
        current = all_strings.get()
        for index, value in enumerate(range(len(chars))):
            all_strings.put(current+chars[index])

    strlist = []
    for num in range(pow(4,num)):
        strlist.append(all_strings.get())
    return strlist





