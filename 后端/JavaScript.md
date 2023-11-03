# 1. 什么是JavaScript？

JavaScript 是世界上最流行的脚本语言

Java、JavaScript 没有多大的联系

是由一个叫 Brendan Eich（布兰登·艾克）的大神用10天时间搞出来的！

# 2. 快速入门

### 2.1 引入JavaScript

1. 内部标签

~~~html
<script>
	//  ......
</script>
~~~

2. 外部引用

![image-20230906170635556](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906170635556.png)

## 2.2 基本语法入门

浏览器必备调试须知：

![image-20230906172104250](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906172104250.png)

## 2.3 数据类型：

**值类型(基本类型)**：字符串（String）、数字(Number)、布尔(Boolean)、空（Null）、未定义（Undefined）、Symbol。

**引用数据类型（对象类型）**：对象(Object)、数组(Array)、函数(Function)，还有两个特殊的对象：正则（RegExp）和日期（Date）。

> 具体参考：[JavaScript 数据类型 | 菜鸟教程 (runoob.com)](https://www.runoob.com/js/js-datatypes.html)

总结：1. JavaScript中数组中的类型可以不同

			2. 对象和类有点相似，可以通过`对象.属性`来进行访问
			2.  存在精度问题，== 与 ===，前者值相等就可，后者类型也必须一致
			2.  可以直接用中文来做变量 `var 王者荣耀="倔强青铜";  `
			2.  可以用`var $1=1;  ` 其中$1为变量名

## 2.4 严格模式

![image-20230906174451953](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906174451953.png)

# 3. 数据类型

## 3.1 字符串

~~~javascript
1. ""
// 转义字符
\n
// 3. 多行编码
var name = `ag
        asga
        b`
// 4.模板字符串
let msg = "你好：${name}"
// 5. 字符串长度
msg.length
// 6. 字符串不可以改变
// 7.常见方法
name.toUpperCase()
name.toLowerCase()
name.indexOf('?') // 获取某个字符串的位置

~~~

## 3.2 数组

![image-20230913184629196](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230913184629196.png)

![image-20230913184645542](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230913184645542.png)

![image-20230913184657751](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230913184657751.png)

## 3.3 对象

![image-20230913184812222](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230913184812222.png)

![image-20230913185053040](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230913185053040.png)

![image-20230913185144998](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230913185144998.png)

## 3.4 流程控制

~~~javascript
for
do while
while
这些都一样
特有:
~~~

![image-20230913185818809](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230913185818809.png)

## 3.5 Map和Set

![image-20230913190322742](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230913190322742.png)

## 3.6 iterator

![image-20230913190548297](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230913190548297.png)

# 4. 函数

## 4.1 定义函数

![image-20230914192051576](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230914192051576.png)

![image-20230914192158750](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230914192158750.png)

![image-20230914192323219](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230914192323219.png)

![image-20230914192545822](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230914192545822.png)

![image-20230914192950932](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230914192950932.png)

## 4.2 变量作用域

JavaScript中的作用域和其它语言类似。

![image-20230915170505614](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230915170505614.png)

> 区别:

![image-20230915171550118](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230915171550118.png)

## 4.3 方法

![image-20230915172143470](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230915172143470.png)

![image-20230915172814673](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230915172814673.png)

![image-20230915173040978](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230915173040978.png)

# 5.内部对象

## 5.1 Date

![image-20230915180817089](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230915180817089.png)

## 5.2 JSON

![image-20230915181857993](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230915181857993.png)

![image-20230915181941559](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230915181941559.png)

## 5.3  Ajax

![image-20230915182014540](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230915182014540.png)



# 6.面向对象

在JavaScript中，可以通过两种方式进行继承：

![image-20230915183121552](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230915183121552.png)

![image-20230915183311538](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230915183311538.png)

**JavaScript中会存在一个链式结构，会有无穷的父类（都是它本身）**

![image-20230915183414654](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230915183414654.png)

# 7.操作BOM对象（重点）

![image-20230915191702329](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230915191702329.png)

![image-20230915191716282](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230915191716282.png)

![image-20230915191727003](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230915191727003.png)

![image-20230915191754882](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230915191754882.png)

![image-20230915191810975](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230915191810975.png)

# 8.操作DOM对象

## 获取DOM节点

![image-20230916095341587](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230916095341587.png)

## 更新节点

![image-20230916100341311](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230916100341311.png)

## 删除节点

![image-20230916102950209](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230916102950209.png)

## 创建和插入节点

![image-20230918104022379](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230918104022379.png)

![image-20230918104327812](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230918104327812.png)

![image-20230918104845973](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230918104845973.png)

# 操作表单

## 获取表单的值

![image-20230918105304196](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230918105304196.png)

## MD5加密

![image-20230918110656443](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230918110656443.png)

# 10.jQuery

![image-20230918111036030](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230918111036030.png)

## 选择器

![image-20230918111247797](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230918111247797.png)

**中文文档：**[jQuery API 中文文档 | jQuery API 中文在线手册 | jquery api 下载 | jquery api chm (cuishifeng.cn)](https://jquery.cuishifeng.cn/)

## 事件

鼠标事件，键盘事件，其它事件

> 主要使用：mousemove,

![image-20230918112607107](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230918112607107.png)

# 11. VUE

![image-20230918120136600](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230918120136600.png)

![image-20230918151926016](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230918151926016.png)

![image-20230918152059131](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230918152059131.png)

![image-20230918152438916](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230918152438916.png)![image-20230918152643736](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230918152643736.png)

![image-20230918152932420](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230918152932420.png)

![image-20230918153221989](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230918153221989.png)

# 12.Ajax

![image-20230918153544846](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230918153544846.png)

![image-20230918153525156](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230918153525156.png)

![image-20230918154607293](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230918154607293.png)
