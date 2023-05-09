import operator

def count(article):  #iss code ko views.py ke def result se utaya h.taki views.py easy dikh ske.or is code ko def count() mai daal diya h.
    words = article.split()  # iska mtlb h ki ye words ko space se split krega
    word_count = len(words)  # ye words ko count krega
    dict_word = {}
    for word in words:
        if word in dict_word:
            dict_word[word] += 1
        else:
            dict_word[word] = 1
    var_dict = sorted(dict_word.items(), key=operator.itemgetter(1), reverse=True)

    return var_dict, word_count