import streamlit as st
from PIL import Image
import os
import webbrowser

os.chdir(os.path.dirname(__file__))

st.set_page_config(
    page_title="中大车协-宣传招新",  # 页面标题
    page_icon=":bicyclist:",  # icon
    layout="centered",  # 页面布局
    initial_sidebar_state="auto"  # 侧边栏
)

# home_header_image = Image.open('pic001.png')
# st.image(home_header_image, caption='')

st.title('中山大学 Infinity 自行车协会')
st.subheader(':green[用车轮托载梦想，以双手把握方向]')
st.caption('本站由[:green[Herbal Jelly]](https://github.com/HerbalJelly23)提供技术支持')

st.header('车协招新宣传海报')
with st.expander('点击以收起宣传海报', expanded=1):
    poster_image = Image.open('./pic002.png')
    st.image(poster_image, caption='')

st.header('车协招新QA简报')
with st.expander('点击以收起QA简报', expanded=1):
    poster_qa_image = Image.open('./pic003.png')
    st.image(poster_qa_image, caption='')

col1, col2, col3 = st.columns(3)
if col1.button('Home-首页', use_container_width=True):
    webbrowser.open('https://ca-sysu.streamlit.app', new=0, autoraise=True)
if col2.button('骑行手册', use_container_width=True):
    webbrowser.open('https://ca-sysu.streamlit.app/%E2%80%8D%E5%9F%BA%E7%A1%80%E9%AA%91%E8%A1%8C%E6%89%8B%E5%86%8C', new=0, autoraise=True)
if col3.button('骑游分享', use_container_width=True):
    webbrowser.open('https://ca-sysu.streamlit.app/%E2%80%8D%E9%95%BF%E9%80%94%E9%AA%91%E6%B8%B8%E5%88%86%E4%BA%AB', new=0, autoraise=True)