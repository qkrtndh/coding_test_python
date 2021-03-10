"""
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다.
이때 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에
모든 숫자를 더한 값을 이어서 출력한다."""

#아이디어
"""입력된 값을 하나씩 읽어서 문자열은 따로 하나씩 list에 저장하고
숫자는 변수에 각기 더하고, list.sort후 출력하면 되지 않을까?"""
"""
string = input()
result = 0
num=['0','1','2','3','4','5','6','7','8','9']
a = []
for i in string:
    if i in num:
        result+=int(ord(i)-ord('0'))
    else:
        a.append(i)
a.sort()
print(''.join(a)+str(result))
"""

#개선
string = input()
result = 0
a = []
#코드 간결화
for i in string:
    if i.isalpha():
        a.append(i)
    else:
        result+=int(i)
a.sort()

#0처리
if(result!=0):
    a.append(str(result))
print(''.join(a))