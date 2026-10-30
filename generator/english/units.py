"""Published English units: one registry for pages, catalog and progress IDs."""
from english.u01.content import TESTS

UNITS=[
 dict(n=1,key='u01',dir='Unit1_AllAboutMe',name='All about me!',pages='10–15',version=2),
 dict(n=2,key='u02',dir='Unit2_OurHomes',name='Our homes',pages='16–21',version=1),
 dict(n=3,key='u03',dir='Unit3_MyForeignFriends',name='My foreign friends',pages='22–27',version=1),
]


def test_id(unit,index):
    return f"en-{unit['key']}-de{index}-v{unit['version']}"


def tests_for(unit):
    descriptions={
      2:['Làm quen loại nhà, địa chỉ và cách nói nơi ở.','Nhận biết nhà ở qua tranh, từ chỉ khoảng cách và số nhà.','Hỏi đáp về nhà ở, địa chỉ và gần/xa trường.','Đọc các hồ sơ nhà ở tự soạn và đối chiếu địa chỉ.','Viết câu về loại nhà, địa chỉ và khoảng cách theo thẻ.','Kết hợp nghe, từ vựng, đọc và viết trong Unit 2.'],
      3:['Làm quen quốc tịch và tính cách của bạn bè.','Nhận biết tính cách qua hành động; ghép quốc gia và quốc tịch.','Hỏi đáp về quốc tịch, quê quán và tính cách.','Đọc hồ sơ bạn bè, phân biệt quốc tịch và tính cách.','Viết câu giới thiệu bạn từ thẻ thông tin.','Kết hợp nghe, từ vựng, đọc và viết trong Unit 3.'],
    }
    return [(slug,name,descriptions[unit['n']][i]) for i,(slug,name,_) in enumerate(TESTS)] if unit['n'] in descriptions else TESTS


def catalog():
    return [dict(file=f"TiengAnh5/{u['dir']}/De{i}_{slug}.html",id=test_id(u,i),subject='en')
            for u in UNITS for i,(slug,*_) in enumerate(TESTS,1)]


def index_data():
    return [dict(n=u['n'],dir=u['dir'],name=u['name'],range=f"Unit {u['n']} · Trang {u['pages']}",overview=f"TongQuan_Unit{u['n']}",
                 tests=[dict(id=test_id(u,i),file=f'De{i}_{slug}.html',name=name,theme=theme) for i,(slug,name,theme) in enumerate(tests_for(u),1)]) for u in UNITS]
