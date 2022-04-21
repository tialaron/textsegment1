import os

import streamlit as st

spisok_doc = os.listdir('/original_docs/')

st.set_page_config(layout='wide')
st.header('Рассмотрим работу нейронной сети по сегментации договоров.')

def doc_lines(textor_any):
  counter_str = 0
  for i in textor_any:
    if i == '\n':
      counter_str+=1
  return counter_str


counter2 = st.slider('Выберите номер документа для обработки',0,4,1)

col1, col2, col3 = st.columns(3)
with col1:
  with st.container():
    st.subheader('Оригинал договора')
    filename1 = '/original_docs/'+spisok_doc[counter2]
    f = open(filename1 ,'r',encoding="utf8")
    textor = f.read()
    st.write(textor)

with col2:
  with st.container():
    st.subheader('В данной работе проводится анализ договора')
    st.subheader('Каждый цвет отображает определенный элемент, который мы ищем.')

    st.markdown(f'<h1 style="color:#c71585;font-size:14px;">{"розовый  - Условия"}</h1>', unsafe_allow_html=True)
    st.markdown(f'<h1 style="color:#ff0000;font-size:14px;">{"красный - Запреты"}</h1>', unsafe_allow_html=True)
    st.markdown(f'<h1 style="color:#228b22;font-size:14px;">{"зеленый - Стоимость, всё про цены и деньги"}</h1>', unsafe_allow_html=True)
    st.markdown(f'<h1 style="color:#4169e1;font-size:14px;">{"синий   - Всё про сроки"}</h1>', unsafe_allow_html=True)
    st.markdown(f'<h1 style="color:#ff8c00;font-size:14px;">{"оранжевый - Неустойка"}</h1>', unsafe_allow_html=True)
    st.markdown(f'<h1 style="color:#00ffff;font-size:14px;">{"голубой - Всё про адреса и геолокации"}</h1>', unsafe_allow_html=True)

with col3:
  with st.container():
    st.subheader('Договор обработанный нейронной сетью.')
    filename2 = '/original_docs/'+spisok_doc[counter2]
    f2 = open(filename2 , 'r', encoding="utf8")
    textor2 = f2.read()
    #st.write(textor2)
    all_lines = doc_lines(textor2)
    all_doc = []
    str_doc = ''
    for i in textor2:
      if i != '\n':
        str_doc+=i
      elif i == '\n':
        all_doc.append(str_doc)
        str_doc = ''
    for j in range(all_lines):
      if '<s1>' in all_doc[j]:
        st.markdown(f'<h6 style="color:#c71585">{all_doc[j]}</h6>', unsafe_allow_html=True)
      elif '<s2>' in all_doc[j]:
        st.markdown(f'<h6 style="color:#ff0000">{all_doc[j]}</h6>', unsafe_allow_html=True)
      elif '<s3>' in all_doc[j]:
        st.markdown(f'<h6 style="color:#228b22">{all_doc[j]}</h6>', unsafe_allow_html=True)
      elif '<s4>' in all_doc[j]:
        st.markdown(f'<h6 style="color:#4169e1">{all_doc[j]}</h6>', unsafe_allow_html=True)
      elif '<s5>' in all_doc[j]:
        st.markdown(f'<h6 style="color:#ff8c00">{all_doc[j]}</h6>', unsafe_allow_html=True)
      elif '<s6>' in all_doc[j]:
        st.markdown(f'<h6 style="color:#00ffff">{all_doc[j]}</h6>', unsafe_allow_html=True)
      else:
        st.write(all_doc[j])




