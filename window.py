import tkinter as tk
import random
from menu_parser import MenuParser
import json

restaurants = []
with open("data.json") as f:
    restaurants = json.load(f)

menus = []
for restaurant in restaurants:
    for menu in restaurant["menus"]:
        menus.append(
            {"name": menu["name"], "price": menu["price"], "store": restaurant}
        )


def recommend_menu():
    pass

    chosen_restaurant = random.choice(restaurants)
    chosen_menu = random.choice(chosen_restaurant["menus"])

    result_label.config(text=chosen_menu["name"])
    store_label.config(text=f"가게: {chosen_restaurant['name']}")
    price_label.config(text=f"가격: {chosen_menu['price']}원")


def recommend_price_menu():
    price_range = price_entry.get()  # 가격대 입력값 가져오기
    price_range = price_range.strip()  # 입력값 앞뒤 공백 제거

    if price_range:
        try:
            price_range = price_range.split(",")
            min_price = int(price_range[0].strip())
            max_price = int(price_range[1].strip())

            # 가격 범위에 맞는 음식 추천 로직 작성
            matched_menus = []
            for menu in menus:
                if min_price <= menu["price"] <= max_price:
                    matched_menus.append(menu)

            if matched_menus:
                random_menu = random.choice(matched_menus)
                restaurant = random_menu["store"]

                result_label.config(text=random_menu["name"])
                store_label.config(text=f"가게: {restaurant['name']}")
                price_label.config(text=f"가격: {random_menu['price']}원")
            else:
                result_label.config(text="해당 가격 범위의 음식이 없습니다.")
                store_label.config(text="")
                price_label.config(text="")
        except (ValueError, IndexError):
            result_label.config(text="가격대를 형식에 맞게 입력해주세요.")
            store_label.config(text="")
            price_label.config(text="")
    else:
        result_label.config(text="가격대를 입력해주세요.")
        store_label.config(text="")
        price_label.config(text="")


def recommend_tag_menu():
    tag = tag_entry.get()
    tag = tag.strip()

    if not tag:
        result_label.config(text="태그를 입력해주세요.")
        store_label.config(text="")
        price_label.config(text="")
        return

    matched_restaurants = []
    for restaurant in restaurants:
        if tag in restaurant["tags"]:
            matched_restaurants.append(restaurant)

    if matched_restaurants:
        matched_restaurant = random.choice(matched_restaurants)
        random_menu = random.choice(matched_restaurant["menus"])

        result_label.config(text=random_menu["name"])
        store_label.config(text=f"가게: {matched_restaurant['name']}")
        price_label.config(text=f"가격: {random_menu['price']}원")

    else:
        result_label.config(text="해당 태그의 음식이 없습니다.")
        store_label.config(text="")
        price_label.config(text="")


root = tk.Tk()
root.title("점심 메뉴 추천 프로그램")
root.geometry("1280x720")


# 왼쪽 박스
left_box = tk.Frame(root, padx=5, pady=5)
left_box.pack(side="left", expand=True, fill="both")
title_label = tk.Label(left_box, text="오늘의 학식", font=("굴림체", 12))
title_label.pack()

menuParser = MenuParser("20230531", 1)
menu = menuParser.get_menu_string()
left_menu_label = tk.Label(
    left_box, text=menu, font=("굴림체", 12), bg="white", justify="left"
)
left_menu_label.pack(fill="both")

# 오른쪽 박스
right_box = tk.Frame(root, padx=5, pady=5, width=300)
right_box.pack(side="right", expand=True, fill="y")

menu_list_frame = tk.Frame(right_box)
menu_list_frame.pack()

menu_list_label = tk.Label(menu_list_frame, text="메뉴 리스트", font=("굴림체", 12))
menu_list_label.pack()

scrollbar = tk.Scrollbar(menu_list_frame, orient="vertical")
scrollbar.pack(side="right", fill="both")

restaurant_box = tk.Listbox(menu_list_frame, yscrollcommand=scrollbar.set)
restaurant_box.pack(fill="both")
scrollbar["command"] = restaurant_box.yview

i = 0
for restaurant in restaurants:
    restaurant_box.insert(i, f"[ {restaurant['name']} ]")
    i += 1
    for menu in restaurant["menus"]:
        restaurant_box.insert(i, menu["name"])
        i += 1
    restaurant_box.insert(i, "")
    i += 1

tag_list_frame = tk.Frame(right_box)
tag_list_frame.pack()

tag_list_label = tk.Label(tag_list_frame, text="태그 리스트", font=("굴림체", 12))
tag_list_label.pack()

tag_scrollbar = tk.Scrollbar(tag_list_frame, orient="vertical")
tag_scrollbar.pack(side="right", fill="both")

tag_box = tk.Listbox(tag_list_frame, yscrollcommand=tag_scrollbar.set)
tag_box.pack(fill="both")

tag_scrollbar["command"] = tag_box.yview

tag_list = []
for restaurant in restaurants:
    for tag in restaurant["tags"]:
        if tag not in tag_list:
            tag_list.append(tag)

i = 0
for tag in tag_list:
    tag_box.insert(i, tag)
    i += 1


# 가운데 레이블
center_box = tk.Frame(root, padx=5, pady=5)
center_box.pack(expand=True, fill="both")


title_label = tk.Label(center_box, text="오늘의 점심 메뉴는?", font=("굴림체", 12))
title_label.pack()

menu_frame = tk.Frame(center_box)
menu_frame.pack()

recommend_button = tk.Button(menu_frame, text="메뉴 추천 받기", command=recommend_menu)
recommend_button.pack()

result_label = tk.Label(menu_frame, text="", font=("굴림체", 18), pady=30)
result_label.pack()

store_label = tk.Label(menu_frame, text="", font=("굴림체", 12))
store_label.pack()

price_label = tk.Label(menu_frame, text="", font=("굴림체", 12))
price_label.pack()


tag_frame = tk.Frame(center_box)
tag_frame.pack(side="bottom")

tag_entry_label = tk.Label(tag_frame, text="태그 입력:")
tag_entry_label.pack(side="left")

tag_entry = tk.Entry(tag_frame)
tag_entry.pack(side="left")

recommend_tag_button = tk.Button(
    tag_frame, text="태그별 음식 추천", command=recommend_tag_menu
)
recommend_tag_button.pack()


price_frame = tk.Frame(center_box)
price_frame.pack(side="bottom")

price_entry_label = tk.Label(price_frame, text="가격대 입력:")
price_entry_label.pack(side="left")

price_entry = tk.Entry(price_frame)
price_entry.pack(side="left")

recommend_price_button = tk.Button(
    price_frame, text="가격별 음식 추천", command=recommend_price_menu
)
recommend_price_button.pack()

root.mainloop()
