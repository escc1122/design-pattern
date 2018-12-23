#Builder 建造者模式

目前覺得這種模式適合用在 可以整理出固定流程的情況 但是細節有所不同

目前感覺不出他跟 TemplateMethod 有何使用上的差異


1.假設把發票建立過程拆解成  建立發票外觀=====>填入資料=======>列印

那麼 Director 就是建立這個流程,然後builder實作每個細節應該做什麼

![image](https://github.com/escc1122/design-pattern/blob/master/new/13_Builder/Builder.jpg)


2.如果今天把Director類別加入簡單工廠模式 這樣使用者也可以不用知道builder類別 但之後每新增一個類都必需要修改Director 但反射可解決

3.如果今天把這個模式用在出貨流程 那就可以切割成 訂單整理====>庫存檢查,庫存扣留====>建立出貨明細====>建立發票

但這樣會有很多細節是一致的 所以或許可以在拉出一個父類別去繼承
