# 방법 1
# %d 사용 시 정수만 가능
print("나는 %d살입니다" % 23) # 나는 23살입니다
# %s 사용 시 문자열 가능
print("제 이름은 %s입니다" % "김대희") # 제 이름은 김대희입니다
# %c 사용 시 한 문자만 가능
print("Apple은 %c로 시작해요" % "A") # Apple은 A로 시작해요

# %s로 정수, 문자 모두 가능
print("나는 %s살입니다" % 23) # 나는 23살입니다
print("제 이름은 %s입니다" % "김대희") # 제 이름은 김대희입니다
print("Apple은 %s로 시작해요" % "A")# Apple은 A로 시작해요

# 콤마를 사용하여 두 개 이상의 값도 가능
print("나는 %s색과 %s색을 좋아합니다." % ("노랑", "파랑")) # 나는 노랑색과 파랑색을 좋아합니다.

# 방법 2
# {} 사용 후 .format() 안에 원하는 값 집어 넣기
print("나는 {}살 입니다.".format(23)) # 나는 23살 입니다.
print("나는 {}색과 {}색을 좋아합니다.".format("노랑","파랑")) # 나는 노랑색과 파랑색을 좋아합니다.

# 중괄호 속 숫자를 사용하여 값을 연속적이지 않게 대입할 수 있다.
print("나는 {0}색과 {1}색을 좋아합니다.".format("노랑","파랑")) # 나는 노랑색과 파랑색을 좋아합니다.
print("나는 {1}색과 {0}색을 좋아합니다.".format("노랑","파랑")) # 나는 파랑색과 노랑색을 좋아합니다.

# 방법 3
# 중괄호 속에 변수를 넣을 수 있다. 변수는 바로 다음에 선언됨
print("나는 {age}살이며, {color}색을 좋아합니다.".format(age = 23, color = "노랑"))

# 방법 4
# 미리 선언 된 변수를 f를 사용하여 사용할 수 있다.
age = 23
color = "노랑"
print(f"나는 {age}살이며, {color}색을 좋아합니다.") # 나는 23살이며, 노랑색을 좋아합니다.
# 변수가 미리 선언되더라도 f를 사용하지 않으면 .format을 사용하여 변수를 다시 선언해야 한다.
print("나는 {age}살이며, {color}색을 좋아합니다.".format(age =20, color = "빨간")) # 나는 20살이며, 빨간색을 좋아합니다.