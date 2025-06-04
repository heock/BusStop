from flag import korea_flag,swiss_flag,germany_flag, columbia_flag, vietnam_flag,china_flag,paki_flag,singa_flag,chill_flag,scott_flag,zun_flag
def country_favorite(rank):
    country = {
        1: "대한민국", 2: "스위스", 3: "독일", 4: "콜롬비아",
        5: "베트남", 6: "중국", 7: "파키스탄", 8: "싱가포르",
        9: "칠레", 10: "스코틀랜드", 11: "행복의 준혁나라"
    }

    if rank in country:
        print("해당 순위의 국가는 %s입니다." % country[rank])
        if rank == 1:
            korea_flag()
        elif rank == 2:
            swiss_flag()
        elif rank == 3:
            germany_flag()
        elif rank == 4:
            columbia_flag()
        elif rank == 5:
            vietnam_flag()
        elif rank == 6:
            china_flag()
        elif rank == 7:
            paki_flag()
        elif rank == 8:
            singa_flag()
        elif rank == 9:
            chill_flag()
        elif rank == 10:
            scott_flag()
        else :
            zun_flag()
        
        
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
