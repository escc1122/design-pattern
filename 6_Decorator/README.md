# 裝飾模式 Decorator

在不變更主要類別的情況下 可以格外新增功能 但要注意裝飾的順序
可用於某些特例情況下 不改寫原程式碼而進行新增特殊功能

![image](https://github.com/escc1122/design-pattern/blob/master/6_Decorator/Decorator.jpg)



    主要功能類別 a = new 主要功能類別();
    新增功能類別A aa = new 新增功能類別A(a);
    新增功能類別B bb = new 新增功能類別B(aa);
  
    bb.toDo();

結果會是 先執行主要功能類別 toDo() ====> 新增功能類別A toDo() =====> 新增功能類別B toDo()





也可以去掉介面 改寫成繼承主要功能類別

![image](https://github.com/escc1122/design-pattern/blob/master/6_Decorator/Decorator2.jpg)
