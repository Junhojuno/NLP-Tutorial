# Preprocessing function 만들기
# html 태그 제거 by BeautifulSoup
from bs4 import BeautifulSoup

# 특수문자 제거 by 정규표현식(re)
import re

# 어간추출, 형태소 분석 by SnowballStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import PorterStemmer

# 불용어 제거 by stopwords
from nltk.corpus import stopwords

def review_to_words(raw_review):
    # remove html tag
    review_text = BeautifulSoup(raw_review, 'html.parser').get_text()
    
    # remove special symbols(특수문자 제거)
    letters_only = re.sub('[^a-zA-Z]', " ", review_text)
    
    # 소문자 변환, 토큰화
    words = letters_only.lower().split()
    
    # remove stopwords, list-->set(for speed up)
    if remove_stopwords:
        stopword = set(stopwords.words('english'))
        words = [w for w in words if not w in stopword]
    
    # 어간 추출
    stemmer = PorterStemmer()
    words = [stemmer.stem(w) for w in words]
    
    return " ".join(stemming_words)