# 流畅的Python

## 本书大纲

### 关于本书 

- 发版次数

	- 2017-05

		- 2020-04

- 页数

	- P600

- 适用人群

	- 本书致力于帮助 Python 开发人员挖掘这门语言及相关程序库的优秀特性，避免重复劳动， 同时写出简洁、流畅、易读、易维护，并且具有地道 Python 风格的代码。本书尤其深入探讨了 Python 语言的高级用法，涵盖数据结构、Python 风格的对象、并行与并发，以及元编程等不同 的方面。
本书适合中高级 Python 软件开发人员阅读参考。

- 勉励的话

	- 夫夷以近，则游者众；险以远，则至者少。而世之奇伟、瑰怪，非常之观，常在于险远，而人之所罕至焉，故非有志者不能至也。

### 第一部分

- 第1章 python数据模型

### 第二部分

- 数据结构

	- 第2章 序列构成的数组
	- 第3章 字典和集合
	- 第4章 文本和字节序列

### 第三部分

- 把函数视作对象

## 第一部分 （序幕）

### 第1章 Python数据模型

- 本章目标

	- 一致性体现在哪些方面、好处与优势
	- Python纸牌案例分析
	- 特殊方法的使用

- Python风格之一致性

	- len(collection)而非collection.len()

- Python纸牌

	- 实现原理

		- namedtuple 具名元组

			- 适用场景：构建只有少数属性，没有方法的对象

				-  比普通tuple具有更好的可读性，代码更易于维护。 
				- 通过索引值进行访问
				- 不能对其值进行修改（元组）
				- 通过属性取值
				- 与字典相比，又更加的轻量和高效。

		- 列表生成式
		- 魔术方法

			- __init__:初始化
			- __len__:求长度
			- __getitem__：取特定数据

	- 功能

		- 查看总数

			- len(deck)

		- 取指定的牌

			- deck[0]

		- 随机取牌

			- choice(deck)

		- 某张牌是否存在

			- Card('Q','hearts') in deck

		- 排序

			- 规则

				- A最大，2最小。黑桃最大、红桃次之、方块再次、梅花最小

			- 点数索引 * 权重的个数 + 自身花色权重

- 如何使用特殊方法

	- 存在的意义是被解释器调用
	- 大可不必自己调用，通过内置函数才是正解
	- 内置的数据类型，会有自己的调用方式

		- PyVarObject里的ob_size属性
		- PyVarObject 是表示内存中长度可变的内置对象的 C 语言结构体
		- 看原码了解PyVarObject

	- 调用时隐式的

		-  可迭代对象

			- __iter__() 
			- __next__()

	- 不要自己随意添加特殊方法

		- 绝对不要使用两个前导下划线，这是很烦人的自私行为。    --Ian Bicking

- 模拟数值类型

	- __init__
	- __repr__

		- __str__

	- __abs__
	- __bool__
	- __add__
	- __mul__

- 本章总结

	- 一致性体现在哪些方面、好处与优势

		- 对内：风格统一
		- 对外：

			- 扩展性：避免重复造轮子
			- 兼容性：跟第三方插件，甚至未来可能出现的功能兼容

	- Python纸牌案例分析、模拟数值类型
	- 为什么len方法不是普通方法
	- 可迭代对象
	- 常见的几种魔术方法

## 第二部分 （数据结构）

### 第2章 序列构成的数组

- 本章目标

	- Python风格之一致性

- ABC与Python

	- 高级语言为时过早

		- 在错误的时间里做错误的事，那是一段荒谬；  在错误的时间里做正确的事，那是一次遗憾；  在正确的时间里做错误的事，那是一种无奈；  在正确的时间里做正确的事；那是一场幸福。

	- 平台迁移能力弱
	- 拓展性差，难以添加新功能
	- 使用人群范围窄，仅仅专注于编程初学者，没有把有经验的编程人员纳入其中
	- 失败是成功之母

- 深入理解不同的序列类型

	- 作用

		- 避免重复造车
		- 把自己定义的 API 设计得跟原生的序列一样
		- 甚至是跟未来可能出现的序列类型 保持兼容。
		- 写出准确、高效、地道的python代码

	- 序列类型

		- 存储类型

			- 容器序列：存放对象的引用

				- 特点：可以存放任意类型

					- list、tuple 和 collections.deque 

			- 扁平序列：存放对象的值

				- 只能存放字符、字节、数值等基础类型，更加紧凑

					- str、bytes、bytearray、memoryview 和 array.array

		- 是否可变

			- 可变序列

				- list、bytearray、array.array、collections.deque 和 memoryview

			- 不可变序列

				- tuple、str 和 bytes

		- 值引用和地址引用

			- id()
			- 深浅copy

		- 参数传递

			- Python中函数参数的传递是传递的变量的值，即就是变量所指向的对象的地址。
			- 一般的，我们有下面的规律：

				- 1. 不可变对象作为函数参数，相当于C系语言的值传递。

2. 可变对象作为函数参数，相当于C系语言的引用传递。

3.一旦函数中遇到=，就会重新开辟一个内存空间，不再对传递过来的参数有影响

	- 列表推导式和生成器

		- 列表推导式

			- 纸牌案例中出现了两次

				- 续行符可以省略

			- 使用场景

				- 通常用于创建新列表，并尽量保持简短 不超过两行
				- 过滤或加工其他可迭代类型，生成一个新列表

			- 特性

				- 可读性

				  ranks=[]
				  for n in range(2,11):
				      ranks.append(n)
				  ranks.append("J")
				  ranks.append("Q")
				  ranks.append("K")
				  ranks.append("A")
				  print(ranks)
				  
				  su=0
				  for i in range(0,101):
				      su+=i
				  print(su)
				  su2=sum([n for n in range(0,101)])
				  print(su2)
				  sum(range(101))

				- 高效性

					- filter

						- 过滤器函数

							- 把可迭代类型中的元素，通过函数名加工，生成一个新的列表

					- map

						- 格式map(函数名,可迭代类型)

							- 把可迭代类型中的元素，通过函数名加工，生成一个新的列表

					- timeit

						- 第一个参数是你要计时的语句或者函数。 传递给 Timer 的第二个参数是为第一个参数语句构建环境的导入语句。 从内部讲， timeit 构建起一个独立的虚拟环境， 手工地执行建立语句，然后手工地编译和执行被计时语句。
						- timeit.repeat(cmd, setup=SETUP, number=TIMES)

							-  它接受两个可选参数。 第一个参数是重复整个测试的次数，第二个参数是每个测试中调用被计时语句的次数。 两个参数都是可选的，它们的默认值分别是 3 和1000000。 repeat() 方法返回以秒记录的每个测试循环的耗时列表。

					- 高效性demo

					  import timeit
					  
					  TIMES = 10000
					  
					  SETUP = """
					  symbols = '$¢£¥€¤'
					  def non_ascii(c):
					      return c > 127
					  """
					  
					  def clock(label, cmd):
					      res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
					      print(label, *('{:.3f}'.format(x) for x in res))
					  
					  clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
					  clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
					  clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
					  clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')

					- 参考博客

						- https://www.cnblogs.com/YK2012/p/9656809.html

			- 笛卡尔积

				- SQL语句多表连接的时候常提到
				- 列表推导可以

					- ps：P20、PDF49

				- demoCode

				  colors = ['black','white']
				  sizes = ['S','M','L']
				  tshirts = [(color,size) for color in colors for size in sizes]
				  print(tshirts)
				  for color in colors:
				      for size in sizes:
				          print((color,size))
				  
				  
				  tshirts = [(color,size) for size in sizes for color in colors]
				  print(tshirts)

		- 生成器

			- 特点：节省内存

				- 遵守了迭代器协议，可以逐个地产出元素，而不是先建 立一个完整的列表

			- 语法：跟列表推导类似，把[]换成()
			- demoCode

			  import sys
			  
			  colors = ['black', 'white']
			  sizes = ['S', 'M', 'L']
			  listcomps = [i for i in range(0, 100000)]
			  print(sys.getsizeof(listcomps))
			  
			  genexps =  (i for i in range(0, 100000))
			  print(sys.getsizeof(genexps))
			  
			  genexps2 = range(0, 100000)
			  print(sys.getsizeof(genexps2))
			  
			  print(listcomps[100])
			  print(next(genexps))
			  print(genexps2[100])

		- 其他推导式

			- 字典推导式
			- 集合推导式
			- 更多

				- https://www.cnblogs.com/YK2012/p/9726739.html

	- 元组

		- 元组和记录

			- 定义变量时候通过,逗号分割就是数组。a=1,2,3
			- 不可变的列表

				- 性能高
				- + 两个元组合并

					- 重新生成了新元组

				- 元组内部如果有可变数据类型，可变数据可进行修改操作

				  t = (1, 2, [30, 40])
				  t[2].extend([50, 60])

				- 自己总结：可变与不可变是指元素的内存地址值

			- 没有字段名的记录

				- CodeDemo

				  lax_coordinates = (33.9425, -118.408056)
				  city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
				  traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
				                  ('ESP', 'XDA205856')]
				  for passport in sorted(traveler_ids):
				      print('%s/%s' % passport)
				  for country, _ in traveler_ids:
				      print(country)

			- 如果在任何的表达式里我们在元组内对元素排 序，这些元素所携带的信息就会丢失，因为这些信息是跟它们的位置有关的。？？？

		- 元组拆包

			- 拆包让元组可以完美地被当作记录来使用
			- 拆包可以应用到任何可迭代对象上
			- 被可迭代对象 中的元素数量必须要跟接受这些元素的元组的空档数一致

				- _

					- 因为它也是 gettext.gettext 函数的常用别名

				- *

					- 用*来处理剩下的元素 
					- 在平行赋值中，* 前缀只能用在一个变量名前面，但是这个变量可以出现在赋值表达式的 任意位置

			- 最好辨认的元组拆包形式就是平行赋值

				-  b, a = a, b
				- CodeDemo

				  a=(1,2,3,4,5)
				  print(a)
				  print("-------")
				  a,_,_,_,c=(1,2,3,4,5)
				  print(a,c)
				  print("-------")
				  a,*b,c,d=(1,2,3,4,5)
				  print(b)
				  print(a,c,d)
				  print("-------")
				  a,*b,c,d,e,f=(1,2,3,4,5)
				  print(b,d)

		- 嵌套元祖拆包

			- CodeView

			  metro_areas = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
			                 ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
			                 ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
			                 ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
			                 ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)), ]
			  
			  print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
			  fmt = '{:15} | {:9.4f} | {:9.4f}'
			  for name,cc,pop,(latitude,longitude) in metro_areas:
			      if longitude <= 0:
			          print(fmt.format(name,latitude,longitude))

				- print

					- 
format方式
2.1 格式：
[[fill]align][sign][#][0][width][,][.precision][type]
fill 【可选】空白处填充的字符
align 【可选】对齐方式（需配合width使用）
<，内容左对齐
>，内容右对齐(默认)
＝，内容右对齐，将符号放置在填充字符的左侧，且只对数字类型有效。 即使：符号+填充物+数字
^，内容居中
sign 【可选】有无符号数字
+，正号加正，负号加负；
-，正号不变，负号加负；
空格 ，正号空格，负号加负；
# 【可选】对于二进制、八进制、十六进制，如果加上#，会显示 0b/0o/0x，否则不显示
， 【可选】为数字添加分隔符，如：1,000,000
width 【可选】格式化位所占宽度
.precision 【可选】小数位保留精度
type 【可选】格式化类型
传入” 字符串类型 “的参数
s，格式化字符串类型数据
空白，未指定类型，则默认是None，同s
传入“ 整数类型 ”的参数
b，将10进制整数自动转换成2进制表示然后格式化
c，将10进制整数自动转换为其对应的unicode字符
d，十进制整数
o，将10进制整数自动转换成8进制表示然后格式化；
x，将10进制整数自动转换成16进制表示然后格式化（小写x）
X，将10进制整数自动转换成16进制表示然后格式化（大写X）
传入“ 浮点型或小数类型 ”的参数
e， 转换为科学计数法（小写e）表示，然后格式化；
E， 转换为科学计数法（大写E）表示，然后格式化;
f ， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
F， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
g， 自动在e和f中切换
G， 自动在E和F中切换
%，显示百分比（默认显示小数点后6位）

		- 具名元组

			- collections.namedtuple 是一个工厂函数，它可以用来构建一个带字段名的元组和一个有 名字的类
			- 特点

				- 创建（类名，字段名集合）
				- 从普通元组中继承来的属性（见第一章）

				  from collections import namedtuple
				  
				  City = namedtuple('City', 'name country population coordinates') #创建一个具名元组
				  tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
				  print(tokyo)
				  print(tokyo.population)
				  print(tokyo.coordinates)
				  print(tokyo[1])

				- 专有属性

					- 类属性_fields 

						- 所有字段名称

					- 类方法 _make(iterable) 

						- 顾名思义，生成类实例

					- 实例方法 _asdict()

						- 顾名思义，转换成字典

			- CodeView

			  from collections import namedtuple
			  
			  City = namedtuple('City', 'name country population coordinates')  # 创建一个具名元组
			  tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
			  
			  
			  print("------专有属性--------")
			  # 1:类属性 _fields
			  print(City._fields)
			  LatLong = namedtuple('LatLong', 'lat long')
			  beijing_data = ('BeiJing', 'China', 2153, LatLong(39.5427, 116.2317))
			  # 2:类方法 _make(iterable)
			  bj=City._make(beijing_data)
			  # 3:实例方法 _asdict()
			  print(bj._asdict())

		- 不可变列表的元组

			- https://www.cnblogs.com/YK2012/p/9645058.html
			- PDF57

	- 切片

		- 切片和区间会忽略最后一个元素 

			- 左闭右开原则
			- 好处

				- 只有最后一个元素信息时，快速知晓元素个数

					- range(3)
					- my_list[:3]

				- 起止位置信息都可见时，可以快速计算出切片和区间长度:stop-start

					- rang(1,3)
					- my_list[1:3]

				- 利用任意一个下标把序列分割成不重叠的两部分

					- l = [10, 20, 30, 40, 50, 60] 
l[:2] # 在下标2的地方分割 [10, 20] 
l[2:] # [30, 40, 50, 60] 
l[:3] # 在下标3的地方分割 [10, 20, 30]  
l[3:] # [40, 50, 60]

		- 对对象进行切片 

			- [i : i+n : m] 

				- i 是切片的起始索引值，为列表首位时可省略；i+n 是切片的结束位置，为列表末位时可省略；m 是步长，默认值是1，不允许为0 ，当m为负数时，列表翻转。
				- 从序列的第i位索引起，向右取到后n位元素为止，按m间隔过滤

			- 把其实索引想象成左手，终止索引想象成右手，手心之间表示取出的结果。如果是步长为负数表示右手为起始位置，左手为终止位置，然后再把得到的内容翻转。
			- codeView

			  invoice = """
			  0.....6................................40..........52.55........
			  1909  Pimoroni PiBrella                    $17.50    3    $52.50
			  1489  6mm Tactile Switch x20                $4.95    2     $9.90
			  1510  Panavise Jr. - PV-201                $28.00    1    $28.00
			  1601  PiTFT Mini Kit 320x240               $34.95    1    $34.95
			  """
			  SKU = slice(0, 6)
			  DESCRIPTION = slice(6, 40)
			  UNIT_PRICE = slice(40, 52)
			  QUANTITY = slice(52, 55)
			  ITEM_TOTAL = slice(55, None)
			  line_items = invoice.split('\n')[2:]
			  for item in line_items:
			      print(item[UNIT_PRICE], item[DESCRIPTION])

		- 多维切片和省略

			- ToDo：数组补充

		- 给切片赋值

			- 通过切片操作对象
			- codeDemo

			  li = list(range(10))
			  print(li)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
			  # 嫁接
			  li[2:5] = [10, 30]
			  print(li)  # [0, 1, 10, 30, 5, 6, 7, 8, 9]
			  # 切除
			  del li[5:7]
			  print(li)  # [0, 1, 10, 30, 5, 8, 9]
			  # 匹配替换
			  li[3::2] = [11,22] # 小心这种写法，如果匹配的个数与给定替换的个数不一致，会有问题：
			  print(li)
			  li[2:5]=[100]  # 警惕这种写法，右侧必须是个可迭代对象
			  print(li)

		- 切片练习题

			- https://www.cnblogs.com/YK2012/p/11919109.html

				- 数据类型 3、4

	- 对序列使用

		- + *

			- 通常: 1：相同类型的数据，2：原序列不被修改:3：产生一个新的
			- 元素是对其他可变对象的引用的话，就要格外小心
			- codeView

			  board = [["_"] * 3] * 3  
			  print(board) 
			  board[1][2] = "x" 
			  print(board) 
			  
			  row = ["_"] * 3
			  board = []
			  for i in range(3):
			    board.append(row)

		- += *=

			- 就地加法

				- 对不可变序列进行重复拼接操作的话，效率会很低，因为每次都有一个新对象，而解释器 需要把原来对象中的元素先复制到新的对象里，然后再追加新的元素
				- str 是个例外

			- 一个谜题

				- t = (1, 2, [30, 40])
t[2] += ([50, 60])

					- a. t 变成 (1, 2, [30, 40, 50, 60])。
					- b. 因为 tuple 不支持对它的元素赋值，所以会抛出 TypeError 异常。 
					- c. 以上两个都不是。 
					-  d. a 和 b 都是对的。

				- 谜题结论

				  dis.dis('s[a] += b') 
				  1       0 LOAD_NAME        0 (s)   # Pushes the value associated with co_names[namei] onto the stack.
				                             将s压到堆栈中
				         2 LOAD_NAME        1 (a)   # 将a压到堆栈中
				         4 DUP_TOP_TWO             # 将两个引用复制到堆栈顶部，并以相同的顺序保留它们。
				         6 BINARY_SUBSCR            # Implements TOS = TOS1[TOS]. 将 s[a] 的值存入 TOS（Top Of Stack，栈的顶端）。 
				         8 LOAD_NAME        2 (b)   # 将b压到堆栈中
				         10 INPLACE_ADD             # Implements in-place TOS = TOS1 + TOS. 计算 TOS += b。这一步能够完成，是因为 TOS 指向的是一个可变对象（也就是示例 2-15 里的列表）。 
				         12 ROT_THREE              # 将第二个和第三个堆栈项目向上提起一个位置，从上向下移动到位置三。
				         14 STORE_SUBSCR            # Implements TOS1[TOS] = TOS2. s[a] = TOS 赋值。这一步失败，是因为 s 是不可变的元组（示例 2-15 中的元组 t）。
				         16 LOAD_CONST        0 (None)  # Pushes co_consts[consti] onto the stack.
				         18 RETURN_VALUE            # 将TOS一起返回给函数的调用者。

					- 1• 不要把可变对象放在元组里面。
					-  2• 增量赋值不是一个原子操作。
					-  3• 查看 Python 的字节码对我们了解代码背后的运行机制很有帮助。

	- 排序

		- list.sort()与sorted

		  fruits = ['grape', 'raspberry', 'apple', 'banana']
		  
		  print(sorted(fruits))  #  ['apple', 'banana', 'grape', 'raspberry']
		  print(fruits) # ['grape', 'raspberry', 'apple', 'banana']  #原列表不受影响
		  print(sorted(fruits, reverse=True)) # ['raspberry', 'grape', 'banana', 'apple']
		  print(sorted(fruits, key=len))  # ['grape', 'apple', 'banana', 'raspberry']  #排序算法稳定
		  print(sorted(fruits, key=len, reverse=True)) #['raspberry', 'banana', 'grape', 'apple'] #算法稳定
		  fruits.sort()
		  print(fruits)  # fruits ['apple', 'banana', 'grape', 'raspberry']  #就地排序

			- 区别

				- 就地排序list.sort()

					- 列表可以，元组没有
					- 返回值None 

						- 弊端：无法串联

						  hh=" asdF ".upper().replace('A','z').lower().replace('f','F')[10:1:-1].strip()
						  print(hh)

				- 新建表

					- 返回一个新的列表

		- 练习题

		  l = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19] 
		   sorted(l, key=int)

			- https://www.cnblogs.com/YK2012/p/11919109.html   数据类型 9、10  函数 5

		- 二分法管理管理有序序列

			- 二分查找

	- bisect

		- 简约之美

			- 二分查找
			-  前提：有序序列
			- 查询（源码分析）

				- CodeView

				  import bisect
				  import sys
				  
				  HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
				  NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
				  ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'
				  
				  def bisect_right(a, x, lo=0, hi=None):
				      """Return the index where to insert item x in list a, assuming a is sorted.
				  
				      The return value i is such that all e in a[:i] have e <= x, and all e in
				      a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
				      insert just after the rightmost x already there.
				  
				      Optional args lo (default 0) and hi (default len(a)) bound the
				      slice of a to be searched.
				      """
				  
				      if lo < 0:
				          raise ValueError('lo must be non-negative')
				      if hi is None:
				          hi = len(a)
				      while lo < hi:
				          mid = (lo+hi)//2
				          if x < a[mid]: hi = mid
				          else: lo = mid+1
				      return lo
				  
				  def demo(bisect_fn):
				      for needle in reversed(NEEDLES):
				          # position = bisect_fn(HAYSTACK, needle)
				          position = bisect.bisect_left(HAYSTACK, needle)
				          offset = position * '  |'
				          print(ROW_FMT.format(needle, position, offset))
				  
				  
				  if __name__ == '__main__':
				      if sys.argv[-1] == 'left':
				          bisect_fn = bisect.bisect_left
				      else:
				          bisect_fn = bisect.bisect
				      print('DEMO:', bisect_fn.__name__)
				      print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
				      demo(bisect_fn)

				- CodeView

				  import bisect
				  import sys
				  
				  
				  def grade(socre,brakpoints=[60,70,80,90],grades='FDCBA'):
				      i=bisect.bisect(brakpoints,socre)
				      return grades[i]
				   
				  print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

			- 插入

				- CodeView

				  import bisect
				  import random
				  
				  SIZE = 7
				  random.seed(1729) #种子值
				  my_list = []
				  for i in range(SIZE):
				      new_item = random.randrange(SIZE * 2)
				      bisect.insort(my_list, new_item)
				      print('%2d ->' % new_item, my_list)
				  bisect.insort_left(my_list, 10.0)
				  print('%2d ->' % new_item, my_list)

	- 当列表不是首选

		-  数组（只包含数字）

			- （不是float对象，而是字节表述）

				- array.fromfile 读取速度快

					- 用 array.fromfile 从一个二 进制文件里读出 1000 万个双精度浮点数只需要 0.1 秒，这比从文本文件里读取的速度要快 60 倍，因为后者会使用内置的 float 方法把每一行文字转换成浮点数。

				-  array. tofile 写入快

					- 使用 array. tofile 写入到二进制文件，比以每行一个浮点数的方式把所有数字写入到文本文件要快 7 倍。

				- 占用空间少

					- 1000 万个这样的数在二进制文件里只占用 80 000 000 个字节(每个浮点数占用 8 个字节，不需要任何额外空间)，如果是文本文件的话，我们需要 181 515 739 个字节。

				- codeView

				  from array import array
				  from random import random
				  
				  floats = array('d', (random() for i in range(10 ** 7))) # d:双精度
				  print(floats[0],floats[10 ** 7 - 1])
				  
				  # fp=open('floats.bin','wb')
				  # floats.tofile(fp)
				  # fp.close()
				  
				  # floats2=array('d')
				  # fp=open('floats.bin','rb')
				  # floats2.fromfile(fp,10**7)
				  # fp.close()
				  # print(floats2[10 ** 7 - 1])
				  
				  floats3=array(floats.typecode,sorted(floats))
				  print(floats3[0],floats3[10 ** 7 - 1])

				- sorted 排序 和 插入

				  import bisect
				  from array import array
				  from random import random, randrange
				  
				  floats = array('d', (randrange(1, 50) for i in range(10)))  # d:双精度
				  print(floats)  # array('d', [7.0, 34.0, 15.0, 16.0, 30.0, 5.0, 2.0, 44.0, 14.0, 19.0])
				  
				  floats2 = array(floats.typecode, sorted(floats))
				  print(floats2)  # array('d', [2.0, 5.0, 7.0, 14.0, 15.0, 16.0, 19.0, 30.0, 34.0, 44.0])
				  
				  bisect.insort(floats2, 25)
				  print(floats2)  # array('d', [2.0, 5.0, 7.0, 14.0, 15.0, 16.0, 19.0, 25.0, 30.0, 34.0, 44.0])

		- 内存视图

		  from array import array
		  from random import random
		  
		  numbers = array('h', [-2, -1, 0, 1, 2]) #signed short
		  memv = memoryview(numbers)      #5个短整型有符号整数的数组创建一个memoryview
		  print (len(memv))               #打印长度
		  print (memv.tolist())           #转换成列表形式
		  
		  memv_oct = memv.cast('B')       #内存共享 转换成无符号字符类型
		  print (memv_oct.tolist()) 
		  # memv_oct.tolist()产生的元素比原始数组多了一倍？
		  # memv.cast(‘B’)把memv转换成一个unsigned char int的新memoryview，并返回给memv_oct。signed short int在内存中是以2个字节存储，而unsigned char int在内存中则是1个字节存储。
		  # signed short int类型的原码最高位表示正负，0代表正数，1代表负数。它们内存中是以补码的形式存储的，其中正数的补码和原码相同；负数的补码，是其原码除符号位（即最高位，也就是最后一位）外，其余全部取反，再加1。
		  # 所以，signed short int类型的-2，其原码为0100 0000 0000 0001，除符号位取反，为1011 1111 1111 1111，再加1，为0111 1111 1111 1111。当以unsigned char int类型读出来的时候，就成了254 255了；-1亦是同理，即255 255
		  
		  memv_oct[5] = 4                 #把位置5的字节赋值成4
		  print (numbers)                 #因为我们把占 2 个字节的整数的高位字节改成了 4，所以这个有符号整数的值就变成了 1024
		  
		  print("-------------")

		- 队列（频繁执行先进先出操作）

			- numpy多维数组

			  import numpy, scipy
			  
			  a = numpy.arange(1, 31)  # 创建一个数组
			  print(a)
			  print(type(a))  # <class 'numpy.ndarray'>
			  print(a.shape)  # (30,)
			  a.shape = 6, 5  # 把数组转换成二维的，需要注意 转换后的数组个数和当前数组个数一致
			  print(a)
			  #  [ 1  2  3  4  5]
			  #  [ 6  7  8  9 10]
			  #  [11 12 13 14 15]
			  #  [16 17 18 19 20]
			  #  [21 22 23 24 25]
			  #  [26 27 28 29 30]
			  
			  print(a[2])  # [11 12 13 14 15]
			  print(a[2][1])  # 12
			  print("多维切片")
			  print(a[6:2:-1,1:5:2])
			  # [[27 29]
			  #  [22 24]
			  #  [17 19]]
			  
			  a.shape = 2, 5,3  # 把数组转换成二维的，需要注意 转换后的数组个数和当前数组个数一致
			  print(a)
			  #
			  # [
			  # [[ 1  2  3]
			  #   [ 4  5  6]
			  #   [ 7  8  9]
			  #   [10 11 12]
			  #   [13 14 15]]
			  #
			  #  [[16 17 18]
			  #   [19 20 21]
			  #   [22 23 24]
			  #   [25 26 27]
			  #   [28 29 30]]
			  #   ]
			  print("省略")
			  print(a[1:,...,0:3:2])
			  # [[[18]
			  #   [21]
			  #   [24]
			  #   [27]
			  #   [30]]]
			  
			  a.transpose() #  行列转换

			- numpy读写

			  from array import array
			  from random import random
			  from time import perf_counter as pc
			  import numpy
			  
			  # floats = array('d', (random() for i in range(10 ** 7)))  # d:双精度
			  # t0=pc()
			  #  numpy.save('floats-10M', floats)
			  # print(pc()-t0) #0.07865749999999999
			  floats2 = numpy.load('floats-10M.npy', 'r+')
			  print(floats2[-3:])  # [0.62999599 0.80283711 0.03370366]
			  floats2 *= .5       # 把数组中每个数都乘以0.5
			  print(floats2[-3:])
			  t0=pc()
			  floats2 /= 3
			  print(pc()-t0) #0.0122691

			- 双向队列（快速从首尾两端增删数据）

				- CodeView

				  from collections import deque
				  
				  dq = deque(range(10), maxlen=10)
				  print(dq)
				  dq.rotate(3)  #队列旋转 deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
				  print(dq)  # 可以看做一个环
				  dq.rotate(-4) # deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)
				  print(dq)  # 可以看做一个环
				  dq.appendleft(-1)
				  print(dq)  # 可以看做一个环
				  dq.extend([11, 22, 33])
				  print(dq)
				  dq.extendleft([10, 20, 30, 40])
				  print(dq)

- 本章小结

	- Python 风格的一致性

		- 不管哪种数据结构（字符串、列表、元组.....）都用一套丰富的操作（迭代、切片、排序......）

	- 类型划分

		- 变与不变
		- 容器、扁平

	- 列表推导式与生成器
	- 元组、切片、排序
	- 列表替换场景

### 第3章 字典和集合

- 本章大纲

	- 基于原著、合理丰富
	- • 常见的字典方法 
	- • 如何处理查找不到的键 
	- • 标准库中 dict 类型的变种 
	- • set 和 frozenset 类型 
	- • 散列表的工作原理 
	- • 散列表带来的潜在影响（什么样的数据类型可作为键、不可预知的顺序，等等）

- 字典

	- 可散列

		- 用 isinstance 而不是 type 来检查某个参数是否为 dict 类型 （PDF：84）

		  from collections import abc, OrderedDict, UserDict
		  
		  # isinstance和type区别
		  # isinstance()：认为子类是一种父类类型，考虑继承关系
		  # type()：不会认为子类是一种父类类型，不考虑继承关系。
		  # 如果要判断两个类型是否相同推荐使用 isinstance()。
		  my_dict = {}
		  print(isinstance(my_dict, abc.Mapping), type(my_dict).__name__ == 'dict')
		  my_dict2 = OrderedDict([])
		  print(isinstance(my_dict2, abc.Mapping), type(my_dict2).__name__ == 'dict')
		  
		  
		  class StrkeyDict(UserDict):
		      pass
		  
		  
		  my_dict3 = StrkeyDict()
		  print(isinstance(my_dict3, abc.Mapping), type(my_dict2).__name__ == 'dict')

			- isinstance和type区别

				- isinstance()：认为子类是一种父类类型，考虑继承关系
				- 不会认为子类是一种父类类型，不考虑继承关系。

		- 特点

			- 散列值不变

				- 如果一个对象是可散列的，那么在这个对象的生命周期中，它的散列值是不变 的

					- 注意：生命周期中不变

			- 实现两个方法

				- __hash__()和__qe__()

			- 两个可散列对象是相等的，那么它们的 散列值一定是一样的。若a==b，那么hash(a)==hash(b)

				- print(hash(1.0000000000000001))

		- 常见 类型

			- 原子不可变数据类型

				- str、bytes 和数值类型

			- frozenset 里只能容纳可散列类型
			- 元组

			  t1 = (1, 2, "a", (3, 4))
			  print(hash(t1))
			  t2 = (1, 2, frozenset([30, 40]))
			  print(hash(t2))
			  t3 = (1, 2, "a", [3, 4])
			  # print(hash(t3))

				- 组包含的所有元素都是可散列类型

	- 创建方法

		- 构造方法

		  a = dict(one=1, two=2, three=3)
		  b = {'one': 1, "two": 2, "three": 3}
		  c = dict(zip(["one", "two", "three"], [1, 2, 3]))  # 拉链函数:可迭代对象 打包成元组
		  d = dict([("two", 2), ('one', 1), ("three", 3)])  #
		  e = dict({"two": 2, 'one': 1, "three": 3})
		  print(a == b == c == e == d)
		  
		  print("----------")
		  
		  a = [1, 2, 3]
		  b = [4, 5, 6]
		  c = [4, 5, 6, 7, 8]
		  zipped = zip(a, b)  # 打包为元组的列表
		  print(type(zipped))
		  print(*zipped)  # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
		  print(*zip(a, c))  # 元素个数与最短的列表一致

			- dict(one=1)
			- {"one"=1}
			- dict(zip)
			- dict([元组])
			- dict({字典})

		- 字典推导

		  dial_codes = [(86, 'China'),
		                (91, 'India'),
		                (1, 'United States'),
		                (62, 'Indonesia'),
		                (55, 'Brazil'),
		                (92, 'Pakistan'),
		                (880, 'Bangladesh'),
		                (234, 'Nigeria'),
		                (7, 'Russia'),
		                (81, 'Japan')]
		  
		  print(dial_codes)
		  # 利用推导来获取数据
		  country_code = {country: code for code, country in dial_codes}
		  print(country_code)
		  country_code2 = {code: country.upper() for code, country in dial_codes  if code < 66}
		  print(country_code2)

			- 字典推导（dictcomp）可以从任何以键值对作为元素的可迭 代对象中构建出字典
			- 格式：{key:value for key,value in 集合}

	- 常见字典类与映射方法 （PDF87 X）

		- 字典 dict
		- 默认字典 DefaultDict

		  from collections import defaultdict
		  
		  #参数是类型
		  d=defaultdict(list)
		  d['a'].append(1)
		  d['a'].append(2)
		  d['a'].append(2)
		  d['b'].append(3)
		  print(d)
		  
		  d2=defaultdict(set)
		  d2['a'].add(1)
		  d2['a'].add(2)
		  d2['a'].add(2)
		  d2['b'].add(3)
		  print(d2)
		  
		  d3 = {}
		  d3.setdefault('a', []).append(1)
		  d3.setdefault('a', []).append(2)
		  d3.setdefault('b', []).append(3)
		  print(d3)  # {'a': [1, 2], 'b': [3]}
		  
		  # 有序字典 OrderedDict
		  # 一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维 护着另外一个链表
		  # OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。
		  # 每次当一个新的元素插入进来的时候，它会被放到链表的尾部。对于一个已经存在的键的重复赋值不会 改变键的顺序
		  from collections import OrderedDict
		  
		  d4 = OrderedDict()
		  d4['a'] = 1
		  d4['b'] = 2
		  d4['c'] = 3
		  d4['d'] = 4
		  for k, v in d4.items():
		      print(k, '=====', v)
		  
		  import json
		  print(json.dumps(d4)) # {"a": 1, "b": 2, "c": 3, "d": 4}
		  # 删除
		  d4.popitem() #默认一处字典中最先插入的元素（先进先出）
		  print(json.dumps(d4)) # {"a": 1, "b": 2, "c": 3}
		  d4.popitem(last=False) #默认一处字典中最先插入的元素（先进先出）
		  print(json.dumps(d4)) # {"b": 2, "c": 3}
		  
		  print("-----循环-----")
		  prices = {
		      'ACME': 45.23,
		      'AAPL': 612.78,
		      'IBM': 205.55,
		      'HPQ': 37.20,
		      'FB': 10.75
		  }
		  price1 = zip(prices.values(), prices.keys())
		  for k, v in price1.__iter__():
		      print(k, '==', v)

		- 有序字典 OrderedDict

			- 字典是有序的还是无序的？

			  dicta = {"a": 1, "b": 2}
			  dictb = {"b": 2, "a": 1, }
			  print(dicta,dictb)
			  print(dicta == dictb)
			  print("------列表-------")
			  lista = ["a", "b"]
			  listb = ["b", "a", ]
			  print(lista,listb)
			  print(lista==listb)
			  print("------有序字典-------")
			  from collections import OrderedDict
			  d4 = OrderedDict()
			  d4['a'] = 1
			  d4['b'] = 2
			  d5 = OrderedDict()
			  d5['b'] = 2
			  d5['a'] = 1
			  print(d4,d5)
			  print(d4==d5)

				- 哈希结构会有一个head地址，里面的数据会分散到不同的列表链，所以看似是无序的，但对于同一组字典，总需要有一个标识去连结，所以读取时也会按存储顺序取数据，只是不会按特定规则排列。

		- 鸭子类型

			- 鸭子类型（duck typing）是动态类型的一种风格
			- 一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由"当前方法和属性的集合"决定。
			- 一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟可以被称为鸭子“
			- 关注点在于对象的行为，能作什么；而不是关注对象所属的类型
			- codeView

			  class duck():
			      def walk(self):
			          print('I walk like a duck')
			      def swim(self):
			          print('I swim like a duck')
			  
			  class person():
			      def walk(self):
			          print('this one walk like a duck')
			      def swim(self):
			          print('this one swim like a duck')
			  
			  # 我们并不关心这个对象的类型本身或是这个类继承，而是这个类是如何被使用的。我们可以通过下面的代码来调用这些类的方法。
			  
			  def watch_duck(animial):
			      """
			      函数接收到这个类对象，并没有检查对象的类型，而是直接调用这个对象的走和游的方法，如果不存在，就报错
			      :param animial:
			      :return:
			      """
			      animial.walk()
			      animial.swim()
			  
			  small_duck = duck()
			  watch_duck(small_duck)
			  
			  duck_like_man = person()
			  watch_duck(duck_like_man)

		- update 方法处理参数 m 的方式

		  dicta={"a":0,"b":2}
		  dictb={"a":1,"c":3} # 映射对象
		  dicta.update(dictb)
		  print(dicta)
		  tuplec=[("a",11),("b",22),("d",33)]
		  dicta.update(tuplec) # 键值对迭代器
		  print(dicta)
		  
		  "--------同样的鸭子模型（extend）多态---------"
		  a=["a","b"]
		  name_tuple=("e","f")
		  a.extend(name_tuple)
		  print(a)
		  name_set=set()
		  name_set.add("g")
		  name_set.add("h")
		  a.extend(name_set)
		  print(a)
		  a.extend(i for i in range(3))
		  print(a)

	- setdefault 处理默认值

	  import sys
	  import re
	  
	  WORD_RE = re.compile(r'\w+')
	  index = {}
	  with open(sys.argv[0], encoding='utf-8') as fp:
	      for line_no, line in enumerate(fp, 1):
	          for match in WORD_RE.finditer(line):
	              word = match.group()
	              column_no = match.start() + 1
	              location = (line_no, column_no)
	              # 方法一
	              # occurrences = index.get(word, []) # 提取 word 出现的情况，如果还没有它的记录返回 【】
	              # occurrences.append(location) # 把新单词出现的位置添加到列表的后面
	              # index[word] = occurrences # 把新的列表放回到字典中 #又涉及一次到查询
	              # 方法二
	              index.setdefault(word,[]).append(location)
	  # 以字母顺序打印结果
	  for word in sorted(index, key=str.upper):
	      print(word, index[word])

	- 映射的弹性键查询

		- 有时候为了方便起见，就算某个键在映射里不存在，我们也希望在通过这个键读取值的 时候能得到一个默认值

			- 方法一：是通过 defaultdict 这 个类型而不是普通的 dict，
			- 方法二：另一个是给自己定义一个 dict 的子类，然后在子类中实现 __missing__ 方法

		- 方法一defaultdict（PDF90描述的很清楚）

			- codeView

			  import sys
			  import re
			  import collections
			  
			  WORD_RE = re.compile(f'\w+')
			  
			  index = collections.defaultdict(list)
			  
			  with open(sys.argv[0], encoding='utf-8') as fp:
			      for line_no, line in enumerate(fp, 1):
			          for match in WORD_RE.finditer(line):
			              word = match.group()
			              column_no = match.start() + 1
			              location = (line_no, column_no)
			              index[word].append(location) # 如果index并没有word的记录，那么 default_factory 会被调用，为查询不到的键创造一个值
			  for word in sorted(index, key=str.upper):
			      print(word, index[word])

		- 特殊方法__missing__

		  """
		  查询的时候，映射类型里面的键，统统换成str﻿
		  如果一个类例如StrKeyDict0继承了dict。然后这个继承类提供了一个__missing__方法，
		  那么在__getitem__碰到找不到的键的时候，Python会自动调用它
		  """
		  
		  
		  class StrKeyDict0(dict):
		      # 该类继承了dict
		      def __missing__(self, key):
		          print("i'm missing")
		          # 如果找不到的键，本身就是字符串，抛异常
		          if isinstance(key, str):
		              raise KeyError(key)
		          return self[str(key)]
		  
		      def get(self, key, default=None):
		          try:
		              return self[key]  # 通过这种形式委托给__getitem__.如果这个时候再找不到那就走__missing__
		          except KeyError:
		              return default  # 如果__missing__也是失败
		  
		      def __contains__(self, key):
		          # 先按照传入键的原本的值来查找（我们的映射类型中可能含有非字符串的键），如果没 找到，再用 str() 方法把键转换成字符串再查找一次。
		          return key in self.keys() or str(key) in self.keys()
		  
		  
		  # 当有非字符串的键被查找的时候，StrKeyDict0 是如何在该键不存在的情况下， 把它转换为字符串的
		  d = StrKeyDict0([('2', 'two'), ('4', 'four')])
		  # print(d['2'])
		  # print("-------非字符串查找,转换成字符串后存在--------")
		  # print(d[4])
		  # print("-------非字符串查找,转换成字符串后仍然不存在--------")
		  # print(d[1])
		  
		  # d.get('2')
		  # d.get(4)
		  # print(d.get(1))
		  # print( 2 in d )
		  print( 1 in d )

			- 如果一个类继承了dict，然后这个继承类提供了__missing__方法，那么在__getitem__碰到找不到的键的时候，Python 会就会调用它

	- 字典的变种

		- collections.OrderedDict

			- 字典的有序与无序（跟python版本有关3.7之后）

			  import collections
			  
			  d2 = {}
			  d2['a'] = 'A'
			  d2['b'] = 'B'
			  d2['c'] = 'C'
			  
			  d3 = {}
			  d3['c'] = 'C'
			  d3['a'] = 'A'
			  d3['b'] = 'B'
			  print(d2 , d3)
			  print(d2 == d3)  # True
			  print('OrderedDict:')
			  d4 = collections.OrderedDict()
			  d4['a'] = 'A'
			  d4['b'] = 'B'
			  d4['c'] = 'C'
			  d5 = collections.OrderedDict()
			  d5['c'] = 'C'
			  d5['a'] = 'A'
			  d5['b'] = 'B'
			  print(d4 , d5)
			  print(d4 == d5)  # False

		- collections.ChainMap

			- 这些对象会被当 作一个整体被逐个查找，直到键被找到为止。
			- ChainMap实际上是把放入的字典存储在一个队列中，当进行字典的增加删除等操作只会在第一个字典上进行，当进行查找的时候会依次查找

			  from collections import ChainMap
			  
			  a = {"x": 1, "z": 3}
			  b = {"y": 2, "z": 4}
			  c = ChainMap(a, b)
			  # print(c)
			  
			  a.update({"x": 2})
			  # print(c)  # 同步更新
			  
			  # 当对ChainMap进行修改的时候总是只会对第一个字典进行修改
			  print(c["z"])
			  c["z"]=5
			  # print(c)
			  
			  c.pop('z')
			  # print(c)
			  
			  # c.pop('z')  # 报错
			  # del c["y"]    # 报错
			  print('-------------------')
			  a = ChainMap()
			  a["x"]=1
			  print(a) # ChainMap({'x': 1})
			  
			  b=a.new_child()
			  print(b) # ChainMap({}, {'x': 1})
			  b["x"]=2
			  print(b) # ChainMap({'x': 2}, {'x': 1})
			  b["y"]=3
			  print(b) # ChainMap({'x': 2, 'y': 3}, {'x': 1})
			  print(a) # ChainMap({'x': 1})
			  
			  c=a.new_child()
			  print(c) # ChainMap({}, {'x': 1})
			  print(c["x"]) # 1
			  c["y"]=1
			  print(c) # ChainMap({'y': 1}, {'x': 1})
			  
			  d=c.parents
			  print(d) # ChainMap({'x': 1})
			  print(type(d))
			  print(d is a,d==a) # False True

			- new_child()方法实质上是在列表的第一个元素前放入一个字典，默认是{}

		- collections.Counter

			- 每次更新一个键的时候都会增加这个计数 器

			  from collections import Counter
			  
			  s = 'To be,or not to be:that is the question'
			  c = Counter(s)
			  print(c)
			  #Counter({' ': 7, 't': 6, 'o': 5, 'e': 4, 'b': 2, 'n': 2, 'h': 2, 'i': 2, 's': 2, 'T': 1, ',': 1, 'r': 1, ':': 1, 'a': 1, 'q': 1, 'u': 1})
			  total = sum([v for k, v in c.items() if k in ['y', 'a', 'n', 'g', 'o']])
			  print(total) # 简单理解c是一个dict，使用items()方法可以遍历dict的key和value。 如果 k
			  
			  # 同样的，可以对list统计
			  from collections import Counter
			  
			  elements = ['jack', 'JACK', 'lucy', 'April', 'Lucy', 'mike', 'JAck']
			  c = Counter(elements)
			  print(c) # Counter({'jack': 1, 'JACK': 1, 'lucy': 1, 'April': 1, 'Lucy': 1, 'mike': 1, 'JAck': 1})
			  new_elements=['alice','steven']
			  c.update(new_elements)
			  print(c) # Counter({'jack': 1, 'JACK': 1, 'lucy': 1, 'April': 1, 'Lucy': 1, 'mike': 1, 'JAck': 1, 'alice': 1, 'steven': 1})
			  new_elements=['JACK','JAck','jaCK']
			  c.subtract(new_elements)
			  print(c) # Counter({'jack': 1, 'lucy': 1, 'April': 1, 'Lucy': 1, 'mike': 1, 'alice': 1, 'steven': 1, 'JACK': 0, 'JAck': 0, 'jaCK': -1})
			  del c['jack']
			  print(c) # Counter({'lucy': 1, 'April': 1, 'Lucy': 1, 'mike': 1, 'alice': 1, 'steven': 1, 'JACK': 0, 'JAck': 0, 'jaCK': -1})
			  
			  a = Counter('aaab')
			  b = Counter('ccdd')
			  
			  # +
			  a_sum_b = a + b
			  print(a_sum_b)
			  
			  # -
			  a_sub_b = a - b
			  print(a_sub_b)
			  
			  # &， 交集
			  a_and_b = a & b
			  print(a_and_b)
			  
			  # |， 并集
			  a_union_b = a | b
			  print(a_union_b)

		- 子类化UserDict

			- 以 UserDict 为基类，总比以普通的 dict 为基类要来得方便
			- UserDict 并不是dict 的子类，但是UserDict 有一个叫作 data 的属性，是 dict 的实例，这个属性实际上是 UserDict 最终存储数据的地
			- CodeView

			  from collections import UserDict
			  
			  
			  class StrkeyDict(UserDict):
			      def __missing__(self, key):
			          if isinstance(key,str):
			              raise KeyError
			          return self[str(key)]
			  
			      def __setitem__(self, key, value):
			          self.data[str(key)]=value
			  
			      def __contains__(self, key):
			          return str(key) in self.data
			  
			  # 当有非字符串的键被查找的时候，StrkeyDict 是如何在该键不存在的情况下， 把它转换为字符串的
			  d = StrkeyDict([('2', 'two'), ('4', 'four')])
			  print(d['2'])
			  print("-------非字符串查找,转换成字符串后存在--------")
			  print(d[4])
			  print("-------非字符串查找,转换成字符串后仍然不存在--------")
			  # print(d[1]) 报错
			  
			  d.get('2')
			  d.get(4)
			  print(d.get(1))
			  print( 2 in d )
			  print( 1 in d )

- 不可变映射类型

  from types import MappingProxyType
  
  d = {1: 'A'}
  d_proxy = MappingProxyType(d)
  print(d_proxy)  # {1: 'A'}
  
  print(d_proxy[1])  # A
  d_proxy[2] = 'x' #直接赋值就报错

- 常见练习题

	- 参考博客 3数据类型 8

- 集合

	- 特点

		- 本质：许多唯一对象的聚集

			- 去重

		- 集合中的元素必须是可散列的
		- 中缀运算符

			- 交 &
			- 差 -
			- 并 ∪
			- 补 \

		- 高效性demo

		  import timeit
		  
		  # 在含有 10 000 000 个元素的 haystack 里搜 索 1000 个值，算下来大概是每个元素 3 微秒。
		  TIMES = 100
		  
		  SETUP = """
		  from random import randint
		  haystack = {i for i in range(10 ** 7)}
		  needles = {randint(0, 10 ** 7) for i in range(1000)}
		  """
		  
		  cmd = "found = len(needles & haystack)"
		  res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
		  print("交集耗时：", *('{:.3f}'.format(x) for x in res))
		  
		  cmd2 = """  
		  found = 0   
		  for n in needles:   
		      if n in haystack:  
		          found += 1  
		  """
		  res = timeit.repeat(cmd2, setup=SETUP, number=TIMES)
		  print("循环耗时：", *('{:.3f}'.format(x) for x in res))

			- 散列表

	- 创建方式

		- 集合字面量

			- {1}

				- set([1])

			- set(1)
			- set()
			-  frozenset(range(10)) 

		- 集合推导式

			- {i for i in range(10)}

	- 集合的操作

	  a = {1, 2, 3}
	  b = {3, 4, 5}
	  
	  print("--------数学运算符---------")
	  # 交集  s &= z
	  print(a & b, a, b)  # {3} {1, 2, 3} {3, 4, 5}
	  print(b & a, a, b)
	  # 差集  s -= z
	  print(a - b, a, b)  # {1, 2} {1, 2, 3} {3, 4, 5}
	  print(b - a, a, b)  # {4, 5} {1, 2, 3} {3, 4, 5}
	  # 并集  s |= z
	  print(a | b, a, b)  # {3} {1, 2, 3} {3, 4, 5}
	  print(b | a, a, b)
	  # 补集  s ^= z
	  print(a ^ b, a, b)  # {1, 2, 4, 5} {1, 2, 3} {3, 4, 5}
	  print(b ^ a, a, b)  # {1, 2, 4, 5} {1, 2, 3} {3, 4, 5}
	  
	  c = {1, 2}
	  e = 2
	  f = {1, 2, 3}
	  print("-----比较运算符-----")
	  print(e in a)  # 元素 e 是否属于 s
	  print(f<=a,c<=a)
	  print(f<a,c<a)

		- 数学运算

			- 交差并补

			  a = {1, 2, 3}
			  b = {3, 4, 5}
			   
			  # 交集  s &= z
			  print(a & b, a, b)  # {3} {1, 2, 3} {3, 4, 5}
			  print(b & a, a, b)
			  # 差集  s -= z
			  print(a - b, a, b)  # {1, 2} {1, 2, 3} {3, 4, 5}
			  print(b - a, a, b)  # {4, 5} {1, 2, 3} {3, 4, 5}
			  # 并集  s |= z
			  print(a | b, a, b)  # {3} {1, 2, 3} {3, 4, 5}
			  print(b | a, a, b)
			  
			  # 补集  s ^= z
			  print(a ^ b, a, b)  # {1, 2, 4, 5} {1, 2, 3} {3, 4, 5}
			  print(b ^ a, a, b) # {1, 2, 4, 5} {1, 2, 3} {3, 4, 5}

		- 比较运算符
		- 其他运算符

- 散列表

	- 本节目标

		- • Python 里的 dict 和 set 的效率有多高？
		-  • 为什么它们是无序的？ 
		-  • 为什么不应该在迭代循环 dict 或是 set 的同时往里添加元素？
		- • 为什么 dict 的键和 set 元素的顺序是跟据它们被添加的次序而定的，以及为什么在映射对象的生命周期中，这个顺序并不是一成不变的？
		- • 为什么并不是所有的 Python 对象都可以当作 dict 的键或 set 里的元素？ 

	- 一个关于效率的实验

		- 所有的 Python 程序员都从经验中得出结论，认为字典和集合的速度是非常快的。接下来我 们要通过可控的实验来证实这一点。
		- CodeView

			- 1：准备数据

			  """
			  为容器性能测试生成数据
			  """
			  
			  import random
			  import array
			  
			  MAX_EXPONENT = 7  #最大指数
			  HAYSTACK_LEN = 10 ** MAX_EXPONENT     # 干草垛
			  NEEDLES_LEN = 10 ** (MAX_EXPONENT - 1) # 针
			  SAMPLE_LEN = HAYSTACK_LEN + NEEDLES_LEN // 2  # 样品长度
			  
			  needles = array.array('d') # 声场双精度浮点类型数据
			  
			  sample = {1/random.random() for i in range(SAMPLE_LEN)} #集合
			  print('initial sample: %d elements' % len(sample))  # 初始化样本: 10500000 elements
			  
			  # complete sample, in case duplicate random numbers were discarded #完整样本，以防重复的随机数被丢弃（严谨）
			  while len(sample) < SAMPLE_LEN:
			      sample.add(1/random.random())
			  
			  print('complete sample: %d elements' % len(sample)) # complete sample: 10500000 elements
			  
			  sample = array.array('d', sample)
			  random.shuffle(sample)  # 用于将一个列表中的元素打乱
			  
			  not_selected = sample[:NEEDLES_LEN // 2]
			  print('not selected: %d samples' % len(not_selected))
			  print('  writing not_selected.arr')
			  with open('not_selected.arr', 'wb') as fp:
			      not_selected.tofile(fp)
			  
			  selected = sample[NEEDLES_LEN // 2:]
			  print('selected: %d samples' % len(selected))
			  print('  writing selected.arr')
			  with open('selected.arr', 'wb') as fp:
			      selected.tofile(fp)

			- 2：测试

			  """
			  Container ``in`` operator performance test
			  """
			  import sys
			  import timeit
			  
			  SETUP = '''
			  import array
			  selected = array.array('d')
			  with open('selected.arr', 'rb') as fp:
			      selected.fromfile(fp, {size})
			  if {container_type} is dict:
			      haystack = dict.fromkeys(selected, 1)
			  else:
			      haystack = {container_type}(selected)
			  if {verbose}:
			      print(type(haystack), end='  ')
			      print('haystack: %10d' % len(haystack), end='  ')
			  needles = array.array('d')
			  with open('not_selected.arr', 'rb') as fp:
			      needles.fromfile(fp, 500)
			  needles.extend(selected[::{size}//500])
			  if {verbose}:
			      print(' needles: %10d' % len(needles), end='  ')
			  '''
			  
			  TEST = '''
			  found = 0
			  for n in needles:
			      if n in haystack:
			          found += 1
			  if {verbose}:
			      print('  found: %10d' % found)
			  '''
			  
			  def test(container_type, verbose):
			      MAX_EXPONENT = 7
			      for n in range(3, MAX_EXPONENT + 1):
			          size = 10**n
			          setup = SETUP.format(container_type=container_type,
			                               size=size, verbose=verbose)
			          test = TEST.format(verbose=verbose)
			          tt = timeit.repeat(stmt=test, setup=setup, repeat=5, number=1)
			          print('|{:{}d}|{:f}'.format(size, MAX_EXPONENT + 1, min(tt)))
			  
			  if __name__=='__main__':
			      if '-v' in sys.argv:
			          sys.argv.remove('-v')
			          verbose = True
			      else:
			          verbose = False
			      if len(sys.argv) != 2:
			          print('Usage: %s <container_type>' % sys.argv[0])
			      else:
			          test(sys.argv[1], verbose)

		- yangoCode

			- 1：基础原理

			  import time
			  from random import randint
			  
			  
			  # 创建测试
			  def make_data(size=1):
			      haystack = {i for i in range( size)}
			      needles_in = {randint(0, size) for i in range(500)}
			      while len(needles_in) < 500:
			          needles_in.add(randint(0, size))
			      needles_not_in = {i for i in range( size, size + 500)}
			      needles = needles_in | needles_not_in
			      return haystack, needles
			  
			  
			  for n in range(3, 8):
			      size = 10 ** n
			      ha, ne = make_data(size)
			      print(len(ha), len(ne))

			- 2：测试1.0

			  import timeit
			  from random import randint
			  from time import perf_counter as pc
			  
			  # 创建测试
			  def make_data(size=1):
			      haystack = {i for i in range( size)}
			      needles_in = {randint(0, size) for i in range(500)}
			      while len(needles_in) < 500:
			          needles_in.add(randint(0, size))
			      needles_not_in = {i for i in range( size, size + 500)}
			      needles = needles_in | needles_not_in
			      return haystack, needles
			  
			  def find_data(haystack,needles):
			      found = 0
			      for n in needles:
			          if n in haystack:
			              found += 1
			  
			  for n in range(3, 8):
			      size = 10 ** n
			      ha, ne = make_data(size)
			      print(len(ha), len(ne))
			      p0=pc()
			      find_data(ha, ne)
			      print(pc()-p0)
			      # cmd="find_data(ha, ne)"
			      # res = timeit.repeat(cmd, setup=SETUP, number=10)
			      # print("耗时：", *('{:.3f}'.format(x) for x in res))

	- 基本概念

		- 基本思想

			- 记录的存储位置与关键字之间存在对应关系
			- 对应关系---------hash函数
			- Loc(i) = H(keyi)
			- 举例

				- 1：直接按照关键字的值 （1,5,7,6,3,4,8）

					- 缺点：空间浪费

				- 2：除法哈希法方法（3,5,7,10000）

					- 目标数和长度计算余数

				- 3：拉链法

			- 查询效率高：如果hash算法ok，查找的次数无限接近于1

		- 相关术语

			- 散列方法

				-  依照函数按关键字计算元素的存储位置，并按此存放。查找时，由同一函数对给定值K计算地址

			- 散列函数

				- hash()  

			- 散列表

				- 按照上述思想构造的表

			- 冲突

				- 不同的关键码映射到同一散列地址

			- 同义词

				- 具有相同函数值的多个关键字

	- 代码实现散列表

		- https://runestone.academy/runestone/books/published/pythonds/SortSearch/Hashing.html

		  """
		  整体思想其实并不难
		  1：主要功能包含：存值、取值。
		  2：丰富：存值得时候调用了hash算法，随便处理了hash冲突
		  3：hash算法：用的是 取余算法
		  4：解决冲突：用的是
		  """
		  
		  
		  class HashTable:
		      def __init__(self):
		          self.size = 11
		          self.slots = [None] * self.size  # 插槽
		          self.data = [None] * self.size  # 数据
		  
		      def put(self, key, data):
		          # 通过 hash 算法，计算出插槽的位置
		          hashvalue = self.hashfunction(key, len(self.slots))
		  
		          if self.slots[hashvalue] == None:
		              # 如果 这个插槽为空
		              self.slots[hashvalue] = key
		              self.data[hashvalue] = data
		          else:
		              # 计算后的hash值和key值相等
		              if self.slots[hashvalue] == key:
		                  self.data[hashvalue] = data  # replace
		              else:
		                  # hash 冲突 通过 重新计算hash值的办法 继续
		                  nextslot = self.rehash(hashvalue, len(self.slots))
		                  while self.slots[nextslot] != None and self.slots[nextslot] != key:
		                      nextslot = self.rehash(nextslot, len(self.slots))
		  
		                  if self.slots[nextslot] == None:
		                      self.slots[nextslot] = key
		                      self.data[nextslot] = data
		                  else:
		                      self.data[nextslot] = data  # replace
		  
		      def hashfunction(self, key, size):
		          """哈希方法，取余"""
		          return key % size
		  
		      def rehash(self, oldhash, size):
		          """解决冲突，重新开地址的方法"""
		          return (oldhash + 1) % size
		  
		      def get(self, key):
		          # 获取的时候也一样，
		          startslot = self.hashfunction(key, len(self.slots))
		  
		          data = None
		          stop = False
		          found = False
		          position = startslot
		          while self.slots[position] != None and not found and not stop:
		              if self.slots[position] == key:
		                  found = True
		                  data = self.data[position]
		              else:
		                  position = self.rehash(position, len(self.slots))
		                  if position == startslot:
		                      stop = True
		          return data
		  
		      def __getitem__(self, key):
		          return self.get(key)
		  
		      def __setitem__(self, key, data):
		          self.put(key, data)
		  
		  
		  H = HashTable()
		  H[54] = "cat"       # 10
		  H[26] = "dog"       # 4
		  H[93] = "lion"      # 5
		  H[17] = "tiger"     # 6
		  H[77] = "bird"      # 0
		  H[31] = "cow"       # 10
		  H[44] = "goat"      # 0
		  H[55] = "pig"       # 0
		  H[20] = "chicken"   # 9
		  print(H.slots)
		  print(H.data)
		  
		  print(H[20])
		  
		  print(H[17])
		  H[20] = 'duck'
		  print(H[20])
		  print(H[99])

		- 自定义实现

		  # 仿造set，设置hash
		  class HashTable:
		      def __init__(self):
		          self.size = 11
		          self.lst = [[] for n in range(self.size)]  # 卡槽
		  
		      def get(self, data):
		          h = self.hs(data)
		          lst = self.lst[h]
		          if data in lst:
		              return True
		          else:
		              return False
		  
		      def put(self, data):
		          h = self.hs(data)
		          lst = self.lst[h]
		          if data not in lst:
		              # 实现集合的去重功能
		              lst.append((data))
		  
		      def hs(self, data):
		          return data % self.size
		  
		  H = HashTable()
		  
		  H.put(54)   # 10
		  H.put(26)   # 4
		  H.put(93)   # 5
		  H.put(17)   # 6
		  H.put(77)   # 0
		  H.put(31)   # 10
		  H.put(44)   # 0
		  H.put(55)   # 0
		  H.put(20)   # 9
		  
		  print(H.get(20))

	- 散列表 PDF:105

		- 字典

			- 稀疏数组

				- 表元

					- 散列表里的单元

				- 每个键值对都 占用一个表元

					- 一个是对键的引用
					- 另一个是对值的引用

				- 所有表元的大小一致

					- 可以通过偏移量来读取某个表元

			-  散列值和相等性 

				- 例如，如果 1 == 1.0 为真，那么 hash(1) == hash(1.0) 也必须为真。

			- 散列表算法 
			- 优缺点

				- 1：键必须是可散列的

					-  支持 hash() 函数，并且通过 __hash__() 方法所得到的散列值是不变的 
					- 支持通过 __eq__() 方法来检测相等性
					- 若 a == b 为真，则 hash(a) == hash(b) 也为真

				- 2： 字典在内存上的开销巨大 

					- 数量巨大建议使用元组

						- 其一是避免了散列表所耗费的空间
						- 其二是无需 把记录中字段的名字在每个元素里都存一遍

				- 3. 键查询很快

					- 典型的空间换时间

				- 4. 键的次序取决于添加顺序 

				  DIAL_CODES = [(86, 'China'), (91, 'India'), (1, 'United States'), (62, 'Indonesia'), (55, 'Brazil'), (92, 'Pakistan'),
				                (880, 'Bangladesh'), (234, 'Nigeria'), (7, 'Russia'), (81, 'Japan'), ]
				  
				  d1 = dict(DIAL_CODES)
				  print('d1:', d1.keys())
				  d2 = dict(sorted(DIAL_CODES))
				  print('d2:', d2.keys())
				  d3 = dict(sorted(DIAL_CODES, key=lambda x: x[1]))
				  print('d3:', d3.keys())
				  assert d1 == d2 and d2 == d3   
				  # d1: dict_keys([86, 91, 1, 62, 55, 92, 880, 234, 7, 81])
				  # d2: dict_keys([1, 7, 55, 62, 81, 86, 91, 92, 234, 880])
				  # d3: dict_keys([880, 55, 86, 91, 62, 81, 234, 92, 7, 1])

					- 断言：assert

					  x=1
					  y=2
					  # 用法，expression2 可选，用来传递具体的异常信息
					  # assert expression1 [",",expression2]
					  
					  # 运行时，加上-O 的参数就可以禁用断言
					  # python -O examp.py
					  
					  # 不要滥用
					  def foo(x):
					      assert(x)
					  
					  foo(1)

				- 5. 往字典里添加新键可能会改变已有键的顺序 

					- 无论何时往字典里添加新的键，Python 解释器都可能做出为字典扩容的决定。扩容导致的 结果就是要新建一个更大的散列表，并把字典里已有的元素添加到新表里。这个过程中可能会发生新的散列冲突，导致新散列表中键的次序变化

						- 不要对字典同时进行迭代和修改。

							- 列表迭代删除也需要注意

							  lista=[1,2,3,4]
							  for i in lista:
							      lista.remove(i)
							  print(lista)

		- 集合

			- 提到的字典和散列表的几个特点，对集合来说几乎都是适用的
			- • 集合里的元素必须是可散列的。
			-  • 集合很消耗内存。
			-  • 可以很高效地判断元素是否存在于某个集合。
			-  • 元素的次序取决于被添加到集合里的次序。
			-  • 往集合里添加元素，可能会改变集合里已有元素的次序。 

		- 本节目标答案

			- • Python 里的 dict 和 set 的效率有多高？

				- 效率demo

			-  • 为什么它们是无序的？ 

				- hash算法+扩容重排

			-  • 为什么不应该在迭代循环 dict 或是 set 的同时往里添加元素？

				- 扩容的时候可能会发生散列冲突、进而导致散列表中键的次序变化

			- • 为什么 dict 的键和 set 元素的顺序是跟据它们被添加的次序而定的，以及为什么在映射对象的生命周期中，这个顺序并不是一成不变的？
			- • 为什么并不是所有的 Python 对象都可以当作 dict 的键或 set 里的元素？ 

				- 可散列的

- 本章小结

	- 字典

		- 除了基本的 dict 之外，标准库还提供现成且好用的特殊 映射类型，这些映射类型都属于 collections 模块，这个模块还提供了便于扩展的 UserDict 类。

			- defaultdict
			- OrderedDict
			- ChainMap 
			- Counter
			- UserDict 

	- 映射类型常用的方法

		- setdefault 

			- setdefault 方法可 以用来更新字典里存放的可变值（比如列表），从而避免了重复的键搜索

		- update

			- 让批量更新成为可能，它可以用来插入新值或者更新已有键值对

		- __missing__

			- 当对象找不到某个键的时候，可以通过这个方法自定义会发生什么。

	- 散列表

		- 原理
		- 代码

### 第4章 文本和字节序列

- 本章将讨论

	-  • 字符、码位和字节表述 
	-  • bytes、bytearray 和 memoryview 等二进制序列的独特特性 
	-  • 全部 Unicode 和陈旧字符集的编解码器 
	-  • 避免和处理编码错误 
	-  • 处理文本文件的最佳实践 
	-  • 默认编码的陷阱和标准 I/O 的问题 
	-  • 规范化 Unicode 文本，进行安全的比较
	-  • 规范化、大小写折叠和暴力移除音调符号的实用函数 
	-  • 使用 locale 模块和 PyUCA 库正确地排序 Unicode 文本 
	-  • Unicode 数据库中的字符元数据 
	-  • 能处理字符串和字节序列的双模式 API

- 字符、码位和字节表述

	- 基础准备

		- 字符编码

		  将 英文字母 + 数字 + 标点符号 （可见字符95） + 换行 + 回车 （控制字符） 进行编码
		  
		  码位  0  1  ...... 10 ...... 65  ...... 99 
		  解释 标题开始      换行     A      a
		  以上 这些 称作：ASCII字符集
		  ASCII码 00000000 。。。。。。。。。。。。。。。 01111111
		  扩展ASCII码                  11111111
		  GB2312
		  GBK
		  GB18030 
		  ----------------------------------------------------
		  Unicode
		  UTF-8

	- 字符的编码与解码

	  s = 'café'
	  
	  # --------编码----开始--------
	  b = s.encode('utf-8')
	  print(b)  # b'caf\xc3\xa9'
	  
	  s2 = "hello"
	  b2 = s2.encode("ASCII")
	  print(b2)
	  
	  # --------编码--ASCII码--失败--------
	  # b=s.encode("ASCII")
	  # print(b)
	  """
	  UnicodeEncodeError: 'ascii' codec can't encode character '\xe9' in position 3: ordinal not in range(128)
	  ASCII码 中 无法编码  '\xe9' ，因为 它不在（0,128）之间
	  # 通过utf-8 解码得出b'caf\xc3\xa9' ，
	  é  这个特殊符号在 ASCII字符集 中不存在。
	  """
	  # --------编码----结束--------
	  
	  # --------解码----开始--------
	  # 1:正常用某种编码格式编码，就应该用相应的格式解码
	  s2 = "hello"
	  b2 = s2.encode("ASCII")
	  s3 = b2.decode("ASCII")
	  print(b2, s3)
	  # 2:用另外一种格式解码
	  s4 = b2.decode("utf-8")
	  print(b2, s3, s4)
	  
	  # 3:但是
	  s3 = '国标'
	  b3 = s3.encode("utf-8")
	  s4 = b3.decode("utf-8")
	  s5 = b3.decode("utf-16")
	  print(b3, s4,s5 )  #
	  
	  # --------解码----结束--------

		- 把字节序列变成人类可读的文本字符串就是解码
		- 把字符串变成用于 存储或传输的字节序列就是编码。

	- 字节概要

	  # 获取字节bytes对象
	  s = 'café'
	  # 1：把字符串转成字节对象
	  b1 = bytes(s, encoding="utf-8")
	  print(b1, len(b1))
	  print(b1[1], b1[4], hex(169))  # 各个元素是介于 0 - 255 之间的整数
	  # 2：用 utf-16 解码
	  b2 = bytes(s, encoding="utf-16")
	  print(b2, len(b2))
	  print(b2[0], b2[1], b2[2], b2[3], b2[4], b2[5], b2[6], b2[7], b2[8], b2[9])
	  # 3: 二进制序列的切片始终是同一类型的二进制序列
	  print(b1[:1], b1[3:4], b1[3:5])
	  
	  # 获取字节bytearray对象
	  s = 'café'
	  b1 = bytes(s, encoding="utf-8")
	  b_arr = bytearray(b1)
	  print(b_arr, b_arr[:1], b1[3:4], b1[3:5])

- 结构体和内存视图

  import struct
  
  fmt = '<3s3sHH' #结构体的格式：<是小字节序，3s3s 两个3字节序列，HH 是两个16位二进制整数
  with open('filter.gif', 'rb') as fp:
      img = memoryview(fp.read())
  header = img[:10] # 这里通过贴片再创建一个memoryview对象，不会复制字节序列
  print(bytes(header))  # b'GIF89a\xcd\x04{\x01'
  print(struct.unpack(fmt,header))
  del header
  del img

	- struct 模块

		- 字节序列转换成不同类型字段组成的元组
		- 一些函数用于执行反向转换
		- 元组转换成打包的字节序列
		- 能处理 对象

			- bytes
			-  bytearray 
			- memoryview 

- 基本的编解码器

  for codec in ['latin_1', 'utf_8', 'utf_16']:
      print(codec, 'El Niño'.encode(codec), sep='\t')
  
  # latin_1  b'El Ni\xf1o'
  # utf_8        b'El Ni\xc3\xb1o'
  # utf_16   b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'
  
  # 编码错误
  print("----------编码错误-----------")
  city = 'São Paulo'
  print(city.encode('utf_8'))
  print(city.encode('utf_16'))
  print(city.encode('iso8859_1'))
  # print(city.encode('cp437'))
  print(city.encode('cp437',errors='ignore')) #  忽略错误，直接跳过
  print(city.encode('cp437',errors='replace')) # 将无法转换的字符 替换成“？”
  print(city.encode('cp437',errors='xmlcharrefreplace')) # 将无法编码的字符替换成XML实体
  
  # 解码错误
  print("----------解码错误-----------")
  octets = b'Montr\xe9al'
  print(octets.decode('cp1252'))
  print(octets.decode('iso8859_7'))
  print(octets.decode('koi8_r'))
  # print(octets.decode('utf_8'))
  print(octets.decode('utf_8',errors='replace'))

	- 自带了超过 100 种编解码器

		- 每个编解码器都有一个名称，如 'utf_8'，而且经常有几个别名，如 'utf8'、'utf8' 和 'U8'。

	- 乱码 PDF 117 图表值得一看

- 了解编解码问题

  city = 'São Paulo'
  # 编码时候
  print(city.encode("U8"))
  print(city.encode("utf_16"))
  print(city.encode("iso8859_1"))
  # print(city.encode("ascii")) # 出错
  print(city.encode("ascii",errors="ignore")) # 出错 直接忽略
  print(city.encode("ascii",errors="replace")) # 出错 替换 ？
  print(city.encode("ascii",errors='xmlcharrefreplace')) # 出错 替换 把无法编码的字符替换成 XML 实体
  
  # 解码时候
  city_b = b'S\xc3\xa3o Paulo'
  print(city_b.decode("utf-8"))
  print(city_b.decode("utf_16"))    # 乱码
  print(city_b.decode("iso8859_1"))
  # print(city_b.decode("ascii")) # 出错
  print(city_b.decode("ascii",errors="ignore")) # 出错 直接忽略
  print(city_b.decode("ascii",errors="replace")) # 出错 替换 ？
  print(city_b.decode("ascii",errors='xmlcharrefreplace')) # 出错 替换 把无法编码的字符替换成 XML 实体

	- 　处理UnicodeEncodeError（编码问题） 
	- 　处理UnicodeDecodeError （解码问题）

- 如何找出字节序列的编码 

  # 用chardet检测字符编码
  # pip install chardet
  
  import chardet
  
  print(chardet.detect('São Paulo'.encode("U8")))  # 这个其实是utf-8 编译生成
  print(chardet.detect('São Paulo'.encode("utf-16")))
  print(chardet.detect(b'S\xe3o Paulo'))
  
  data = '离离原上草，一岁一枯荣'.encode('gbk')
  print(chardet.detect(data))
  # 注意到GBK是GB2312的超集，两者是同一种编码，检测正确的概率是74%，language字段指出的语言是’Chinese’。

- 字节序标识

  """
  计算机硬件有两种储存数据的方式：大端字节序（big endian）和小端字节序（little endian）。
  举例来说，数值0x2211使用两个字节储存：高位字节是0x22，低位字节是0x11。
  大端字节序：高位字节在前，低位字节在后，这是人类读写数值的方法。
  小端字节序：低位字节在前，高位字节在后，即以0x1122形式储存。
  首先，为什么会有小端字节序？
  
  答案是，计算机电路先处理低位字节，效率比较高，因为计算都是从低位开始的。所以，计算机的内部处理都是小端字节序。
  
  但是，人类还是习惯读写大端字节序。所以，除了计算机的内部处理，其他的场合几乎都是大端字节序，比如网络传输和文件储存。
  计算机处理字节序的时候，不知道什么是高位字节，什么是低位字节。它只知道按顺序读取字节，先读第一个字节，再读第二个字节。
  如果是大端字节序，先读到的就是高位字节，后读到的就是低位字节。小端字节序正好相反。
  理解这一点，才能理解计算机如何处理字节序。
  
  字节序的处理，就是一句话：:"只有读取的时候，才必须区分字节序，其他情况都不用考虑。"
  """
  
  u16 = 'El Niño'.encode('utf_16')
  print(u16)
  # b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'
  """
  \xff\xfe 这就是BOM即 byte-order mark 字节序标记：指明编码时使用InterlCPU的小字节序
  """
  print(list(u16))
  
  u16le = 'El Niño'.encode('utf_16le')
  u16be = 'El Niño'.encode('utf_16be')
  print(list(u16le))
  print(list(u16be))

- 处理文本文件 

	- codeView

	  """
	  要尽早把输入（例 如读取文件时）的字节序列解码成字符串。
	  这种三明治中的“肉片”是程序的业务逻辑， 在这里只能处理字符串对象。
	  在其他处理过程中，一定不能编码或解码。
	  对输出来说，则 要尽量晚地把字符串编码成字节序列。
	  """
	  
	  fp = open('cafe.txt', 'w', encoding="U8").write('café')
	  print(fp)  # 4
	  fp1=open('cafe.txt').read()
	  print(fp1,len(fp1))  # caf茅
	  fp2=open('cafe.txt', encoding="U8").read()
	  print(fp2,len(fp2))  # café
	  
	  """
	  证明：为什么写入的时候是4个字符，读取的时候用了5个字符？？？？？
	  fp=open("文件名",'w',encoding="编码")
	  """
	  print("------------------------------")
	  # 01-写入文件
	  fp = open('cafe.txt','w',encoding="U8")
	  print(fp.write('café'))   #4
	  fp.close()
	  
	  # os.stat() 方法用于在给定的路径上执行一个系统 stat 的调用。
	  import os
	  ooss=os.stat('cafe.txt')
	  print(ooss.st_size)   #5  原因是：UTF-8 编码的 'é' 占两个字节，0xc3 和 0xa9。
	  
	  # 读取的时候不指定编码
	  fp2=open('cafe.txt')
	  print(fp2.encoding)
	  print(fp2.read())
	  
	  # 以指定编码打开文件
	  fp3 = open("cafe.txt",encoding="utf-8")
	  print(fp3.read())
	  
	  
	  # 以二进制模式读取文件
	  fp4= open('cafe.txt','rb')
	  print(fp4.read())

	- 参考博客

	  https://www.cnblogs.com/YK2012/p/9719684.html

- 为了正确比较而规范化Unicode字符串

  '''
  因为Unicode有组合字符（变音符号+附加到前一个字符上的记号）
  '''
  s1 = 'café' # 把"e"和重音符组合在一起
  s2 = 'cafe\u0301' # 分解成"e"和重音符
  
  print(s1, s2) # café café
  print("叶徒相似其实味不同")
  print("在 Unicode 标准中，'é' 和 'e\u0301' 这样的序列叫“标准等价物”（canonical equivalent），"
     "应用程序应该把它们视作 相同的字符。但是，Python 看到的是不同的码位序列，因此判定二者不相等。")
  print(len(s1), len(s2))
  print(s1 == s2)
  
  # ---------------Unicode 规范化-----------------
  # NFC（Normalization Form C）使用最少的码位构成等价的字符串，
  # 而 NFD 把组合字符分 解成基字符和单独的组合字符。
  # 这两种规范化方式都能让比较行为符合预期：
  from unicodedata import normalize
  
  print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
  print(normalize('NFC', s1) == normalize('NFC', s2))
  print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))
  print(normalize('NFD', s1) == normalize('NFD', s2))
  
  # ---------------有些单字符会被规范成另一个单字符----------------
  # 电阻的单位欧姆（Ω）会被 规范成希腊字母大写的欧米加。
  # 这两个字符在视觉上是一样的，但是比较时并不相等
  
  from unicodedata import normalize, name
  
  ohm = '\u2126'
  print(ohm, name(ohm)) # Ω
  ohm_c = normalize('NFC', ohm)
  print(ohm_c, name(ohm_c)) # Ω
  print(len(normalize('NFC', ohm_c)), len(normalize('NFC', ohm)))
  print(normalize('NFC', ohm_c) == normalize('NFC', ohm))
  
  # --------------------在 NFKC 和 NFKD 形式中，各个兼容字符会被替换成一个或多个“兼容分解”字符------------------------------
  # 二分之一 '½'（U+00BD）经过兼容分解后得到 的是三个字符序列 '1/2'；
  # 微符号 'µ'（U+00B5）经过兼容分解后得到的是小写字母 'μ' （U+03BC）。
  half = '½'
  print(normalize('NFC', half))
  four_squared = '4²'
  print(normalize('NFKC', four_squared))
  micro = 'µ'
  print(normalize('NFKC', micro))

	- 大小写折叠 

	  '''
	  大小写折叠其实就是把所有文本变成小写，再做些其他转换。
	  这个功能由 str.casefold() 方法（Python 3.3 新增）支持。
	  '''
	  from unicodedata import name
	  
	  micro = 'µ'
	  print(micro,name(micro))
	  micro_cf = micro.casefold()
	  print(micro_cf,name(micro_cf))
	  micro_lo = micro.lower()
	  print(micro_lo,name(micro_lo))
	  print(micro,micro_cf,micro_lo)
	  
	  eszett = 'ß'
	  print(eszett,name(eszett))
	  eszett_cf = eszett.casefold()
	  print(eszett_cf,)
	  eszett_lo = eszett.lower()
	  print(eszett_lo,name(eszett_lo))
	  print(eszett,eszett_cf,eszett_lo)

	- 规范化文本匹配实用函数 

	  '''
	   nfc_equal 和 fold_equal 函数。
	  '''
	  from unicodedata import name, normalize
	  
	  
	  def nfc_equal(str1, str2):
	      return normalize('NFC', str1) == normalize('NFC', str2)
	  
	  
	  def fold_equal(str1, str2):
	      return (normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold())
	  
	  
	  s1 = 'café'
	  s2 = 'cafe\u0301'
	  print(s1 == s2, nfc_equal(s1, s2), fold_equal(s1, s2))
	  s3 = 'Straße'
	  s4 = 'strasse'
	  print(s3 == s4, nfc_equal(s3, s4), fold_equal(s3, s4))

	- 极端“规范化”：去掉变音符号 

	  '''
	   nfc_equal 和 fold_equal 函数。
	  '''
	  import unicodedata
	  from unicodedata import name, normalize
	  import string
	  
	  
	  def nfc_equal(str1, str2):
	      return normalize('NFC', str1) == normalize('NFC', str2)
	  
	  
	  def fold_equal(str1, str2):
	      return (normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold())
	  
	  
	  s1 = 'café'
	  s2 = 'cafe\u0301'
	  print(s1 == s2, nfc_equal(s1, s2), fold_equal(s1, s2))
	  s3 = 'Straße'
	  s4 = 'strasse'
	  print(s3 == s4, nfc_equal(s3, s4), fold_equal(s3, s4))
	  
	  """#####################去掉变音符号############################"""
	  
	  
	  def shave_marks(txt):
	      """去掉全部变音符号"""
	      norm_txt = unicodedata.normalize('NFD', txt)  # 把所有字符分解成：基字符 和 组合记号
	      shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))  # 过滤掉所有的组合记号
	      return unicodedata.normalize('NFC', shaved)  # 重组所有字符
	  
	  
	  order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
	  # ------’“Herr Voß: • ½ cup of Œtker™ caffe latte • bowl of acai.”‘
	  print(shave_marks(order))
	  Greek = 'Zέφupoς, Zéfiro'
	  # -----'Zεφupoς, Zefiro'
	  print(shave_marks(Greek))
	  
	  """#####################删除拉丁字母中组合记号的函数############################"""
	  
	  
	  def shave_marks_latin(txt):
	      """把拉丁基字符中所有的变音符号删除"""
	      norm_txt = unicodedata.normalize('NFD', txt)
	      latin_base = False
	      keepers = []
	      for c in norm_txt:
	          if unicodedata.combining(c) and latin_base:
	              continue  # 忽略拉丁基字符上的变音符号
	          keepers.append(c)
	          # 如果不是组合字符，那就是新的基字符
	          if not unicodedata.combining(c):
	              latin_base = c in string.ascii_letters
	      shaved = ''.join(keepers)
	      return unicodedata.normalize('NFC', shaved)
	  
	  
	  print(Greek, shave_marks_latin(Greek), shave_marks(Greek), shave_marks_latin(Greek) == shave_marks(Greek))
	  # Zέφupoς, Zéfiro # Zέφupoς, Zefiro # Zεφupoς, Zefiro # False
	  
	  """#####################西文印刷字符转换成ASCII 字符############################"""
	  
	  single_map = str.maketrans(""",ƒ,,†ˆ‹‘’“” •––˜›""",
	                             """'f"*^<''""---~>""")
	  multi_map = str.maketrans({
	      '€': '<euro>',
	      '…': '...',
	      'Œ': 'OE',
	      '™': '(TM)',
	      'œ': 'oe',
	      '‰': '<per mille>',
	      '‡': '**', })
	  multi_map.update(single_map)  # 合并两个映射表
	  
	  
	  def dewinize(txt):
	      """把Win1252符号替换成ASCII字符或序列"""
	      return txt.translate(multi_map)
	  
	  
	  def asciize(txt):
	      no_marks = shave_marks_latin(dewinize(txt))
	      no_marks = no_marks.replace('ß', 'ss')
	      return unicodedata.normalize('NFKC', no_marks)
	  
	  
	  print(dewinize(order))
	  print(asciize(order))

- Unicode文本排序

  """
  Unicode文本排序
  """
  fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
  
  # 非 ASCII 文本的标准排序方式是使用 locale.strxfrm 函数,“把字符串转换成适合所在区域进行比较的形式”。
  
  # ---------------------使用 locale.strxfrm 函数做排序键--------------------
  import locale
  
  locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
  print(sorted(fruits))
  print(sorted(fruits, key=locale.strxfrm))  # 因此，使用 locale.strxfrm 函数做排序键之前，要调用 setlocale(LC_COLLATE, «your_locale»)。
  
  # ---------------------使用Unicode排序算法排序-------------------
  import pyuca
  coll = pyuca.Collator()
  print(sorted(fruits, key=coll.sort_key))

- Unicode数据库

  """
  Unicode 标准提供了一个完整的数据库，不仅包括码位与字符名称之间的映射，还有各个字符的元数据，以及字符之间的关系。
  例如，Unicode 数据库 记录了字符是否可以打印、是不是字母、是不是数字，或者是不是其他数值符号。
  字符串 的 isidentifier、isprintable、isdecimal 和 isnumeric 等方法就是靠这些信息作判断的。
  """
  import unicodedata
  import re
  
  re_digit = re.compile(r'\d')
  
  sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'
  
  for char in sample:
      print('U+%04x' % ord(char),                         # U+0000 格式的码位
            char.center(6),                               # 在长度为 6 的字符串中居中显示字符。
            're_dig' if re_digit.match(char) else '-',    # re_dig 表示字符匹配正则表达式 r'\d'
            'isdig' if char.isdigit() else '-',
            'isnum' if char.isnumeric() else '-',
            format(unicodedata.numeric(char), '5.2f'),
            unicodedata.name(char),
            sep='\t')
  
  """
  1：正则表达式r'\d' 能匹配数字“1”和梵文数字3，但是不能匹配isdigit 方法判断为数字的其他字符。
  
  """

- 支持字符串和字节序列的双模式API

	- 正则表达式中的字符串和字节序列 

## 第三部分（把函数视作对象）

### 第5章 一等函数

- 一等对象

  def funa(n):
      ''' 返回 n！'''
      return 1 if n<2 else n * funa(n-1)
  
  print(funa(42))
  print(funa.__doc__)
  print(type(funa))
  
  # 验证函数对象的一等本性
  
  # • 在运行时创建
  # • 能赋值给变量或数据结构中的元素
  fact=funa
  print(fact)
  # • 能作为参数传给函数
  map(funa,range(3))
  # • 能作为函数的返回结果
  def get_funa():
      return funa
  print(get_funa()(2))

	- 运行时创建
	- 能赋值给变量或数据结构中的元素
	- 能作为参数传递给函数
	- 能作为函数的返回结果
	- 整数、字符串、字典

- 高阶函数

	- 接受     函数为参数，或者把函数作为结果返回的函数是高阶函数
	- map、filter、reduce 

		- 替代

		  # 高阶函数的替代品
		  # 在 Python 3 中，map 和 filter 返回生成器（一种迭代器），因此现在它们的直接替代品是 生成器表达式
		  from functools import reduce
		  from operator import add
		  
		  
		  def factorial(n):
		      return 1 if n < 2 else factorial(n - 1) * n
		  
		  
		  # 求出 1-6 的阶乘
		  print(list(map(factorial, range(6))))
		  print([factorial(i) for i in range(6)])
		  
		  # 求出 1-6 之间 偶数的阶乘
		  print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
		  print([factorial(i) for i in range(6) if i % 2])
		  
		  # reduce() 函数会对参数序列中元素进行累积。
		  # 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数
		  # function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
		  # reduce() 函数语法：reduce(function, iterable[, initializer])
		  
		  # 累计求和 （1-100）
		  print(reduce(add,range(100)))
		  print(sum(range(100)))

- 可调用对象

	- 如果想判断对象能 否调用，可以使用内置的 callable() 函数
	- 7种可调用对象

		- 1 用户定义的函数
		- 2 内置函数
		- 3 内置方法
		- 4 方法
		- 5 类
		- 6 类的实例
		- 7 生成器函数

- 用户定义的可调用类型

  # 实现了 BingoCage 类。这个类的实例使用任何可迭代对象构建，而且会在内部存 储一个随机顺序排列的列表。
  import random
  
  
  class BingoCage:
      def __init__(self, items):
          self._items = list(items)  # 接受可迭代对象，在本地构建副本
          random.shuffle(self._items)  # 打乱次序
  
      def pick(self):
          try:
              return self._items.pop()  # 删除数据，防止重复获取
          except IndexError:
              raise LookupError('列表内容为空！')
  
      def __call__(self, *args, **kwargs):
          return self.pick()
  
  
  bingo = BingoCage(range(3))
  print(bingo.pick())
  print(bingo())
  print(callable(bingo))
  print(bingo())
  # print(bingo()) 再调报错

- 函数内省

  def factorial(n):
      return 1 if n < 2 else factorial(n - 1) * n
  
  
  print(dir(factorial))
  # ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__',
  # '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__',
  # '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__',
  # '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
  # '__subclasshook__']
  
  factorial.short_description = 'short_Name'
  factorial.long_description = 'long_Name'
  print(factorial.__dict__)
  
  
  # 列出常规对象没有而函数有的属性
  class C: pass
  
  
  obj = C()
  
  
  def func(): pass
  
  
  print(sorted(set(dir(func)) - set(dir(obj))))
  # 详细说明 见PDF155
  # ['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']

- 从定位参数到仅限关键字参数

  def tag(name, *content, cls=None, **attrs):
      "生成一个或多个html标签"
      if cls is not None:
          attrs["class"] = cls
  
      if attrs:
          attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
      else:
          attr_str = ''
  
      if content:
          return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
      else:
          return '<%s%s />' % (name, attr_str)
  
  
  print(tag('br'))  # 自闭标签(无内容)
  print(tag('p', 'hello'))  #
  print(tag('p', 'hello world !', "I'm Yango !"))  # 第一个参数后面的人一个参数会被*content捕获，存入一个元组
  print(tag('p', 'hello', id=33))
  print(tag('p', "带有类名的P标签", cls="namedP"))
  my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
  
  print(tag(**my_tag))

- 获取关于参数的信息

  import bobo
  
  @bobo.query('/')
  def hello(person):
      return 'Hello %s!' %person

	- 运行方式

		- # bobo -f 3-2.py # 运行方式
		- # http://localhost:8080/?person=yango

- 支持函数式编程的包

	- 计算阶乘

### 第6章 使用一等函数实现设计模式

- 重构“策略”模式

	- 经典的“策略”模式  6-2

	  # 上下文：把计算委托给实现不同算法的可互换组件，它提供服务。上下文是Order，它会根据不同的算法计算促销折扣
	  # 策略：实现不同算法的组件共同的接口
	  #       策略1：有 1000 或以上积分的顾客，每个订单享 5% 折扣
	  #       策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
	  #       策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  # 具体策略：策略的具体子类。
	  
	  from abc import ABC, abstractmethod
	  from collections import namedtuple
	  
	  Customer = namedtuple("Customer", "name fidelity")  # 通过具名元组定义一个”顾客“类型，包含【顾客名称、顾客积分】
	  
	  
	  class LineItem:
	      """定义清单明细"""
	  
	      def __init__(self, product, quantity, price):
	          self.product = product  # 物品
	          self.quantity = quantity  # 数量
	          self.price = price  # 单价
	  
	      def total(self):
	          """明细价格：价格*数量"""
	          return self.price * self.quantity
	  
	  
	  class Order:
	      """订单信息"""
	  
	      def __init__(self, customer, cart, promotion):
	          self.customer = customer  # 顾客
	          self.cart = list(cart)  # 购物车
	          self.promotion = promotion  # 折扣策略
	  
	      def total(self):
	          """总价格（未打折）= 购物车中明细价格之和"""
	          if not hasattr(self, '__total'):
	              return sum(item.total() for item in self.cart)
	          return self.__total
	  
	      def due(self):
	          """最终价格/确定价格 总价格-折扣价格"""
	          if self.promotion is None:
	              discount = 0
	          else:
	              discount = self.promotion.discount(self)
	          return self.total() - discount
	  
	      def __repr__(self):
	          fmt = '<Order total:{:.2f} due:{:.2f}>'
	          return fmt.format(self.total(), self.due())
	  
	  
	  class Promotion(ABC):
	      """策略，抽象基类"""
	  
	      @abstractmethod
	      def discount(self, order):
	          """返回折扣金额（正值）"""
	  
	  
	  class FidelityPromo(Promotion):
	      def discount(self, order):
	          # 策略1：有 1000 或以上积分的顾客，每个订单享 5% 折扣
	          return order.total() * .05 if order.customer.fidelity > 1000 else 0
	  
	  
	  class BulkItemPromo(Promotion):
	      def discount(self, order):
	          # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
	          discout = 0
	          for item in order.cart:
	              if item.quantity >= 20:
	                  discout += item.total() * .1
	          return discout
	  
	  
	  class LargeOrderPromo(Promotion):
	      def discount(self, order):
	          # 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	          # return order.total() * .07 if len(order.cart) >= 10 else 0
	          distinct_items = {item.product for item in order.cart}
	          if len(distinct_items) >= 10:
	              return order.total() * .07
	          return 0
	  
	  # 两个顾客：joe 的积分是 0，ann 的积分是 1100。
	  
	  joe = Customer('John Doe', 0)
	  ann = Customer('Ann Smith', 1100)
	  cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermellon', 5, 5.0)]
	  print(Order(joe, cart, FidelityPromo())) # <Order total:42.00 due:42.00> 不打折
	  print(Order(ann, cart, FidelityPromo())) # <Order total:42.00 due:39.90> 策略1：有 1000 或以上积分的顾客，每个订单享 5% 折扣
	  banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
	  print(Order(joe, banana_cart, BulkItemPromo())) #<Order total:30.00 due:28.50> # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
	  long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
	  print(Order(joe, long_order, LargeOrderPromo())) #<Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  print(Order(joe, cart, LargeOrderPromo()))

	- 使用函数实现“策略”模式 6-3

	  # 优化6-2 没必要在新建订单时实例化新的促销对象，函数拿来即用
	  # 上下文：把计算委托给实现不同算法的可互换组件，它提供服务。上下文是Order，它会根据不同的算法计算促销折扣
	  # 策略：实现不同算法的组件共同的接口
	  #       策略1：有 1000 或以上积分的顾客，每个订单享 5% 折扣
	  #       策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
	  #       策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  # 具体策略：策略的具体子类。
	  
	  # from abc import ABC, abstractmethod
	  from collections import namedtuple
	  
	  Customer = namedtuple("Customer", "name fidelity")  # 通过具名元组定义一个”顾客“类型，包含【顾客名称、顾客积分】
	  
	  
	  class LineItem:
	      """定义清单明细"""
	  
	      def __init__(self, product, quantity, price):
	          self.product = product  # 物品
	          self.quantity = quantity  # 数量
	          self.price = price  # 单价
	  
	      def total(self):
	          """明细价格：价格*数量"""
	          return self.price * self.quantity
	  
	  
	  class Order:
	      """订单信息"""
	  
	      def __init__(self, customer, cart, promotion):
	          self.customer = customer  # 顾客
	          self.cart = list(cart)  # 购物车
	          self.promotion = promotion  # 折扣策略
	  
	      def total(self):
	          """总价格（未打折）= 购物车中明细价格之和"""
	          if not hasattr(self, '__total'):
	              return sum(item.total() for item in self.cart)
	          return self.__total
	  
	      def due(self):
	          """最终价格/确定价格 总价格-折扣价格"""
	          if self.promotion is None:
	              discount = 0
	          else:
	              discount = self.promotion(self)
	          return self.total() - discount
	  
	      def __repr__(self):
	          fmt = '<Order total:{:.2f} due:{:.2f}>'
	          return fmt.format(self.total(), self.due())
	  
	  def fidelity_promo(order):
	      # 策略1：有 1000 或以上积分的顾客，每个订单享 5% 折扣
	      return order.total() * .05 if order.customer.fidelity > 1000 else 0
	  
	  def bulk_item_promo(order):
	      # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
	      discout = 0
	      for item in order.cart:
	          if item.quantity >= 20:
	              discout += item.total() * .1
	      return discout
	  
	  def large_order_promo(order):
	      # 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	      # return order.total() * .07 if len(order.cart) >= 10 else 0
	      distinct_items = {item.product for item in order.cart}
	      if len(distinct_items) >= 10:
	          return order.total() * .07
	      return 0
	  
	  
	  # 两个顾客：joe 的积分是 0，ann 的积分是 1100。
	  
	  joe = Customer('John Doe', 0)
	  ann = Customer('Ann Smith', 1100)
	  cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermellon', 5, 5.0)]
	  print(Order(joe, cart, fidelity_promo))  # <Order total:42.00 due:42.00> 不打折
	  print(Order(ann, cart, fidelity_promo))  # <Order total:42.00 due:39.90> 策略1：有 1000 或以上积分的顾客，每个订单享 5% 折扣
	  banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
	  print(Order(joe, banana_cart, bulk_item_promo))  # <Order total:30.00 due:28.50> # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
	  long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
	  print(Order(joe, long_order, large_order_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  print(Order(joe, cart, large_order_promo))

	- 选择最佳策略：简单的方式  6-6

	  # 找到最优的优惠方案
	  # 上下文：把计算委托给实现不同算法的可互换组件，它提供服务。上下文是Order，它会根据不同的算法计算促销折扣
	  # 策略：实现不同算法的组件共同的接口
	  #       策略1：有 1000 或以上积分的顾客，每个订单享 5% 折扣
	  #       策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
	  #       策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  # 具体策略：策略的具体子类。
	  
	  # from abc import ABC, abstractmethod
	  from collections import namedtuple
	  
	  Customer = namedtuple("Customer", "name fidelity")  # 通过具名元组定义一个”顾客“类型，包含【顾客名称、顾客积分】
	  
	  
	  class LineItem:
	      """定义清单明细"""
	  
	      def __init__(self, product, quantity, price):
	          self.product = product  # 物品
	          self.quantity = quantity  # 数量
	          self.price = price  # 单价
	  
	      def total(self):
	          """明细价格：价格*数量"""
	          return self.price * self.quantity
	  
	  
	  class Order:
	      """订单信息"""
	  
	      def __init__(self, customer, cart, promotion):
	          self.customer = customer  # 顾客
	          self.cart = list(cart)  # 购物车
	          self.promotion = promotion  # 折扣策略
	  
	      def total(self):
	          """总价格（未打折）= 购物车中明细价格之和"""
	          if not hasattr(self, '__total'):
	              return sum(item.total() for item in self.cart)
	          return self.__total
	  
	      def due(self):
	          """最终价格/确定价格 总价格-折扣价格"""
	          if self.promotion is None:
	              discount = 0
	          else:
	              discount = self.promotion(self)
	          return self.total() - discount
	  
	      def __repr__(self):
	          fmt = '<Order total:{:.2f} due:{:.2f}>'
	          return fmt.format(self.total(), self.due())
	  
	  
	  def fidelity_promo(order):
	      # 策略1：有 1000 或以上积分的顾客，每个订单享 5% 折扣
	      return order.total() * .05 if order.customer.fidelity > 1000 else 0
	  
	  
	  def bulk_item_promo(order):
	      # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
	      discout = 0
	      for item in order.cart:
	          if item.quantity >= 20:
	              discout += item.total() * .1
	      return discout
	  
	  
	  def large_order_promo(order):
	      # 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	      # return order.total() * .07 if len(order.cart) >= 10 else 0
	      distinct_items = {item.product for item in order.cart}
	      if len(distinct_items) >= 10:
	          return order.total() * .07
	      return 0
	  
	  
	  def best_promo(order):
	      """
	      选择最优的折扣方案
	      :param order: 订单
	      :return: 最优解
	      """
	      promos = [fidelity_promo, bulk_item_promo, large_order_promo]  # 列出函数实现的各个策略
	      return max(promo(order) for promo in promos)
	  
	  
	  # 两个顾客：joe 的积分是 0，ann 的积分是 1100。
	  joe = Customer('John Doe', 0)
	  ann = Customer('Ann Smith', 1100)
	  # 三种购物车
	  cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermellon', 5, 5.0)]
	  banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
	  long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
	  
	  print("------------joe的选择（普通购物车）------------")
	  print(Order(joe, cart, fidelity_promo))  # <Order total:42.00 due:42.00> 不打折
	  print(Order(joe, cart, bulk_item_promo))  # <Order total:30.00 due:28.50> # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
	  print(Order(joe, cart, large_order_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  print(Order(joe, cart, best_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  print("------------ann的选择（普通购物车）------------")
	  print(Order(ann, cart, fidelity_promo))  # <Order total:42.00 due:42.00> 不打折
	  print(Order(ann, cart, bulk_item_promo))  # <Order total:30.00 due:28.50> # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
	  print(Order(ann, cart, large_order_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  print(Order(ann, cart, best_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  print("------------joe的选择（香蕉购物车）------------")
	  print(Order(joe, banana_cart, fidelity_promo))  # <Order total:42.00 due:42.00> 不打折
	  print(Order(joe, banana_cart, bulk_item_promo))  # <Order total:30.00 due:28.50> # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
	  print(Order(joe, banana_cart, large_order_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  print(Order(joe, banana_cart, best_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  print("------------joe的选择（长订单购物车）------------")
	  print(Order(joe, long_order, fidelity_promo))  # <Order total:42.00 due:42.00> 不打折
	  print(Order(joe, long_order, bulk_item_promo))  # <Order total:30.00 due:28.50> # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
	  print(Order(joe, long_order, large_order_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  print(Order(joe, long_order, best_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣

	- 选择最佳策略：灵活的方式 6-8

	  #  6-6 的有一个缺陷：若添加新的促销策略，要定义相应的函数，需要及得把它添加到 promos 列表中。否则 best_promo 不会考虑它
	  #  globals() 返回一个字典，表示当前的全局符号表。 使用 globals 函数帮助 best_promo 自动找到其他可用的 *_promo 函数，过程有点 曲折。
	  
	  # from abc import ABC, abstractmethod
	  from collections import namedtuple
	  
	  Customer = namedtuple("Customer", "name fidelity")  # 通过具名元组定义一个”顾客“类型，包含【顾客名称、顾客积分】
	  
	  
	  class LineItem:
	      """定义清单明细"""
	  
	      def __init__(self, product, quantity, price):
	          self.product = product  # 物品
	          self.quantity = quantity  # 数量
	          self.price = price  # 单价
	  
	      def total(self):
	          """明细价格：价格*数量"""
	          return self.price * self.quantity
	  
	  
	  class Order:
	      """订单信息"""
	  
	      def __init__(self, customer, cart, promotion):
	          self.customer = customer  # 顾客
	          self.cart = list(cart)  # 购物车
	          self.promotion = promotion  # 折扣策略
	  
	      def total(self):
	          """总价格（未打折）= 购物车中明细价格之和"""
	          if not hasattr(self, '__total'):
	              return sum(item.total() for item in self.cart)
	          return self.__total
	  
	      def due(self):
	          """最终价格/确定价格 总价格-折扣价格"""
	          if self.promotion is None:
	              discount = 0
	          else:
	              discount = self.promotion(self)
	          return self.total() - discount
	  
	      def __repr__(self):
	          fmt = '<Order total:{:.2f} due:{:.2f}>'
	          return fmt.format(self.total(), self.due())
	  
	  
	  def fidelity_promo(order):
	      # 策略1：有 1000 或以上积分的顾客，每个订单享 5% 折扣
	      return order.total() * .05 if order.customer.fidelity > 1000 else 0
	  
	  
	  def bulk_item_promo(order):
	      # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
	      discout = 0
	      for item in order.cart:
	          if item.quantity >= 20:
	              discout += item.total() * .1
	      return discout
	  
	  
	  def large_order_promo(order):
	      # 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	      # return order.total() * .07 if len(order.cart) >= 10 else 0
	      distinct_items = {item.product for item in order.cart}
	      if len(distinct_items) >= 10:
	          return order.total() * .07
	      return 0
	  
	  
	  def best_promo(order):
	      """
	      选择最优的折扣方案
	      :param order: 订单
	      :return: 最优解
	      """
	      # promos = [fidelity_promo, bulk_item_promo, large_order_promo]  # 列出函数实现的各个策略
	      promos = [globals()[name] for  name in globals() if name.endswith('_promo') and name != 'best_promo']
	      return max(promo(order) for promo in promos)
	  
	  
	  # 两个顾客：joe 的积分是 0，ann 的积分是 1100。
	  joe = Customer('John Doe', 0)
	  ann = Customer('Ann Smith', 1100)
	  # 三种购物车
	  cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermellon', 5, 5.0)]
	  banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
	  long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
	  
	  print("------------joe的选择（普通购物车）------------")
	  print(Order(joe, cart, fidelity_promo))  # <Order total:42.00 due:42.00> 不打折
	  print(Order(joe, cart, bulk_item_promo))  # <Order total:30.00 due:28.50> # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
	  print(Order(joe, cart, large_order_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  print(Order(joe, cart, best_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  print("------------ann的选择（普通购物车）------------")
	  print(Order(ann, cart, fidelity_promo))  # <Order total:42.00 due:42.00> 不打折
	  print(Order(ann, cart, bulk_item_promo))  # <Order total:30.00 due:28.50> # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
	  print(Order(ann, cart, large_order_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  print(Order(ann, cart, best_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  print("------------joe的选择（香蕉购物车）------------")
	  print(Order(joe, banana_cart, fidelity_promo))  # <Order total:42.00 due:42.00> 不打折
	  print(Order(joe, banana_cart, bulk_item_promo))  # <Order total:30.00 due:28.50> # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
	  print(Order(joe, banana_cart, large_order_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  print(Order(joe, banana_cart, best_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  print("------------joe的选择（长订单购物车）------------")
	  print(Order(joe, long_order, fidelity_promo))  # <Order total:42.00 due:42.00> 不打折
	  print(Order(joe, long_order, bulk_item_promo))  # <Order total:30.00 due:28.50> # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
	  print(Order(joe, long_order, large_order_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
	  print(Order(joe, long_order, best_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣

- 命令模式

	- “命令”设计模式也可以通过把函数作为参数传递而简化
	- “命令”模式的目的是解耦调用操作的对象（调用者）和提供实现的对象（接收者）。

### 第7章 函数装饰器和闭包

- 本章目标

	- 最终目标是解释清楚函数装饰器的工作原理
	- 基础知识

		- • Python 如何计算装饰器句法 
		- • Python 如何判断变量是不是局部的 
		- • 闭包存在的原因和工作原理 
		- • nonlocal 能解决什么问题

	- 进一步探讨

		- • 实现行为良好的装饰器 
		- • 标准库中有用的装饰器 
		- • 实现一个参数化装饰器

- 装饰器的特性

	- 能把被装饰的函数替换成其他函数。 
	- 装饰器 在加载模块时立即执行。

- 装饰器基础知识 

	- 装饰器是可调用的对象，其参数是另一个函数（被装饰的函数）。
	- 装饰器可能会处理被装 饰的函数，然后把它返回，或者将其替换成另一个函数或可调用对象
	- CodeDemo

	  # 装饰器通常把函数替换成另一个函数
	  def deco(fun):
	      def inner():
	          print('running inner()')
	      return inner
	  
	  
	  @deco
	  def target():
	      print('running target()')
	  
	  
	  print(target())
	  print(target)

- Python何时执行装饰器

	- 它们在被装饰的函数定义之后立即运行

	  # 如何证明装饰器是在被装饰的函数后立即执行
	  registry = []  # 定义一个[]用于存储被装饰的函数引用
	  
	  
	  def register(func):
	      print('running register(%s)' % func)  # 打印被装饰的函数
	      registry.append(func)  # 将被装饰的函数添加到registry中
	      return func
	  
	  
	  @register
	  def f1():
	      print("running f1() ")
	  
	  
	  @register
	  def f2():
	      print("running f2() ")
	  
	  
	  def f3():
	      print("running f3() ")
	  
	  
	  def main():
	      print("running main() ")
	      print("registry  ->", registry)
	      f1()
	      f2()
	      f3()
	  
	  
	  if __name__ == '__main__':
	      main()
	  
	  '''
	  running register(<function f1 at 0x0122D618>)   ①
	  running register(<function f2 at 0x035BD978>)   ②
	  running main()                                  ③
	  registry  -> [<function f1 at 0x0122D618>, <function f2 at 0x035BD978>] ④
	  running f1()                                    ⑤
	  running f2()                                    ⑥
	  running f3()                                    ⑦
	  '''
	  """
	  结果分析：
	  从①②，可以看出 register 在 main 方法之前已经运行了两次。分别是调用函数 f1 和 f2
	  从③④，可以看出 在方法调用之前已经执行，换句话说：是在被装饰的时候调用
	  
	  """

	- 函数装饰器在导入模块时立即执行，而被装饰的函数只在明确调用 时运行。这突出了 Python 程序员所说的导入时和运行时之间的区别
	- __main__ 与 __name__
	- 更常用

		- • 装饰器函数与被装饰的函数在同一个模块中定义。实际情况是，装饰器通常在一个模块 中定义，然后应用到其他模块中的函数上。 
		- • register 装饰器返回的函数与通过参数传入的相同。实际上，大多数装饰器会在内部定 义一个函数，然后将其返回。

- 使用装饰器改进“策略”模式

  # 使用注册装饰器可以改进 6.1 节中的电商促销折扣示例。
  # 回顾一下，示例 6-6 的主要问题是，定义体中有函数的名称，但是 best_promo 用来判断哪 个折扣幅度最大的 promos 列表中也有函数名称。
  # 这种重复是个问题，因为新增策略函数后 可能会忘记把它添加到 promos 列表中，导致 best_promo 忽略新策略，而且不报错，为系 统引入了不易察觉的缺陷。
  # 示例 7-3 使用注册装饰器解决了这个问题
  
  
  promos=[]
  
  def promotion(promo_func):
      promos.append(promo_func)
      return promo_func
  
  from collections import namedtuple
  
  Customer = namedtuple("Customer", "name fidelity")  # 通过具名元组定义一个”顾客“类型，包含【顾客名称、顾客积分】
  
  
  class LineItem:
      """定义清单明细"""
  
      def __init__(self, product, quantity, price):
          self.product = product  # 物品
          self.quantity = quantity  # 数量
          self.price = price  # 单价
  
      def total(self):
          """明细价格：价格*数量"""
          return self.price * self.quantity
  
  
  class Order:
      """订单信息"""
  
      def __init__(self, customer, cart, promotion):
          self.customer = customer  # 顾客
          self.cart = list(cart)  # 购物车
          self.promotion = promotion  # 折扣策略
  
      def total(self):
          """总价格（未打折）= 购物车中明细价格之和"""
          if not hasattr(self, '__total'):
              return sum(item.total() for item in self.cart)
          return self.__total
  
      def due(self):
          """最终价格/确定价格 总价格-折扣价格"""
          if self.promotion is None:
              discount = 0
          else:
              discount = self.promotion(self)
          return self.total() - discount
  
      def __repr__(self):
          fmt = '<Order total:{:.2f} due:{:.2f}>'
          return fmt.format(self.total(), self.due())
  
  @promotion
  def fidelity_promo(order):
      # 策略1：有 1000 或以上积分的顾客，每个订单享 5% 折扣
      return order.total() * .05 if order.customer.fidelity > 1000 else 0
  
  @promotion
  def bulk_item_promo(order):
      # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
      discout = 0
      for item in order.cart:
          if item.quantity >= 20:
              discout += item.total() * .1
      return discout
  
  @promotion
  def large_order_promo(order):
      # 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
      # return order.total() * .07 if len(order.cart) >= 10 else 0
      distinct_items = {item.product for item in order.cart}
      if len(distinct_items) >= 10:
          return order.total() * .07
      return 0
  
  
  def best_promo(order):
      """
      选择最优的折扣方案
      :param order: 订单
      :return: 最优解
      """
      # promos = [fidelity_promo, bulk_item_promo, large_order_promo]  # 列出函数实现的各个策略
      return max(promo(order) for promo in promos)
  
  
  # 两个顾客：joe 的积分是 0，ann 的积分是 1100。
  joe = Customer('John Doe', 0)
  ann = Customer('Ann Smith', 1100)
  # 三种购物车
  cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermellon', 5, 5.0)]
  banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
  long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
  
  print("------------joe的选择（普通购物车）------------")
  print(Order(joe, cart, fidelity_promo))  # <Order total:42.00 due:42.00> 不打折
  print(Order(joe, cart, bulk_item_promo))  # <Order total:30.00 due:28.50> # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
  print(Order(joe, cart, large_order_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
  print(Order(joe, cart, best_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
  print("------------ann的选择（普通购物车）------------")
  print(Order(ann, cart, fidelity_promo))  # <Order total:42.00 due:42.00> 不打折
  print(Order(ann, cart, bulk_item_promo))  # <Order total:30.00 due:28.50> # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
  print(Order(ann, cart, large_order_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
  print(Order(ann, cart, best_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
  print("------------joe的选择（香蕉购物车）------------")
  print(Order(joe, banana_cart, fidelity_promo))  # <Order total:42.00 due:42.00> 不打折
  print(Order(joe, banana_cart, bulk_item_promo))  # <Order total:30.00 due:28.50> # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
  print(Order(joe, banana_cart, large_order_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
  print(Order(joe, banana_cart, best_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
  print("------------joe的选择（长订单购物车）------------")
  print(Order(joe, long_order, fidelity_promo))  # <Order total:42.00 due:42.00> 不打折
  print(Order(joe, long_order, bulk_item_promo))  # <Order total:30.00 due:28.50> # 策略2：同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣
  print(Order(joe, long_order, large_order_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
  print(Order(joe, long_order, best_promo))  # <Order total:10.00 due:9.30> 策略3：订单中的不同商品达到 10 个或以上，享 7% 折扣
  
  #---------------------- 方案比较 --------------------------
  '''
  1：促销策略函数无需使用特殊的名称
  2：便于临时禁用启用
  3：可以在系统中其他模块使用
  '''

- 变量作用域规则

  b = 6
  
  
  def f1(a):
      print(a)
      print(b)
  
  
  def f2(a):
      """
      Python 在变异函数的定义体时，它判断b是局部变量，因为（b=5）给它赋过值了，
      但是  print(b) 时，却发现b没有绑定数值
      """
      print(a)
      print(b)
      b = 5
  
  
  def f3(a):
      global b
      print(a)
      print(b)
      b = 5
  
  
  f1(3)
  print(b)
  
  from dis import dis
  print(dis(f1))
  print("----------------------------")
  print(dis(f2))

- 闭包

	- 实现计算移动平均值

	  class Averager():
	      '''计算移动平均值的类 '''
	  
	      def __init__(self):
	          self.series = []
	  
	      def __call__(self, newvalue):
	          self.series.append(newvalue)
	          total = sum(self.series)
	          return total / len(self.series)
	  
	  
	  ave = Averager()
	  print(ave(10))
	  print(ave(11))
	  print(ave(12))
	  
	  
	  def make_average():
	      '''计算移动平均值的高阶函数 '''
	      series = []  #自由变量 未在本地作用域中绑定的变量
	  
	      def averager(new_value):
	          series.append(new_value)
	          total = sum(series)
	          return total / len(series)
	  
	      return averager
	  
	  
	  print("-------------通过函数调用--------------")
	  aver = make_average()
	  print(aver(10))
	  print(aver(11))
	  print(aver(12))
	  print("变量名称：",aver.__code__.co_varnames)
	  print("自由变量：",aver.__code__.co_freevars)
	  print(aver.__closure__)
	  print(aver.__closure__[0].cell_contents)
	  
	  # 只有嵌套在其他函数中的函数才能需要处理不再全局作用域中的外部变量

	- 进阶版，提高性能

	  # 1：效率不高，每次都全部计算。
	  # 2：只存储目前的总值和元素个数，然后计算平均值
	  
	  def make_average():
	      count = 0
	      total = 0
	  
	      def averager(new_value):
	          nonlocal count,total # 把变量标记为 自由变量 （未在本地作用域中绑定的变量）
	          # 如果为nonlocal 声明的变量赋予新值，闭包中保存的绑定会更新
	          count += 1
	          total += new_value
	  
	          return total / count
	  
	      return averager

- 实现一个简单的装饰器

	- 装饰器

	  # 一个简单的装饰器，输出函数的运行时间
	  
	  from time import perf_counter as pc
	  
	  
	  def clock(func):
	      """
	      把被装饰的函数替换成新函数，二者接受相同的参数，而且（通常）返回被装饰的函数本该返回的值，同时还有一些额外操作
	      :param func:
	      :return:
	      """
	      def clocked(*args):
	          p0 = pc()  # (1) 记录初始时间
	          result = func(*args)  # （2）调用原来的函数，保存结果
	          elapsed = pc() - p0  # 计算经过时间
	          name = func.__name__
	          arg_str = ", ".join(repr(arg) for arg in args)
	          print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))  # 格式化收集的数据，然后打印出来
	          return result
	  
	      return clocked

	- 调用

	  import time
	  
	  from clockdeco_demo import clock
	  
	  
	  # 定义两个方法（睡眠+阶乘）
	  @clock
	  def snooze(seconds):
	      time.sleep(seconds)
	  
	  
	  @clock
	  def factorial(n):
	      return 1 if n < 2 else factorial(n - 1) * n
	  
	  
	  if __name__ == '__main__':
	      print('*' * 40, 'Calling snooze(.123)')
	      snooze(.123)
	      print('*' * 40, 'Calling factorial(6)')
	      print('6! =', factorial(6))

	- 装饰器2.0

	  # 一个简单的装饰器，输出函数的运行时间
	  import functools
	  from time import perf_counter as pc
	  
	  
	  def clock(func):
	      """
	      把被装饰的函数替换成新函数，二者接受相同的参数，而且（通常）返回被装饰的函数本该返回的值，同时还有一些额外操作
	      :param func:
	      :return:
	      """
	      @functools.wraps(func)
	      def clocked(*args,**kwargs):
	          p0 = pc()  # (1) 记录初始时间
	          result = func(*args,**kwargs)  # （2）调用原来的函数，保存结果
	          elapsed = pc() - p0  # 计算经过时间
	          name = func.__name__
	          arg_str = ", ".join(repr(arg) for arg in args)
	          print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))  # 格式化收集的数据，然后打印出来
	          return result
	  
	      return clocked

- 标准库中的装饰器

	- 使用functools.lru_cache做备忘 

		- 它把耗时的函数的结果保存起来，避免传入相同的参数时重复计算

		  import functools
		  
		  from clockdeco_demo import clock
		  
		  # @functools.lru_cache() # lru_cache 可以接受配置参数，稍后说明
		  @clock
		  def fibonacci(n):
		      if n < 2:
		          return n
		      return fibonacci(n - 2) + fibonacci(n - 1)
		  
		  
		  if __name__ == '__main__':
		      print(fibonacci(20))
		  
		  """
		  这里叠放了装饰器，@functools.lru_cache() 应用到 @clock 返回的函数上
		  """

- 单分派泛函数 

	- functools.singledispatch 

*XMind - Trial Version*