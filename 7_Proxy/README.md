# 代理模式 Proxy

![image](https://github.com/escc1122/design-pattern/blob/master/7_Proxy/Proxy.jpg)


目前想到的好處是
由於clinet與實際物件間夾了一個中間層
所以可以
1.更換指向的位置
2.延後載入
3.只指向唯一實體物件
4.檢查使用者權限

servlet分流,進入的時後才開始指定對應的sevlet 


    Subject aaaa = new Proxy();

    aaaa.method();
