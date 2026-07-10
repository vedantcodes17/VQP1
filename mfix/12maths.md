# Manual Formula Fixes

## Chapter 4 – Determinants

### Determinant Properties and Applications Exercise (Q1–Q6) (ID 297)

$$
\begin{aligned}
1.\quad &
\text{Prove that the determinant }
\begin{vmatrix}
-x & \sin\theta & \cos\theta\\\\
-x & -x & 1\\\\
\cos\theta & 1 & x
\end{vmatrix}
\text{ is independent of }\theta.\\\\[1ex]

2.\quad &
\text{Evaluate }
\begin{vmatrix}
\cos\alpha\cos\beta & \cos\alpha\sin\beta & -\sin\alpha\\\\
-\sin\beta & \cos\beta & 0\\\\
\sin\alpha\cos\beta & \sin\alpha\sin\beta & \cos\alpha
\end{vmatrix}.\\\\[1ex]

3.\quad &
\text{If }A^{-1}
= \frac1{15}
\begin{bmatrix}
3&1&1\\\\
6&5&2\\\\
5&2&2
\end{bmatrix},
\quad
B=
\begin{bmatrix}
1&3&0\\\\
2&2&1\\\\
0&-2&-1
\end{bmatrix},
\text{ find }AB.\\\\[1ex]

4.\quad &
\text{Let }
A=
\begin{bmatrix}
1&2&1\\\\
2&3&1\\\\
1&1&5
\end{bmatrix}.
\text{ Verify that }
\begin{cases}
[\operatorname{adj}(A)]^{-1}=\operatorname{adj}(A^{-1}),\\\\
(A^{-1})^{-1}=A.
\end{cases}\\\\[1ex]

5.\quad &
\text{Evaluate }
\begin{vmatrix}
x+y & x & y\\\\
y & x+y & x\\\\
x+y & x & y
\end{vmatrix}.\\\\[1ex]

6.\quad &
\text{Evaluate }
\begin{vmatrix}
1 & 1 & 1\\\\
x+y & y & y\\\\
x & x+y & y
\end{vmatrix}.
\end{aligned}
$$

---

## Chapter 5 – Continuity and Differentiability

### Derivative of a Parametric Power Function (ID 598)

$$
\frac{dx}{dt}
= a\left(t+\frac{1}{t}\right)^{a-1}
\left(1-\frac{1}{t^{2}}\right)
$$

which gives

$$
\frac{dx}{dt}\neq0
\quad\text{only if}\quad
t\neq\pm1.
$$

---

## Chapter 8 – Application of Integrals

### Area of an Ellipse (Horizontal Strip Method) (ID 40)

$$
\begin{aligned}
\text{Alternatively, considering horizontal strips as shown in Fig.\ 8.8, the area of the ellipse is}\\\\
&=4\int_{0}^{b}x\\,dy
=4\frac{a}{b}\int_{0}^{b}\sqrt{b^{2}-y^{2}}\\,dy\\\\
&=\frac{4a}{b}\left[
\frac{y}{2}\sqrt{b^{2}-y^{2}}
+\frac{b^{2}}{2}\sin^{-1}\\!\left(\frac{y}{b}\right)
\right]_{0}^{b}\\\\
&=\frac{4a}{b}
\left[
\left(
\frac{b}{2}\times0+\frac{b^{2}}{2}\sin^{-1}1
\right)-0
\right]\\\\
&=\frac{4a}{b}\cdot\frac{b^{2}}{2}\cdot\frac{\pi}{2}
=\pi ab.
\end{aligned}
$$

---

## Chapter 13 – Probability

### Conditional Probabilities P(A|E_i) (ID 223)

$$
\begin{aligned}
P(A\mid E_1)&=1,\\\\
P(A\mid E_2)&=0,\\\\
P(A\mid E_3)&=\frac12.
\end{aligned}
$$

### Probability Distribution of a Fair Die (ID 351)

| X | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| P(X) | $\frac16$ | $\frac16$ | $\frac16$ | $\frac16$ | $\frac16$ | $\frac16$ |

## Chapter 7 – Integrals

### Fundamental Theorem of Calculus Verification (ID 51)

$$
\begin{aligned}
\therefore\quad
\frac{d}{dx}\left(\int f(x)\\,dx\right)
&=\frac{d}{dx}\left(F(x)+C\right)\\\\
&=F'(x)\\\\
&=f(x).
\end{aligned}
$$

---

### Integral of tan x (ID 160)

$$
\begin{aligned}
\text{Put }\cos x=t
\text{ so that }
-\sin x\\,dx=dt.\\\\
\therefore\quad
\int\tan x\\,dx
&=-\int\frac{dt}{t}\\\\
&=-\log|t|+C\\\\
&=-\log|\cos x|+C\\\\
&=\log|\sec x|+C.
\end{aligned}
$$

---

### Integral of sin x / sin(x + a) (ID 165)

$$
\begin{aligned}
\int\frac{\sin x}{\sin(x+a)}\\,dx
&=\int\frac{\sin(t-a)}{\sin t}\\,dt\\\\
&=\int\frac{\sin t\cos a-\cos t\sin a}{\sin t}\\,dt\\\\
&=\cos a\int dt-\sin a\int\cot t\\,dt\\\\
&=(\cos a)t-(\sin a)\left[\log|\sin t|+C_1\right]\\\\
&=(\cos a)(x+a)-(\sin a)\log|\sin(x+a)|+C\\\\
&=x\cos a-\sin a\log|\sin(x+a)|+C.
\end{aligned}
$$

---

### Integration Exercise – Rational Functions (ID 296)

$$
\begin{aligned}
\text{Find the following integrals:}\\\\[4pt]
(i)\\;&\int\frac{dx}{x^2-6x+13}\\\\[2pt]
(ii)\\;&\int\frac{x^2+13x-10}{x^3-6x^2+13x-10}\\,dx\\\\[2pt]
(iii)\\;&\int\frac{x^2-6x+13}{x^3-6x^2+13x-10}\\,dx
\end{aligned}
$$

---

### Integration Exercise – Exponential and Inverse-Trig Forms (ID 522)

$$
16.\\;e^x(\sin x+\cos x)
\qquad
17.\\;\frac{x\\,e^x}{(1+x)^2}
\qquad
18.\\;e^x\left(\frac{1+\sin x}{1+\cos x}\right)
\\\\[4pt]
19.\\;\frac{(x-3)e^x}{(x-1)^3}
\qquad
20.\\;e^x\left(\frac1x-\frac1{x^2}\right)
\qquad
21.\\;e^{2x}\sin x
\\\\[4pt]
22.\\;\sin^{-1}\\!\left(\frac{2x}{1+x^2}\right)
$$

### First-Order Linear Differential Equations Exercise (ID 392)

$$
\begin{aligned}
\text{For each of the differential equations given in Exercises 1 to 12, find the general solution:}\\\\[4pt]
1.\\;&\frac{dy}{dx}+\frac{y}{x^{2}}=\sin x\\\\[4pt]
2.\\;&\frac{dy}{dx}+y=e^{-3x^{2}}\\\\[4pt]
3.\\;&\frac{dy}{dx}+\frac{2}{x}y=x^{2}\\\\[4pt]
5.\\;&\frac{dy}{dx}+y\tan x=\cos^{2}x,
\qquad 0\le x<\frac{\pi}{2}\\\\[4pt]
6.\\;&\frac{dy}{dx}+\frac{2}{x}y=x^{2}\log x\\\\[4pt]
7.\\;&\frac{dy}{dx}+\frac{\log x}{x}y=\frac{2\log x}{x}\\\\[4pt]
8.\\;&(1+x^{2})\\,dy+2xy\\,dx=\cot x\\,dx,
\qquad (x\neq0)\\\\[4pt]
9.\\;&x\frac{dy}{dx}+\frac{\cot x}{x}\\,y-\frac{y}{x}+x=0,
\qquad (x\neq0)\\\\[4pt]
10.\\;&(x+1)\frac{dy}{dx}+y=1\\\\[4pt]
11.\\;&y\\,dx+(x-y^{2})\\,dy=0\\\\[4pt]
12.\\;&\frac{dy}{dx}+\left(\frac{x}{y^{3}}\right)y=0,
\qquad (y>0)
\end{aligned}
$$
