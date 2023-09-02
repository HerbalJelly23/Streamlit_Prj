import streamlit as st
from PIL import Image
import webbrowser

st.set_page_config(
    page_title="中大车协-基础骑行手册",  # 页面标题
    page_icon=":bicyclist:",  # icon
    layout="wide",  # 页面布局
    initial_sidebar_state="auto"  # 侧边栏
)

# home_header_image = Image.open('pic001.png')
# st.image(home_header_image, caption='')

st.title('中山大学 Infinity 自行车协会')
st.subheader(':green[用车轮托载梦想，以双手把握方向]')
st.caption('本站由[:green[Herbal Jelly]](https://github.com/HerbalJelly23)提供技术支持')

st.markdown('***')
st.header('《基础骑行手册》')
st.markdown('***')

st.subheader('骑行装备', anchor='sec1')
with st.expander('点击以收起章节', expanded=1):
    content = '''
        * :green[**车辆的种类、特点、品牌**]  
        山地车、公路车、攀爬车、土坡车、BMX、死飞、淑女车  
          * 山地车： 
          * 公路车： 
          * 攀爬车： 
          * 土坡车： 
          * BMX： 
          * 死飞： 
          * 淑女车： 
          
          ***
        * :green[**安全装备**]  
        头盔、护膝与护肘、风镜、照明灯、尾灯  
          * 头盔： 
          * 护膝与护肘： 
          * 风镜： 
          * 照明灯： 
          * 尾灯： 
          
          ***
        * :green[**进阶装备**]  
        骑行服、锁鞋与锁踏/狗嘴与束带、码表、心率计、踏频/速度计、功率计  
          * 骑行服： 
          * 锁鞋与锁踏/狗嘴与束带： 
          * 码表： 
          * 心率计： 
          * 踏频/速度计： 
          * 功率计： 
          
          ***
        * :green[**车辆升级选择**]  
        车架、轮组、内外胎、牙盘套件、坐垫、刹车、车把与把立、变速  
          * 车架：  
          * 轮组：  
          * 内外胎：  
          * 牙盘套件：  
          * 坐垫：  
          * 刹车：  
          * 车把与把立：  
          * 变速：  
          
          ***
        * :green[**团队保障装备**]  
        维修、给养、医疗、后勤车“4+2”
          * 维修：  
          * 给养：  
          * 医疗：  
          * 后勤车：  
    '''
    st.markdown(content)

st.subheader('骑行安全技术', anchor='sec2')
with st.expander('点击以收起章节', expanded=1):
    content = '''
        * :green[**独自骑行**]  
          * :green[①]选择正确车道，遵守交规  
            没有自行车道的情况下，在机动车道上靠着右边走；优先走自行车道，但要看情况，过于窄、
            拥挤或障碍物多的自行车道还不如机动车道安全。  
            遵守交规，不要闯红灯、逆行，不要闯入隧道、高速、高架等非机动车禁入区域，不要在校道等拥挤路段飙车；
            弯道中控制车速，尽量不要进入对向车道。  
            ***
 
          * :green[②]转弯姿势：  
            正确的转弯：转弯一侧的脚踏要转到高位，避免倾斜时刮到脚踏（如：向右转时，右脚在高位、左脚在低位）；
            转动车把的幅度要小，主要靠身体重心倾斜来转弯（“压弯”），但要注意幅度。自行车胎比摩托窄得多，抓地力有限，压弯太深容易侧滑（尤其是公路车）。
            入弯前要减速，转弯中不要急刹车（尤其路面有水渍、沙石的时候！），否则容易因轮胎抱死侧滑。多加练习。
            ***

          * :green[③]如何使用变速器：  
            变速的原理：观察你的传动系统。一般变速车均有1-3个和踏板相连的大齿轮（牙盘），多个后轮上被带动的小齿轮（飞轮）。通过车把上的手变可以带动变速器，将链条挂上不同的牙盘和飞轮，各车型具体操作方法不同（一般左手控制牙盘，右手控制飞轮）。只有边踩边换挡才有用。  
            牙盘小、飞轮大时，为低档位，踩一圈踏板，后轮转过的圈数少。此时单车踩踏省力，爬坡、加速能力强，但速度没法太快。  
            牙盘大、飞轮小时，为高档位，踩一圈踏板，后轮转过的圈数多。此时单车踩踏费力，但能达到更高速度。  
            一般而言，起步、上坡、崎岖路面用较低档位，平路巡航或下坡用较高档位。请视情况灵活使用档位。  
            上坡前、停车前，提前降低档位，避免在链条承受大拉力时（脚下踩不动）时才换档，容易伤害变速器。  
            ***

        
          * :green[④]如何减少爆胎：  
            1. 如在机动车道上靠右走，没有汽车经过时不要过于贴近路边，路边往往有井盖、碎石、铁屑铁钉等杂物。  
            2. 目光不要离开路面，保持警惕（尤其高速巡航时），避免碾到坑洼、突起物，在安全的情况下避让（不要突然急转，小心翻车或后方来车）。如避让不及，减速后碾过去。  
            3. 要根据外胎上的标识、自身体重、应对路面选择正确的胎压，后面说换胎时会详谈。  
            4. 公路车的外胎比较薄弱，如果技术不过硬，不要强行挑战非铺装路面，更加不要尝试跳台阶、下路肩一类操作。路太烂时下车推过去无妨。  
            ***

            
          * :green[⑤]如何避免事故：  
            1. 主动防御驾驶：主动戒备路上其他交通参与者，保持安全车距，礼让一切，包括四轮、二轮、行人，千万不要有“我有路权”的想法（自行车撞谁都撞不赢，也撞不起），更加不要主动违反交规。路过路口、公交站、斑马线，减速观察。  
            尤其远离大型车，大型车驾驶位高，盲区很大，且在其转弯时，转向的一侧前后轮间会产生一个能将二轮车与行人卷入的危险区。遇大车应尽量远离或快速通过。  
            可以用手势示意，请汽车先过或减速为你让行，对方能明白即可。注意礼貌。  
            2. 不要疲劳驾驶。长时间、高强度骑行时，疲劳会影响精神状态，造成注意力分散，不能对路况变化及时做出反应。应该适时停下休息，补充水分糖分盐分。  
            3. 上下坡不要逞能！无论上下坡，把握不住就推车走！  
            上坡提前调整到合适档位，不要上坡时踩不动才降档，对变速器伤害很大，而且容易零速摔。上坡不要勉强，快踩不动就主动下车推（如穿了锁鞋，提前脱锁，以免停车时无法挣脱而摔倒）。  
            下坡尤为危险！升高档位，和前车保持距离，始终将速度保持在自己能控制的范围内。善用点刹（一下一下刹车），长时间捏住刹车（拖刹）会加剧过热和磨损。下坡时急刹效果不佳，入弯前一定要提前减速！另：长时间下坡捏刹车，手会严重疲劳。务必坚持住，或者停下休息。  
            4. 应对爆胎等车况异常：行驶中发现爆胎、掉链、异响、刹车失灵等异常，立刻停止踩踏，缓慢靠边，千万不要路中间突然急停。停下后再检查情况、排除异常。  
            爆胎不要继续骑着走！没有气的情况下承重，轮圈会受压变形！  
            5. 应对抽筋：四肢发生抽筋时，保持冷静，抽筋的肢体不要尝试做任何动作，首先控制车辆缓慢减速，靠边停车，保证紧急情况跳车可以倒向车流量少的地方（比如人行道的合适路段）。停车后，有队友的话第一时间通知队友，不严重的话，补充适当电解质，进行拉伸放松，检查无肌肉拉伤后，经过短暂休息可以继续骑行；否则打车返回，不得冒险。  
            6. 几种致命陷阱  
            车道分隔线（虚、实线）：车道分隔线是油漆面，摩擦力不如路面。有些地方的车道分隔线甚至可能直接令车滑倒。不要长时间骑线行驶。  
            水渍和沙石：水渍和沙石会导致严重的侧滑翻车风险（尤其是带着刹车进弯的时候），更不用说水渍还可能是汽车漏下的机油！务必万分小心。  
            伸缩缝和排水渠盖：和路面平行的伸缩缝和排水渠盖开口有可能宽于轮胎，导致车轮直接陷进去卡住翻车，尤其是胎宽窄的公路车23C轮胎。若发现这种情况，走斜线跨过去避免陷车，或直接下车推车。  
            与前进方向平行的低路肩或路面高低级差：当要跨越这种级差时，应该大打一把方向拐上去，不要试图并线“蹭”上去。轮胎侧边磨到路肩极易令车失去平衡，外胎也会因此损坏。  
            ***
          
          * :green[⑥]如何使用锁鞋/狗嘴/束带：  
            如前述，锁鞋是与锁踏搭配，将脚掌以一定角度锁定在踏板上的专用鞋子，可以改善发力、提高踩踏稳定性。死飞所用的狗嘴和束带也有类似作用（再次强调不推荐骑死飞）。  
            使用锁鞋等脚掌束缚装备，必须在出车前勤加练习，形成能迅速上锁脱锁的肌肉记忆。锁鞋的基本锁定方式时“前勾后踩”，锁片前段勾住锁踏后，脚掌心向下踩，若上锁成功会有“咔”的声响。脱锁方式为“脚跟外拐”，脚掌呈内八字方向将脚跟向外转就能脱锁。狗嘴和束带则将脚向前伸入/向后抽出即可。  
            锁踏导致的事故最常见为零速摔（原地摔），多为停车/上坡踩不动时来不及脱锁导致。要记得停车前提前脱锁，“车还在动就不会倒”。  
            ***
  
          * :green[⑦]如何使用锁鞋/狗嘴/束带：    
            1. 关注天气：天气不佳不要出车（高温暴晒、寒冷、有雨、大风、冰雪……等），要根据气温做好防暑防晒或保暖措施。如遇阵雨，尽量找地方避雨。湿身注意感冒，车辆打湿之后要及时清洁、擦干、补上油，放置于通风干燥处。  
            2. 照明设备：夜骑要装备照明设备，配备尾灯和前灯/头灯。光照不良时降低车速。  
            3. 补充水糖盐：  
            水分：少量多次，以常温最佳。尽量不要喝冰水。能量饮料、泡腾饮料也可，注意不要过浓。  
            糖分：大pro们会食用能量胶。一般骑游，香蕉、能量棒、士力架都是可行选择（注意口渴）。  
            盐分：竞技时建议吃专用的盐丸。如果只是骑游，喝运动饮料或直接吃点小鱼干豆干一类的小吃也行。  
            4. 关于导航：出发前提前确认路线（可以用骑行软件的路书），尽量避开正在修路和过于繁忙的路段。在路上，有导航功能的码表是最好选择，否则只能用手机。（据笔者测试，几乎没有手机架能保证在单车上夹稳手机，要留意检查）。  
            最好准备两个以上地图软件作为备选项；活用地图中步行、骑行、汽车三种交通方式的路线规划。  
            ***

        * :green[**团队骑行**]  
          * :green[①]手势  
            没有自行车道的情况下，在机动车道上靠着右边走；优先走自行车道，但要看情况，过于窄、
            拥挤或障碍物多的自行车道还不如机动车道安全。  
            遵守交规，不要闯红灯、逆行，不要闯入隧道、高速、高架等非机动车禁入区域，不要在校道等拥挤路段飙车；
            弯道中控制车速，尽量不要进入对向车道。  
            ***
            
          * :green[②]在队列中  
            没有自行车道的情况下，在机动车道上靠着右边走；优先走自行车道，但要看情况，过于窄、
            拥挤或障碍物多的自行车道还不如机动车道安全。  
            遵守交规，不要闯红灯、逆行，不要闯入隧道、高速、高架等非机动车禁入区域，不要在校道等拥挤路段飙车；
            弯道中控制车速，尽量不要进入对向车道。  
            ***
            
          * :green[③]在集团中  
            没有自行车道的情况下，在机动车道上靠着右边走；优先走自行车道，但要看情况，过于窄、
            拥挤或障碍物多的自行车道还不如机动车道安全。  
            遵守交规，不要闯红灯、逆行，不要闯入隧道、高速、高架等非机动车禁入区域，不要在校道等拥挤路段飙车；
            弯道中控制车速，尽量不要进入对向车道。  
            ***
        
          * :green[④]其他  
            没有自行车道的情况下，在机动车道上靠着右边走；优先走自行车道，但要看情况，过于窄、
            拥挤或障碍物多的自行车道还不如机动车道安全。  
            遵守交规，不要闯红灯、逆行，不要闯入隧道、高速、高架等非机动车禁入区域，不要在校道等拥挤路段飙车；
            弯道中控制车速，尽量不要进入对向车道。  
    '''
    st.markdown(content)

st.subheader('基本维修技术', anchor='sec3')
with st.expander('点击以收起章节', expanded=1):
    content = '''
        * :green[**换胎**]  

        ***
        * :green[**姿势设定调整**]  
        
        ***
        * :green[**维护传动系统**]  

        ***
        * :green[**刹车调整**]  

        ***
        * :green[**须及时送往车店的故障**]
    '''
    st.markdown(content)

st.markdown('***')
st.subheader('本文协作者')
with st.expander('点击以展开章节', expanded=0):
    st.caption('李仲元（2019届珠海分会会长-起草）')
    st.caption('曾蠡（2019届东校总会装备部部长-起草）')
    st.caption('胡润楠（2019届东校总会会长-起草）')
    st.caption('严志宇（2021届珠海分会会长-修订）')



with st.sidebar:
    st.subheader('手册目录')
    content = '''
        [:green[**骑行装备**]](%E2%80%8D基础骑行手册#sec1)  
        * [:green[车辆的种类、特点、品牌]](%E2%80%8D基础骑行手册#sec1)  
        * [:green[安全装备]](%E2%80%8D基础骑行手册#sec1)  
        * [:green[进阶装备]](%E2%80%8D基础骑行手册#sec1)  
        * [:green[车辆升级选择]](%E2%80%8D基础骑行手册#sec1)  
        * [:green[团队保障装备]](%E2%80%8D基础骑行手册#sec1)  

        [:green[**骑行安全技术**]](%E2%80%8D基础骑行手册#sec2)  
        * [:green[独自骑行]](%E2%80%8D基础骑行手册#sec2)  
        * [:green[团队骑行]](%E2%80%8D基础骑行手册#sec2)  
        
        [:green[**基本维修技术**]](%E2%80%8D基础骑行手册#sec3)  
        * [:green[换胎]](%E2%80%8D基础骑行手册#sec3)  
        * [:green[姿势设定调整]](%E2%80%8D基础骑行手册#sec3)  
        * [:green[维护传动系统]](%E2%80%8D基础骑行手册#sec3)  
        * [:green[刹车调整]](%E2%80%8D基础骑行手册#sec3)  
        * [:green[须及时送往车店的故障]](%E2%80%8D基础骑行手册#sec3)  
    '''
    st.markdown(content, unsafe_allow_html=True)

st.markdown('***')
col1, col2, col3 = st.columns(3)
if col1.button('Home-首页', use_container_width=True):
    webbrowser.open('https://ca-sysu.streamlit.app', new=2, autoraise=True)
if col2.button('车协招新', use_container_width=True):
    webbrowser.open('https://ca-sysu.streamlit.app/%E8%BD%A6%E5%8D%8F%E6%8B%9B%E6%96%B0', new=2, autoraise=True)
if col3.button('骑游分享', use_container_width=True):
    webbrowser.open('https://ca-sysu.streamlit.app/%E2%80%8D%E9%95%BF%E9%80%94%E9%AA%91%E6%B8%B8%E5%88%86%E4%BA%AB', new=2, autoraise=True)