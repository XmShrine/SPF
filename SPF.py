class MonomialNotEqualError(Exception):
    pass
class SymmetricPolynomialError(Exception):
    pass
class Monomial:
    def update(self):
        temp = []
        sign = len(self.variables)
        for i in range(len(self.variables)):
            if self.variables[len(self.variables)-1-i] != 0:
                sign = i
                break
        for i in range(len(self.variables)-sign):
            temp.append(self.variables[i])
        self.variables = temp
        return self
    def len(self): # 单项式中变量的个数
        self.update()
        return len(self.variables) 
    def equal(self, mon): # 注意这个函数不比较系数
        self.update()
        mon.update()
        if self.len() != mon.len():
            return False
        for i in range(self.len()):
            if self.variables[i] != mon.variables[i]:
                return False
        return True
    def full_equal(self, mon): # 这个函数比较系数
        self.update()
        mon.update()
        if self.len() != mon.len():
            return False
        for i in range(self.len()):
            if self.variables[i] != mon.variables[i] or self.coeff != mon.coeff:
                return False
        return True 
    def inverse(self):
        self.coeff = -self.coeff
        return self
    def swap(self, i, j):
        self.update()
        num = max(i, j, self.len())
        temp = [0] * (num+1)
        for l in range(num):
            if l < self.len():
                temp[l] = self.variables[l]
        temp[i], temp[j] = temp[j], temp[i]
        return Monomial(self.coeff, temp)
    def copy(self):
        self.update()
        return Monomial(self.coeff.copy(), self.variables.copy())
    def __init__(self, coeff, variables):
        self.coeff = coeff
        self.variables = variables
        self.update()
        pass
    def __add__(self, mon):
        self.update()
        mon.update()
        if self.equal(mon) == False:
            raise MonomialNotEqualError()
        return Monomial(self.coeff+mon.coeff, self.variables)
    def __str__(self):
        return f"[{self.coeff}]{self.variables}"
    def __lt__(self, mon):
        self.update()
        mon.update()
        num = max(len(self.variables), len(mon.variables))
        for i in range(len(self.variables), num):
            self.variables.append(0)
        for i in range(len(mon.variables), num):
            mon.variables.append(0)
        for i in range(num):
            if self.variables[i] < mon.variables[i]:
                    return True
            if self.variables[i] > mon.variables[i]:
                    return False
        return False
    def __mul__(self, mon):
        self.update()
        mon.update()
        temp = [0] * max(len(self.variables), len(mon.variables))
        for i in range(len(temp)):
            if i < len(self.variables):
                temp[i] += self.variables[i]
            if i < len(mon.variables):
                temp[i] += mon.variables[i]
        return Monomial(self.coeff * mon.coeff, temp)

class Polynomial:
    def update(self):
        for i in self.vars:
            i.update()
        i, j = 0, 0
        while i < len(self.vars):
            j = i + 1
            while j < len(self.vars):
                if self.vars[i].equal(self.vars[j]) == True:
                    temp = self.vars[i] + self.vars[j]
                    del self.vars[j]
                    del self.vars[i]
                    self.vars.append(temp)
                    i -= 1
                    break
                j += 1
            i += 1
        i, j = 0, 0
        while i < len(self.vars):
            if self.vars[i].coeff == 0:
                del self.vars[i]
                i -= 1
            i += 1
        i, j = 0, 0
        while i < len(self.vars):
            j = i + 1
            while j < len(self.vars):
                if self.vars[i] < self.vars[j]:
                    self.vars[i], self.vars[j] = self.vars[j], self.vars[i]
                j += 1
            i += 1
        for i in self.vars:
            i.update()
        i, j = 0, 0
        return self
    def len(self): # 多项式中单项式的个数
        self.update()
        return len(self.vars)
    def length(self): # 多项式中变量的个数
        num = 0
        self.update()
        for i in self.vars:
            num = max(num, i.len())
        return num
    def swap(self, i, j):
        self.update()
        temp = Polynomial([])
        for k in self.vars:
            temp = temp + Polynomial([k.swap(i, j)])
        return temp.update()
    def equal(self, pol): # 注意这个函数不比较系数
        self.update()
        pol.update()
        if len(self.vars) != len(pol.vars):
            return False
        for i in range(len(self.vars)):
            if self.vars[i].equal(pol.vars[i]) == False:
                return False
        return True
    def full_equal(self, pol): # 这个函数比较系数
        self.update()
        pol.update()
        if len(self.vars) != len(pol.vars):
            return False
        for i in range(len(self.vars)):
            if self.vars[i].full_equal(pol.vars[i]) == False:
                return False
        return True
    def __init__(self, mon_arr):
        self.vars = mon_arr
        pass
    def __str__(self):
        string = ""
        self.update()
        for i in range(len(self.vars)):
            string += str(self.vars[i])
            if i != len(self.vars) - 1:
                string += " + "
        return string
    def __add__(self, pol):
        self.vars.extend(pol.vars)
        return self.update()
    def __mul__(self, pol):
        temp = Polynomial([])
        for i in self.vars:
            for j in pol.vars:
                temp.vars.append(i * j)
        return temp.update()
    def __pow__(self, n):
        if n == 0:
            return Polynomial.num(1)
        if n == 1:
            return self
        result = Polynomial.num(1)
        for i in range(n):
            result = result * self
        return result.update()
    def num(n):
        return Polynomial([Monomial(n, [])])
class BasicSymPolynomial:
    def __init__(self, n):
        self.n = n
        self.sym = []
        for i in range(self.n):
            self.sym.append(self.generate(i + 1))
    def generate(self, n):
        if n == 0:
            return Monomial(0, [])
        if n == 1:
            temp = [0] * self.n
            result = Polynomial([])
            for i in range(self.n):
                temp[i] = 1
                result = result + Polynomial([Monomial(1, temp.copy())])
                temp[i] = 0
            return result
        temp = self.generate(n - 1).vars
        arr = []
        for i in temp:
            tmp = []
            for j in range(self.n):
                if j < i.len():
                    tmp.append(i.variables[j])
                else:
                    tmp.append(0)
            arr.append(tmp)
        result = []
        i, j = 0, 0
        while i < len(arr):
            j = 0
            while j < self.n:
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    result.append(arr[i].copy())
                    arr[i][j] = 0
                j += 1
            i += 1
        i, j = 0, 0
        while i < len(result):
            j = i + 1
            while j < len(result):
                if result[i] == result[j]:
                    del result[j]
                    j -= 1
                j += 1
            i += 1
        return_value = Polynomial([])
        for i in result:
            return_value = return_value + Polynomial([Monomial(1, i)])
        return return_value

def if_SPF(sp): # 检查是否为对称多项式
    for i in range(sp.length()):
        for j in range(i+1, sp.length()):
            temp = sp.swap(i, j)
            if temp.full_equal(sp) == True:
                continue
            return False
    return True

def SPF_helper(standard, sp):
    sp.update()
    if sp.len() < 1:
        return (Polynomial.num(0), Polynomial.num(0))
    first = sp.vars[0]
    coeff = first.coeff
    other_coeff =  [first.variables[i]-first.variables[i+1] if i < first.len()-1 else first.variables[i]  for i in range(first.len())]
    temp = Polynomial.num(1)
    for i in range(len(other_coeff)):
        temp = temp * (standard.sym[i]**(other_coeff[i]))
    return (Polynomial([Monomial(1, other_coeff)])*Polynomial.num(coeff), sp + Polynomial.num(-coeff)*temp)

def SPF(sp):
    if if_SPF(sp) == False:
        raise SymmetricPolynomialError()
    standard = BasicSymPolynomial(sp.length())
    left = sp
    result = Polynomial.num(0)
    while left.equal(Polynomial.num(0)) == False:
        temp = SPF_helper(standard, sp)
        sp = temp[1]
        result = result + temp[0]
    return result.update()
