from abc import ABCMeta, abstractmethod
import requests
from bs4 import BeautifulSoup


class MenuParser(metaclass=ABCMeta):
    def __init__(self, date, cafeteria_type) -> None:
        self.date = date
        self.cafeteria_type = cafeteria_type
        self.menus = []

    def get_menu(self):
        res = self.__get_menu()
        return res

    def get_menu_string(self):
        res = self.__get_menu()
        menu_string = ""
        for menu in res:
            menu_string += f"[ {menu} ]\n"
            for i in res[menu]["menus"]:
                menu_string += f"{i}\n"
            menu_string += "\n"
        return menu_string

    def __get_soup(self):
        raw_data = requests.get(
            f"http://m.soongguri.com/m_req/m_menu.php?rcd={self.cafeteria_type}&sdt={self.date}"
        )
        soup = BeautifulSoup(raw_data.content, "html.parser")
        return soup

    def __get_menu_rows(self):
        soup = self.__get_soup()

        tr_list = soup.find_all("tr")
        menu_nm_dict = dict()

        for tr_tag in tr_list:
            td_tag = tr_tag.find("td", {"class": "menu_nm"})
            if not td_tag:
                continue

            menu_nm_dict[td_tag.text] = tr_tag

        return menu_nm_dict

    def __get_menu(self):
        menu_rows = self.__get_menu_rows()

        menus = {}

        for menu_corner in menu_rows:
            menu_soup = menu_rows[menu_corner]

            corner = menu_soup.select_one(".menu_list font:nth-of-type(1)").text

            menu_soup.select_one(".menu_list font:nth-of-type(1)").decompose()
            menus_raws = menu_soup.select(".menu_list div")

            menu_list = []
            before_value = ""
            for menu_raw in menus_raws:
                if menu_raw.text in ["*알러지유발식품:", "*원산지:", ""]:
                    continue

                if before_value.startswith(menu_raw.text):
                    menu_list.pop()

                before_value = menu_raw.text
                menu_list.append(menu_raw.text)

            menus[menu_corner] = {
                "corner": corner,
                "menus": menu_list,
            }

        return menus
