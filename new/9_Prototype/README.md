# 原型模式 Prototype

不新建一個物件 而是從一個已存在的物件進行複製
複製過程中會扯到淺複製跟深複製

淺複製 : 單純複製值 如果有連結會跟原物件指向同一位置

深複製 : 連連結都要進行複製 但就會扯到要複製到幾層的問題

![image](https://github.com/escc1122/design-pattern/blob/master/new/9_Prototype/Prototype.jpg)


java的話直接使用clone就行
runntime情況下 使用序列化也可

感覺這種模式javascript 原型鍊更像

