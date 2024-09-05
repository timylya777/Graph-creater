def help():  print("work in progress")
def Graph_Valuer():
	x = 0
	while True:
		x += 1
		yield x
graph_valuer = Graph_Valuer()

class Map():
	def __init__(self):
		self.map = {}
	def new(self,id,item):
		self.map[id] = Graph(item,False,id)
	def update(self,id,item):
		self.map[id] = Graph(item,False,id)
	def get(self,id:int): #Return Graph
		return self.map[id] 
	def get_map(self):
		return self.map
	def get_str_map(self): 
		ret = []
		for i in self.map.keys():
			ret.append(str(self.map[i]))
		return ret
graph_map = Map()
def x(): global graph_map
x()
class Graph():
	def __init__(self,item,glob=True,id=0,connects=[]):#do not touch glob, fix id and connects if you can fix it
		self.item = item
		if id == 0: self.id = graph_valuer.__next__()
		else: self.id = id
		self.connects = []
		self.glob = glob
		if self.glob:
			graph_map.new(self.id,self.item)
	def update(self):
		if self.glob:
			graph_map.update(self.id,self.item)
	def append(self,x):
		self.connects.append(x)
		self.update()
	def remove(self,x):
		self.connects.remove(index(x.id))
		self.update()
	def __add__(self,x):
		if type(x) != type(self):
			print("Error: can't connect Graph with other type")
			return
		if self.id == x.id:
			print("Error: can't add self id")
			return
		if x.id in self.connects:
			print("Error: connect is in connects")
			return
		self.append(x.id)
		x.append(self.id)
	def __neg__(self,x):
		self.id.remove(x)
		x.id.remove(self)
	def __str__(self): return "id:"+str(self.id)+"; item:"+str(self.item)+"; connects:"+str(self.connects)
	def get(self):return self.item
	def replace(self,item): self.item = item
if __name__ == "__main__":
    pass
graph1 = Graph([Graph([2,1,Graph(5).get()]),Graph(2)])

print(graph_map.get_str_map())
graph_map.get(2).item = "hi" 
graph_map.get(2) + graph_map.get(3)
graph_map.get(1) + graph_map.get(2)
graph_map.get(2) + graph_map.get(1)
print(graph_map.get_str_map())
 