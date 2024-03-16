"""
计算不同图形的面积合
"""


class GraphController:
    def __init__(self):
        self.__list_graph = []

    @property
    def list_graph(self):
        return self.__list_graph

    def add_Graph(self, graph):
        self.__list_graph.append(graph)

    def calculate_total_area(self):
        total_area = 0
        for item in self.__list_graph:
            total_area += item.calc()
        return total_area


class Calculate:
    def calc(self):
        pass


class Rectangle(Calculate):
    def __init__(self, long=0, wide=0):
        self.long = long
        self.wide = wide

    def calc(self):
        super().calc()
        return self.long * self.wide


controller = GraphController()
controller.add_Graph(Rectangle(20, 50))
controller.add_Graph(Rectangle(40, 50))
print(controller.calculate_total_area())
for item in controller.list_graph:
    print(item.__dict__)




