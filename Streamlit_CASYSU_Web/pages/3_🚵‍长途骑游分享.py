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

st.title('中山大学Infinity自行车协会')
st.subheader(':green[用车轮托载梦想，以双手把握方向]')
st.caption('本站由[:green[Herbal Jelly]](https://github.com/HerbalJelly23)提供技术支持')

st.markdown('***')
st.header('《胡润楠会长的骑游经验分享》')
st.markdown('***')

content = '''
    现金：主要是用于支付个别轮渡，手机电量耗尽后的补给购买。有时晴天出行手机稍加使用就高烧不退，进而导致部分型号的触屏热敏电阻工作情况不佳，现金支付也显得更加方便。现金携带最好放在骑行服的防水袋中，不然出汗以后，感觉怪怪的。  
    天气：提前关注，太热易于中暑，太冷注意热身，不然易于抽筋。阴天骑行要未雨绸缪，淘宝上有专门的骑行雨衣，鞋套，价格自由度也较大，但雨衣个人推荐100元以上的非一次性装备。以广州的天气，常常遇到突然出现的暴雨，不过有时在路边等个半个小时就会停了，所以不必头铁雨骑。另外，学会利用实时天气预报软件（学会用这个这还能避免你期中期末泡馆复习时，不会在饭点时被困在冷气十足的图书馆挨饿，有过类似经历的小盆友一定印象深刻）。最后一点，雷暴天不要出车，雷雨天不要在树下避雨。  
    时刻注意行车安全：  
    1. 不要疲劳驾驶。骑行时多少比走路快些，有时你已经累了，但自己不觉 得，但注意力已经开始分散，不能对路况变化及时做出反应。应该定时停下休息，补充水分糖分盐分。
    2. 注意车况，有异常（一般是异响）冷静对待，最好及时维护，不能排除异常时，检查各螺栓是否松动，制动是否正常，没有问题的话，可以低速骑行。
    意外情况：  
    3. 高速巡航时，遇到路上有坑，大的突起物，如避让困难，建议尽量减速后碾过去，突然变道可能会被后车撞到，而且强行避让可能引起侧滑导致摔车
    4. 四肢发生抽筋时，保持冷静，抽筋的那只手（那条腿）不要尝试做任何动作，首先控制车辆缓慢减速，然后这个过程尝试向路边靠近，保证紧急情况跳车时不会躺尸路中央，而是可以倒向车流量少的地方（比如人行道的合适路段）。停车后，有队友的话第一时间通知队友，不严重的话，补充适当电解质，进行拉伸放松，检查无肌肉拉伤后，经过短暂休息可以继续骑行；否则打车返回，不得冒险。
    关于特殊路段：  
    5. 上下坡：上坡前适当加速，开始爬坡后，前面自选，后面挂较大的飞轮，不要踩不动才换，避免零速摔，不建议萌新一直摇车，因为你可能会在到达坡顶前耗尽体力导致控车出现失误。下坡注意保持与前车的距离，前方摔车后有足够反应时间；不要大力捏刹车，可能会抱死，然后后轮发飘摔车。前面挂大的牙盘，后面挂最小的飞轮，便于控车。
    6. 转弯前，观察人流与车流，大型车辆转弯时，车身会向内偏移，最好留3M以上的距离  
    7. 当路边有靠边停车的车辆时，注意保持距离，有些人会无转向灯启动或无警示开门下车  
    8. 不要在弯道占用逆向车道超车  
    9. 货车，大巴因为驾驶位较高，存在视野盲区，可以的话，快速通过或减速远离，详情：[:green[参考条目]](https://www.sohu.com/a/244478427_99901299)  
    
    人身安全：  
    饮食：  
    1. 饭后半小时不宜运动，但不是坐着不动，不要瞎搞就行；饭后一个半小时内不宜剧烈运动，否则可能引起胃下垂。  
    2. 均衡补充，蛋白质在不影响消化时，可以多多益善  
    3. 有条件的话，到卫生条件有保障的店面解决  
    4. 不要吃得太饱，奶茶什么的适可而止  
    
    防中暑：  
    主要是在发生先兆中暑时，及时应对。也就是说，难点在于，区分中暑与运动导致的必然的疲劳与不适，这点希望各医学生支招。
'''
st.markdown(content)

with st.expander('中暑临床表现', expanded=0):
    content = '''
        :green[中暑临床表现]  
        根据我国《职业性中暑诊断标准》（GB11508-89），中暑分为先兆中暑、轻症中暑、重症中暑。  
        1. 先兆中暑　  
        在高温环境下，出现头痛、头晕、口渴、多汗、四肢无力发酸、注意力不集中、动作不协调等，体温正常或略有升高。  
        2. 轻症中暑  
        除上述症状外，体温往往在38℃以上，伴有面色潮红、大量出汗、皮肤灼热，或出现四肢湿冷、面色苍白、血压下降、脉搏增快等表现。  
        3. 重症中暑  
        包括热痉挛、热衰竭和热射病。  
        热痉挛是突然发生的活动中或者活动后痛性肌肉痉挛，通常发生在下肢背面的肌肉群（腓肠肌和跟腱），也可以发生在腹部。肌肉痉挛可能与严重体钠缺失（大量出汗和饮用低张液体）和过度通气有关。热痉挛也可为热射病的早期表现。  
        热衰竭是由于大量出汗导致体液和体盐丢失过多，常发生在炎热环境中工作或者运动而没有补充足够水分的人中，也发生于不适应高温潮湿环境的人中，其征象为：大汗、极度口渴、乏力、头痛、恶心呕吐，体温高，可有明显脱水征如心动过速、直立性低血压或晕厥，无明显中枢神经系统损伤表现。热衰竭可以是热痉挛和热射病的中介过程，治疗不及时，可发展为热射病。  
        热射病是一种致命性急症，根据发病时患者所处的状态和发病机制，临床上分为两种类型：劳力性和非劳力性热射病。劳力性者主要是在高温环境下内源性产热过多，多见于健康年轻疼，常见重体力劳动、
        体育运动（如炎热天气中长距离的跑步者）或军训时发病。高热、抽搐、昏迷、多汗或无汗、心率快，它可以迅速发生。其非劳力性主要是在高温环境下体温调节功能障碍引起散热减少
        （如在热浪袭击期间生活环境中没有空调的老年人），它可以在数天之内发生。其征象为：高热（直肠温度≥41℃）、皮肤干燥（早期可以湿润），意识模糊、惊厥、甚至无反应，
        周围循环衰竭或休克。此外，劳力性者更易发生横纹肌溶解、急性肾衰竭、肝衰竭、DIC或多器官功能衰竭，病死率较高。  
    '''
    st.markdown(content)

with st.expander('中暑的治疗', expanded=0):
    content = '''
        :green[中暑的治疗]  
        1. 先兆中暑与轻症中暑的治疗
        立即将患者转移到阴凉通风处或电风扇下，最好移至空调室，以增加辐射散热，给予清凉含盐饮料，体温高者给予冷敷。
        2. 重症中暑的治疗
            * 降温治疗
            快速降温是治疗的首要措施。
                * 体外降温：迅速脱离高温高湿环境，转移至通风阴凉处，将患者平卧并去除全身衣物，对皮肤肌肉按摩，促进散热。无循环障碍者，冰水擦浴或将躯体侵入27℃~30℃水中降温。对循环障碍者，采用蒸发散热降温，用凉水反复擦拭皮肤，同时应用电风扇或空调加快蒸发。
                * 体内降温：体外降温无效者，用冰盐水进行胃或直肠灌洗，也可用无菌生理盐水进行腹膜腔灌洗或血液透析，或将自体血液体外冷却后回输体内降温。
                * 药物降温：患者出现寒战时可应用氯丙嗪静脉输注．并同时监测血压。
            * 对症处理
                * 昏迷患者应保持呼吸道畅通，给予吸氧，必要时气管插管。
                * 积极纠正水、电解质紊乱，维持酸碱平衡。
                * 补液速度不宜过快，以免触发心力衰竭，发生心力衰竭予以快速效应的洋地黄制剂，
                * 应用升压药纠正休克。
                * 疑有脑水肿患者应给甘露醇脱水。
                * 有急性肾衰竭患者可进行血液透析。
                * 发生弥散性血管内凝血时酌情使用肝素，需要时加用抗纤维蛋白溶解药物。
                * 肾上腺皮质激素对高温引起机体的应激和组织反应以及防治脑水肿、肺水肿均有一定的效果，但剂量不宜过大，用药时间不宜过长，以避免发生继发感染。
                * 积极防治感染。
    '''
    st.markdown(content)

content = '''
    其他：和你外出旅游差不多，重要证件啦，深夜女生不独自外出啦.......不作死就行，但还是建议大一新生们上网看看，避免有所遗漏。
    小动物：狗，笔者在海南被狗追过，所以建议大家，进村后正常一点，不过一般大多数人拼命骑还是比狗狗快的。
    
    :green[**夜骑**]      
    1. 前灯：两百流明市区足矣，其它区域建议400流明+，另外淘宝商家给出的续航真假难辨，建议自己试试看。如果购买充电锂电池的，不要贪便宜，也不要乱接充电头，锂电池爆炸不是闹着玩的。
    2. 尾灯：组队夜骑时，押尾的同学必须配备尾灯。尾灯电量不多时，不时观察一下，免得他挂了你还不知道。
    3. 速度：根据前灯，路灯（有些路段两路灯中间比较黑）的有效照明距离，与自身反应速度决定车速上限，实际情况是，若没有路灯，建议20以下巡航。
    4. 如果身处相对荒凉的地方，不必犹豫，打车吧，货拉拉，打车软件皆可。
    导航与路线选择：广州的城市建设规划对非机动车其实不太友好。最好准备两个以上地图软件作为备选项；活用地图中步行，骑行，汽车三种交通方式的路线规划，但一般而言不要上高速。有些地段存在这种情况，扛车几米换条路可以少走几公里（即参考步行方案改进路线）；或路况极差不如绕远路（即参考汽车方案改进路线，考虑到开车普遍不慢，导航倾向于推荐路况较好的，路口较少的路线）
    补给：
    1. 购买自行车时，选购能装载两个水壶架的车架。已经买了只能装一个的，不要在没有孔洞的地方自己开孔，可能会造成车架损坏与安全问题。有两瓶水能有效规避断水。可以加装龙头包，上杆包，座管包，用于摆放各种物资与消耗性补给，而不是背一个大双肩包，另外绝对不要背单肩包。长途骑行如果背包太重，会对脊柱和腰部肌肉，核心区肌肉造成损伤。
    2. 补充水分糖分盐分：
    水分：少量多次，以常温最佳。尽量不要喝冰水。
    糖分：碳水化合物和单糖中的葡萄糖都是十分重要的能量来源，总的来说
    碳水持久性好些，而葡萄糖适合快速（个人感觉大概15min后起效）补给。注意一次不要吃太多。
    盐分：竞技时建议专门的盐丸，淘宝自己买。但如果你只是骑游，觉得不划算，也有很多办法（野路子），比如，骑游时我的做法是脉动1：1或1：1.5兑水喝。如果状态还可以 ，少量吃一些高盐食品也行（卤鸡蛋，卤XX.......）。Ps：但无论补充糖分还是盐分，如果出现胃部的渗透压太高的意外，会非常难搞，这时候你喝的水难以被快速吸收。然后口渴，再然后你就不知不觉地喝了一肚子水，然后就得边用腹肌固定着这个水袋，边忍受着口渴，边骑车（awsl，没错我就这么干过，你们快可怜本宝宝）
    修理维护：  
    工具：  
    1. 一个组合式螺丝刀，淘宝大概二十元一个，便宜好用
    2. 薄片扳手三+个
    3. 翘胎棒三根，实用还都不贵
    4. 便携式气筒，最好带气压计（大概100RMB）
    5. 补胎片，分需要胶水和不需要胶水的，按需挑选；记得携带配套的锉子，不然没法修。
    技能：会拆、装自己的车，能补胎（这是没带备胎时的选择，回来记得及时换）换胎，能实时调节座包高度，刹车线松紧（优先保证制动性能，其次力求手感舒适）  
    防晒：腿套，袖套，或长袖长裤骑行服，但不要穿太多会中暑；面罩（顺便防尘（保护咽喉），防灰（出汗以后小脸容易沾灰））；防晒霜，主要是涂耳朵，手指脸，等未被遮住的部位  
    受伤与医药：  
    1. 创可贴，可以的话，再带上消毒与跌打肿痛类的药物
    2. 有中暑经历的，又要白天骑到没药店的地方的，注意自备解药
    3. 可以上网学习伤口处理方法
'''
st.markdown(content)

st.markdown('***')
st.subheader('本文协作者')
with st.expander('点击以展开章节', expanded=0):
    st.caption('胡润楠（2019届东校总会会长-起草）')
    st.caption('严志宇（2021届珠海分会会长-修订）')

st.markdown('***')
col1, col2, col3 = st.columns(3)
if col1.button('Home-首页', use_container_width=True):
    webbrowser.open_new('https://ca-sysu.streamlit.app')
if col2.button('车协招新', use_container_width=True):
    webbrowser.open('https://ca-sysu.streamlit.app/%E8%BD%A6%E5%8D%8F%E6%8B%9B%E6%96%B0', new=2, autoraise=True)
if col3.button('骑行手册', use_container_width=True):
    webbrowser.open('https://ca-sysu.streamlit.app/%E2%80%8D%E5%9F%BA%E7%A1%80%E9%AA%91%E8%A1%8C%E6%89%8B%E5%86%8C', new=2, autoraise=True)
