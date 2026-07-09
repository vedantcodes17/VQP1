

# APPLICATION OF DERIVATIVES

出With the Calculus as a key, Mathematics can be successfully applied to the explanation of the courseof Nature.”— WHITEHEAD

### 6.1 Introduction

In Chapter 5, we have learnt how to find derivative of composite functions, inverse trigonoiitnxpolndtmi fution.Inthischaptr, e wil tudy apliionofeivtiveiniousiciplie,.g., in engineering, science, social science, and many other fields.For instance, we will learn how the derivative can be used (i) to determine rate of change of quantities, (ii) to find theeuiofrmlurviid ntson the graph of a function which in turn will help us to locate points at which largest or smallest value (locally)ofafunctioncurs.We will also use derivative tofind intervals on which a function is increasing or decreasing. Finally, we use the derivative to find approximate value of certain quantities.

### 6.2 Rate of Change of Quantities

Recall that by the derivative $\frac{d s}{d t}$ we mean the rate of change of distance s with respect to the time t. In a similar fashion, whenever one quantity y varies with another quantity x, satisfying some rule $y=f(x)$ ,then $\frac{dy}{dx}(\mathrm{or}f'(x))$ represents the rate of change of y with respect to x and $\left[{\frac{d y}{d x}}\right]_{x=x_{0}}\;\left(\mathrm{o r}f^{\prime}(x_{_0})\right)$ represents the rate of change of y with respect to x at $x=x_{0}$

F $t,$ i.e.,if $x=f(t)and y=g(t)$ , then by Chain Rule

$$\frac{dy}{dx}=\frac{dy}{dt}\bigg/\frac{dx}{dt},\quad if\quad\frac{dx}{dt}\neq0.

$$

Thus, the rate of change ofy with respect to x can be calculated using the rate of change of y and that of x both with respect to t.

Let us consider some examples.

Example1 Find the rate of change of the area of a circle per second with respect to its radius r when $r=5cm$

Solution The area A of a circle with radius r is given by $A=\pi r^{2}$ .Therefore, the rate

of change of the area A with respect to its radius r is given by $\frac{dA}{dr}=\frac{d}{dr}\left(\pi r^{2}\right)=2\pi r$

When $r=5cm,\frac{dA}{dr}=10\pi$ . Thus, the area of the circle is changing at the rate of

$10\pi\mathrm{c m^{2}/s}$

Example2 The volume of a cube is increasing at a rate of 9 cubic centimetres per second. How fast is the surface area increasing when the length of an edge is 10centimetres ?

Solution Let x be the length of a side, V be the volume and S be the surface area of the cube. Then,$V=x^{3}and S=6x^{2}$ where x is a function of time .

Now

Therefore

or

Now

<div style="text-align: center;"><img src="imgs/img_in_image_box_277_791_342_856.jpg" alt="Image" width="6%" /></div>

$$

not to \begin{aligned}\frac{d V}{d t}&=\frac{d V}{d t}\cdot\frac{d V}{d t}\\9&=\frac{d V}{d t}=\frac{d}{d t}(x^3)=\frac{d}{d x}(x^3)\cdot\frac{d x}{d t}\quad(By Chain Rule)\\&=3x^2\cdot\frac{d x}{d t}\\frac{d x}{d t}&=\frac{3}{x^2}\\frac{d S}{d t}&=\frac{d}{d t}(6x^2)=\frac{d}{d x}(6x^2)\cdot\frac{d x}{d t}\quad(By Chain Rule)\\&=12x\cdot\left(\frac{3}{x^2}\right)=\frac{36}{x}\quad(Using(1))\end{aligned}

$$

Hence, when $x=10cm,\frac{dS}{dt}=3.6cm^2/s$

Example 3 A stone is dropped into a quiet lake and waves move in circles at a speed of 4cm per econd.At theinstan,whentheradiusof thecircular wave is10cm, how fast is the enclosed area increasing?

Solution The area A of a circle with radius r is given by $A=\pi r^{2}$ . Therefore, the rate of change of area A with respect to time t is

$$

\frac{dA}{dt}=\frac{d}{dt}(\pi r^2)=\frac{d}{dr}(\pi r^2)\cdot\frac{dr}{dt}=2\pi r\cdot\frac{dr}{dt}

$$

It is given that

$$

\frac{dr}{dt}=4cm/s 

$$

Therefore, when $r=10cm$ $\frac{dA}{dt}=2\pi(10)(4)=80\pi$

Thus,,$r=10$ cm cid:1)

Note $\frac{d y}{d x}$ ispositiveiincrasicaeandisngativeidcreas asx increases.

Example4 The length xof a rectangle is decreasing at the rate of 3 cm/minute and the width y is increasing at the rate of 2cm/minute. When $x=10cm and y=6cm,$ , find the rates of change of (a) the perimeter and (b) the area of the rectangle.

Solution Sincethe length is decreasing and the width is increasing with respet to time, we have Q

$$

\frac{dx}{dt}=-3\ cm/min\quad and\quad\frac{dy}{dt}=2\ cm/min 

$$

(a) The perimeter P of a rectangle is given by

$$

P=2(x+y)

$$

Therefore

$$

\frac{dP}{dt}=2\left(\frac{dx}{dt}+\frac{dy}{dt}\right)=2(-3+2)=-2\mathrm{cm/min}

$$

(b)TheaAoteleisgivenby

$$

A=x\;.\;y 

$$

Therefore

$$

\left\{\begin{aligned}\frac{dA}{dt}&=\frac{dx}{dt}\cdot y+x\cdot\frac{dy}{dt}\\ &=-3(6)+10(2)\quad(as x=10cm and y=6cm)\\ &=2cm^2/min\end{aligned}\right.}

$$

Example 5 The total cost $\mathrm{C}(x)$ an item is given by

$$

C(x)=0.005x^{3}-0.02x^{2}+30x+5000

$$

Find the marginal cost when 3 units are produced, where by marginal cost we mean the instantaneous rate of change of total cost at any level of output.

Solution Since marginal cost is the rate of change of total cost with respect to the output, we have

Marginal

When

$$

\begin{aligned}\cot(MC)&=\frac{dC}{dx}=0.005(3x^2)-0.02(2x)+30\\x=3,\quad&MC=0.015(3^2)-0.04(3)+30\\&=0.135-0.12+30=30.015\end{aligned} ned 

$$

Hence, the required marginal cost is $\bar{\mathbb{Z}}30.02(nearly)$

ExampTlvuinudmlooroduct ned is given by $R(x)=3x^{2}+36x+5$ . Find the marginal revenue, when $\bar{x}=5$ , where by marginal revenue we mean the rate of change of total revenue with respect to the number of items sold at an instant.

Solution Since marginal revenue is the rateof changeoftotal revenue with respect to the number of units sold, we have

Hence, the required marginal revenue is † 66.

When

Marginal Revenue

$$

\frac{dR}{dx}=\frac{6x+36}{x}=5,\quad MR=6(5)+36=66.Hence, the required marginal revenue is † 66.

$$

### EXERCISE 6.1

1. Find therateofchangeof the areaof acircle with respectto its radius when (a)$r=3cm$ (b)$r=4\mathrm{c m}$

2. The volumeof a cube is increasing at the rate of 8 cm3/s.How fast is the surface area increasing when the length of an edge is 12 cm?

3. The radiusofacircle is increasing uniformly at therateof3 cm/s.Find the rate at which the area of the circle is increasing when the radius is 10 cm.

4. An edge of a variable cube is increasing at the rate of 3 cm/s. How fast is the volume of the cube increasing when the edge is 10 cm long?

5. A stone is dropped into a quiet lake and waves move in circles at the speed of 5 cm/s. At the instant when the radius of the circular wave is 8 cm, how fast is the enclosed area increasing?

6. The radiusofacircleisincreasing at therateof0.7cm/s.Whatis therae of increase of its circumference?

7. The length x of a rectangle is decreasing at the rate of 5 cm/minute and the width y is increasing at the rate of 4 cm/minute. When $x=8cm and y=6cm$ , find the rates of changeof (a) the perimeter, and (b) the area of the rectangle.

8. in 900 cubic centimetres of gas per second. Find the rate at which the radius of the balloon increases when the radius is 15 cm.

9. A balloon, which always remains spherical has a variable radius. Find the rate at which its volume is increasing with the radius when the later is 10 cm.

10. A ladder 5 m long is leaning against a wall. The bottom of the ladder is pulled along the ground, away from the wall, at the rate of 2cm/s. How fast is its height on the wall decreasing when the foot of the ladder is 4 m away from the wall ?11. A particle moves along the curve $6y=x^{3}+2$ . Find the points on the curve at which the y-coordinate is changing 8 times as fast as the x-coordinate.

12. The radius of an air bubble is increasing at the rate of $\frac{1}{2}cm/s$ . At what rate is the volume of the bubble increasing when the radius is 1 cm?

13. A balloon, which always remains spherical, has a variable diameter $\frac{3}{2}(2x+1)$ Find the rate of change of its volume with respect to .

14. Sand is pouringfrom a pipeatthe rateof12cm/s.Thefalling sandforms acone on the ground in such a way that the height of the cone is always one-sixth of the radius of the base. How fast is the height of the sand cone increasing when the height is 4 cm?

15. The total cost $\underline{{\mathrm{C}}}\left(x\right)$ in Rupees associated with the production of x units of an item is given by

$$

C\left(x\right)=0.007x^{3}-0.003x^{2}+15x+4000.

$$

Find the marginal cost when 17 units are produced.

16. The totalrevenue in Rupees receivedfrom thesaleofunitsof a product is

$$

R(x)=13x^{2}+26x+15.

$$

Find the marginal revenue when $x=7$

Choose the correct answer for questions 17 and 18.

17. The rateof changeoftheareaof acircle with respect toits radius r at $r=6$ cm is

(A)10π(B)12π(C)8π(D)11π

18. The total revenue in Rupees received from the sale of x units of a product is given by

$R(x)=3x^{2}+36x+5$ . The marginal revenue, when $x=15$ is

(A)116(B)96(C)90(D)126Ta]

### 6.3 Increasing and Decreasing Functions

Intis,leir decreasing or none.

Consider the function f given by $f(x)=x^{2},x\in\mathbf{R}$ The graph of this function is a parabola as given in Fig 6.1.

$$

f(x)=x^{2}

$$

$$

f(x)=x^{2}

$$

$$

f(x_{0})

$$

as we move from left to right, the height of the graph decreases

<div style="text-align: center;">as we move from left to right, the height of the graph increases </div>

<div style="text-align: center;">Fig 6.1</div>

First consider the graph (Fig 6.1) to the right of the origin. Observe that as we movefromttorihtlonteraphteitotherahontiuouslis.For this reason, the function is said to be increasing for the real numbers $x>0$

Now consider the graph to the left of the origin and observe here that as we move from left to right along the graph, the height of the graph continuously decreases.Consequently, the function is said to be decreasing for the real numbers $x\leq0$

We shall now give the following analytical definitions for a function which is increasing or decreasing on an interval.

Definition1 LetI be an interval contained in the domain of a real valued functionf.Then f is said to be

(i) increasing on $\mathrm{I}\mathrm{if}x_{1}<x_{2}\mathrm{in}\mathrm{I}\Rightarrow f(x_{1})\leq f(x_{2})\text{for all}x_{1},x_{2}\in\mathrm{I}$

_(ii) decreasing on I,$\mathrm{if}x_{1}<x_{2}\mathrm{in}\mathrm{I}\Rightarrow f(x_{1})\geq f(x_{2})$ EM $\mathrm{if}x_{1}<x_{2}\mathrm{in}\mathrm{I}\Rightarrow f(x_{1})\geq f(x_{2})$ for all $x_{_{1}},x_{_{2}}\in\mathrm{I}$

(ii) constant on I,$\mathrm{if}f(x)=c$ for all $x\in I$ , where c is a constant.

(iv) strictly increasing on I if $x_{1}<x_{2}in I\Rightarrow f(x_{1})<f(x_{2})for all x_{1},x_{2}\in I$

(v) strictly decreasing on I if $x_{1}<x_{2}\quad in\quad\quad f(x_{1})>f(x_{2})$ for all $x_{_1},x_{_2}\in\mathrm{I}$ For graphical representation of such functions see Fig 6.2.

<div style="text-align: center;">Neither Increasing nor Decreasing function (ii) </div>

<div style="text-align: center;">Fig 6.2</div>

We shall now define when a function is increasing or decreasing at a point.

Definition 2 Let $x_{0}$ beapoint in thedomaiof deiitionofal valued futio Then $f$ is said to be increasing, decreasing at $x_{0}if$ there exists an open interval I containing $x_{_0}$

Let us clarify this definition for the case of increasing function.

Example 7 Show that the function given by $f(x)=7x-3$ is increasing on R.

Solution Let $x_{t}$ and $x_{2}$ be any two numbers in R. Then

$$

x_{1}<x_{2}\Rightarrow7x_{1}<7x_{2}\Rightarrow7x_{1}-3<7x_{2}-3\Rightarrow f(x_{1})<f(x_{2})

$$

Thus, by Definition 1, it follows thatf is strictly increasing on R.

We shall now give the first derivative test for increasing and decreasing functions.The proof of this test requires the Mean Value Theorem studied in Chapter 5.

Theorem 1 Let f be continuous on [a, b] and differentiable on the open interval (a,b). Then

(a) is increasing in [a,b] i $f^{\prime}(x)\geq0$ for each $x\in(a,b)$

(b)f is decreasing in $[a,b]\mathrm{if}f'(x)\leq0$ for each $x\in(a,b)$

(c) f is a constant function in $[a,b]\mathrm{if}f'(x)=0$ for each $x\in(a,b)$

Proof (a) Let $x_{_1},x_{_2}\in[a,b]$ be such that $x_{1}<x_{2}$

Then, by Mean Value Theorem (Theorem 8 in Chapter 5), there exists a point c between $x_{1}$ and $x_{2}$ such that

i.e.

i.e.

$$

\begin{aligned}f(x_{2})-f(x_{1})&=f^{\prime}(c)(x_{2}-x_{1})\\f(x_{2})-f(x_{1})&>0\quad(as f^{\prime}(c)>0(given))\\f(x_{2})>f(x_{1})&=f^{\prime}(c)-f(x_{1})\end{aligned}

$$

Thus, we have

$$

x_{1}<x_{2}\Rightarrow f(x_{1})<f(x_{2}),\quad\mathrm{for}\quad\mathrm{all}x_{1},x_{2}\in[a,b]

$$

Hence $,f$ is an increasing function in [,].

The proofs of part (b) and (c) are similar. It is left as an exercise to the reader.

## Remarks

There is a more generalised theorem, which states that i $f f_{\mathcal{C}}(x)>0\mathrm{f o r}x$ in an interval excluding the end points andf is continuous in the interval, then fis increasing. Similarly,if $f_{\mathbb{C}}(x)<0$ for x in an interval excluding the end points andf is continuous in the interval, thenf is decreasing.

Example 8 Show that the function given by

is increasing on R.

Solution Note that

<div style="text-align: center;"><img src="imgs/img_in_image_box_285_786_351_850.jpg" alt="Image" width="7%" /></div>

$$

f(x)=x^{3}-3x^{2}+4x,x\in\mathbf{R}

$$

$$

\begin{aligned}\vec{f}^{\prime}(x)&=3x^{2}-6x+4\\&=3(x^{2}-2x+1)+1\\&=3(x-1)^{2}+1>0,in every interval of\mathbb{R}\end{aligned}

$$

Therefore, the function f is increasing on R.

Example 9 Prove that the function given by.$f(x)=\cos x$ is

(a) decreasing in (0, π)

(b) increasing in (, 2), and

(c) neither increasing nor decreasing in (0, 2).

Solution Note that $f^{\prime}(x)=-\sin x$

(a) Since for each $x\in(0,\pi),\sin x>0$ ,we have $f^{\prime}(x)<0$ and so f is decreasing in

$(0,\pi)$

(b) Since for each $x\in(\pi,2\pi)$ ,sin $x<0$ , we have $f^{\prime}(x)>0$ and so f is increasing in

$(\pi,2\pi)$

(c)Clearlby)nd)bov,iticino cang(,.

Example 10 Find the intervals in which the functionf given by $f(x)=x^{2}-4x+6$ is Q

(a) increasing (b)decreasing

Solution We have

or

$$

f(x)=x^{2}-4x+6

$$

<div style="text-align: center;">Fig 6.3</div>

Therefore,$f^{\prime}(x)=0\mathrm{~gives~}x=2$ . Now the point $x=2$ divides the real line into two disjoint intervals namely,$(-\infty,2)$ and (2, ∞) (Fig6.3).In the interval $(-\infty,2),f^{\prime}(x)=2x$

$-4<0$

Therefore, is decreasing in this interval.Also, in the interval $\left[\left(2,\infty\right),f^{\prime}\left(x\right)>0\right.]$ and so the function f is increasing in this interval.

Example 11 Find the intervals in which the functionf given by $f(x)=4x^{3}-6x^{2}-72x$ $\pm30$ is (a) increasing (b) decreasing

Solution We have

or

$$

\begin{aligned}f(x)&=4x^{3}-6x^{2}-72x+30\\f^{\prime}(x)&=12x^{2}-12x-72\\&=12(x^{2}-x-6)\\&=12(x-3)(x+2)\end{aligned}

$$

Therefore,$f^{\prime}(x)=0gives x=-2,3$ . The points $x=-2$ and $x=3$ divides the real line into three disjoint intervals, namely,$(-\infty,-2),(-2,3)$ and $(3,\infty)$ 1.

<div style="text-align: center;"><img src="imgs/img_in_chart_box_536_911_874_1133.jpg" alt="Image" width="36%" /></div>

<div style="text-align: center;">Fig 6.4</div>

In the intervals $(-\infty,-2)\mathrm{a n d}(3,\infty),f^{\prime}(x)$ is positive while in the interval $(-2,3)$ 1,$f^{\prime}(x)$ isnegative.Coqlthio $f$ is increasing in the intervals $(-\infty,-2)$ and (3,∞) whilethefunction is decreasing in the interval (−2,3).However,f is neither increasing nor decreasing in R.

<div style="text-align: center;"><html><body><table border="1"><tr><td>Interval</td><td>${\mathrm{S i g n~o f}}f^{\prime}(x)$</td><td>Nature of function f</td></tr><tr><td>$(-\infty,-2)$</td><td>$(-)\;(-)\geq0$</td><td>f is increasing</td></tr><tr><td>$(-2,3)$</td><td>$(-)\;(+)<0$</td><td>f is decreasing</td></tr><tr><td>(3,∞)</td><td>$(+)(+)>0$</td><td>f is increasing</td></tr></table></body></html></div>

(a) increasing (b) decreasing.which the function iven by $y f(x)=\sin3x,\;x\in\left[0,\frac{\pi}{2}\right]$ l $y f(x)=\sin3x,\;x\in\left[0,\frac{\pi}{2}\right]$ is

Solution We have

or

$$

f(x)=\sin3x 

$$

Therefore,$f^{\prime}(x)=0gives\cos3x=0which$ $3x=\frac{\pi}{2},\frac{3\pi}{2}(as x\in\left[0,\frac{\pi}{2}\right])$ implies $3x\in\left[0,\frac{3\pi}{2}\right]\quad\text{S o}x=\frac{\pi}{6}\quad\text{and}\quad\frac{\pi}{2}$ The point$x={\frac{\pi}{6}}$ divides the interval $\left[0,\frac{\pi}{2}\right]$ into two disjoint intervals $\left[0,\frac{\pi}{6}\right]\mathrm{a n d}\left(\frac{\pi}{6},\frac{\pi}{2}\right)$ 0π6元2

<div style="text-align: center;">Fig 6.5</div>

Now,$f^{\prime}(x)>0for all x\in\left[0,\frac{\pi}{6}\rightas0\leq x<\frac{\pi}{6}\Rightarrow0\leq3x<\frac{\pi}{2}]$ and $f^{\prime}(x)<0$ for all $x\in\left(\frac{\pi}{6},\frac{\pi}{2}\right)\quad as\quad\frac{\pi}{6}<x<\frac{\pi}{2}\Rightarrow\frac{\pi}{2}<3x<\frac{3\pi}{2}$

Therefore,f is increasing in $\left[0,\frac{\pi}{6}\right]$ and decreasing in $\left[\left(\frac{\pi}{6},\frac{\pi}{2}\right)\right.]$

Also, the given function is continuous at $x=0and x=\frac{\pi}{6}$ . Therefore, by Theorem 1,f is increasing on $\left[0,\frac{\pi}{6}\right]$ and decreasing on $\left[\frac{\pi}{6},\frac{\pi}{2}\right]$

Example13Findtheintervalsinwhichthefunctioniven

$f(x)=\sin x+\cos x,0\le x\le2\pi$ is increasing or decreasing.

$$

f(x)=\sin x+\cos x,0\le x\le2\pi is increasing or decreasing.

$$

Solution We have

or

$$

\begin{aligned}f(x)&=\sin x+\cos x,\\f^{\prime}(x)&=\cos x-\sin x\end{aligned}

$$

Now $f^{\prime}(x)=0$ gives sin $x=\cos x$ which gives that that $$

The points $x=\frac{\pi}{4}and x=\frac{5\pi}{4}$ divide the interval [0aalinte thtii 2π]into thredijoint iervals,namely,$\left[0,\frac{\pi}{4}\right,\left(\frac{\pi}{4},\frac{5\pi}{4}\right)\text{and}\left(\frac{5\pi}{4},2\pi\right])$ are $0\frac{\pi}{4}$ [T]$\frac{5\pi}{4}$ EMY 2π

Note that

$$

erer f^{\prime}(x)>0if x\in\left[0,\frac{\pi}{4}\right\cup\left(\frac{5\pi}{4},2\pi\right]CO 
)

$$

<div style="text-align: center;">Fig 6.6</div>

CO

or f is increasing in the intervals$\left[0,\frac{\pi}{4}\right\;\mathrm{a n d}\;\left(\frac{5\pi}{4},2\pi\right])$ Also 2$f^{\prime}(x)<0if x\in\left(\frac{\pi}{4},\frac{5\pi}{4}\right)$

or $f is decreasing in\left(\frac{\pi}{4},\frac{5\pi}{4}\right)$

<div style="text-align: center;"><html><body><table border="1"><tr><td>Interval</td><td>$\operatorname{S i g n\;o f}^{'}f^{\prime}(x)$</td><td>Nature of function</td></tr><tr><td>$\left[0,{\frac{\pi}{4}}\right]$</td><td>$\geq0$</td><td>f is increasing</td></tr><tr><td>$\left(\frac{\pi}{4},\frac{5\pi}{4}\right)$</td><td>$\leq0$</td><td>f is decreasing</td></tr><tr><td>$\left[\frac{5\pi}{4},2\pi\right]$</td><td>$\geq0$</td><td>f is increasing</td></tr></table></body></html></div>

### EXERCISE 6.2

1. Show that the function given by $f(x)=3x+17$

2. Show that the function given by $f(x)=e^{2x}$ is increa

3. Show that the function given by $f(x)=\sin x$ is

(a) increasing in $\left(0,\frac{\pi}{2}\right)$ $\operatorname{decreasing}\left(\frac{\pi}{2},\pi\right)$

(c) neither increasing nor decreasing in (0, π)

4. Find the intervals in which the functionf given by $f(x)=2x^2-3x$ is

(a) increasing (b)decreasing

5. Find the intervals in which the functionf given by.$f(x)=2x^{3}-3x^{2}-36x+7$ is (a) increasing (b)decreasing

6. Find the intervals in which the following functions are strictly increasing or decreasing:

(a)$x^{2}+2x-5$ (b)$10-6x-2x^{2}$ (c)$-2x^{3}-9x^{2}-12x+1$ (d)$6-9x-x^{2}$ (e)$(x+1)^{3}(x-3)^{3}$

7. Show that $y=\log(1+x)-\frac{2x}{2+x}$ ,is an increasing function of x throughout its domain.

8. Find the values of x for which $y=[x(x-2)]^2$ is an increasing function.

9. Prove that $y=\frac{4\sin\theta}{(2+\cos\theta)}-\theta$ is an increasing function of θ in $\left[0,\frac{\pi}{2}\right]$

10. Prove that the logarithmic function is increasing on $(0,\infty)$ 1.

11. Prove that the function f given by $f(x)=x^{2}-x+1$ is neither strictly increasing nor decreasing on $(-1,1)$

12. Which of the following functions are decreasing on $0,\frac{\pi}{2}\quad?$

(A) cos x (B)$\cos2x$ (C) cos 3x (D)tan x

13. On which of the following intervals is the functionf given by $f(x)=x^{100}+\sin x-1$ decreasing ?a

(A) (0,1)(B)$\frac{\pi}{2},\pi$ (C)$0,\frac{\pi}{2}$ (D) None of thes 。

14. For what values of a the functionf given by $f(x)=x^{2}+ax+1$

[1, 2]?

15.$f(x)=x+\frac{1}{x}$ ,is increasing on I.fomm $$

 Prove that thefunction given by

16. Prove that the function $f g i v e n b y f(x)=\log\sin x$ $f g i v e n b y f(x)=\log\sin x$ is increasing on $\left(0,\frac{\pi}{2}\right)$ and decreasing on $\left(\frac{\pi}{2},\pi\right)$

17. Prove that the function f given by $f(x)=\log\left|\cos x\right|$ is decreasing on $\left(0,\frac{\pi}{2}\right)$ and increasing on $\left(\frac{3\pi}{2},2\pi\right)$

18. Prove that the function given by.$f(x)=x^{3}-3x^{2}+3x-100$ is increasing in R.19.The interval in which $y=x^{2}e^{-x}$ is increasing is

(A)$(-\infty,\infty)$ (B)$(-2,0)$ (C) (2, ∞)(D) (0,2)

### 6.4 Maxima and Minima

In this section, we will use the concept of derivatives to calculate the maximum or minimum values of various functions. In fact, we will find the 'turning points' of the graph of a function and thus find points at which the graph reaches its highest (or lowest) locally.Thekoweeofuc tsisr uflikteraphof a given function. Further, we will also find the absolute maximum and absolute minimum ofafu.

1. ....

(i) The profit from a grove of orange trees is given by $P(x)=ax+bx^2$ , where $a,b$ are constant andisthenumberoforangetres per acre.How manytrees per acre will maximise the profit?

(iAlllrlat given by $h(x)=60+x-\frac{x^2}{60}$ , where x is the horizontal distance from the building and $h(x)$ is the height of the ball . What is the maximum height the ball will reach?

(ii) An Apache helicopter of enemy is flying along the path given by the curve $f(x)=x^{2}+7$ . A soldier, placed at the point (1, 2), wants to shoot the helicopter when it is nearest to him. What is the nearest distance

Ineach oftheabove problem,there is omethingcommoniwe wishto find out the maximum or minimum values of the given functions. In order to tackle such problems,we first formally define maximum or minimum values of a function, points of local maxima and minima and test for determining such points.

Definition 3 Letf be a function defined on an interval I. Then

(a)f is said to have a maximum value in I, if there exists a point c in I such that

$f(c)>f(x),\mathrm{forall}x\in\mathrm{I}.$

The number $f(c)$ is called the maximum value off in I and the point c is called a point of maximum value of f in I.

(b) is said to have a minimum value in I, if there exists a point c in I such that

$f(c)<f(x),\quad for\quad all\quad x\in\mathbb{I}$

The number $f(c)$ , in this case, is called the minimum value off in I and the point $c,$ in this case, is called a point of minimum value of in I.

(c) f is said to have an extreme value in I if there exists a point c in I such that $f(c)$ is either a maximum value or a minimum value off in I.

The number $f(c)$ , in this case, is called an extreme value of f in I and the point c is called an extreme point.

Remark Inig6.7a),)and, wehaveexhibidthtraphofcertaiparticular functions help us to find maximum value and minimum value at a point. Infact, through graphs, we can even find maximum/minimum value of a function at a point at which it is not even differentiable (Example 15).

<div style="text-align: center;"><img src="imgs/img_in_image_box_94_134_841_395.jpg" alt="Image" width="79%" /></div>

<div style="text-align: center;">Fig 6.7</div>

Example 14 Find the maximum and the minimum values, if any, of the functionf given by i

$$f(x)=x^{2},x\in\mathbb{R}.

$$

have Solut $f(x)=0if x=0$ . Also c

$$

f(x)\geq0,for all x\in\mathbf{R}.

$$

Theref m ff of minimum value of $f\mathrm{is}\;x=0$ .Further, it may be observed fromthei and hence no point of maximum value of in R.

Notef werestrictthedomainof t[2,] only,thenf will have maximum value $(-2)^{2}=4\mathrm{at}x=-2$

<div style="text-align: center;"><img src="imgs/img_in_image_box_592_851_876_1106.jpg" alt="Image" width="30%" /></div>

<div style="text-align: center;">Fig 6.9</div>

Example 15 Find the maximum and minimum values of f,if any, of the function gienb $f(x)=|x|,x\in\mathbb{R}$ Solution From the graphof the given function (Fig 6.9) , note that

$f(x)\geq0$ , for all $x\in\mathbb{R}$ and $f(x)=0if x=0$

Therefore, the functionf has a minimum value 0and the point of minimum value of $f\mathrm{is}x=0.\mathrm{Als}0$ ,the graph clearly shows thatf has no maximum value in R and hence no point of maximum value in R.

## Note

<div style="text-align: center;"><img src="imgs/img_in_image_box_626_440_878_750.jpg" alt="Image" width="26%" /></div>

<div style="text-align: center;">Fig 6.8</div>

(i)$|-2|=2$ r

(i) One may note that the function in Example27 is not differentiable at

$x=0$

Example 16 Find the maximum and the minimum values, if any, of the function given by

$$

f(x)=x,x\in(0,1).

$$

Solution The given function is an increasing (strictly) function in the given interval (0, 1). From the graph (Fig6.10) of the function $f$ , it seems that, it should have the minimum value at a point closest to 0 on its right and the maximum value at a point closest to l on its left. Are such points available? Of course, not. It is not possible to locate such points. Infact, if a point $x_{0}$ is closest to 0, then we find $\frac{x_{0}}{2}<x_{0}$ for all $x_{0}\in(0,1)$ .Aso if $f_{x_{1}}$ is closest

to 1, then $\frac{x_{1}+1}{2}>x_{1}$ for all $x_{1}\in(0,1)$

<div style="text-align: center;"><img src="imgs/img_in_chart_box_577_345_865_597.jpg" alt="Image" width="30%" /></div>

<div style="text-align: center;">Fig 6.10</div>

Therefore, the given function has neither the maximum value nor the minimum value in the interval (0,

Remark The reader may observe that in Example 16, if we include the points 0 and 1in the domain of , i.e., if we extend the domain of f to [0,1], then the function $f$ has minimum value 0 at $x=0$ and maximum value l at $x=1$ .Infact, we have the following results (The proof of these results are beyond the scope of the present text)

Every monotonic function assumes its maximum/minimum value at the end points of the domain of definition of the function.

A more general result is

Every continuous function on a closed interval has a maximum and a minimum value.

Note]By a monotonic functionfin an interval I, we mean thatfis either increasing in I or decreasing in I.

Maximum and minimum values of a function defined on a closed interval will be discussed later in this section.

Let us now examine the graph of a function as shown in Fig 6.1. Observe that at points A, B, C and D on the graph, the function changes its nature from decreasing to increasing or vice-versa. These points may be called turning points of the given function.Furthrbrvetat atturig poits,teraphater lilellr a litle valley. Roughly speaking, the function has minimum value in some neighbourhood (interval) of each of the points A and C which are at the bottom of their respective <div style="text-align: center;"><img src="imgs/img_in_image_box_229_137_726_396.jpg" alt="Image" width="53%" /></div>

<div style="text-align: center;">Fig 6.11</div>

valleys. Similarly, the function has maximum value in some neighbourhood of points B a may be regarded as points of local minimum value (or relative minimum value) and pointsBndDmayerddapiof localaximumaluorlativemaximum value) for the function.The local maximum value and local minimum value of the functillon.

We now formally give the following definition

Definito4tblludubieomain off. Then

(a) c is called a point of local maxima if there is an $h>0$ such that

$$

f(c)\geq f(x),\quad for all x in(c-h,c+h),x\neq c 

$$

The value $f(c)$ is called the local maximum value of f.

(b) c is called a point of local minima if there is an $h\geq0$ such that

$$

f(c)\leq f(x),\quad for all x in(c-h,c+h)

$$

The value $f(c)$ is called thelocalminimum valueoff.

Geometrically, the above definition states that if $x=c$ is a point of local maxima of $f,$ then the graph off around c will be as shown in Fig $6.12(a)$ . Note that the functionf is increasing $(\mathrm{i.e.},\dot{f}'(x)>0)$ in the nterval $(c-h,c)$ and decreasing $(\mathrm{i.e.},f^{\prime}(x)<0)$ in the interval $(c,c+h)$

This suggests that $f^{\prime}(c)$ must be zero.

$$

f^{\prime}(c)=0

$$

$$

increasing f^{\prime}(c)=0

$$

Similarly,iipoitofloal miimaoffththeaphoffroundlbas shown in Fig 6.14(b). Heref is decreasing $(\mathrm{i.e.},f^{\prime}(x)<0)$ in the interval $(c-h,c)$ and increasing $(\mathrm{i.e.},f'(x)>0)$ in the interval $(c,c+h)$ 1. This again suggest that $f^{\prime}(c)$ must be zero.

The above discussion lead us to the following theorem (without proof).

Theorem 2 Let f be a function defined on an open interval I. Suppose $c\in\mathrm{I}$ be any point. Iff has a local maxima or a local minima at $x=c.$ , then either $f^{\prime}(c)=0$ orf is not differentiable at .

Remark The converse of above theorem need not be true, that is, a point at which the derivative vanishes need not be a point of local maxima or local minima.For example, if $f(x)=x^{3}$ ,then $f^{\prime}(x)=3x^{2}$ and so $f^{\prime}(0)=0$ .But O is neither a point of local maxima nor a point of local minima (Fig 6.13).

Note]Apointcin the domain oa functionfat which either $f^{\prime}(c)=0$ or f is not differentiable is called a critical point off.Note that iffis continuous at c and $f^{\prime}(c)=0$ , then there exists an $h\geq0$ such that f is differentiable in the interval

$(c-h,c+h)$

<div style="text-align: center;">Fig 6.13</div>

$$

f(x)=x^{3}

$$

We shall now give a working rule for finding points of local maxima or points of local minima using only the first order derivatives.

Theorem 3 (First Derivative Test) Letf be a function defined on an open interval I Letf be continuous at a critical point c in I. Then

(i)$\operatorname{I f}f^{\prime}(x)$ changes sign from positive to negative as increases through c, i.e., if $f^{\prime}(x)>0$ at every pointsuficientlycloseto and to the left of $c,$ and $f^{\prime}(x)<0$ at every point sufficientlyclose to and to the rightof ,then is a point of local maxima

(ii)$\mathrm{If}f^{\prime}(\underline{x})$ changes sign from negative to positive as x increases through $c.$ i.e., if $f^{\prime}(x)<0$ at every point sufficiently close to and to the lefft of $c,$ and $f^{\prime}(x)>0$ at every $c_{z}$ then c is a point of local minima.

(iii)$\operatorname{I f}f^{\prime}(x)$ does not change sign as x increases through c, then c is neither a point of local maxima or apoint of local minima.Infact,such a point iscalled point of inflection (Fig 6.13).

Nooumal f. Similalyo li,$f(c)$ isa localminimumvalueoff

Figures 6.13 and 6.14, geometrically explain Theorem 3.

<div style="text-align: center;"><img src="imgs/img_in_chart_box_166_273_803_580.jpg" alt="Image" width="68%" /></div>

<div style="text-align: center;">Fig 6.14</div>

Example17 Find all points of local maxima and local mi nimaof the function f given by

$$

f(x)=x^{3}-3x+3

$$

Solution We have

or or

$$

\begin{aligned}f(x)&=x^{3}-3x+3\\f^{\prime}(x)&=3x^{2}-3=3(x-1)(x+1)\\f^{\prime}(x)&=0\mathrm{at}x=1\mathrm{and}x=-1\end{aligned}

$$

Thus,$x=\pm1$ arethe onlyctial poits whichcould psiblyethepits o local maxima and/or local minima off . Let us first examine the point $x=1$

Note that for values close to 1 and to the right of 1$f^{\prime}(x)>0$ andfor values close to 1 and to the left of 1.$f^{\prime}(x)\leq0$ . Therefore, by first derivative test,$x=1$ is a point of local minima and local minimum value is $f(1)=1$ . In the case of $x=-1$ ,note that $f^{\prime}(x)>0$ , for values close to and to the left of –1 and $f^{\prime}(x)<0$ , for values close to and to the right of–1.Therefore, by first derivative tst,$x=-1$ is a point of local maxima and local maximum value is $f(-1)=5$

<div style="text-align: center;"><html><body><table border="1"><tr><td>Values of x</td><td>Sign $f^{\prime}(x)=3(x-1)(x+1)$</td><td></td></tr><tr><td>/to the right (say 1.1 etc.) Close to 1 to the left (say 0.9 etc.)</td><td>>0 <0</td><td></td></tr><tr><td>Close to -1</td><td>/to the right (say –0.9 etc.) to the left (say −1.1 etc.)</td><td><0 >0</td></tr></table></body></html></div>

Example 18 Find all the points of local maxima and local minima of the function f given by

$$

f(x)=2x^{3}-6x^{2}+6x+5

$$

Solution We have

or

or

$$

\begin{aligned}f(x)&=2x^{3}-6x^{2}+6x+5\\f^{\prime}(x)&=6x^{2}-12x+6=6(x-1)^{2}\\f^{\prime}(x)&=0\quad at\quad x=1\end{aligned}

$$

Thus,$x=1$ is the only critical point off.We shall now examinethis point for local maxima and/or local minima off. Observe that $f^{\prime}(x)\geq0$ , for all $x\in\mathbb{R}$ . and in particular $f^{\prime}(x)>0.$ ,for values close to l and to the left and to the right of 1. Therefore, by first derivative test, the point $x=1$ is neither a point of local maxima nor a point of local minima. Hence $x=1$ is a point of inflexion.

Remark One may note that since $f^{\prime}(x)$ 1,in Example 30, never changes its sign on R,graph off has no turning points and hence no point of local maxima or local minima.

We shall now give another test to examine local maxima and local minima of a given function. This test is often easier to apply than the first derivative test.

Theorem 4 (Second Derivative Test) Let be a function defined on an interval I and $c\in\mathrm{I.~L e t}f$ be twice differentiable at c. Then

(i)$x=c$ is a point of local maxima ii $\mathrm{f}f^{\prime}(c)=0\text{and}f^{\prime\prime}(c)<0$

The value $f(c)$ is local maximum value of f

(ii)$x=c$ is a point of local minima if $f^{\prime}(c)=0\ \mathrm{and}\ f^{\prime\prime}(c)>0$

In this case,$,f(c)$ is local minimum value of f.

(ii) The test fails if $f^{\prime}(c)=0\text{and}f^{\prime\prime}(c)=0$

In this case, we go back to the first derivative test and find whether c is a point of local maxima, local minima or a point of inflexion.

Y

Note] Asf is twice differentiableat $c,$ we mean second order derivative off exists at c.

Example 19 Find local minimum value of the function f given by $f(x)=3+|x|,x\in\mathbb{R}$

Solution Note that the given function is not differentiable at $x=0$ . So, second derivative test fails. Let us try first derivative test. Note that O is a critical point off . Now to the left of $0,f(x)=3-x$ :and so $f^{\prime}(x)=-1<0$ .Also to

<div style="text-align: center;">Fig 6.15</div>

$$

$f (x)   $\dot{\cdot}\times\dot{\cdot}

$$

the right of $0,f(x)=3+x\mathrm{\ and\ so\ }f^{\prime}(x)=1>0$ . Therefore, by first derivative test,$x=$ O is a point of local minima of f and local minimum value of $f\mathrm{is}f(0)=3$

Example20Find local maximum and local minimumvaluesofthefunction iveny

$$

f(x)=3x^{4}+4x^{3}-12x^{2}+12

$$

Solution We have

or

$$

\begin{align*}f(x)&=3x^{4}+4x^{3}-12x^{2}+12\\f^{\prime}(x)&=12x^{3}+12x^{2}-24x=12x(x-1)(x+2)\end{align*}

$$

or

$$

f^{\prime}(x)=0\text{at}x=0,x=1\text{and}x=-2.

$$

Now

$$

f^{\prime\prime}(x)=36x^{2}+24x-24=12(3x^{2}+2x-2)

$$

or

$$

\begin{cases}f''(0)&=-24<0\\f''(1)&=36>0\\f''(-2)&=72>0\end{cases}

$$

maximum value of Therefore, by second derivative test,$\begin{aligned}fatx=0is f(0)=12while x=1and x=-2\end{aligned}$ $x=0$ s a point of lo $\begin{aligned}fatx=0is f(0)=12while x=1and x=-2\end{aligned}$ ,are the points of local minima and local minimum values of $\begin{aligned}fatx=-1and-2are f(1)=7and f(-2)=-20\end{aligned}$ respectively.

Example 21 Find all the points of local maxima and local minima of the functionf given by

Solution We have

<div style="text-align: center;"><img src="imgs/img_in_image_box_277_781_340_844.jpg" alt="Image" width="6%" /></div>

$$

f(x)=2x^{3}-6x^{2}+6x+5

$$

or

$$

\begin{aligned}f(x)&=2x^{3}-6x^{2}+6x+5\\begin{cases}f^{\prime}(x)=6x^{2}-12x+6=6(x-1)^{2}\\f^{\prime\prime}(x)=12(x-1)\end{cases}\end{aligned}

$$

Now $f^{\prime}(x)=0\quad gives x=1.Also f^{\prime\prime}(1)=0$ . Therefore, the second derivative test fails in this case. So, we shall go back to the first derivative test.

We have already seen (Example 18) that, using first derivative test,$x=1$ is neither a point of local maxima nor a point of local minima and so it is a point of inflexion.

Example 22 Find two positive numbers whose sum is 15 and the sum of whose squares is minimum.

Solution Let one of the numbers be x. Then the other number is $(15-x)$ Let S(x)denote the sum of the squares of these numbers. Then

or

$$

\begin{array}{c}\mathrm{S}(x)=x^{2}+(15-x)^{2}=2x^{2}-30x+225\\begin{cases}\mathrm{S}^{\prime}(x)=4x-30\\mathrm{S}^{\prime\prime}(x)=4\end{cases}\end{array}

$$

Now $\mathrm{S}^{\prime}(x)=0$ gives $x=\frac{15}{2}.\mathrm{Also}\mathrm{S}^{\prime\prime}\left(\frac{15}{2}\right)=4>0.$ . Therefore, by second derivative test,$x=\frac{15}{2}$ is the point of local minima of S. Hence the sum of squares of numbers is minimum when the numbers are $\frac{15}{2}\bmod15-\frac{15}{2}=\frac{15}{2}$ sitive numbers.whose sum is k and the sum of whose squares is minimum, are $\frac{k}{2}\bmod\frac{k}{2}$

Example 23 Find the shortest distance of point (0,from the parabola $y=x^{2}$ where $\frac{1}{2}\leq c\leq5$

Solution Let $(h,k)$ be any point on the $parabola y=x^{2}$ Let D be the required distance between $(h,k)$ and $(0,c)$ .Then

$$

\mathrm{D}=\sqrt{(h-0)^{2}+(k-c)^{2}}=\sqrt{h^{2}+(k-c)^{2}}

$$

Since (h, ) lies on the parabola $y=x^{2}$ , we have $k=h^{2}$ . So (1) gives not to

or

Now

$$

not to \begin{aligned}D&=D(k)=\sqrt{k+(k-c)^2}\\ D^{\prime}(k)&=\frac{1+2(k-c)}{2\sqrt{k+(k-c)^2}}\\ D^{\prime}(k)&=0gives k=\frac{2c-1}{2}\end{aligned}

$$

Observe that when $k<\frac{2c-1}{2}$ ,then $2(k-c)+1<0,\mathrm{i.e.},\mathrm{D}'(k)<0$ . Also when $k>\frac{2c-1}{2}$ ,then $\mathrm{D}^{\prime}(k)>0$ . So, by first derivative test, D (k) is minimum at $k=\frac{2c-1}{2}$

Hence, the required shortest distance is given by

$$

\mathrm{D}\left(\frac{2c-1}{2}\right)=\sqrt{\frac{2c-1}{2}+\left(\frac{2c-1}{2}-c\right)^2}=\frac{\sqrt{4c-1}}{2}

$$

Note The reader may note that in Example 35, we have used first derivative test instead of the second derivative test as the former is easy and short.

Example 24 Let AP and BQ be two vertical poles at points A and B, respectively.$\mathrm{If}\mathrm{AP}=16\mathrm{m},\mathrm{BQ}=22$ m and $AB=20$ m, then find the distance of a point R on AB from the point A such that $\mathrm{RP}^{2}+\mathrm{RQ^{2}}$ is minimum.Solution Let R be a point on AB such that $\mathrm{AR}=x$ m.Then $\mathrm{RB}=(20-x)\mathrm{m}\quad(\mathrm{as}\mathrm{AB}=20\mathrm{m})$ ). From Fig 6.16,we have

and

Therefore

Let

<div style="text-align: center;"><img src="imgs/img_in_chart_box_613_370_885_648.jpg" alt="Image" width="29%" /></div>

<div style="text-align: center;">$$

 ; 6.16</div>

$$[T]0m  ; 6.16\mathrm{S}\equiv\mathrm{S}(x)=\mathrm{RP}^{2}+\mathrm{RQ}^{2}=2x^{2}-40x+1140.

$$

$$

\mathrm{S}\equiv\mathrm{S}(x)=\mathrm{RP}^{2}+\mathrm{RQ}^{2}=2x^{2}-40x+1140.

$$

Therefore

Now $\mathrm{S}'(x)=0\mathrm{~gives}x=10\mathrm{~Als}0\mathrm{~S}''(x)=4>0$ , for all x and so $S''(10)\geq0$ Therefore, by second derivative test,$x=10$ is the point of local minima of S. Thus, the distance of R from A on AB is $AR=x=10m$

Example 25 If length of three sides of a trapezium other than base are equal to 10cm,then find the area of the trapezium when it is maximum.

nTheequd

<div style="text-align: center;"><img src="imgs/img_in_chart_box_257_1054_715_1286.jpg" alt="Image" width="48%" /></div>

<div style="text-align: center;">Fig 6.17</div>

CQon AB.Let $\mathrm{AP}=x\mathrm{cm}$ .Note that $\Delta APD\sim\Delta BQC$ .Therefore,$QB=x cm$ . Also, by Pythagoras theorem,$\mathrm{DP}=\mathrm{QC}=\sqrt{100-x^{2}}$ . Let A be the area of the trapezium. Then or

$$

\begin{aligned}A\equiv A(x)&=\frac{1}{2}(sum of parallel sides)(height)\\&=\frac{1}{2}(2x+10+10)\left(\sqrt{100-x^2}\right)\\&=(x+10)\left(\sqrt{100-x^2}\right)\\ A'(x)&=(x+10)\frac{(-2x)}{2\sqrt{100-x^2}}+\left(\sqrt{100-x^2}\right)\\&=\frac{-2x^2-10x+100}{\sqrt{100-x^2}}\end{aligned} .éd 

$$

Now

$$

\mathrm{A}^{\prime}(x)=0\text{gives}2x^{2}+10x-100=0,\text{i.e.,}x=5\text{and}x=-10.

$$

Since x represents distance, it can not be negative.

So,

$$

x=5.\;Now 

$$

$$

\begin{aligned}\mathrm{A}^{\prime\prime}(x)&=\frac{\sqrt{100-x^{2}}(-4x-10)-(-2x^{2}-10x+100)\frac{(-2x)}{2\sqrt{100-x^{2}}}}{100-x^{2}}\\&=\frac{2x^{3}-300x-1000}{(100-x^{2})^{\frac{3}{2}}}\quad(\mathrm{on}\mathrm{sim}\mathrm{i})\end{aligned}

$$

or

$$

\mathrm{A}^{\prime\prime}(5)=\frac{2(5)^{3}-300(5)-1000}{\left(100-(5)^{2}\right)^{\frac{3}{2}}}=\frac{-2250}{75\sqrt{75}}=\frac{-30}{\sqrt{75}}<0

$$

Thus, area of trapezium is maximum at $x=5$ and the area is given by

$$

\mathrm{A}(5)=(5+10)\sqrt{100-(5)^{2}}=15\sqrt{75}=75\sqrt{3}\mathrm{~cm}^{2}

$$

Example 26 Prove that the radius of the right circular cylinder of greatest curved surface area which can be inscribed in a given cone is half of that of the cone.

Solution Let $OC=r$ be the radius of the cone and $OA=h$ be its height.Let a cylinder with radius $OE=x$ inscribed in the given cone (Fig 6.18). The height QE of the cylinder is given by

or

or

$$

\begin{aligned}\frac{\mathrm{QE}}{\mathrm{OA}}&=\frac{\mathrm{EC}}{\mathrm{OC}}\quad(since\Delta\mathrm{QEC}\sim\Delta\mathrm{AOC})\\frac{\mathrm{QE}}{h}&=\frac{r-x}{r}\\mathrm{QE}&=\frac{h(r-x)}{r}\end{aligned}

$$

Let S be the curved surface area of the given cylinder. Then

<div style="text-align: center;"><img src="imgs/img_in_image_box_602_145_877_469.jpg" alt="Image" width="29%" /></div>

<div style="text-align: center;">Fig 6.18</div>

$$

\mathrm{S}\equiv\mathrm{S}(x)=\frac{2\pi x h(r-x)}{r}=\frac{2\pi h}{r}(r x-x^{2}) E 

$$

or

$$

\left\{\begin{aligned}\mathrm{S}'(x)&=\frac{2\pi h}{r}(r-2x)\\ \mathrm{S}''(x)&=\frac{-4\pi h}{r}\end{aligned}\right.}

$$

$$

\mathrm{Now}\;\mathrm{S}'(x)=0\;\mathrm{gives}\;x=\frac{r}{2}\;\mathrm{Since}\;\mathrm{S}''(x)<0\;\mathrm{for}\;\mathrm{all}\;x,\;\mathrm{S}''\left(\frac{r}{2}\right)<0.\;\mathrm{So}\;x=\frac{r}{2}\;\mathrm{is}\;\mathrm{a}

$$

point of maxima of S.Hence,the radius ofthe cylinder of greatt curvd surace area which can be inscribed in a given cone is half of that of the cone.

# 6.4.1 Maximum and Minimum Values of a Function in a Closed Interval Let us consider a function f given by

$$

f(x)=x+2,x\in(0,1)

$$

Observe that the function is continuous on (0, 1) and neither has a maximum value nor has a minimum value. Further, we may note that the function even has neither a local maximum value nor a local minimum value.

However, if we extend the domain off to the closed interval [, 1], then still may not have a local maximum (minimum) values but it certainly does have maximum alue $3=f(1)$ and minimum value $2=f(0)$ . The maximum value 3 off at $x=1$ is called absolute maximum value (global maximum or greatest value) off on the interval [0, 1]. Similarly, the minimum value 2 of f at $x=0$ is called the absolute minimum value (global minimum or least value) off on [0, 1].

Consider the graph given in Fig 6.19 of a continuous function defined on a closed interval [a, d]. Observe that the function has a local minima at..$x=b$ and local <div style="text-align: center;"><img src="imgs/img_in_chart_box_234_125_736_428.jpg" alt="Image" width="53%" /></div>

<div style="text-align: center;">Fig 6.19</div>

minimum value isf(b).The function also has a local maxima at $x=c$ and local maximum value is $f(c)$

Also from the graph, it is evident thatf hasabsolute maximum value $f(a)$ and absolute minimum value $f(d)$ .Further note that the absolute maximum (minimum)value off is different from local maximum (minimum) value off.

We will now state two results (without proof) regarding absolute maximum and absolute minimum values of a function on a closed interval I.

Theorem 5 Letf be a continuous function on an interval $\mathrm{I}=[a,b]$ .Thenf has the absolute maximum value and f attains it at least once in I. Also, has the absolute minimum value and attains it at least once in I.

Theorem 6 Letf be a differentiable function on a closed interval I and let c be any interior point of I. Then

(i)$f^{\prime}(c)=0$ if f attains its absolute maximum value at c.

(ii)$f^{\prime}(c)=0$ if f attains its absolute minimum value at .

In view of the above results, we have the following working rule for finding absolute maximum and/or absolute minimum values of a function in a given closed interval [a, ].

## Working Rule

Step1: Findallcritical points ofin the interval,ie.,find points x where either $f^{\prime}(x)=0$ orfis not differentiable.

Step 2: Take the end points of the interval.

Step3: At all these points (listed in Step 1 and 2),calculatethe values of f.

Step 4: Identify the maximum and minimum values of out of the values calculated in Step 3. This maximum value will be the absolute maximum (greatest) value of f and the minimum value will be the absolute minimum (least) value of f.

Example27Findthe abolute maximum and minimum alue oafunctiongivn by

$$

f(x)=2x^{3}-15x^{2}+36x+1on the interval[1,5].

$$

Solution We have

or

$$

\begin{align*}f(x)&=2x^{3}-15x^{2}+36x+1\\f^{\prime}(x)&=6x^{2}-30x+36=6(x-3)(x-2)\end{align*}

$$

Note that $f^{\prime}(x)=0$ gives $x=2and x=3$

We shall now evaluate the value off at these points and at the end points of the interval [1, 5], i.e., at $x=1,x=2,x=3$ and at $x=5.\mathrm{~S}0$ ied

$$

\begin{aligned}f(1)&=2(1^{3})-15(1^{2})+36(1)+1=24,\\f(2)&=2(2^{3})-15(2^{2})+36(2)+1=29,\\f(3)&=2(3^{3})-15(3^{2})+36(3)+1=28,\\f(5)&=2(5^{3})-15(5^{2})+36(5)+1=56.\end{aligned} ied 

$$

Thus, we concludethat abolute maximum valueofon[1,5] is56,currig at $x=5$ , and absolute minimum value off on [1, 5] is 24 which occurs at $x=1$

Example 28 Find absolute maximum and minimum values of a functionf given by

Solution We have

or

$$

\begin{aligned}f(x)&=12x^{\frac{4}{3}}-6x^{\frac{1}{3}},x\in[-1,1]\\f(x)&=12x^{\frac{4}{3}}-6x^{\frac{1}{3}}\\f^{\prime}(x)&=16x^{\frac{1}{3}}-\frac{2}{x^{\frac{2}{3}}}=\frac{2(8x-1)}{x^{\frac{2}{3}}}\end{aligned}C 

$$

Thus,$f^{\prime}(x)=0\mathrm{~gives~}x=\frac{1}{8}$ . Further note that $f^{\prime}(x)$ is not defined at $x=0$ So the critical points $\mathrm{are}\;x=0\;\mathrm{and}\;x=\frac{1}{8}$ . Now evaluating the value of f at critical points $x=0,\frac{1}{8}$ and at end points of the interval $x=-1and x=1$ , we have

$$

f(-1)=12(-1)^{\frac{4}{3}}-6(-1)^{\frac{1}{3}}=18

$$

$$

f\left(\frac{1}{8}\right)=12\left(\frac{1}{8}\right)^{\frac{4}{3}}-6\left(\frac{1}{8}\right)^{\frac{1}{3}}=\frac{-9}{4}

$$

$$

f(1)=12(1)^{\frac{4}{3}}-6(1)^{\frac{1}{3}}=6

$$

Hence, we conclude that absolute maximum value of $f$ is 18 that occurs at $x=-1$ and absolute minimum value of $\mathrm{f}\mathrm{i}\mathrm{s}\frac{-9}{4}$ that occurs at $x=\frac{1}{8}$

Example 29 An Apache helicopter of enemy is flying along the curve given by $y=x^{2}+7$ . A soldier, placed at (3, 7), wants to shoot down the helicopter when it is nearest to him. Find the nearest distance.

Solution Foreach valueof x, the heliopter $\mathrm{'s}$ position is at point $(\bar{x},x^{2}+7)$ Therefore, the distance between the helicopter and the soldier placed at (3,7) is Let

or

$$

\sqrt{(x-3)^{2}+(x^{2}+7-7)^{2}},\quad\sqrt{(x-3)^{2}+x^{4}}.\quad f(x)=(x-3)^{2}+x^{4}\quad,\quad f^{\prime}(x)=2(x-3)+4x^{3}=2(x-1)(2x^{2}+2x+3)

$$

Thus,$f^{\prime}(x)=0gives x=1or2x^2+2x+3=0$ for which there are no real roots.Also,there arenond pointsoftheitrvaltobe added tothe t for which $f^{\prime}$ is zero,i.e., there is only one point, namely,$x=1$ The value of f at this point is given by $f(1)=(1-3)^{2}+(1)^{4}=5.Thus$ , the distance between the solider and the helicopter is

$\sqrt{f(1)}=\sqrt{5}$

Note that $\sqrt{5}$ is either a maximum value or a minimum value. Since

$$

\sqrt{f(0)}=\sqrt{(0-3)^2+(0)^4}=3>\sqrt{5}

$$

it follows that $\sqrt{5}$ is the minimum value of $\sqrt{f(x)}$ . Hence,$\sqrt{5}$ is the minimum distance between the soldier and the helicopter.

### EXERCISE 6.3

1. Find the maximum and minimum values, if any, of the following functions given by

$$

\begin{align*}(\mathrm{i})f(x)&=(2x-1)^2+3\quad&(\mathrm{ii})f(x)&=9x^2+12x+2\\(\mathrm{iii})f(x)&=-(x-1)^2+10\quad&(\mathrm{iv})g(x)&=x^3+1\end{align*}

$$

2. Find the maximum and minimum values, if any,of the following functions given by

$$

\begin{aligned}(i)&f(x)=|x+2|-1\quad&(ii)g(x)=-|x+1|+3\\ (iii)&h(x)=\sin(2x)+5\quad&(iv)f(x)=|\sin4x+3|\end{aligned}(v)

$$

(v)

$$

h(x)=x+1,x\in(-1,1)

$$

3. Findte local maximaand local miimaif any,ofthellowing functions. Find also the local maximum and the local minimum values, as the case may be:

$$

f(x)=x^{2}\quad(ii)\quad g(x)=x^{3}-3x shed 

$$

(i

$$

h(x)=\sin x+\cos x,0<x<\frac{\pi}{2}

$$

(iv)

$$

f(x)=\sin x-\cos x,\quad0<x<2\pi 

$$

(v)

$$

f(x)=x^{3}-6x^{2}+9x+15\quad(vi)\quad g(x)=\frac{x}{2}+\frac{2}{x},\quad x>0 shed 

$$

$$

shed g(x)=\frac{1}{x^{2}+2}\quad(\mathrm{vii})\quad f(x)=x\sqrt{1-x},\quad0<x<1

$$

Prove that the following functions do not have maxima or minima:

$$

(i)$f(x)=e^{x}\quad(\mathrm{i i})\quad g(x)=\log x

$$$\begin{array}{r}{\mathrm{(i i i)}\quad h\left(x\right)=x^{3}+x^{2}+x+1}\end{array}$ $$

5. Find the abolute maximum alue and the abolute miimum alue of the following functions in the given intervals:

$$

f(x)=x^{3},x\in[-2,2]\quad(ii)\ f(x)=\sin x+\cos x,x\in[0,\pi]

$$

(i)

$$

f(x)=4x-\frac{1}{2}x^{2},\;x\in\left[-2,\frac{9}{2}\right]\;(\mathrm{iv})\;f(x)=(x-1)^{2}+3,\;x\in[-3,1]

$$

6. Find the maximum profit that a company can make, if the profit function is given by

$$

p\left(x\right)=41-72x-18x^{2}

$$

7. Find both the maximum value and the minimum value of

$$

3x^{4}-8x^{3}+12x^{2}-48x+25on the interval[0,3].

$$

8. At what poitsintirval2,ethefunctioni2 aaiits maximum value?

9. What is the maximum value of the function sin $x+\cos x?$

10. Find the maximum value of $2x^{3}-24x+107$ in the interval [1, 3]. Find the maximum value of the same function in $[-3,-1]$

11. It is given that at $x=1$ , the function $x^{4}-62x^{2}+ax+9$ attains its maximum value,on the interval [0, 2].Find the value of a.

12. Find the maximum and minimum values of $x+\sin2x on[0,2\pi]$

13. Find two numbers whose sum is 24 and whose product is as large as possible.

14. Find two positive numbers and y such that $x+y=60$ and $x y^{3}$ is maximum.

15. Findtwo positivenumbersxandsuchthattheir sum is35 andthe product $x^{2}y^{5}$ is a maximum.

16. Find two positive numbers whose sum is 16 and the sum of whose cubes is minimum.

17. A square piece oftinof side18 cm is to be made into a box without to by cutting quem diurmeb should bete sieofthe squaretobecutoff sothatheolumeof thebox is the maximum possible.

18. Arectangular sheet oftin 45cmby24cm is to be made into abox without top,by cutting off square from each corner and folding up the flaps. What should be the side of thesquaretobecutoff sothat thevolumeofthebox is maximum?19.Show that of all the rectangles inscribed in a given fixed circle, the square has the maximum area.

20. Show that the right circular cylinder of given surface and maximum volume is such that its height is equal to the diameter of the base.

21. Of all the closed cylindrical cans (right circular), of a given volume of 100 cubic centimetres,find the dimensions of the can which has the minimum surface area?

22. A wire of length 28 m is to be cut into two pieces. One of the pieces is to be made into a square and the other into a circle. What should be the length of the two pieces so that the combined area of the square and the circle is minimum?23. Prove that the volume of the largest cone that can be inscribed in a sphere of radius R $\mathrm{is}\frac{8}{27}$ of the volume of the sphere.

24. Show that theright circularconeof leastcurved surface and givenvolume has an altitude equal to $\left\{\sqrt{2}\right.}$ time the radius of the base.

25. Show that the semi-vertical angle of the cone of the maximum volume and of given slant height is $\tan^{-1}{\sqrt{2}}$

26. Show htmivrtilagleofihticulooiveuraceaaand maximum volume is $\sin^{-1}\left(\frac{1}{3}\right)$

Choose the correct answer in Questions 27 and 29.

27. The point on the curve $x^{2}=2y$ which is nearest to the point (0, 5) is

(A)$(2\sqrt{2},4)$ (B)$(2\sqrt{2},0)$ (C)(0,0)(D)(2,2)

28. For all real values of x, the minimum value of $\frac{1-x+x^{2}}{1+x+x^{2}}$ is

(A)0(B)1(C)3-(D)$\frac{1}{3}$

29. The maximum value of $\left[x(x-1)+1\right]^{\frac{1}{3}},0\leq x\leq1$ is

(A)$\left(\frac{1}{3}\right)^{\frac{1}{3}}$ (B)$\frac{1}{2}$ (C) 1b (D)0

## les

Example 30 Acar starts from a pointPat time $t=0$ e nds nd p nt he ,distance x, in metres, covered by it, in t seconds is given by

$$

x=t^{2}\left(2-\frac{t}{3}\right)

$$

Find the time taken by it to reach Q and also find distance between P and Q.

LetvoeteveiocityOl

Now

$$

x=t^{2}\left(2-\frac{t}{3}\right)

$$

ore

$$

y=\frac{dx}{dt}=4t-t^2=t(4-t)

$$

Thus,$$

 [T]and/or $t=4$ −

Now $v=0$ at P as well as at Q and at [Ta]$P,t=0.\ So,at\ Q,t=4$ . Thus, the car will reach the point Q after4 seconds.Also the distance travelled in4 seconds is given by

$$x_{t=4}=4^{2}\left(2-\frac{4}{3}\right)=16\left(\frac{2}{3}\right)=\frac{32}{3}m 

$$

Example31Awater tank hasthe shapeof aninverted right circularcone with its axis vertical and vertex lowermost. Its semi-vertical angle is $\tan^{-1}(0.5)$ ). Water is poured into it at aconstant rateof5cubic metre per hour.Find the rate at whichthe level of the water is rising at the instant when the depth of water in the tank is 4 m.

Solution Let $r,$ hand α be as in Fig 6.20. Then tan $\alpha=\frac{r}{h}$

So

$$

\alpha=\tan^{-1}\left(\frac{r}{h}\right).

$$

But

$$

\alpha=\tan^{-1}(0.5)\quad(given)

$$

or

$$

\frac{r}{h}=0.5

$$

or

$$

r=\frac{h}{2}

$$

Let V be the volume of the cone. Then

<div style="text-align: center;"><img src="imgs/img_in_image_box_645_351_863_612.jpg" alt="Image" width="23%" /></div>

<div style="text-align: center;">Fig 6.20</div>

$$

V=\frac{1}{3}\pi r^{2}h=\frac{1}{3}\pi\left(\frac{h}{2}\right)^{2}h=\frac{\pi h^{3}}{12}

$$

Therefore

<div style="text-align: center;"><img src="imgs/img_in_image_box_272_777_336_842.jpg" alt="Image" width="6%" /></div>

$$

\frac{dV}{dt}=\frac{d}{dh}\left(\frac{\pi h^3}{12}\right)\cdot\frac{dh}{dt}

$$

$$

=\frac{\pi}{4}h^2\frac{dh}{dt}

$$

(by Chain Rule)

$\frac{dV}{dt}=5\ m^3/h and\ h=4\ m.$

Therefore

$$

5=\frac{\pi}{4}\left(4\right)^2\cdot\frac{dh}{dt}

$$

or

$$

\frac{dh}{dt}=\frac{5}{4\pi}=\frac{35}{88}m/h\left(\pi=\frac{22}{7}\right)

$$

Thus, the rate of change of water level is $\frac{35}{88}m/h$

Example 32 A man of height 2 metres walks at a uniform speed of 5 km/h away from a lamp post which is 6 metres high. Find the rate at which the length of his shadow increases.

Solution In Fig 6.21, Let AB be the lamp-post, the lamp being at the position B and let MN be the man at a particular time t and let $AM=l$ metres. Then, MS is the shadow of the man. Let $ MS=s$ metres.

Note that

$$

\Delta\mathrm{M S N}\sim\Delta\mathrm{A S B}

$$

or

$$

\frac{MS}{AS}=\frac{MN}{AB}

$$

or

$$

\mathrm{AS}=3s\left(\mathrm{as}\mathrm{MN}=\right.)

$$

<div style="text-align: center;"><img src="imgs/img_in_chart_box_592_152_896_408.jpg" alt="Image" width="32%" /></div>

<div style="text-align: center;">Fig 6.21</div>

2 and $AB=6(given)$ )

Thus

So

Therefore

$$

\begin{aligned}AM&=3s-s=2s.But AM=l\\l&=2s\\frac{dl}{dt}&=2\frac{ds}{dt}\end{aligned}

$$

Since $\frac{dl}{dt}=5\mathrm{km/h}$ $\frac{5}{2}km/h$

Example 33 Find intervals in which the function given by

$$

f(x)=\frac{3}{10}x^{4}-\frac{4}{5}x^{3}-3x^{2}+\frac{36}{5}x+11

$$

utionWehave

refore

$$

\begin{aligned}f(x)&=\frac{3}{10}x^{4}-\frac{4}{5}x^{3}-3x^{2}+\frac{36}{5}x+11\\f^{\prime}(x)&=\frac{3}{10}(4x^{3})-\frac{4}{5}(3x^{2})-3(2x)+\frac{36}{5}\\&=\frac{6}{5}(x-1)(x+2)(x-3)\quad(on simplification)\end{aligned}

$$

Now $f^{\prime}(x)=0\text{gives}x=1,x=-2,\text{or}x=3$ . The points $x=1,-2$ ,and 3 divide the real line into four -213disjoint intervals namely,"$(-\infty,-2),(-2,1),(1,3)$ Fig 6.22and (3, ∞) (Fig 6.22).

Consider the interval $(-\infty,-2)$ ,i.e.,$\mathrm{when}-\infty<x<-2$

In this case, we have $x-1<0,\\ x+2<0and x-3<0$

(In particular, observe that for $x=-3,f^{\prime}(x)=(x-1)(x+2)(x-3)=(-4)(-1)$ $(-6)<0$ E Therefore,$$

Thus, the function f is decreasing in $$

 .

Consider the interval $(-2,1)$ , i.e., when e 

$$ .

In this case, we have $$

 [Ta]

$=6>0$ (In particular, observe that for 

$$ (-))(−3)

So

$$

f^{\prime}(x)>0when-2<\underline{x}<\underline{1}.

$$

Thus,$$

$x-1>0,x+2>0and x-3\leq0.$ Now con),n , i.e., when $$

 .In this case, we have .n is , e a

So,

$$f^{\prime}(x)<0when1<x<3.

$$

Thus,3).

Finally, consider the interval $(3,\infty),i.e.$ ., when $x>3$ . In this case, we have $x-1>0$ $x+2>0$ and $x-3>0.\ \mathrm{So}\ f^{\prime}(x)>0$ when $x\geq3$

Thus, is increasing in the interval (3, ∞).

Example 34 Show that the functionf given by

$$

f(x)=\tan^{-1}(\sin x+\cos x),x>0

$$

is always an increasing function in $\left(0,\frac{\pi}{4}\right)$

Solution We have

Therefore

$$

f(x)=\tan^{-1}(\sin x+\cos x),x>0

$$

$$

\cos x-\sin x 

$$

(on simplification)

Note that $2+\sin2x>0\ for\ all\ x\ in\ \ 0,\frac{\pi}{4}$

$$

\begin{aligned}&Therefore\quad f^{\prime}(x)>0if\cos x-\sin x>0\\&for\quad f^{\prime}(x)>0if\cos x>\sin x or\cot x>1\end{aligned}

$$

Now

$$

\cot x>1\quad if\tan x<1,i.e.,if0<x<\frac{\pi}{4} ished 

$$

Thus

$$

f^{\prime}(x)>0in\left(0,\frac{\pi}{4}\right)

$$

Hence f is increasing function in $\left(0,\frac{\pi}{4}\right)$

Example 35 A circular disc of radius 3cm is being .Due to expansion, its radius increases at the rateof 0.05 cm/s.Find the rate at which its area is increasing when radius is 3.2 cm.

Solution Let r be the radius of the given disc and A be its area. Then

or

<div style="text-align: center;"><img src="imgs/img_in_image_box_274_789_339_855.jpg" alt="Image" width="6%" /></div>

$$

\frac{A=\pi r^{2}}{dt}=2\pi r\frac{dr}{dt}

$$

Now approximate rate of increase of radius $s=dr=\frac{dr}{dt}\Delta t=0.05cm/s$

Therefore, the approximate rate of increase in area is given by

$$

\mathrm{dA}=\frac{\mathrm{dA}}{\mathrm{dt}}(\Delta t)=2\pi r\left(\frac{\mathrm{d}r}{\mathrm{dt}}\Delta t\right)\\=2\pi(3.2)(0.05)=0.320\pi\mathrm{cm}^{2}\mathrm{~s}\quad(r=3.2\mathrm{~cm})

$$

Example 36 An open topped box is to be constructed by removing equal squares from each corner of a 3 metre by 8 metre rectangular shet of aluminium and folding up the sides. Find the volume of the largest such box.

Solution Let x metre be the length of a side of the removed squares.Then, the height of the box is x, length is $8-2x$ and breadth is $3-2x$ (Fig 6.23). If $\nabla(x)$ is the volume of the box, then

<div style="text-align: center;"><img src="imgs/img_in_image_box_189_247_810_393.jpg" alt="Image" width="66%" /></div>

<div style="text-align: center;">Fig 6.23</div>

$$

\begin{aligned}\mathrm{V}(x)&=x(3-2x)(8-2x)\\&=4x^3-22x^2+24x\end{aligned}

$$

Therefore

$$

\begin{cases}V'(x)=12x^2-44x+24=4(x-3)(3x-2)\\V''(x)=24x-44\end{cases} ished 

$$

Now

$$

V^{\prime}(x)=0\text{gives}x=3,\frac{2}{3}\text{But}x\neq3(Why?)

$$

Thus, we have $x=\frac{2}{3}.\;\;\mathrm{Now}\;V''\left(\frac{2}{3}\right)=24\left(\frac{2}{3}\right)-44=-28<0.$

Therefore,$x=\frac{2}{3}is the$ point of maxima, i.e., if we remove a square of side $\frac{2}{3}$ metre from each corner of the sheet and make a box from the remaining sheet, then the volume of the box such obtained will be the largest and it is given by

$$

ot t \begin{aligned}\frac{2}{3}\times\frac{1}{3}&=4\left(\frac{2}{3}\right)^3-22\left(\frac{2}{3}\right)^2+24\left(\frac{2}{3}\right)^3\\&=\frac{200}{27}m^3\end{aligned}

$$

ot t

Example 37 Manufacturer can sell x items at a price of rupees $\left(5-\frac{x}{100}\right)$ each. The cost price of x items is $\mathrm{RS}\left(\frac{x}{5}+500\right)$ . Find the number of items he should sell to earn maximum profit.

Solution Let $\operatorname{S}\left(x\right)$ be the selling price of x items and let $\mathrm{C}\left(x\right)$ be the cost price of items. Then, we have

and

$$

\mathrm{S}(x)=\left(5-\frac{x}{100}\right)x=5x-\frac{x^{2}}{100}

$$

Thus, the profit function $\operatorname{P}\left(x\right)$ is given by

$$

\mathrm{P}(x)=\mathrm{S}(x)-\mathrm{C}(x)=5x-\frac{x^{2}}{100}-\frac{x}{5}-500 'lished 

$$

i.e.

$$

\mathrm{P}(x)=\frac{24}{5}x-\frac{x^{2}}{100}-500 'lished 

$$

or

$$

\mathrm{P}^{\prime}(x)=\frac{24}{5}-\frac{x}{50}

$$

$$

\mathrm{Now}P^{\prime}(x)=0\text{gives}x=240.\mathrm{Also}P^{\prime\prime}(x)=\frac{-1}{50}\cdot\mathrm{So}P^{\prime\prime}(240)=\frac{-1}{50}<0 'lished 

$$

Thus,$x=240$ is a point of maxima.Hence, the manufacturer can earn maximum profit, if he sells 240 items.

## Miscellaneous Exercise on Chapter 6

1. Show that the function given by $f(x)=\frac{\log x}{x}$ has maximum at $x=e$

2. Thetwoequal sidesof anisoscelestriangle with fixedbaseare decreasing at the rate of 3 cm per second. How fast is the area decreasing when the two equal sides are equal to the base ?

3. Find the intervals in which the functionf given by

$$

f(x)=\frac{4\sin x-2x-x\cos x}{2+\cos x}

$$

is (i) increasing (ii) decreasing.

4. Find the intervals in which the functionf given by $f(x)=x^{3}+\frac{1}{x^{3}},x\ne0$ is

(i) increasing

(ii) decreasing.

5. Fidaulipe $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$ with its vertex at one end of the major axis.

6. Atank with rectangular base andrectangularsides,openat the top is to be constructed so that its depth is 2 m and volume is 8 m3. If building of tank costs Rs 70 per sq metres for the base and Rs 45 per square metre for sides. What is the cost of least expensive tank?

7. Thesumohimofclndsqureis,whreimeona.Prove that the sum of their areas is least when the side of square is double the radius of the circle.

8. A window is in the form of a rectangle surmounted by a semicircular opening.The total perimeter of the window is 10 m. Find the dimensions of the window to admit maximum light through the whole opening.

9. A point on the hypotenuse of a triangle is at distance a and from the sides of the triangle.

Show that the minimum length of the hypotenuse is $\left(a^{\frac{2}{3}}+b^{\frac{2}{3}}\right)^{\frac{3}{2}}$

10. Find the points at which the function f given by $f(x)=(x-2)^4(x+1)^3$ has (i) local maxima local minima

(i)point of inflexion

11. Find the absolute maximum and minimum values of the functionf given by

$$

f(x)=\cos^{2}x+\sin x,x\in[0,\pi]

$$

12. Show that the altitude of the right circular cone of maximum volume that can be inscribed in a sphere of radius $r\mathrm{i}\mathrm{s}\frac{4r}{3}$

13. Let f be a function defined on [a, b] such that $f^{\prime}(x)>0$ , for all $x\in(a,b)$ . Then prove thatf is an increasing function on (a, b).

14. Show that the height of the cylinder of maximum volume that can be inscribed in a sphere of radius R is $\frac{2\mathsf{R}}{\sqrt{3}}$ .Also find the maximum volume.

15. Show that height of the cylinder of greatest volume which can be inscribed in a right circular cone of height h and semi vertical angle α is one-third that of the cone and the greatest volume of cylinder is $\frac{4}{27}\pi h^{3}\tan^{2}\alpha$

16. Acllkoai1ibldwe14EaM

(A)1m/h (A (B)0.1 m/h (C)1.1 m/h (D)0.5 m/h

## Summary

■If aquantitwrt,ome rule $y=f(x)$ then $\frac{dy}{dx}\left(\mathrm{or}f'(x)\right)$ represents the rate of change ofy withepect and $\frac{dy}{dx}\left(\mathrm{or}f^{\prime}(x_0)\right)$ represents the rate of change

$x=x_{0}$

■If two variables x and y are varying wit ariable t, i.e., if $x=f(t)and y=g(t)$ , then by Chain Rule

$$

\frac{dy}{dx}=\frac{dy}{dt}\bigg/\frac{dx}{dt},\quad if\quad\frac{dx}{dt}\neq0.

$$

■A function is said to be

(a) increasing on an interval $(a,b)$ if

$$

x_{1}<x_{2}\quad in\quad(a,b)\Rightarrow f(x_{1})<f(x_{2})\quad for all\quad x_{1},x_{2}\in(a,b).

$$

Alternatively, if $f^{\prime}(x)\geq0$ for each x in (a, b)

(b) decreasing on (a,b) if

$$

x_{1}<x_{2}\quad\mathrm{in}\quad(a,b)\Rightarrow f(x_{1})>f(x_{2})\quad\mathrm{for}\quad\mathrm{all}\quad x_{1},x_{2}\in(a,b).$$

(c) constant in (a, b),$\mathrm{if}f(x)=c$ for all $x\in(a,b)$ , where c is a constant.

■A point c in the domain of a functionf at which either $f^{\prime}(c)=0$ or f is not differentiable is called a critical point off.

■First Derivative Test Letf beafunctiondefined on anopeninterval I.Let fbe continuous at a critical point c in I. Then

(i)$\operatorname{I f}f^{\prime}(x)$ changes sign from positive to negative asincreases through c,i.e.,$\operatorname{if}f^{\prime}(x)>0$ at every point sufficienlyclose to and to the left of c,and $f^{\prime}(x)<0$ at every point sufficientlyclosetoand totherightof c,then c is a point of local maxima.

(ii)$\operatorname{I f}f^{\prime}(x)$ changes sign from negative to positive as x increases through $c,$ i.e., if $f^{\prime}(x)<0$ at every point sufficiently close to and to the left of $c,$ and $f^{\prime}(x)>0$ at every point sufficiently close to and to the right of $c,$ then c is a point of local minima.

(iii)$\operatorname{I f}f^{\prime}(x)$ does not change sign as x increases through c, then c is neither apointof lcalmaximooitoloaliima.In,uchaoint is called point of inflexion.

■Second Derivative Test Letf be a function defined on an interval Iand $c\in\mathrm{I}$ Letf be twice differentiable at c. Then eral Iand

(i)$x=c$ is a point of local maxima $$

The values $f(c)$ is local maximum value of f .

(i)$x=c$ is a point of local minima $$

In this case,$f(c)$ is local minimum value of f .

(i) The test fails $\mathrm{if}f^{\prime}(c)=0\mathrm{and}f^{\prime\prime}(c)=0$

In this case, we go back to the first derivative test and find whether c is a point of maxima, minima or a point of inflexion.

■Working rule for finding absolute maxima and/or absolute minima

Step1: Findall critical pointsoffin theinterval,i.e.,find points x where either $f^{\prime}(x)=0$ orf is not differentiable.

Step 2:Take the end points of the interval.

Step3:At all these points (listed inStep1and2),calculatethevalues off.Step 4: Identify the maximum and minimum values off out of the values calculated in Step 3. This maximum value will be the absolute maximum value of f and the minimum value will be the absolute minimum value of f.