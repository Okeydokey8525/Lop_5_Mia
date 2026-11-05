"""Small constructors for unit-owned learning data, not quiz scoring."""


def word(group,name,meaning,example,**extra):
    return dict(id=name.lower().replace(' ','-'),word=name,group=group,meaning=meaning,example=example,**extra)


def question(id,group,prompt,answer,hint,**extra):
    return dict(id=id,group=group,title='Try and remember.',prompt=prompt,answer=answer,hint=hint,
                kind='text',instruction='Điền từ hoặc cụm từ còn thiếu.',**extra)


def choice(id,group,prompt,answer,hint,options,**extra):
    q=question(id,group,prompt,answer,hint)
    q.update(kind='choice',instruction='Chọn đáp án đúng.',options=options,**extra)
    return q


def dialogue(group,title,a,b,meaning):
    return dict(group=group,title=title,a=a,b=b,meaning=meaning)
