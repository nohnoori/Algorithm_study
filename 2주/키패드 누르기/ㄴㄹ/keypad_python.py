def solution(numbers, hand):
    answer = ''
    loc=[10,12]

    for num in numbers:
        if str(num) in '147':
            answer+='L'
            loc[0]=num
        elif str(num) in '369':
            answer+='R'
            loc[1]=num
        else:
            if num==0:
                num=11
            al,bl=divmod(abs(num-loc[0]),3)
            ar,br=divmod(abs(num-loc[1]),3)

            if al+bl==ar+br:
                if hand=='right':
                    answer+='R'
                    loc[1]=num
                else:
                    answer+='L'
                    loc[0]=num
            elif al+bl<ar+br:
                answer+='L'
                loc[0]=num
            else:
                answer+='R'
                loc[1]=num

    return answer
