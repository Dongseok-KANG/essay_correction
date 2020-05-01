import pandas as pd

def read_dict(): #final_error에서 단어 or 숙어 데이터 불러와서 dictionary 형태로 저장
    phrase_csv = pd.read_csv('../resource/final_error.csv')
    phrase_del = phrase_csv.fillna('None')
    phrase_dict = phrase_del.set_index('before').T.to_dict('dict')

    return phrase_dict




