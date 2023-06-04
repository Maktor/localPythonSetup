#1
def greetings():
  print("Wasssap, user")
  
#2
def pack(a,b,c):
  return [a,b,c]

#3
def eat_lunch(myList):
  if len(myList) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(myList)):
      if i == 0:
        print(f"First I eat {myList[0]}")
      else:
        print(f"Next I eat {myList[i]}")

#Output
greetings()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["shawerma"])
eat_lunch(["shawerma","lamp","kebabs","Homus"])