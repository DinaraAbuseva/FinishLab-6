class Figure:

    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def count(self):
        return self.a * self.b * self.c
    
    def __add__(self, other):
        a = self.a + other.a
        b = self.a + other.a
        c = self.a + other.a
        return Figure(a, b, c)
    
    def __str__(self):
        return f"Объём фигуры: {Figure(self.a, self.b, self.c)}"
        
    
class Figure_with_empty(Figure):

    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d

    def count(self):
        empty = (self.a - self.d)*(self.b - self.d)*(self.c - self.d)
        return super().count() - empty
    
    def __str__(self):
        return f"Объём фигуры с полостью: {Figure_with_empty(self.a, self.b, self.c, self.d)}"
    
    
class Sum_figure_same(Figure):

    def __init__(self, a, b, c, same_num):
        super().__init__(a, b, c)
        self.same_num = same_num
    
    def count(self):
        return super().count() * self.same_num
    
    def __add__(self, other):
        if (self.a, self.b, self.c) == (other.a, other.b, other.c):
            return Sum_figure_same(self.a, self.b, self.c, self.same_num + 1)
    
    def __str__(self):
        return f"Суммарный объём одинаковых фигур: {Sum_figure_same(self.a, self.b, self.c, self.same_num)}"
    
