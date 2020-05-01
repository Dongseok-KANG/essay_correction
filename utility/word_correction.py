def word_correction(seq_dict, sentence, phrase_dict):

    for key in sorted(seq_dict):
        item = seq_dict[key]
        print('\n' + '[\x1b[1;33m' + item + '\x1b[1;m]' + ' 아래와 같이 교정이 필요합니다.')
        phrase_dict2 = phrase_dict[item]
        phrase_dict2 = {k: v for k, v in phrase_dict2.items() if v is not 'None'} #단어 리스트에 빈 셀이 있을경우 삭제
        print(phrase_dict2)

        if len(phrase_dict2) == 1: #교정할 단어가 한가지만 있는 경우
            while 1:
                answer_ox = input("교정하시겠습니까? (y/n) : ")
                if answer_ox == 'y': #교정을 원할때(y를 선택한 경우)
                    sentence = sentence.replace(item, phrase_dict[item]['1'])
                    print(sentence + ' 로 교정되었습니다.')
                    break
                elif answer_ox == 'n': #교정하지 않고 그대로(n을 선택한 경우)
                    break
                else: #y,n이외의 문자를 넣었을때 다시 입력 받기
                    print('y 또는 n 중에 다시 입력해 주세요.')
                    continue

        else: #교정할 단어가 여러가지(최대 3가지)인 경우
            while 1:
                answer_ox = input("교정하시겠습니까? (y/n) : ")
                if answer_ox == 'y': #교정을 원할때(y를 선택한 경우)
                    answer = input('원하는 단어의 번호를 입력해 주세요 : ') #교정하면 좋을 단어를 보여주고 1,2,3 중에 입력받음
                    for i in range(len(phrase_dict[item])):  # 선택 반복문(1,2,3중에)
                        i = str(i)
                        if answer == i:
                            sentence = sentence.replace(item, phrase_dict[item][i])
                            print(sentence + ' 로 교정되었습니다.')
                    break
                elif answer_ox == 'n': #교정하지 않고 그대로(n을 선택한 경우)
                    break
                else:
                    print('y 또는 n 중에 다시 입력해 주세요') #y,n이외의 문자를 넣었을때 다시 입력 받기
                    continue

    return sentence