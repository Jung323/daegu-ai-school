def calculator(var1,var2,str1):
    if str1=="+":
        결과=var1+var2
    elif str1=="-":
        결과=var1-var2
    elif str1=="*":
        결과=var1*var2
    elif str1=="/":
        결과=var1/var2
    else:
        결과="연산기호오류"
    return 결과

var1=int(input("첫번째 숫자: "))
str1=input("연산기호: ")
var2=int(input("두번째 숫자: "))
print(calculator(var1,var2,str1))