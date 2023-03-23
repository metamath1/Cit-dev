#####################################################################
# 실습문제10: 급여계산하기 02.숫자데이터 데이터 13번 슬라이드
# lab 10
# 시급, 일일근무시간, 한달동안 일한 날수, 보너스 입력받아서 이번달 급여

time_salary = int(input("시급: "))
workingtime_per_day = int(input("근무시간: "))
workday = int(input("근무날: "))
bonus = int(input("보너스: "))

print(time_salary * workingtime_per_day * workday + bonus)
#####################################################################