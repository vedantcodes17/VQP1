

# APPLICATION OF INTEGRALS 

:One should study Mathematics because it is only through Mathematics that nature can be conceived in harmonious form. – BiRKHOFF 出

### 8.1 Introduction 

In geometry, we have learnt formulae to calculate areas of various geometrical figures including triangles,rectangles, trapezias and circles. Such formulae are fundamental in the applications of mathematics to many real life problems. The formulae of elementary geometry allow us to calculate areas of many simple figures.However, they are inadequate for calculating the areas enclosed by curves. For that we shall need some concepts of Integral Calculus.



In the previous chapter, we have studied to find the area bounded by the curve $y=f(x)$ 1, the ordinats $x=a$ $x=b$ and x-axis, while calculating definite integral as the limit of a sum. Here, in this chapter, we shall study a specific application of integrals to find the area under simple curves,area between lines and arcs of circles, parabolas and ellipses (standard forms only). We shall also deal with finding the area bounded by the above said curves.

### 8.2 Area under Simple Curves 

In the previous chapter, we have studied definite integral as the limit of a sum and how to evaluate definite integral using Fundamental Theorem of Calculus. Now,we consider the easy and intuitive way of finding the area bounded by the curve $y=f(x)$ 1,x-axis and the ordinates $x=a$ and $x=b$ .From Fig 8.1, we can think of area under the curve as composed of large number of very thin vertical strips. Consider where,h A $y=f(x)$ 1.the elementary 人${\mathrm{strip}}=y d x$ $x\{}$,

$$x=a $$

<div style="text-align: center;"><img src="imgs/img_in_image_box_783_683_1063_1011.jpg" alt="Image" width="23%" /></div>


<div style="text-align: center;">A.L. Cauchy (1789-1857)</div>


$$x=b $$

## MATHEMATICS 

This area is called the elementary area which is located at an arbitrary position within the egin whch is ciied by me value o bteen  nd .Wecan think of the total area A of the region between x-axis, ordinates $x=a,x=b$ and the curve $y=f(x)$ as the result of adding up the elementary areas of thin strips across the region PQRSP. Symbolically, we express 



$$\mathrm{A}=\int_{a}^{b}d\mathrm{A}=\int_{a}^{b}ydx=\int_{a}^{b}f(x)dx $$

The area A of the region bounded by the curve $x=g\ (y)$ , y-axis and the lines $y\;=\;c$ ,$y=d$ is given by 



$$\mathrm{A}=\int_{c}^{d}x d y=\int_{c}^{d}g(y)d y $$

Here, we consider horizontal strips as shown in the Fig 8.2



<div style="text-align: center;"><img src="imgs/img_in_image_box_655_453_996_750.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;">Fig 8.2</div>


Remark If the position of the curve under consideration is below the -axis, then since $f(x)<0from x=a to x=b$ , as shown in Fig 8.3, the area bounded by the curve, x-axis and the ordinates $x=a,x=b$ come out to be negative. But, it is only the numerical value of the area which is taken into consideration. Thus, if the area is negative, we take its absolute value, i.e.,$\left|\int_{a}^{b}f(x)dx\right|$ 

$$x=a $$

<div style="text-align: center;">Fig 8.3</div>


A bounded by the curve $y=f(x)$  in e  .e ,  ad $A_{1}<0$ and $\mathrm{A_{2}}>0$ $x=a$ and $x=b$ is given ,the area by $\mathrm{A}=|\mathrm{A}_{1}|+\mathrm{A}_{2}$ 



$$x=b $$

<div style="text-align: center;">Fig 8.4</div>


Example 1 Find the area enclosed by the circle $x^{2}+y^{2}=a^{2}$ 

Solution From Fig 8.5, the whole area enclosed by the given circle 



$=4$ (area of the region AOBA bounded by the curve, x-axis and the ordinates $x=0$ and $x=a$ [as the circle is symmetrical about both x-axis and y-axis]



$$\begin{aligned}=&4\int_{0}^{a}y dx\left(taking vertical strings\right)\\=&4\int_{0}^{a}\sqrt{a^{2}-x^{2}}dx\end{aligned}{\mathrm{S i n c e~}}x^{2}+y^{2}=a^{2}{\mathrm{~g i v e s~}}\quad y=\pm{\sqrt{a^{2}-x^{2}}}$$

<div style="text-align: center;">8</div>


$$\xrightarrow{\mathbf{A}(a,0)}\mathbf{X}$$

  e  e e     e e r e ie  e  i  



$$\frac{4\left[\left(\frac{x}{2}\sqrt{a^{2}-x^{2}}+\frac{a^{2}}{2}\sin^{-1}\frac{x}{a}\right)\right]^{a}}{}=4\left[\left(\frac{a^{2}}{2}\times0+\frac{a^{2}}{2}\sin^{-1}1\right)-0\right]=4\left(\frac{a^{2}}{2}\right)\left(\frac{\pi}{2}\right)=\pi a^{2}$$

 e  ee 

Y 



$$\begin{aligned}&\frac{1}{2}=4\int_{0}^{a}xdy=4\int_{0}^{a}\sqrt{a^{2}-y^{2}}dy\\&=4\left[\frac{y}{2}\sqrt{a^{2}-y^{2}}+\frac{a^{2}}{2}\sin^{-1}\frac{y}{a}\right]_{0}^{a}\\&=4\left[\left(\frac{a}{2}\times0+\frac{a^{2}}{2}\sin^{-1}1\right)-0\right]\\&=4\frac{a^{2}}{2}\frac{\pi}{2}=\pi a^{2}\\ \end{aligned}$$

Fig 8.6Example 2 Find the area enclosed by the ellipse $\left[\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1\right]$ 

Solution From Fig 8.7, the area of the region AB $\mathrm{A^{\prime}B^{\prime}A}$ bounded by the ellipse 

$$=4\left(\begin{aligned}&a r e a o f t h e r e g i o n A O B A\sin t h e f i r s t q u a d r a n t b o u n d e d\\ &b y t h e c u r v e,x-a x i s a n d t h e o r d i n a t e s x=0,x=a\end{aligned}\right)$$

(as the ellipse is symmetrical about both x-axis and y-axis)

$=4\int_{0}^{a}y dx$ (taking vert ical strips)

Now $\left(\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1\right)\mathrm{g}\mathrm{i}\mathrm{v}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{e}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}\mathrm{e}$ , but as the region AOBA lies in the first quadrant, y is taken as positive. So, the required area is 

$$\begin{aligned}&=4\int_{0}^{a}\frac{b}{a}\sqrt{a^{2}-x^{2}}dx\\&=\frac{4b}{a}\left[\frac{x}{2}\sqrt{a^{2}-x^{2}}+\frac{a^{2}}{2}\sin^{-1}\frac{x}{a}\right]_{0}^{a}(\mathrm{Why}?)\quad\overbrace{\quad\left.\frac{\mathbf{B}[(0,b)]}{\quad y\quad}\right|}^{\mathbf{B}\quad\left[\left(0,b\right)\right]}\\&=\frac{4b}{a}\left[\left(\frac{a}{2}\times0+\frac{a^{2}}{2}\sin^{-1}1\right)-0\right]\\&=\frac{4b}{a}\frac{a^{2}}{2}\frac{\pi}{2}=\pi ab\quad\overbrace{\quad\left.\frac{\mathbf{B}\left(0,b\right)}{\quad\left(-a,0\right)}\right|}^{\mathbf{X}\quad\left[\left(0,b\right)\right]}\quad\overbrace{\quad\left.\frac{\mathbf{B}\left(0,b\right)}{\quad\left(-a,0\right)}\right|}^{\mathbf{A}}\\ \end{aligned}Alte1show \begin{aligned}& 五寝证 \mathrm{e}\mathrm{f},\mathrm{considering}\quad\mathrm{horizontal}\mathrm{s}\mathrm{ps}\quad\mathrm{X}\quad\\ &\mathrm{yn}\quad\mathrm{in}\quad\mathrm{Fig}\quad8.8,\quad\mathrm{the}\quad\mathrm{are}\quad\mathrm{of}\quad\mathrm{the}\quad\mathrm{elipsis}\quad\mathrm{as}\quad\\ &=4\int_{0}^{b}x d y=4\frac{a}{b}\int_{0}^{b}\sqrt{b^2-y^2}d y\quad(\mathrm{Why?})\underbrace{\quad\mathrm{X}\llcorner\quad\mathrm{A}\quad\mathrm{B}\bigg|\underbrace{(0,b)}_{x\quad x\quad\mathrm{B}}\quad\mathrm{A}\quad\mathrm{X}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\quad\mathrm{B}\quad\mathrm{B}\quad\quad\mathrm{B}\quad\mathrm{B}\quad\mathrm{B}\quad\quad\mathrm{B}\quad\mathrm{B}\quad\quad\mathrm{B}\quad\mathrm{B}\quad\quad\mathrm{B}\quad\mathrm{B}\quad\quad\mathrm{B}\quad\mathrm{B}\quad\quad\mathrm{B}\quad\mathrm{B}\quad\quad\mathrm{B}\quad\mathrm{B}\quad\quad\mathrm{B}\quad\mathrm{B}\quad\quad\mathrm{B}\quad\mathrm{B}\quad\quad\mathrm{B}\quad\quad\mathrm{B}\quad\quad\mathrm{B}\quad\mathrm{B}\quad\quad\mathrm{B}\quad\mathrm{B}\quad\quad\mathrm{B}\quad\quad\mathrm{B}\quad\mathrm{B}\quad\quad\mathrm{B}\quad\quad\mathrm{B}\quad\quad\mathrm{B}\quad\quad\mathrm{B}\quad\quad\mathrm{B}\quad\quad\mathrm{B}\quad\quad\mathrm{B}\quad\quad\mathrm{B}\quad\quad\quad\mathrm{B}\quad\quad\mathrm{B}\quad\quad\mathrm{B}\quad\quad \end{aligned}}$$

#### 8.2.1 The area of the region bounded by a curve and a line 

In this subsection, we will find the area of the region bounded by a line and a circle,a line and a parabola, a line and an ellipse. Equations of above mentioned curves will be in their standard forms only as the cases in other forms go beyond the scope of this textbook.

Y←

Example 3 Find the area of the region bounded by the curve.$y=x^{2}$ and the line $y=4$ 

Solution Since the given curve represented by the equation $y=x^{2}$ is a parabola symmetrical about y-axis only, therefore, from Fig 8.9, the required area of the region AOBA is given by 

$$2{\int_{0}^{4}}xdy=2\left(\begin{aligned}&area of the region BONB bounded by curve,y-axis\\ &and the lines y=0and y=4\end{aligned}\right)$$

<div style="text-align: center;">Fig 8.9</div>


$$y=42\int_{0}^{4}\sqrt{y}dy=2\times\frac{2}{3}\left[y^{\frac{3}{2}}\right]_{0}^{4}=\frac{4}{3}\times8=\frac{32}{3}\quad(\mathrm{Why})$$

Here, we have taken horizontal strips as indicated in the Fig 8.9.

## MATHEMATICS 

Alternatively, we may consider the vertical strips like PQ as shown in the Fig 8.10 to obtain the area of the region AOBA. To this end, we solve the equations $x^{2}=y$ and.$y=4$ which gives $x=-2{\mathrm{~a n d~}}x=2$ 



$$x^{2}=y $$

Thus, the region AOBA may be stated as the region bounded by the curve.$y=x^{2},y=4$ and the ordinates $x=-2and x=2$ 

Therefore, the area of the region AOBA 

<div style="text-align: center;">$\begin{aligned}&\mathbf{Fig}_{2}=\int_{-2}^{2}ydx\quad&\mathbf{Fig}_{3}\\&\quad[y=(y-coordinate of Q)-(y-coordinate of P)=4-x^{2}]\\&=2\int_{0}^{2}\left(4-x^{2}\right)dx\quad&(\mathrm{Why}?)\\&=2\left[4x-\frac{x^{3}}{3}\right]_{0}^{2}=2\left[4\times2-\frac{8}{3}\right]_{0}^{2}=\frac{32}{3}\\ \end{aligned}$ 8.10</div>


$$\begin{aligned}&\mathbf{Fig}_{2}=\int_{-2}^{2}ydx\quad&\mathbf{Fig}_{3}\\&\quad[y=(y-coordinate of Q)-(y-coordinate of P)=4-x^{2}]\\&=2\int_{0}^{2}\left(4-x^{2}\right)dx\quad&(\mathrm{Why}?)\\&=2\left[4x-\frac{x^{3}}{3}\right]_{0}^{2}=2\left[4\times2-\frac{8}{3}\right]_{0}^{2}=\frac{32}{3}\\ \end{aligned}x=2$$

Remark From the above examples, it is inferred that we can consider either vertical strips or horizontal strips for calculating the area of the region. Henceforth, we shall consider either of these two, most preferably vertical strips.

Example 4 Find the area of the region in the first quadrant enclosed by the x-axis,

the line $y=x$ , and the circle $x^{2}+y^{2}=32$ 0

Y←



Solution The given equations are 

$${\begin{array}{rlr}&{}&{y=~x}\\ &{{\mathrm{and}}\qquad x^{2}+y^{2}=~32.}\end{array}}$$

Solving (1) and (2), we find that the line and the circle meet at B(4, 4) in the first quadrant (Fig 8.11). Draw perpendicular BM to the x-axis.



Therefore, the required :$\mathtt{area}=\mathtt{area}$ of the region OBMO + area of the region BMAB.



Now, the area of the region OBMO 

$$\begin{aligned}=\int_{0}^{4}ydx=\int_{0}^{4}xdx\\=\frac{1}{2}\left[x^{2}\right]_{0}^{4}=8\end{aligned}$$

<div style="text-align: center;">Fig 8.11</div>


$$y=x $$

Again, the area of the region BMAB 

$$\begin{aligned}&=\int_{4}^{4\sqrt{2}}ydx=\int_{4}^{4\sqrt{2}}\sqrt{32-x^{2}}dx\\ &=\left[\frac{1}{2}x\sqrt{32-x^{2}}+\frac{1}{2}\times32\times\sin^{-1}\frac{x}{4\sqrt{2}}\right]_{4}^{4\sqrt{2}}\\ &=\left(\frac{1}{2}4\sqrt{2}\times0+\frac{1}{2}\times32\times\sin^{-1}1\right)-\left(\frac{4}{2}\sqrt{32-16}+\frac{1}{2}\times32\times\sin^{-1}\frac{1}{\sqrt{2}}\right)\\ &=8\pi-(8+4\pi)=4\pi-8\\ \end{aligned}$$

Adding (3) and (4), we get, the required $\mathtt{area}=4\pi$ 

Example 5 Find the area bounded by the ellipse $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$ and the ordinates $x=0$ and $x=a e,\mathrm{where},b^{2}=a^{2}(1-e^{2})\mathrm{and}e<1$ 



Solution The required area (Fig 8.12) of the region BOB'RFSB is enclosed by the 

ellipse and the lines $x=0\;{\mathrm{and}}\;x=a e$ 

Y←



Note that the area of the region BOB'RFSB 

$$\begin{aligned}&a=\frac{1}{2}\int_{0}^{ae}ydx=2\frac{b}{a}\int_{0}^{ae}\sqrt{a^{2}-x^{2}}dx\\ &=\frac{2b}{a}\left[\frac{x}{2}\sqrt{a^{2}-x^{2}}+\frac{a^{2}}{2}\sin^{-1}\frac{x}{a}\right]_{0}^{ae}\\ &=\frac{2b}{2a}\left[ae\sqrt{a^{2}-a^{2}e^{2}}+a^{2}\sin^{-1}e\right]\\ &=ab\left[e\sqrt{1-e^{2}}+\sin^{-1}e\right]\\ \end{aligned}$$

<div style="text-align: center;">Fig 8.12</div>


$$x=a e $$

### EXERCISE 8.1

1. Find the area of the region bounded by the curve $y^{2}=x$ and the lines $x=1$ $x=4$ and the x-axis in the first quadrant.



2.Find the area of the region bounded by.$y^{2}=9x,x=2,x=4$ and the x-axis in the first quadrant.



## 366 MATHEMATICS 

3.first quadrant.of e   $x^{2}=4y,y=2,y=4$ and the y-axis in the 

4.Find the area of the region bounded by the ellipse $\frac{x^{2}}{16}+\frac{y^{2}}{9}=1$ 

5. Find the area of the region bounded by the ellipse $\frac{x^{2}}{4}+\frac{y^{2}}{9}=1$ 

6. Find the area of the region in the first quadrant enclosed by x-axis, line $x=\sqrt{3}y$ and the circle $x^{2}+y^{2}=4$ 0V c8T 7. Find the area of the EM a EM EM号e ci cle $x^{2}+y^{2}=a^{2}$ cut off by the line 公司添

8.$x=a,$ find the valu  et $$ .and $$ idividedl $$ (ci:2)

添司9.Find the area of the region bounded by the parabola $y=x^{2}and y=\left|x\right|$ 

10. Find the area bounded by the curve 添司添$x^{2}=4y$ and the line.EM $x=4y-2$ 

11. Find the area of the region bounded by the curve $y^{2}=4x$ and the line $x=3$ 

Choose the correct answer in the following Exercises 12 and 13.

12. Area lying in the first quadrant and bounded by the circle $x^{2}+y^{2}=4$ and the lines $x=0\;{\mathrm{and}}\;x=2$ is 



(A)π(B)$\frac{\pi}{2}$ (C)$\frac{\pi}{3}$ (D)$\frac{\pi}{4}$ 

13. Area of the region bounded by the curve $y^{2}=4x$ , y-axis and the line $y=3$ is 

(A)2(B)$\left[\frac{9}{4}\right.]$ (C)$\left[{\frac{9}{3}}\right.]$ (D)$\frac{9}{2}$ 

### 8.3 Area between Two Curves 

Intuitively, true in the sense of Leibnitz, integration is the act of calculating the area by cutting the region into a large number of small strips of elementary area and then adding up these elementary areas. Suppose we are given two curves represented by $y=f(x),y=g\left(x\right)$ ,where $f(x)\geq g(x)$ in $[a,b]$ as shown in Fig 8.13. Here the points of intersection of these two curves are given by $x=a$ and $x=b$ obtained by taking common values of y from the given equation of two curves.

For setting up a formula for the integral, it is convenient to take elementary area in the form of vertical strips. As indicated in the Fig 8.13, elementary strip has height  $f(x)-g(x)$ and width dx so that the elementary area 

$$y=f(x)x=a x=b $$

<div style="text-align: center;">Fig 8.13</div>


$d\mathrm{A}=[f(x)-g(x)]$ dx, and the total area A can be taken as 

$$\mathrm{A}=\int_{a}^{b}[f(x)-g(x)]d x $$

Alternatively,

$$\begin{aligned}\mathrm{A}=&\left[\mathrm{area}\right.\mathrm{bounded}\mathrm{by}y=f(x),x-\mathrm{axis}\mathrm{and}\mathrm{the lines}x=a,x=b]\\ &-\left[\mathrm{area}\right.\mathrm{bounded}\mathrm{by}y=g(x),x-\mathrm{axis}\mathrm{and}\mathrm{the lines}x=a,x=b]\\ =&\left.\int_{a}^{b}f(x)dx-\int_{a}^{b}g(x)dx\right.=\left.\int_{a}^{b}\left[f(x)-g(x)\right]dx,\mathrm{where}f(x)\geq g(x)\mathrm{in}[a,b]\right.\end{aligned}$$

I $\mathrm{f}f\left(x\right)\geq g\left(x\right)$ in [a, c] and $f(x)\leq g$ (x)in $[c,b]$ ,where $a<c<b$ as shown in the E 



Total $\mathrm{A r e a=A r e a}$ EM of the region $\mathrm{A C B D A+A r e a}$ ,of the region BPRQB 

$$\int_{a}^{c}\left[f\left(x\right)-g\left(x\right)\right]d x+\int_{c}^{b}\left[g\left(x\right)-f\left(x\right)\right]d x y=f(x)y=g\left(x\right)P \widetilde{y=g\left(x\right)}y=f(x)x=c x=b $$

Example 6 Find the area of the region bounded by the two parabolas $y=x^{2}\quad and\quad y^{2}=x$ 

parabolas are $\mathrm{~O~}(0,0)$ and $\mathrm{~A~}(1,1)$ as shown in the Fig 8.15.



Here, we can set $y^{2}=x\quad or\quad y=\sqrt{x}=f(x)$ and $y=x^{2}$ $=g\left(x\right)$ ,where,$f\left(x\right)\geq g\left(x\right)$ in [0, 1].

Therefore, the required area of the shaded region 

$$\begin{aligned}&f=\int_{0}^{1}\left[f(x)-g(x)\right]dx\\&=\int_{0}^{1}\left[\sqrt[3]{x}-x^2\right]dx=\left[\frac{2}{3}x^{\frac{3}{2}}-\frac{x^3}{3}\right]_{0}^{1}\\&=\frac{2}{3}-\frac{1}{3}=\frac{1}{3}\\ \end{aligned}$$

<div style="text-align: center;"><img src="imgs/img_in_image_box_678_379_1051_724.jpg" alt="Image" width="31%" /></div>


<div style="text-align: center;">Fig 8.15</div>


Example7 Find the area lying above $x\mathtt{-a x}$ :is and included between the circle $x^{2}+y^{2}=8x$ and inside of the parabola.$y^{2}=4x$ 



Solution The given equation of the circle $x^{2}+y^{2}=8x$ can be expressed as $(x-4)^{2}+y^{2}=16$ . Thus, the centre of the Y 

<div style="text-align: center;"><img src="imgs/img_in_image_box_609_942_1025_1315.jpg" alt="Image" width="34%" /></div>


circle is $(4,0)$ and radius is 4. Its intersection with the parabola $y^{2}=4x$ gives 

or 

or 

or 

$$\begin{aligned}x^{2}+4x&=8x\\x^{2}-4x&=0\\x\ (x-4)&=0\\x=0,x&=4\end{aligned}$$

Thus, the points of intersection of these two curves are $\mathrm{O}(0,0)$ and $\mathrm{P}(4{,}4)$ above the -axis.



From the Fig 8.16, the required area of the region OpQco included between these two curves above x-axis is 

$${\begin{array}{rl}&{=({\mathrm{a r e a~o f~t h e~r e g i o n~O C P O}})+({\mathrm{a r e a~o f~t h e~r e g i o n~P C Q P}})}\\ &{=\int_{0}^{4}y d x+\int_{4}^{8}y d x}\\ &{=2{\int_{0}^{4}}{\sqrt{x}}d x+{\int_{4}^{8}}{\sqrt{4^{2}-(x-4)^{2}}}d x\quad{\mathrm{(W h y?)}}}\end{array}}\begin{aligned}&=2\times\frac{2}{3}\left[x^{\frac{3}{2}}\right]_{0}^{4}+\int\limits_{0}^{4}\sqrt{4^{2}-t^{2}}dt,where,x-4=t\quad(Why?)\\&=\frac{32}{3}+\left[\frac{t}{2}\sqrt{4^{2}-t^{2}}+\frac{1}{2}\times4^{2}\times\sin^{-1}\frac{t}{4}\right]_{0}^{4}\\ \end{aligned}\frac{32}{3}+\left[\frac{4}{2}\times0+\frac{1}{2}\times4^{2}\times\sin^{-1}1\right]=\frac{32}{3}+\left[0+8\times\frac{\pi}{2}\right]=\frac{32}{3}+4\pi=\frac{4}{3}(8+3\pi)$$

Example 8 In Fig 8.17, AOBA is the part of the ellipse $9x^{2}+y^{2}=36$ in the first quadrant such that $OA=2and OB=6$ . Find the area between the arc AB and the chord AB.



Solution Given equation of the ellipse $9x^{2}+y^{2}=36$ can be expressed as $\frac{x^{2}}{4}+\frac{y^{2}}{36}=1$ or 

$$\left\{\frac{x^{2}}{2^{2}}+\frac{y^{2}}{6^{2}}=1and hence,its shape is as given in Fig8.17.\right\}$$

<div style="text-align: center;"><img src="imgs/img_in_image_box_711_852_1008_1264.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;">Fig 8.17</div>


Accordingly, the equation of the chord AB is 

or 

or 

$$\begin{aligned}y-0&=\frac{6-0}{0-2}(x-2)\\y&=-3(x-2)\\y&=-3x+6\end{aligned}$$

Area of the shaded region as shown in the Fig 8.17.

$$3\int_{0}^{2}\sqrt{4-x^{2}}dx-\int_{0}^{2}(6-3x)dx\quad(\mathrm{Why}?)3\left[\frac{x}{2}\sqrt{4-x^{2}}+\frac{4}{2}\sin^{-1}\frac{x}{2}\right]^{2}-\left[6x-\frac{3x^{2}}{2}\right]^{2}_{0}3\left[\frac{2}{2}\times0+2\sin^{-1}(1)\right]-\left[12-\frac{12}{2}\right]=3\times2\times\frac{\pi}{2}-6=3\pi-6$$

Example9Usin integrationindtheareof regioboundedbthe tiangle whose vertices are (1, 0), (2, 2) and (3, 1).Y 

<div style="text-align: center;"><img src="imgs/img_in_image_box_636_367_1042_638.jpg" alt="Image" width="34%" /></div>


<div style="text-align: center;">Fig 8.18</div>


Solution Let A(1, 0), B(2, 2) and C(3, 1) be the vertices of a triangle ABC (Fig 8.18).

Area of ∆ABC 

$$\begin{array}{r}{=\mathrm{A r e a~o f~}\Delta\mathrm{A B D~}+\mathrm{A r e a~o f~t r a p e z i u m}}\\ {\mathrm{BDEC}-\mathrm{A r e a~o f~}\Delta\mathrm{AEC}}\end{array}$$

Now equation of the sides AB, BC and CA are given by 



$$y=2(x-1),y=4-x,y={\frac{1}{2}}(x-1). , respectively.{\begin{aligned}&Hence,\quad area of\Delta ABC=\int_{1}^{2}2\left(x-1\right)dx+\int_{2}^{3}(4-x)dx-\int_{1}^{3}{\frac{x-1}{2}}dx\\ &\quad=2\left[{\frac{x^2}{2}}-x\right]_{1}^{2}+\left[4x-{\frac{x^2}{2}}\right]_{2}^{3}-{\frac{1}{2}}\left[{\frac{x^2}{2}}-x\right]_{1}^{3}\\ &\quad=2\left[\left({\frac{2^2}{2}}-2\right)-\left({\frac{1}{2}}-1\right)\right]+\left[\left(4\times3-{\frac{3^2}{2}}\right)-\left(4\times2-{\frac{2^2}{2}}\right)\right]-{\frac{1}{2}}\left[\left({\frac{3^2}{2}}-3\right)-\left({\frac{1}{2}}-1\right)\right]\\ &\quad={\frac{3}{2}}\end{aligned}}Example 10 Find the area of the region enclosed between the two circles:x^{2}+y^{2}=4$$



${\begin{aligned}&Hence,\quad area of\Delta ABC=\int_{1}^{2}2\left(x-1\right)dx+\int_{2}^{3}(4-x)dx-\int_{1}^{3}{\frac{x-1}{2}}dx\\ &\quad=2\left[{\frac{x^2}{2}}-x\right]_{1}^{2}+\left[4x-{\frac{x^2}{2}}\right]_{2}^{3}-{\frac{1}{2}}\left[{\frac{x^2}{2}}-x\right]_{1}^{3}\\ &\quad=2\left[\left({\frac{2^2}{2}}-2\right)-\left({\frac{1}{2}}-1\right)\right]+\left[\left(4\times3-{\frac{3^2}{2}}\right)-\left(4\times2-{\frac{2^2}{2}}\right)\right]-{\frac{1}{2}}\left[\left({\frac{3^2}{2}}-3\right)-\left({\frac{1}{2}}-1\right)\right]\\ &\quad={\frac{3}{2}}\end{aligned}}$ Example 10 Find the area of the region enclosed between the two circles:$x^{2}+y^{2}=4$ and $(x-2)^{2}+y^{2}=4$ 



Solution Equations of the given circles are 

$$x^{2}+y^{2}=4$$

and 

$$(x-2)^{2}+y^{2}=4$$

Equation (1) is a circle with centre O at the origin and radius 2. Equation (2) is a circle with centre C (2, 0) and radius 2. Solving equations (1) and (2), we have 



or 

or 

$$\begin{aligned}(x-2)^{2}+y^{2}&=x^{2}+y^{2}\\x^{2}-4x+4+y^{2}&=x^{2}+y^{2}\\x=1which gives y&=\pm\sqrt[\cdot]_{3}\end{aligned}$$

Thus, the points of intersection of the given circles are $\mathrm{A}(1,\sqrt{3})$ and $\mathrm{A}^{\prime}(1,-\sqrt{3})$ as shown in the Fig 8.19.



<div style="text-align: center;"><img src="imgs/img_in_image_box_689_1106_1035_1418.jpg" alt="Image" width="29%" /></div>


<div style="text-align: center;">Fig 8.19</div>


Required area of the enclosed region OACA'O between circles 

$$\begin{aligned}&=2\left[area of the region ODCAO\right]^{1}\quad(Why?)\\&=2\left[area of the region ODAO+area of the region DCAD\right]\\&=2\left[\int_{0}^{1}y dx+\int_{1}^{2}y dx\right]\\&=2\left[\int_{0}^{1}\sqrt{4-(x-2)^{2}}dx+\int_{1}^{2}\sqrt{4-x^{2}}dx\right]\quad(Why?)\\&=2\left[\frac{1}{2}\ (x-2)\sqrt{4-(x-2)^{2}}+\frac{1}{2}\times4\sin^{-1}\left(\frac{x-2}{2}\right)\right]_{0}^{1}\\&\quad+2\left[\frac{1}{2}\ x\sqrt{4-x^{2}}+\frac{1}{2}\times4\sin^{-1}\frac{x}{2}\right]_{1}^{1}\\&=\left[(x-2)\sqrt{4-(x-2)^{2}}+4\sin^{-1}\left(\frac{x-2}{2}\right)\right]_{0}^{1}+\left[x\sqrt{4-x^{2}}+4\sin^{-1}\frac{x}{2}\right]_{1}^{1}\\&=\left[\left(-\sqrt{3}+4\sin^{-1}\left(\frac{-1}{2}\right)\right)-4\sin^{-1}(-1)\right]+\left[4\sin^{-1}1-\sqrt{3}-4\sin^{-1}\frac{1}{2}\right]\\&=\left[\left(-\sqrt{3}-4\times\frac{\pi}{6}\right)+4\times\frac{\pi}{2}\right]+\left[4\times\frac{\pi}{2}-\sqrt{3}-4\times\frac{\pi}{6}\right]\\&=\left(-\sqrt{3}-\frac{2\pi}{3}+2\pi\right)+\left(2\pi-\sqrt{3}-\frac{2\pi}{3}\right)\\&=\frac{8\pi}{3}-2\sqrt{3}\\ \end{aligned}EXERCISE 8.2$$

1. Find the area of the circle $4x^{2}+4y^{2}=9$ which is interior to the parabola $x^{2}=4y$ 

2.Find the area bounded by curves $(x-1)^{2}+y^{2}=1and x^{2}+y^{2}=1$ 

3.Find the area of the region bounded by the curves.$y=x^{2}+2,y=x,x=0$ and 

$x=3$ 



Using egi d te aof gionboued bte iage hoe ertices are $(-1,0)$ , (1, 3) and (3, 2).



5.Using integration find the areaof the triangular region whose sides have the equations $y=2x+1,y=3x+1and x=4$ 



## MATHEMATICS 

公司添添



(′i:2)6(A)不$$ [Ta]  (ci)$x^{2}+y^{2}=4$ EM $x^{2}+y^{2}=4$ E and the line $$ is 

(A)A (ci)Ea](B)(ci)$\pi-2$ E (C)$2\pi-1$ (D)EM $2\:(\pi+2)$ TS 1

7. Area lying betwee E curves $y^{2}=4x$ and $y=2x$ is 

(A)$\frac{2}{3}$ (B)$\frac{1}{3}$ (C)$\frac{1}{4}$ (D)$\left[\frac{3}{4}\right.]$ 

## Miscellaneous Examples 

添司Example 11 Find the area of the parabola.$y^{2}=4ax$ :bounded by its latus rectum.

Soluti      e la $y^{2}=4ax$ is at origin (0, 0). The equation of the latus rectum $\mathrm{LSL'}$ is $x=a$ . Also, parabola is symmetrical about the x-axis.



The required area of the region OLL'O 

$$\begin{aligned}&\overset{\cdot}{\underset{\cdot}{=2}}\overset{\cdot}{\underset{\cdot}{\left(area of the region OLSO\right)}}\\ &\overset{\cdot}{\underset{\cdot}{=2}}\overset{\cdot}{\underset{\cdot}{\int_{0}^{a}ydx}}\overset{\cdot}{\underset{\cdot}{=2}}\overset{\cdot}{\underset{\cdot}{\int_{0}^{a}}}\overset{\cdot}{\underset{\cdot}{\sqrt{4ax}}}dx\\ &\overset{\cdot}{\underset{\cdot}{=2}}\overset{\cdot}{\underset{\cdot}{\times}}\overset{\cdot}{\underset{\cdot}{2}}\overset{\cdot}{\underset{\cdot}{\int_{0}^{a}}}\overset{\cdot}{\underset{\cdot}{\sqrt{x}dx}}\\ &\overset{\cdot}{\underset{\cdot}{=4}}\overset{\cdot}{\underset{\cdot}{\sqrt{a}}}\overset{\cdot}{\underset{\cdot}{\times}}\overset{\cdot}{\underset{\cdot}{2}}\overset{\cdot}{\underset{\cdot}{\sqrt{a}}}\overset{\cdot}{\underset{\cdot}{\sqrt{a}}}\overset{\cdot}{\underset{\cdot}{\sqrt{a}}}\\ &\overset{\cdot}{\underset{\cdot}{=8}}\overset{\cdot}{\underset{\cdot}{\sqrt{a}}}\overset{\cdot}{\underset{\cdot}{\sqrt{a}}}\overset{\cdot}{\underset{\cdot}{\sqrt{a}}}\overset{\cdot}{\underset{\cdot}{\sqrt{a}}}\overset{\cdot}{\underset{\cdot}{\sqrt{a}}}\\ \end{aligned}$$

Example 12 Find the area of the region bounded by the line $y=3x+2,$ the x-axis and the ordinates 

$x=-1{\mathrm{~a n d~}}x=1$ 



Solution As shown in the Fig 8.21, the line $y=3x+2$ meets x-axis at $x=\frac{-2}{3}$ and its graph lies below x-axis for $x\in\left(-1,{\frac{-2}{3}}\right)$ and above  $x\in\left({\frac{-2}{3}},1\right)$ 



<div style="text-align: center;"><img src="imgs/img_in_image_box_654_654_1002_1018.jpg" alt="Image" width="29%" /></div>


<div style="text-align: center;">Fig 8.20</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_637_1065_1020_1439.jpg" alt="Image" width="32%" /></div>


<div style="text-align: center;">Fig 8.21</div>


e e $\mathtt{a r e a=A r e a}$  e $\mathrm{A C B A+A r e a}$  e 

$$\left|\int_{-1}^{\frac{-2}{3}}(3x+2)dx\right|+\int_{\frac{-2}{3}}^{1}(3x+2)dx \left|\left[\frac{3x^{2}}{2}+2x\right]^{\frac{-2}{3}}\right|+\left[\frac{3x^{2}}{2}+2x\right]^{1}_{\frac{-2}{3}}=\frac{1}{6}+\frac{25}{6}=\frac{13}{3}$$

<div style="text-align: center;"><img src="imgs/img_in_image_box_567_636_1032_906.jpg" alt="Image" width="39%" /></div>


<div style="text-align: center;">Fig 8.22</div>


Example 13 Find the area bounded by the curve.$y=\cos x$ :between $x=0$ and 

$x=2\pi$ 



Solution From the Fig 8.22, the required $\mathtt{area}=\mathtt{area}$ of the region $\mathrm{OABO}+$ area of the region $\mathrm{BCDB}+\mathrm{area}$ of the region DEFD.



Thus, we have the required area 

$$\int_{0}^{\frac{\pi}{2}}\cos xdx+\left|\int_{\frac{\pi}{2}}^{\frac{3\pi}{2}}\cos xdx\right|+\int_{\frac{3\pi}{2}}^{2\pi}\cos xdx \left[\sin x\right]_{0}^{\frac{\pi}{2}}+\left|\left[\sin x\right]_{\frac{\pi}{2}}^{\frac{3\pi}{2}}\right|+\left[\sin x\right]_{\frac{3\pi}{2}}^{2\pi}=1+2+1=4$$

Example 13 Prove that the curves $y^{2}=4x\ and\ x^{2}=4y$ divide the area of the square bounded by $x=0,x=4$ ,X{0$ $y=4{\mathrm{~a n d~}}y=0$ into three equal parts.

Solution Note that the point of intersection of the parabolas.$y^{2}=4x$ and $x^{2}=4y$ are (0, 0) and (4, 4) as 

$$x^{2}=4y y^{2}=4x Q (4,4)$$

<div style="text-align: center;">Fig 8.23</div>


## MATHEMATICS 

shown in the Fig 8.23.

Now, the area of the region OAQBO bounded by curves $y^{2}=4x\ and\ x^{2}=4y$ 

$$\int_{0}^{4}\left(2\sqrt{x}-\frac{x^2}{4}\right)dx=\left[2\times\frac{2}{3}x^{\frac{3}{2}}-\frac{x^3}{12}\right]_{0}^{4}=\frac{32}{3}-\frac{16}{3}=\frac{16}{3}$$

Again, the area of the region $\mathrm{OPQAO}$ bounded by the curves $x^{2}=4y,x=0,x=4$ and x-axis 



$$\int_{0}^{4}\frac{x^{2}}{4}dx=\frac{1}{12}\left[x^{3}\right]_{0}^{4}=\frac{16}{3}$$

Similarly, the area of the region OBQRO bounded by the curve $y^{2}=4x$ ,y-axis,

$y=0\;{\mathrm{and}}\;y=4$ 



$$\int_{0}^{4}xdy=\int_{0}^{4}\frac{y^{2}}{4}dy=\frac{1}{12}\left[y^{3}\right]_{0}^{4}=\frac{16}{3}$$

From (1), (2) and (3), it is concluded that the area of the region $\mathrm{OAQBO}=\mathrm{area}$ of the region $\mathrm{O P Q A O=a r e a}$ of the region OBQRO, i.e., area bounded by parabolas $y^{2}=4x$ and $x^{2}=4y$ divides the area of the square in three equal parts.

Example 14 Find the area of the region 

$$\{(x,y):0\leq y\leq x^{2}+1,0\leq y\leq x+1,0\leq x\leq2\}$$

Solution Let us first sketch the region whose area is to be found out. This region is the intersection of the following regions.



and 

$$\begin{aligned}&\mathrm{A}_{1}=\{(x,y):0\leq y\leq x^{2}+1\},\\&\mathrm{A}_{2}=\{(x,y):0\leq y\leq x+1\}\\&\mathrm{A}_{3}=\{(x,y):0\leq x\leq2\}\\ \end{aligned}$$

<div style="text-align: center;">Fig 8.24</div>


$$x=2$$

The points of intersection of $y=x^{2}+1$ and $y=x+1$ are points P(0, 1) and Q(1, 2).From the Fig 8.24, the required region is the shaded region OPQRSTO whose area $=\mathtt{area}$ of the region $\mathrm{O T Q P O+a r e a}$  of the region TSRQT 

$$\int_{0}^{1}(x^2+1)dx+\int_{1}^{2}(x+1)dx\quad(\mathrm{Why}?)\begin{aligned}&x=\left[\left(\frac{x^3}{3}+x\right)\right]_1^1+\left[\left(\frac{x^2}{2}+x\right)\right]_1^2\\ &=\left[\left(\frac{1}{3}+1\right)-0\right]+\left[(2+2)-\left(\frac{1}{2}+1\right)\right]=\frac{23}{6}\\ \end{aligned}$$

## Miscellaneous Exercise on Chapter 8

1. Find the area under the given curves and given lines:

$$\begin{aligned}(i)y=x^{2},x=1,x=2and x-axis;\\ (ii)y=x^{4},x=1,x=5and x-axis;\end{aligned}$$

2. Find the area between the curves $y=x{\mathrm{~a n d~}}y=x^{2}.$ 

3.Find theaaoftiolittquadndboundd y $y=4x^{2}$ 

$x=0,y=1{\mathrm{~a n d~}}y=4$ 



4. Sketch the graph of $y=\left|x+3\right|$ and evaluate $\int_{-6}^{0}\left|x+3\right|dx$ 

5.Find the area bounded by the curve $y=\sin x$ : between $x=0\;{\mathrm{and}}\;x=2\pi$ 

6.Find the area enclosed between the parabola_$y^{2}=4a x$ and the line.$y=m x$ 

7. Find the area enclosed by the parabola $4y=3x^{2}$ and the line $2y=3x+12$ 

8.Find the area of the smaller region bounded by the ellipse $\frac{x^{2}}{9}+\frac{y^{2}}{4}=1$ and the 

$\mathrm{line}{\frac{x}{3}}{+}{\frac{y}{2}}{=}1$ 



9. Find the area of the smaller region bounded by the ellipse $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$ and the line $\frac{x}{a}+\frac{y}{b}=1$ 



10. Find the area of the region enclosed by the parabola $x^{2}=y$ ,the line $y=x+2$ and the x-axis.



11.Usingte mod of itegaioind te areabounddbyerve $|x|+|y|=1$ [Hint: The required region is bounded by lines $x+y=1,x-y=1,-x+y=1$ and 

$-x-y=1$ 



## 376 MATHEMATICS 

12.Find the area bounded by curves $\{(x,y):y\geq x^{2}\;{\mathrm{and}}\;y=|x|\}$ 

13. Using te method of integration ind the ara of the triangle ABC, oordinates of whose vertices are A(2, 0), B (4, 5) and $\mathrm{~C~}(6,3)$ 



14. Using the method of integration find the area of the region bounded by lines:

$$2x+y=4,3x-2y=6and x-3y+5=0$$

15. Find the area of the region $\{(x,y):y^{2}\leq4x,4x^{2}+4y^{2}\leq9\}$ 

Choose the correct answer in the following Exercises from 16 to 20.

16. Area bounded by the curve $y=x^{3}$ , the x-axis and the ordinates $x=-2and x=1$ is 

(A)$-9$ (B)$\frac{-15}{4}$ (C)$\frac{15}{4}$ (D)$\frac{17}{4}$ 

17. The area bounded by the curve $y=x\left|x\right|$ , x-axis and the ordinates $x=-1$ and $x=1$ is given by 



(A)0(B)$\left[{\frac{1}{3}}\right.]$ (C)$\frac{2}{3}$ (D)$\frac{4}{3}$ 

[Hint : $y=x^{2}if x>0and y=-x^{2}if x<0.$ 

18. The area of the circle $x^{2}+y^{2}=16$ exterior to the parabola $y^{2}=6x$ is 

(A)${\frac{4}{3}}(4\pi-{\sqrt{3}})$ (B)$\frac{4}{3}(4\pi+\sqrt{3})$  (C)${\frac{4}{3}}(8\pi-{\sqrt{3}})$ (D)${\frac{4}{3}}(8\pi+{\sqrt{3}})$ 

19. The area bounded by the y-axis,$y=\cos x\;and\;y=\sin x$ when $0\leq x\leq{\frac{\pi}{2}}$ is 

(A)$2({\sqrt{2-1}})$ (B)$\sqrt{2}-1$ (C)$\sqrt{2}+1$ (D)$\sqrt{2}$ 

## Summary 

The area of the region bounded by the curve $y=f(x)$ , x-axis and the lines $x=a\;{\mathrm{and}}\;x=b\;(b>a)$ is given by the formula:$\mathrm{Area}=\int_{a}^{b}ydx=\int_{a}^{b}f(x)dx$ 

国The area of the region bounded by the curve $x=\phi\;(y)$ , y-axis and the lines $y=c,y=d$ is given by the formula:$\mathrm{Area}=\int_{c}^{d}x d y=\int_{c}^{d}\phi(y)d y$ 

The area of the region enclosed between two curves $y=f\left(x\right),y=g\left(x\right)$ and the lines $x=a,x=b$ isgiven by the formula,

$$\begin{aligned}\mathrm{Area}=&\int_{a}^{b}\left[f(x)-g(x)\right]dx,\quad\mathrm{where},f(x)\geq g(x)\quad\mathrm{in}[a,b]\\mathrm{If}\quad&\mathrm{If}\quad f(x)\geq g(x)\quad\mathrm{in}[a,c]\quad\mathrm{and}\quad f(x)\leq g(x)\quad\mathrm{in}[c,b],\quad a<c<b,\quad\mathrm{then}\\mathrm{Area}=&\int_{a}^{c}\left[f(x)-g(x)\right]dx+\int_{c}^{b}\left[g(x)-f(x)\right]dx.\end{aligned}$$

## Historical Note 

The origin of the Integral Calculus goes back to the early period of development ofMathematics and it is related to the method of exhaustion developed by the mathematicians of ancient Greece.This method arose in the solution of problems on calculating areas of plane figures, surface areas and volumes of solid bodies etc.In this sense,the method of exhaustion can be regarded as an early method of integration.The greatest development of methodof exhaustion in the early period was obtained in the works of Eudoxus (440B.C.)and Archimedes (300B.C.)



Systematic approach to the theory of Calculus began in the 17th century.In 1665, Newton began his work on the Calculus described by him as te theory of fluxions and used his theory in finding the tangent andradiusofcurvature at any point on a curve.Nev wton introduced the basic notion of inverse function called the anti deriv ative (indef integral)or the inverse method of tangents.

During 168486,ib published an article in the Acta Eruditorum which he called Calculas was connected with the summation of a number of infinitely small areas,whose sum,he indicated by the symbol''.In 1696,he followed a su ggestion made by J.B Bernoulli and changed this article to Calculus integrali.This corresponded to Newt yton's inverse method of tangents.

Both Newton andLeibnitz adopted quite independent lines of approach which was radically different.However,respective theories accomplished results that were practically identical.Leibnitz tion of definite integral and what is quite certain is that he first clearly appreciated tie up between the antiderivative and thedefinite integral.ilea and 0primarily its relationships with Differential Calculus were developed in the work of P.de Fermat,,I.Newton and G.Leibnitz at the end of 17th century. However, this justification by the concept of limit was only developed in the works ofA..auchy intely9hentury.atlyt is worth mentioning the following quotation by Lie Sophie's:

I quotient tand integral which in their origin certainly go back to Archimedes were introduced in Science by the investi…vry that differentiation and integration are inverse operations belongs to Newton andLeibnitz".

