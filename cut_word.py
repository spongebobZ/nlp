import json

words_path = 'test_dir/allfiles.txt'
dict_path = 'test_dir/big_dict.txt'

word_dict = dict()


def create_dict():
    with open(words_path, 'r', encoding='utf-8') as fr:
        for line in fr:
            words = line.strip().split(' ')
            for word in words:
                save_word(word, word_dict)
        persist_dict(dict_path, word_dict)


def persist_dict(path, d):
    with open(path, 'w', encoding='utf-8') as fw:
        fw.write(json.dumps(d))


def load_dict():
    with open(dict_path, 'r', encoding='utf-8') as fr:
        return json.loads(fr.read())


def save_word(word, d):
    if not word:
        d['end'] = 1
        return 0
    if word[0] not in d:
        d[word[0]] = dict()
    save_word(word[1:], d[word[0]])


def insert_word(word, d):
    save_word(word, d)
    persist_dict(dict_path, d)


def search_word(key, d):
    return d[key]


def cut_s(s, d):
    tmps = s
    r = []

    def get_max_word(s):
        notebook = [0] * len(s)
        notebook[0] = 1
        tmpd = d.get(s[0], {})
        for i in range(1, len(s)):
            r = tmpd.get(s[i], {})
            if r == {}:
                notebook[i - 1] = notebook[i - 1] - 1
                break
            notebook[i] = notebook[i - 1] + 1
            if len(r) == 1 and 'end' in r:
                break
            tmpd = r
        notebook[0] = 1
        return s[:max(notebook)]

    while tmps:
        max_word = get_max_word(tmps)
        r.append(max_word)
        tmps = tmps[len(max_word):]
    return r


# create_dict()
d = load_dict()
# insert_word('高洁云', d)
# d = load_dict()
print(json.dumps(search_word('大', d)))
s = '高洁云在学习大数据'
# print(cut_s(s, '', d, d))
print(cut_s(s, d))
