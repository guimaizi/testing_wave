# coding: utf-8
'''
Created on Nov 12, 2019

@author: guimaizi
'''

import json,tkinter
from urllib import parse
class config_function:
    def __init__(self):
        self.path=''
        self.time_out=10
        
    def callback_target(self):
        with open('/Users/guimaizi/hack-tool/burp_lib/tmp.json', 'r') as f:
            data = json.load(f)
        return data
    def show_text(self):
        root = tkinter.Tk()
        te = tkinter.Text(root)
        sl = tkinter.Scrollbar(root)
        sl.pack(side='right', fill='y')
        te['yscrollcommand'] = sl.set
        for i in range(10):
            string = str(i) + '\n'
            te.insert('end', string)
        te.pack(side='left')
        sl['command'] = te.yview
        te.insert('end', 'xsssssss')
        te.update()
        root.mainloop()
if __name__ == '__main__':
    url='http://www.target.cn/zxft/20483.htm?dsdsa=dsadsa&dada=1&dsdada=3fdsf'
    payload='xsssguimaizi'
    p1=config_function()
    print(p1.url_process(url, payload))