def word_corrections_index(sentence,word_dict):
    temp_dict = {}
    for item in word_dict.keys(): #csv파일에 있는 단어에 숫자를 지정해, 문장 처음부터 차례대로 교정하게끔 만들어줌
        if item in sentence:
            temp_dict[sentence.index(item)] = item

    return temp_dict



