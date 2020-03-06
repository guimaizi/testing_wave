# coding: utf-8
'''
@author: guimaizi
'''
from burp import IBurpExtender
from burp import IContextMenuFactory
from burp import IBurpExtenderCallbacks
from burp import IContextMenuInvocation
from burp import IHttpRequestResponse
from javax.swing import JMenuItem
import os,json,subprocess

class BurpExtender(IBurpExtender,  IContextMenuFactory):
    
    def registerExtenderCallbacks(self, callbacks):
        self._actionName = "test_vul"
        self._helers = callbacks.getHelpers()
        self._callbacks = callbacks
        callbacks.setExtensionName("test_vul")
        callbacks.registerContextMenuFactory(self)
        return 

    def createMenuItems(self, invocation):
        menu = []
        responses = invocation.getSelectedMessages()
        if len(responses) == 1:
            menu.append(JMenuItem(self._actionName, None , actionPerformed= lambda x, inv=invocation: self.Action(inv)))
            return menu
        return None

    def Action(self, invocation):
        request = invocation.getSelectedMessages().pop()
        analyzedRequest = self._helers.analyzeRequest(request)
        url = analyzedRequest.url
        headers = analyzedRequest.getHeaders()
        json_strs={}
        for value in headers:
            strs=value.split(':',1)
            if len(strs)>1 and strs[0] not in ['Host','GET','POST']:
                json_strs['%s'%strs[0]]=strs[1].lstrip()
        method=0
        if analyzedRequest.getMethod() == "POST":
            body = request.getRequest().tostring()[analyzedRequest.getBodyOffset():]
            method=1
        else:body='null'
        path=r"G:/Code/testing_wave"
        test_vul = "%s/main.py"%path        
        data={"method":method,"url":str(url),"post":body,"headers":json_strs}
        json_data=json.dumps(data)
        print json_data
        print 3333
        with open('%s/tmp.json'%path, 'w') as json_file:
            json_file.write(json_data)
        #subprocess.call('python3 /Users/guimaizi/hack-tool/burp_lib/test_vul.py')
        #os.system('open -a Terminal.app /Users/guimaizi/eclipse-workspace/testing_wave/start.sh')
        os.system('start cmd /k python G:/Code/testing_wave/main.py')