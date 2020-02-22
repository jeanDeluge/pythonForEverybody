#문자열을 저장하는 아래 파이썬 코드에서 find와 문자열 슬라이스를 사용해서 콜론 이후의 문자열을 가져온 다음, 
#float 함수를 써서 실수로 변환시켜보자.

str = 'X=DSPAM-Confidence:0.8475'

char = str.find(':')
last =str.find("5",char)
answer = float(str[char+1:last+1])

print(answer)