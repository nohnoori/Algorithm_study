def solution(str1, str2):
		#각 문자열을 두 글자씩 쌍으로 묶고 특수부호 등이 포함된 경우는 제외하여 배열에 넣기
    arr1=[str1.lower()[i:i+2] for i in range(len(str1)-1) if str1.lower()[i:i+2].isalpha()]
    arr2=[str2.lower()[i:i+2] for i in range(len(str2)-1) if str2.lower()[i:i+2].isalpha()]
    cnt=0
    noset=[]    #중복되어 교집합 처리가 되는 경우를 없애기 위해 인덱스를 넣어두는 배열
    
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]==arr2[j] and j not in noset:
                cnt+=1
                noset.append(j)
                break   #같은 거 하나 찾으면 제외

		#if문에서 and를 했는데 오류가 나서 or로 바꿨더니 정답처리
		#분명 문제에는 모두 공집합일 경우에 1이라 한댔는데 의문
    return int(cnt/(len(arr1)+len(arr2)-cnt)*65536) if cnt!=0 or len(arr1)+len(arr2)-cnt!=0 else 65536
