# 轮换对称多项式的分解
## 使用方式
直接复制 `SPF.py` 并在需要使用时通过 `import SPF` 引入
## 依赖说明
本项目只依赖 python 本体
## 具体说明
以 $x_1^5x_2x_3+x_1x_2^5x_3+x_1x_2x_3^5$ 为例子，想要对其分解，首先需要将其转化为 `Polynomial`（多项式），而想要构造多项式，其构造函数要求如下：
```
class Polynomial:
    def __init__(self, mon):
        ...
```
要求传入一个由 `Monomial` （单项式）组成的数组，而 `Monomial` 对应的构造函数要求如下：
```
class Monomial:
    def __init__(self, coeff, variables):
        ...
```
要求传入单项式的系数和每个变量对应的次数，例如，想要初始化一个 $2x_1^5 x_2^4 x_3^3$ 的单项式通过 `Monomial(2, [5, 4, 3])`，而如果想要构造最上面的例子，需要通过：
```
poly = Polynomial([Monomial(1, [5, 1, 1]), Monomial(1, [1, 5, 1]), Monomial(1, [1, 1, 5])])
```
而在完成初始化后可以通过 `SPF.SPF` 来进行分解，值得注意的是，如果传入的不是轮换对称多项式，`SPF.SPF` 会抛出一个`SymmetricPolynomialError` 的错误，需要捕获，而该函数会同样返回一个多项式：
```
result = SPF(poly)
```
对于多项式可以通过 `print()` 打印信息，例如 `print(poly)` 的结果为
```
[1][5, 1, 1] + [1][1, 5, 1] + [1][1, 1, 5]
```
前面的中括号是系数，后面的则是变量的次数
而打印 `result` 得到的结果是：
```
[1][4, 0, 1] + [-4][2, 1, 1] + [4][1, 0, 2] + [2][0, 2, 1]
```
意思是，原来的多项式可以被分解为
$\sigma_1^4\sigma_3-4\sigma_1^2\sigma_2\sigma_3+4\sigma_1\sigma_3^2+2\sigma_2^2\sigma_3$
简而言之就是原来多项式中代表变量 $x_i$ 次数的部分变成代表轮换对称多项式 $\sigma_i$ 的次数
## 另一些可能有用的函数
`if_SPF` 可判断一个多项式是否是轮换对称多项式（这个函数不抛出异常）
`Polymonial.num(n)` 可以生成一个常数项单项式（以多项式的格式）