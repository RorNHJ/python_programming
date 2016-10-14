
# coding: utf-8

# ### Assignment_2
# ### 2013136035 라현지

# ### 1. 다음 6 개의 Expression에 대해 Evaluation 결과 값을 출력하고, 해당 결과가 나온 이유에 대해 설명하시오
# > 1 and 2 and 3 and 4
# 
# > 1 or 2 or 3 or 4
# 
# > 1 and 2 or 3 and 4
# 
# > (1 and 2) or (3 and 4)
# 
# > 1 or 2 and 3 or 4
# 
# > (1 or 2) and (3 or 4)

# In[9]:

print 1 and 2 and 3 and 4
print 1 or 2 or 3 or 4
print 1 and 2 or 3 and 4
print (1 and 2) or (3 and 4)
print 1 or 2 and 3 or 4
print (1 or 2) and (3 or 4)


# ### 1번 문제 설명
# 0이 아닌 값이 있을 경우 true 또는 그 값을 반환하고 False, 0, '', "" 일 경우엔 false 또는 0을 반환한다.
# and는 양 쪽의 식이 true일 때 값을 반환하다. 앞에 값이 true이면 뒤의 값을 비교하고 뒤의 값도 true이면 뒤의 값을 반환한다. 
# 그래서 마지막 값이 4가 반환이 된다. 하지만 or은 앞에 값을 비교해서 만약 false 또는 true가 나온다면 뒤의 값을 비교할 필요 없이 false 또는 값을 반환한다. 굳이 뒤에 값까지 판단할 필요가 없기 때문이다. 
# 즉, and일 경우 앞에서부터 뒤에 값까지 모두 비교하고 마지막 값을 반환하고, or은 앞에 값만 보고 판단한다.

# ### 2. 경로에 해당하는 문자열 1개를 입력 받아 그 안에 디렉토리 경로명과 파일명을 분리하여 리스트로 반환하는 함수 div_path(s)를 작성하시오.
# > 인자로 전달하는 문자열은 경로만 들어간다고 가정한다.
# 
# > 각 디렉토리와 파일을 구분하는 문자는 '/'로 가정한다.
# 
# > 반환하는 리스트의 첫번째 원소는 디렉토리이고 두번째 원소는 파일명이다.
# 
# > 다음과 같은 실행 및 출력 결과가 도출되어야 한다.
# 
# > div_path('/usr/local/bin/python')
# 
# > ['/usr/local/bin', 'python']
# 
# > div_path('/home/chulsoo/test.txt')
# 
# > ['/home/chulsoo', 'test.txt']
# 
# > [참고] 리스트(l) 내에 새로운 정수값 (예를 들어 10)을 넣는 방법은 l.append(10) 이다.

# In[47]:

def div_path(s):
    list =  s.split('/')
    for i in range(0,len(list)):
        s = list[:i]
    s = '/'.join(s)
    v = list.pop(-1)
    result = [s,v]
    return result

print div_path('/home/chulsoo/test.txt')


# ### 2번 문제 설명
# 문제의 전제 조건에서 디렉토리와 파일의 구분은 오로지 '/' 이므로 마지막 / 뒤에 오는 문자열이 파일 이름이다. 물론 디렉토리 일 수 도 있지만 문제 전제 조건이 오로지 / 이므로 마지막 문자열이 파일이라고 판단해야한다. 
# 문자열을 함수로 넘겨서 split 함수를 사용해 '/' 단위로 문자를 슬라이싱하고 리스트로 정리한다. 그리고 마지막 원소가 파일이름이므로 
# 반복문을 사용하여 마지막 원소전까지의 원소끼리  join함수를 사용하여 다시 / 로 합쳐서 s에 저장한다.이 때 반환값은 string 이다. 
# 그리고 마지막 원소를 pop 함수를 사용하여 v에 저장한다. v에 저장된 자료형도 string이다.
# result 변수에 s와 v를 리스트 형식으로 저장하고 반환한다.

# ### 3. 두 개의 리스트를 인자로 받아서 그 두 개의 리스트에 대한 '합집합'을 반환하는 함수 list_union(lista, listb)를 작성하시오.
# 
# > 인자로 전달하는 리스트 2 개에는 정수값만 들어간다고 가정하자.
# 
# > 함수 내에서 새로운 리스트를 만들어 그 리스트 내에 인자로 받은 두 리스트의 모든 원소를 넣어 반환한다.
# 
# > 반환하는 리스트에는 절대로 중복된 원소가 들어 있으면 안된다 (집합의 조건).
# 
# > 반환하는 리스트는 정렬이 되어 있어야 한다.
# 
# > 다음과 같은 실행 및 출력 결과가 도출되어야 한다.
# 
# > list_union([1, 2, 3], [1, 2, 4])
# 
# > [1, 2, 3, 4]
# 
# > list_union([-10, -5, 0, -1], [100, 9, 0, 9])
# 
# > [-10, -5, -1, 0, 9, 100]
# 
# > list_union([0, 1, 2], [0, 1, 2])
# 
# > [0, 1, 2]
# 
# > [참고] 리스트(l) 내에 새로운 정수값 (예를 들어 10)을 넣는 방법은 l.append(10) 이다.
# 
# > [참고] 임의의 정수값 (x)이 리스트 (l) 내에 존재하는지 판단하는 방법은 x in l 이다.

# In[77]:

def list_union(lista, listb):
    temp = lista + listb
    temp2 = []
    

    for x in range(0,len(temp)-1):
        for y in range(x+1,len(temp)):
            if temp[x] == temp[y]:
                temp2.append(temp[y])
    
    for z in range(0,len(temp2)):
        temp.remove(temp2[z])
    temp.sort()
    
    return temp
        
print list_union([-10, -5, 0, -1], [100, 9, 0, 9])


# ### 문제설명
# 
# > 먼저 입력받은 두 리스트를 하나로 합쳐서 temp 라는 리스트를 만든다. 반복문을 이용해서 temp 리스트의 원소를 비교하면서 같은 값이 있으면 그 원소를 temp2라는 리스트에 따로 저장한다. 반복문이 끝나면 다시 temp2리스트의 크기 만큼 반복문으로 remove함수를 사용하여 중복된 값을 temp에서 지운다.그리고 sort 함수를 사용하여 정렬한다. 

# ### Problem 오일러 4 
# > 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.
# 
# > 두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.
#  
# > 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?

# In[5]:

max = 0
for x in range(100,1000):
    for y in range(100,1000):
        num = x*y
        st = str(num)
        if st[0:3] == st[:-4:-1] :
            max = num
else:
    print max


# ### 문제설명
# > 반복문을 사용하여 x와 y를 곱한 값을 num에 저장한다. 그리고  num을 string 값으로 변환 하여 st에 저장한다. 
# st의 0,1,2 자리의 원소값과 뒤에서부터 -1씩 차이나는 원소 -1,-2,-3 자리의 원소값을 비교했을 때 값은 대칭수이면 max에 저장한다.
# 반복문이 끝났을 때 max에 저장된 값이 가장 큰 수 이므로 이값을 출력한다. 

# ### Problem 5
# > 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
# 
# > 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?

# In[42]:

# 20까지의 수가 담긴 temp 리스트 생성
temp = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
temp_y = [] # 소인수 분해의 값들이 담긴 리스트
i = 0
mult = 1;


def func(check):
    for x in [2,3,5,7,11,13,17,19]: # 20까지의 수들 중에서 소수인 수들안에서 반복.
        for i,y in enumerate(temp):
            if y%x == 0 : 
                temp[i] = y/x
                check = 1 # 중복계산을 하지 않기 위한 방지.
        
        if check == 1 :
            temp_y.append(x) # 소인수 분해서 나온 값들을 append 한다.
            check = 0
    
    if temp.count(1) != len(temp): # 나온 몫들이 모두 1이면 종료하고 아니면 함수 한번더 호출
        func(0)
      
    
func(0) # 함수 호출... 


for z in temp_y:
    mult = mult * z # 나온 몫들의 값들을 모두 곱한다.
    
print mult
    


# ### 문제 설명
# > 이 문제는 주어진 범위의 최소공배수를 구하는 문제이다. 이때 1에서 20까지의 최소공배수를 구할 때 20까지의 소수를 이용해서 최소공배수를 구한다. 20까지의 소수는 [2,3,5,7,11,13,17,19] 가 있으며 소수를 계속 반복해서 20까지 몫이 1이 나올 때 까지 나눠주고 나눈 값들을 모두 곱하면 빠른 시간안에 최소 공배수를 구할 수 있다. 알고리즘 도출 식은 간단하게 10까지의 수로 예를 들어서 설명하면...
# 
# > x  :  y
# 
# > 2  :  1  2  3  4  5  6  7  8  9  10
# 
# > 3  :  1  1  3  2  5  3  7  4  9  5
# 
# > 5  :  1  1  1  2  5  1  7  4  3  5
# 
# > 7  :  1  1  1  2  1  1  7  4  3  1
# 
# > 2  :  1  1  1  2  1  1  1  4  3  1
# 
# > 3  :  1  1  1  1  1  1  1  2  3  1
# 
# > 2  :  1  1  1  1  1  1  1  2  1  1
# 
# > 1  :  1  1  1  1  1  1  1  1  1  1
#    
# > x의 값들을 모두 곱하면 최소공배수이다!

# ### Problem 6
# > 1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같습니다 (제곱의 합).
# 
# > 12 + 22 + ... + 102 = 385
# 
# > 1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다 (합의 제곱).
# 
# >(1 + 2 + ... + 10)2 = 552 = 3025
# 
# > 따라서 1부터 10까지 자연수에 대해 "합의 제곱"과 "제곱의 합" 의 차이는 3025 - 385 = 2640 이 됩니다.
# 
# >그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는 얼마입니까?
# 

# In[2]:

result = 0

for x in range(1,101):
    result = pow((x*(x+1)/2),2) - x*(x+1)*(2*x+1)/6

print result


# ### 문제설명
# > 제곱의 합 공식은 x*(x+1)*(2*x+1)/6 이고
# > 합의 제곱 공식은 (x*(x+1)/2)^2 이다
# > 이 공식을 사용하여 1부터 100 까지 반복문을 사용하면 답을 쉽게 구할 수 있다.

# ### Incremental Project
# 
# 웹 URL로 지정된 웹페이지를 문자열로 가져와
# 1) 모든 HTML 태그를 제외한 순수 텍스트 문자열만을 걸러내고, 
# 2) 그 순수 텍스트 문자열 안에 존재하는 단어가 총 몇개인지 출력하는 프로그램을 작성하시오.
# 
# HTML 태그는 다음 조건을 가지는 것이다.
# 
# > < 로 시작하여 >로 끝난다.
# 예를 들어, 아래와 같은 HTML 내용 내에 한 줄이 있다고 가정하자.
# <label for="keep_signed">로그인 유지</label>
# 위 소스에서 HTML 태그를 제외한 순수 텍스트 문자열은 아래와 같다.
# 로그인 유지
# 한편, 아래와 같은 HTML 한 줄이 있다고 가정하자.
# <link rel="stylesheet" href="/common/css/xe.min.css?20150910092654" />
# 위 소스는 HTML 태그로만 구성된 것이며 걸러낼 수 있는 순수 텍스 문자열은 존재하지 않는다.
# 단어를 나누는 기준은 오로지 공백문자 (whitespace)이다.
# 
# >즉, 위 순수 텍스트 문자열인 "로그인 유지"에서 분리한 단어는 "로그인"과 "유지"이다.
# 다음은 URL로 지정된 웹페이지를 특정 문자열로 가져오는 코드이다.
# 즉, 숙제 코드는 아래 코드로 부터 시작해야 한다.

# In[3]:

import urllib2
# source 변수에 페이지 소스를 읽어온다.
source = urllib2.urlopen("http://cse.kut.ac.kr/").read()
# 읽어온 페이지의 줄띄움, 탭, 빈 공간을 모두 없애주고 한줄로 깔끔하게 정리한다.
source = source.replace('\n','')
source =  source.replace('\t','')
source =  source.replace(' ','')



while 1:
    # <의 위치값
    start = source.find('<')
    # >의 위치값은 항상 <보다 커야한다. 그래야 html 태그라고 볼 수 있다.
    end = source.find('>',start)
    
    # html 태그가 아닌 순수한 문자열 중에서도 <와 >가 있을 수 있다. 그것을 구분하기 위한 코드이다.
    # html 태그라면 <의 위치값이 >의 위치값 보다 항상 낮다. 만약 크다면 순수한 문자열이라고 볼 수 있다.
    if (start-end) >= 1 :
        continue
    
    # html 태그가 맞다면 태그 부분을 빈 공간으로 대체한다.
    if ( start != -1) and (end != -1):
        source = source.replace(source[start:end+1],' ')
    
    # html 태그를 모두 찾고 더이상 없으면 반복문을 종료
    if ( start == -1) and (end == -1):
        break
print source


# ### 문제설명
# > html 태그라고 판단하는 기준은 <와 >로 둘러싸여있을 경우로 판단하였다. 
# > 하지만 html태그가 아님에도 순수한 문자열일 수도 있는 <와 >를 구분하기 위해서 <의 위치값이 > 보다 클 경우 순수한 문자열이라고 판단한다.
# > html 태그를 빈공간으로 replace 시켜서 순수한 문자열만 남게 끔 하였다. 
# 

# # 소감
# 
# ### 이번 기회를 통해서 파이썬 문법 중 헷갈렸던 부분들을 바로 잡을 수 있었습니다.

# In[ ]:



