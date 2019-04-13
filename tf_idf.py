import os
import math

#定义文件路径
base_dir = './allfiles/'

# 取得语料库列表,file_list是语料库文章list（带路径）
file_list = [base_dir + file for file in os.listdir(base_dir)]

# 取得停用词列表方法
def get_stop_words(stop_word_file):
    with open(stop_word_file, 'r', encoding='utf-8') as f:
        stop_words = [x.strip() for x in f.readlines()]
    return stop_words


# 取得停用词列表，stop_words是停用词list
stop_words = get_stop_words('./stop_words')


# 对文章进行分词以及过滤停用词方法,返回list
def cut_and_filte(file):
    word_list = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            list(map(word_list.append, [x for x in line.strip().split(' ') if x not in stop_words]))
    return word_list


# 计算语料库指定数量文章分词
def get_total_words(file_list, get_len=0):
    total_dict = {}
    if get_len == 0:
        for file in file_list:
            total_dict[file] = cut_and_filte(file)
        return total_dict
    else:
        for i, file in enumerate(file_list):
            total_dict[file] = cut_and_filte(file)
            if i > get_len - 1:
                break
        return total_dict



# 取得语料库文章分词信息,total_words是语料库文章dict信息，{filename1:[word1,word2],filename2...}
total_words = get_total_words(file_list)

# 计算TF
def cacl_tf(test_file_words):
    df_dict = {}
    for i in test_file_words:
        df_dict[i] = 0
        for j in test_file_words:
            if i == j:
                df_dict[i] += 1
    return df_dict


# 计算IDF
def cacl_idf(test_file_words,totalLen=0):
    idf_dict = {}
    #语料库长度
    total_len = len(file_list) if totalLen == 0 else totalLen
    for i in test_file_words:
        idf_dict[i] = 0
    for w in idf_dict:
        for words in total_words.values():
            if w in words:
                idf_dict[w] += 1
        idf_dict[w] = math.log(total_len/(idf_dict[w]+1))
    return idf_dict


# 计算目标文章每个词的TF-IDF，tfidf_dict是储存目标文章每个词的TF-IDF的dict，{'word1':0.123456,'word2':...}
def cacl_tfidf(test_file_words,totalLen=0):
    df_dict = cacl_tf(test_file_words)
    idf_dict = cacl_idf(test_file_words,totalLen)
    tfidf_dict = {}
    for i in test_file_words:
        tfidf_dict[i] = df_dict[i]*idf_dict[i]

    #对目标目标文章TF-IDF的value进行降序排序，输出是list，[(k1,v1),(k2,v2)...]
    tfidf_dict=sorted(tfidf_dict.items(),key=lambda k:k[1],reverse=True)
    return tfidf_dict

#入口函数，需要传入计算文件、期望关键词数量、可选语料库数量0为全部,返回指定数量关键词和文章的分词list
def get_key_words(file,key_nums,total_files_cnt=0):
    test_file_words = cut_and_filte(file)
    tmp=cacl_tfidf(test_file_words,total_files_cnt)
    result=[]
    for i in range(key_nums):
        result.append(tmp[i][0])
    return result,test_file_words


