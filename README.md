### 介绍

好久没有更技术文章了，今天更一个，算是造了一个轮子，花费了我很大精力，一个"web安全被动常规漏洞扫描器"，在全网范围内数万甚至数十万的web漏洞扫描器中，我的扫描器如何出众? 哈哈哈...可能也不是多么出众，但是我这种一线技术人员、一线实战派web漏洞挖掘选手觉得很实用，很实在，并不花里胡哨的。

既然是web漏洞扫描器，那么就要基本了解下什么是web漏洞挖掘，说白了就是修改http/s请求包的数据。

![](https://raw.githubusercontent.com/guimaizi/cloud/test/img/20200307181557.png)

如图，很标椎的一个http请求包，也是很标准的一个xss漏洞，那么判断xss的方式就是修改name参数的值，然后判断http的响应内容，如此来判断xss的漏洞存在，通常我们会手工在name参数追加payload:

```<img src=a onerror=alert(1)>```

判断响应内容来判断这是不是存在一个xss漏洞,或者追加' 、and 1=1、or 1=1、and sleep(3)来判断是否存在sql注入等，而且他妈的很奇怪的是每次都是这样，流水线了，不胜其烦，我也是服了 我们是黑客啊，居然开始干流水线工作了，这不科学啊,太傻逼了,那么这个时候你就需要我这个扫描器了。

效果视频: 

<video src="https://github.com/guimaizi/cloud/raw/test/20200307-190212967.mp4"/>

常规get\post 包括 Content-Type: application/json 、均可测。

思路就是把burp的http请求包抓出来保存为tmp.json

格式:

```{
{"headers": 
    {
        "Origin": "http://192.168.0.137",
         "Cookie": "PHPSESSID=fjkq8kiuutn3hkoj4uppsg30da",
         "Accept": "application/json,
         text/javascript,
         */*; q=0.01",
         "X-Requested-With": "XMLHttpRequest",
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,
         like Gecko) Chrome/81.0.4009.0 Safari/537.36",
         "Referer": "http://192.168.0.137/12345.php",
         "Connection": "close",
         "Accept-Encoding": "gzip,
         deflate",
         "Accept-Language": "en-US,
        en;q=0.9",
         "Content-Length": "85",
         "Content-Type": "application/json"
    },
     "method": 1,
     "url": "http://192.168.0.137:80/12345.php",
     "post": "
    {
        \"userName\":\"asdas\",
        \"passWord\":\"dsadsa\",
        \"type\":1,
        \"data\":
        {
            \"aaaa\":\"bbbb\",
            \"cccc\":11111
        }
    }
    "
}
```

然后通过脚本处理、追加payload后 进行测试漏洞。

如果配合 [mitmproxy](https://github.com/mitmproxy/mitmproxy)   那么就是个类似闭源工具[xray](https://github.com/chaitin/xray) 的被动扫描器、如果你再配合上一个强大的爬虫，那就是个主动扫描器。

反正开源的,你随意折腾,我没意见。

github: https://github.com/guimaizi/testing_wave



这么好的工具，有没有大爷大妈愿意赏我一碗鸡煲翅 wechat支付:

![](https://raw.githubusercontent.com/guimaizi/cloud/test/img/20200307192617.png)



建议/反馈/问问题前 请先赏碗鸡煲翅....

联系方式WeChat : 

![](https://raw.githubusercontent.com/guimaizi/cloud/test/img/20200307193002.jpg)



