

# DIFFERENTIAL EQUATIONS 

出He who seeks for methods without having a definite problem in mind seeks for the most part in vain. – D. HILBERT …

### 9.1 Introduction 

In Class XI and in Chapter 5 of the present book, we discussed how to diferentiate a given functionf with respect toan $f^{\prime}(x)$ for a given function at each  in its domain of definition. Further, in the chapter on Integral Calculus, we discussed how to find a functionwhose derivative is thefunction g, wich may also be formulated as follows:

For a given function g, find a functionf such that 

$$\frac{dy}{dx}=g(x),\quad where y=f(x)$$

An equation of the form (1) is known as a diferential equation. A formal definition will be given later.

<div style="text-align: center;"><img src="imgs/img_in_image_box_685_559_948_889.jpg" alt="Image" width="26%" /></div>


<div style="text-align: center;">Henri Poincare (1854-1912 )</div>


These quiii itof,itiy,hmit Biolog equationshumed pimeimptacein l modertiicinvtiations.

Inthischa,wll studyomeaicottil quatio,general andparticulaolutionof entialquationormationof dfrential equations,metluao d some applications of differential equations in different areas.

### 9.2 Basic Concepts 

We are already familiar with the equations of the type:

$$\begin{aligned}x^{2}-3x+3&=0,\\sin x+\cos x&=0,\\x+y&=7\end{aligned}$$

Let us consider the equation:

$$x\frac{dy}{dx}+y=0$$

We see that equations (1), (2) and (3) involve independent and/or dpendent variable (variableyutuviblliivefpnt variable y with respect to the independent variable x. Such an equation is called a differential equation.



In general, an equation involving derivative (derivatives) of the dependent variable with respcttipndt iabeaislld difil quation.

Adifferentiluilviiot hspect o 

$$2\frac{d^{2}y}{d x^{2}}+\left(\frac{dy}{dx}\right)^{3}=0is an ordinary differential equation $$

Of course, there are differential equations involving derivatives with respect to more thadptalld illuout tis stage weshallconfineourslvestothestudyofordinarydirntialquationsonly.Now onward, we will use the term differential equation'for ordinary differential equation'.



## Note 

1.We shall prefer to use thefollowing notationsfor derivatives:

$$\frac{dy}{dx}=y',\frac{d^{2}y}{dx^{2}}=y'',\frac{d^{3}y}{dx^{3}}=y'''$$

2.Forderivativesofhigherorder,itwillbeinconvenienttoueso many dashes 

as supersuffix therefore, we use the notation $y_{n}$ for nth order derivative $\frac{d^{n}y}{d x^{n}}$ 

##### 9.2.1. Order of a differential equation 

Orde fiief the dependnt iable with espct totheindepedentvariableinvolved i the given differential equation.



Consider the following differential equations:

$$\frac{dy}{dx}=e^x \frac{d^{2}y}{dx^{2}}+y=0\left(\frac{d^{3}y}{dx^{3}}\right)+x^{2}\left(\frac{d^{2}y}{dx^{2}}\right)^{3}=0$$

The equations (6), (7) and (8) involve the highest derivative of first, second and thirdrr.uively.

#### 9.2.2 Degree  of a differential equation 

To study the degree of a differential equation, the key point is that the differential followil $y^{\prime},y^{\prime\prime},y^{\prime\prime\prime}$ ,etc. Consider the 

$$\frac{d^{3}y}{dx^{3}}+2\left(\frac{d^{2}y}{dx^{2}}\right)^{2}-\frac{dy}{dx}+y=0.\left(\frac{dy}{dx}\right)^2+\left(\frac{dy}{dx}\right)-\sin^2y=0\frac{dy}{dx}+\sin\left(\frac{dy}{dx}\right)=0$$

Wb $y''',y''$ and $y^{\prime}$ , equation (10)is a polynomil atio in $y^{\prime}$ (equatio $y^{\prime}$ and degree of such a differential equation can not be defined.



By the degree of a differential equation, when it is a polynomial equation in derivatives, we mean the highest power (positive integral index) of the highest order derivative involved in the given differential equation.



In vie of te above detin, ne a brvet frial quations (), (7),(8) and (9) each are of degree one, equation (10) is of degree two while the degree of differential equation (11) is not defined.



Note Order and degree (if defined)of a differential equation are always positive integers.



Example1Fid er and i deid, of achoftellowi dirential equations:

(i)

$$\frac{dy}{dx}-\cos x=0$$

(ii)

$$xy\frac{d^{2}y}{dx^{2}}+x\left(\frac{dy}{dx}\right)^{2}-y\frac{dy}{dx}=0$$

(im 

$$y'''+y^{2}+e^{y'}=0$$

Solution 

(i)Thehighestorder derivative present inthe differential equation is $\frac{dy}{dx}$ so its $y^{\prime}$ and the t or  $\frac{dy}{dx}$ is one, so its degree is one.



(i)Teiii lo $\frac{d^{2}y}{dx^{2}}$ ,SO its order is two. It is a polynomial equation in $\frac{d^{2}y}{dx^{2}}\quad and\quad\frac{dy}{dx}$ and the highest power raised to $\frac{d^{2}y}{dx^{2}}$ is one, so its degree is one.



(iii The highest order derivative present in the differential equation is $\left[y^{\prime\prime}\right.]$ ,so its order is three. The given differential equation is not a polynomial equation in its derivatives and so its degree is not defined.



### EXERCISE 9.1

Determine order and degree (if defined) of differential equations given in Exercises 1 to 10.



$$\frac{d^{4}y}{dx^{4}}+\sin(y^{\prime\prime})=0\quad2.\quad y^{\prime}+5y=0\quad3.\quad\left(\frac{ds}{dt}\right)^{4}+3s\frac{d^{2}s}{dt^{2}}=0.$$

4.

$$\left(\frac{d^{2}y}{dx^{2}}\right)^{2}+\cos\left(\frac{dy}{dx}\right)=0$$

5.

$$\frac{d^{2}y}{dx^{2}}=\cos3x+\sin3x $$

6.

$$(y''')^{2}+(y'')^{3}+(y')^{4}+y^{5}=0$$

7.

$$y'''+2y''+y'=0y^{\prime}+y=e^{x}\quad y^{\prime\prime}+(y^{\prime})^{2}+2y=0\quad10\quad y^{\prime\prime}+2y^{\prime}+\sin y=011. The degree of the differential equation $$

11. The degree of the differential equation 

$$\left(\frac{d^{2}y}{dx^{2}}\right)^{3}+\left(\frac{dy}{dx}\right)^{2}+\sin\left(\frac{dy}{dx}\right)+1=0is $$

(A)3Ea (B)2(C) 1(D)  not defined 

12. The order of the dirential equation 

$$2x^{2}\frac{d^{2}y}{dx^{2}}-3\frac{dy}{dx}+y=0\ is $$

(A)2(B)1(C)0



9.3. General and Particular Solutions of a Differential Equation In earlier Classes, we have solved the equations of the type:

$$x^{2}+1=0\sin^{2}x-\cos x=0$$

Solution ofquations1) and 2) are umbers, eal rcomplex, that wllaisy th given equation i.e., when that number is substituted for the unknown x in the given equation, L.H.S. becomes equal to the R.H.S..



$$Now consider the differential equation$\frac{d^{2}y}{d x^{2}}+y=0$ $$

In contrastto the first two equations,the solutionof this diferential quation i a function φ that will satisfy it i.e., when the function  is substituted for the unknown y (dependent variable) inthe given diferential equation, L.H.S. becomes equal to R.H.S.

The curve $y=\phi(x)$ is called the solution curve (integral curve) of the given differential equation. Consider the function given by 

$$y=\phi(x)=a\sin(x+b),$$

where a,$b\in\mathbb{R}$ When this function and its derivative are substituted in equation (3),$L.H.S.=R.H.S.$ ..So it is a solution of the differential equation ().

Let a and b be given some particular values say $a=2$ and $b=\frac{\pi}{4}$ , then we get a 

function 

$$y=\phi_{1}(x)=2\sin\left(x+\frac{\pi}{4}\right)$$

When this function and its derivative are substituted in equation (3) again $\mathrm{L.H.S.}=\mathrm{R.H.S}$ .. Therefore $\phi_{1}$ is also a solution of equation (3).

## MATHEMATICS 

Function φ consists oftwo arbitrary constants (parameters) a, and it is called general oliooftviluio.aunction $\boldsymbol{\upphi}_{1}$ contains no arbitrarycbutteiulluoftheam nandhene is called a particular solution of the given differential equation.

The solution which contains arbitrary constants is called the general solution (primitive) of the differential equation.



The solution free from arbitrary constants i.e., the solution obtained from the general solution by giving particular values to the arbitrary constants is called a particular solution of the differential equation.



Example 2 Verify that the function $y=e^{-3x}$ is a solution of the differential equation 

$$\frac{d^{2}y}{dx^{2}}+\frac{dy}{dx}-6y=0$$

Solution Given function is $y=e^{-3x}$ . Differentiating both sides of equation with respect to x , we get 



$$\frac{dy}{dx}=-3e^{-3x}$$

Now, differentiating (1) with respect to x, we have 

$$\frac{d^{2}y}{dx^{2}}=9e^{-3x}$$

Substituting the values of $\frac{d^{2}y}{dx^{2}},\frac{dy}{dx}$ and y in the given differential equation, we get 

$$\mathrm{L}.\mathrm{H}.\mathrm{S}_{x}=9e^{-3x}+(-3e^{-3x})-6e^{-3x}=9e^{-3x}-9e^{-3x}=0=\mathrm{R}.\mathrm{H}.\mathrm{S}.$$

Therefore, the given function is a solution of the given differential equation.

Example 3 Verify that the function $y=a\cos x+b$ sin , whre, a,$b\in\mathbb{R}$ .is a solution of the differential equation $\frac{d^{2}y}{dx^{2}}+y=0$ 



Solution The given function is 

$$y=a\cos x+b\sin x $$

Differentiating both sides of equation(1) with respectto , successively, we get 

$$\left\{\begin{aligned}\frac{dy}{dx}=-a\sin x+b\cos x\\ \frac{d^{2}y}{dx^{2}}=-a\cos x-b\sin x\end{aligned}\right.}$$

Substituting the values of $\frac{d^{2}y}{dx^{2}}$ and y in the given differential equation, we get 

$$\mathrm{L.H.S.}=(-a\cos x-b\sin x)+(a\cos x+b\sin x)=0=\mathrm{R.H.S.}Therefore, te ivn ti is a lti of te iv ial quation.$$

Therefore, te ivn ti is a lti of te iv ial quation.

### EXERCISE 9.2

Ich x)is solution of the corresponding differential equation:

$$\begin{aligned}&1\text{.}\quad y=e^{x}+1\quad&&:\quad y^{\prime\prime}-y^{\prime}=0\\&2\text{.}\quad y=x^{2}+2x+C\quad&&:\quad y^{\prime}-2x-2=0\\&3\text{.}\quad y=\cos x+C\quad&&:\quad y^{\prime}+\sin x=0\\&4\text{.}\quad y=\sqrt{1+x^{2}}\quad&&:\quad y^{\prime}=\frac{xy}{1+x^{2}}\\&5\text{.}\quad y=A x\quad&&:\quad xy^{\prime}=y(x\neq0)\\&6\text{.}\quad y=x\sin x\quad&&:\quad xy^{\prime}=y+x\sqrt{x^{2}-y^{2}}(x\neq0and x>y or x<-y)\\&7\text{.}\quad xy=\log y+C\quad&&:\quad y^{\prime}=\frac{y^{2}}{1-xy}(xy\neq1)\\&8\text{.}\quad y-\cos y=x\quad&&:\quad(y\sin y+\cos y+x)y^{\prime}=y\\&9\text{.}\quad x+y=\tan^{-1}y\quad&&:\quad y^{2}y^{\prime}+y^{2}+1=0\end{aligned}$$

10.

$$y=\sqrt{a^{2}-x^{2}}x\in(-a,a):\quad x+y\frac{dy}{dx}=0\left(y\neq0\right)$$

The numbr ofatryonantsinte eral oluio of ifrntial quation of fourth order are:

(A)0(B)2(C)3(D)4

12.The number of arbitrary constants in the particular solution of a diferential equation of third order are:

(A)3(B)2(C)1(D)0

9.4 Formation of a Differential Equation whose General Solution is given We know that the equation 



$$x^{2}+y^{2}+2x-4y+4=0$$

represents a circle having centre at (−1, 2) and radius 1 unit.

Differentiating equation (1) with respect to x, we get 

$$\frac{dy}{dx}=\frac{x+1}{2-y}(y\neq2)$$

whichll[that this equation represents the family of circles and one member of the family is the circle given in equation (1).



Let us consider the equation 

$$x^{2}+y^{2}=r^{2}$$

By giving differentvalues to r, we get diferent membersof thefamily e.g.$x^{2}+y^{2}=1,x^{2}+y^{2}=4,x^{2}+y^{2}=9$ etc. (see Fig 9.1).1

<div style="text-align: center;"><img src="imgs/img_in_image_box_605_515_913_802.jpg" alt="Image" width="30%" /></div>


<div style="text-align: center;">Fig 9.1</div>


Thus, equation (3) represents a family of concentric circles centered at the origin and having different radii.

We are interested in finding a differential equation that is satisfied by each member of the family. The differential equation must be free from r because r is different for different members of the family. This equati      h respect to , i.e,

$$2x+2y\frac{dy}{dx}=0\quad or\quad x+y\frac{dy}{dx}=0$$

which represents the family of concentric circles given by equation (3).

Again, let us consider the equation 

$$y=m x+c $$

By giving difrntaluestoe paramtrs  and , we et dint memers of the family, e.g.,

$$\begin{aligned}y&=x\quad&(m&=1,\ c&=0)\\y&=\sqrt{3}x\quad&(m&=\sqrt{3},\ c&=0)\\y&=x+1\quad&(m&=1,\ c&=1)\\y&=-x\quad&(m&=-1,\ c&=0)\\y&=-x-1\quad&(m&=-1,\ c&=-1)\mathrm{etic}.\end{aligned}$$

Thus,equaio()pteamilofaihties,whre,are parmr.We are now interested in finding a differential equation that is satisfied by each member of the family.Further, the equation must be free from m and  because m and 

c are different for different members of the family.This is obtained by differentiating equation (5) with respect to $x,$ successively we get 

$$\frac{dy}{dx}=m,\quad and\quad\frac{d^{2}y}{dx^{2}}=0$$

The equation (6) represents the family of straight lines given by equation (5).



Note that equations (3) and (5) are the general solutions of equations (4) and (6) respectively.

$$= −x-1\mathbf{X^{\prime}}$$

<div style="text-align: center;">Fig 9.2</div>


# 9.4.1Procedure toform adifferentialequationthatwill represent a given  family of curves  

(a)If the given family ci $ F_{1}$ of curves depends on only one parameter then it is represented by an equation of the form 

$$F_{1}(x,y,a)=0$$

For example, the family of parabolas $y^{2}=ax$ can be represented by an equation of the form $f(x,y,a):y^{2}=ax$ 



Differentiating equation (1) with respect to x, we get an equation involving $y^{\prime},y,x,$ and $a,$ i.e.,

$$g\left(x,y,y^{\prime},a\right)=0$$

The required dfferential equation is then obtained by liminating a from equations (1) and (2) as 



$$F(x,y,y')=0$$

(b)If the given family $\mathrm{F}_{\bar{2}}$ of curves depends on the parameters a,$b\:(\mathrm{say})$ then it is represented by an equation of the from 

$$F_{2}(x,y,a,b)=0$$

Differentiating equation (4) with respect to x, we get an equation involving $y^{\prime},x,y,\;a,b,\mathrm{i.e.}$ 9



$$g\left(x,y,y^{\prime},a,b\right)=0$$

But it is not possible to eliminate two parameters a and b from the two equations and so, we need a third equation. This equation is obtained by differentiating equation (5), with respect to x, to obtain a relation of the form 

$$h\left(x,y,y^{\prime},y^{\prime\prime},a,b\right)=0$$

The required differential equation is then obtained by eliminating a and b from equations (4), (5) and (6) as 



$$\mathrm{F}\left(x,y,y^{\prime},y^{\prime\prime}\right)=0$$

Note The order of a differential equation representing a family of curves is same as thenumberoarbiarycontantspresetithequationcorrespondig the family of curves.nnhato where, m is arbitrary constant.il qu  rve $$ 

Solution We have 

$$y=m x $$

e   

$$\frac{dy}{dx}=m $$

Substituting thevalueof ineqution (1) we get t $$ 

or 

$$x\frac{dy}{dx}-y=0$$



Example5 Form the differential equation representing the family of curves $y=a\sin(x+b)$ ,where a, b are arbitrary constants.



Solution We have 

$$y=a\sin(x+b)$$

Differentiatingboth sideofquation1)wih ect o $x,$ successively we get 

$$\frac{dy}{dx}=a\cos(x+b)\frac{d^{2}y}{dx^{2}}=-a\sin(x+b)$$

Eliminating a and b from equations (1), (2) and (3), we get 

$$\frac{d^{2}y}{dx^{2}}+y=0$$

whil equation.



Example 6 Form the differential equation representing the family of ellipses having foci on x-axis and centre at the origin.



/of ellipses (see Fig 9.3) is 

$$\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$$

<div style="text-align: center;"><img src="imgs/img_in_image_box_575_170_905_406.jpg" alt="Image" width="32%" /></div>


<div style="text-align: center;">Fig 9.3</div>


Differentiating equation (1) with respect to x, we get $\frac{2x}{a^{2}}+\frac{2y}{b^{2}}\frac{dy}{dx}=0$ 

or 

$$\frac{y}{x}\left(\frac{dy}{dx}\right)=\frac{-b^{2}}{a^{2}}$$

Differentiating both sides of equation (2) with respect to x, we get 

$$\frac{y}{x}\quad\frac{d^{2}y}{d x^{2}}\quad\frac{x\frac{dy}{dx}}{x^{2}}\quad\frac{dy}{dx}=0$$

or 

$$xy\frac{d^{2}y}{dx^{2}}\quad x\frac{dy}{dx}^{2}-y\frac{dy}{dx}=0$$

which is the required differential equation.

Example 7 Form the differential equation of the family of circles touching the x-axis at origin.

Solution Let C denote the family of circles touching x-axis at origin. Let (0, a) be the coordinates of the centre of any member of the family (see Fig 9.4).Therefore, equation of family C is 

$$x^{2}+(y-a)^{2}=a^{2}\ or\ x^{2}+y^{2}=2ay $$

where, a is an arbitrary constant. Differentiating both sides of equation (1) with respect to x,we get 

$$2x\quad2y\frac{dy}{dx}=2a\frac{dy}{dx}$$

<div style="text-align: center;"><img src="imgs/img_in_image_box_620_939_926_1275.jpg" alt="Image" width="30%" /></div>


<div style="text-align: center;">Fig 9.4</div>


or 

$$\int x\quad y{\frac{dy}{dx}}=a{\frac{dy}{dx}}\quad{\mathrm{or}}\quad a={\frac{x\quad y{\frac{dy}{dx}}}{\displaystyle{\frac{dy}{dx}}}}$$

Substituting the value of a from equation (2) in equation (1), we gt 

$$x^{2}+y^{2}=2y\frac{x\ dy\ dy}{\ dy}$$

or 

$$\frac{dy}{dx}(x^{2},y^{2})=2xy,2y^{2}\frac{dy}{dx}$$

or 

$$\frac{dy}{dx}=\frac{2xy}{x^{2}-y^{2}}$$

arr e a  e   r e e e qn 

 re   e  r  rrr ee e ee  r  rer r 

 e rre  r  ee ee r $(a,0)$ c er a rr e r a r  a   e 

$$y^{2}=4ax $$

Differentiating both sides of equation (1) with respect to x, we get 

$$2y\frac{dy}{dx}=4a $$

Substituting the value of 4a from equation (2)in equation (1), we get 



$$y^{2}=\left(2y\frac{dy}{dx}\right)(x)$$

or 

$$y^{2}-2xy\frac{dy}{dx}=0$$

which is the differential equation of the given family of parabolas.



<div style="text-align: center;"><img src="imgs/img_in_image_box_592_1025_906_1311.jpg" alt="Image" width="31%" /></div>


<div style="text-align: center;">Fig 9.5</div>


### EXERCISE 9.3

In each of the Exercises1 to 5,form a differential equation representing the given family of curves by eliminating arbitrary constants a and b.

$$\frac{x}{a}+\frac{y}{b}=1\quad2.\quad y^{2}=a(b^{2}-x^{2})\quad3.\quad y=a e^{3x}+b e^{-2x}$$

6.Form the differential equation of the family of circles touching the y-axis at origin.



7.Form the ifrential quatiootefamilyof parabolashaving vrtex at origin and axis along positive y-axis.



8.F centre at origin.



9.Frmoaxis and centre at origin.



10.Formthedifialqutioofamilofciclehavinreon-axis and radius 3 units.



11.Which of the following differential equations has $y=c_{1}e^{x}+c_{2}e^{-x}$ as the general solution?



$$\frac{d^{2}y}{dx^{2}}+y=0\quad(B)\quad\frac{d^{2}y}{dx^{2}}-y=0\quad(C)\quad\frac{d^{2}y}{dx^{2}}+1=0\quad(D)\quad\frac{d^{2}y}{dx^{2}}-1=0$$

12.  Which of the following differential equations has $y=x$ as one of its particular solution?



$$\begin{align*}\left(\mathrm{A}\right)\frac{d^{2}y}{d x^{2}}-x^{2}\frac{dy}{dx}+x y=x\quad\left(\mathrm{B}\right)\frac{d^{2}y}{d x^{2}}+x\frac{dy}{dx}+x y=x\\left(\mathrm{C}\right)\frac{d^{2}y}{d x^{2}}\quad x^{2}\frac{dy}{dx}\quad x y\quad0\quad\left(\mathrm{D}\right)\frac{d^{2}y}{d x^{2}}+x\frac{dy}{dx}+x y=0\end{align*}$$

9.5. Methods of Solving First Order, First Degree Differential Equations Insl equations.



#### 9.5.1 Differential equations with variables separable 

A first order-first degree differential equation is of the form 

$$\frac{dy}{dx}=\mathrm{F}(x,y)$$

If F $(x,y)$ can be expressed as a product $\mathrm{g}\:(x)\:h(y)$ , where,$g(x)$ is a function of x and $h(y)$ is a function of y, then the differential equation (1) is said to be of variable separable type. The differential equation (1) then has the form 

$$\frac{dy}{dx}=h\left(y\right).g\left(x\right)$$

If $h\left(y\right)\neq0$ , separating the variables, (2) can be rewritten as 

$$\frac{1}{h(y)}dy=g(x)dx $$

Integrating both sides of (3), we get 

$$\int\frac{1}{h(y)}dy=\int g(x)dx $$

Thus,4 ovoluioivfil uiin rm 

$$\mathrm{H}(y)=\mathrm{G}(x)+\mathrm{C}$$

Here, H (y) and $\mathrm{~G~}(x)$ are the anti derivatives of $\frac{1}{h(y)}$ and $g(x)$ respectively and C is the arbitrary constant.



Example 9 Find the general solution of the differential equation $\frac{dy}{dx}=\frac{x+1}{2-y},(y\neq2)$ Solution We have 



$$\frac{dy}{dx}=\frac{x+1}{2-y}$$

Separating the variables in equation (1), we get 

$$(2-y)dy=(x+1)dx $$

Integrating both sides of equation (2), we get 

$$\int\left(2-y\right)dy=\int\left(x+1\right)dx $$

or 

$$2y-\frac{y^{2}}{2}=\frac{x^{2}}{2}+x+C_{1}x^{2}+y^{2}+2x-4y+2C_{1}=0$$

which is thalluiootio1.

Example 10 Find the general solution of the differential equation $\frac{dy}{dx}=\frac{1+y^{2}}{1+x^{2}}$ 

Solution Since $1+y^{2}\neq0$ , therefore separating the variables, the given differntial equation can be writen as 



$$\frac{dy}{1+y^{2}}=\frac{dx}{1+x^{2}}$$

Integrating both sides of equation (1), we get 

$$\int\frac{dy}{1+y^{2}}=\int\frac{dx}{1+x^{2}}$$

or 

$$\tan^{-1}y=\tan^{-1}x+C $$

which is the general solution of equation (1).

Exame c $\frac{dy}{dx}=-4xy^{2}$ ,given that.$y=1$ ,when $x=0$ 



Solution If $y\neq0$ , the given differential equation can be written as 

$$\frac{dy}{y^{2}}=-4x\ dx $$

Integrating both sides of equation (1), we get 

or 

or 

$$\begin{aligned}\int\frac{dy}{y^{2}}&=-4\int x dx\\-\frac{1}{y}&=-2x^{2}+C\\y&=\frac{1}{2x^{2}-C}\end{aligned}$$

Substituting.$y=1and x=0$ in equation (2), we get,$C=-1$ 

Now substituting the value of C in equation (2), we get the particular solution of the given differential equation as $y=\frac{1}{2x^{2}+1}$ 



Example 12 Find the equation of the curve passing through the point (1, 1) whose differential equation is x $dy=(2x^{2}+1)dx\quad(x\neq0)$ 



Solution The given differential equation can be expressed as 

$$dy^{*}=\frac{2x^{2}\quad1}{x}dx^{*}$$

or 

$$dy=\left(2x+\frac{1}{x}\right)dx $$

Integrating both sides of equation (1), we get 

$$\int d y=\int\left(2x+\frac{1}{x}\right)d x $$

or 

$$y=x^{2}+\log|x|+C $$

Equation (2) represents the family of solution curves of the given diferential equation but we are interested in fnding the equation of a particular member of the family which passes through the point (1, 1). Therefore substituting $x=1,y=1$ in equation (2), we get $\mathrm{C}=0$ 



Now substittite valueoCi quati2) wet te quio ote required curve as $y=x^{2}+\log|x|$ 



Example13idequaioof urve aioueoit,, iventhat the slope of the tangent to the curve at any point $(x,y)\mathrm{is}\frac{2x}{y^2}$ 

Solution We know that the slope of the tangent to a curve is given by $\frac{dy}{dx}$ 

SO,

$$\frac{dy}{dx}=\frac{2x}{y^{2}}$$

Separating the variables, equation (1) can be written as 

$$y^{2}dy=2x dx $$

Integrating both sides of equation (2), we get 

$$\int y^{2}dy=\int2x dx $$

or 

$$\frac{y^{3}}{3}=x^{2}+C $$

Substituting $x=-2,y=3$ in equation (3), we get $\mathrm{C}=5$ 

Substituteuio,quofed curves 

$$\frac{y^{3}}{3}=x^{2}+5\quad or\quad y=(3x^{2}+15)^{\frac{1}{3}}$$

how many years Rs 1000 double itself? ly t e ra $$ per ear. In ,

cording to the given problem.

or 

$$\left\{\begin{aligned}\frac{dp}{dt}&=\left(\frac{5}{100}\right)\times\mathrm{P}\\ \frac{dp}{dt}&=\frac{\mathrm{P}}{20}\end{aligned}\right.$$

separating the variables in equation (1), we get 

$$\frac{dp}{\mathrm{P}}=\frac{dt}{20}$$

Integrating both sides of equation (2), we get 

or 

or 

Now 

$$\log\mathrm{P}=\frac{t}{20}+\mathrm{C}_{1}\quad\mathrm{P}=e^{\frac{t}{20}}\cdot e^{\mathrm{C}_{1}}\quad\mathrm{P}=\mathrm{C}e^{\frac{t}{20}}\quad\text{(where}e^{\mathrm{C}_{1}}=\mathrm{C})\quad\text{(where}t=0\text{)}$$

Substituting the values of P and t in (3), we get $C=1000$ . Therefore, equation (3),gives 



$$\mathbb{P}=1000e^{\frac{t}{20}}$$

Let t years be the time required to double the principal. Then 

$$2000=1000e^{\frac{t}{20}}\Rightarrow t=20\log_{a}2$$

### EXERCISE 9.4

Frcintion 

$$\frac{dy}{dx}=\frac{1-\cos x}{1+\cos x}\quad2.\quad\frac{dy}{dx}=\sqrt{4-y^{2}}\quad(-2<y<2)$$

3.

$$\frac{dy}{dx}+y=1(y\neq1)\sec^{2}x\tan ydx+\sec^{2}y\tan xdy=0\left(e^{x}+e^{-x}\right)d y-\left(e^{x}-e^{-x}\right)d x=0\quad 使 \quad\frac{dy}{dx}=\left(1+x^{2}\right)\left(1+y^{2}\right)$$

7.y log y $dx-x dy=0$ 

8.

$$x^{5}\frac{dy}{dx}=-y^{5}$$

9.

$$\frac{dy}{dx}=\sin^{-1}x e^{x}\tan y\ dx+(1-e^{x})\sec^{2}y\ dy=0$$

For each ofthe diferential equations in Exercises11 to14,fnd a particular solution satisfying the given condition:

11.

$$(x^{3}+x^{2}+x+1)\frac{dy}{dx}=2x^{2}+x;y=1\ when\ x=0$$

12.

$$x(x^{2}-1)\frac{dy}{dx}=1;y=0\ when\ x=2$$

13.$$ 

14.

$$\frac{dy}{dx}=y\tan x;y=1\ when\ x=0$$

equation is $y^{\prime}=e^{x}$ sin .



16.For the differential equation $xy\frac{dy}{dx}=(x+2)(y+2)$ , find the solution curve passing through the point $(1,-1)$ ).



17. Find the equation of a curve passing through the point (o, –2) given that at any point $(x,y)$ on the curve, the product of the slope of its tangent and y coordinate of the point is equal to the x coordinate of the point.



18. At any point $(x,y)$ of a curve, the slope of the tangent is twice the slope of the line segment joining the point of contact to the point $(-4,-3)$ 1.Find the equation of the curve given that it passes through (–2, 1).



19. The volume of spherical balloon being inflated changes at a constant rate. If initially its radius is 3 units and after 3 seconds it is 6 units. Find the radius of balloon after t seconds.



.$r\%$ per year. Find the value of r if Rs 100 double itself in 10 years $\log_{e}2=0.6931$ ).

2.Ilo%of Rs 1000is deposited with this bank,how much will it worth after10years $e^{0.5}=1.648$ E 22.In aculture,thebactria count is 1,00,000.Thenumber is incrased by 10% in 2hours. In how many hours will the count reach 2,000,if the rate of growth of bacteria is proportional to the number present?Ya0

2.quation $$ is is 

$$\begin{align*}\left(A\right)e^{x}+e^{-y}&=C\quad&\left(B\right)e^{x}+e^{y}&=C\\\left(C\right)e^{-x}+e^{y}&=C\quad&\left(D\right)e^{-x}+e^{-y}&=C\end{align*}$$

#### 9.5.2 Homogeneous dfferential equations 

Consider the following functions in x and y 

$$\begin{aligned}\mathrm{F}_{1}(x,y)&=y^{2}+2x y,\quad\mathrm{F}_{2}(x,y)=2x-3y,\\mathrm{F}_{3}(x,y)&=\cos\left(\frac{y}{x}\right),\quad\mathrm{F}_{4}(x,y)=\sin x+\cos y.\end{aligned}$$

If we replace x andy by λx and λy respectively in the above functions, for any nonzero constant λ, we get 



$$\begin{aligned}&\mathrm{F}_{1}\left(\lambda x,\lambda y\right)=\lambda^{2}\left(y^{2}+2x y\right)=\lambda^{2}\mathrm{F}_{1}(x,y)\\&\mathrm{F}_{2}\left(\lambda x,\lambda y\right)=\lambda\left(2x-3y\right)=\lambda\mathrm{F}_{2}(x,y)\\ \end{aligned}\mathrm{F}_{3}(\lambda x,\lambda y)=\cos\left(\frac{\lambda y}{\lambda x}\right)=\cos\left(\frac{y}{x}\right)=\lambda^{0}\mathrm{~F}_{3}(x,y)\mathrm{F}_{4}\left(\lambda x,\lambda y\right)=\sin\lambda x+\cos\lambda y\neq\lambda^{n}\mathrm{F}_{4}\left(x,y\right) , for any n\in\mathbf{N}$$

Here, we observe that the functions $\mathrm{F}_{1},\mathrm{F}_{2},\mathrm{F}_{3}$ can be written in the form $F(\lambda x,\lambda y)=\lambda^{n}F(x,y)$ but $ F_{4}$ can not be writt in this orm.Tis lads tothefollowing definition:

A function $\mathrm{F}(x,y)$ is said to be homogeneous function of degree n if 

$\mathrm{F}(\lambda\overline{x},\lambda y)=\lambda^n\mathrm{F}(x,y)$ for any nonzero constant $\lambda$ .

We note that in the above examples,$\mathrm{F}_{1},\mathrm{F}_{2},\mathrm{F}_{3}$ are homogeneous functions of degree 2, 1, 0 respectively but $ F_{4}$ is not a homogeneous function.

We also observe that 

$$\mathrm{F}_{1}(x,y)=x^{2}\left(\frac{y^{2}}{x^{2}}+\frac{2y}{x}\right)=x^{2}h_{1}\left(\frac{y}{x}\right)$$

or 

$$\mathrm{F}_{1}(x,y)=y^{2}\left(1+\frac{2x}{y}\right)=y^{2}h_{2}\left(\frac{x}{y}\right) ablish \mathrm{F}_{2}(x,y)=x^{1}\left(2-\frac{3y}{x}\right)=x^{1}h_{3}\left(\frac{y}{x}\right) ablish $$

or 

$$\mathrm{F}_{2}(x,y)=y^{1}\left(2\frac{x}{y}-3\right)=y^{1}h_{4}\left(\frac{x}{y}\right) ablish F_{3}(x,y)=x^{0}\cos\left(\frac{y}{x}\right)=x^{0}h_{5}\left(\frac{y}{x}\right) ablish \mathrm{F}_{4}(x,y)\neq x^{n}h_{6}\left(\frac{y}{x}\right),\text{for any}n\in\mathbf{N} ablish $$

or 

$$\mathrm{F}_{4}(x,y)\neq y^{n}h_{7}\left(\frac{x}{y}\right),\text{for any}n\in\mathbf{N} ablish $$

Therefore, a function F $(x,y)$ is a homogeneous function of degree n if 

$$\mathrm{F}(x,y)=x^{n}g\left(\frac{y}{x}\right)\quad\text{or}\quad y^{n}h\left(\frac{x}{y}\right)$$

A differential equation of the form $\frac{dy}{dx}=\mathrm{F}\left(x,y\right)$ is said to be homogenous if $\mathrm{F}(x,y)$ is a homogenous function of degree zero.



To solve a homogeneous differential equation of the type 

$$\frac{dy}{dx}=F(x,y)=g\left(\frac{y}{x}\right)$$

We make the substitution 

$$y=y.x $$

Differentiating equation (2) with respect to x, we get 

$$\frac{dy}{dx}=v+x\frac{dv}{dx}$$

Substituting the value of $\frac{dy}{dx}$ from equation (3) in equation (1), we get 

$$v+x\frac{dv}{dx}=g(v)$$

or 

$$x\frac{dv}{dx}=g(v)-v $$

Separating the variables in equation (4), we get 

$$\frac{dv}{g(v)-v}=\frac{dx}{x}$$

Integrating both sides of equation (5), we get 

$$\int\frac{dv}{g(v)-v}=\int\frac{1}{x}dx+C $$

Eua we replace v by $\frac{y}{x}$ 



Note If the homogeneous differential equation is in the form $\frac{dx}{dy}=\mathrm{F}(x,y)$ where, F $(x,y)$ is homogenous function of degree zero, then we make substitution $\frac{x}{y}=v i.e.,x=vy$ and we proceed further to find the general solution as discussed above by writing $\frac{dx}{dy}=\mathrm{F}(x,y)=h\left(\frac{x}{y}\right).$ 



Example 15 Show that the differential equation $(x-y)\frac{dy}{dx}=x+2y$ 'is homogeneous and solve it.



Solution The given differential equation can be expressed as 

$$\frac{dy}{dx}=\frac{x+2y}{x-y}$$

Let 

$$\mathrm{F}(x,y)=\frac{x\quad2y}{x\quad y}$$

Now 

$$\mathrm{F}(\lambda x,\lambda y)=\frac{\left(x\quad2y\right)}{\left(x\quad y\right)}\quad^{0}F(x,y)$$

Therefore,$\mathrm{F}\left(x,y\right)$ isa homogeous function of e o.$\mathrm{So}.$ the given differential equation is ahomogenous difrential quatio.



Alternatively,

$$\frac{dy}{dx}=\left(\frac{1+\frac{2y}{x}}{1-\frac{y}{x}}\right)=g\left(\frac{y}{x}\right)$$

R.H.S. of differential equation (2) is of the form $g\ \frac{y}{x}$ and so it is a homogeneous function of degree ero.Therefore, quation 1) is ahomogeneous diferential equation.To solve it we make the substitution 



$$y=vx $$

Differentiating equation (3) with respect to, x we get 

$$\frac{dy}{dx}=v+x\frac{dv}{dx}$$

Substituting the value ofy and $\frac{dy}{dx}$  in equation (1) we get 

or 

$$\left\{\begin{aligned}v+x\frac{dv}{dx}&=\frac{1+2v}{1-v}\\ x\frac{dv}{dx}&=\frac{1+2v}{1-v}-v\end{aligned}\right.}$$

or 

$$x\frac{dv}{dx}=\frac{v^{2}\quad v\quad1}{1\quad v}\frac{v\quad1}{y^{2}\quad y\quad1}dv=\frac{dx}{x}$$

Integrating both sides of equation (5), we get 

$$\frac{v\quad1}{v^{2}\quad v\quad1}dv=\quad\frac{dx}{x}\frac{1}{2}\frac{2v\quad1\quad3}{v^{2}\quad v\quad1}dv=-\log|x|+C_{1}\begin{aligned}&\frac{1}{2}\ \frac{2v\ 1}{v^{2}\ v\ 1}dv\ \frac{3}{2}\ \frac{1}{v^{2}\ v\ 1}dv\ \log|x|\ C_{1}\\ &\frac{1}{2}\log|v^{2}\ v\ 1|\ \frac{3}{2}\ \frac{1}{v\ \frac{1}{2}\ ^{2}\ \sqrt{3}}\ \frac{2v}{2}dv\ \log|x|\ C_{1}\\ &\\ &\frac{1}{2}\log|v^{2}\ v\ 1|\ \frac{3}{2}.\frac{2}{\sqrt{3}}\tan^{1}\ \frac{2v\ 1}{\sqrt{3}}\ \log|x|\ C_{1}\\ &\\ &\frac{1}{2}\log|v^{2}\ v\ 1|\ \frac{1}{2}\log x^{2}\ \sqrt{3}\tan^{1}\ \frac{2v\ 1}{\sqrt{3}}\ C_{1}\\ \end{aligned} bish $$

Replacing v by $\frac{y}{x}$ , we get 

or 

or 

or 

or 

$$bish \begin{aligned}&\frac{1}{2}\log\left|\frac{y^{2}}{x^{2}}\quad\frac{y}{x}\quad1\right|\quad\frac{1}{2}\log x^{2}\quad\sqrt{3}\tan^{1}\frac{2y\quad x}{\sqrt{3}x}\quad C_{1}\\ &\left|\frac{1}{2}\log\left|\left(\frac{y^{2}}{x^{2}}+\frac{y}{x}+1\right)x^{2}\right|=\sqrt{3}\tan^{-1}\left(\frac{2y+x}{\sqrt{3}x}\right)+C_{1}\right|\\ &+\log\left|\left(y^{2}+xy+x^{2}\right)\right|=2\sqrt{3}\tan^{-1}\left(\frac{2y+x}{\sqrt{3}x}\right)+2C_{1}\\ &+\log\left|\left(x^{2}+xy+y^{2}\right)\right|=2\sqrt{3}\tan^{-1}\left(\frac{x+2y}{\sqrt{3}x}\right)+C\\ \end{aligned}$$

which is the general solution of the differential equation (1)

Example16 Show that the differential equation $x\cos\left(\frac{y}{x}\right)\frac{dy}{dx}=y\cos\left(\frac{y}{x}\right)+x$ is homogeneous and solve it.



Solution The given differential equation can be written as 

$$\frac{dy}{dx}=\frac{y\cos\left(\frac{y}{x}\right)+x}{x\cos\left(\frac{y}{x}\right)}$$

It is a differential equation of the form $\frac{dy}{dx}=\mathrm{F}(x,y)$ 

Here 

$$\mathrm{F}(x,y)=\frac{y\cos\left(\frac{y}{x}\right)+x}{x\cos\left(\frac{y}{x}\right)}$$

Replacing  by λx and  by $\lambda y$ , e et 

$$\mathrm{F}(\lambda x,\lambda y)=\frac{\lambda[y\cos\left(\frac{y}{x}\right)+x]}{\lambda\left(x\cos\frac{y}{x}\right)}=\lambda^0[\mathrm{F}(x,y)] lulishe $$

Thus,E $\mathrm{F}\left(x,y\right)$ is ahomooioof dgeeo.a 

To solve it we make the substitution T lulishe 

$$y=vx $$

Dieren) ,

$$\frac{dy}{dx}=v+x\frac{dv}{dx}$$

Substituting the value of y and $\frac{dy}{dx}$ in equation (1), we get 

$$\begin{aligned}v+x\frac{dv}{dx}&=\frac{v\cos v+1}{\cos v}\\x\frac{dv}{dx}&=\frac{v\cos v+1}{\cos v}-v\\x\frac{dv}{dx}&=\frac{1}{\cos v}\\cos v\ dv&=\frac{dx}{x}\end{aligned}$$

Therefre 

$$\int\cos v dv=\int\frac{1}{x}dx $$

or 

or 

$$\begin{aligned}\sin v&=\log|x|+\log|C|\\sin v&=\log|Cx|\end{aligned}$$

Replacing v by $\frac{y}{x}$ , we get 

$$\sin\left(\frac{y}{x}\right)=\log|\mathrm{C}x|$$

ential equation (1).

Example 17 Show that the differential equation homogeneous and find its particular solution, given that,al eqution  $$ 

can be written as 

$$ERT \frac{dx}{dy}=\frac{2x e^{\frac{x}{y}}-y}{2y e^{\frac{x}{y}}}$$

Let 

ERT Then 

$$ERT \mathrm{F}(x,y)=\frac{2x e^{\frac{x}{y}}-y}{2y e^{\frac{x}{y}}}ERT 
\mathrm{F}(\lambda x,\lambda y)=\frac{\lambda\left(2xe^{\frac{x}{y}}-y\right)}{\lambda\left(2ye^{\frac{x}{y}}\right)}=\lambda^{0}[\mathrm{F}(x,y)]$$

Thus,$\mathrm{F}(x,y)$ is a homogeneous function of degree zero. Therefore, the given differential equation is a homogeneous differential equation.



To solve it, we make the substitution 

$$x=v y $$

Differentiating equation (2) with respect to y, we get 

$$\frac{dx}{dy}=v+y\frac{dv}{dy}$$

Substituting the value of x and $\frac{dx}{dy}$ in equation (1), we get 

$$\int_{v+y}^{}\frac{dv}{dy}=\frac{2v\ e^{v}-1}{2e^{v}}y\frac{dv}{dy}=\frac{2v e^{v}-1}{2e^{v}}-v y\frac{dv}{dy}=-\frac{1}{2e^{v}}2e^{v}dv=\frac{-dy}{y}\int2e^{v}\cdot dv=-\int\frac{dy}{y}$$

or 

$$2e^{y}=-\log|y|+C $$

and replacing v by $\frac{x}{y}$ we get 

$$2e^{\frac{x}{y}}+\log|y|=C $$

Substituting $x=0and y=1$  uation (3), weet 

$$2e^{0}+\log|1|=C\Rightarrow C=2$$

Substituting the value of C in equation (3), we get 

$$2e^{\frac{x}{y}}+\log|y|=2$$

which is the particular solution of the given differential equation.

Example 18 Show that the family of curves for which the slope of the tangent at any 

point $(x,y)$ on it is , is given by $x^{2}-y^{2}=cx$ 

Solution We know that the slope of the tangent at any point on a curve is $\frac{dy}{dx}$ 

Therefore,

$$\frac{dy}{dx}=\frac{x^{2}+y^{2}}{2xy}$$

or 

$$\frac{dy}{dx}=\frac{1+\frac{y^{2}}{x^{2}}}{\frac{2y}{x}}$$

ial equation.To solve it we make susitution 

$$y=vx $$

Differentiating.$y=vx$    with respect to (,)$$ we get we get 

$$\frac{dy}{dx}=v+x\frac{dv}{dx}$$

or 

$$\left[v+x\frac{dv}{dx}=\frac{1+v^2}{2v}\right]$$

or 

$$ERT x\frac{dv}{dx}=\frac{1-v^{2}}{2v}ERT \left[\frac{2v}{1-v^{2}}\right]=\frac{dx}{x}$$

or 

$$ERT \frac{2v}{v^{2}-1}dv=-\frac{dx}{x}$$

Therefore ERT 

or or or 

$$ERT \begin{aligned}\int\frac{2v}{v^{2}-1}dv&=-\int\frac{1}{x}dx\\log|v^{2}-1|&=-\log|x|+\log|C_{1}|\\log|(v^{2}-1)(x)|&=\log|C_{1}|\\(v^{2}-1)x&=\pm C_{1}\end{aligned}$$

Replacing v by $\frac{y}{x}$ ,we get 

$$\left(\frac{y^{2}}{x^{2}}-1\right)x=\pm C_{1}\quad(y^{2}-x^{2})=\pm C_{1}x or x^{2}-y^{2}=C x $$

### EXERCISE 9.5

In ac us and solve each of them.



$$\begin{aligned}1.\quad&(x^{2}+xy)dy=(x^{2}+y^{2})dx\quad&2.\quad y^{\prime}=\frac{x+y}{x}\\3.\quad&(x-y)dy-(x+y)dx=0\quad&4.\quad(x^{2}-y^{2})dx+2xy dy=0\\5.\quad&x^{2}\frac{dy}{dx}=x^{2}-2y^{2}+xy\quad&6.\quad xdy-y dx=\sqrt{x^{2}+y^{2}}dx\end{aligned}$$

7.

$$\left\{x\cos\left(\frac{y}{x}\right)+y\sin\left(\frac{y}{x}\right)\right\}y dx=\left\{y\sin\left(\frac{y}{x}\right)-x\cos\left(\frac{y}{x}\right)\right\}x dy 15x\frac{dy}{dx}-y+x\sin\left(\frac{y}{x}\right)=0\quad y\ dx+x\log\left(\frac{y}{x}\right)dy-2x\ dy=0 h x\frac{dy}{dx}-y+x\sin\left(\frac{y}{x}\right)=0\quad y\ dx+x\log\left(\frac{y}{x}\right)dy-2x\ dy=0$$

10.

$$1\quad e^{\frac{x}{y}}\quad dx\quad e^{\frac{x}{y}}\quad1\quad\frac{x}{y}\quad dy\quad0$$

For each of the differential equations in Exercises from 11 to 15, find the particular solution satisfying the given condition:

11.

$$(x+y)dy+(x-y)dx=0;y=1\ when\ x=1$$

12.$x^{2}dy+(xy+y^{2})dx=0;y=1\ when\ x=1$ 

13.

$$x\sin^{2}\frac{y}{x}\quad y\quad dx\quad x\quad dy\quad0;y\quad-\quad when x=1$$

14.

$$\frac{dy}{dx}-\frac{y}{x}+\csc\left(\frac{y}{x}\right)=0;\;y=0\;when\;x=1$$

15.

$$2xy+y^{2}-2x^{2}\frac{dy}{dx}=0;\ y=2\ when\ x=1$$

16.A homogeneous differential equation of the from $\frac{dx}{dy}=h\left(\frac{x}{y}\right)$ can be solved by making the substitution.



(A)$y=vx$ (B)$y=yx$ (C)$x=v y$ (D)$x=v$ 

17. Which of the following is a homogeneous differential equation?

$$\begin{aligned}&(A)(4x+6y+5)dy-(3y+2x+4)dx=0\\&(B)(xy)dx-(x^3+y^3)dy=0\\&(C)(x^3+2y^2)dx+2xy dy=0\\&(D)y^2dx+(x^2-xy-y^2)dy=0\end{aligned}$$

#### 9.5.3 Lineardifferential equations 

A differential equation of the from 

$$\frac{dy}{dx}+P y=Q $$

where,P andQare constantsorfunctionsofonly,isknown as afirstorder liear differentialquation.omexampleoftertordr liearirtialquation a oub 

$$\frac{dy}{dx}+y=\sin x \frac{dy}{dx}+\left(\frac{1}{x}\right)y=e^x \frac{dy}{dx}+\left(\frac{y}{x\log x}\right)=\frac{1}{x}$$

Another form of first order linear differential equation is 

$$\frac{dx}{dy}+P_{1}x=Q_{1}$$

where,$ P_{1}$ and $\mathrm{Q}_{1}$ are constants or functions of y only. Some examples of this type of differential equation are 



$$\left\{\begin{aligned}\frac{dx}{dy}+x=\cos y\\ \frac{dx}{dy}+\frac{-2x}{y}=y^{2}e^{-y}\end{aligned}\right.}$$

To solve the first order linear diferential equation of the type 

$$\frac{dy}{dx}\quad\mathrm{P}y=Q $$

Multiply both sides of the equation by a function of x say $g\left(x\right)$ to get 

$$g(x)\frac{dy}{dx}+P.(g(x))y=Q.g(x)$$

Choose $g\left(x\right)$ in such a waythat R.H.S.becomes a deriative of $\left[y\cdot g\left(x\right)\right.]$ 

i.e.

$$g(x)\frac{dy}{dx}+P.g(x)y=\frac{d}{dx}\left[y.g(x)\right]g(x)\frac{dy}{dx}+P.g(x)y=g(x)\frac{dy}{dx}+y g^{\prime}(x)$$

↓

$$P.g(x)=g^{\prime}(x)$$

or 

$$\mathrm{P}=\frac{g^{\prime}(x)}{g(x)}$$

Integrating both sides with respect to x, we get 

$$\int\mathrm{P}dx=\int\frac{g^{\prime}(x)}{g(x)}dx $$

or 

$$\int P\cdot dx=\log\left(g(x)\right)$$

or 

$$g(x)=e^{\int\mathbb{P}dx}$$

On multiple qui $g(x)=e^{\int\mathrm{P}dx}$ -, the L.H.S. becomes the derivative of some function of x and y. This function $g(x)=e^{\int\mathrm{P}dx}$ is called Integrating Factor (I.F.) of the given diferential equation.



Substituting the value of $g\left(x\right)$ in equation (2), we get 

or 

$$\begin{aligned}e^{\frac{\mathrm{P}dx}{dx}}\frac{dy}{dx}\mathrm{P}e^{\frac{\mathrm{P}dx}{dx}}y=Q e^{\frac{\mathrm{P}dx}{dx}}\\frac{d}{dx}y e^{\frac{\mathrm{P}dx}{dx}}=Q e^{\frac{\mathrm{P}dx}{dx}}\end{aligned}$$

Integrating both sides with respect to x, we get 

or 

$$\left\{\begin{aligned}y e^{\mathrm{P}d x}&=\quad\mathrm{Q}e^{\mathrm{P}d x}d x\\ &=e^{\mathrm{P}d x}\mathrm{Q}e^{\mathrm{P}d x}d x\quad\mathrm{C}\end{aligned}\right.}$$

which is the general solution of the differential equation.

Steps involved to solve firstorder linear differential equation:

(i) Write the given differential equation in the form $\frac{dy}{dx}+\mathrm{P}y=\mathrm{Q}$ where P, Q are constants or functions of x only.



(i) Find the Integrating Factor $(\mathrm{I}.\mathrm{F})=e^{\mathrm{P}d x}$ 

(i)ofilution s 

$$y\left(I.F\right)=\quad Q\times I.F dx\quad C $$

In case, the first order linear differential equation is in the form $\frac{dx}{dy}+P_{1}x=Q_{1}$ 

where,$ P_{1}$ and $\mathrm{Q}_{1}$ are constants or functions of y only. Then $\mathrm{I}.\mathrm{F}=e^{\mathrm{P}_{1}dy}$ and the solution of the differential equation is given by 

$$x_{n}(I.F)=\int\left(Q_{1}\times I.F\right)dy+C $$

Example 19 Find the general solution of the differential equation $\frac{dy}{dx}-y=\cos x$ 

Solution Given differential equation is of the form 

Therefore 

$$\frac{dy}{dx}+\mathrm{P}y=Q,\quad where\mathrm{P}=-1and Q=\cos x,\quad\mathrm{I},\mathrm{F}=e^{\frac{1}{2}dx}e^x $$

Multiplying both sides of equation by I.F, we get 

or 

$$\begin{aligned}e^{-x}\frac{dy}{dx}-e^{-x}y=e^{-x}\cos x,\\frac{dy}{dx}\left(y e^{-x}\right)=e^{-x}\cos x.\end{aligned}$$

On integrating both sides with respect to x, we get 

Let 

$$\begin{aligned}ye^{-x}&=\int e^{-x}\cos x dx+C\\ I&=\int e^{-x}\cos x dx\\&=\cos x\left(\frac{e^{-x}}{-1}\right)-\int(-\sin x)(-e^{-x})dx\end{aligned}\begin{aligned}\mathrm{I}&=\int\cos x\mathrm{e}^{-x}\mathrm{e}^{-x}\mathrm{d}x\\&=-\cos x\mathrm{e}^{-x}-\int\sin x\mathrm{e}^{-x}\mathrm{d}x\\&=-\cos x\mathrm{e}^{-x}-\left[\sin x\left(-e^{-x}\right)-\int\cos x\left(-e^{-x}\right)\mathrm{d}x\right]\\&=-\cos x\mathrm{e}^{-x}+\sin x\mathrm{e}^{-x}-\int\cos x\mathrm{e}^{-x}\mathrm{d}x\\mathrm{I}&=-e^{-x}\cos x+\sin x\mathrm{e}^{-x}-\mathrm{I}\\2\mathrm{I}&=\left(\sin x-\cos x\right)e^{-x}\\mathrm{I}&=\frac{\left(\sin x-\cos x\right)e^{-x}}{2}\end{aligned}$$

Substituting the value of I in equation (1), we get 

$$ye^{-x}=\left(\frac{\sin x-\cos x}{2}\right)e^{-x}+C $$

or 

$$y=\left(\frac{\sin x-\cos x}{2}\right)+C e^{x}$$

equation.

$x\frac{dy}{dx}+2y=x^{2}\left(x\ne0\right)$ c Solution The given differential equation is 

$$x\frac{dy}{dx}+2y=x^{2}$$

Dividing both sides of equation (1) by x, we get 

$$\frac{dy}{dx}+\frac{2}{x}y=x $$

which is a linear differential equation of the type $\frac{dy}{dx}+\mathrm{P}y=\mathrm{Q}$ , where $\mathrm{P}=\frac{2}{x}\text{and}\mathrm{Q}=x$ 

So 

$$\mathrm{IF}=e^{\int_{x}^{2}dx}=e^{2\log x}=e^{\log x^{2}}=x^{2}\left[\cos e^{\log f(x)}=f(x)\right]$$

Therefore, solution of the given equation is given by 

or 

$$y\cdot x^{2}=\int\left(x\right)\left(x^{2}\right)dx+C=\int x^{3}dx+C $$

which is the general solution of the given differential equation.

Exampe1loltion $dx-(x+2y^{2})dy=0$ Solution The given differential equation can be writen as cYano 

$$\frac{dx}{dy}-\frac{x}{y}=2y $$

This is   l uitt $$ 

$Q_{1}=2y$ '.Therefore $$ F 

uation is 

or 

or 

or 

$$\begin{aligned}\int x\frac{1}{y}&=\int(2y)\left(\frac{1}{y}\right)dy+C\\frac{x}{y}&=\int(2dy)+C\\frac{x}{y}&=2y+C\\x&=2y^2+C y\end{aligned}$$

which is a general solution of the given differential equation.

Example 22 Find the particular solution of the differential equation 

$$\frac{dy}{dx}+y\cot x=2x+x^{2}\cot x\left(x\neq0\right)$$

given that $y=0$ when $x=\frac{\pi}{2}$ 

Solution The given equation is a linear differential equation of the type $\frac{dy}{dx}+\mathrm{P}y=Q$ where $\mathrm{P}\equiv\cot x$ and $Q=2x+x^{2}$ cot x. Therefore 

$$\mathrm{I}.\mathrm{F}=e^{\cot xdx}\quad e^{\log\sin x}\quad\sin x $$

Hence, the solution of the differential equation is given by 

$$y\cdot\sin x=\int\left(2x+x^{2}\cot x\right)\sin x dx+C y\sin x=\int2x\sin x\ dx+\int x^{2}\cos x\ dx+C y\sin x=\sin x\left(\frac{2x^{2}}{2}\right)-\int\cos x\left(\frac{2x^{2}}{2}\right)dx+\int x^{2}\cos x dx+C $$

or 

$$y\sin x=x^{2}\sin x-\int x^{2}\cos x\ dx+\int x^{2}\cos x\ dx+C $$

Substituting $y=0$ and $x=\frac{\pi}{2}$ in equation in equation (1), we get (1), we get 

$$0=\left(\frac{\pi}{2}\right)^2\sin\left(\frac{\pi}{2}\right)+C $$

or 

$$\mathrm{C}=\frac{-\pi^{2}}{4}$$

), we get 

$$y\sin x=x^{2}\sin x-\frac{\pi^{2}}{4}$$

or 

$$y=x^{2}-\frac{\pi^{2}}{4\sin x}\quad(\sin x\neq0)$$

en differential equation.

nessing throuoh the point (0  1) If the slope of the tangent to the curve at any point $(x,y)$ is equal to the sum of the x coordinate (abscissa) and the product of the x coordinate and y coordinate (ordinate) of that poin.Solution We know that the $\frac{dy}{dx}$ 

Therefore,

$$\frac{dy}{dx}=x+xy $$

or 

$$\frac{dy}{dx}-xy=x $$

Thi is ee quation of the type $\frac{dy}{dx}+\mathrm{P}y=\mathrm{Q}$ , where $\mathrm{P}=-x\mathrm{~and~Q}=x$ 

Therefore,

$$\mathrm{F}=e^{\int-x dx}=e^{\frac{-x^2}{2}}$$

Hence, the solution of equation is given by 

$$y\cdot e^{\frac{-x^2}{2}}=\int(x)\left(e^{\frac{-x^2}{2}}\right)dx+C $$

Let 

$$\mathrm{I}=\int(x)e^{\frac{-x^2}{2}}dx $$

Let $\frac{-x^{2}}{2}=t$ ,then $-x dx=dt or x dx=-dt.$ 

Therefore,

$$\mathrm{I}=-\int e^{t}dt=-e^{t}=-e^{\frac{-x^{2}}{2}}$$

Substituting the value of I in equation (2), we get 

or 

$$\begin{aligned}y e^{\frac{-x^2}{2}}&=-\frac{x^2}{2}+C\\y&=-1+C e^{\frac{x^2}{2}}\end{aligned}$$

Now (3) represents the equation of family of curves. But we are interested in urves.Bt ee n finding a particular member of the family passing through (0, 1). Substituting $x=0$ and $y=1$ in equation (3) we get 



$$1=-1+C,e^{0}\quad\mathrm{or}\quad C=2$$

Substituting the value of C in equation (3), we get 

$$y=-1+2e^{\frac{x^2}{2}}$$

which is the equation of the required curve.

### EXERCISE 9.6

For each of the dfrential quations given in Exrcis 1 to2,ind the eneral solution:

$$\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{x}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{y}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{y}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{y}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{y}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{y}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{y}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{y}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{y}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{y}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{y}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{y}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{y}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{y}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{y}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{y}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}=\frac{y}{2}\cdot\frac{y}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}+\cos x=\frac{y}{2}\cdot\frac{2}{2}\cdot\frac{dy}{dx}+\frac{y}{\cos x}+\frac{\cos x}{2}+\cdot\frac{y}{\cos x}=\frac{2}{2}\cdot\frac{\cos x}{2}+\cdot\frac{y}{2}\cdot\frac{\cos x}{2}+\cdot\frac{\cos x}{2}+\frac{\cos x}{2}+\cdot\frac{\cos x}{2}+\cdot\frac{y}{2}\cdot\frac{\cos x}{2}+\cdot\frac{\cos x}{2}+\frac{2}\cdot\frac{\cos x}{2}+\cdot\frac{2}{2}+\cdot\frac{\cos x}{2}+\frac{2}\cdot\frac{2}{2}\cdot\cdot\frac{\frac{2}{2}\cdot\cdot\frac{2}{2}\cdot\cdot\frac{2}{2}}\cdot\cdot\frac{2}{2}\cdot\cdot\frac{2}\cdot\frac{2}{2}\cdot\cdot\frac{2}{2}\cdot\cdot\frac{2}\cdot\frac{2}{2}\cdot\cdot\frac{2}\cdot\cdot\frac{2}{2}\cdot\cdot\frac{2}{2}\cdot\cdot\cdot\frac{2}\cdot\frac{2}{2}\cdot\cdot\cdot\frac{2}\cdot\frac{2}{2}\cdot\cdot\cdot\frac{2}\cdot\cdot\frac{2}{2}\cdot\cdot\cdot\frac{2}\cdot\frac{2}\cdot\cdot\frac{2}{2}\cdot\cdot\cdot\frac{2}\cdot\cdot\frac{2}{2}\cdot\cdot\cdot\frac{2}\cdot\cdot\cdot\frac{2}{2}\cdot\cdot\cdot\cdot\frac{2}\cdot\cdot\frac{2}\cdot\cdot\cdot\frac{2}{2}\cdot\cdot\cdot\cdot\frac{2}\cdot\cdot\cdot\frac{2}\cdot\cdot\cdot\frac{2}\cdot\cdot\frac{2}\cdot\cdot\cdot\cdot\frac{2}\cdot\cdot\cdot\frac{2}\cdot\cdot\cdot\cdot\frac{2}\cdot\cdot\cdot\cdot\frac{2}\cdot\cdot\cdot\frac{2}\cdot\cdot\cdot\cdot\frac{2}\cdot\cdot\cdot\cdot\cdot\cdot\frac{2}\cdot\cdot\cdot\cdot\cdot\frac{2}\cdot\cdot\cdot\cdot\cdot\cdot\frac{2}\cdot\cdot\cdot\cdot\cdot\cdot\frac{2}\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\frac{2}\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\frac{2}\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\frac{2}\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\x\frac{dy}{dx}+y-x+xy\cot x=0\quad(x\neq0)\quad(x+y)\frac{dy}{dx}=1$$

For each of the differential equations given in Exercises 13 to 15,find a particular solution satisfying the given condition:

13.

$$\frac{dy}{dx}+2y\tan x=\sin x;y=0\quad when\quad x=\frac{\pi}{3}$$

14.$(1+x^{2})\frac{dy}{dx}+2xy=\frac{1}{1+x^{2}};y=0\quad when x=1$ 

15.$\frac{dy}{dx}-3y\cot x=\sin2x;y=2\ when\ x=\frac{\pi}{2}$ 

16.Find uo uvethtei te of the tangent to the curve at any point (, ) is equal to the sum of the coordinates of the point.



17.Find the quationof acurve pasing through the point (,2) given that the sum of the coordinates of any point on the curve exceeds the magnitude of the slope of the tangent to the curve at that point by 5.



18. The Integrating Factor of the differential equation $x\frac{dy}{dx}-y=2x^{2}$ is 

(A)$e^{-x}$ (B)$e^{-y}$ (C)$\frac{1}{x}$ (D)

19. The Integrating Factor of the differential equation 

$$(1-y^{2})\frac{dx}{dy}+yx=ay(1\quad y\quad1)is $$

(A)$\frac{1}{y^{2}}$ (B)$\frac{1}{\sqrt{y^{2}-1}}$ (C)$\frac{1}{1-y^{2}}$ (D)$\frac{1}{\sqrt{1-y^{2}}}$ 

## Miscellaneous Examples 

Example 24 Verify that the function $y=c_{1}e^{ax}\cos bx+c_{2}e^{ax}$ sin bx, where $c_{1},c_{2}$ are arbitrary constants is a solution of the diferential equation 

$$\frac{d^{2}y}{dx^{2}}-2a\frac{dy}{dx}+\left(a^{2}+b^{2}\right)y=0$$

Solution The given function is 

$$y=e^{ax}\left[c_1\cos bx+c_2\sin bx\right]$$

Differentiating both sides of equation (1) with respect to x, we get 

or 

$$\begin{aligned}\frac{dy}{dx}&=e^{ax}-bc_{1}\sin bx\quad bc_{2}\cos bx\quad c_{1}\cos bx\quad c_{2}\sin bx e^{ax}\quad a\\frac{dy}{dx}&=e^{ax}[(bc_{2}+ac_{1})\cos bx+(ac_{2}-bc_{1})\sin bx]\end{aligned}$$

Differentiating both sides of equation (2) with respect to x, we get 

$$\begin{aligned}\frac{d^{2}y}{dx^{2}}=&e^{ax}\left[\left(bc_{2}\quad ac_{1}\right)\left(\quad b\sin bx\right)\quad\left(ac_{2}\quad bc_{1}\right)\left(b\cos bx\right)\right]\\&+\left[\left(bc_{2}+ac_{1}\right)\cos bx+\left(ac_{2}-bc_{1}\right)\sin bx\right]e^{ax}.a\\=&e^{ax}\left[\left(a^{2}c_{2}-2abc_{1}-b^{2}c_{2}\right)\sin bx+\left(a^{2}c_{1}+2abc_{2}-b^{2}c_{1}\right)\cos bx\right]\end{aligned}$$

Substituting the values of $\frac{d^{2}y}{dx^{2}},\frac{dy}{dx}$ and y in the given differential equation, we get 

$$\begin{aligned}L.H.S.=&e^{ax}[a^{2}c_{2}-2abc_{1}-b^{2}c_{2}\sin bx+(a^{2}c_{1}+2abc_{2}-b^{2}c_{1})\cos bx]\\&2ae^{ax}[(bc_{2}\quad ac_{1})\cos bx\quad(ac_{2}\quad bc_{1})\sin bx]\\&(a^{2}\quad b^{2})e^{ax}[c_{1}\cos bx\quad c_{2}\sin bx]\\=&e^{ax}\left[\left(a^{2}c_{2}-2abc_{1}-b^{2}c_{2}-2a^{2}c_{2}+2abc_{1}+a^{2}c_{2}+b^{2}c_{2}\right)\sin bx\right.\\&\left.+(a^{2}c_{1}+2abc_{2}-b^{2}c_{1}-2abc_{2}-2a^{2}c_{1}+a^{2}c_{1}+b^{2}c_{1})\cos bx\right]\end{aligned}e^{ax}[0\times\sin bx+0\cos bx]=e^{ax}\times0=0$$

Hence, the given function is a solution of the given differential equation.

Example 25 Form the differential equation of the family of circles in the second quadrant and touching the coordinate axes.



Solution Let C denote the family of circles in the second quadrant and touching the coordinate axes. Let $(-a,a)$ be the coordinate of the centre of any member of this family (see Fig 9.6).



Equation representing the family C is 

or 

$$\begin{align*}(x+a)^{2}+(y-a)^{2}&=a^{2}\\x^{2}+y^{2}+2ax-2ay+a^{2}&=0\end{align*}$$

Differentiainquation (2)with pctto , we et 

$$2x+2y\frac{dy}{dx}+2a-2a\frac{dy}{dx}=0$$

or 

$$x+y\frac{dy}{dx}=a\left(\frac{dy}{dx}-1\right)$$

or 

$$a=\frac{x+y y^{\prime}}{y^{\prime}-1}$$

<div style="text-align: center;"><img src="imgs/img_in_image_box_602_203_909_493.jpg" alt="Image" width="30%" /></div>


<div style="text-align: center;">9.6</div>


Substituting the value of a in equation (1), we get 

or 

or 

or 

$$\begin{aligned}&\left[x+\frac{x+y y^{\prime}}{y^{\prime}-1}\right]^{2}+\left[y-\frac{x+y y^{\prime}}{y^{\prime}-1}\right]^{2}=\left[\frac{x+y y^{\prime}}{y^{\prime}-1}\right]^{2}\\ &\left[x y^{\prime}-x+x+y y^{\prime}\right]^{2}+\left[y y^{\prime}-y-x-y y^{\prime}\right]^{2}=\left[x+y y^{\prime}\right]^{2}\\ &\left(x+y\right)^{2}y^{\prime2}+\left[x+y\right]^{2}=\left[x+y y^{\prime}\right]^{2}\\ &\left(x+y\right)^{2}\left[(y^{\prime})^{2}+1\right]=\left[x+y y^{\prime}\right]^{2}\\ \end{aligned}$$

which istheluatioptigtiv mlyofrl.

Example 26 Find the particular solution of the difrential equation $\log\left(\frac{dy}{dx}\right)=3x+4y$ given that $y=0when x=0$ 



Solution The given differential equation can be written as 

or 

$$\begin{aligned}\frac{dy}{dx}&=e^{(3x+4y)},\\frac{dy}{dx}&=e^{3x}.e^{4y}\end{aligned}$$

Separating the variables, we get 

$$\frac{dy}{e^{4y}}=e^{3x}dx $$

Therefore 

$$\int e^{-4y}dy=\int e^{3x}dx $$

or 

$$\frac{e^{-4y}}{-4}=\frac{e^{3x}}{3}+C $$

or 

$$4e^{3x}+3e^{-4y}+12C=0$$

Substituting $x=0$ and,$y=0$ in (2), we get 

$4+3+12C=0\ or\ C=\frac{-7}{12}$ 

$$4+3+12C=0\ or\ C=\frac{-7}{12}$$

Substituting the value ofCin equation (2), we get 

$$4e^{3x}+3e^{-4y}-7=0$$

uation.

Example 27 Solve the differential equation 

$$(x dy-y dx)y\sin\left(\frac{y}{x}\right)=(y dx+x dy)x\cos\left(\frac{y}{x}\right).$$

as 

$$\left[x y\sin\left(\frac{y}{x}\right)-x^2\cos\left(\frac{y}{x}\right)\right]dy=\left[x y\cos\left(\frac{y}{x}\right)+y^2\sin\left(\frac{y}{x}\right)\right]dx $$

or 

$$\frac{dy}{dx}=\frac{xy\cos\left(\frac{y}{x}\right)+y^{2}\sin\left(\frac{y}{x}\right)}{xy\sin\left(\frac{y}{x}\right)-x^{2}\cos\left(\frac{y}{x}\right)}$$

Dividing numerator and denominator on RHS by $x^{2}$ , we get 

$$\frac{dy}{dx}=\frac{\frac{y}{x}\cos\left(\frac{y}{x}\right)+\left(\frac{y^{2}}{x^{2}}\right)\sin\left(\frac{y}{x}\right)}{\frac{y}{x}\sin\left(\frac{y}{x}\right)-\cos\left(\frac{y}{x}\right)}$$

Cearly,rm $\frac{dy}{dx}=g\left(\frac{y}{x}\right)$ To solve it, we make the substitution . (2

$$\left\{\begin{aligned}y&=vx\\ \frac{dy}{dx}&=y+x\frac{dv}{dx}\end{aligned}\right.}$$

or 

$$\int v+x\frac{dv}{dx}=\frac{v\cos v+v^2\sin v}{v\sin v-\cos v}$$

or 

$$x\frac{dv}{dx}=\frac{2v\cos v}{v\sin v-\cos v}$$

or 

$$\left(\frac{v\sin v-\cos v}{v\cos v}\right)dv=\frac{2dx}{x}$$

Therefore 

$$\int\left(\frac{v\sin v-\cos v}{v\cos v}\right)dv=2\int\frac{1}{x}dx $$

or 

$$\int\tan v dv-\int\frac{1}{y}dv=2\int\frac{1}{x}dx $$

or 

$$\log\left|\sec v\right|-\log\left|v\right|=2\log\left|x\right|+\log\left|C_{1}\right|$$

or 

$$\log\left|\frac{\sec v}{v x^{2}}\right|=\log\left|C_{1}\right|$$

or 

$$\frac{\sec v}{v x^{2}}=\pm\mathrm{C}_{1}$$

Replacing v by $\frac{y}{x}$ in equation (3)we get ,

$$\frac{\sec\left(\frac{y}{x}\right)}{\left(\frac{y}{x}\right)(x^2)}=C where,C=\pm C_1$$

or 

$$\sec\left(\frac{y}{x}\right)=C x y $$

which is the general solution of the given differential equation.

Example 28 Solve the differential equation 

$$\left(\tan^{-1}y-x\right)dy=\left(1+y^{2}\right)dx.$$

Solution The given differential equation can be written as 

$$\frac{dx}{dy}+\frac{x}{1+y^{2}}=\frac{\tan^{-1}y}{1+y^{2}}$$

Now (1) is a linear differential equation of the form $\frac{dx}{dy}+P_{1}x=Q_{1}$ 

where,$\mathrm{P}_{1}=\frac{1}{1+y^{2}}\text{and}\mathrm{Q}_{1}=\frac{\tan^{-1}y}{1+y^{2}}$ 

Therefore,$\mathrm{I}.\mathrm{F}=e^{\int\frac{1}{1+y^{2}}dy}=e^{\tan^{-1}y}$ 

on is 

$$x e^{\tan^{-1}y}=\int\left(\frac{\tan^{-1}y}{1+y^2}\right)e^{\tan^{-1}y}dy+C $$

Let 

$$\mathrm{I}=\int\left(\frac{\tan^{-1}y}{1+y^2}\right)e^{\tan^{-1}y}dy $$

Substituting tan-1$y=t$ so that $\left(\frac{1}{1+y^{2}}\right)dy=dt$ ,, we get we get 

or 

$$\begin{aligned}&\mathrm{I}=\int t e^{t}d t=t e^{t}-\int1.e^{t}d t=t e^{t}-e^{t}=e^{t}(t-1)\\ &\mathrm{I}=e^{\tan^{-1}y}(\tan^{-1}y-1)\\ \end{aligned}$$

Substituting the value of I in equation (2), we get 

or 

$$x\cdot e^{\tan^{-1}y}=e^{\tan^{-1}y}\left(\tan^{-1}y-1\right)+C $$

which is the general solution of the given differential equation.

## Miscellaneous Exercise on Chapter 9

For each of the differential equations given below, indicate its order and degree (if defined).



$$\frac{d^{2}y}{dx^{2}}+5x\left(\frac{dy}{dx}\right)^{2}-6y=\log x\quad\left(ii\right)\left(\frac{dy}{dx}\right)^{3}-4\left(\frac{dy}{dx}\right)^{2}+7y=\sin x $$

2.For acoftxlw,itteiuctiimlicit r explicit) is a solution of the corresponding differential equation.

(i)

$$(i)y=a e^{x}+b e^{-x}+x^{2}\quad:\quad x\frac{d^{2}y}{d x^{2}}+2\frac{dy}{dx}-x y+x^{2}-2=0$$

(ii)

$$y=e^{x}\left(a\cos x+b\sin x\right)\quad:\quad\frac{d^{2}y}{d x^{2}}-2\frac{dy}{dx}+2y=0$$

(ii))

$$(ii)y=x\sin3x \frac{d^{2}y}{dx^{2}}+9y-6\cos3x=0\mathrm{iv}\quad x^{2}=2y^{2}\log y\quad:\quad(x^{2}+y^{2})\frac{dy}{dx}-x y=0$$

3. Form the differential equation representing the family of curves given by $(x-a)^{2}+2y^{2}=a^{2}$ , where a is an arbitrary constant.



4. Prove that $x^{2}-y^{2}=c\left(x^{2}+y^{2}\right)^{2}$ is the general solution of differential equation $(x^{3}-3x y^{2})dx=(y^{3}-3x^{2}y)$ dy, where c is a parameter.

5.Form therenial quatio otheamilyoicle ite fst uadant which touch the coordinate axes.



6. Find the general solution of the differential equation $\frac{dy}{dx}+\sqrt{\frac{1-y^{2}}{1-x^{2}}}=0$ 

7.Showtel oeialequation $\frac{dy}{dx}+\frac{y^{2}+y+1}{x^{2}+x+1}=0$ is given by $(x+y+1)=\mathrm{A}(1-x-y-2xy)$ , where A is parameter.

Find the etin of te curve sig thuh the point $\left(0,\frac{\pi}{4}\right)$ whose differential equation is sin x cos y $dx+\cos x\sin y dy=0$ 



9.Find the particular solution of the differential equation 

$\left(1+e^{2x}\right)d y+\left(1+y^{2}\right)e^{x}d x=0$ , given that.$y=1when x=0$ 

10. Solve the differential equation $y e^{\frac{x}{y}}d x=\left(x e^{\frac{x}{y}}+y^{2}\right)d y(y\neq0)$ 

11. Find a particular solution of the differential equation $(x-y)(dx+dy)=dx-dy$ given that $y=-1$ , when $x=0.(\mathrm{Hint}:\mathrm{put}x-y=t)$ 



12. Solve the differential equation $\left[\left[\frac{e^{-2\sqrt{x}}}{\sqrt{x}}-\frac{y}{\sqrt{x}}\right]\frac{dx}{dy}=1(x\neq0)\right]$ 

13. Find a particular solution of the differential equation $\frac{dy}{dx}+y\cot x=4x$ cosec x $(x\neq0)$ J, given that $y=0when x=\frac{\pi}{2}$ 



1.Fid tiulaoluiooftetil uion $(x+1)\frac{dy}{dx}=2e^{-y}-1$ given that_$y=0when x=0$ 



15.The population of a village increases continuously at the rate proportional to the number of its inhabitants present at any time. If the population of the village was 20,000 in 1999 and 25000 in the year 2004, what will be the population of the village in 2009?



16. The general solution of the differential equation $\frac{\sqrt{y}dx-x\ dy}{y}=0$ is 

(A)$xy=\mathbf{C}$ (B)$x=\mathrm{C}y^{2}$ $y=\mathrm{C}x$ (D)$y=C x^{2}$ 

17. The general solution of a differential equation of the type $\frac{dx}{dy}+P_{1}x=Q_{1}$ is 

(A)

$$y e^{\int P_{1}dy}=\int\left(Q_{1}e^{\int P_{1}dy}\right)dy+C $$

(B)

$$y\cdot e^{\int P_{1}dx}=\int\left(Q_{1}e^{\int P_{1}dx}\right)dx+C $$

(C)

$$x e^{\int P_{1}dy}=\int\left(Q_{1}e^{\int P_{1}dy}\right)dy+C $$

(D)

$$x e^{\int P_{1}dx}=\int\left(Q_{1}e^{\int P_{1}dx}\right)dx+C $$

18.The general solution of the differential equation $e^{x}dy+(ye^{x}+2x)dx=0$ is 

(A)

$$x e^{y}+x^{2}=C $$

(B)

$$x e^{y}+y^{2}=\mathbf{C}$$

(C) .

$$(C) .y e^{x}+x^{2}=\mathbf{C}$$

(D) .

$$(D) .y e^{y}+x^{2}=C $$

## Summary 

■An equation involving derivatives of the dependent variable with respect to independent variable (variables) is known as a differential equation.

■Order of a differential equation is the order of the highest order derivative occurring in the differential equation.



■Degree ofreilquionideediinomialuationin its derivatives.



■Degree(weded)oifiluaion is iest wrositive integer only) of the highest order derivative in it.

■The solution which contains as many arbitrary constants as the order of the differential equation is called a general solution and the solution free from arbitrary constants is called particular solution.



■To form a differential equation from a given functionwe differentiate the function successively as many timesastumerofataryconstnts in the given function and then eliminate the arbitrary constants.

■Variable separable method is used to solve such an equation in which variables can be separated completely i.e. terms containing y should remain with dy and terms containing x should remain with dx.



■A differential equation which can be expressed in the form $\frac{dy}{dx}\quad f(x,y)\quad or\quad\frac{dx}{dy}\quad g(x,y)where,f(x,y)$ and $g(x,y)$ are homogenous functions of degree zero is called a homogeneous differential equation.

A differential equation of the form ${\frac{dy}{dx}}^{+}\mathtt{P}y$ Q, wherePandQare constants or functionsofxonlyiscalledairstorderlineardifrntialequation.

## Historical Note 

One of the principal languages of Science is that of differential equations.Interestingly, the date of birth of differential equations is taken to be November,11,1675, when Gottfried Wilthelm Freiherr Leibnitz(1646 - 1716) first put in black and white the identity $\int y dy=\frac{1}{2}y^2$ , thereby introducing both the symbols∫and dy. Leibnitulliboetents were prei.s lditodovedoparaiofariables'1691.A year later he formulated themethod of solving the homogeneous differential equations of the first order'. He went further in a very short time to the discovery of themethod of solving a linear differential equation of the first-order'. How surprising is it that all these methodscamefroma singleman and that too within 25 years of the birth of differential equations!

In the old days, what we now call the 'solution'of a differential equation,was used to be referred to as integral'of the differential equation, the word being coined by James Bernoulli (16541705)in 1690. The word solution was first used by Joseph Louis Lagrange (17361813)in 1774,which was almost hundred years since the birth of differential equations. It was Jules Henri Poincare (1854-1912)who strongly advocated the use of the word solution' and thus the word 'solution' has found its deserved place in modern terminology.The name of themethod of separation of variables'is due to John Bernoulli (1667- 1748),a younger brother of James Bernoulli.



Application to geometric problems were also considered. It was again John Bernoulliwh s o light the intricate nature of differential equations.In a letter to Leibnitz,dated May 20,1715,he revealed the solutions of the differential equation 



$$x^{2}y^{\prime\prime}=2y,$$

which led to three types of curves, viz.,parabolas,hyperbolas and aclassof cubic curves.This shows how varied the solutions of such innocent looking differenloo has been differential equations,under the heading qualitative analysis s of differential equations'. Now-a-days,this has acquired prime importance being absolutely necessary in almost all investigations.

