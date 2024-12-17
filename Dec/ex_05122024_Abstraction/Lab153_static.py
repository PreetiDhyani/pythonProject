
class o:

  @staticmethod
  def sum(a, b):
    return a + b

  def sub(self,a,b):
      return a-b

print(o.sum(2,3))

print("------------")

obj_r = o()
result = obj_r.sub(4,6)
print(result)
