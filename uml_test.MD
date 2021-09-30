![image](https://github.com/escc1122/design-pattern/blob/master/images/association.jpg)

    class Climate:
        def __init__(self):
            pass

    class Animal:
        def __init__(self):
            self._climate = Climate
            
            
![image](https://github.com/escc1122/design-pattern/blob/master/images/Aggregation.jpg)

    class WildGoode:
        def __init__(self):
            pass

    class WildGoodeAggregate:
        def __init__(self):
             self._arrayWildGoose:WildGoode[WildGoode] = []


![image](https://github.com/escc1122/design-pattern/blob/master/images/Composition.jpg)

    class Wing:
        def __init__(self):
            pass

    class bird:
        def __init__(self):
            self._wing_a = Wing()
            self._wing_b = Wing()

![image](https://github.com/escc1122/design-pattern/blob/master/images/Dependency.jpg)

    class Oxygen:
        def __init__(self):
            pass

    class Water:
        def __init__(self):
            pass

    class Animal2:
        def metabolism(self,oxygen:Oxygen,water:Water):
            pass
