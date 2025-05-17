#https://blog.zarathu.com/posts/2023-02-01-streamlit/

import streamlit as st

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다.
tab1, tab2 = st.tabs(['Tab A', 'Tab B'])

with tab1:
    # tab A 를 누르면 표시될 내용
    st.write('hello')
    # st.sidebar는

    st.sidebar.title('this is sidebar')
    st.sidebar.checkbox('체크박스에 표시될 문구')
    # 사이드바에 체크박스, 버튼등 추가할 수 있습니다!

with tab2:
    # tab B를 누르면 표시될 내용
    st.write('hi')