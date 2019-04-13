import math


# 计算句子向量方法
def word_2_vec(list, word_set):
    vec_list = [0] * len(word_set)
    for i, word in enumerate(word_set):
        for ele in list:
            if ele == word:
                vec_list[i] += 1
    return vec_list


# 计算余弦相似度
def count_yxxsd(vec1, vec2):
    fz = 0
    for i in range(len(vec1)):
        fz += vec1[i] * vec2[i]
    mo1 = 0
    for i in list(map(lambda x: x ** 2, vec1)):
        mo1 += i
    mo1 = math.sqrt(mo1)
    mo2 = 0
    for i in list(map(lambda x: x ** 2, vec2)):
        mo2 += i
    mo2 = math.sqrt(mo2)
    fm = mo1 * mo2
    result = fz / fm
    return result


# 入口函数，需要传入两个文本的分词列表、关键词列表
def get_yxxsd(word_list1, list1_key_list, word_list2, list2_key_list):
    s1_set = set(list1_key_list)
    s2_set = set(list2_key_list)
    set_cnt = s1_set.union(s2_set)
    s1_vec = word_2_vec(word_list1, set_cnt)
    s2_vec = word_2_vec(word_list2, set_cnt)
    result = count_yxxsd(s1_vec, s2_vec)
    return result
