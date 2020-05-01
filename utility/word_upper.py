import pandas as pd

def word_upper(sentence):
    noun_csv = pd.read_csv('../resource/noun.csv') #고유명사만 저장되어 있는 csv파일을 불러옴
    sentence = sentence.lower()
    sentence = sentence.capitalize() #문장의 첫글자는 대문자로 시작

    for item in noun_csv.keys(): #고유명사인 경우 첫글자 대문자로 바꿀지 말지
        if item in sentence:
            print('\n' + '[\x1b[1;33m' + item + '\x1b[1;m]' + ' 아래와 같이 교정이 필요합니다.')
            print('{' + item.capitalize() + '}')
            answer_ox = input("교정하시겠습니까? (y/n) : ")
            if answer_ox == 'y':
                sentence = sentence.replace(item, item.capitalize())

    print('\n' + '최종 문장입니다. : ' + sentence) #교정이 완료된 최종 문장 보여줌
    print('교정을 종료합니다. 워드바이스를 이용해주셔서 감사합니다.')










