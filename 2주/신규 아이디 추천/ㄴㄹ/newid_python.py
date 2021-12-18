def solution(new_id):
    answer=''
    new_id=new_id.lower()
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
    new_id=answer
    while '..' in new_id:
        new_id=new_id.replace('..','.')

    for i in range(2):
        if len(new_id)>0 and new_id[0]=='.':
            new_id=new_id[1:]
        if len(new_id)>0 and new_id[-1]=='.':
            new_id=new_id[:-1]

        if len(new_id)==0:
            new_id='a'

        if len(new_id)>15:
            new_id=new_id[:15]
        elif len(new_id)<3:
            new_id+=new_id[-1]*(3-len(new_id))

    return new_id
