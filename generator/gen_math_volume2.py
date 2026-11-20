import json
from pathlib import Path
from cfg import CDS
from math_volume2.content import generate, LESSONS7, LESSONS8
from math_volume2.topics910 import questions9, questions10, LESSONS9, LESSONS10
from g4lib import write


def wrappers():
    root = Path(__file__).parent / 'common'
    for num, lessons in [(7, LESSONS7), (8, LESSONS8), (9, LESSONS9), (10, LESSONS10)]:
        cd = next(cd for cd in CDS if cd['n'] == num)
        data = dict(decimal=True, meta=dict(book='Toán 5 · Tập hai · Kết nối tri thức với cuộc sống',
            title=f'Kiểm tra Chủ đề {num}', topic=cd['name'], range=cd['range'], minutes=40,
            tip='Đọc đúng đơn vị và thứ tự tỉ số. Ô có kí hiệu % bên cạnh: chỉ nhập số. Có thể nhập dấu phẩy hoặc dấu chấm thập phân. Phân số: nhập dạng tối giản.' if num == 7 else
                'Đếm khối theo cột hoặc theo lớp. Đổi về cùng đơn vị trước khi tính: mỗi bậc thể tích hơn kém 1 000 lần. Có thể nhập dấu phẩy hoặc dấu chấm thập phân.' if num==8 else
                'Đọc đúng các mặt cần tính. Hộp không nắp chỉ có một đáy; đổi cùng đơn vị trước khi tính diện tích hoặc thể tích. Có thể nhập dấu phẩy hoặc dấu chấm thập phân.' if num==9 else
                'Đổi phút và giờ đúng hệ 60. Khi điền giờ–phút hoặc phút–giây, phần phút/giây phải nhỏ hơn 60. Chỉ tính thời gian đang chạy khi đề yêu cầu vận tốc lúc chạy; có thể gõ dấu phẩy hoặc dấu chấm.'),
            lessons={k: v[0] for k,v in lessons.items()}, levels=[
                dict(id='tb',name='Mức 1 · Trung bình',desc='Nhận biết và tính một bước',stars=1,pts=3),
                dict(id='kha',name='Mức 2 · Khá',desc='Đổi đơn vị và vận dụng hai bước',stars=2,pts=5),
                dict(id='gioi',name='Mức 3 · Giỏi',desc='Phối hợp nhiều bước trong chương trình',stars=3,pts=5)])
        text = json.dumps(data,ensure_ascii=False)[:-1]+',"questions":questions}'
        (root/f'cd{num}.js').write_text(f'window.MK{num}=function(questions){{return {text};}};\n',encoding='utf-8',newline='\n')

if __name__ == '__main__':
    wrappers()
    generate()
    for cd,builder in [(9,questions9),(10,questions10)]:
        for i in range(1,7):write(i,builder(i),cd=cd)
