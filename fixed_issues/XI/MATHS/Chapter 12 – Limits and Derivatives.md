

# LIMITS AND DERIVATIVES 

## :With the Calculus asakey,Mathematics can be successfullyapplied to the explanation of the course of Nature – WHITEHEAD 

### 12.1 Introduction 

<div style="text-align: center;"><img src="imgs/img_in_image_box_631_502_868_842.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">Sir Issac Newton (1642-1727)</div>


This chapter is an introduction to Calculus.Calculus is that branch of mathematics which mainly deals with the study of change in the value of a function as the points in the domain change.First, we give an intuitive idea of derivative (without actually defining it). Then we give a naive definition of limit and study some algebra of limits. Then we come back to a definition of derivative and study some algebra of derivatives. We also obtain derivatives of certain standard functions.



### 12.2 Intuitive Idea of Derivatives 

Physical experiments have confirmed that the body droped from a tall cliff covers a distance of 4.9t2 metres in t seconds,

i.e., distance sin metres covered by the body as afunction oftime in seconds is given by $s=4.9t^{2}$ 



Theadjoiig Table.1ivtedacetavldinmtreataiouirvals of time in seconds of a body dropped from a tall cliff.



The objective is to find the veloctiy of the body at time $t=2$ seconds from this data. One way to approach this problem is to find the average velocity for various intervals of time ending at $t=2$ seconds and hope that these throw some light on the velocity at $t=2$ seconds.



Average velocity between $t=t_{1}$ and $t=t_{2}$ equals distance travelled between $t=t_{l}$ and $t=t_{z}$ seconds divided by $(t_{2}-t_{1})$ ). Hence the average velocity in the first two seconds 



$$\begin{aligned}&\mathrm{Distance\ revealed\ between\ }t_{2}=2\ and\ t_{1}=0,\\ &\mathrm{Time\ interval\ }(t_{2}-t_{1})\\ &=\frac{(19.6-0)m}{(2-0)s}=9.8m/s.\\ \end{aligned}$$

Similarly, the average velocity between $t=1$ and $t=2is$ 



$$\frac{(19.6-4.9)m}{(2-1)s}=14.7m/s $$

Likewise we compute the average velocitiy between $t=t_{1}$ and $t=2$ for various $t_{1}$ . The following Table 13.2 gives the average velocity (v),$t^{2}-t$ seconds and $t=2$ seconds.



<div style="text-align: center;">Table 12.1</div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>t</td><td>S</td></tr><tr><td>0</td><td>0</td></tr><tr><td>1</td><td>4.9</td></tr><tr><td>1.5</td><td>11.025</td></tr><tr><td>1.8</td><td>15.876</td></tr><tr><td>1.9</td><td>17.689</td></tr><tr><td>1.95</td><td>18.63225</td></tr><tr><td>2</td><td>19.6</td></tr><tr><td>2.05</td><td>20.59225</td></tr><tr><td>2.1</td><td>21.609</td></tr><tr><td>2.2</td><td>23.716</td></tr><tr><td>2.5</td><td>30.625</td></tr><tr><td></td><td>44.1</td></tr><tr><td></td><td>78.4</td></tr></table></body></html></div>


<div style="text-align: center;">Table 12.2</div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>$t_{1}$</td><td>0</td><td>1</td><td>1.5</td><td>1.8</td><td></td><td>1.95</td><td>1.99</td></tr><tr><td>V</td><td>9.8</td><td>14.7</td><td>17.15</td><td></td><td>19.11</td><td>19.355</td><td>19.551</td></tr></table></body></html></div>


From Table12.2, weobserve thatthe average velocity is gradually increasing.As we make the time intervals ending at $\bar{\mathcal{N}}=2$ smaller, we see that we get a better idea of the velocity at $t=2$ . Hoping that nothing really dramatic happens between 1.99seconds and 2 seconds, we conclude that the average velocity at $t=2$ seconds is just above 19.551m/s.



This conclusion is somewhat strengthened by the following set of computation.Compute the average velocities for various time intervals starting at $t=2$ seconds.As before the average velocity v between $t=2$ seconds and $t=t_{2}$ seconds is 

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_1053_216_1113.jpg" alt="Image" width="5%" /></div>


Dstanceo $t_{2}$ seconds 

$$t_{2}-2$$

Distance travelled in $t_{2}$ seconds–Ditceavlld2conds 

$$t_{2}-2$$

$$\frac{Distance traveled in t_2seconds-19.6}{t_2-2}$$

The following Table 12.3 gives the average velocity v in metres per second between $t=2$ seconds and $t_{2}$ seconds.



<div style="text-align: center;">Table 12.3</div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>$t_{2}$</td><td>4</td><td>3</td><td>2.5</td><td>2.2</td><td>2.1</td><td>2.05</td><td>2.01</td></tr><tr><td>V</td><td>29.4</td><td>24.5</td><td>22.05</td><td>20.58</td><td>20.09</td><td>19.845</td><td>19.649</td></tr></table></body></html></div>


Here again we note that if we take smaller time intervals starting at $t\in2.$ we get better idea of the velocity at $t=2$ 



In the first set of computations, what we have done is to find average velocities in increasing time intervals ending at $t=2$ and then hope that nothing dramatic happens just before $t=2$ _. In the second set of computations, we have found the average velocities decreasing in time intervals ending at $t=2$ and then hope that nothing dramatic happens just after $t=2$ 1. Purely on the physical grounds, both these sequences of average velocities must approach a common limit. We can safely conclude that the velocity of the body at $t=2$ is between 19.551m/s and 19.649 m/s. Technically, we say that the instantaneous velocity at $t\equiv2$ is between 19.551$m/s$ and 19.649 m/s. As is well-known, velocity is the rate of change of displacement. Hence what we have accomplished is the following. From the given data of distance covered at various time change of the distance at a given instant of time. We say that the derivative of the distance function $s=4.9t^{2}at t=2$ is between 19.551 and 19.649.

An alternate way of viewing this limiting process is shown in Fig 12.1.This is a plot of distance s of the body from the top of the cliff versus the time t elapsed. In the limit as the sequence of time intervals $h_{1},h_{2},\ldots$ ,approaches zero, the sequence of average velocities approaches the same limit as does the sequence of ratios 



<div style="text-align: center;"><img src="imgs/img_in_chart_box_432_851_869_1225.jpg" alt="Image" width="46%" /></div>


<div style="text-align: center;">Fig 12.1</div>


$$\left[\frac{\mathrm{C}_{1}\mathrm{B}_{1}}{\mathrm{AC}_{1}},\frac{\mathrm{C}_{2}\mathrm{B}_{2}}{\mathrm{AC}_{2}},\frac{\mathrm{C}_{3}\mathrm{B}_{3}}{\mathrm{AC}_{3}},\ldots\right.]$$

where $C_{1}B_{1}=s_{1}-s_{0}$ is the distance travelled by the body in the time interval $h_{1}=AC_{1}$ etc. From the Fig12.1 it is safe to concludethat this latter sequence approaches the slope of thetatttecurveat itA.Inr wo,teaaou vlocity $v(t)$ of a body at time $t=2$ is equal to the slope of the tangent of the curve $s=4.9t^{2}$ at $t=2$ '

### 12.3 Limits 

The above discussion clearly points towards the fact that we need to understand limiting process in greater clarity. We study a few illustrative examples to gain some familiarity with the concept of limits.



Consider the function $f(x)=x^{2}$ . Observe that as x takes values very close to 0,the value of $f(x)$ aomovewse.1).Way 

$$\lim_{x\to0}f(x)=0$$

(to be read as limit $\mathrm{of}f(x)$ as x tends to zero equals zero). The limit of $f(x)$ as x tends to zero is to be thought of as the value $f(x)$ should assume at $x=0$ 1

In general as $x\to a,f(\underline{x})\to l,$ then l is called limit of the function $f(x)$ which is symbolically written as $\lim_{x\to a}f(x)=l$ 



Consider the following function $g(x)=|x|,x\neq0$ Computing the value ofg(x) for values of x very near to 0, we see that the value of g(x) moves towards 0. So,$\lim_{x\to0}g(x)=0$ . This is intuitively clear from the graph $\mathrm{of}y=|x|$ for $x^{\cdot}\ne0$ (See Fig 2.13, Chapter 2).



Consider the following function.

$$h(x)=\frac{x^{2}-4}{x-2},x\ne2$$

Compute the value of $h(x)$ for values of x very near to 2 (but not at 2). Convince yourself that all these values are near to 4. This is somewhat strengthened by considering the graph of the function $y=h(x)$ given here (Fig 12.2).

$$. Observe that g(0) is not defined.$$

<div style="text-align: center;">Fig 12.2</div>


$$y=h(x)$$

In all these illustrations the value which the function should assume at a given point $x=a$ did not reallydepend onhow istndingto a.Notethatthere aressenialy two ways x could approach a number a either from left or from right, i.e., all the values of x near a could be less than a or could be greater than a. This naturally leads to two limits –the right hand limit and the left hand limit. Right hand limit of a function $f(x)$ is )to afromit.aleftand imi.Tollutei,orteucon 

$$f(x)=\begin{cases}1,&x\leq0\\2,&x>0\end{cases}$$

Graph of this function is shown in the Fig 12.3. It is clear that the value off at 0 dictated by values off(x) with $x\leq0$ equals 1, i.e.,the left hand limit of $f\left(x\right)$ at 0 is 

$$\lim_{x\to\overline{0}}f(x)=1$$

Similarly, the value of f at 0 dictated by values $f(x)$ with $x\geq0$ equals 2, i.e., the right hand limit of $f(x)$ at 0 is 



$$\lim_{x\to0^{+}}f(x)=2$$

<div style="text-align: center;"><img src="imgs/img_in_image_box_619_401_855_681.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">Fig 12.3</div>


In this case the right and left hand limits are different, and hence we say that the limit $\mathrm{of}f(x)$ asx tends t zero does not exist(enthough thefunction is defind at 

## Summary 

We say $\mathrm*{lim}_{x\to a^{-}}f(x)$ is the expected value of f at $x=a$ given the values off near x to the left of a.This value is called the left hand limit off at a.

We say $\mathrm*{lim}_{x\to a^{+}}f(x)$ is the expected value off at $x=a$ given the values of f near x to the right of a.This value is called the right hand limit of $f(x)$ at a.

If the right and left hand limits coincide, we call that common value as the limit $f(x)at x=a$ and denote it by $\mathrm*{lim}_{x\to a}f(x)$ 



Illustration 1 Consider the function $f(x)=x+10$ . We want to find the limit of this function at $x=5$ . Let us compute the value of the function $f(x)$ for x very near to 5.Some of the points near and to the left of5 are 4.9,4.95,4.99,4.995...,etc.Values of the function at these points are tabulated below. Similarly, the real number 5.001, 5.01,.1o.ofe are also given in the Table 12.4.



<div style="text-align: center;">Table 12.4</div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>x</td><td>4.9</td><td>4.95</td><td>4.99</td><td>4.995</td><td>5.001</td><td>5.01</td><td>5.1</td></tr><tr><td>$f(x)$</td><td>14.9</td><td>14.95</td><td>14.99</td><td>14.995</td><td>15.001</td><td>15.01</td><td>15.1</td></tr></table></body></html></div>


From the Table 12.4, we deduce that value of f(x) at $x=5$ should be greater than 14.995 and less than 15.001 assuming nothing dramatic happens between $x=4.995$ ·and5.01.talssumtaluet ,$f(x)$ at $x=5$ as dictated by the numbers to the left of 5 is 15, ie.,

$$\lim_{x\to5^{-}}f(x)=15$$

Similarly, wenppraces5omte righ,${\mathcal{f}}(x)$ 



$$\lim_{x\to5^{+}}f(x)=15$$

Hence,it is likely that the lefthand limit $\mathrm{of}f(x)$ and the right hand limit $\mathrm{of}f(x)$ are both equal to 15. Thus,

$$\lim_{x\to5^{-}}f(x)=\lim_{x\to5^{+}}f(x)=\lim_{x\to5^{-}}f(x)=15$$

This conclusion about the limit being equal to 15 is somewhat strengthened by seeingthegraphofthisfunction which is giveninFig2.16,Chaptr2.Ithisfigure, we note that as x approaches 5 from either right or left, the graph of the function $f(x)=x+10$ approaches the point (5, 15).



We observethat thevalueofthe utio t $x=5$ also happens to be equal to 15.

Illustration 2 Consider the function $f(x)=x^{3}$ . Let us try to find the limit of this function at $x=1$ Proceedinivu,wa $f(x)$ x near 1. This is given in the Table 12.5.



<div style="text-align: center;">Table 12.5</div>



<div style="text-align: center;"><html><body><table border="1"><thead><tr><td>$x$</td><td>0.9</td><td>0.99</td><td>0.999</td><td>1.001</td><td>1.01</td><td>1.1</td></tr></thead><tbody><tr><td>$f(x)$</td><td>0.729</td><td>0.970299</td><td>0.997002999</td><td>1.003003001</td><td>1.030301</td><td>1.331</td></tr></table></body></html></div>


From this table, we deduce that value of $f(x)$ at $x=1$ should be greater than 0.997002999 and less than 1.003003001 assuming nothing dramatic happens between  $x=0.999$ and 1.001. It is reasonable to assume that the value of the $f(x)$ at $x=1$ as dictated by the numbers to the left of 1 is 1, i.e.,

$$\lim_{x\to1^{-}}f(x)=1$$

Similarly, when x approaches 1 from the right $,f(x)$ should be taking value 1, i.e 

$$\lim_{x\to1^{+}}f(x)=1$$

Hnce,$f(x)$  both equal to 1. Thus,[Ta]

$$\lim_{x\to1^{-}}f(x)=\lim_{x\to1^{+}}f(x)=\lim_{x\to1}f(x)=1$$

11seeing the graph of this function which is given in Fig 2.11, Chapter 2.In this figure, we note that as x approaches 1 from either right or left, the graphof the function $f(x)=x^{3}$ approaches the point (1, 1).



We observe, again, that the value of the function at $x^{2}-1$ also happens to be equal to 1.



Illustration 3 Consider the function $f(x)=3x$ t us try to find the limit of this function at $x=2$ .The following Table 12.6 is now self-explanatory.

<div style="text-align: center;">Table 12.6</div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>x</td><td>1.9</td><td>1.95</td><td>1.99</td><td>1.999</td><td>2.001</td><td>2.01</td><td>2.1</td></tr><tr><td>$f(x)$</td><td>5.7</td><td>5.85</td><td></td><td>5.997</td><td>6.003</td><td>6.03</td><td>6.3</td></tr></table></body></html></div>


As before we observe that as x approaches 2from either left or right, the value of f(x) seem to approach 6. We record this as 

$$\lim_{x\to2^{-}}f(x)=\lim_{x\to2^{+}}f(x)=\lim_{x\to2}f(x)=6$$

Its graph shown in Fig 12.4 strengthens this fact.



Here again we note that the value of the function at $x=2$ coincides with the limit at $x=2$ ;

Illustration 4 Consider the constant function $f(x)=3$  Let us try to find its limit at $x=2$ . This function being the constant function takes the same 

<div style="text-align: center;"><img src="imgs/img_in_image_box_570_869_869_1218.jpg" alt="Image" width="31%" /></div>


<div style="text-align: center;">Fig 12.4</div>


value.

$$\lim_{x\to2}f(x)=\lim_{x\to2^+}f(x)=\lim_{x\to2}f(x)=3$$

Graph of $f(x)=3$ is anw t lieparallt -ais psiouh , 3) and is I fact, it is easily observed that $\lim_{x\to a}f(x)=3$ for any real number a.

Illustration 5 Consider the function $f(x)=x^{2}+x$  We want to find $\lim_{x\to1}f(x)$ .We tabulate the values of $f(x)$ near $x=1$ in Table 12.7.



<div style="text-align: center;">Table 12.7</div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>x</td><td>0.9</td><td>0.99</td><td>0.999</td><td>1.01</td><td>1.1</td><td>1.2</td></tr><tr><td>$f(x)$</td><td>1.71</td><td>1.9701</td><td>1.997001</td><td>2.0301</td><td>2.31</td><td>2.64</td></tr></table></body></html></div>


at 

$$\lim_{x\to1^{-}}f(x)=\lim_{x\to1^{+}}f(x)=\lim_{x\to1}f(x)=2$$

appr From the graph of $f(x)=x^{2}+x$ roaches (1, 2).2 ci::,

,

$$\lim_{x\to1}f(x)=f(1)$$

Now, convince yourself of the following three facts:

Then 

$$\begin{aligned}\lim_{x\to1}x^2&=1,\quad\lim_{x\to1}x=1and\quad\lim_{x\to1}x+1=2\\\lim_{x\to1}x^2&+\lim_{x\to1}x=1+1=2=\lim_{x\to1}\left[x^2+x\right].\end{aligned}$$

$$y=f(x)$$

<div style="text-align: center;">Y′Fig 12.5</div>


Also $\lim_{x\to1}x\cdot\lim_{x\to1}(x+1)=1.2=2=\lim_{x\to1}\left[x(x+1)\right]=\lim_{x\to1}\left[x^2+x\right]$ 

Illustration 6 Consider the function $f(x)=\sin x$ .We are interested in $\lim_{x\to\frac{\pi}{2}}\sin x$ where the angle is measured in radians.



Here, we tabulate the (approximate) value of $f(x)$ near $\frac{\pi}{2}\left(Table12.8\right)$ 1. From this, we may deduce that 



$$\lim_{x\to\frac{\pi}{2}}f(x)=\lim_{x\to\frac{\pi}{2}}f(x)=\lim_{x\to\frac{\pi}{2}}f(x)=1$$

Further, this is supported by the graph of $f(x)=\sin x$ 

(Chapter 3). In this case too, we observe that lim sin $x=1$ lish 

$$x{\rightarrow}{\frac{\pi}{\overline{\sigma}}}$$

<div style="text-align: center;">Table 12.8</div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>x</td><td>$\frac{\pi}{2}-0.1$</td><td>$\frac{\pi}{2}-0.01$</td><td>$\frac{\pi}{2}+0.01$</td><td>$\frac{\pi}{2}+0.1$</td></tr><tr><td>$f(x)$</td><td>0.9950</td><td>0.9999</td><td>0.9999</td><td>0.9950</td></tr></table></body></html></div>


Illustration 7 Consider the function $f(x)=x+\cos x$ . We want to find the $\lim_{x\to0}f(x)$ Here we tabulate the (approximate) value of $f(x)$ near 0 (Table 12.9).

<div style="text-align: center;">Table 12.9</div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>x</td><td>-0.1</td><td>$-.0.01$</td><td>−0.001</td><td>0.001</td><td>0.01</td><td>0.1</td></tr><tr><td>$f(x)$</td><td>0.9850</td><td>0.98995</td><td>0.9989995</td><td>1.0009995</td><td>1.00995</td><td>1.0950</td></tr></table></body></html></div>


From the Table 13.9, we may deduce that 

$$\lim_{x\to0^{-}}f(x)=\lim_{x\to0^{+}}f(x)=\lim_{x\to0}f(x)=1$$

In this case too, we observe that $\lim_{x\to0}f(x)=f(0)=1$ 

Now, can you convince yourself that 

$$\lim_{x\to0}\left[x+\cos x\right]=\lim_{x\to0}x+\lim_{x\to0}\cos x is indeed true?$$

Illustration 8 Consider the function $f(x)=\frac{1}{x^{2}}\quad for\quad x>0$ . We want to know $\lim_{x\to0}f(x)$ 

Here, observe that the domain of the function is given to be all positive real numbers. Hence, when we tabulate the values $\mathrm{of}f(x)$ 1, it does not make sense to talk of xapproaching romthe lft.low wetbulatethe values ofthe function for positive x close to 0 (in this table n denotes any positive integer).



From the Table 12.10 given below, we see that as x tends to 0,$f(x)$ becomes lare $f(x)$ may be made lar t any given number.



<div style="text-align: center;">Table 12.10</div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>x</td><td>1</td><td>0.1</td><td>0.01</td><td></td></tr><tr><td>$f(x)$</td><td>1</td><td>100</td><td>10000</td><td>10²n</td></tr></table></body></html></div>


Mathematically, we say 

$$\lim_{x\to0}f(x)=+\infty $$

We also remark that we will not come across such limi ERT bll in this course.

Illustration 9 We want to find $\lim_{x\to0}f(x)$ 



$$f(x)=\left\{\begin{aligned}x-2,\quad&x<0\\ 0,\quad&x=0\\ x+2,\quad&x>0\end{aligned}\right.$$

As usual we make a table ofx near 0 withf(x). Observe that for negative values of we need to evaluate $x-2\mathrm{and}$ for positive values, we need to evaluate $x\pm2$ 

<div style="text-align: center;">Table 12.11</div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>x</td><td></td><td>-0.01</td><td>−0.001</td><td>0.001</td><td>0.01</td><td>0.1</td></tr><tr><td>$f(x)$</td><td>2.1</td><td>-2.01</td><td>-2.001</td><td>2.001</td><td>2.01</td><td>2.1</td></tr></table></body></html></div>


From the first three entries of the Table 12.11, we deduce that the value of the function is decreasing to –2 and hence.



$$\lim_{x\to0^{-}}f(x)=-2$$

From the last three entires ofthetable we deduce that the valueof the function is increasing from 2 and hence 

<div style="text-align: center;"><img src="imgs/img_in_image_box_629_169_863_414.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">Fig 12.6</div>


$$\lim_{x\to0^{+}}f(x)=2$$

Since the left and right hand limits at 0 do not coincide,we say that the limit of the function at 0 does not exist.

Graph of this function is given in the Fig12.6. Here,we remark that the value of the function at $x=0$ is well defined and is, inded, equal to 0, but the limit of the function at $x=0$ is not even defined.



Illustration 10 As a final ilustration, we find $\lim_{x\to1}f(x)$ where 



$$f(x)=\left\{\begin{aligned}x+2x\neq1\\0\quad x=1\end{aligned}\right.$$

<div style="text-align: center;">Table 12.12</div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>x</td><td>0.9</td><td>0.99</td><td>0.999</td><td>1.001</td><td>1.01</td><td>1.1</td></tr><tr><td>$f(x)$</td><td>2.9</td><td>2.99</td><td>2.999</td><td>3.001</td><td>3.01</td><td>3.1</td></tr></table></body></html></div>


As usual we tabulate the values of f(x) for x near 1. From the values $\mathrm{of}f(x)$ for  less than 1,it seemsthatthe function should take value a $x=1$ ., i.e.,

$$\lim_{x\to1^{-}}f(x)=3$$

Similarly, the value $\mathrm{if}f(x)$ should be 3 as dictated by values of $f(x)$ at x greater than 1. i.e.

$$\lim_{x\to1}f(x)=3$$

But then the left and right hand limits coincide and hence 



$$\lim_{x\to1^{-}}f(x)=\lim_{x\to1^{+}}f(x)=\lim_{x\to1}f(x)=3$$

Graph of function given in Fig 12.7 srengthens our deduction about the limit. Here, we 

$$y=f(x)$$

<div style="text-align: center;">Fig 12.7</div>


note that in general, at a given point the value of the function and its limit may be different (even when both are defined).



12.3.1AoflimtIovelueblimting proceslid  l t lmis and functions under conideration are well defined.This isnot acoincidence. In fact,below we formalise these as a theorem without proof.



Theorem 1 Letf and g be two functions such that both $\lim_{x\to a}f(x)\mathrm{and}\lim_{x\to a}g(x)$ exist.Then 

($$ ,

$$\lim_{x\to a}\left[f(x)+g(x)\right]=\lim_{x\to a}f(x)+\lim_{x\to a}g(x).$$

(ii) Limit of dfrence of to untion is rence of te limits of th functions, i.e.,

$$\lim_{x\to a}\left[f(x)-g(x)\right]=\lim_{x\to a}f(x)-\lim_{x\to a}g(x)$$

(i) Limit of product of two functions is product of the limits of the functions, i.e.,

$$\lim_{x\to a}\left[f(x)\cdot g(x)\right]=\lim_{x\to a}f(x)\cdot\lim_{x\to a}g(x).$$

(iv)vr the denominator is non zero), i.e.,

$$\lim_{x\to a}\frac{f(x)}{g(x)}=\frac{\lim\limits_{x\to a}f(x)}{\lim\limits_{x\to a}g(x)}$$

NoteInparticularasaspecialcaseof(i),whenistheconstantfunction such that $g(x)=\lambda$ , for some real number $\lambda$ , we have 

$$\lim_{x\to a}\left[(\lambda_{-}f)(x)\right]=\lambda_{-}\lim_{x\to a}f(x)$$

In the next two subsections, we illustrate how to exploit this theorem to evaluate limits of special types of functions.



12.3.2Limitsof polynomialsandrationalfunctions A function $f$ is said to be a polynomial function of degree n $f(x)=a_{0}+a_{1}x+a_{2}x^{2}+\cdots+a_{n}x^{n}$ ,where $a_{i}s$ are real numbers such that $a_{n}\ne0$ for some natural number n.



We know that $\lim_{x\to a}x=a$ . Hence 

$$\lim_{x\to a}x^2=\lim_{x\to a}(x.x)=\lim_{x\to a}x.\lim_{x\to a}x=a.a=a^2$$

An easy exercise in induction on n tells us that 

$$\lim_{x\to a}x^n=a^n $$

Now, let $f(x)=a_{0}+a_{1}x+a_{2}x^{2}+\ldots+a_{n}x^{n}$ be a polynomial function. Thinking of each of $a_{0},a_{1}x,a_{2}x^{2},...,a_{n}x^{n}$ as a function, we have 

shed 

$$\begin{aligned}\lim_{x\to a}f(x)&=\lim_{x\to a}\left[a_0+a_1x+a_2x^2+\ldots+a_nx^n\right]\\&=\lim_{x\to a}a_0+\lim_{x\to a}a_1x+\lim_{x\to a}a_2x^2+\ldots+\lim_{x\to a}a_nx^n\\&=a_0+a_1\lim_{x\to a}x+a_2\lim_{x\to a}x^2+\ldots+a_n\lim_{x\to a}x^n\\&=a_0+a_1a+a_2a^2+\ldots+a_na^n\\&=f(a)\end{aligned} shed $$

(Make sure that you understand the justification for each step in the above!)

A function is said to be a rational function,$\mathrm{if}f(x)=\frac{g(x)}{h(x)}$ ,where $g(x)$ and $h(x)$ are polynomials such that $h(x)\neq0$ . Then 



$$\lim_{x\to a}f(x)=\lim_{x\to a}\frac{g(x)}{h(x)}=\frac{\lim\limits_{x\to a}g(x)}{\lim\limits_{x\to a}h(x)}=\frac{g(a)}{h(a)}$$

However,$\mathrm{if}\hbar(a)=0$ , there are two scenarios − (i) when $g(a)\neq0$ and (ii) when $g(a)=0$ .In the former case we say that the limit does not exist.In the latter case we can write $g(x)=(x-a)^k g_1(x)$ , where k is the maximum of powers of $(x-a)\;in\;g(x)$ Similarly,$h(x)=(x-a)^l h_1(x)$ ash $(a)=0$ cYNoif $k>l$ ,we have 

$$\lim_{x\to a}f(x)=\frac{\lim\limits_{x\to a}g(x)}{\lim\limits_{x\to a}h(x)}=\frac{\lim\limits_{x\to a}(x-a)^k g_1(x)}{\lim\limits_{x\to a}(x-a)^l h_1(x)}$$

$$\frac{\lim\limits_{x\to a}(x-a)^{(k-l)}g_1(x)}{\lim\limits_{x\to a}h_1(x)}=\frac{0.g_1(a)}{h_1(a)}=0$$

If $k\leq l.$ ,the limit is not defined.

Example 1 Find the limits: (i)$\lim_{x\to1}\left[x^3-x^2+1\right]$ (ii)$\lim_{x\to3}\left[x(x+1)\right]$ 

(m)

$$\lim_{x\to-1}\left[1+x+x^2+\ldots+x^{10}\right]$$

Solution The required limitsare all limitsof some polynomialfunctions.Hence the limits are the values of the function at the prescribed points. We have `lishe 

(i)

$$\lim_{x\to1}\left[x^3-x^2+1\right]=1^3-1^2+1=1 NC.T $$

(ii)

$$\lim_{x\to3}\left[x(x+1)\right]=3(3+1)=3(4)=12 NC.T $$

(i)

$$\lim_{x\to-1}\left[1+x+x^2+\ldots+x^{10}\right]=1+(-1)^2+(-1)^{2}+\ldots+(-1)^{10} NCATT Aish e \lim_{x\to-1}\left[1+x+x^2+\ldots+x^{10}\right]=1+(-1)^2+(-1)^{2}+\ldots+(-1)^{10}$$

$$1-1+1\ldots+1=1$$

Example 2 Find the limits:NC.T 

(i)

$$NC.T \lim_{x\to1}\left[\frac{x^2+1}{x+100}\right]$$

(ii)

$$NC.T 
\lim_{x\to2}\left[\frac{x^3-4x^2+4x}{x^2-4}\right]$$

(i)

$$\lim_{x\to2}\left[\frac{x^2-4}{x^3-4x^2+4x}\right]八U $$

(iv)

$$\lim_{x\to2}\left[\frac{x^3-2x^2}{x^2-5x+6}\right]$$

(v)

$$八U \lim_{x\to1}\left[\frac{x-2}{x^2-x}-\frac{1}{x^3-3x^2+2x}\right]$$

Solution All the functions under consideration are rational functions. Hence, we frst el $\left[\frac{0}{0}\right.]$ , we try to rewrite the function cancelling the factors which are causing the limit to be of the form $\left[\frac{0}{0}\right.]$ 



(i)We have $\lim_{x\to1}\frac{x^2+1}{x+100}=\frac{1^2+1}{1+100}=\frac{2}{101}$ 

()Evaluting thefunction at2it is ofthe form $\frac{0}{0}$ 

$$\lim_{x\to2}\frac{x^3-4x^2+4x}{x^2-4}=\lim_{x\to2}\frac{x(x-2)^2}{(x+2)(x-2)}$$

0

Hence $\lim_{x\to2}\frac{x^2-4}{x^3-4x^2+4x}=\lim_{x\to2}\frac{(x+2)(x-2)}{x(x-2)^2}$ 

$$\lim_{x\to2}\frac{(x+2)}{x(x-2)}=\frac{2+2}{2(2-2)}=\frac{4}{0}$$

which is not defined.

<div style="text-align: center;"><img src="imgs/img_in_image_box_310_920_369_971.jpg" alt="Image" width="6%" /></div>


$\left[\frac{0}{0}\right.]$ 

$$\lim_{x\to2}\frac{x^3-2x^2}{x^2-5x+6}=\lim_{x\to2}\frac{x^2(x-2)}{(x-2)(x-3)}$$

(v) First, we rewrite the function as a rational function.

*[Formula could not be recovered from OCR — see source PDF]*

Evaluating the function at 1, we get it of the form $\frac{0}{0}$ 'blished 

Hence 

$$'blished \begin{aligned}\lim_{x\to1}\left[\frac{x^2-2}{x^2-x}-\frac{1}{x^3-3x^2+2x}\right]&=\lim_{x\to1}\frac{x^2-4x+3}{x(x-1)(x-2)}\\&=\lim_{x\to1}\frac{(x-3)(x-1)}{x(x-1)(x-2)}\\&=\lim_{x\to1}\frac{x-3}{x(x-2)}=\frac{1-3}{1(1-2)}=2.\end{aligned}$$

We remark that we could cancel the term $(x-1)$ in the above evaluation because 

$x\neq1$ 



Evaluation of an important limit which will be used in the sequel is given as a theorem below.



Theorem 2 For any positive integer n,_



$$\lim_{x\to a}\frac{x^n-a^n}{x-a}=na^{n-1}$$

Remark The expression in the above theorem for the limit is true even if n is any rational number and a is positive.



Proof Dividing $\left(x^{n}-a^{n}\right)\text{by}(x-a)$ ,we see that 

$$x^{n}-a^{n}=(x-a)\left(x^{n-1}+x^{n-2}a+x^{n-3}a^{2}+\ldots+xa^{n-2}+a^{n-1}\right)$$

Thus,

$$\begin{aligned}\lim_{x\rightarrow a}\frac{x^{n}-a^{n}}{x-a}&=\lim_{x\rightarrow a}\left(x^{n-1}+x^{n-2}a+x^{n-3}a^{2}+\ldots+x a^{n-2}+a^{n-1}\right)\\&=a^{n-1}+a^{n-2}+\ldots+a^{n-2}(a)+a^{n-1}\\&=a^{n-1}+a^{n-1}+\ldots+a^{n-1}+a^{n-1}(n terms)\\&=\frac{\cdot}{n}a^{n-1}\end{aligned}uolished $$

Example 3 Evaluate:

(i)

$$\lim_{x\to1}\frac{x^{15}-1}{x^{10}-1}$$

(ii)

$$\lim_{x\to0}\frac{\sqrt{1+x}-1}{x} uolished $$

Solution (i) We have 

$$\lim_{x\to1}\frac{x^{15}-1}{x^{10}-1}=\lim_{x\to1}\left[\frac{x^{15}-1}{x-1}\div\frac{x^{10}-1}{x-1}\right] uolished $$

$$\lim_{x\to1}\left[\frac{x^{15}-1}{x-1}\right]\div\lim_{x\to1}\left[\frac{x^{10}-1}{x-1}\right] uolished $$

$15^{-}(1)^{14}\div10(1)^{9}$ (by the theorem above)

$$15\div10=\frac{3}{2}$$

(ii)

$$\mathrm{Put}y=1+x\quad\mathrm{so}\quad\mathrm{that}y\rightarrow1\quad\mathrm{as}x\rightarrow0.$$

$$\lim_{x\to0}\frac{\sqrt{1+x}-1}{x}=\lim_{y\to1}\frac{\sqrt{y}-1}{y-1}=\lim_{y\to1}\frac{y^{\frac{1}{2}}-1^{\frac{1}{2}}}{y-1}=\lim_{x\to1}\frac{1}{2}=\lim_{y\to1}\frac{1}{2}$$

### 12.4 Limitsof Trigonometric Functions 

The following facts (stated as theorems) about functions in general come in handy in calculating limits of some trigonometric functions.



Theorem 3 Letf and g be two real valued functions with the same domain such that $f(x)\leq\mathrm{g}(x)$ for all x in the domain of definition, For some a, if both $\lim_{x\to a}f(x)$ and x→a $g(x)$ exist, then $\lim_{x\to a}f(x)\leq\lim_{x\to a}g(x)$ This is illustrated in Fig .

<div style="text-align: center;"><img src="imgs/img_in_chart_box_289_390_656_666.jpg" alt="Image" width="39%" /></div>


Theorem 4 (Sandwich Theorem) Let f,$f(x)\leq g(x)\leq h(x)$ for all x in the common domain of definition.For some real number a, if $\lim_{x\to a}f(x)=l=\lim_{x\to a^{-}}h(x)$ ,then lim $x→ag(x)=1$ This is illustrated in Fig 12.9.

<div style="text-align: center;"><img src="imgs/img_in_image_box_258_806_660_1094.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;">Fig 12.9</div>


Given below is a beautiful geometric proof of the following important inequalitio.



$$\cos x<\frac{\sin x}{x}<1\quad for0<|x|<\frac{\pi}{2}$$

Proof We know that sin $(-x)=-\sin x$ and $\cos(-x)=\cos x$ . Hence, it is sufficient B to prove the inequality for $0<x<\frac{\pi}{2}$ C 

<div style="text-align: center;"><img src="imgs/img_in_image_box_702_169_868_368.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">Fig 12.10</div>


In the Fig12.10,O is the centre of the unit circle such that the angle AOC is x radians and $0<x<\frac{\pi}{2}$ . Line segments B A and CD are perpendiculars to OA. Further, join AC. Then 

Area of $\Delta\mathrm{OAC}<\mathrm{Area}$ of sector $\mathrm{OAC}<\mathrm{Area}$ of $\Delta\mathrm{OAB}$ 

i.e.,

$$\frac{1}{2}OA.CD<\frac{x}{2\pi}.\pi.(OA)^{2}<\frac{1}{2}OA.AB $$

i.e.,$\mathrm{CD}<x.\mathrm{OA}<\mathrm{AB}.$ 

From ∆ OCD,

sin $x=\frac{CD}{OA}\quad(since OC=OA)$ $\mathrm{CD}=\mathrm{OA}$ $x=\frac{AB}{OA}$ and 

hence 

$$AB=OA .tan x. Thus $$

OA sin $x<OA.x\leq OA.$ tan x.

Since length OA is positive, we have 

sin $x<x<\tan x.$ 

Since $0<x<\frac{\pi}{2}$ ,siniae 

$\frac{x}{\sin x}<\frac{1}{\cos x}$ tO 



$$\cos x<\frac{\sin x}{x}<1 tO $$

which complete the proof.

Theorem 5 The following are two important limits.

(i)$\lim_{x\to0}\frac{\sin x}{x}=1$ (ii)$\lim_{x\to0}\frac{1-\cos x}{x}=0$ 

Proof (i) The inequality in (*) says that the function $\frac{\sin x}{x}$ is sandwiched between the function cos x and the constant function which takes value 1.

Further, since $\lim_{x\to0}\cos x=1$ , we see that the proof of (i) of the theorem is complete by sandwich theorem.



To prove (i), we recall the trigonometric identity $1-\cos x=2\sin^{2}\left(\frac{x}{2}\right)$ 

Then 

$$\lim_{x\to0}\frac{1-\cos x}{x}=\lim_{x\to0}\frac{2\sin^2\left(\frac{x}{2}\right)}{x}=\lim_{x\to0}\frac{\sin\left(\frac{x}{2}\right)}{\frac{x}{2}}\cdot\sin\left(\frac{x}{2}\right)$$

$$\lim_{x\to0}\frac{\sin\left(\frac{x}{2}\right)}{\frac{x}{2}}\cdot\lim_{x\to0}\sin\left(\frac{x}{2}\right)=1.0=0$$

$x\to0$ is equivalent to $\frac{x}{2}\rightarrow0$ .This may be justified by $\widehat{\mathrm{puting}y}=\frac{x}{2}$ 



Example 4 Evaluate:(i)$\lim_{x\to0}\frac{\sin4x}{\sin2x}$ (ii)$\lim_{x\to0}\frac{\tan x}{x}$ 

 Solution (i)noL $\lim_{x\to0}\frac{\sin4x}{\sin2x}=\lim_{x\to0}\left[\frac{\sin4x}{4x}\cdot\frac{2x}{\sin2x}\cdot2\right]$ 

$$2.\lim_{x\to0}\left[\frac{\sin4x}{4x}\right]\div\left[\frac{\sin2x}{2x}\right]$$

$$2.\lim_{4x\to0}\left[\frac{\sin4x}{4x}\right]\div\lim_{2x\to0}\left[\frac{\sin2x}{2x}\right]$$

$$2.1.1=2\left(\mathrm{as}\;x\rightarrow0,\;4x\rightarrow0\;\mathrm{and}\;2x\rightarrow0\right)$$

$$\lim_{x\to0}\frac{\tan x}{x}=\lim_{x\to0}\frac{\sin x}{x\cos x}=\lim_{x\to0}\frac{\sin x}{x}\cdot\lim_{x\to0}\frac{1}{\cos x}=1.1=1$$

A 

Say, given that the limit $\lim_{x\to a}\frac{f(x)}{g(x)}$ exists and we want to evaluate this. First we check 

the value of $f(a)$ and g(a). If both are 0,then we see if we can get the factor which is causing the terms to vanish, i.e., see if we can write $f(x)=f_{1}(x)f_{2}(x)$ so that $f_{1}\left(a\right)=0and f_{2}\left(a\right)\neq0$ . Similarly, we write $g(x)=g_{1}(x)g_{2}(x)$ ,where $g_{1}(a)=0$ and $g_{2}(a)\neq0$ (x) and g(x) (if possible) and 

$$\frac{f(x)}{g(x)}=\frac{p(x)}{q(x)},where q(x)\neq0.$$

Then 

$$\lim_{x\to a}\frac{f(x)}{g(x)}=\frac{p(a)}{q(a)}$$

2.1

Evaluate the following limits in Exercises 1 to −

1.$\lim_{x\to3}x+3$ 22.$\lim_{x\to\pi}\left(x-\frac{22}{7}\right)$ $\lim_{r\to1}\pi r^{2}$ 

$$ −

5.

$$\lim_{x\to-1}\frac{x^{10}+x^5+1}{x-1}$$

6.

$$\lim_{x\to0}\frac{(x+1)^5-1}{x}$$

7.lim $x→2 8(cid:2)$\lim_{x\to3}\frac{x^4-81}{2x^2-5x-3}$ 9.$\lim_{x\to0}\frac{ax+b}{cx+1}$ 

10.$\lim_{z\to1}\frac{z^{\frac{1}{3}}-1}{z^{\frac{1}{6}}-1}$ 心$\lim_{x\to1}\frac{ax^2+bx+c}{cx^2+bx+a},a+b+c\neq0$ 

12.$\lim_{x\to-2}\frac{\frac{1}{x}+\frac{1}{2}}{x+2}$ 13.$\lim_{x\to0}\frac{\sin ax}{bx}$ 14.$\lim_{x\to0}\frac{\sin ax}{\sin bx},a,b\neq0$ 

15.$\lim_{x\to\pi}\frac{\sin(\pi-x)}{\pi(\pi-x)}$ 16.$\lim_{x\to0}\frac{\cos x}{\pi-x}$ 17.$\lim_{x\to0}\frac{\cos2x-1}{\cos x-1}$ 

18.$\lim_{x\to0}\frac{ax+x\cos x}{b\sin x}$ 19.$\lim_{x\to0}x\sec x$ 

20.

$$\lim_{x\to0}\frac{\sin ax+bx}{ax+\sin bx}a,b,a+b\neq0$$

22.$\lim_{x\to\frac{\pi}{2}}\frac{\tan2x}{x-\frac{\pi}{2}}$ 

23. Find $\lim_{x\to0}f(x)$ and $\lim_{x\to1}f(x)$ ,where $$ 

24.Find $\lim_{x\to1}f(x)$ ,where $$ 

25. Evaluate $$ 

26.Find $\lim_{x\to0}f(x)$ $\mathrm{where}f(x)=\left\{\begin{aligned}\frac{x}{|x|},&\quad x\neq0\\ 0,&\quad x=0\end{aligned}\right.$ 

27. Find $\lim_{x\to5}f(x)$ , where $f(x)=|x|-5$ 

28. Suppose $f(x)=\begin{cases}a+bx,&x<1\\ 4,&x=1\\ b-ax,&x>1\end{cases}$ 

and if $\lim_{x\to1}f(x)=f(1)$ what are possible values of a and b?

29. Let $a_{1},a_{2},\ldots,a_{n}$ be fixed real numbers and define a function 

$$f(x)=\left(x-a_{1}\right)\left(x-a_{2}\right)\ldots\left(x-a_{n}\right).$$

What is $\mathrm*{lim}_{x\to a_{1}}f(x)?$ For some $a\neq a_{1},\;a_{2},\;...,\;a_{n},$ ,compute $\lim_{x\to a}f(x)$ 

30.If $f(x)=\begin{cases}|x|+1,&x<0\\0,&x=0\\|x|-1,&x>0\end{cases}$ 

For what value (s) of a does ${\mathrm*{lim}_{x\to a}}f(x){\mathrm{~e x i s t s?}}$ 

31. If the function $f(x)$ satisfies satisfies lim x→$$\frac{f(x)-2}{x^2-1}=\pi$ $f(x)$ 

32.If $f(x)=\begin{cases}mx^{2}+n,&x<0\\nx+m,&0\leq x\leq1\\nx^{3}+m,&x>1\end{cases}$ $\lim_{x\to0}f(x)$ 

and $\lim_{x\to1}f(x)\mathrm{e}^{\mathrm{i}\frac{\pi}{2}t}$ 

### 12.5 Derivatives 

We have seen in the Section 13.2, that by knowing the position of a body at various time intervals it is possible to find the rate at which the position of the body is changing.It is of very general interest to know a certain parameter at various instants of time and try to finding the rate at which it is changing. There are several real life situations where such a process needs to be carried out. For instance, people maintaining a reservoir need to know when will a reservoir overflow knowing the depth of the water at several instances of time, Rocket Scientists need to compute the precise velocity with which the satellite needs to be shot out from the rocket knowing the height of the rocket at various times. Financial institutions need to predict the changes in the value of a particular stock knowing its present value. In these, and many such cases it is desirable to know how a particular parameter is changing with respect to some other parameter.The heart of the matter is derivative of a function at a given point in its domain of definition.



Definitio1upposeiealvaluducioanioiiimnf definition. The derivative of f at a is defined by 

$$\lim_{h\to0}\frac{f(a+h)-f(a)}{h}$$

provided this limit exists.Derivativeof 添司添$f(x)$ at a is denoted $by f(a)$ #

Observe that $$ quantifies te han in $$ a a with espect to .

Example5 Find the derivative at $x=2$ of the function $f(x)=3x$ 

Solution We have 

$$\lim_{h\to0}\frac{f(2+h)-f(2)}{h}=\lim_{h\to0}\frac{3(2+h)-3(2)}{h}=\lim_{h\to0}\frac{3h}{h}=\lim_{h\to0}\frac{3h}{h}=\lim_{h\to0}3=3 ied $$

The derivative of the function 3x at $x=2\mathrm{i}\mathrm{s}\bar{3}$ 

Example 6 Find the derivative of the function $f(x)=2x^{2}+3x-5\mathrm{at}x=-1$ . Also prove that_$f^{\prime}(0)+3f^{\prime}(-1)=0$ 



 Solution We first find the derivatives of f(x)$\textcircled{at}x=1$ and at $x=0$ .We have 

and 

$$\begin{aligned}f^{\prime}(-1)&=\lim_{h\to0}\frac{f(-1+h)-f(-1)}{h}\\&=\lim_{h\to0}\frac{\left[2(-1+h)^2+3(-1+h)-5\right]-\left[2(-1)^2+3(-1)-5\right]}{h}\\&=\lim_{h\to0}\frac{2h^2-h}{h}=\lim_{h\to0}(2h-1)=2(0)-1=-1\\f^{\prime}(0)&=\lim_{h\to0}\frac{f(0+h)-f(0)}{h}\\&=\lim_{h\to0}\frac{\left[2(0+h)^2+3(0+h)-5\right]-\left[2(0)^2+3(0)-5\right]}{h}\end{aligned}$$

$$\lim_{h\to0}\frac{2h^2+3h}{h}=\lim_{h\to0}(2h+3)=2(0)+3=3$$

Clearly 

$$f(0)+3f(-1)=0At this taetettevalutin eivtive at  oitnvlective use $$

Remark At this taetettevalutin eivtive at  oitnvlective use of various rules, limits are subjected to. The following illustrates this.

Example 7 Find the derivative of sin x at $x=0$ 1

Solution Let $f(x)=\sin x$ .Then 

$$\begin{aligned}f^{\prime}(0)&=\lim_{h\rightarrow0}\frac{f(0+h)-f(0)}{h}\\&=\lim_{h\rightarrow0}\frac{\sin(0+h)-\sin(0)}{h}=\lim_{h\rightarrow0}\frac{\sin h}{h}=1\end{aligned} ished $$

Example 8 Find the derivative o $f(x)=3atx=0and x=3$ 

Solution Since the derivative measuresthechange in function, intuitively it is clear that the derivativeoftheconstant function must be zeroatevery point.This isindeed,supported by the following computation.



Similarly 

$$f^{\prime}(0)=\lim_{h\to0}\frac{f(0+h)-f(0)}{h}=\lim_{h\to0}\frac{3-3}{h}=\lim_{h\to0}\frac{0}{h}=0.$$

We now present a geometric interpretation of derivative of a function at a $\mathrm{point}\;\mathrm{Let}y=f(x)$ be afunction and let $\mathbb{P}=(a,f(a))$ and $Q=(a+h,f(a+h))$ be two points close to each other on the graph of this function. The Fig 12.11 is now self explanatory.



<div style="text-align: center;"><img src="imgs/img_in_chart_box_408_918_879_1246.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Fig12.11</div>


We know that $f^{\prime}(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}$ 

From the triangle PQR, it is clear that the ratio whose limit we are taking is precisely qultta(QPR)whichiste lopeotchord Q.Ithe limiting process,as h tends to 0, the point Q tends to P and we have 

$$\lim_{h\to0}\frac{f(a+h)-f(a)}{h}=\lim_{Q\to P}\frac{QR}{PR}$$

This is equivalent to the fact that the chord PQ tends to the tangent at $\mathrm{Pef}$ the curve $y=f(x)$ . Thus the limit turns out to be equal to the slope of the tangent. Hence 

$$f^{\prime}(a)=\tan\psi $$

Foraivefuction wecafndtedrivtiveatvery poi.Ifteivative exists at vr iit ewuioldivformally, we define derivative of a function as follows.



Definition Suppose is a real valued function,thefunctiondefined by 

$$\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$$

wherever the limit exists is defined to be the rivative of f at x and is denoted by $f(x)$ . This definition of derivative is also called the first principle of derivative.Thus 

$$f^{\prime}(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$$

Clearly the domain of definition of $f^{\prime}(x)$ is wherever the above limit exists. There are different notations for derivative of a function. Sometimes $f^{\prime}(x)$ is denoted by $\left\{\frac{d}{dx}\left(f(x)\right)\quad or\quad\left\{y=f(x)\right\}\quad if\quad\frac{dy}{dx}\right\}$ . This is referred to as derivative $\mathrm{of}f(x)$ or y with respect to $x.\mathrm{It}$ is also denoted by D $(f(x))$ ). Further, derivative of $f\mathrm{at}x=a$ is also denoted by $\left|\frac{d}{dx}f(x)\right|_a\left.\mathrm{or}\frac{df}{dx}\right|_a\left.\mathrm{or}\mathrm{even}\left(\frac{df}{dx}\right)_{x=a}\right.$ 

Example 9 Find the derivative of $f(x)=10x$ 

Solution Since $f^{\prime}(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$ 

$$\lim_{h\to0}\frac{10(x+h)-10(x)}{h}=\lim_{h\to0}\frac{10h}{h}=\lim_{h\to0}\frac{10}{h}$$

Example 10 Find the derivative of $f(x)=x^{2}$ 

$$\begin{aligned}S_{0lu11011}\mathrm{We have},f^{\prime}(x)&=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}\\&=\lim_{h\to0}\frac{(x+h)^2-(x)^2}{h}=\lim_{h\to0}(h+2x)=2x.\end{aligned}$$

Example11inhditivoftcontnion $f(x)=a$ 

number a.



$$\begin{aligned}\lim_{h\to0}\mathrm{We have},f'(x)&=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}\\&=\lim_{h\to0}\frac{a-a}{h}=\lim_{h\to0}\frac{0}{h}=0\quad\mathrm{as}\quad h\neq0\end{aligned}$$

Example 12 Find the $\text{derivative of}f(x)=\frac{1}{x}$ 

$$\lim_{h\to0}\frac{1}{h}\left[\frac{x-(x+h)}{x(x+h)}\right]=\lim_{h\to0}\frac{1}{x(x+h)}=\lim_{h\to0}\frac{1}{x(x+h)}=\lim_{h\to0}\frac{1}{x(x+h)}=\lim_{h\to0}\frac{1}{x(x+h)}=\lim_{h\to0}\frac{1}{x(x+h)}=\lim_{h\to0}\frac{1}{x(x+h)}=\lim_{h\to0}\frac{1}{x(x+h)}=\lim_{h\to0}\frac{1}{x^2}$$

12.5.1AlgebaofdrivativeofunctionSincetheverydefintioof drivatives involve limits in a rather direct fashion, we expect the rules for derivatives to follow closely that of limits. We collect these in the following theorem.

Theorem 5 Letf and g be two functions such that their derivatives are defined in a common domain. Then 



(i)Derivative of sum of two functions is sum of the derivatives of the functions.



$$\frac{d}{dx}\left[f(x)+g(x)\right]=\frac{d}{dx}f(x)+\frac{d}{dx}g(x).$$

(i)ivs of the functions.  e ei 

$$\frac{d}{dx}\left[f(x)-g(x)\right]=\frac{d}{dx}f(x)-\frac{d}{dx}g(x),$$

by the following p rule.



$$\left[\frac{d}{dx}\left[f(x)\cdot g(x)\right]=\frac{d}{dx}f(x)g(x)+f(x)\cdot\frac{d}{dx}g(x)\right]$$

(iv)Derivative of quotient of two functions is given by the following quotient rule (whenever the denominator is non-zero).



$$\frac{d}{dx}\left(\frac{f(x)}{g(x)}\right)=\frac{d}{dx}\frac{f(x)\cdot g(x)-f(x)\cdot\frac{d}{dx}g(x)}{\left(g(x)\right)^{2}}$$

The proofs of these follow esentially from the analogous theorem for limits. We will not prove thesehere.As in thecase of limits this theorem tells us how to comute derivatives of special types of functions. The last two statements in the theorem may be restated in the following fashion which aids in recalling them easily:

Let $u=f(x)and v=g(x)$ . Then 

$$(uv)^{\prime}=u^{\prime}v+uv^{\prime}$$

This is referred to a Leibnitz rule for differentiating product of functions or the product rule. Similarly, the quotient rule is 



$$\left(\frac{u}{v}\right)'=\frac{u'v-uv'}{v^2}$$

Now, let ustackle derivativesofsome standard functions.

It is easy to see that the derivative of the function $f(x)=x$ is the constant 

$$\lim_{h\to0}\frac{f(x+h)-f(x)}{h}=\lim_{h\to0}\frac{x+h-x}{h}ished $$

$f(x)=10x=x+\cdots+x$ We use this and th (ten terms). By (i) of the above theorem S  e ed e f 

$$\begin{aligned}\frac{df(x)}{dx}&=\frac{d}{dx}(x+\ldots+x)(ten terms)\\&=\frac{d}{dx}x+\ldots+\frac{d}{dx}x(ten terms)\\&=1+\ldots+1(ten terms)=10.\end{aligned} ished $$

We note that this limit may be evaluated using product rule too. Write $f(x)=10x=uv$ , where u is the constant function taking value 10 everywhere and $v(x)=x$ . Here,$f(x)=\underline{10x}=uv$ :know that the derivative of u equals 0. Also derivative of $v(x)=x\quad\mathrm{eq}\quad\mathrm{a}\quad\mathrm{s}$ 1. Thus by the product rule we have 心I 



$$f^{\prime}(x)=(10x)^{\prime}=(uv)^{\prime}=u^{\prime}v+uv^{\prime}=0.x+10.1=10$$

On similar lines the derivative of $f(x)=x^{2}$ may be evaluated. We have $f(x)=x^{2}=x$ .x and hence 



$$\frac{df}{dx}=\frac{d}{dx}(x.x)=\frac{d}{dx}(x).x+x.\frac{d}{dx}(x)$$

More generally, we have the following theorem.

Theorem 6 Derivative of $f(x)=x^n\quad is\quad nx^{n-1}$ for any positive integer n.

Proof By definition of the derivative function, we have 

$$f(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}=\lim_{h\to0}\frac{(x+h)^n-x^n}{h}$$

Binomial theorem tells that $(x+h)^n=\left({}^n\mathrm{C}_0\right)x^n+\left({}^n\mathrm{C}_1\right)x^{n-1}h+\ldots+\left({}^n\mathrm{C}_n\right)h^n$ and hence $(x+h)^n-x^n=h(nx^{n-1}+\cdots+h^{n-1})$ . Thus 

$$\begin{aligned}\frac{df(x)}{dx}&=\lim_{h\to0}\frac{(x+h)^n-x^n}{h}\\&=\lim_{h\to0}\frac{h\left(nx^{n-1}+\ldots+h^{n-1}\right)}{h}\\&=\lim_{h\to0}\left(nx^{n-1}+\ldots+h^{n-1}\right)=nx^{n-1}\end{aligned}$$

follows. The result is true for $n=1$ , which has been proved earlier. We have 

$$\begin{aligned}\frac{d}{dx}\left(x^{n}\right)&=\frac{d}{dx}\left(x.x^{n-1}\right)\\&=\frac{d}{dx}\left(x\right)\left(x^{n-1}\right)+x.\frac{d}{dx}\left(x^{n-1}\right)\left(by product rule\right)\\&=1.x^{n-1}+x.\left(\left(n-1\right)x^{n-2}\right)\left(by induction hypothesis\right)\\&=x^{n-1}+\left(n-1\right)x^{n-1}=nx^{n-1}.\end{aligned}$$

Remark eoveul f $[x,]$ i.e., n can be any eal umr (but we will not prove it here)



12.5.2Derivativeof polynomials and trigonometric functionsWe start with the following theorem which tlls us the derivative of a polynomial function.

Theorem $\mathrm{Let}f(x)=a_n x^n+a_{n-1}x^{n-1}+\ldots+a_1x+a_0$ be a polynomial function, where $a_{i}s$ are all real numbers and $a_{n}^{'}\ne0$ . Then, the derivative function is given by 

$$\frac{df(x)}{dx}=na_{n}x^{n-1}+(n-1)a_{n-1}x^{x-2}+\ldots+2a_{2}x+a_{1}$$

Proof of this theorem is just putting together part (i) of Theorem 5 and Theorem 6.Example 13 Compute the derivative of $6x^{100}-x^{55}+x$ 



Solution A direct application of the above theorem tells that the derivative of the above function is $600x^{99}-55x^{54}+1$ 



Example 14 Find the derivative of $f(x)=1+x+x^2+x^3+\ldots+x^{50}\quad at\quad x=1$ 

Solution A direct applicationof the above Theorem6tells that the derivative of the above function is $1+2x+3x^{2}+\cdots+50x^{49}$ .the value of this function equals 

$$1+2(1)+3(1)^{2}+\ldots+50(1)^{49}=1+2+3+\ldots+50=\frac{(50)(51)}{2}=1275.$$

Example 15 Find the derivative of $f(x)=\frac{x+1}{x}$ 

Solution Clearly this function is defined everywhere except at $x=0$ . We use the quotient rule with $u=x+1and y=x$ . Hence $u^{\prime}=1and v^{\prime}=1$ . Therefore 

$$\frac{df(x)}{dx}=\frac{d}{dx}\left(\frac{x+1}{x}\right)=\frac{d}{dx}\left(\frac{u}{v}\right)=\frac{u^{\prime}v-uv^{\prime}}{v^{2}}=\frac{1(x)-(x+1)1}{x^{2}}=\frac{1}{x^{2}}$$

Example 16 Compute the derivative of sin 

Solution Let $f(x)=\sin$ . Then 

$$\begin{aligned}\frac{df(x)}{dx}&=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}=\lim_{h\to0}\frac{\sin(x+h)\sin(x)}{h}\\&=\lim_{h\to0}\frac{2\cos\left(\frac{2x+h}{2}\right)\sin\left(\frac{h}{2}\right)}{h}\quad(using formula for sin A-sin B)\\&=\lim_{h\to0}\cos\left(x+\frac{h}{2}\right)\lim_{h\to0}\frac{\sin\frac{h}{2}}{\frac{h}{2}}=\cos x.1=\cos x.\end{aligned}$$

Example 17 Compute the derivative of tan .

Solution $\mathrm{Let}f(x)=\tan x$ .Then 

$$\frac{df(x)}{dx}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}=\lim_{h\to0}\frac{\tan(x+h)-\tan(x)}{h}=\lim_{h\to0}\frac{1}{h}\left[\frac{\sin(x+h)}{\cos(x+h)}-\frac{\sin x}{\cos x}\right]$$

$$\begin{aligned}&\lim_{h\to0}\left[\frac{\sin(x+h)\cos x-\cos(x+h)\sin x}{h\cos(x+h)\cos x}\right]\\ &=\lim_{h\to0}\frac{\sin(x+h-x)}{h\cos(x+h)\cos x}\quad(using formula for\sin(A+B))\\ &=\lim_{h\to0}\frac{\sin h}{h}\cdot\lim_{h\to0}\frac{1}{\cos(x+h)\cos x}\\ &=1.\frac{1}{\cos^2x}=\sec^2x.\\ \end{aligned}Slished $$

Example 18 Compute the derivative of $f(x)=\sin^2x$ 

Solution We use the Leibnitz product rule to evaluate this.Slished 

*[Formula could not be recovered from OCR — see source PDF]*

1.Find the derivative $\mathrm{of}x^{2}-2\mathrm{at}x=10$ 

2.Find the derivative $\partial f_{x} 故 x=1$ 

3. Find the derivative of 99 at $x=100$ 

4.  i 



(i)

(i)

$$(i)\frac{x^{3}}{x^{2}}$$

(ii)

(iv)

$$(x-1)(x-2)$$

$$\frac{x+1}{x-1}$$

5. For the function 

$$f(x)=\frac{x^{100}}{100}+\frac{x^{99}}{99}+\ldots+\frac{x^2}{2}+x+1$$

Prove that $f^{\prime}(1)=100f^{\prime}(0)$ 

6.Find the derivative of $x^{n}+ax^{n-1}+a^{2}x^{n-2}+\ldots+a^{n-1}x+a^{n}$ for some fixed real number a.



7. For some constants a and $b,$ find the derivative of 

(i)$\left(x-a\right)\left(x-b\right)$ (ii)$\left(a x^{2}+b\right)^{2}$ (iii)$\frac{x-a}{x-b}$ 

8.Find the derivative of $\frac{x^{n}-a^{n}}{x-a}$ for some constant a.ablished 

9.Find the derivative of 

(i)

$$2x-\frac{3}{4}$$

(ii)

$$\left(5x^{3}+3x-1\right)(x-1) ablished $$

(i)

$$x^{-3}(5+3x)$$

(iv)

$$x^{5}\left(3-6x^{-9}\right) ablished $$

(v)

$$x^{-4}\left(3-4x^{-5}\right)$$

(vi)

$$\frac{2}{x+1}-\frac{x^{2}}{3x-1} ablished $$

10. Find the derivative of cos x from first principle.

11. Find the derivative of the following functions:

(i)sin x cos x secx (ii)$5\sec x+4\cos x$ 

(iv) cosec x $3\cot x+5\csc x$ 

(vi)$5\sin x-6\cos x+7$ (vii)$2\tan x-7\sec x$ 



##  Miscellaneous Examples 

Example19Find thederivativeofromthefirst principle,whereis iven 

(i)

$$f(x)=\frac{2x+3}{x-2}$$

(ii)

$$f(x)=x+\frac{1}{x}$$

Solution (i) Note that function is not defined at $x=2$ .But, we have 

$$f^{\prime}(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}=\lim_{h\to0}\frac{\frac{2(x+h)+3}{x+h-2}-\frac{2x+3}{x-2}}{h}$$

$$\begin{aligned}&=\lim_{h\to0}\frac{(2x+2h+3)(x-2)-(2x+3)(x+h-2)}{h(x-2)(x+h-2)}\\&=\lim_{h\to0}\frac{(2x+3)(x-2)+2h(x-2)-(2x+3)(x-2)-h(2x+3)}{h(x-2)(x+h-2)}\\&=\lim_{h\to0}\frac{-7}{(x-2)(x+h-2)}=-\frac{7}{(x-2)^2}\end{aligned}hed $$

Again, note that the function $f^{\prime}$ is also not defined at $x=2$ i ed 

(ii)  The function is not defined at $x=0$ .But, we have 

$$hed \begin{aligned}\int f^{\prime}(x)&=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}=\lim_{h\to0}\frac{\left(x+h+\frac{1}{x+h}\right)-\left(x+\frac{1}{x}\right)}{h}\\&=\lim_{h\to0}\frac{1}{h}\left[h+\frac{1}{x+h}-\frac{1}{x}\right]\\&=\lim_{h\to0}\frac{1}{h}\left[h+\frac{x-x-h}{x(x+h)}\right]=\lim_{h\to0}\frac{1}{h}\left[h\left(1-\frac{1}{x(x+h)}\right)\right]\\&=\lim_{h\to0}\left[1-\frac{1}{x(x+h)}\right]=1-\frac{1}{x^2}\end{aligned}$$

Again, note that the function f ' is not defined at $x=0$ 

Example 20 Find the derivative of f(x) from the first principle, where $f(x)$ is 

$$\begin{aligned}(i)\sin x+\cos x\quad&(ii)x\sin x\\ (iii)(i)\mathrm{we have}\quad&f(x)=\frac{f(x+h)-f(x)}{h}\\ &=\lim_{h\to0}\frac{\sin(x+h)+\cos(x+h)-\sin x-\cos x}{h}\\ &=\lim_{h\to0}\frac{\sin x\cos h+\cos x\sin h+\cos x\cos h-\sin x\sin h-\sin x-\cos x}{h}\end{aligned}$$

$$\begin{aligned}=\lim_{h\rightarrow0}\frac{\sin h(\cos x-\sin x)+\sin x(\cos h-1)+\cos x(\cos h-1)}{h}\\=\lim_{h\rightarrow0}\frac{\sin h}{h}(\cos x-\sin x)+\lim_{h\rightarrow0}\sin x\frac{(\cos h-1)}{h}+\lim_{h\rightarrow0}\cos x\frac{(\cos h-1)}{h}\\=\cos x-\sin x\end{aligned}$$

(ii)

$$\begin{aligned}f^{\prime}(x)&=\lim_{h\rightarrow0}\frac{f(x+h)-f(x)}{h}=\lim_{h\rightarrow0}\frac{(x+h)\sin(x+h)-x\sin x}{h}\\&=\lim_{h\rightarrow0}\frac{(x+h)(\sin x\cos h+\sin h\cos x)-x\sin x}{h}\\&=\lim_{h\rightarrow0}\frac{x\sin x(\cos h-1)+x\cos x\sin h+h(\sin x\cos h+\sin h\cos x)}{h}\\&=\lim_{h\rightarrow0}\frac{x\sin x(\cos h-1)}{h}+\lim_{h\rightarrow0}x\cos x\frac{\sin h}{h}+\lim_{h\rightarrow0}(\sin x\cos h+\sin h\cos x)\\&=x\cos x+\sin x\end{aligned}$$

Example 21 Compute derivative of 

$$f(x)=\sin2x\quad(ii)\quad g(x)=\cot x $$

Solution (i) Recall thetrigonometric formula sin $2x=2$ sin x cos x. Thus 

$$\frac{df(x)}{dx}=\frac{d}{dx}(2\sin x\cos x)=2\frac{d}{dx}(\sin x\cos x)^{\prime}\left[\left(\sin x\right)^{\prime}\cos x+\sin x\left(\cos x\right)^{\prime}\right]^{\prime}=2\left[\left(\cos x\right)\cos x+\sin x\left(-\sin x\right)\right]^{\prime}=2\left(\cos^{2}x-\sin^{2}x\right)$$

(ii) By definition,$\mathrm{g}(x)=\cot x=\frac{\cos x}{\sin x}$ . We use the quotient rule on this function 

wherever it is defined.$\frac{dg}{dx}=\frac{d}{dx}\left(\cot x\right)=\frac{d}{dx}\left(\frac{\cos x}{\sin x}\right)$ 

$$\begin{aligned}&\frac{\cos x}{x}=\frac{(\cos x)^{\prime}(\sin x)-(\cos x)(\sin x)^{\prime}}{(\sin x)^{2}}\\ &=\frac{(-\sin x)(\sin x)-(\cos x)(\cos x)^{\prime}}{(\sin x)^{2}}\\ &=-\frac{\sin^{2}x+\cos^{2}x}{\sin^{2}x}=-\cos\sec^{2}x\\ \end{aligned}$$

Alternatively, this may be computed by noting that cot $x=\frac{1}{\tan x}$ . Here, we use the fact that the derivative of tan  is derivative of the constant func $s e c^{2}$  h  e is 0.wu bis h that the 

$$\begin{aligned}\frac{dg}{dx}&=\frac{d}{dx}(\cot x)=\frac{d}{dx}\left(\frac{1}{\tan x}\right)^{\prime}\\&=\frac{(1)^{\prime}(\tan x)-(1)(\tan x)^{\prime}}{(\tan x)^{2}}\\&=\frac{(0)(\tan x)-(\sec x)^{2}}{(\tan x)^{2}}\\&=\frac{-\sec^{2}x}{\tan^{2}x}=\csc^{2}x\end{aligned} ublish $$

Example 22 Find the derivative of 

$$\frac{x^{5}-\cos x}{\sin x}\quad(ii)\quad\frac{x+\cos x}{\tan x}$$

Solution (i) Let $h(x)=\frac{x^{5}-\cos x}{\sin x}$ . We use the quotient rule on this function wherever it is defined.



$$h^{\prime}(x)=\frac{(x^{5}-\cos x)^{\prime}\sin x-(x^{5}-\cos x)(\sin x)^{\prime}}{(\sin x)^{2}}$$

$$\begin{aligned}&\frac{(5x^{4}+\sin x)\sin x-(x^{5}-\cos x)\cos x}{\sin^{2}x}\\ &=\frac{-x^{5}\cos x+5x^{4}\sin x+1}{(\sin x)^{2}}\\ \end{aligned}$$

(ii) We use quotient rule on the function $\frac{x+\cos x}{\tan x}$ wherever it is defined.

$$\begin{aligned}h^{\prime}(x)&=\frac{(x+\cos x)^{\prime}\tan x-(x+\cos x)(\tan x)^{\prime}}{(\tan x)^{2}}\\&=\frac{(1-\sin x)\tan x-(x+\cos x)\sec^{2}x}{(\tan x)^{2}}\end{aligned}$$

## Miscellaneous Exercise on Ch 

1. Find the derivative of the following functions from first principle:

(i)$-x$ (ii)(-x)−(ii)$\sin(x+1)$ (iv)$\cos(x-{\frac{\pi}{8}})$ 

Find the derivative ofthe following functions (it is to be understood that a, , ,p, q, r and s are fixed non-zero constants and m and n are integers):

2.$(x+a)$ 

3.

$$(px+q)\left(\frac{r}{x}+s\right)$$

4.

$$(ax+b)(cx+d)^2$$

5.$$ c 

6.

$$\frac{1+\frac{1}{x}}{1-\frac{1}{x}}$$

7.

$$\frac{1}{ax^{2}+bx+c}$$

8.

$$\frac{ax+b}{px^{2}+qx+r}$$

9.

$$\frac{px^{2}+qx+r}{ax+b}$$

10.

$$\frac{a}{x^{4}}-\frac{b}{x^{2}}+\cos x $$

11.

$$4\sqrt{x}-2$$

12.

$$(ax+b)^n $$

13.

$$(ax+b)^{n}(cx+d)^{m}$$

14.

$$\sin(x+a)$$

15. cosec x cot x 

16.

$$\frac{\cos x}{1+\sin x}$$

17.

$$\frac{\sin x+\cos x}{\sin x-\cos x}$$

18.

$$\frac{\sec x-1}{\sec x+1}$$

19.$\sin^{n}x$ 

20.

$$\frac{a+b\sin x}{c+d\cos x}$$

21.

$$\frac{\sin(x+a)}{\cos x}$$

22.

$$x^{4}(5\sin x-3\cos x)$$

23.

$$\left(x^{2}+1\right)\cos x\quad24.\quad\left(ax^{2}+\sin x\right)(p+q\cos x)$$

25.

$$\left(x+\cos x\right)\left(x-\tan x\right)\quad26.\quad\frac{4x+5\sin x}{3x+7\cos x}$$

27.

$$\frac{x^{2}\cos\left(\frac{\pi}{4}\right)}{\sin x}$$

28.

$$\frac{x}{1+\tan x}$$

29.

$$(x+\sec x)(x-\tan x)$$

30

$$\frac{x}{\sin^{n}x}$$

## Summary 

ne nointa to the laft ofs ofa point hand limit.



of the left and right hand limits, if they coincide.



For a function f and a real number a,$\varlimsup_{x\to a}f(x)$ and $f(a)$ may not be same (In 

For functionsf and g the following holds:

$$\begin{aligned}&\lim_{x\to a}\left[f(x)\pm g(x)\right]=\lim_{x\to a}f(x)\pm\lim_{x\to a}g(x)\\ &\lim_{x\to a}\left[f(x).g(x)\right]=\lim_{x\to a}f(x).\lim_{x\to a}g(x)\\ &\lim_{x\to a}\left[\frac{f(x)}{g(x)}\right]=\lim_{x\to a}f(x)\\ \end{aligned}$$

Following are some of the standard limits 

$$\lim_{x\to a}\frac{x^n-a^n}{x-a}=na^{n-1}$$

$$\lim_{x\to0}\frac{\sin x}{x}=1$$

$$\lim_{x\to0}\frac{1-\cos x}{x}=0$$

The derivative of a functionf at a is defined by 

$$f^{\prime}(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}$$

Derivative of a functionf at any point x is defined by 

$$f^{\prime}(x)=\frac{df(x)}{dx}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$$

wing holds:

$$\left\{\begin{aligned}(u\pm v)'=u'\pm v'\\ (uv)'=u'v+uv'\end{aligned}\right.$$

$\left(\frac{u}{v}\right)'=\frac{u'v-uv'}{v^2}$ provided all are defined.

Lobe 

$$\frac{d}{dx}(x^n)=nx^{n-1} Lobe $$

$$\frac{d}{dx}(\sin x)=\cos x Lobe $$

$$\frac{d}{dx}(\cos x)=-\sin x Lobe $$

## Historical Note 

In the history of mathematics two names are prominent to share the credit for inventing calculus,IssacNewton(1642–1727) and GW.Leibnitz(1646–1717).Both of them independently invented calculus around the seventeenth century.After the advent of calculus many mathematicians contributed for further development ofcalculus.The rigorous concept is mainly tributed to the great  mathematicians, A.L. Cauchy, J.L.Lagrange and Karl Weierstrass. Cauchy gave the foundation of calculus as we have now generally accepted in our textbooks.Cauchy used D'Alembert's limitconcepttodefinethederivativeofafunction.Starting withdefinitionofalimit, Cauchygave examplessuchasthe limit of $\frac{\sin\alpha}{\alpha}\quad for\quad\alpha=0.He\quad write\quad\frac{\Delta y}{\Delta x}=\frac{f(x+i)-f(x)}{i},$ and calledthe limit for $i\rightarrow0$ , the"functionderive'e, y'for $f^{\prime}\left(x\right)^{\ast}$ 



Before100,itasthought that calculus is quite diicult totach.Socalculus became beyond the reach of youngsters. But just in 1900, John Perry and others in England started propagating the view that sential ideas and methods ofcalculus weresimpleandcouldbetaughteveninschools.F npioneerde teaching of calculus to first year students. Thiswas regarded as one of the most daring act in those days.



Today notonly the mathematics but asPhysics,Chennstly,LcononihesandBlologicarSciencesareenjoyill 0g the fruits of calculus.

<div style="text-align: center;"><img src="imgs/img_in_image_box_130_659_633_1136.jpg" alt="Image" width="53%" /></div>
