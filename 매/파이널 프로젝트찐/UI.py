from flag import japan_flag
def country_favorite(rank):
    country = {
        1: "대한민국", 2: "스위스", 3: "독일", 4: "콜롬비아",
        5: "베트남", 6: "일본", 7: "파키스탄", 8: "싱가포르",
        9: "칠레", 10: "스코틀랜드", 11: "행복의 준혁나라"
    }

    if rank in country:
        print("해당 순위의 국가는 %s입니다." % country[rank])
        if rank == 6:
            japan_flag()
        
        
        
    else:
        print("1부터 11 사이의 순위를 입력하세요.")

while True:
    country = input("궁금한 랭크를 말해보세요 (f를 누르면 종료): ")

    if country.lower() == "f":
        print("프로그램을 종료합니다.")
        break

    if country.isdigit():
        rank = int(country)
        if 1 <= rank <= 11:
            country_favorite(rank)
        else:
            print("1부터 11 사이의 숫자를 입력하세요.")
    else:
        print("1부터 11 사이의 숫자 또는 'f'를 입력하세요.")