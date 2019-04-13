import yxxsd
import tf_idf

if __name__ == '__main__':
    base_dir = './allfiles/'
    file1 = '1business.seg.cln.txt'
    file2 = '31business.seg.cln.txt'
    key_word_1, word_list1 = tf_idf.get_key_words(base_dir + file1, 30)
    key_word_2, word_list2 = tf_idf.get_key_words(base_dir + file2, 30)
    common_key_word = []
    for w1 in key_word_1:
        for w2 in key_word_2:
            if w1 == w2:
                common_key_word.append(w1)
    result = yxxsd.get_yxxsd(word_list1, key_word_1, word_list2, key_word_2)
    print('the key word of %s is：%s' % (file1, ', '.join(key_word_1)))
    print('the key word of %s is：%s' % (file2, ', '.join(key_word_2)))
    print('common key word is:%s' % ', '.join(common_key_word))
    print('the Cosine similarity of %s and %s is: %s' % (file1, file2, result))
