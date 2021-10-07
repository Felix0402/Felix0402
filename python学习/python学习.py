#python学习 作者唐凤廷 记录python学习过程和用于教学
#严禁复制 违者必究
#直接打印文本
print("Hello Python world!")

#用变量打印文本
message="Hello Python world!"
print(message)

#学习区分变量
message="Hello Python Crash Cours world!"
print(message)

#学习使用简易字符串
name="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#学习使用f字符串
first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"
print(full_name)
print(f"Hello,{full_name.title()}!")
message=f"Hello,{full_name.title()}!"
print(message)

#学习在突出显示文本中使用撇号
#message=‘One of Python's strengths is its diveres community’
message="One of Python's strengths is its diveres community"
print(message)

#学习在Python中进行计算
print(5+3)
print(16-8)
print(2*4)
print(16/2)

#学习在Python中使用列表
#创建列表
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
#提取列表中的元素
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])
#使用列表发送信息
message=f"My first bicycle was a {bicycles[0].title()}."
print(message)
names=['Felix','Ken','Ben','Tony']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
message=f"Hello,{names[0]}."
print(message)
message=f"Hello,{names[1]}."
print(message)
message=f"Hello,{names[2]}."
print(message)
message=f"Hello,{names[3]}."
print(message)
Commuter_tools=['Car','bike','Motorcycle','Train','Plane']
message=f"I would like to own a {Commuter_tools[0]}"
print(message)
message=f"I would like to own a {Commuter_tools[1]}"
print(message)
message=f"I would like to own a {Commuter_tools[2]}"
print(message)
message=f"I would like to own a {Commuter_tools[3]}"
print(message)
message=f"I would like to own a {Commuter_tools[4]}"
print(message)
#更改列表
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)