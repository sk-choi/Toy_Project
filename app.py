# 스트림릿 라이브러리를 import하기
import streamlit as st
import pandas as pd
import numpy as np #데이터 처리를 위해 numpy와 pandas를 불러오기
# 스트림릿은 main함수 내에서 작동한다.
# 반드시 main 함수가 있어야 한다.

def main() :
    st.title('안녕하세요. ')
    st.title('Hello')

    st.markdown(':smile:')

    df = pd.read_csv('shelter_info.csv')#데이터 프레임으로 파일 불러오기(서울 방공호데이터 사용)
    st.dataframe(df) #main frame

    st.dataframe(df['좌표정보(x)']) #좌표정보(x)만 출력
    st.dataframe(df['좌표정보(y)']) #좌표정보(y)만 출력

    

    
if __name__ == '__main__' :
    main()