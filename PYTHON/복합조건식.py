#연도가 4로 나누어 떨어지면 윤년이다.
#100으로 나누어 떨어지는 연도는 제외한다.
#400으로 나누어 떨어지는 연도는 윤년이다.

year = int(input("연도를 입력하시오: "))

if ( (year % 4 ==0 and year % 100 != 0) or year % 400 == 0) :
    print(year, "년은 윤년 입니다.")
else :
    print(year, "년은 평년 입니다.")