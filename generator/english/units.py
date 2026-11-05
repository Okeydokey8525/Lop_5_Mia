"""Published English units: one registry for pages, catalog and progress IDs."""
from english.u01.content import TESTS

UNITS=[
 dict(n=1,key='u01',dir='Unit1_AllAboutMe',name='All about me!',pages='10–15',version=2),
 dict(n=2,key='u02',dir='Unit2_OurHomes',name='Our homes',pages='16–21',version=1),
 dict(n=3,key='u03',dir='Unit3_MyForeignFriends',name='My foreign friends',pages='22–27',version=1),
 dict(n=4,key='u04',dir='Unit4_OurFreeTimeActivities',name='Our free-time activities',pages='28–33',version=1),
 dict(n=5,key='u05',dir='Unit5_MyFutureJob',name='My future job',pages='34–39',version=1),
 dict(n=6,key='u06',dir='Unit6_OurSchoolRooms',name='Our school rooms',pages='44–49',version=1),
 dict(n=7,key='u07',dir='Unit7_OurFavouriteSchoolActivities',name='Our favourite school activities',pages='50–55',version=1),
 dict(n=8,key='u08',dir='Unit8_InOurClassroom',name='In our classroom',pages='56–61',version=1),
 dict(n=9,key='u09',dir='Unit9_OurOutdoorActivities',name='Our outdoor activities',pages='62–67',version=1),
 dict(n=10,key='u10',dir='Unit10_OurSchoolTrip',name='Our school trip',pages='68–73',version=1),
]

REVIEWS=[dict(n='R1',key='r01',dir='Review1_Units1_5',name='Review 1 · Ôn Unit 1–5',label='Review 1',pages='40–43',version=1,kind='review',overview='TongQuan_Review1'),
         dict(n='R2',key='r02',dir='Review2_Units6_10',name='Review 2 · Ôn Unit 6–10',label='Review 2',pages='74–77',version=1,kind='review',overview='TongQuan_Review2')]
TOPICS=UNITS[:5]+[REVIEWS[0]]+UNITS[5:]+[REVIEWS[1]]


def label(unit):return unit.get('label',f"Unit {unit['n']}")
def overview_name(unit):return unit.get('overview',f"TongQuan_Unit{unit['n']}")

DETAILS={
 'R1':dict(topic='Ôn tổng hợp Units 1–5',lessons={1:'Bản thân, nhà ở và bạn bè',2:'Sở thích và nghề nghiệp',3:'Đọc và viết tổng hợp'},colour='#A63C70',bg='#FFE4F0'),
 'R2':dict(topic='Ôn tổng hợp Units 6–10',lessons={1:'Trường lớp và sở thích',2:'Đồ dùng và chuyến đi',3:'Đọc và viết tổng hợp'},colour='#A33876',bg='#FFE5F2'),
 10:dict(topic='Chuyến đi của trường, địa điểm, hoạt động và thời gian',lessons={1:'Đã đi đến đâu?',2:'Đã làm gì?',3:'Tháng, đọc và viết'},colour='#A83A71',bg='#FFE5F0'),
 8:dict(topic='Vị trí và chủ sở hữu đồ dùng trong lớp',lessons={1:'Vị trí đồ dùng',2:'Đồ dùng của ai?',3:'Đọc góc học tập và viết'},colour='#A33372',bg='#FFE3F2'),
 9:dict(topic='Địa điểm đã đến và hoạt động đã làm',lessons={1:'Địa điểm trong quá khứ',2:'Hoạt động đã làm',3:'Đọc và kể chuyến đi'},colour='#AC3A68',bg='#FFE6EF'),
 6:dict(topic='Phòng học, tầng và chỉ đường trong trường',lessons={1:'Phòng học và tầng',2:'Hỏi và chỉ đường',3:'Đọc sơ đồ và viết'},colour='#A53E78',bg='#FFE6F2'),
 7:dict(topic='Hoạt động yêu thích ở trường và lý do',lessons={1:'Hoạt động ở trường',2:'Hỏi và nói lý do',3:'Đọc hồ sơ và viết'},colour='#AC3F68',bg='#FFE8F0'),
 2:dict(topic='Nhà ở và địa chỉ',lessons={1:'Loại nhà',2:'Địa chỉ và khoảng cách',3:'Đọc và viết'},colour='#AD4278',bg='#FFE3F1'),
 3:dict(topic='Quốc tịch và tính cách của bạn bè',lessons={1:'Quốc gia và quốc tịch',2:'Tính cách',3:'Đọc và viết'},colour='#AF4771',bg='#FFE8F1'),
 4:dict(topic='Sở thích lúc rảnh và hoạt động cuối tuần',lessons={1:'Hoạt động lúc rảnh',2:'Cuối tuần và tần suất',3:'Đọc và viết'},colour='#A13D79',bg='#FFE5F4'),
 5:dict(topic='Nghề nghiệp tương lai và lý do lựa chọn',lessons={1:'Nghề nghiệp tương lai',2:'Lý do lựa chọn',3:'Đọc và viết'},colour='#B03D70',bg='#FFE4EE'),
}


def test_id(unit,index):
    return f"en-{unit['key']}-de{index}-v{unit['version']}"


def tests_for(unit):
    descriptions={
      'R1':['Ôn bản thân, nhà ở, bạn bè, sở thích và nghề nghiệp.','Phân biệt từ vựng qua tranh và ngữ cảnh các Unit 1–5.','Ghép đúng loại câu hỏi và câu trả lời theo hồ sơ.','Đọc hồ sơ mới kết hợp địa chỉ, quốc tịch, sở thích và ước mơ.','Viết câu về nhiều thông tin từ cùng hồ sơ giả định.','Kết hợp nghe, đọc và viết trong phạm vi Review 1.'],
      'R2':['Ôn trường lớp, sở thích, đồ dùng và những chuyến đi.','Nhận biết từ vựng và các dạng động từ trong Unit 6–10.','Hỏi đáp vị trí, chủ sở hữu và các chuyến đi đã qua.','Đọc hồ sơ mới, phân biệt yesterday với school trip.','Viết câu vị trí, sở thích, sở hữu và chuyến đi theo thẻ.','Kết hợp nghe, đọc và viết trong phạm vi Review 2.'],
      10:['Làm quen địa điểm, hoạt động và thời gian chuyến đi.','Nhận biết hoạt động qua tranh và các dạng quá khứ.','Hỏi Did they go…?/What did they do…? theo thẻ.','Đọc chuyến đi, phân biệt cùng nơi nhưng khác tháng hoặc hoạt động.','Viết với did/go/went và động từ quá khứ theo thẻ.','Kết hợp nghe, nơi, tháng, hoạt động, đọc và viết.'],
      8:['Làm quen đồ dùng, vị trí và chủ sở hữu.','Nhận biết đồ dùng qua tranh, số ít/số nhiều và giới từ.','Hỏi Where/Whose, đáp vị trí và chủ sở hữu.','Đọc góc học tập, khớp đồ vật, người sở hữu và vị trí.','Viết câu vị trí và sở hữu theo thẻ dữ kiện.','Kết hợp nghe, từ vựng, vị trí, sở hữu, đọc và viết.'],
      9:['Làm quen địa điểm và hoạt động đã qua.','Nhận biết địa điểm, động từ quá khứ và thời gian.','Hỏi Were you…?/What did you do…? và đáp theo thẻ.','Đọc chuyến đi, phân biệt địa điểm giống nhưng hoạt động khác.','Viết với was/were và động từ quá khứ theo thẻ.','Kết hợp nghe, nơi chốn, thời gian, hoạt động, đọc và viết.'],
      6:['Làm quen tên phòng học và cách gọi tầng.','Nhận biết phòng qua đồ dùng; từ chỉ tầng và hướng đi.','Hỏi vị trí và hỏi đường lịch sự trong trường.','Đọc kế hoạch phòng học và đối chiếu tầng, hướng đi.','Viết câu xác định vị trí và sắp xếp chỉ dẫn.','Kết hợp nghe, tên phòng, tầng, hội thoại và chỉ đường.'],
      7:['Làm quen hoạt động yêu thích ở trường.','Nhận biết hoạt động qua tranh và các từ nêu lý do.','Hỏi sở thích với does và trả lời lý do với Because.','Đọc hồ sơ, phân biệt hoạt động giống nhau nhưng lý do khác nhau.','Viết câu likes + V-ing và because theo hồ sơ.','Kết hợp nghe, hoạt động, lý do, đọc hiểu và viết câu.'],
      2:['Làm quen loại nhà, địa chỉ và cách nói nơi ở.','Nhận biết nhà ở qua tranh, từ chỉ khoảng cách và số nhà.','Hỏi đáp về nhà ở, địa chỉ và gần/xa trường.','Đọc các hồ sơ nhà ở tự soạn và đối chiếu địa chỉ.','Viết câu về loại nhà, địa chỉ và khoảng cách theo thẻ.','Kết hợp nghe, từ vựng, đọc và viết trong Unit 2.'],
      3:['Làm quen quốc tịch và tính cách của bạn bè.','Nhận biết tính cách qua hành động; ghép quốc gia và quốc tịch.','Hỏi đáp về quốc tịch, quê quán và tính cách.','Đọc hồ sơ bạn bè, phân biệt quốc tịch và tính cách.','Viết câu giới thiệu bạn từ thẻ thông tin.','Kết hợp nghe, từ vựng, đọc và viết trong Unit 3.'],
      4:['Làm quen hoạt động lúc rảnh và từ chỉ tần suất.','Nhận biết hoạt động qua tranh, ghép cụm từ và nghĩa.','Hỏi đáp về sở thích và hoạt động cuối tuần.','Đọc lịch sinh hoạt, đối chiếu hoạt động và tần suất.','Viết câu với like + V-ing và thói quen cuối tuần.','Kết hợp nghe, từ vựng, đọc và viết trong Unit 4.'],
      5:['Làm quen tên nghề và mẫu câu nói ước mơ.','Nhận biết nghề qua tranh, ghép nghề với việc làm.','Hỏi đáp về nghề nghiệp tương lai và lý do.','Đọc hồ sơ ước mơ, tìm nghề và lý do lựa chọn.','Viết câu với would like to be và Because.','Kết hợp nghe, từ vựng, đọc và viết trong Unit 5.'],
    }
    return [(slug,name,descriptions[unit['n']][i]) for i,(slug,name,_) in enumerate(TESTS)] if unit['n'] in descriptions else TESTS


def catalog():
    return [dict(file=f"TiengAnh5/{u['dir']}/De{i}_{slug}.html",id=test_id(u,i),subject='en',kind=u.get('kind','unit'),topic=u['key'],
                 overview=f"TiengAnh5/{u['dir']}/{overview_name(u)}.html") for u in TOPICS for i,(slug,*_) in enumerate(TESTS,1)]


def index_data():
    return [dict(n=u['n'],badgeLabel='Review' if u.get('kind')=='review' else 'Unit',badge=str(u['n'])[1:] if u.get('kind')=='review' else str(u['n']),dir=u['dir'],name=u['name'],range=f"{label(u)} · Trang {u['pages']}",overview=overview_name(u),
                 tests=[dict(id=test_id(u,i),file=f'De{i}_{slug}.html',name=name,theme=theme) for i,(slug,name,theme) in enumerate(tests_for(u),1)]) for u in TOPICS]
