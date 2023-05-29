from menu_parser import MenuParser


s = MenuParser("20230531", 1)
menus = s.get_menu()

for menu in menus:
    print("=================")
    print(menu)
    for i in menus[menu]["menus"]:
        print(i)
