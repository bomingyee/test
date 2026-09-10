file=open("test.txt","w",encoding="utf-8")
file.write("안녕하세요")
file.close()

with open("test.txt","w",encoding="utf-8") as file:
	file.write("안녕하세요")
# open()은 파일을 여는 함수.
# "test.txt"는 파일 이름.
# "w"는 쓰기 모드.
# encoding="utf-8"은 한글이 깨지지 않도록 설정.
# with를 사용하면 파일을 자동으로 닫아줍니다.

# 파일 모드
# "w": 쓰기; 기존 내용이 있으면 덮어씀
# "r": 읽기; 파일이 없으면 오류 발생
# "a": 추가; 기존 내용 뒤에 추가
# "x": 새 파일 생성; 파일이 이미 있으면 오류 발생

with open("test.txt","w",encoding="utf-8") as file:
	file.write("1일차 학습\n")
	file.write("2일차 학습\n")
	file.write("3일차 학습\n")

with open("test.txt","r",encoding="utf-8") as file:
	content=file.read()

print(content)

# 한 줄씩 읽기
with open("test.txt","r",encoding="utf-8") as file:
	line1=file.readline()
	line2=file.readline()

print(line1)
print(line2)

# 여러 줄 읽기
with open("test.txt","r",encoding="utf-8") as file:
	lines=file.readlines()

print(lines)

# 문자열 메서드와 연결
for line in lines:
	print(line.strip()) # strip(): 공백제거