### 工具介绍

被动式web扫描器，为了在挖洞中降低工作量，避免重复工作，进而研发出该开源工具,支持get/post/json  http/s传参的漏洞检测。

### 功能介绍/目录说明

代理抓取http/s请求包按格式入库，通过py读取数据库内容，追加或者修改http请求参数进行漏洞测试。

attack_plugin目录是攻击测试模块，目前包含xss sql 命令注入。



### burpsuite插件模式

burpsuite Python插件

https://www.jython.org/download

```
插件文件  burp_vul_plugin.py   请自行修改代码内路径相关
burpsuite插件不会安装 请自行百度...
```



### http/s代理模式

安装该软件: https://github.com/mitmproxy/mitmproxy

设置https证书



```
cd 该脚本目录/porxy_module
mitmdump -s ./http_porxy.py -p 8788
#等加载完成后
cd 该脚本目录
python3 proxy_run.py
```







### 环境设置/要求

**要求**:

 python3.5+ mongodb  burpsuite mitmproxy  没有系统要求  py嘛...自己改。

**设置**:

pip3 install -r requirements.txt

设置 config_module/config.json文件  

设置 config_module/config_function.py  文件内路径



### 关于我

**wechat**: 

![](https://s1.ax1x.com/2018/12/06/F10y28.png)

**e-mail**: 635713319@qq.com



**谢谢打赏** : 

![](https://raw.githubusercontent.com/guimaizi/cloud/test/img/20190301182006.jpg)



