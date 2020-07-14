# -*- coding: utf-8 -*-
# @File  : adapter_model_02.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-14
# @Desc  :
import os


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

    def get_page(self, page_num):
        pass


class TxtBook(IBook):
    """Txt解析类"""

    def parse_file(self, file_path):
        print(file_path + ' 文件解析成功')
        self.__page_count = 500
        return True

    def get_catalogue(self):
        return Catalogue('Txt电子书')

    def get_page_count(self):
        return self.__page_count

    def get_page(self, page_num):
        return Page(page_num)


class EpubBook(IBook):
    """Epub解析类"""

    def parse_file(self, file_path):
        print(file_path + ' 文件解析成功')
        self.__page_count = 800
        return True

    def get_catalogue(self):
        return Catalogue('Epub电子书')

    def get_page_count(self):
        return self.__page_count

    def get_page(self, page_num):
        return Page(page_num)


class PdfPage:
    """PDF页"""

    def __init__(self, page_num):
        self.__page_num = page_num

    def get_page_num(self):
        return self.__page_num


class ThirdPdf:
    """第三方PDF解析类"""
    def __init__(self):
        self.__page_num = 0

    def open(self, file_path):
        print('第三方解析PDF文件: ', file_path)
        self.__page_num = 1000
        return True

    def get_outline(self):
        pass

    def page_size(self):
        return self.__page_num

    def page(self, page_num):
        return PdfPage(page_num)


class PdfAdapterBook(IBook, ThirdPdf):

    def parse_file(self, file_path):
        rtn = super().parse_file(file_path)
        if rtn:
            print((file_path + '文件解析成功'))
        return rtn

    def get_catalogue(self):
        outline = super().get_catalogue()
        print('将Outline结构的目录换成Catalogue结构的目录')
        return Catalogue('PDF电子书')

    def get_page_count(self):
        return super().get_page_count()

    def get_page(self, page):
        page = super().get_page(page)
        print('将PdfPage的面向对象转化成Page的对象')
        return Page(page.get_page_num())


class Reader:
    """阅读器"""
    def __init__(self, name):
        self.__name = name
        self.__file_path = ''
        self.__cur_book = None
        self.__cur_page_num = -1

    def __init_book(self, file_path):
        self.__file_path = file_path
        ext_name = os.path.splitext(file_path)[1]
        if(ext_name.lower() == '.epub'):
            self.__cur_book = EpubBook()
        elif(ext_name.lower() == '.txt'):
            self.__cur_book = TxtBook()
        elif(ext_name.lower() == '.pdf'):
            self.__cur_book = PdfAdapterBook()
        else:
            self.__cur_book = None

    def open_flle(self, file_path):
        self.__init_book(file_path)
        if(self.__cur_book is not None):
            rtn = self.__cur_book.parse_file(file_path)
            if (rtn):
                self.__cur_page_num = 1
            return rtn
        return False

    def close_file(self):
        print('关闭 ' + self.__file_path + ' 文件')
        return True

    def show_catalogue(self):
        catalogue = self.__cur_book.get_catalogue()
        catalogue.show_info()

    def pre_page(self):
        return self.goto_page(self.__cur_page_num - 1)

    def next_page(self):
        return self.goto_page(self.__cur_page_num + 1)

    def goto_page(self, page_num):
        pass


def main():
    reader = Reader('阅读器')
    for book in ['平凡的世界.txt', '平凡的世界.epub', '平凡的世界.pdf']:
        if(not reader.open_flle(book)):
            return
        reader.show_catalogue()
        reader.goto_page(1)
        reader.next_page()
        reader.close_file()
        print()


if __name__ == '__main__':
    main()

