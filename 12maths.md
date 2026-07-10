# Manual Formula Fixes

## Chapter 4 – Determinants

### ID 297

```latex
\begin{aligned}
1.\quad &
\text{Prove that the determinant }
\begin{vmatrix}
-x & \sin\theta & \cos\theta\\
-x & -x & 1\\
\cos\theta & 1 & x
\end{vmatrix}
\text{ is independent of }\theta.\\[1ex]

2.\quad &
\text{Evaluate }
\begin{vmatrix}
\cos\alpha\cos\beta & \cos\alpha\sin\beta & -\sin\alpha\\
-\sin\beta & \cos\beta & 0\\
\sin\alpha\cos\beta & \sin\alpha\sin\beta & \cos\alpha
\end{vmatrix}.\\[1ex]

3.\quad &
\text{If }A^{-1}
=
\frac1{15}
\begin{bmatrix}
3&1&1\\
6&5&2\\
5&2&2
\end{bmatrix},
\quad
B=
\begin{bmatrix}
1&3&0\\
2&2&1\\
0&-2&-1
\end{bmatrix},
\text{ find }AB.\\[1ex]

4.\quad &
\text{Let }
A=
\begin{bmatrix}
1&2&1\\
2&3&1\\
1&1&5
\end{bmatrix}.
\text{ Verify that }
\begin{cases}
[\operatorname{adj}(A)]^{-1}=\operatorname{adj}(A^{-1}),\\
(A^{-1})^{-1}=A.
\end{cases}\\[1ex]

5.\quad &
\text{Evaluate }
\begin{vmatrix}
x+y & x & y\\
y & x+y & x\\
x+y & x & y
\end{vmatrix}.\\[1ex]

6.\quad &
\text{Evaluate }
\begin{vmatrix}
1 & 1 & 1\\
x+y & y & y\\
x & x+y & y
\end{vmatrix}.
\end{aligned}
```

---

## Chapter 5 – Continuity and Differentiability

### ID 598

```latex
\frac{dx}{dt}
=
a\left(t+\frac{1}{t}\right)^{a-1}
\left(1-\frac{1}{t^{2}}\right)
```

which gives

```latex
\frac{dx}{dt}\neq0
\quad\text{only if}\quad
t\neq\pm1.
```

---

## Chapter 8 – Application of Integrals

### ID 40

```latex
\begin{aligned}
\text{Alternatively, considering horizontal strips as shown in Fig.\ 8.8, the area of the ellipse is}\\
&=4\int_{0}^{b}x\,dy
=4\frac{a}{b}\int_{0}^{b}\sqrt{b^{2}-y^{2}}\,dy\\
&=\frac{4a}{b}\left[
\frac{y}{2}\sqrt{b^{2}-y^{2}}
+\frac{b^{2}}{2}\sin^{-1}\!\left(\frac{y}{b}\right)
\right]_{0}^{b}\\
&=\frac{4a}{b}
\left[
\left(
\frac{b}{2}\times0+\frac{b^{2}}{2}\sin^{-1}1
\right)-0
\right]\\
&=\frac{4a}{b}\cdot\frac{b^{2}}{2}\cdot\frac{\pi}{2}
=\pi ab.
\end{aligned}
```

---

## Chapter 13 – Probability

### ID 223

```latex
\begin{aligned}
P(A\mid E_1)&=1,\\
P(A\mid E_2)&=0,\\
P(A\mid E_3)&=\frac12.
\end{aligned}
```

### ID 351

```latex
\begin{array}{c|cccccc}
X & 1 & 2 & 3 & 4 & 5 & 6\\
\hline
P(X) & \frac16 & \frac16 & \frac16 & \frac16 & \frac16 & \frac16
\end{array}
```