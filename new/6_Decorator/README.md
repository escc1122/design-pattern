#裝飾模式 Decorator

在不變更主要類別的情況下 可以格外新增功能

![image](https://github.com/escc1122/design-pattern/blob/master/new/6_Decorator/Decorator.jpg)



  主要功能類別 a = new 主要功能類別();
  新增功能類別A aa = new 新增功能類別A(a);
  新增功能類別B bb = new 新增功能類別B(aa);
  
  bb.toDo();

結果會是 先執行主要功能類別 toDo() ====> 新增功能類別A toDo() =====> 新增功能類別B toDo()
