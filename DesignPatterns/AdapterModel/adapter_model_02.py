# -*- coding: utf-8 -*-
# @File  : adapter_model_02.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-14
# @Desc  :


class Page:
    def __init__(self, page_num):
        self.__page_num = page_num

    def get_content(self):
        return f'第 {self.__page_num} 页内容'


class Catalogue:
    """目录结构"""
    def __init__(self, title):
        self.__title = title
        self.__chapters = []
        self.set_chapter('第一章')
        self.set_chapter('第二章')

    def set_chapter(self, title):
        self.__chapters.append(title)

    def show_info(self):
        print(f'标题: {self.__title}')
        for chapter in self.__chapters:
            print(chapter)


class IBook:
    """电子书接口类"""
    def __init__(self):
        self.__page_count = 0

    def parse_file(self, file_path):
        pass

    def get_catalogue(self):
        pass

    def get_page_count(self):
        pass

    def get_page(self, page):
        pass


class TxtBook(IBook):
    """Txt解析类"""

    def parse_file(self, file_path):
        print(file_path + ' 文件解析成功')
        self.__page_count = 500
        return False

    def get_catalogue(self):
        return Catalogue('Txt电子书')

    def get_page_count(self):
        return self.__page_count

    def get_page(self, page):
        return Page(page)


class EpubBook(IBook):
    """Epub解析类"""

    def parse_file(self, file_path):
        print(file_path + ' 文件解析成功')
        self.__page_count = 800
        return False

    def get_catalogue(self):
        return Catalogue('Epub电子书')

    def get_page_count(self):
        return self.__page_count

    def get_page(self, page):
        return Page(page)


def main():
    pass


if __name__ == '__main__':
    main()

