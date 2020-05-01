def word_color(seq_dict, sentence): #교정해야 할 단어 노란색으로 보여주기
    print('입력하신 문장입니다. : ' + sentence) #입력받은 문장 보여주기
    for key in (seq_dict):
        item = seq_dict[key]
        sentence = sentence.replace(item, '\x1b[1;33m' + item + '\x1b[1;m') #교정 단어마다 색 변경
    print('교정이 필요한 단어들입니다. : ' + sentence)





