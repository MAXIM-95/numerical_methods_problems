# Задача 1 (папка dam_break)

Задана квазилинейная система уравнений мелкой воды, описывающая неустановившееся течение в тонком слое жидкости:

$$\begin{equation*}
 \begin{cases}
   \frac{∂h}{∂t} + \frac{∂hu}{∂x} = 0, 
   \\
   \frac{∂hu}{∂t} + \frac{∂}{∂x}(hu^2 + \frac{gh^2}{2}) = -gh*\frac{∂b}{∂x};
 \end{cases}
\end{equation*}$$

h – толщина слоя жидкости,
u – скорость жидкости,
b – профиль дна,
g – ускорение свободного падения.

Область решения: $0 ≤ x ≤ l, 0 ≤ t ≤ T; l = 1.0; T = 1.0$
Начальные условия: $h(0,x) = φ(x); u(0,x) = ψ(x).$
Краевые условия: $u(t,0) = f(t); h_x(t,l) = s(t).$

Данная программа реализовывает решение задачи методом Годунова.
Проводятся вычислительные эксперименты для задачи "Прорыв плотины", со следующими краевыми условиями:

$$φ(x)=\begin{equation*}
 \begin{cases}
   2.0, x ≤ 0.5, 
   \\
   1.0, x ≥ 0.5.
 \end{cases}
\end{equation*}
ψ(x) = 0,\\
f(t) = 0,\\
s(t) = 0.$$

Результаты работы программы:
1) Толщина слоя жидкости на 10-м слое:

![Толщина первого слоя](https://github.com/MAXIM-95/numerical_methods_problems/blob/main/dam_break/results/h_10.jpg)

2) Скорость жидкости на 10-м слое:

![Толщина первого слоя](https://github.com/MAXIM-95/numerical_methods_problems/blob/main/dam_break/results/u_10.jpg)


# Задача 2 (папка wind)

Нелинейное взаимодействие атмосферы, воды и пассатных ветров в экваториальной области Тихого океана можно описать трёхмерной неавтономной системой уравнений, предложенной Дж. Валлисом:

$$\begin{equation*}
 \begin{cases}
   Y_1^\prime*A_1*(Y_2-Y_3 )-A_2*(Y_1-f(t))= 0, 
   \\
   Y_2^\prime=Y_1*Y_3-Y_2+A_5,
   \\
   Y_3^\prime==-Y_1*Y_2-Y_3+A_5;
 \end{cases}
\end{equation*}$$


