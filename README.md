Задана квазилинейная система уравнений мелкой воды, описывающая неустановившееся течение в тонком слое жидкости:

$\frac{∂h}{∂t} + \frac{∂hu}{∂x} = 0, \frac{∂hu}{∂t} + \frac{∂}{∂x}(hu^2 + \frac{gh^2}{2}) = -gh*\frac{∂b}{∂x};$

h – толщина слоя жидкости,
u – скорость жидкости,
b – профиль дна,
g – ускорение свободного падения.

Область решения: $0 ≤ x ≤ l, 0 ≤ t ≤ T; l = 1.0; T = 1.0$
Начальные условия: $h(0,x) = φ(x); u(0,x) = ψ(x).$
Краевые условия: $u(t,0) = f(t); h_x(t,l) = s(t).$

Данная программа на языке Python реализовывает решение задачи методом Годунова.
Проводятся вычислительные эксперименты для задачи "Прорыв плотины", сос ледующими краевыми условиями:

$φ(x) = 2.0, x ≤ 0.5,\\
φ(x) = 1.0, x ≥ 0.5,\\
ψ(x) = 0,\\
f(t) = 0,\\
s(t) = 0.$

$$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$
$$\begin{equation*}
 \begin{cases}
   \frac{∂h}{∂t} + \frac{∂hu}{∂x} = 0, 
   \\
   \frac{∂hu}{∂t} + \frac{∂}{∂x}(hu^2 + \frac{gh^2}{2}) = -gh*\frac{∂b}{∂x};
 \end{cases}
\end{equation*}$$
