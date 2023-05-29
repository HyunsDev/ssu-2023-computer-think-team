import json

restaurant_names = [
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

tag = {
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


def get_restaurant(name):
    with open(f"./data/{name}.csv", "rt", encoding="utf-8") as f:
        menus = []
        while True:
            line = f.readline().strip()
            if line == "":
                break
            menu_name, menu_price = line.split("-")
            menus.append({"name": menu_name, "price": int(menu_price)})

        return {
            "name": name,
            "tags": tag[name].split(", "),
            "menus": menus,
        }


restaurants = []
for restaurant_name in restaurant_names:
    restaurant = get_restaurant(restaurant_name)

    restaurants.append(restaurant)
    print(restaurant)

with open("data.json", "w", encoding="utf8") as outfile:
    json.dump(restaurants, outfile, indent=4, ensure_ascii=False)
