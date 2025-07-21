```
sp1 = SPF.Polynomial([SPF.Monomial(2, [1, 2]), 
SPF.Monomial(1, [2, 1])]) 
```
本句话所定义的是多项式 $2x_1x_2^2+x_1^2x_2$，判断其不是轮换对称多项式，所以没有做进一步的操作。
```
sp2 = SPF.Polynomial([SPF.Monomial(1, [4]), 
SPF.Monomial(1, [0, 4]), 
SPF.Monomial(1, [0, 0, 4]), 
SPF.Monomial(1, [0, 0, 0, 4])])
```
这句话定义的是多项式 $x_1^4+x_2^4+x_3^4+x_4^4$，并证明其是轮换对称多项式，可以被表示为 
$\sigma_1^4-4\sigma_1^2\sigma_2+4\sigma_1\sigma_3$ <br>
$\sigma_1 = x_1+x_2+x_3+x_4$<br>
$\sigma_2=x_1x_2+x_1x_3+x_1x_4+x_2x_3+x_2x_4+x_3x_4$<br>
$\sigma_3 = x_1x_2x_3+x_1x_2x_4+x_1x_3x_4+x_2x_3x_4$<br>
$\sigma_4 = x_1x_2x_3x_4$<br>
这几个 $\sigma$ 都是轮换对称多项式
