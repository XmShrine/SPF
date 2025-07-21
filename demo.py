import SPF

# 先给出一个不是对称多项式的例子

sp1 = SPF.Polynomial([SPF.Monomial(2, [1, 2]), SPF.Monomial(1, [2, 1])]) 

try: # 尝试分解
    result = SPF.SPF(sp1)
except SPF.SymmetricPolynomialError:
    print("不是轮换对称多项式")

# 再给出一个对称多项式的例子

sp2 = SPF.Polynomial([SPF.Monomial(1, [4]), SPF.Monomial(1, [0, 4]), SPF.Monomial(1, [0, 0, 4]), SPF.Monomial(1, [0, 0, 0, 4])])

try: # 尝试分解
    result = SPF.SPF(sp2)
    print("分解结果:", result)
except SPF.SymmetricPolynomialError:
    print("不是轮换对称多项式")