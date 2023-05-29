import os
import random

# with open("889 상도.csv", 'w') as f:
#     f.write('2')
# with open("The Kone.csv", 'w') as f:
#     f.write('2')
# with open("고렝.csv", 'w') as f:
#     f.write('2')
# with open("긴자료코 숭실대입구역점.csv", 'w') as f:
#     f.write('2')
# with open("내가찜한닭 숭실대점.csv", 'w') as f:
#     f.write('2')
# with open("밀플랜비 숭실대점.csv", 'w') as f:
#     f.write('2')
# with open("백채김치찌개 숭실대점.csv", 'w') as f:
#     f.write('2')
# with open("베트남식당 퍼민.csv", 'w') as f:
#     f.write('2')
# with open("샤로스톤.csv", 'w') as f:
#     f.write('2')
# with open("손칼국수.csv", 'w') as f:
#     f.write('2')
# with open("스톤 504 스테이크하우스.csv", 'w') as f:
#     f.write('2')
# with open("쑝쑝돈까스 숭실대점.csv", 'w') as f:
#     f.write('2')
# with open("은화수식당 숭실대점.csv", 'w') as f:
#     f.write('2')
# with open("지지고 숭실대점.csv", 'w') as f:
#     f.write('2')
# with open("청년다방.csv", 'w') as f:
#     f.write('2')
# with open("크라이치즈버거 숭실대점.csv", 'w') as f:
#     f.write('2')
# with open("현선이네 숭실점.csv", 'w') as f:
#     f.write('2')
식당 = [
    "889 상도",
    "The Kone",
    "고렝",
    "긴자료코 숭실대입구역점",
    "내가찜한닭 숭실대점",
    "밀플랜비 숭실대점",
    "백채김치찌개 숭실대점",
    "베트남식당 퍼민",
    "샤로스톤",
    "손칼국수",
    "스톤 504 스테이크하우스",
    "쑝쑝돈까스 숭실대점",
    "은화수식당 숭실대점",
    "지지고 숭실대점",
    "청년다방",
    "크라이치즈버거 숭실대점",
    "현선이네 숭실점",
]

태그 = {
    "889 상도": "육류, 고기요리",
    "The Kone": "종합분식",
    "고렝": "아시아 음식",
    "긴자료코 숭실대입구역점": "돈가스",
    "내가찜한닭 숭실대점": "찜닭",
    "밀플랜비 숭실대점": "핫도그",
    "백채김치찌개 숭실대점": "찌개, 전골",
    "베트남식당 퍼민": "베트남 음식",
    "샤로스톤": "스테이크, 립",
    "손칼국수": "칼국수, 만두",
    "스톤 504 스테이크하우스": "스테이크, 립",
    "쑝쑝돈까스 숭실대점": "돈가스",
    "은화수식당 숭실대점": "돈가스",
    "지지고 숭실대점": "도시락, 컵밥",
    "청년다방": "분식",
    "크라이치즈버거 숭실대점": "햄버거",
    "현선이네 숭실점": "떡볶이",
}

favorite = []

d_889_상도 = {"음식점": "889 상도"}
d_The_Kone = {"음식점": "The Kone"}
d_고렝 = {"음식점": "고렝"}
d_긴자료코_숭실대입구역점 = {"음식점": "긴자료코 숭실대입구역점"}
d_내가찜한닭_숭실대점 = {"음식점": "내가찜한닭 숭실대점"}
d_밀플랜비_숭실대점 = {"음식점": "밀플랜비 숭실대점"}
d_백채김치찌개_숭실대점 = {"음식점": "백채김치찌개 숭실대점"}
d_베트남식당_퍼민 = {"음식점": "베트남식당 퍼민"}
d_샤로스톤 = {"음식점": "샤로스톤"}
d_손칼국수 = {"음식점": "손칼국수"}
d_스톤_504_스테이크하우스 = {"음식점": "스톤 504 스테이크하우스"}
d_쑝쑝돈까스_숭실대점 = {"음식점": "쑝쑝돈까스 숭실대점"}
d_은화수식당_숭실대점 = {"음식점": "은화수식당 숭실대점"}
d_지지고_숭실대점 = {"음식점": "지지고 숭실대점"}
d_청년다방 = {"음식점": "청년다방"}
d_크라이치즈버거_숭실대점 = {"음식점": "크라이치즈버거 숭실대점"}
d_현선이네_숭실점 = {"음식점": "현선이네 숭실점"}

with open("./data/889 상도.csv", "rt", encoding="UTF8") as f:
    while True:
        line = f.readline().strip()
        if line == "":
            break
        k, v = line.split("-")
        d_889_상도[k] = v
with open("./data/The Kone.csv", "rt", encoding="UTF8") as f:
    while True:
        line = f.readline().strip()
        if line == "":
            break
        k, v = line.split("-")
        d_The_Kone[k] = v
with open("./data/고렝.csv", "rt", encoding="UTF8") as f:
    while True:
        line = f.readline().strip()
        if line == "":
            break
        k, v = line.split("-")
        d_고렝[k] = v
with open("./data/긴자료코 숭실대입구역점.csv", "rt", encoding="UTF8") as f:
    while True:
        line = f.readline().strip()
        if line == "":
            break
        k, v = line.split("-")
        d_긴자료코_숭실대입구역점[k] = v
with open("./data/내가찜한닭 숭실대점.csv", "rt", encoding="UTF8") as f:
    while True:
        line = f.readline().strip()
        if line == "":
            break
        k, v = line.split("-")
        d_내가찜한닭_숭실대점[k] = v
with open("./data/밀플랜비 숭실대점.csv", "rt", encoding="UTF8") as f:
    while True:
        line = f.readline().strip()
        if line == "":
            break
        k, v = line.split("-")
        d_밀플랜비_숭실대점[k] = v
with open("./data/백채김치찌개 숭실대점.csv", "rt", encoding="UTF8") as f:
    while True:
        line = f.readline().strip()
        if line == "":
            break
        k, v = line.split("-")
        d_백채김치찌개_숭실대점[k] = v
with open("./data/베트남식당 퍼민.csv", "rt", encoding="UTF8") as f:
    while True:
        line = f.readline().strip()
        if line == "":
            break
        k, v = line.split("-")
        d_베트남식당_퍼민[k] = v
with open("./data/샤로스톤.csv", "rt", encoding="UTF8") as f:
    while True:
        line = f.readline().strip()
        if line == "":
            break
        k, v = line.split("-")
        d_샤로스톤[k] = v
with open("./data/손칼국수.csv", "rt", encoding="UTF8") as f:
    while True:
        line = f.readline().strip()
        if line == "":
            break
        k, v = line.split("-")
        d_손칼국수[k] = v
with open("./data/스톤 504 스테이크하우스.csv", "rt", encoding="UTF8") as f:
    while True:
        line = f.readline().strip()
        if line == "":
            break
        k, v = line.split("-")
        d_스톤_504_스테이크하우스[k] = v
with open("./data/쑝쑝돈까스 숭실대점.csv", "rt", encoding="UTF8") as f:
    while True:
        line = f.readline().strip()
        if line == "":
            break
        k, v = line.split("-")
        d_쑝쑝돈까스_숭실대점[k] = v
with open("./data/은화수식당 숭실대점.csv", "rt", encoding="UTF8") as f:
    while True:
        line = f.readline().strip()
        if line == "":
            break
        k, v = line.split("-")
        d_은화수식당_숭실대점[k] = v
with open("./data/지지고 숭실대점.csv", "rt", encoding="UTF8") as f:
    while True:
        line = f.readline().strip()
        if line == "":
            break
        k, v = line.split("-")
        d_지지고_숭실대점[k] = v
with open("./data/청년다방.csv", "rt", encoding="UTF8") as f:
    while True:
        line = f.readline().strip()
        if line == "":
            break
        k, v = line.split("-")
        d_청년다방[k] = v
with open("./data/크라이치즈버거 숭실대점.csv", "rt", encoding="UTF8") as f:
    while True:
        line = f.readline().strip()
        if line == "":
            break
        k, v = line.split("-")
        d_크라이치즈버거_숭실대점[k] = v
with open("./data/현선이네 숭실점.csv", "rt", encoding="UTF8") as f:
    while True:
        line = f.readline().strip()
        if line == "":
            break
        k, v = line.split("-")
        d_현선이네_숭실점[k] = v

while 1:
    print("-----점심 메뉴 추천 프로그램-----")
    print("1. 식당 추천")
    print("2. 가격별 음식 추천")
    print("3. 태그 별 식당 추천")
    print("4. 즐겨찾기")
    print("5. 프로그램 종료")
    select = int(input("입력: "))
    os.system("cls")

    if select == 1:
        r_식당 = random.choice(식당)
        r_index = 식당.index(r_식당)
        print("\n")
        print(r_식당)
        print("\n--------------메뉴판--------------\n")
        if r_index == 0:
            a = 0
            for k, v in d_889_상도.items():
                if a == 0:
                    a += 1
                else:
                    print(k, v + "원")
        elif r_index == 1:
            a = 0
            for k, v in d_The_Kone.items():
                if a == 0:
                    a += 1
                else:
                    print(k, v + "원")
        elif r_index == 2:
            a = 0
            for k, v in d_고렝.items():
                if a == 0:
                    a += 1
                else:
                    print(k, v + "원")
        elif r_index == 3:
            a = 0
            for k, v in d_긴자료코_숭실대입구역점.items():
                if a == 0:
                    a += 1
                else:
                    print(k, v + "원")
        elif r_index == 4:
            a = 0
            for k, v in d_내가찜한닭_숭실대점.items():
                if a == 0:
                    a += 1
                else:
                    print(k, v + "원")
        elif r_index == 5:
            a = 0
            for k, v in d_밀플랜비_숭실대점.items():
                if a == 0:
                    a += 1
                else:
                    print(k, v + "원")
        elif r_index == 6:
            a = 0
            for k, v in d_백채김치찌개_숭실대점.items():
                if a == 0:
                    a += 1
                else:
                    print(k, v + "원")
        elif r_index == 7:
            a = 0
            for k, v in d_베트남식당_퍼민.items():
                if a == 0:
                    a += 1
                else:
                    print(k, v + "원")
        elif r_index == 8:
            a = 0
            for k, v in d_샤로스톤.items():
                if a == 0:
                    a += 1
                else:
                    print(k, v + "원")
        elif r_index == 9:
            a = 0
            for k, v in d_손칼국수.items():
                if a == 0:
                    a += 1
                else:
                    print(k, v + "원")
        elif r_index == 10:
            a = 0
            for k, v in d_스톤_504_스테이크하우스.items():
                if a == 0:
                    a += 1
                else:
                    print(k, v + "원")
        elif r_index == 11:
            a = 0
            for k, v in d_쑝쑝돈까스_숭실대점.items():
                if a == 0:
                    a += 1
                else:
                    print(k, v + "원")
        elif r_index == 12:
            a = 0
            for k, v in d_은화수식당_숭실대점.items():
                if a == 0:
                    a += 1
                else:
                    print(k, v + "원")
        elif r_index == 13:
            a = 0
            for k, v in d_지지고_숭실대점.items():
                if a == 0:
                    a += 1
                else:
                    print(k, v + "원")
        elif r_index == 14:
            a = 0
            for k, v in d_청년다방.items():
                if a == 0:
                    a += 1
                else:
                    print(k, v + "원")
        elif r_index == 15:
            a = 0
            for k, v in d_크라이치즈버거_숭실대점.items():
                if a == 0:
                    a += 1
                else:
                    print(k, v + "원")
        elif r_index == 16:
            a = 0
            for k, v in d_현선이네_숭실점.items():
                if a == 0:
                    a += 1
                else:
                    print(k, v + "원")
        print("-" * 31)
        print("\n")
        answer1 = input("즐겨찾기에 추가하시겠습니까? (Y / N)")
        if answer1 == "Y":
            favorite.append(r_식당)

    if select == 2:
        print("가격대 () ~ ()")
        c1, c2 = map(int, input("입력: ").split(","))
        os.system("cls")
        print(c1, "~", c2, "가격대 음식 추천\n")

        a = 0
        for i in list(d_889_상도.values()):
            try:
                if int(i) >= c1 and int(i) <= c2:
                    if a == 0:
                        print("<" + d_889_상도["음식점"] + ">")
                        a += 1
                    location = list(d_889_상도.values()).index(i)
                    print(list(d_889_상도.keys())[location], i + "원")
                    print("\n")
            except:
                pass

        b = 0
        for i in list(d_The_Kone.values()):
            try:
                if int(i) >= c1 and int(i) <= c2:
                    if b == 0:
                        print("<" + d_The_Kone["음식점"] + ">")
                        b += 1
                    location = list(d_The_Kone.values()).index(i)
                    print(list(d_The_Kone.keys())[location], i + "원")
                    print("\n")
            except:
                pass

        c = 0
        for i in list(d_고렝.values()):
            try:
                if int(i) >= c1 and int(i) <= c2:
                    if c == 0:
                        print("<" + d_고렝["음식점"] + ">")
                        c += 1
                    location = list(d_고렝.values()).index(i)
                    print(list(d_고렝.keys())[location], i + "원")
                    print("\n")
            except:
                pass

        d = 0
        for i in list(d_긴자료코_숭실대입구역점.values()):
            try:
                if int(i) >= c1 and int(i) <= c2:
                    if d == 0:
                        print("<" + d_긴자료코_숭실대입구역점["음식점"] + ">")
                        d += 1
                    location = list(d_긴자료코_숭실대입구역점.values()).index(i)
                    print(list(d_긴자료코_숭실대입구역점.keys())[location], i + "원")
                    print("\n")
            except:
                pass

        e = 0
        for i in list(d_내가찜한닭_숭실대점.values()):
            try:
                if int(i) >= c1 and int(i) <= c2:
                    if e == 0:
                        print("<" + d_내가찜한닭_숭실대점["음식점"] + ">")
                        e += 1
                    location = list(d_내가찜한닭_숭실대점.values()).index(i)
                    print(list(d_내가찜한닭_숭실대점.keys())[location], i + "원")
                    print("\n")
            except:
                pass

        f = 0
        for i in list(d_밀플랜비_숭실대점.values()):
            try:
                if int(i) >= c1 and int(i) <= c2:
                    if f == 0:
                        print("<" + d_밀플랜비_숭실대점["음식점"] + ">")
                        f += 1
                    location = list(d_밀플랜비_숭실대점.values()).index(i)
                    print(list(d_밀플랜비_숭실대점.keys())[location], i + "원")
                    print("\n")
            except:
                pass

        g = 0
        for i in list(d_백채김치찌개_숭실대점.values()):
            try:
                if int(i) >= c1 and int(i) <= c2:
                    if g == 0:
                        print("<" + d_백채김치찌개_숭실대점["음식점"] + ">")
                        g += 1
                    location = list(d_백채김치찌개_숭실대점.values()).index(i)
                    print(list(d_백채김치찌개_숭실대점.keys())[location], i + "원")
                    print("\n")
            except:
                pass

        h = 0
        for i in list(d_베트남식당_퍼민.values()):
            try:
                if int(i) >= c1 and int(i) <= c2:
                    if h == 0:
                        print("<" + d_베트남식당_퍼민["음식점"] + ">")
                        h += 1
                    location = list(d_베트남식당_퍼민.values()).index(i)
                    print(list(d_베트남식당_퍼민.keys())[location], i + "원")
                    print("\n")
            except:
                pass

        j = 0
        for i in list(d_샤로스톤.values()):
            try:
                if int(i) >= c1 and int(i) <= c2:
                    if j == 0:
                        print("<" + d_샤로스톤["음식점"] + ">")
                        j += 1
                    location = list(d_샤로스톤.values()).index(i)
                    print(list(d_샤로스톤.keys())[location], i + "원")
                    print("\n")
            except:
                pass

        k = 0
        for i in list(d_손칼국수.values()):
            try:
                if int(i) >= c1 and int(i) <= c2:
                    if k == 0:
                        print("<" + d_손칼국수["음식점"] + ">")
                        k += 1
                    location = list(d_손칼국수.values()).index(i)
                    print(list(d_손칼국수.keys())[location], i + "원")
                    print("\n")
            except:
                pass

        l = 0
        for i in list(d_스톤_504_스테이크하우스.values()):
            try:
                if int(i) >= c1 and int(i) <= c2:
                    if l == 0:
                        print("<" + d_스톤_504_스테이크하우스["음식점"] + ">")
                        l += 1
                    location = list(d_스톤_504_스테이크하우스.values()).index(i)
                    print(list(d_스톤_504_스테이크하우스.keys())[location], i + "원")
                    print("\n")
            except:
                pass

        m = 0
        for i in list(d_쑝쑝돈까스_숭실대점.values()):
            try:
                if int(i) >= c1 and int(i) <= c2:
                    if m == 0:
                        print("<" + d_쑝쑝돈까스_숭실대점["음식점"] + ">")
                        m += 1
                    location = list(d_쑝쑝돈까스_숭실대점.values()).index(i)
                    print(list(d_쑝쑝돈까스_숭실대점.keys())[location], i + "원")
                    print("\n")
            except:
                pass

        n = 0
        for i in list(d_은화수식당_숭실대점.values()):
            try:
                if int(i) >= c1 and int(i) <= c2:
                    if n == 0:
                        print("<" + d_은화수식당_숭실대점["음식점"] + ">")
                        n += 1
                    location = list(d_은화수식당_숭실대점.values()).index(i)
                    print(list(d_은화수식당_숭실대점.keys())[location], i + "원")
                    print("\n")
            except:
                pass

        o = 0
        for i in list(d_지지고_숭실대점.values()):
            try:
                if int(i) >= c1 and int(i) <= c2:
                    if o == 0:
                        print("<" + d_지지고_숭실대점["음식점"] + ">")
                        o += 1
                    location = list(d_지지고_숭실대점.values()).index(i)
                    print(list(d_지지고_숭실대점.keys())[location], i + "원")
                    print("\n")
            except:
                pass

        p = 0
        for i in list(d_청년다방.values()):
            try:
                if int(i) >= c1 and int(i) <= c2:
                    if p == 0:
                        print("<" + d_청년다방["음식점"] + ">")
                        p += 1
                    location = list(d_청년다방.values()).index(i)
                    print(list(d_청년다방.keys())[location], i + "원")
                    print("\n")
            except:
                pass

        q = 0
        for i in list(d_크라이치즈버거_숭실대점.values()):
            try:
                if int(i) >= c1 and int(i) <= c2:
                    if q == 0:
                        print("<" + d_크라이치즈버거_숭실대점["음식점"] + ">")
                        q += 1
                    location = list(d_크라이치즈버거_숭실대점.values()).index(i)
                    print(list(d_크라이치즈버거_숭실대점.keys())[location], i + "원")
                    print("\n")
            except:
                pass

        r = 0
        for i in list(d_현선이네_숭실점.values()):
            try:
                if int(i) >= c1 and int(i) <= c2:
                    if r == 0:
                        print("<" + d_현선이네_숭실점["음식점"] + ">")
                        r += 1
                    location = list(d_현선이네_숭실점.values()).index(i)
                    print(list(d_현선이네_숭실점.keys())[location], i + "원")
                    print("\n")
            except:
                pass

    if select == 3:
        l_식당 = []
        for i in set(list(태그.values())):
            print(i, end="/ ")
        print("\n")
        while 1:
            tag = input("태그 입력: ")
            if tag not in set(list(태그.values())):
                print("태그가 올바르지 않습니다.\n")
            else:
                loc = 0
                for k in list(태그.values()):
                    if tag == k:
                        l_식당.append(list(태그.keys())[loc])
                    loc += 1
                for k in l_식당:
                    print(k)
                print("\n")
                break

    if select == 4:
        for i in set(favorite):
            print(i)
        print("\n")
        answer2 = input("음식점의 정보를 보시겠습니까? (Y / N)")
        if answer2 == "Y":
            for i in set(favorite):
                i_식당 = 식당.index(i)
                print("\n<" + i + ">")
                print("\n--------------메뉴판--------------\n")
                if i_식당 == 0:
                    a = 0
                    for k, v in d_889_상도.items():
                        if a == 0:
                            a += 1
                        else:
                            print(k, v + "원")
                elif i_식당 == 1:
                    a = 0
                    for k, v in d_The_Kone.items():
                        if a == 0:
                            a += 1
                        else:
                            print(k, v + "원")
                elif i_식당 == 2:
                    a = 0
                    for k, v in d_고렝.items():
                        if a == 0:
                            a += 1
                        else:
                            print(k, v + "원")
                elif i_식당 == 3:
                    a = 0
                    for k, v in d_긴자료코_숭실대입구역점.items():
                        if a == 0:
                            a += 1
                        else:
                            print(k, v + "원")
                elif i_식당 == 4:
                    a = 0
                    for k, v in d_내가찜한닭_숭실대점.items():
                        if a == 0:
                            a += 1
                        else:
                            print(k, v + "원")
                elif i_식당 == 5:
                    a = 0
                    for k, v in d_밀플랜비_숭실대점.items():
                        if a == 0:
                            a += 1
                        else:
                            print(k, v + "원")
                elif i_식당 == 6:
                    a = 0
                    for k, v in d_백채김치찌개_숭실대점.items():
                        if a == 0:
                            a += 1
                        else:
                            print(k, v + "원")
                elif i_식당 == 7:
                    a = 0
                    for k, v in d_베트남식당_퍼민.items():
                        if a == 0:
                            a += 1
                        else:
                            print(k, v + "원")
                elif i_식당 == 8:
                    a = 0
                    for k, v in d_샤로스톤.items():
                        if a == 0:
                            a += 1
                        else:
                            print(k, v + "원")
                elif i_식당 == 9:
                    a = 0
                    for k, v in d_손칼국수.items():
                        if a == 0:
                            a += 1
                        else:
                            print(k, v + "원")
                elif i_식당 == 10:
                    a = 0
                    for k, v in d_스톤_504_스테이크하우스.items():
                        if a == 0:
                            a += 1
                        else:
                            print(k, v + "원")
                elif i_식당 == 11:
                    a = 0
                    for k, v in d_쑝쑝돈까스_숭실대점.items():
                        if a == 0:
                            a += 1
                        else:
                            print(k, v + "원")
                elif i_식당 == 12:
                    a = 0
                    for k, v in d_은화수식당_숭실대점.items():
                        if a == 0:
                            a += 1
                        else:
                            print(k, v + "원")
                elif i_식당 == 13:
                    a = 0
                    for k, v in d_지지고_숭실대점.items():
                        if a == 0:
                            a += 1
                        else:
                            print(k, v + "원")
                elif i_식당 == 14:
                    a = 0
                    for k, v in d_청년다방.items():
                        if a == 0:
                            a += 1
                        else:
                            print(k, v + "원")
                elif i_식당 == 15:
                    a = 0
                    for k, v in d_크라이치즈버거_숭실대점.items():
                        if a == 0:
                            a += 1
                        else:
                            print(k, v + "원")
                elif i_식당 == 16:
                    a = 0
                    for k, v in d_현선이네_숭실점.items():
                        if a == 0:
                            a += 1
                        else:
                            print(k, v + "원")
                print("-" * 31)
                print("\n")

    if select == 5:
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바르지 않은 입력입니다.\n")
