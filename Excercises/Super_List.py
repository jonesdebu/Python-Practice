class SuperList(list):
  def __len__(self):
    return 1000


MyList = SuperList()
MyList.extend([1,2,3])
print(MyList)
print(len(MyList))
print(MyList.__len__())
print(issubclass(SuperList, list))