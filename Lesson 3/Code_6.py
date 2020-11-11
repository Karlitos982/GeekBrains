def process(sentences):
    sent = sentences.split()
    return list(filter(no_rus_key, sent))


def no_rus_key(word):
    for i in word:
        if ord(i) < 65 or ord(i) > 122:
            return False
    return True


result = process("nice авп ъghj jапро hjjпаро вапрghgh cool")
for i in result:
    print(i.capitalize(), end=" ")
