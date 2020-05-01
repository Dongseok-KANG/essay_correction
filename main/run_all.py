import pandas as pd

from utility import read_dict
from utility import word_color
from utility import word_correction_index
from utility import word_correction
from utility import word_upper

sentence = input('>>> ')
# but this study is important

phrase_dict = read_dict.read_dict() #csv파일 데이터 불러오기
seq_dict = word_correction_index.word_corrections_index(sentence, phrase_dict) #교정 순서를 위해
word_colored = word_color.word_color(seq_dict, sentence) #교정될 단어 색 변경하여 보기좋게
sentence_fin = word_correction.word_correction(seq_dict, sentence, phrase_dict) #실제 교정이 이루어짐
word_upper.word_upper(sentence_fin) #문장의 첫글자 or 고유명사 대문자로 변경
