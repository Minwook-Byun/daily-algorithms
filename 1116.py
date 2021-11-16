# n = int(input())
# print(n)
# arr  = [] 

# for w in input().split():
#     t  = int(w)
#     arr.append(t)
    
# s = [str(w) for w in arr]
# s.reverse()
# output = ' '.join(s)
# print(output)

# #반복 알고리즘 설계하기 
# #아무리 어려운 알고리즘도 쪼개어 보면 이 패턴으로 만들 수 있다

# for i in range(n):
#     # 0 ~ n-1에 대해서 
#     do_something(i)
    
#     # A[0] ~ A[n-1]에 대해서 
#     do_something(A[i])
    
    
# for i in range(0, n, 2):
#     print(i) # n 보다 작은 짝수 
    
# for (int i = 0 ;  i < n ; i++){
#     # 이부분은 모든 i에 대해서 수행 
#      if(조건s){
#         #  i의 의미가 축소된다. 조건을 만족한 i에 대해서만 수행 
#     }
    
#     # 모든 i에 대해서 수행  
# }
   
#두 수중에 더 큰 값을 반환하는 함수
def get_max(a, b):
	# return max(a, b)
    if(a > b):
        answer = a
    else:
        answer = b
    return answer
     
if __name__ == '__main__':
	a, b = [ int(w) for w in input().split() ]
	answer = get_max(a, b)
	print(answer)
 
# max로도 구현 가능하지만 조건문을 활용해서도 구현해봤음! 

#문제 1B - 원소의 합 구하기 
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 정수가 N개 주어진다. 이 N개의 정수의 합을 출력하는 프로그램을 작성하시오.

# 입력 형식
# 첫 줄에 입력되는 데이터의 수 N이 공백없이 입력된다. N은 1이상 1,000이하의 자연수이다.

# 두 번째 줄에는 공백으로 구분된 N개의 정수가 주어진다. 모든 숫자와 그 숫자들의 합은 항상 32비트 정수형으로 표현가능하다.

# 출력 형식
# 첫 줄에 입력된 N개의 숫자의 합을 공백없이 출력한다.

# def get_sum(data, n):
# 	# answer = 0
# 	# for num in data:
#     #      answer += num
# 	# return answer
#     answer = 0 
#     for i in range(n): #parameter로 n을 받았기 때문에 이렇게 2가지 방식으로  
#         answer += data[i] #data[i] data[0] ~ data[i-1]까지의 원소가 한 번씩 차례로 
#     return answer
        
# if __name__ == '__main__':
# 	n = int(input())
# 	data = [ int(w) for w in input().split() ]
# 	answer = get_sum(data, n)
# 	print(answer)

#문제1C-배열의 최대값
#배열(data)의 원소 중 가장 큰 정수를 반환하는 함수를 작성해보자
def get_max(data, n):
    for i in range(1, n):
        answer = data[0]
        if(data[i] > data[i-1]):
            answer = data[i]
        else:
            answer = data[i-1]
    return answer

n = int(input())
data = map(int, input().split())
answer = get_max(data, n)
print(answer)

#'map' object is not subscriptable