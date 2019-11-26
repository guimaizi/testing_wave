# coding: utf-8
'''
Created on Nov 25, 2019

@author: guimaizi
'''
from attack_plugin import  xss_testing,sqlinj_testing
class main:
    def __init__(self):
        print('--------------------------\n\n')
        print('-------scaning...--------\n\n')
        print('--------------------------\n\n\n')
    def main(self):
        xss=xss_testing.xss_testing()
        xss.run()
        sql=sqlinj_testing.sqlinj_testing()
        sql.run()
        print('\n-------------\nfinished')
if __name__ == '__main__':
    p1=main()
    p1.main()