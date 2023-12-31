import streamlit as st
from PIL import Image
import os
import webbrowser

os.chdir(os.path.dirname(__file__))

st.set_page_config(
    page_title="中大车协-宣传手册首页",  # 页面标题
    page_icon=":bicyclist:",  # icon
    layout="wide",  # 页面布局
    initial_sidebar_state="auto"  # 侧边栏
)

# home_header_image = Image.open('pic001.png')
# st.image(home_header_image, caption='')

st.title('中山大学 Infinity 自行车协会', anchor='home')
st.subheader(':green[用车轮托载梦想，以双手把握方向]')
st.caption('本站由[:green[Herbal Jelly]](https://github.com/HerbalJelly23)提供技术支持')

st.header('协会简介')
with st.expander('点击以收起协会简介', expanded=1):
    home_header_image = Image.open('./pic001.png')
    st.image(home_header_image, caption='')

    st.subheader('协会性质')
    content = '''
        :green[**中山大学 Infinity 自行车协会**]创办于2014年（珠海中山大学自行车协会先行创立于2002年，
        已于2019年并入:green[**中山大学 Infinity 自行车协会**]成为分会）旨在推动自行车运动在我校的发展，提高我校学生身体素质，
        并为爱好骑行和向往参加专业自行车比赛的同学提供一个交流的平台，是一个体育竞技类社团，
        在团委和体育部的指导下由骑行爱好者自发组建。截至2022年，本协会以东校区车协为总会，
        分会已遍布北、深、珠三校区， 为中大骑行爱好者提供服务并引导爱好者正确骑行。 
        社团活动主要以各种骑行为主，包括长短途骑游，专业山地车运动和专业公路车运动。平时活动范围以广州周边地区为主，
        在寒暑假会开展如环青海湖、环海南岛骑行等长途骑游活动。
    '''
    st.markdown(content)

    st.markdown('***')
    st.subheader('指导单位')
    content = '''
        :green[**中山大学 Infinity 自行车协会**]接受校党委的领导，校团委、体育部的指导，根据《高校学生社团建设管理办法》（教党【2020】13号）、
        《中山大学学生社团建设管理办法》（2020年9月1日起施行）开展活动。
    '''
    st.markdown(content)

    st.markdown('***')
    st.subheader('活动内容')
    content = '''
         * :green[**夜骑**]：主要在各校区周边路况、照明良好路段进行夜间骑行训练。  
         * :green[**骑游**]：一般为周末或节假日在校区附近作中短途骑游，往返距离约为50公里。  
         * :green[**竞速活动**]：不定期开展竞速比赛（个人计时赛）。  
         * :green[**假期长途骑游**]：节假日前往省内外如从化、花都、韶关、青海湖、海南岛等地开展长途骑游活动。  
         * :green[**其他**]：包括骑行相关讲座、参观自行车厂家、观看骑行比赛、跨校联谊等各种形式活动。  
    '''
    st.markdown(content)

    st.markdown('***')
    st.subheader('干部与会员权力与义务')
    content = '''
        * :green[**会长**]：拥有活动决策权，以及任命各部长的权力；有维护社团内良好氛围的义务。
        * :green[**副会长**]：拥有否决会长决策及任命的权力；有协助会长维护社团内良好氛围的义务。
        * :green[**各部长**]：拥有管理部内干事的权力；有提供良好骑行、社团内环境，听从会长副会长的义务。
        * :green[**干事**]：拥有活动优先参与权，以及会长、副会长、部长选举权与被选举权；义务是需听从部长指挥。
        * :green[**会员**]：拥有参与活动与提出建议的权力。
    '''
    st.markdown(content)

    st.markdown('***')
    st.subheader('社团内部规章制度——:green[总会与分会关系]')
    content = '''
        * :green[**会长**]：拥有活动决策权，以及任命各部长的权力；有维护社团内良好氛围的义务。
        * :green[**副会长**]：拥有否决会长决策及任命的权力；有协助会长维护社团内良好氛围的义务。
        * :green[**各部长**]：拥有管理部内干事的权力；有提供良好骑行、社团内环境，听从会长副会长的义务。
        * :green[**干事**]：拥有活动优先参与权，以及会长、副会长、部长选举权与被选举权；义务是需听从部长指挥。
        * :green[**会员**]：拥有参与活动与提出建议的权力。
    '''
    st.markdown(content)

    st.markdown('***')
    st.subheader('社团内部规章制度——:green[组织制度]')
    content = ''' 
        以下部门各设部长一名、干事若干名  
        * :green[**活动部**]：负责活动策划、带队出行、日常训练；  
        * :green[**秘书部**]：负责财政管理、活动申请、保险购买、人事管理等后勤事务；  
        * :green[**宣传部**]：负责推送制作、摆台宣传、摄影记录等宣传事务；  
        * :green[**技术部**]：负责自行车和骑行装备的采购、维护、使用指导；  
        * :green[**竞技部**]：负责协助活动部组织成员的日常训练，并参加各种专业比赛。  
        1. 本协会各校区分会内包含以上部门及职位（除会长必须设立外，其余部门职位根据各校区实际状况调整）：  
        会长一名，总管社团各项事务，拥有最终决策权、各部部长任免权；  
        副会长一名，协助会长管理社团事务，有权否决会长决策及任命；  
        2. 各干部干事及会员均可参与下一届会长、副会长、部长竞选，全员均可进行投票选举，一人一票。  
        3. 若干部不足可由会长任命。  
        4. 副会长可否决会长提议，歧义较大可进行社团内投票。  
        5. 原则上干部（会长、副会长、部长、干事）每学期至少要举行一次社团活动，干事需参与组织活动（摆台、海报、记录人员或后勤工作）。
    '''
    st.markdown(content)

    st.markdown('***')
    st.subheader('社团内部规章制度——:green[财政管理]')
    content = '''
        1. 经费来源  
        经费来源由学校下拨，不得收取会费，不得设立小金库，不得擅自收取费用。未经体育部批准，
        不得接受校外资助。经审核批准的校外资助经费纳入学习财务统一核算，统一管理。每学期向全体成员公布经费使用情况。
        任何单位和个人不得侵占、私分或挪用学生社团活动专项经费  
        2. 报销制度  
        各类活动、物资采购向体育部申请经费者，原则上由秘书部部长及干事负责相关事宜；
        若协会因人数较少而组织编制不全时，报销事宜由会长、副会长负责。  
        本协会每年度经费报销额度为1500元。  
        每次报销需完整保留相关文件记录以备核对检查。  
        3. 公共装备  
        本社团拥有工具箱、急救包、备用内外胎、气泵等统一采购的公共装备，资金来源于社团经费。
        上述各类装备由装备部保管（协会因人数较少而组织编制不全时由会长保管），不允许私人占用，需要使用时须向会长与装备部长公开提出申请。

    '''
    st.markdown(content)

    st.markdown('***')
    st.subheader('安全制度')
    content = '''
        1. 平常教授会员简单的骑行、保养车辆、维修车辆的知识，教授简单的急救知识（主要为摔伤应急处理）。  
        2. 每次出车（包括夜骑、骑游、竞速）前，所有人车辆要经过组织人员检查车况及装备，且所有人需至少佩戴头盔，
        竞速活动还需佩戴护肘、护膝及防滑手套、锁脚；夜骑必须装备车尾警示灯，若需要经过昏暗路段，还需装备照明前灯或头灯。  
        :red[**特别强调：不佩戴头盔者坚决不允许出车！**]  
        3. 骑行实行签到制，需签到才能参与活动、签退方可离开。  
        4. 骑游要两人或以上组队，一起骑行，并选出队长及时报告情况。  
        5. 骑行需有至少一人带药包（社团统一采购）。  
        6. 骑游前需教授参与人员简单急救知识，有条件邀请红十字会员参与。  
    '''
    st.markdown(content)

st.markdown('***')
col1, col2, col3 = st.columns(3)
if col1.button('车协招新', use_container_width=True):
    webbrowser.open('https://ca-sysu.streamlit.app/%E8%BD%A6%E5%8D%8F%E6%8B%9B%E6%96%B0', new=2, autoraise=True)
if col2.button('骑行手册', use_container_width=True):
    webbrowser.open('https://ca-sysu.streamlit.app/%E2%80%8D%E5%9F%BA%E7%A1%80%E9%AA%91%E8%A1%8C%E6%89%8B%E5%86%8C', new=2, autoraise=True)
if col3.button('骑游分享', use_container_width=True):
    webbrowser.open('https://ca-sysu.streamlit.app/%E2%80%8D%E9%95%BF%E9%80%94%E9%AA%91%E6%B8%B8%E5%88%86%E4%BA%AB', new=2, autoraise=True)

