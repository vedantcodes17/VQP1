

# INTEGRALS

...Just as a mountainer climbs amountain –because it isthere,so a good mathematics student studies new material because it is there. —JAMES B. BRISTOL ...

### 7.1 Introduction

Differential Calculus is centred on the concept of the derivative. The original motivation for the derivative was the problem of defining tangent lines to the graphs of functions and calculating the slope of such lines. Integral Calculus is motivated by the problem of defining and calculating the area of the region bounded by the graph of the functions.

If a functionf is differentiable in an interval I, i.e, its derivativef exists at each point of I, then a natural question arises that given f 'at each point of I, can we determine the function? The functions that could possibly have given function as a derivative are called anti derivatives (or primitive) of the function. Further, the formula that gives

<div style="text-align: center;"><img src="imgs/img_in_image_box_760_752_1032_1073.jpg" alt="Image" width="22%" /></div>

<div style="text-align: center;">G .W. Leibnitz (1646 -1716)</div>

all these anti derivatives is called the indefinite integral of the function and such process of finding anti derivatives is called integration.Such type of problems arise in many practical situations. For instance, if we know the instantaneous velocity of an object at any instant, then there arises a natural question, i.e., can we determine the position of the object at any instant? There are several such practical and theoretical situations where the process of integration is involved. The development of integral calculus arises out of the efforts of solving the problems of the following types:

(a) the problem of finding a function whenever its derivative is given,

(b) the problem of finding the area bounded by the graph of a function under certain conditions.

These two problems lead to the two forms of the integrals, e.g., indefinite and definite integrals, which together constitute the Integral Calculus.

## MATHEMATICS

There is a connection, known as the Fundamental Theorem of Calculus, between ie olor .eting problems from various disciplines like economics, finance and probability.

In this Chapter, we shall confine ourselves to the study of indefinite and definite integrals and their elementary properties including some techniques of integration.

### 7.2 Integration as an Inverse Process of Differentiation

IntegraIf ion,we areof iinal function. Such a process is called integration or anti differentiation.

Let us consider the following examples:

We know that

$$\left[{\frac{d}{d x}}(\sin x)=\cos x\right]

$$

$$

\frac{d}{d x}(\frac{x^{3}}{3})=x^{2}

$$

and

$$

\frac{d}{dx}(e^{x})=e^{x}

$$

Weobservehatin1),huctiistheiveducioof iWy that i o l,i)n $(3),\frac{x^{3}}{3}$ and $e^{x}$ e)$x^{2}$ and $e^{x}$ , espectiv.for any real number C,treated a constant function, its derivative is ero and hence, we can write (1), (2) and (3) as follows :

$$

\left[\frac{d}{dx}\left(\sin x+C\right)=\cos x,\frac{d}{dx}\left(\frac{x^3}{3}+C\right)=x^2\mathrm{and}\frac{d}{dx}\left(e^x+C\right)=e^x\right]Thus, anti derivatives (or integrals) of the above cited functions are not unique.

$$

Thus, anti derivatives (or integrals) of the above cited functions are not unique.Actually, there exist infinitely many anti derivatives of each of these functions which can be obtained by choosing C arbitrarily from the set of real numbers. For this reason C is customarily referred to as arbitrary constant. In fact, C is the parameter by varying which one gets different anti derivatives (or integrals) of the given function.More generally, if there is a function F such that ${\frac{d}{d x}}\mathrm{F}\left(x\right)=f\left(x\right),\forall x\in\mathrm{I}\left(\mathrm{i n t e r v a l}\right)$ then for any arbitrary real number C, (also called constant of integration)

$$

{\frac{d}{d x}}{\bigl[}\operatorname{F}\left(x\right)+\operatorname{C}{\bigr]}=f(x),x\in\operatorname{I}

$$

Thus,

$\{\mathrm{F}+\mathrm{C},\mathrm{C}\in\mathbb{R}\}$ denotes a family of anti derivatives of f

Remark Functions with same derivatives differ by a constant. To show this, let $g$ and h be two functions having the same derivatives on an interval I.

Consider the function $f=g-h$ defined by.$f(x)=g(x)-h\left(x\right)$ $\forall x\in I$

Then

$$

{\frac{d f}{d x}}=f^{\prime}=g^{\prime}-h^{\prime}{\mathrm{g i v i n g}}\quad f^{\prime}(x)=g^{\prime}(x)-h^{\prime}(x)\quad\forall\quad x\in\mathrm{~I~}

$$

or

$$

f^{\prime}(x)=0,\forall x\in\mathrm{I}\;\mathrm{b y}\;\mathrm{h y p o t h e s i s},

$$

i.e., the rate of change of f with respect to x is zero on I and hence f is constant.

In view of the above remark, it is justified to infer that the family $\{\operatorname{F}+\operatorname{C},\operatorname{C}\in\operatorname{\mathbb{R}}\}$ |provides all possible anti derivatives off.

We introduce a new symbol, namely,$\int f(x)$ dx which will represent the entire class of anti derivatives read as the indefinite integral of f with respect to .

Symbolically, we write $\int f(x)d x=\operatorname{F}(x)+\mathbf{C}$

Notation Given that $\frac{dy}{dx}=f\left(x\right),\mathrm{we write}y=\int f\left(x\right)dx$

For the sake of convenience, we mention below the following symbols/terms/phrases with their meanings as given in the Table (7.1).

<div style="text-align: center;">Table 7.1</div>

<div style="text-align: center;"><html><body><table border="1"><tr><td>Symbols/Terms/Phrases</td><td>Meaning</td></tr><tr><td>$\int f(x)d x$</td><td>Integral off with respect to x</td></tr><tr><td>in $\int f(x)d x$ $f(x)$</td><td>Integrand</td></tr><tr><td>x in $\int f(x)d x$</td><td>Variable of integration</td></tr><tr><td>Integrate</td><td>Find the integral</td></tr><tr><td>An integral of f</td><td>A function F such that $\operatorname{F}^{\prime}(x)=f\left(x\right)$</td></tr><tr><td>Integration</td><td>The process of finding the integral</td></tr><tr><td>Constant of Integration</td><td>Any real number C, considered as constant function</td></tr></table></body></html></div>

## MATHEMATICS

We already know the formulae for the derivatives of many important functions.From these formulae, we can write down immediately the corresponding formulae (referred to a standard formula) for the integrals of these functions, a listed below which will be used to find integrals of other functions.

Derivatives

Integrals (Anti derivatives)

$$

\begin{aligned}&(i)\quad\frac{d}{dx}\big(\frac{x^{n+1}}{n+1}\big)=x^n;\quad&\int x^n dx=\frac{x^{n+1}}{n+1}+C,n\neq-1\\&\quad\int\frac{d}{x}\big(x\big)=1;\quad&\int dx=x+C\\&\quad\int\frac{d}{dx}\big(x\big)=1;\quad&\int\cos x dx=\sin x+C\\&\quad\int\frac{d}{dx}\big(\sin x\big)=\cos x;\quad&\int\cos x dx=\sin x+C\\&\quad\int\left(\mathrm{ii}\right)\quad\frac{d}{dx}\big(-\cos x\big)=\sin x;\quad&\int\sin x dx=-\cos x+C\\&\quad\int\left(\mathrm{iv}\right)\quad\frac{d}{dx}\big(\tan x\big)=\sec^2x;\quad&\int\sec^2x dx=\tan x+C\\&\quad\int\left(\mathrm{iv}\right)\quad\frac{d}{dx}\big(-\cot x\big)=\sec^2x;\quad&\int\cos^{\infty}x dx=-\cot x+C\\&\quad\int\left(\mathrm{vi}\right)\quad\frac{d}{dx}\big(\sec x\big)=\sec x\tan x;\quad&\int\sec x\tan x dx=\sec x+C\\&\quad\int\left(\mathrm{vi}\right)\quad\frac{d}{dx}\big(-\cos\csc x\big)=\csc x\cot x;\quad&\int\cos x\cot x dx=-\cos\csc x+C\\&\quad\int\left(\mathrm{vi}\right)\quad\frac{d}{dx}\big(\sin^{-1}x\big)=\frac{1}{\sqrt{1-x^2}};\quad&\int\frac{dx}{\sqrt{1-x^2}}=-\cos^{-1}x+C\\&\quad\int\frac{dx}{\sqrt{1-x^2}}=-\csc^{-1}x+C\\&\quad\int\frac{dx}{dx}\big(\tan^{-1}x\big)=\frac{1}{\sqrt{1-x^2}};\quad&\int\frac{dx}{\sqrt{1-x^2}}=\tan^{-1}x+C\\&\quad\int\frac{dx}{dx}\big(\tan^{-1}x\big)=\frac{1}{1+x^2};\quad&\int\frac{dx}{1+x^2}=\tan^{-1}x+C\\&\quad\int\frac{dx}{dx}\big(-\cot^{-1}x\big)=\frac{1}{1+x^2};\quad&\int\frac{dx}{1+x^2}=-\cot^{-1}x+C\end{aligned}

$$

$$

{\begin{array}{r l r l}&{{\left({\mathrm{x i i}}\right)}^{\mathrm{~\scriptsize~\cdot~}}{\cfrac{d}{d x}}{\left({\sec^{-1}x}\right)}={\frac{1}{x{\sqrt{x^{2}-1}}}}\quad;}&&{{\int}{\cfrac{d x}{x{\sqrt{x^{2}-1}}}}={\sec^{-1}x}+\mathbf{C}}\\ &{{\left({\mathrm{x i i i}}\right)}^{\mathrm{~\scriptsize~\cdot~}}{\cfrac{d}{d x}}{\left(-{\cos^{-1}x}\right)}={\frac{1}{x{\sqrt{x^{2}-1}}}}\quad;}&&{{\int}{\cfrac{d x}{x{\sqrt{x^{2}-1}}}}=-{\cos^{-1}x}+\mathbf{C}}\\ &{{\left({\mathrm{x i v}}\right)}^{\mathrm{~\scriptsize~\cdot~}}{\cfrac{d}{d x}}{\left(e^{x}\right)}={e^{x}}\quad;}&&{{\int}e^{x}d x=e^{x}+\mathbf{C}}\\ &{{\left({\mathrm{x v}}\right)}^{\mathrm{~\scriptsize~\cdot~}}{\cfrac{d}{d x}}{\left(\log|x|\right)}={\frac{1}{x}};}&&{{\int}{\cfrac{1}{x}}d x=\log|x|+\mathbf{C}}\\ &{{\left({\mathrm{x v i}}\right)}^{\mathrm{~\scriptsize~\cdot~}}{\cfrac{d}{d x}}{\left({\cfrac{a^{x}}{\log a}}\right)}={a^{x}}\quad;}&&{{\int}a^{x}d x={\cfrac{a^{x}}{\log a}}+\mathbf{C}}\end{array}}

$$

N,llous functions are defined. However, in any specific problem one has to keep it in mind.

#### 7.2.1 Geometrical interpretation of indefinite integral

Let $f(x)=2x$ . Then $\int f(x)dx=x^2+C$ . For different values of C, we get different integrals. But these integrals are very similar geometrically.

Thus,.$y=x^{2}+C$ , where C is arbitrary constant, represents a family of integrals. By assigning different values to C, we get diferent members of the family. These together constitute the indefinite integral. In this case, each integral represents a parabola with its axis along y-axis.

Clearly, for $\mathbf{C}=0$ , we obtain $y=x^{2}$ ,a parabola with its vertex on the origin. The curve $y=x^{2}+1$ for $C=1$ is obtained by shifting the parabola $y=x^{2}$ one unit along y-axis in positive direction. For $C=-1,y=x^{2}-1$ is obtained by shifting the parabola $y=x^{2}$ one unit along y-axis in the negative direction. Thus, for each positive value of C,each parabola of the family has its vertex on the positive side of the y-axis and for negative values of C, each has its vertex along the negative side of the y-axis. Some of these have been shown in the Fig 7.1.

Let us consider the intersection of all these parabolas by a line $x=a$ . In the Fig 7.1,we have taken $a>0$ . The same is true when $a<0$ . If the line $x=a$ intersects the parabolas $y=x^{2},\;y=x^{2}+1,\;y=x^{2}+2,\;y=x^{2}-1,\;y=x^{2}-2at\mathrm{P}_{0},\;\mathrm{P}_{1},\;\mathrm{P}_{2},\;\mathrm{P}_{-1},\;\mathrm{P}_{-2}$ etc.,respectively, then $\frac{dy}{dx}$ at these points equals 2a. This indicates that the tangents to the curves at these points are parallel. Thus,$\int2x dx=x^2+C=\mathrm{F}_{\mathrm{C}}(x)(\mathrm{say})$ 1, implies that $$

y=x^{2}+3

$$

$$

y=x^{2}+2

$$

<div style="text-align: center;">Fig 7.1</div>

the tangents to all the curves $y=\operatorname{F}_{\mathbb{C}}{(x)},\mathbb{C}\in\mathbb{R}$ , at the points of intersection of the curves by the line $x=a,(a\in\mathbb{R})$ ),are parallel.

Further, the following equation (statement)$\int f\left(x\right)dx=\mathrm{F}\left(x\right)+\mathrm{C}=y\left(\mathrm{say}\right)$ represents a family of curves. The different values of C will correspond to different members of this family and these members can be obtained by shifting any one of the curves parallel to itself.This is the geometrical interpretation of indefinite integral.

#### 7.2.2 Some propertiesof indefinite integral

In this sub section, we shall derive some properties of indefinite integrals.

(I) The process of differentiation and integration are inverses of each other in the sense of the following results :

$$

\int{\frac{d}{d x}}{\int{f(x)d x}}=f(x)

$$

and

$\int f^{\prime}(x)d x=f(x)+\mathbf{C},$ , where C is any arbitrary constant.

Proof Let F be any anti derivative of f, i.e.,

Then

Therefore

$$

{\begin{array}{r l}&{\quad{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\boldmath~\int~}}\int_{\mathrm{~\mathrm{\boldmath~\int~}}}\int_{\mathrm{\mathrm{~\boldmath~\int~}}}\int_{\mathrm{\mathrm{~\boldmath~\int~}}}\int_{\mathrm{\mathrm{~\boldmath~\int~}}}\int_{\mathrm{\mathrm{~\boldmath~\int~}}}\int_{\mathrm{\mathrm{~\boldmath~\int~}}}\int_{\mathrm{\mathrm{~\boldmath~\int}}}\int_{\mathrm{\mathrm{~\boldmath~\int}}}\int_{\mathrm{\mathrm{~\boldmath~\int}}}_{\mathrm{\mathrm{\boldmath~\int~}}}\int_{\mathrm{\mathrm{\boldmath~\int}}}_{\mathrm{\mathrm{\mathrm~{~\boldmath\int~~\int}}}}_{\mathrm{\mathrm{\mathrm{~~\int~\int}}}_{\mathrm{\mathrm{\int~\int}}}_{\mathrm{\mathrm{\mathrm{~~\int~\int}}}}_{\mathrm{\mathrm{\mathrm{~~\int~\int}}}}_{\mathrm{\mathrm{\mathrm{~~\int~\int}}}}_{\mathrm{\mathrm{\mathrm{\int~~\int~}}}_{\mathrm{\mathrm{\mathrm~~\int}{\int}}}_{\mathrm{\mathrm{\mathrm~~\int}}{\mathrm{\int~~\int}}}_{\mathrm{\mathrm{\mathrm{~\int~~\int}}}}_{\mathrm{\mathrm{\mathrm{\int~~\int}}}}_{\mathrm{\mathrm{\mathrm{\int~\int}}}_{\mathrm{\mathrm{\mathrm{~\int~}}\mathrm{}}}_{\mathrm{\mathrm{\int\mathrm}{\int}}_{\mathrm{\mathrm{\int\mathrm}}{\mathrm}{}}_{\mathrm{\mathrm{\int\int}}}_{\mathrm{\mathrm{\mathrm}{\int}}}_{\mathrm{\mathrm{\mathrm\int}{}}_{\mathrm{\mathrm{\int\int}\mathrm}{\mathrm}{}}_{\mathrm{\mathrm}{\mathrm}{}_{\mathrm{\int\mathrm}}{}_{\mathrm\mathrm{}{\int}}_{\mathrm\mathrm{}{\mathrm}}{d}_{\mathrm{d\mathrm}}{d}_{\mathrm{d\mathrm}}_{{}}_{\mathrm{\mathrm\mathrm{d}}}_{\mathrm{\mathrm}{d}}_{}_{\mathrm\mathrm{}{d}_{\mathrm}}{_{\mathrm}{\mathrm}}_{\mathrm{\mathrm\mathrm}{}}_{}_{\mathrm\mathrm{\mathrm}{\mathrm}{}\mathrm}_{\mathrm}{}_{\mathrm\mathrm}{\mathrm}\mathrm{\mathrm}{\mathrm}_{\mathrm}\mathrm{\mathrm}{}_\mathrm{

$$

Similarly, we note that

$$

f^{\prime}(x)={\frac{d}{d x}}f(x)

$$

and hence

$$

\int f^{\prime}\left(x\right)d x=f(x)+\mathbf{C}

$$

where C is arbitrary constant called constant of integration.

(II) Two indefiniteintegrals with the same derivative lead to the same family of curves and so they are equivalent.

Proof Let f and g be two functions such that

$$

\int\frac{d}{d x}\int f(x)d x=\int\frac{d}{d x}\int g(x)d x.

$$

or

$$

\left[{\frac{d}{d x}}\Big[\int f(x)d x-\int g(x)d x\Big]=0\right]

$$

Hence $\int f(x)d x-\int g(x)d x=\mathrm{~C~}$ , where C is any real number (Why?)

or

$$

\int f(x)dx=\int g(x)dx+C 

$$

So the families of curves $\left\{\int f(x)dx+C_1,C_1\in\mathbb{R}\right\}$

and

$$

\left\{\left\{\int g(x)d x+\mathbb{C}_{2},\mathbb{C}_{2}\in\mathbb{R}\right\}\mathrm{a r e i d e n t i c a l}.\right.}

$$

Hence, in this sense,$\int f(x)d x\mathrm{a n d}\int g(x)d x$ :are equivalent.

 Note]The equivalence of the families $\left\{\int f(x)dx+C_1,C_1\in\mathbf{R}\right\}$ and $\left\{\int g(x)dx+C_2,C_2\in\mathbf{R}\right\}$ is customarily expressed by writing $\int f\left(x\right)d x=\int g\left(x\right)d x$ without mentioning the parameter.

(III)

$$

\left[\int\left[f(x)+g(x)\right]dx=\int f(x)dx+\int g(x)dx\right]

$$

Proof By Property (I), we have

$$

{\frac{d}{d x}}{\left[\int\left[f(x)+g\left(x\right)\right]d x\right]}=f(x)+g\left(x\right)

$$

On the otherhand, we find that

$$

\begin{aligned}\left\{\frac{d}{dx}\left[\int f(x)dx+\int g(x)dx\right]\right.&=\left.\frac{d}{dx}\int f(x)dx+\frac{d}{dx}\int g(x)dx\right.\\&=f(x)+g(x)\end{aligned}}

$$

Thus, in view of Property (II), it follows by (1) and (2) that

$$

\int\left(f\left(x\right)+g\left(x\right)\right)d x=\int f\left(x\right)d x+\int g\left(x\right)d x.

$$

(IV) For any real number ,$\int k f(x)dx=k\int f(x)dx$

Proof By the Property (I),${\frac{d}{d x}}\int k~f(x)d x=k~f(x)\;.$

Also

$$

\left[{\frac{d}{d x}}{\Big[}k\int f(x)d x{\Big]}=k{\frac{d}{d x}}\int f(x)d x=k f(x)\right]

$$

Therefore, using the Property (II), we have $\int k\;f(x)d x=k\int f(x)d x$

(V) Properties (III) and (IV) can be generalised to a finite number of functions $f_{1},f_{2},...,f_{n}$ and the real numbers,$k_{1},k_{2},...,k_{n}$ giving

$$

\begin{align*}\begin{cases}\displaystyle\int\left[k_1f_1\left(x\right)+k_2f_2\left(x\right)+\ldots+k_n f_n\left(x\right)\right]dx\\=\overset{\cdot}{k}\underset{1}{\int}f_1\left(x\right)dx+k_2\underset{2}{\int}f_2\left(x\right)dx+\ldots+k_n\underset{n}{\int}f_n\left(x\right)dx.\end{cases}\end{align*}

$$

To find an anti derivative of a given function, we search intuitively for a function whose ii. u inding an anti derivativeis known asintegationby the methodofinspection.Weillustrate it through some examples.

Example1 Write an anti derivative for eachof the following functions using the method of inspection:

(i)$\cos2x$

(ii)

$$

3x^{2}+4x^{3}

$$

(ii)

$$

\frac{1}{x},x\neq0

$$

Solution

(i) We look for a function whose derivative is cos 2x. Recall that

$$

\left\{{\frac{d}{d x}}\sin2x=2\cos2x\right\}

$$

or

$$

\cos2x=\frac{1}{2}\frac{d}{dx}\left(\sin2x\right)=\frac{d}{dx}\left(\frac{1}{2}\sin2x\right)

$$

Therefore, an anti derivative of cos 2x is $\frac{1}{2}\sin2x$

(ii) We look for a function whose derivative is $3x^{2}+4x^{3}$ . Note that

$$

\left[{\frac{d}{d x}}\left(x^{3}+x^{4}\right)=3x^{2}+4x^{3}\right]

$$

Therefore, an anti derivative of $3x^{2}+4x^{3}\ is\ x^{3}+x^{4}$

(i) We know that

$$

\frac{d}{dx}\left(\log x\right)=\frac{1}{x},x>0and\frac{d}{dx}\left\lbrack\log\left(-x\right)\right\rbrack=\frac{1}{-x}\left(-1\right)=\frac{1}{x},x<0

$$

Combining above, we get $\frac{d}{dx}\left(\log|x|\right)=\frac{1}{x},x\neq0$

Therefore,$\int\frac{1}{x}dx=\log|x|$ is one of the anti derivatives of $\frac{1}{x}$

Example 2 Find the following integrals:

$$

(\mathrm{i})\quad\int\frac{x^{3}-1}{x^{2}}d x\quad(\mathrm{i i})\quad\int(x^{\frac{2}{3}}+1)d x\quad(\mathrm{i i i})\quad\int(x^{\frac{3}{2}}+2\quad e^{x}\quad-\frac{1}{x})d x 

$$

Solution

(i) We have

$$

\int\frac{x^{3}-1}{x^{2}}d x=\int x d x-\int x^{-2}d x\qquad\mathrm{(b y~P r o p e r t y~V)}

$$

$$

\begin{aligned}&\stackrel{\sim}{=}\left(\frac{x^{1+1}}{1+1}+\mathrm{C}_1\right)-\left(\frac{x^{-2+1}}{-2+1}+\mathrm{C}_2\right);\mathrm{C}_1,\mathrm{C}_2are constants of integration\\&=\frac{x^2}{2}+\mathrm{C}_1-\frac{x^{-1}}{-1}-\mathrm{C}_2=\frac{x^2}{2}+\frac{1}{x}+\mathrm{C}_1-\mathrm{C}_2\\&=\frac{x^2}{2}+\frac{1}{x}+\mathrm{C},where C=\mathrm{C}_1-\mathrm{C}_2is another constant of integration.\\ \end{aligned} 1

$$

Note From nowonwards, we shall writeonly oneconstant ofintegrationi the final answer.

$$

\begin{aligned}(ii)&We have\\&\int(x^{\frac{2}{3}}+1)dx=\int x^{\frac{2}{3}}dx+\int dx\\&=\frac{x^{\frac{2}{3}+1}}{\frac{2}{3}+1}+x+C=\frac{3}{5}x^{\frac{5}{3}}+x+C\\ (iii)&We have\int(x^{\frac{3}{2}}+2e^x-\frac{1}{x})dx=\int x^{\frac{3}{2}}dx+\int2e^x dx-\int\frac{1}{x}dx\\&=\frac{x^{\frac{3}{2}+1}}{\frac{3}{2}+1}+2e^x-\log|x|+C\\&=\frac{2}{5}x^{\frac{5}{2}}+2e^x-\log|x|+C\end{aligned}

$$

Example 3 Find the following integrals:

$$

{\mathrm{(i)}}\quad{\overset{\cdot}{\underset{\cdot}{\int}}}\left(\sin x+\cos x\right)d x\quad{\mathrm{(i i)}}{\overset{\cdot}{\underset{\cdot}{\int}}}\cos\infty x\left(\cos\infty x+\cot x\right)d x.

$$

Solution

(i)

$$

\int\left(\sin x+\cos x\right)dx=\int\sin x dx+\int\cos x dx 

$$

(ii)

$$

\begin{aligned}&\begin{aligned}\\ &\int\left(\cos\sec x\left(\cos\sec x+\cot x\right)dx=\int\cos\sec^2x dx+\int\cos\sec x\cot x dx\right)\\&=-\cot x-\cos\sec x+C\\&\int\frac{1-\sin x}{\cos^2x}dx=\int\frac{1}{\cos^2x}dx-\int\frac{\sin x}{\cos^2x}dx\\&=\int\sec^2x dx-\int\tan x\sec x dx\\&=\tan x-\sec x+C\\ &\end{aligned}\\ \end{aligned}

$$

Example 4 Find the anti derivative F of f defined by $f(x)=4x^{3}-6$ ,where F $(0)=3$ Solution One anti derivative of $f\left(x\right)$ s $x^{4}-6x$ since

$$

\frac{d}{d x}(x^{4}-6x)=4x^{3}-6

$$

Therefore, the anti derivative F is given by

$$

F(x)=x^{4}-6x+C,{\mathrm{~w h e r e~}}C{\mathrm{~i s~c o n s t a n t}}

$$

Given that

$$

\mathrm{F}(0)=3,\mathrm{which gives},

$$

$$

3=0-6\times0+C\quad\mathrm{o r}\quad C=3

$$

Hence, the required anti derivative is the unique function F defined by

$$

F(x)=x^{4}-6x+3.

$$

## Remarks

(i) We see that if F is an anti derivative $\operatorname{o f}f,$ then so is $\mathrm{F}+\mathrm{C}$ , where C is any constant. Thus, if we know one anti derivative F of a function f, we can write down an infinite number of anti derivatives of f by adding any constant to F expressed by $\mathbb{F}(x)+\mathbb{C},\mathbb{C}\in\mathbb{R}$ . In applications, it is often necessary to satisfy an additional condition which then determines a specific value of C giving unique anti derivative of the given function.

(i)Sometims,is ot exessile intrms of lmentary unctis i., plynomial,logarithmic, exponential, trigonometric functions and their inverses etc. We are therefore blocked for finding $\int f(x)dx$ :. For example, it is not possible to find $\int e^{-x^{2}}dx$ by inspection since we can not find a function whose derivative is $e^{-x^{2}}$ (ii)Whe formulae are modified accordingly. For instance

$$

\int y^{4}dy=\frac{y^{4+1}}{4+1}+C=\frac{1}{5}y^{5}+C 

$$

## 添司

1. Both are operations on functions.

2. Both satisfy the property of linearity, i.e..

$$

\begin{align*}(i)&\frac{d}{dx}\left[k_{1}f_{1}(x)+k_{2}f_{2}(x)\right]=k_{1}\frac{d}{dx}f_{1}(x)+k_{2}\frac{d}{dx}f_{2}(x)\\ (ii)&\int\left[k_{1}f_{1}(x)+k_{2}f_{2}(x)\right]d x=k_{1}\int f_{1}(x)d x+k_{2}\int f_{2}(x)d x\end{align*}

$$

Here $k_{\mathrm{t}}$ and $k_{2}$ are constants.

3are not integrable.We will learn moreabout nondiferentiable functions and nonintegrable functions in higher classes.

4. The derivative of a function, when it exists, is a unique function. The integral of afunctionit.Hwvryueutieo,,two integrals of a function differ by a constant.

5. When a polynomial function Pis diferentiated, the rsult is a polynomial whose degree is teeofmlia the result is a polynomial whose degree is 1 more than that of P.

6. We can speak of the derivative at a point. We never speak of the integral at a pint,ooa is defined as will be seen in Section 7.7.

7. The derivative of a function has a geometrical meaning, namely, the slope of the tangent to the corresponding curve at a point. imilarly, the indefinite integral of a function represents geometrically, a family of curves placed parallel to each other having parallel tangents at the points of intersection of the curves of the family with the lines orthogonal (perpendicular) to the axis representing the variable of integration.

8. The derivative is used for finding some physical quantities like the velocity of a moving particle, when the distance traversed at any time t is known. Similarly,the integral is used in calculating the distance traversed when the velocity at time t is known.

9. Differentiation is a process involving limits.So isintegration, as will be seen in Section 7.7.

10. The process of differentiation and integration are inverses of each other as discussed in Section 7.2.2 (i).

### EXERCISE 7.1

Find a iion.1. sin 2x 2. cos 3x 3.$e^{2x}$

$$

Find a iion.e^{2x}

$$

4.

$$

(a x+b)^{2}

$$

$$

5。\sin2x-4\ e^{3x}

$$

Find the following integrals in Exercises 6 to 20:

$$

\int\left(4e^{3x}+1\right)d x\quad\int x^{2}\left(1-\frac{1}{x^{2}}\right)d x\quad\int\left(a x^{2}+b x+c\right)d x 

$$

9.

$$

\int\left(2x^{2}+e^{x}\right)dx\quad 双冏 \quad\int\left(\sqrt{x}-\frac{1}{\sqrt{x}}\right)^{2}dx\quad 双冏 \quad\int\frac{x^{3}+5x^{2}-4}{x^{2}}dx 

$$

12.

15.

17.

$$

\begin{aligned}&\int\frac{x^{3}+3x+4}{\sqrt{x}}dx\quad 双水 \quad\int\frac{x^{3}-x^{2}+x-1}{x-1}dx 双水.\int(1-x)\sqrt{x}dx\\ &\int\sqrt{x}\left(3x^{2}+2x+3\right)dx\quad 双水.\int\left(2x-3\cos x+e^{x}\right)dx\\ &\int\left(2x^{2}-3\sin x+5\sqrt{x}\right)dx\quad 双水.\int\sec x\left(\sec x+\tan x\right)dx\\ \end{aligned}

$$

19.

$$

\int\frac{\sec^{2}x}{\cos\csc^{2}x}dx\quad\leq\quad20.\quad\int\frac{2-3\sin x}{\cos^{2}x}dx.

$$

Choose the correct answer in Exercises 21 and 22.

21. The anti derivative of $\left(\sqrt{x}+\frac{1}{\sqrt{x}}\right)$ equals

(A)

$$

\left[\frac{1}{3}x^{\frac{1}{3}}+2x^{\frac{1}{2}}+C\right]

$$

(B)

$$

{\frac{2}{3}}x^{\frac{2}{3}}+{\frac{1}{2}}x^{2}+\mathbf{C}

$$

(C)

$$

\left[{\frac{2}{3}}x^{\frac{3}{2}}+2x^{\frac{1}{2}}+\mathbf{C}\right]

$$

(D)

$$

{\frac{3}{2}}x^{\frac{3}{2}}+{\frac{1}{2}}x^{\frac{1}{2}}+\mathbf{C}

$$

22. If $\frac{d}{d x}f(x)=4x^{3}-\frac{3}{x^{4}}$ such that $f(2)=0$ Then $f(x)$ is

(A)

$$

x^{4}+{\frac{1}{x^{3}}}-{\frac{129}{8}}

$$

(B)

$$

x^{3}+{\frac{1}{x^{4}}}+{\frac{129}{8}}

$$

(C)

$$

x^{4}+\frac{1}{x^{3}}+\frac{129}{8}

$$

(D)

$$

x^{3}+{\frac{1}{x^{4}}}-{\frac{129}{8}}

$$

## MATHEMATICS

### 7.3 Methods of Integration

In previous section, we discussed integrals of those functions which were readily obtainable from derivatives of some functions. It was based on inspection, i.e., on the search of a function F whose derivative isf which led us to the integral of f. However,this method, which depends on inspection, is not very suitable for many functions.Hence, we need to develop additional techniques or methods for finding the integrals by reducing them into standard forms. Prominent among them are methods based on:

1. Integration by Substitution

2. Integration using Partial Fractions

3. Integration by Parts

#### 7.3.1 Integration by substitution

In this section, we consider the method of integration by substitution.

The given integral $\int f(x)$ dx can be transformed into another form by changing the independent variable x to t by substituting $x=g\left(t\right)$

Consider

$$

\mathrm{I}=\int f(x)dx 

$$

Put $x=g(t)$ so that ${\frac{d x}{d t}}=g^{\prime}(t)$

We write

Thus

$$

\begin{aligned}dx&=g^{\prime}(t)dt\\ I&=\int f(x)dx=\int f(g(t))g^{\prime}(t)dt\end{aligned}

$$

This change of variable formula is one of the important tools available to us in the name of integration by substitution. It is often important to guess what will be the useful substitution. Usually, we make a substitution for a function whose derivative also occurs in the integrand as illustrated in the following examples.

Example 5 Integrate the following functions w.r.t. x.

(i) sin mx (ii)$2x\sin\left(x^{2}+1\right)$

(i)

$$

\left[{\frac{\tan^{4}{\sqrt{x}}\sec^{2}{\sqrt{x}}}{\sqrt{x}}}\right.]

$$

(iv)

$$

\frac{\sin\left(\tan^{-1}x\right)}{1+x^{2}}

$$

Solution

$mx=t\;so that\;mdx=dt$

Therefore,

$$

\int\sin mx dx=\frac{1}{m}\int\sin t dt=-\frac{1}{m}\cos t+C=-\frac{1}{m}\cos mx+C 

$$

(ii) Derivative of $x^{2}+1$ is 2x. Thus, we use the substitution $x^{2}+1=t$ so that

$2x\;d x=d t$

$$

Therefore,\int2x\sin\left(x^{2}+1\right)dx=\int\sin tdt=-\cos t+C=-\cos\left(x^{2}+1\right)+C 

$$

(i) Derivative of $\left[{\sqrt{x}}{\mathrm{~i s~}}{\frac{1}{2}}x^{-{\frac{1}{2}}}={\frac{1}{2{\sqrt{x}}}}\right]$ . Thus, we use the substitution

$$

\begin{aligned}\sqrt{x}=t so that\frac{1}{2\sqrt{x}}dx=dt giving dx=2t dt.\\ Thus,\quad\int\frac{\tan^{4}\sqrt{x}\sec^{2}\sqrt{x}}{\sqrt{x}}dx=\int\frac{2t\tan^{4}t\sec^{2}t dt}{t}=2\int\tan^{4}t\sec^{2}t dt.\end{aligned}

$$

Again, we make another substitution tan $t=u$ so that $\sec^{2}t\ dt=du$

Therefore,

Hence,

$$

\begin{aligned}2\int\tan^{4}t\sec^{2}t dt&=2\int u^{4}du=2\frac{u^{5}}{5}+C\\&=\frac{2}{5}\tan^{5}t+C(since u=\tan t)\\&=\frac{2}{5}\tan^{5}\sqrt{x}+C(since t=\sqrt{x})\\int\frac{\tan^{4}\sqrt{x}\sec^{2}\sqrt{x}}{\sqrt{x}}dx&=\frac{2}{5}\tan^{5}\sqrt{x}+C\end{aligned}

$$

Alternatively, make the substitution tan $\sqrt{x}=t$

(iv) Derivative of $\tan^{-1}x=\frac{1}{1+x^{2}}$ . Thus, we use the substitution

$$

\tan^{-1}x=t{\mathrm{~s o~t h a t~}}{\frac{d x}{1+x^{2}}}=d t.

$$

Therefore ,$\int\frac{\sin\left(\tan^{-1}x\right)}{1+x^{2}}dx=\int\sin tdt=-\cos t+C=-\cos\left(\tan^{-1}x\right)+C$

Now, we discuss some important integrals involving trigonometric functions and their standard integrals using substitution technique. These will be used later without reference.

(i) tan $x dx=\log|\sec x|+C$

We have

$$

\int\tan x dx=\int\frac{\sin x}{\cos x}dx 

$$

$$

\begin{aligned}&\begin{aligned}\\ &\text{Put}\cos x=t\text{so that}\sin x dx=-dt\\&\text{until}\\&\text{On}\\&\text{for}\\&\text{for}\\&\text{for}\\&\text{for}\\&\text{for}\\&\text{for}\\&\text{in x}\\&\text{for}\\&\text{in x}\\&\text{for}\\&\text{in x}\\&\text{for}\\&\text{in x}\\&\text{for}\\&\text{in x}\\&\text{for}\\&\text{in x}\\&\text{in}\\&\text{for}\\&\text{in x}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\text{in}\\&\\&\text\\&{in}\\&\text\\&\\&\\&\text{in}\\&\\&\text{in}\\&\\&\\&\text\\&\\&\\&}\\&\text\\&{in\\&\\&}\\&\text\\&\\&\\&\\&\\&\\&\text\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\&\\

$$

Example 6Findthe ollowing iterals:

$$

(\mathrm{i})\quad\int\sin^{3}x\cos^{2}x d x\quad(\mathrm{i i})\quad\int{\frac{\sin x}{\sin{(x+a)}}}d x\quad(\mathrm{i i i})\quad\int{\frac{1}{1+\tan x}}d x 

$$

Solution

$$

\begin{aligned}(i)\quad&We have\\&\int\sin^{3}x\cos^{2}x dx=\int\sin^{2}x\cos^{2}x\left(\sin x\right)dx\\&=\int\left(1-\cos^{2}x\right)\cos^{2}x\left(\sin x\right)dx\\&Put t=\cos x so that dt=-\sin x dx\\&Therefore,\quad\int\sin^{2}x\cos^{2}x\left(\sin x\right)dx=-\int\left(1-t^{2}\right)t^{2}dt\\&=-\int\left(t^{2}-t^{4}\right)dt=-\left(\frac{t^{3}}{3}-\frac{t^{5}}{5}\right)+C\\&=-\frac{1}{3}\cos^{3}x+\frac{1}{5}\cos^{5}x+C\end{aligned}

$$

(ii) Put $x+a=t.$ .Then $d x=d t$ . Therefore

$$

\begin{aligned}\int\frac{\sin x}{\sin\left(x+a\right)}dx=&\int\frac{\sin\left(t-a\right)}{\sin t}dt\\=&\int\frac{\sin t\cos a-\cos t\sin a}{\sin t}dt\\=&\cos a\int dt-\sin a\int\cot t dt\\=&\left.\left(\cos a\right)t-\left(\sin a\right)\right[\log\left|\sin t\right|+\mathrm{C}_{1}\left]\right.\\=&\left.\left(\cos a\right)\left(x+a\right)-\left(\sin a\right)\right[\log\left|\sin\left(x+a\right)\right|+\mathrm{C}_{1}\left]\right.\\=&\left.x\cos a+a\cos a-\left(\sin a\right)\log\left|\sin\left(x+a\right)\right|-\mathrm{C}_{1}\sin a\right\end{aligned}

$$

$$

{\mathrm{H e n c e}},\int{\frac{\sin x}{\sin(x+a)}}d x=x\cos a-\sin a\log\left|\sin(x+a)\right|+C,

$$

where,$\mathrm{C}=-\mathrm{C}_{1}\sin a+a\cos a,$ is another arbitrary constant.

(i)

$$

\begin{aligned}\int\frac{dx}{1+\tan x}&=\int\frac{\cos x dx}{\cos x+\sin x}\\&=\frac{1}{2}\int\frac{(\cos x+\sin x+\cos x-\sin x)dx}{\cos x+\sin x}\end{aligned}

$$

$$

\begin{aligned}&=\frac{1}{2}\int dx+\frac{1}{2}\int\frac{\cos x-\sin x}{\cos x+\sin x}dx\\ &=\frac{x}{2}+\frac{C_1}{2}+\frac{1}{2}\int\frac{\cos x-\sin x}{\cos x+\sin x}dx\\ \end{aligned}

$$

Now, consider $\int\frac{\cos x-\sin x}{\cos x+\sin x}dx$

Put cos $x+\sin$ 1$x=t\;{\mathrm{s o}}$ that (cos − sin x)$dx=dt$

Therefore $\mathrm{I}=\int\frac{dt}{t}=\log|t|+C_2=\log|\cos x+\sin x|+C_2$

Putting it in (1), we get

$$

\begin{aligned}\int\frac{dx}{1+\tan x}&=\frac{x}{2}+\frac{C_1}{2}+\frac{1}{2}\log\left|\cos x+\sin x\right|+\frac{C_2}{2}\\&=\frac{x}{2}+\frac{1}{2}\log\left|\cos x+\sin x\right|+\frac{C_1}{2}+\frac{C_2}{2}\\&=\frac{x}{2}+\frac{1}{2}\log\left|\cos x+\sin x\right|+C_1\left(C=\frac{C_1}{2}+\frac{C_2}{2}\right)\end{aligned}

$$

### EXERCISE 7.2

Integrate the functions in Exercises 1 to 37:

1.$\frac{2x}{1+x^{2}}$ 2.$\frac{\left(\log x\right)^{2}}{x}$ 3.$\frac{1}{x+x\log x}$

4. sin x sin (cos x)5.$\sin(ax+b)\cos(ax+b)$

6.$\sqrt{ax+b}$ 7.$\left[x\sqrt{x+2}\right]$ 8.$x{\sqrt{1+2x^{2}}}$

9.$(4x+2){\sqrt{x^{2}+x+1}}$ 10.$\frac{1}{x-\sqrt{x}}$ 11.$\frac{x}{\sqrt{x+4}},x>0$

12.$(x^{3}-1)^{\frac{1}{3}}\;x^{5}$ 13.$\frac{x^{2}}{\left(2+3x^{3}\right)^{3}}$ 14.$\frac{1}{x\left(\log x\right)^m},x>0,m\neq1$

15.$\frac{x}{9-4x^{2}}$ 16.$\left[e^{2x+3}\right.]$ 17.$\frac{x}{e^{x^{2}}}$

18.$\frac{e^{tan^{-1}x}}{1+x^{2}}$ 19.$\frac{e^{2x}-1}{e^{2x}+1}$ 20.$\left|\frac{e^{2x}-e^{-2x}}{e^{2x}+e^{-2x}}\right|$

21.$\tan^{2}\left(2x-3\right)$ 22.$\sec^{2}\left(7-4x\right)$ 23.$\frac{\sin^{-1}x}{\sqrt{1-x^{2}}}$

24.

$$

\frac{2\cos x-3\sin x}{6\cos x+4\sin x}\quad\frac{1}{25}\quad\frac{1}{\cos^{2}x\left(1-\tan x\right)^{2}}\quad26

$$

27.$\left[{\sqrt{\sin2x}}\cos2x\right.]$ 28.$\frac{\cos x}{\sqrt{1+\sin x}}$ 29. cot x log sin x

30.$\frac{\sin x}{1+\cos x}$ 31.$\frac{\sin x}{\left(1+\cos x\right)^{2}}$ 32.$\frac{1}{1+\cot x}$

$$

\frac{1}{1-\tan x}\quad\frac{\sqrt{\tan x}}{\sin x\cos x}\quad\frac{\left(1+\log x\right)^2}{x}

$$

36.

$$

\frac{(x+1)(x+\log x)^2}{x}\quad\frac{x^3\sin\left(\tan^{-1}x^4\right)}{1+x^8}

$$

Choose the correct answer in Exercises 38 and 39.

38.$\int{\frac{10x^{9}+10^{x}\log_{e^{10}}d x}{x^{10}+10^{x}}}$ equals

(A)

$$

10^{x}-x^{10}+\mathbf{C}

$$

(B)

$$

10^{x}+x^{10}+\mathbf{C}

$$

(C)

$$

(10^{x}-x^{10})^{-1}+\mathbf{C}

$$

(D)

$$

\log(10^{x}+x^{10})+\mathbf{C}

$$

39.$\int{\frac{d x}{\sin^{2}x\cos^{2}x}}\operatorname{e q u a l s}$

(A)$\tan x+\cot x+C$ (B)tan $x-\cot x+\mathbf{C}$ (C)$\tan x\cot x+\mathbf{C}$ (D)tan $x-\cot2x+\mathbf{C}$

#### 7.3.2 Integration using trigonometric identities

Whenhe etities to find the integral as illustrated through the following example.

Example 7 Find (i)$\int\cos^{2}x dx$ (ii)$\int\sin2x\cos3x dx$ (iii)$\int\sin^{3}x dx$

Solution

(i)Recall the identity cos $2x=2\cos^{2}x-1$ , which gives

Therefore,

$$

\begin{aligned}\cos^{2}x&=\frac{1+\cos2x}{2}\\int\cos^{2}x dx&=\frac{1}{2}\int(1+\cos2x)dx=\frac{1}{2}\int dx+\frac{1}{2}\int\cos2x dx\\&=\frac{x}{2}+\frac{1}{4}\sin2x+C\end{aligned}

$$

$$

\begin{aligned}(ii)\quad Recall the identity\sin x\cos y=\frac{1}{2}\left[\sin(x+y)+\sin(x-y)\right]\quad&(Why?)\\ Then\quad\int\sin2x\cos3x dx\quad=\quad&\frac{1}{2}\left[\int\sin5x dx\bullet\int\sin x dx\right]\\=\quad&\frac{1}{2}\left[-\frac{1}{5}\cos5x+\cos x\right]+C\\=\quad&-\frac{1}{10}\cos5x+\frac{1}{2}\cos x+C\end{aligned}

$$

(i) From the identity sin $3x=3\sin x-4\sin^{3}x.$ , we find that

$$

\sin^{3}x={\frac{3{\sin}x-{\sin}3x}{4}}

$$

Therefore,

$$

\begin{aligned}\int\sin^{3}x dx&=\frac{3}{4}\int\sin x dx-\frac{1}{4}\int\sin3x dx\\&=-\frac{3}{4}\cos x+\frac{1}{12}\cos3x+C\end{aligned}

$$

Alternatively,$\int\sin^{3}x dx=\int\sin^{2}x\sin x dx=\int(1-\cos^{2}x)$ sin x dx

Put cos $x=t\;{\mathrm{s o}}$ that − sin x $d x=d t$

Therefore,

$$

\int\sin^{3}x dx=-\int\left(1-t^{2}\right)dt=-\int dt+\int t^{2}dt=-t+\frac{t^{3}}{3}+C 

$$

Remark It can be shown using trigonometric identities that both answers are equivalent.

### EXERCISE 7.3

[abl]

1.$\sin^{2}\left(2x+5\right)$ EM 2. sin 3x cos 4x [Tae]3. cos 2x cos 4x cos 6

4.$\sin^{3}\left(2x+1\right)$ 5.$\sin^{3}x\cos^{3}x$ 6. sin x sin 2x sin 3x

7. sin 4x sin 88.$\frac{1-\cos x}{1+\cos x}$ 9.$\frac{\cos x}{1+\cos x}$

10.$\sin^{4}x$ 11.$\cos^{4}2x$ 12.$\frac{\sin^{2}x}{1+\cos x}$

13.

$$

\frac{\cos2x-\cos2\alpha}{\cos x-\cos\alpha}

$$

$$

\frac{\cos x-\sin x}{1+\sin2x}

$$

$$

\tan^{3}2x\sec2x 

$$

16.$\tan^{4}x$ 17.$\left[{\frac{\sin^{3}x+\cos^{3}x}{\sin^{2}x\cos^{2}x}}\right.]$ 18.$\frac{\cos2x+2\sin^{2}x}{\cos^{2}x}$

19.

$$

\left[\frac{1}{\sin x\cos^3x}\right]_{x=1}\quad\frac{\cos2x}{\left(\cos x+\sin x\right)^2}\quad\frac{21}{x}\quad\sin^{-1}\left(\cos x\right)

$$

22.

$$

\left[{\frac{1}{\cos\left(x-a\right)\cos\left(x-b\right)}}\right.]

$$

Choose the correct answer in Exercises 23 and 24.

23.$\int\frac{\sin^{2}x-\cos^{2}x}{\sin^{2}x\cos^{2}x}dx is equal to$

(A)(C)${\begin{array}{r l}&{\tan x+\cot x+\mathbf{C}}\\ &{-\tan x+\cot x+\mathbf{C}}\end{array}}$ (B)${\begin{array}{r l}&{\tan x+\csc x+\mathbf{C}}\\ &{\tan x+\sec x+\mathbf{C}}\end{array}}$

24.$\int_{\frac{e^{x}(1+x)}{\cos^{2}(e^{x}x)}}d x\mathrm{e q u a l s}$

(A)$-\cot(e x^{x})+\mathbf{C}$ (B)$\tan(x e^{x})+\mathbf{C}$ (C)$\tan\left(e^{x}\right)+\mathbf{C}$ (D)$\cot\left(e^{x}\right)+\mathbf{C}$

### 7.4 Integrals of Some Particular Functions

In this section, we mention below some important formulae of integrals and apply them for integrating many other related standard integrals:

(1)

$$

\int\frac{dx}{x^{2}-a^{2}}=\frac{1}{2a}\log\left|\frac{x-a}{x+a}\right|+C 

$$

(2)

$$

\int\frac{dx}{a^{2}-x^{2}}=\frac{1}{2a}\log\left|\frac{a+x}{a-x}\right|+C 

$$

(3)

$$

\int\frac{dx}{x^{2}+a^{2}}=\frac{1}{a}\tan^{-1}\frac{x}{a}+C 

$$

(4)

$$

\int\frac{dx}{\sqrt{x^{2}-a^{2}}}=\log\left|x+\sqrt{x^{2}-a^{2}}\right|+C 

$$

(5)

$$

\int\frac{dx}{\sqrt{a^{2}-x^{2}}}=\sin^{-1}\frac{x}{a}+C 

$$

(6)

$$

\int\frac{dx}{\sqrt{x^{2}+a^{2}}}=\log\left|x+\sqrt{x^{2}+a^{2}}\right|+C 

$$

We now prove the above results:

$$

\frac{1}{x^{2}-a^{2}}=\frac{1}{(x-a)(x+a)}

$$

Therefore,

$$

\begin{aligned}\int\frac{dx}{x^{2}-a^{2}}&=\frac{1}{2a}\left[\int\frac{dx}{x-a}-\int\frac{dx}{x+a}\right]\\&=\frac{1}{2a}\left[\log|(x-a)|-\log|(x+a)|\right]+C\\&=\frac{1}{2a}\log\left|\frac{x-a}{x+a}\right|+C\end{aligned}

$$

(2) In view of (1) above, we have

$$

(2) In view of (1) above, we have \frac{1}{a^{2}-x^{2}}=\frac{1}{2a}\left[\frac{(a+x)+(a-x)}{(a+x)(a-x)}\right]=\frac{1}{2a}\left[\frac{1}{a-x}+\frac{1}{a+x}\right]

$$ Therefore,

$$

\begin{aligned}\int\frac{dx}{a^{2}-x^{2}}&=\frac{1}{2a}\left[\int\frac{dx}{a-x}+\int\frac{dx}{a+x}\right]\\&=\frac{1}{2a}\left[-\log\left|a-x\right|+\log\left|a+x\right|\right]+C\\&=\frac{1}{2a}\log\left|\frac{a+x}{a-x}\right|+C\end{aligned}

$$

Note]The techique used in(1) will be explained in Section7.5.

(3)Put $x=a$ tan 0. Then $d x=a\sec^{2}\theta$ dθ.

$\int\frac{dx}{x^{2}+a^{2}}=\int\frac{a\sec^{2}\theta d\theta}{a^{2}\tan^{2}\theta+a^{2}}\quad=\quad\frac{1}{a}\int d\theta=\frac{1}{a}\theta+C=\frac{1}{a}\tan^{-1}\frac{x}{a}+C.$ (4) Let $x=a$ sec θ. Then $d x=a\sec\theta\tan\theta d\theta.$

Therefore,

$$

\int\frac{dx}{x^{2}+a^{2}}=\int\frac{a\sec^{2}\theta d\theta}{a^{2}\tan^{2}\theta+a^{2}}\quad=\quad\frac{1}{a}\int d\theta=\frac{1}{a}\theta+C=\frac{1}{a}\tan^{-1}\frac{x}{a}+C.sec θ. Then d x=a\sec\theta\tan\theta d\theta.

$$

Therefore,

$$

\begin{aligned}\int\frac{dx}{\sqrt{x^{2}-a^{2}}}&=\int\frac{a\sec\theta\tan\theta d\theta}{\sqrt{a^{2}\sec^{2}\theta-a^{2}}}\\&=\int\sec\theta d\theta=\log|\sec\theta+\tan\theta|+C_{1}\\&=\log\left|\frac{x}{a}+\sqrt{\frac{x^{2}}{a^{2}}-1}\right|+C_{1}\\&=\log\left|x+\sqrt{x^{2}-a^{2}}\right|-\log|a|+C_{1}\\&=\log\left|x+\sqrt{x^{2}-a^{2}}\right|+C,where C=C_{1}-\log|a|.\end{aligned}

$$

(5) Let $x=a\sin\theta$ . Then $d x=a\cos\theta d\theta$

$\begin{aligned}\int\frac{dx}{\sqrt{a^{2}-x^{2}}}&=\int\frac{a\cos\theta d\theta}{\sqrt{a^{2}-a^{2}\sin^{2}\theta}}\\&=\int d\theta=\theta+C=\sin^{-1}\frac{x}{a}+C.\end{aligned}$ (6) Let $x=a$ tan θ. Then $dx=a\sec^{2}\theta\mathrm{d}\theta$

Therefore,

$$

\begin{aligned}\int\frac{dx}{\sqrt{a^{2}-x^{2}}}&=\int\frac{a\cos\theta d\theta}{\sqrt{a^{2}-a^{2}\sin^{2}\theta}}\\&=\int d\theta=\theta+C=\sin^{-1}\frac{x}{a}+C.\end{aligned}tan θ. Then 

$$

Therefore,

$$

\int\frac{dx}{\sqrt{x^{2}+a^{2}}}=\int\frac{a\sec^{2}\theta d\theta}{\sqrt{a^{2}\tan^{2}\theta+a^{2}}}=\int\sec\theta d\theta=\log|(\sec\theta+\tan\theta)|+C_{1}

$$

$$

\begin{aligned}&\frac{\sqrt[3]{x}}{x}=\frac{\sqrt[3]{x}}{\log\left|\frac{x}{a}+\sqrt{\frac{x^2}{a^2}+1}\right|}+C_1\\ &=\frac{\sqrt[3]{x}}{\log\left|x+\sqrt{x^2+a^2}\right|}-\log|a|+C_1\\ &=\frac{\sqrt[3]{x}}{\log\left|x+\sqrt{x^2+a^2}\right|}+C_1,where C=C_1-\log|a|.\\ \end{aligned}

$$

Applying these standard formulae, we now obtain some more formulae which are useful from applications point of view and can be applied directly to evaluate other integrals.

(7) To find the integral $\int{\frac{d x}{a x^{2}+b x+c}}$ , we write

$$

ax^{2}+bx+c=a\left[x^{2}+\frac{b}{a}x+\frac{c}{a}\right]=a\left[\left(x+\frac{b}{2a}\right)^{2}+\left(\frac{c}{a}-\frac{b^{2}}{4a^{2}}\right)\right]一

$$

Now, put $x+\frac{b}{2a}=t\quad\mathrm{so}$ that $d x=d t$ and writing $\frac{c}{a}-\frac{b^{2}}{4a^{2}}=\pm k^{2}$ . We find the integral reduced to the form $\frac{1}{a}\int_{}\frac{dt}{t^{2}\pm k^{2}}$ depending upon the sign of $\left[\left(\frac{c}{a}-\frac{b^2}{4a^2}\right)\right.]$ and hence can be evaluated.

(8) To find the integral of the type $\int_{\frac{dx}{\sqrt{ax^{2}+bx+c}}}^{\frac{dx}{\sqrt{ax^{2}+bx+c}}}$ , proceeding as in (7), we obtain the integral using the standard formulae.

(9) To find the integral of the type $\int{\frac{p x+q}{a x^{2}+b x+c}}d x$ , where p, q, a,$b,\;c$ are constants, we are to find real numbers A, B such that

$$

px+q=\mathrm{A}\frac{d}{dx}\left(ax^{2}+bx+c\right)+\mathrm{B}=\mathrm{A}\left(2ax+b\right)+\mathrm{B}

$$

To determine A and B, we equate from both sides the coefficients of x and the constant terms. A and B are thus obtained and hence the integral is reduced to one of the known forms.

(10) For the evaluation of the integral of the type $\int_{\frac{\left(px+q\right)dx}{\sqrt{ax^{2}+bx+c}}}^{\frac{\left(px+q\right)dx}{\sqrt{ax^{2}+bx+c}}}$ ,we proceed as in (9) and transform the integral into known standard forms.

Let us illustrate the above methods by some examples.

Example 8 Find the following integrals:

(i)

$$

\int_{\frac{dx}{x^2-16}}^{\frac{dx}{x^2-16}}

$$

(ii)

$$

\int_{\frac{dx}{\sqrt{2x-x^2}}}^{\frac{dx}{\sqrt{2x-x^2}}}

$$

Solution

(i) We have $\int\frac{dx}{x^{2}-16}=\int\frac{dx}{x^{2}-4^{2}}=\frac{1}{8}\log\left|\frac{x-4}{x+4}\right|+C$ [by 7.4 (1)]

(ii)

$$

\int\frac{dx}{\sqrt{2x-x^{2}}}=\int\frac{dx}{\sqrt{1-(x-1)^{2}}}

$$

Put ..$x-1=t.{\mathrm{~T h e n~}}d x=d t$

Therefore,

$$

\int\frac{dx}{\sqrt{2x-x^{2}}}=\int\frac{dt}{\sqrt{1-t^{2}}}=\sin^{-1}\left(t\right)+C 

$$

Example 9 Find the following integrals :

$$

$\left(\mathrm{i}\right)\int_{\frac{x^{2}-6x+13}{x^{2}-6x+13}}^{\frac{dx}{x^{2}-6x+13}}\quad\left(\mathrm{ii}\right)\quad\int_{\frac{x^{2}+13x-10}{x^{2}-13x-10}}^{\frac{dx}{x^{2}-6x+13}}\quad\left(\mathrm{iii}\right)\quad\int_{\frac{x^{2}-6x+13}{x^{2}-2x}}^{\frac{dx}{x^{2}-6x+13}}\quad\left(\mathrm{iii}\right)\quad\int_{\frac{x^{2}-13}{x^{2}-13}}^{\frac{dx}{x^{2}-13}}\quad\left(\mathrm{iii}\right)\quad\int_{\frac{x^{2}-13}{x^{2}-13}}^{\frac{dx}{x^{2}-13}}\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{iii}\right)\quad\left(\mathrm{ix}\right)\quad\left(\mathrm{ix}\right)\quad\left(\mathrm{ix}\right)\quad\quad\left(\mathrm{ix}\right)\quad\left(\mathrm{ix}\right)\quad\left(\right)\quad\left(\mathrm{ix}\right)\quad\quad\left(\mathrm{ix}\right)\quad\left(\mathrm{ix}\right)\quad\quad\left(\mathrm{ix}\right)\quad\quad\left(\mathrm{ix}\right)\quad\left(\right)\quad\left(\mathrm{ix}\right)\quad\quad\left(\mathrm{ix}\right)\quad\quad\left(\mathrm{ix}\right)\quad\quad\left(\right)\quad\left(\mathrm{ix}\right)\quad\quad\left(\mathrm{ix}\right)\quad\quad\left(\right)\quad\quad\left(\mathrm{ix}\right)\quad\quad\left(\right)\quad\quad\left(\mathrm{ix}\right)\quad\quad\left(\right)\quad\quad\left(\mathrm{ix}\right)\quad\quad\quad\left(\right)\quad\quad\left(\mathrm{ix}\right)\quad\quad\right)\quad\quad\left(\quad\left(\right)\quad\quad\left(\right)\quad\quad\quad\mathrm{ix}\right)\quad\quad\left(\right)\quad\quad\quad\left(\right)\quad\quad\quad\left(\right)\quad\quad\quad\left(\right)\quad\quad\quad\left(\right)\quad\quad\quad\left(\right)\quad\quad\quad\left(\right)\quad\quad\quad\left(\right)\quad\quad\quad\quad\left(\right)\quad\quad\quad\quad\left(\right)\quad\quad\quad\quad\quad\left(\right)\quad\quad\quad\quad\left(\right)\quad\quad\quad\quad\quad\left(\right)\quad\quad\quad\quad\quad\quad\left(\right)\quad\quad\quad\quad\quad\quad\left(\right)\quad\quad\quad\quad\quad\quad\quad\left(\right)\quad\quad\quad\quad\quad\quad\quad\quad\quad\left(\right)\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\left(\quad\right)\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad$ $

Solution

(i) We have $x^{2}-6x+13=x^{2}-6x+3^{2}-3^{2}+13=(x-3)^{2}+4$

So,

$$\int\frac{dx}{x^{2}-6x+13}=\int\frac{1}{(x-3)^{2}+2^{2}}dx 

$$

Let

$$

x-3=t.{\mathrm{~T h e n~}}d x=d t 

$$

Therefore,

$$

\int\frac{dx}{x^{2}-6x+13}=\int\frac{dt}{t^{2}+2^{2}}=\frac{1}{2}\tan^{-1}\frac{t}{2}+C 

$$

## MATHEMATICS

(

Thus

$$

\begin{aligned}3x^{2}+13x-10&=3\left(x^{2}+\frac{13x}{3}-\frac{10}{3}\right)\\&=3\left[\left(x+\frac{13}{6}\right)^{2}-\left(\frac{17}{6}\right)^{2}\right]\quad(completing the square)\\int&\frac{dx}{3x^{2}+13x-10}=\frac{1}{3}\int&\frac{dx}{\left(x+\frac{13}{6}\right)^{2}-\left(\frac{17}{6}\right)^{2}}\end{aligned}

$$

Put $x+\frac{13}{6}=t$ .Then $dx=dt$

$$

\begin{aligned}&\int\frac{dx}{3x^{2}+13x-10}=\frac{1}{3}\int\frac{dt}{t^{2}-\left(\frac{17}{6}\right)^{2}}\\ &\\ &=\frac{1}{3\times2\times\frac{17}{6}}\log\left|\frac{t-\frac{17}{6}}{t+\frac{17}{6}}\right|+C_{1}\quad\left[by7.4(i)\right]\\ &\\ &=\frac{1}{17}\log\left|\frac{x+\frac{13}{6}-\frac{17}{6}}{x+\frac{13}{6}+\frac{17}{6}}\right|+C_{1}\\ &\\ &=\frac{1}{17}\log\left|\frac{6x-4}{6x+30}\right|+C_{1}\\ &\\ &=\frac{1}{17}\log\left|\frac{3x-2}{x+5}\right|+C_{1}+\frac{1}{17}\log\frac{1}{3}\\ &\\ &=\frac{1}{17}\log\left|\frac{3x-2}{x+5}\right|+C,where C=C_{1}+\frac{1}{17}\log\frac{1}{3}\\ \end{aligned}

$$

(ii)

$$

{\begin{aligned}{{\stackrel{\cdot}{\int}}{\frac{d x}{{\sqrt{5x^{2}-2x}}}}=}&{{}{\frac{d x}{{\sqrt{5{\left(x^{2}-{\frac{2x}{5}}\right)}}}}}}\\ {=}&{{}{\frac{\cdot}{{\sqrt{5}}}}{\frac{d x}{{\sqrt{\left(x-{\frac{1}{5}}\right)^{2}-{\left({\frac{1}{5}}\right)^{2}}}}}}{\pmod{{\mathrm{s u p l e t i n g~t h e~s q u a r e}}}}}\end{aligned}}

$$

Put $x-\frac{1}{5}=t$ . Then $dx=dt$

Therefore,

$$

\begin{aligned}\int_{\frac{1}{\sqrt{5x^{2}-2x}}}^{\frac{1}{\sqrt{5x^{2}-2x}}}&=\frac{1}{\sqrt{5}}\int_{\frac{1}{\sqrt{t^{2}-\left(\frac{1}{5}\right)^{2}}}}^{\frac{1}{\sqrt{5}}}\\&=\frac{1}{\sqrt{5}}\log\left|t+\sqrt{t^{2}-\left(\frac{1}{5}\right)^{2}}\right|+C\\&=\frac{1}{\sqrt{5}}\log\left|x-\frac{1}{5}+\sqrt{x^{2}-\frac{2x}{5}}\right|+C\end{aligned}

$$

[by 7.4 (4)]

Example 10 Find the following integrals:

$$

\int_{\frac{\pi}{2x^{2}+6x+5}}^{\frac{\pi}{2x+2}}dx\quad(ii)\quad\int_{\frac{\pi}{5-4x+x^{2}}}^{\frac{\pi}{2x+3}}dx 

$$

Solution

(i) Using the formula 7.4 (9), we express

$$

x+2=\mathbf{A}\frac{d}{dx}\left(2x^2+6x+5\right)+\mathbf{B}=\mathbf{A}\left(4x+6\right)+\mathbf{B}

$$

Equating the coefficients of x and the constant terms from both sides, we get

$$

{\begin{aligned}{4\mathrm{A}=1{\mathrm{~a n d~}}6\mathrm{A}+\mathrm{B}=2\quad{\mathrm{o r}}\quad\mathrm{A}}&{{}={\frac{\stackrel{\cdot}{1}}{4}}{\mathrm{~a n d~}}\mathrm{B}={\frac{1}{2}}.}\\ {{\mathrm{T h e r e f o r e}},\qquad{\stackrel{\cdot}{\int}}{\frac{x+2}{2x^{2}+6x+5}}}&{{}={\frac{\stackrel{\cdot}{1}}{4}}{\int}{\frac{4x+6}{2x^{2}+6x+5}}d x+{\frac{1}{2}}{\int}{\frac{d x}{2x^{2}+6x+5}}}\\ &{{}={\frac{\stackrel{\cdot}{1}}{4}}\mathrm{I}_{1}+{\frac{1}{2}}\mathrm{I}_{2}\quad{\mathrm{(s a y)}}}\end{aligned}}

$$

In $\mathrm{I}_{1}$ , put $2x^{2}+6x+5=t,\ so that\ (4x+6)dx=dt$

Therefore,

$$

\begin{aligned}\mathrm{I}_{1}&=\int\frac{dt}{t}=\log|t|+C_{1}\\&=\log|2x^{2}+6x+5|+C_{1}\end{aligned}

$$

and

$$

\mathrm{I}_{2}=\int\frac{dx}{2x^{2}+6x+5}=\frac{1}{2}\int\frac{dx}{x^{2}+3x+\frac{5}{2}}

$$

$$

\frac{1}{2}\int_{\left(x+\frac{3}{2}\right)^2+\left(\frac{1}{2}\right)^2}^{\left(x+\frac{3}{2}\right)^2}\mathrm{d}x 

$$

Put $x+\frac{3}{2}=t$ ,So that $dx=dt$ ,we get

$$

\begin{aligned}\mathrm{I}_{2}&=\frac{1}{2}\int\frac{dt}{t^{2}+\left(\frac{1}{2}\right)^{2}}=\frac{1}{2\times\frac{1}{2}}\tan^{-1}2t+\mathrm{C}_{2}\\&=\tan^{-1}2\left(x+\frac{3}{2}\right)+\mathrm{C}_{2}=\tan^{-1}(2x+3)+\mathrm{C}_{2}\end{aligned}

$$

Using (2) and (3) in (1), we get

$$

\int\frac{x+2}{2x^{2}+6x+5}dx=\frac{1}{4}\log\left|2x^{2}+6x+5\right|+\frac{1}{2}\tan^{-1}(2x+3)+C 

$$

where,

$$

\mathrm{C}=\frac{\mathrm{C}_{1}}{4}+\frac{\mathrm{C}_{2}}{2}

$$

(ii)This integral is of the form given in 7.4 (10). Let us express

$$

x+3=\mathrm{A}\frac{d}{d x}\left(5-4x-x^{2}\right)+\mathrm{B}=\mathrm{A}\left(-4-2x\right)+\mathrm{B}

$$

Equating the coefficients of x and the constant terms from both sides, we get

$$

-2\mathrm{A}=1\mathrm{~and}-4\mathrm{~A}+\mathrm{B}=3,\mathrm{i.e.},\mathrm{A}=-\frac{1}{2}\mathrm{~and~B}=1

$$

Therefore,$\int_{\frac{x+3}{\sqrt{5-4x-x^2}}}^{\frac{x+3}{\sqrt{5-4x-x^2}}}dx=-\frac{1}{2}\int_{\frac{x+3}{\sqrt{5-4x-x^2}}}^{\frac{x-3}{\sqrt{5-4x-x^2}}}dx+\int_{\frac{x+3}{\sqrt{5-4x-x^2}}}^{\frac{x+3}{\sqrt{5-4x-x^2}}}dx$

$$

=-\frac{1}{2}\mathrm{~I}_{_{1}}+\mathrm{~I}_{_{2}}

$$

In $ I_{_{i}}$ , put $5-4x-x^{2}=t.$ so that $(-4-2x)\;d x=d t.$

Therefore,

Now consider

$$

\begin{aligned}I_{1}&=\int\frac{(-4-2x)dx}{\sqrt{5-4x-x^{2}}}=\int\frac{dt}{\sqrt{t}}=2\sqrt{t}+C_{1}\\&=2\sqrt{5-4x-x^{2}}+C_{1}\\ I_{2}&=\int\frac{dx}{\sqrt{5-4x-x^{2}}}=\int\frac{dx}{\sqrt{9-(x+2)^{2}}}\end{aligned}

$$

Put $x+2=t.$ ,so that $dx=dt$

Therefore,

$$

\begin{aligned}\mathrm{I}_{2}&=\int\frac{dt}{\sqrt{3^{2}-t^{2}}}=\sin^{-1}\frac{t}{3}+\mathrm{C}_{2}\\&=\sin^{-1}\frac{x+2}{3}+\mathrm{C}_{2}\end{aligned}

$$

[by 7.4 (5)]

Substituting (2) and (3) in (1), we obtain

$$

\int\frac{x+3}{\sqrt{5-4x-x^{2}}}=-\sqrt{5-4x-x^{2}}+\sin^{-1}\frac{x+2}{3}+C 

$$

### EXERCISE 7.4

Integrate the functions in Exercises 1 to 23.

1.

$$

\frac{3x^{2}}{x^{6}+1}

$$

2.

$$

\frac{1}{\sqrt{1+4x^{2}}}

$$

3.

$$

\frac{1}{\sqrt{\left(2-x\right)^{2}+1}}

$$

4.

7.

$$

\frac{1}{\sqrt{9-25x^{2}}}

$$

$$

\frac{x-1}{\sqrt{x^{2}-1}}

$$

5.

8.

$$

\frac{3x}{1+2x^{4}}

$$

$$

\frac{x^{2}}{\sqrt{x^{6}+a^{6}}}

$$

6.

9.

$$

\frac{x^{2}}{1-x^{6}}

$$

$$

\frac{\sec^{2}x}{\sqrt{\tan^{2}x+4}}

$$

10.

$$

\frac{1}{\sqrt{x^{2}+2x+2}}

$$

11.

$$

\frac{1}{9x^{2}+6x+5}

$$

12.

$$

\left[\frac{1}{\sqrt{7-6x-x^{2}}}\right.]

$$

13.

$$

\frac{1}{\sqrt{(x-1)(x-2)}}

$$

$$

\frac{1}{\sqrt{8+3x-x^{2}}}

$$

15.

$$

\frac{1}{\sqrt{(x-a)(x-b)}}

$$

16.

$$

\left[\frac{4x+1}{\sqrt{2x^2+x-3}}\right]\quad\frac{x+2}{\sqrt{x^2-1}}\quad\frac{5x-2}{1+2x+3x^2}

$$

19.

$$

\left\{\frac{6x+7}{\sqrt{(x-5)(x-4)}}\quad\frac{x+2}{\sqrt{4x-x^2}}\quad\frac{x+2}{21}\quad\frac{x+2}{\sqrt{x^2+2x+3}}\right\}

$$

22.

$$

\left[\frac{x+3}{x^{2}-2x-5}\right]_{23}=\frac{5x+3}{\sqrt{x^{2}+4x+10}}

$$

Choose the correct answer in Exercises 24 and 25.

24.

$$

\int\frac{dx}{x^{2}+2x+2}\quad equals 

$$

(C)$x\tan^{-1}\left(x+1\right)+\mathbf{C}$ $(x+1)\tan^{-1}x+\mathbf{C}$ $x\tan^{-1}\left(x+1\right)+\mathbf{C}$ (B)$\begin{aligned}&\tan^{-1}\left(x+1\right)+\mathbf{C}\\&\tan^{-1}x+\mathbf{C}\\ \end{aligned}$

25.$\int_{\frac{dx}{\sqrt{9x-4x^2}}}^{\frac{dx}{\sqrt{9x-4x^2}}}$ ·equals

(A)$\left[\frac{1}{9}\sin^{-1}\left(\frac{9x-8}{8}\right)+C\right]$ (B)$\frac{1}{2}\sin^{-1}\left(\frac{8x-9}{9}\right)+C$

(C)$\frac{1}{3}\sin^{-1}\left(\frac{9x-8}{8}\right)+C$ (D)$\frac{1}{2}\sin^{-1}\left(\frac{9x-8}{9}\right)+C$

### 7.5 Integration by Partial Fractions

Recall that a rational function is defined as the ratio of two polynomials in the form $\frac{\mathrm{P}(x)}{\mathrm{Q}(x)}$ , where $\mathrm{P}\left(x\right)$ and $\mathrm{Q}\left(x\right)$ are polynomials in x and $\mathrm{Q}\left(x\right)\neq0$ . If the degree of $\mathrm{P}(x)$ is less than the degree of $\mathbb{Q}(x)$ , then the rational function is called proper, otherwise, it is called improper. The improper rational functions can be reduced to the proper rational functions by long division process. Thus, if $\frac{\mathbf{P}(x)}{\mathbf{Q}(x)}$ is improper, then $\frac{\mathrm{P}(x)}{\mathrm{Q}(x)}=\mathrm{T}(x)+\frac{\mathrm{P}_{1}(x)}{\mathrm{Q}(x)}$

where $\mathrm{T}(x)$ is a polynomial in x and $\left\{\frac{\mathrm{P}_{1}\left(x\right)}{\mathrm{Q}(x)}\right.}$ is a proper rational function. As we know

how to integrate polynomials, the integration of any rational function is reduced o the integration of a proper rational function.The rational functions which we shall consider here for integration purposes will be those whose denominators can be factorised into linear and quadratic factors. Assume that we want to evaluate $\int_{\frac{\mathrm{P}(x)}{\mathrm{Q}(x)}d x}^{\mathrm{P}(x)}\mathrm{d}x,\mathrm{w h e r e}\frac{\mathrm{P}(x)}{\mathrm{Q}(x)}$

is proper rational function. It is always possible to write the integrand as a sum of simpler rational functions by a method called partial fraction decomposition. After this,theintegrainanbearid utasily uinge ady known method.The flowig Table 7.2 indicates the types of simpler partial fractions that are to be associated with various kind of rational functions.

<div style="text-align: center;">Table 7.2</div>

<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>S.No.</td><td>Form of the rational function</td><td>Form of the partial fraction</td></tr><tr><td>1.</td><td>$\frac{px+q}{\left(x-a\right)\left(x-b\right)},a\ne b$</td><td>$\overline{\frac{\mathbf{A}}{x-a}+\frac{\mathbf{B}}{x-b}}$</td></tr><tr><td rowspan="3">2.</td><td></td><td></td></tr><tr><td>$\frac{p x+q}{(x-a)^{2}}$</td><td>$\frac{\mathbf{A}}{x-a}+\frac{\mathbf{B}}{\left(x-a\right)^{2}}$</td></tr><tr><td>$\frac{px^{2}+qx+r}{}$</td><td></td></tr><tr><td rowspan="2">3.</td><td>$(x-a)(x-b)(x-c)$</td><td>${\frac{\mathbf{A}}{x-a}}+{\frac{\mathbf{B}}{x-b}}+{\frac{\mathbf{C}}{x-c}}$</td></tr><tr><td></td><td></td></tr><tr><td rowspan="2">4.</td><td>$\frac{p x^{2}+q x+r}{\left(x-a\right)^{2}\left(x-b\right)}$</td><td>$\left[{\frac{\mathbf{A}}{x-a}}+{\frac{\mathbf{B}}{\left(x-a\right)^{2}}}+{\frac{\mathbf{C}}{x-b}}\right]$</td></tr><tr><td></td><td></td></tr><tr><td rowspan="2">5.</td><td>$\frac{p x^{2}+q x+r}{(x-a)(x^{2}+b x+c)}$</td><td>${\frac{\mathbf{A}}{x-a}}+{\frac{\mathbf{B}x+\mathbf{C}}{x^{2}+b x+c}},$</td></tr><tr><td>where cannot be factorised further $x^{2}+b x+c$</td><td></td></tr></tbody></table></body></html></div>

In the above table, A, B and C are real numbers to be determined suitably.

Example 11 Find $\int{\frac{d x}{\left(x+1\right)\left(x+2\right)}}$

Solution The integrand is a proper rational function. Therefore, by using the form of partial fraction [Table 7.2 (i)], we write

$$

\frac{1}{\left(x+1\right)\left(x+2\right)}=\frac{A}{x+1}+\frac{B}{x+2}

$$

where, real numbers A and B are to be determined suitably. This gives

$$

1=\mathrm{A}(x+2)+\mathrm{B}(x+1).

$$

Equating the coefficients of x and the constant term, we get

$$

\mathbf{A}+\mathbf{B}=0

$$

and

$$

2\mathrm{A}+\mathrm{B}=1

$$

Solving these equations, we get $A=1and B=-1$

Thus, the integrand is given by

$$

\frac{1}{(x+1)(x+2)}=\frac{1}{x+1}+\frac{-1}{x+2}

$$

Therefore,

$$

\begin{aligned}\int\frac{dx}{(x+1)(x+2)}&=\int\frac{dx}{x+1}-\int\frac{dx}{x+2}\\&=\int\log|x+1|-\log|x+2|+C\\&=\int\log\left|\frac{x+1}{x+2}\right|+C\end{aligned}

$$

Remark The equation (1) above is an identity, i.e. a statement true for all (permissible)values of x. Some authors use the symbol $ ``\equiv''$ to indicate that the statement is an identity and use the symbol $ ``=''$ to indicate that the statement is an equation, i.e., to indicate that the statement is true only for certain values of x.

Example 12 Find $\int_{\frac{x^2+1}{x^2-5x+6}}^{\frac{x^2+1}{x^2-5x+6}}dx$

Solution Here the integrand $\frac{x^{2}+1}{x^{2}-5x+6}$ is not proper rational function, so we divide $x^{2}+1by x^{2}-5x+6$ and find that

Let

So that

$$

\frac{x^{2}+1}{x^{2}-5x+6}=1+\frac{5x-5}{x^{2}-5x+6}=1+\frac{5x-5}{(x-2)(x-3)}

$$

Equati $\mathrm{A}+\mathrm{B}=5$ and $3\bar{\mathrm{A}}+2\bar{\mathrm{B}}=5$ . Solving these equations, we get $\mathrm{A}=-5$ and $\mathbb{B}=10$

Thus,

Therefore,

Example 13 Find $\begin{aligned}\frac{x^{2}+1}{x^{2}-5x+6}&=1-\frac{5}{x-2}+\frac{10}{x-3}\\int\frac{x^{2}+1}{x^{2}-5x+6}dx&=\int dx-5\int\frac{1}{x-2}dx+10\int\frac{dx}{x-3}\\&=x-5\log|x-2|+10\log|x-3|+C.\\int\frac{3x-2}{(x+1)^{2}(x+3)}dx\end{aligned}$

$$

\begin{aligned}\frac{x^{2}+1}{x^{2}-5x+6}&=1-\frac{5}{x-2}+\frac{10}{x-3}\\int\frac{x^{2}+1}{x^{2}-5x+6}dx&=\int dx-5\int\frac{1}{x-2}dx+10\int\frac{dx}{x-3}\\&=x-5\log|x-2|+10\log|x-3|+C.\\int\frac{3x-2}{(x+1)^{2}(x+3)}dx\end{aligned}

$$

Solution The integrand is of the type as given in Table 7.2 (4). We write

So that

$$

\left\{\begin{aligned}\frac{3x-2}{{(x+1)}^{2}(x+3)}&=\frac{\mathbf{A}}{x+1}+\frac{\mathbf{B}}{{(x+1)}^{2}}+\frac{\mathbf{C}}{x+3}\\ 3x-2&=\mathbf{A}(x+1)(x+3)+\mathbf{B}(x+3)+\mathbf{C}(x+1)^{2}\\ &=\mathbf{A}(x^{2}+4x+3)+\mathbf{B}(x+3)+\mathbf{C}(x^{2}+2x+1)\end{aligned}\right.}

$$

Comparing coefficient of $x^{2}$ ,x and constant term on both sides, we get $\mathrm{A}+\mathrm{C}=0,\stackrel{\sim}{4\mathrm{A}+\mathrm{B}+2\mathrm{C}}=3$ and $3\mathrm{A}+3\mathrm{B}+\mathrm{C}=-2$ . Solving these equations, we get $A=\frac{11}{4},B=\frac{-5}{2}\ and\ C=\frac{-11}{4}$ . Thus the integrand is given by

Therefore,

$$

\begin{aligned}\frac{3x-2}{\left(x+1\right)^{2}\left(x+3\right)}&=\frac{11}{4\left(x+1\right)}-\frac{5}{2\left(x+1\right)^{2}}-\frac{11}{4\left(x+3\right)}\\int\frac{3x-2}{\left(x+1\right)^{2}\left(x+3\right)}&=\frac{11}{4}\int\frac{dx}{x+1}-\frac{5}{2}\int\frac{dx}{\left(x+1\right)^{2}}-\frac{11}{4}\int\frac{dx}{x+3}\\&=\frac{11}{4}\log\left|x+1\right|+\frac{5}{2\left(x+1\right)}-\frac{11}{4}\log\left|x+3\right|+C\\&=\frac{11}{4}\log\left|\frac{x+1}{x+3}\right|+\frac{5}{2\left(x+1\right)}+C\end{aligned}

$$

Example 14 Find $\int_{\frac{x^{2}}{\left(x^{2}+1\right)\left(x^{2}+4\right)}}^{}dx$

SolutionConsider $\frac{x^{2}}{(x^{2}+1)(x^{2}+4)}\mathrm{a n d}\mathrm{p u t}x^{2}=y.$

Then

$$

\frac{x^{2}}{(x^{2}+1)(x^{2}+4)}=\frac{y}{(y+1)(y+4)}

$$

Write

So that

$$

\left\{\begin{aligned}{\frac{y}{(y+1)(y+4)}=}&{{}~\frac{\mathbf{A}}{y+1}+\frac{\mathbf{B}}{y+4}}\\ {y=}&{{}~\mathbf{A}~(y+4)+\mathbf{B}~(y+1)}\end{aligned}\right.}

$$

Comparing coefficients of y and constant terms on both sides, we get $\mathbf{A}+\mathbf{B}=1$ and $4\mathrm{A}+\mathrm{B}=0$ ,which give

$$

\mathrm{A}=-{\frac{1}{3}}\quad{\mathrm{a n d}}\quad\mathrm{B}={\frac{4}{3}}

$$

Thus,

$$

\frac{x^{2}}{\left(x^{2}+1\right)\left(x^{2}+4\right)}=-\frac{1}{3\left(x^{2}+1\right)}+\frac{4}{3\left(x^{2}+4\right)}

$$

Therefore,

$$

\begin{aligned}\int_{\frac{x^{2}}{(x^{2}+1)(x^{2}+4)}}^{\frac{x^{2}}{(x^{2}+1)(x^{2}+4)}}&=-\frac{1}{3}\int_{\frac{x^{2}}{x^{2}+1}}^{\frac{x^{2}}{(x^{2}+1)(x^{2}+4)}}+\frac{4}{3}\int_{\frac{x^{2}}{x^{2}+4}}^{\frac{x^{2}}{(x^{2}+4)}}\\&=-\frac{1}{3}\tan^{-1}x+\frac{4}{3}\times\frac{1}{2}\tan^{-1}\frac{x}{2}+C\\&=-\frac{1}{3}\tan^{-1}x+\frac{2}{3}\tan^{-1}\frac{x}{2}+C\end{aligned}

$$

In the above example, the substitution was made only for the partial fraction part and not for the integration part. Now, we consider an example, where the integration involves a combination of the substitution method and the partial fraction method.

Example 15 Find $\int{\frac{\left(3\sin\phi-2\right)\cos\phi}{5-\cos^{2}\phi-4\sin\phi}}d\phi$

Solution Let $y=\sin\phi$ 1

Then

$$

d y=\cos\phi d\phi 

$$

Therefore,

$$

\int\frac{(3\sin\phi-2)\cos\phi}{5-\cos^{2}\phi-4\sin\phi}d\phi=\int\frac{(3y-2)dy}{5-(1-y^{2})-4y}dy=\int\frac{3y-2}{y^{2}-4y+4}dy=\int\frac{3y-2}{(y-2)^{2}}=\int(\sin\phi)dy 

$$

Now, we write

$$

\frac{3y-2}{\left(y-2\right)^{2}}=\frac{A}{y-2}+\frac{B}{\left(y-2\right)^{2}}

$$

[by Table 7.2 (2)]

Therefore,

$$

3y-2=\mathbf{A}(y-2)+\mathbf{B}

$$

Comparing the coefficients of y and constant term, we get $A=3and B-2A=-2$ which gives $\mathrm{A}=3\mathrm{~and~B}=4$

Therefore, the required integral is given by

$$

\begin{aligned}\mathrm{I}&=\int[\frac{3}{y-2}+\frac{4}{\left(y-2\right)^{2}}]d y=3\int\frac{d y}{y-2}+4\int\frac{d y}{\left(y-2\right)^{2}}\\&=3\log\left|y-2\right|+4\left(-\frac{1}{y-2}\right)+\mathbf{C}\\&=3\log\left|\sin\phi-2\right|+\frac{4}{2-\sin\phi}+\mathbf{C}\\&=3\log\left(2-\sin\phi\right)+\frac{4}{2-\sin\phi}+\mathbf{C}(\mathrm{s i n c e},2-\sin\phi\mathrm{i s~a l w a y s~p o s i t i v e})\\ \end{aligned}

$$

Example 16 Find $\int_{\frac{x^2+x+1}{(x+2)(x^2+1)}}^{\frac{x^2+x+1}{(x+2)(x^2+1)}}$

Solution Theintegrand i properrational function.Decompose therational function into partial fraction [Table 2.2(5)]. Write

Therefore,

$$

\begin{aligned}\frac{x^{2}+x+1}{\left(x^{2}+1\right)\left(x+2\right)}&=\frac{\mathbf{A}}{x+2}+\frac{\mathbf{B}x+\mathbf{C}}{\left(x^{2}+1\right)}\\x^{2}+x+1&=\mathbf{A}\left(x^{2}+1\right)+(\mathbf{B}x+\mathbf{C})\left(x+2\right)\end{aligned}

$$

Equating the coefientsofo $x^{2},x$ and of constant term of both sides, we get $A+B=1,2B+C=1\ and\ A+2C=1$ . Solving these equations, we get

$$

A=\frac{3}{5},B=\frac{2}{5}and C=\frac{1}{5}

$$

Thus, the integrand is given by

$$

\frac{x^{2}+x+1}{\left(x^{2}+1\right)\left(x+2\right)}=\frac{3}{5\left(x+2\right)}+\frac{\frac{2}{5}x+\frac{1}{5}}{x^{2}+1}=\frac{3}{5\left(x+2\right)}+\frac{1}{5}\left(\frac{2x+1}{x^{2}+1}\right)

$$

Therefore,

$$

\begin{aligned}\int\frac{x^{2}+x+1}{\left(x^{2}+1\right)(x+2)}dx&=\frac{3}{5}\int\frac{dx}{x+2}+\frac{1}{5}\int\frac{2x}{x^{2}+1}dx+\frac{1}{5}\int\frac{1}{x^{2}+1}dx\\&=\frac{3}{5}\log\left|x+2\right|+\frac{1}{5}\log\left|x^{2}+1\right|+\frac{1}{5}\tan^{-1}x+C.\end{aligned}

$$

### EXERCISE 7.5

Integrate the rational functions in Exercises 1 to 21.

$$

\begin{aligned}&1\text{.}\quad\frac{x}{\left(x+1\right)\left(x+2\right)}\quad&2\text{.}\quad\frac{1}{x^{2}-9}\quad&3\text{.}\quad\frac{3x-1}{\left(x-1\right)\left(x-2\right)\left(x-3\right)}\\&4\text{.}\quad\frac{x}{\left(x-1\right)\left(x-2\right)\left(x-3\right)}\quad&5\text{.}\quad\frac{2x}{x^{2}+3x+2}\quad&6\text{.}\quad\frac{1-x^{2}}{x\left(1-2x\right)}\\&7\text{.}\quad\frac{x}{\left(x^{2}+1\right)\left(x-1\right)}\quad&8\text{.}\quad\frac{x}{\left(x-1\right)^{2}\left(x+2\right)}\quad&9\text{.}\quad\frac{3x+5}{x^{3}-x^{2}-x+1}\\&10\text{.}\quad\frac{2x-3}{\left(x^{2}-1\right)\left(2x+3\right)}\quad&11\text{.}\quad\frac{5x}{\left(x+1\right)\left(x^{2}-4\right)}\quad&12\text{.}\quad\frac{x^{3}+x+1}{x^{2}-1}\\&13\text{.}\quad\frac{2}{\left(1-x\right)\left(1+x^{2}\right)}\quad&14\text{.}\quad\frac{3x-1}{\left(x+2\right)^{2}}\quad&15\text{.}\quad\frac{1}{x^{4}-1}\end{aligned}

$$

16.$\frac{1}{x\left(x^{n}+1\right)}$ [Hint: multiply numerator and denominator by $x^{n-1}\mathrm{a n d}\mathrm{p u t}x^{n}=t$

17.

$$

{\frac{\cos x}{\left(1-\sin x\right)\left(2-\sin x\right)}}\quad{\mathrm{[H i n t:P u t~s i n~}}x=t{\mathrm{]}}

$$

18.

$$

\frac{\left(x^{2}+1\right)\left(x^{2}+2\right)}{\left(x^{2}+3\right)\left(x^{2}+4\right)}\quad 且 \quad\frac{2x}{\left(x^{2}+1\right)\left(x^{2}+3\right)}\quad 且 \quad\frac{1}{x\left(x^{4}-1\right)}

$$

21.$\frac{1}{(e^{x}-1)}\left[\mathrm{H i n t}:\mathrm{P u t}\;e^{x}=t\right]$

Choose3

22. EM $\int_{\frac{x}{(x-1)(x-2)}}^{\frac{x}{(x-1)(x-2)}}$ E0equals

(A)

$$

\log\left|{\frac{(x-1)^{2}}{x-2}}\right|+C 

$$

(B)

$$

\log\left|{\frac{(x-2)^{2}}{x-1}}\right|+\mathbf{C}

$$

(C)

$$

\log\left|\left(\frac{x-1}{x-2}\right)^2\right|+C 

$$

(D)

$$

\log\left|(x-1)(x-2)\right|+C 

$$

23.$\int{\frac{d x}{x(x^{2}+1)}}{\mathrm{~e q u a l s}}$

$$

\begin{array}{l}{\mathrm{(A)}\log|x|-\displaystyle\frac{1}{2}\log(x^{2}+1)+\mathrm{C}\quad\mathrm{(B)}\log|x|+\displaystyle\frac{1}{2}\log(x^{2}+1)+\mathrm{C}}\\ {\mathrm{(C)}-\log|x|+\displaystyle\frac{1}{2}\log(x^{2}+1)+\mathrm{C}\quad\mathrm{(D)}\displaystyle\frac{1}{2}\log|x|+\log(x^{2}+1)+\mathrm{C}.}\end{array}7.6 Integration by Parts 

$$

### 7.6 Integration by Parts

In this section, we describe one more method of integration, that is found quite useful in integrating products of functions._e

the product rule of differentiation, we have

$\frac{d}{d x}(u v)=u\frac{d v}{d x}+v\frac{d u}{d x}$ Integrating both sides, we get

$$

\frac{d}{d x}(u v)=u\frac{d v}{d x}+v\frac{d u}{d x}Integrating both sides, we get 

$$

or

Let

$$

{\begin{aligned}{u v}&{{}=\int u{\frac{d v}{d x}}d x+\int v{\frac{d u}{d x}}d x}\\ {\int u{\frac{d v}{d x}}d x}&{{}=u v-\int v{\frac{d u}{d x}}d x}\\ {u}&{{}=f(x){\mathrm{~a n d~}}{\frac{d v}{d x}}{=}{\mathrm{~g}}(x).{\mathrm{~T h e n~}}}\\ {{\frac{d u}{d x}}}&{{}=f^{\prime}(x){\mathrm{~a n d~}}v=\int g(x)d x}\end{aligned}}

$$

Therefore, expression (1) can be rewritten as

i.e.,

$$

\begin{aligned}&\int f(x)g(x)dx=f(x)\int g(x)dx-\int[\int g(x)dx]f'(x)dx\\ &\int f(x)g(x)dx=f(x)\int g'(x)dx-\int[f'(x)\int g(x)dx]dx\\ \end{aligned}

$$

If we takef as the first function and g as the second function, then this formula may be stated as follows:

"The integral of the product of two functions = (first function) × (integral of the second function) –Integral of [(diferential coefficient of the first function)× (integral of the second function)]"

Example 17 Find $\int x\cos x dx$

Solution Put $f(x)=x$ :(first function) and $g(x)=\cos x$ (second function).

Then, integration by parts gives

$$

\begin{aligned}\int\int x\cos x dx=&x\int\cos x dx-\int[\frac{d}{dx}(x)\int\cos x dx]dx\\=&x\sin x-\int\sin x dx=x\sin x+\cos x+C.\end{aligned}

$$

Suppose, we take

$$

f(x)=\cos x{\mathrm{~a n d~}}g\left(x\right)=x.{\mathrm{~T h e n~}}

$$

$$

\begin{aligned}\int\int x\cos x dx&=\cos x\int x dx-\int[\frac{d}{dx}(\cos x)\int x dx]dx\\&=(\cos x)\frac{x^2}{2}+\int\sin x\frac{x^2}{2}dx\end{aligned}

$$

Thus, it shows that the integral $\int x\cos x$ : dx is reduced to the comparatively more complicated integral having more power of x. Therefore, the proper choice of the first function and the second function is significant.

## Remarks

(i) It is worth mentioning that integration by parts is not applicable to product of functions in all cases. For instance, the method does not work for $\int{\sqrt{x}}\sin x d x$ The reason is that there does not exist any function whose derivative is $\left[{\sqrt{x}}\right.]$ sin x.

(ii) Observe that while finding the integral of the second function, we did not add any constant of integration. If we write the integral of the second function cos x as sin $x+k$ where k is any constant, then

$$

\begin{aligned}\int x\cos x dx&=x(\sin x+k)-\int(\sin x+k)dx\\&=x(\sin x+k)-\int(\sin x dx-\int k dx\\&=x(\sin x+k)-\cos x-kx+C=x\sin x+\cos x+C\end{aligned}This shows thatadding a constant to the integralof the second function is )

$$

This shows thatadding a constant to the integralof the second function is superfluous so far as the final result is concerned while aplying the method of integration by parts.

(i)Uually, ii of mli,e t as te first function. However, in cases where other function is inverse trigonometric function or logarithmic function, then we take them as first function.

## Example 18 Find $\int\log x d x$

Solution To start with, we are unableto guess a function whose derivativeis log. W take log x as thefirst function and theconstant function 1 as the second functio. Then,the integral of the second function is .

Hence,

$$

\begin{align*}\int\int(\log x.1)dx=&\log x\int1dx-\int[\frac{d}{dx}(\log x)\int1dx]dx\\=&(\log x)\cdot x-\int\frac{1}{x}x dx=x\log x-x+C.\end{align*}

$$

Example 19 Find $\int x e^{x}dx$

Solution Takeirst functionas and econdfunction as $e^{x}$ The integ of e o function is $e^{x}$ .

Therefore,

$$

\int x e^{x}dx=x e^{x}-\int1\cdot e^{x}dx=x e^{x}-e^{x}+C.

$$

Example 20 Find $\int_{\frac{x\sin^{-1}x}{\sqrt{1-x^2}}}^{\frac{x\sin^{-1}x}{\sqrt{1-x^2}}}dx$

Solution Let first function be sin $^{-1}x$ and second function be $\frac{x}{\sqrt{1-x^{2}}}$

First we find the integral of the second function, i.e.,$\int_{\frac{x dx}{\sqrt{1-x^2}}}^{\frac{x dx}{\sqrt{1-x^2}}}$

Put $t=1-x^{2}$ .Then $dt=-2x\ dx$

Therefore,

$$

\int\frac{x dx}{\sqrt{1-x^{2}}}=-\frac{1}{2}\int\frac{dt}{\sqrt{t}}=-\sqrt{t}=-\sqrt{1-x^{2}}

$$

Hence,

$$

\begin{aligned}\int\frac{x\sin^{-1}x}{\sqrt{1-x^2}}dx&=\left(\sin^{-1}x\right)\left(-\sqrt{1-x^2}\right)-\int\frac{1}{\sqrt{1-x^2}}\left(-\sqrt{1-x^2}\right)dx\\&=-\sqrt{1-x^2}\sin^{-1}x+x+C=x-\sqrt{1-x^2}\sin^{-1}x+C.\end{aligned}

$$

Alternatively, this integral can also be worked out by making substitution sin $^{-1}x=\theta$ and then integrating by parts.

Example 21 Find $\int e^{x}\sin x dx$

Solution Take $e^{x}$ as the firstunctionandin as cond unctionThe,integrating by parts, we have

$$

\int\mathrm{I}=\int e^{x}\sin x dx=e^{x}\left(-\cos x\right)+\int e^{x}\cos x dx 

$$

Taking $e^{x}$ a $\mathrm{I}_{1}$ , we get

$$

\mathrm{I}_{1}=e^{x}\sin x-\int e^{x}\sin xdx 

$$

Substituting the value of $\mathrm{I}_{\mathrm{r}}$ in (1), we get

Hence,

$$

Substituting the value of in (1), we get 
\begin{aligned}&\mathrm{I}=-e^{x}\cos x+e^{x}\sin x-\mathrm{I}\quad\mathrm{or}\quad2\mathrm{I}=e^{x}\quad(\sin x-\cos x)\\ &\mathrm{I}=\int e^{x}\sin x dx=\frac{e^{x}}{2}(\sin x-\cos x)+\mathrm{C}\\ \end{aligned}

$$

Alternativl, oveil a obermid ki i et fction and the second function.$e^{x}$

7. 6.1 Integral of the type $\int e^{x}\left[f(x)+f^{'}(x)\right]dx$

We have

$$

\begin{aligned}\mathrm{I}&=\int e^{x}\left[f(x)+f^{\prime}(x)\right]dx=\int e^{x}f(x)dx+\int e^{x}f^{\prime}(x)dx\\&=\int\int e^{x}f^{\prime}(x)dx,\quad where\mathrm{I}_{1}=\int e^{x}f(x)dx\end{aligned}

$$

Taking $f(x)$ and $e^{x}$ al $\mathrm{I}_{\mathrm{~1~}}$ and integrating it by parts, we have $\mathrm{I}_{1}=f\left(x\right)e^{x}-\int f^{\prime}\left(x\right)e^{x}dx+\mathbf{C}$

Substituting $\mathrm{I}_{\mathrm{r}}$ in (1), we get

$$

\mathrm{I}=\mathrm{e}^{x}f(x)-\int f^{\prime}(x)\mathrm{e}^{x}dx+\int\mathrm{e}^{x}f^{\prime}(x)dx+\mathrm{C}=\mathrm{e}^{x}f(x)+\mathrm{C}

$$

Thus,

$$

\int e^{x}\left[f(x)+f^{\prime}(x)\right]dx=e^{x}f(x)+C 

$$

Example 22 Find (i)$\int e^{x}(\tan^{-1}x+{\frac{1}{1+x^{2}}})d x\quad({\mathrm{i i}})\int{\frac{(x^{2}+1)e^{x}}{(x+1)^{2}}}d x$

 Solution

(i) We have $\int e^{x}\left(\tan^{-1}x+\frac{1}{1+x^{2}}\right)dx$

Consider $f(x)=\tan^{-1}x$ , then $f^{\prime}(x)={\frac{1}{1+x^{2}}}$

Thus, the given integrand is of the form $e^{x}\left[f(x)+f^{\prime}(x)\right]$

Therefore,$\int e^{x}\left(\tan^{-1}x+\frac{1}{1+x^{2}}\right)dx=e^{x}\tan^{-1}x+C$

(i) We have $\int\frac{\left(x^{2}+1\right)e^{x}}{\left(x+1\right)^{2}}dx=\int e^{x}\left[\frac{x^{2}-1+1+1}{\left(x+1\right)^{2}}\right]dx$

$$

\int e^{x}\left[\frac{x^{2}-1}{(x+1)^{2}}+\frac{2}{(x+1)^{2}}\right]dx=\int e^{x}\left[\frac{x-1}{x+1}+\frac{2}{(x+1)^{2}}\right]dx 

$$

Consider $f(x)=\frac{x-1}{x+1},\quad then\quad f^{\prime}(x)=\frac{2}{(x+1)^2}$

Thus, the given integrand is of the form $e^{x}\left[f(x)+f^{\prime}(x)\right]$ |

Therefore,$\int\frac{x^{2}+1}{(x+1)^{2}}e^{x}dx=\frac{x-1}{x+1}e^{x}+C$

### EXERCISE 7.6

Integrate the functions in Exercises 1 to 22.

1. x sin x 2.$x\;\mathrm{s i n}\;3x$ 3.$x^{2}\ e^{x}$ 4.$x\log x$

5.$x\log2x$ 6.$x^{2}\log x$ 7.$x\sin^{-1}x$ 8.$x\tan^{-1}$ x

9.$x\cos^{-1}$ x 10.$(\sin^{-1}x)^2$ 11.$\frac{x\cos^{-1}x}{\sqrt{1-x^{2}}}$ 12.$\sec^{2}x$

13.$\tan^{-1}x$ 14.$x\;(\log x)^{2}$ 15.$(x^{2}+1)\log x$

$$

\begin{aligned}&17_e^{x}\left(\sin x+\cos x\right)\quad17_\frac{x\ e^{x}}{\left(1+x\right)^{2}}\quad18_\ e^{x}\left(\frac{1+\sin x}{1+\cos x}\right)\\ &21_e^{x}\left(\frac{1}{x}-\frac{1}{x^{2}}\right)\quad20_\frac{\left(x-3\right)e^{x}}{\left(x-1\right)^{3}}\quad21_e^{2x}\sin x\\ &32_\sin^{-1}\left(\frac{2x}{1+x^{2}}\right)\\ \end{aligned}

$$

Choose the correct answer in Exercises 23 and 24.

23.$\int x^{2}e^{x^{3}}$ dx equals

(A)

$$

\left[\frac{1}{3}e^{x^3}+\mathbf{C}\right.]

$$

(B)

$$

\left[\frac{1}{3}e^{x^2}+\mathbf{C}\right.]

$$

(C)

$$

\left\{\frac{1}{2}e^{x^3}+\mathbf{C}\right\}

$$

(D)

$$

\frac{1}{2}e^{x^{2}}+\mathbf{C}

$$

24.$\int e^{x}\sec x\left(1+\tan x\right)$ dx equals

(A)$e^{x}\cos x+\mathbf{C}$ (B)$e^{x}\;{\mathrm{s e c}}\;x+\mathbf{C}$ (C)$e^{x}\sin x+\mathbf{C}$ (D)$e^{x}\tan x+\mathbf{C}$

#### 7.6.2 Integrals of somemore types

Here, we discuss some special types of standard integrals based on the technique of integration by parts :

$$

(\mathrm{i})\quad\int\sqrt[]{x^{2}-a^{2}}~d x\quad(\mathrm{i i})\quad\int\sqrt[]{x^{2}+a^{2}}~d x\quad(\mathrm{i i i})\quad\int\sqrt[]{a^{2}-x^{2}}~d x 

$$

(i) Let

$$

\mathbf{I}=\int\sqrt{x^{2}-a^{2}}dx 

$$

Taking constant function 1 as the second function and integrating by parts, we have

$$

\begin{aligned}\mathrm{I}=&x\sqrt{x^2-a^2}-\int\frac{1}{2}\frac{2x}{\sqrt{x^2-a^2}}x dx\\=&x\sqrt{x^2-a^2}-\int\frac{x^2}{\sqrt{x^2-a^2}}dx=x\sqrt{x^2-a^2}-\int\frac{x^2-a^2+a^2}{\sqrt{x^2-a^2}}dx.\end{aligned}

$$

or

or

$$

\begin{aligned}=&x\sqrt{x^{2}-a^{2}}-\int\sqrt{x^{2}-a^{2}}\ dx-a^{2}\int\frac{dx}{\sqrt{x^{2}-a^{2}}}\\=&x\sqrt{x^{2}-a^{2}}-\mathrm{I}-a^{2}\int\frac{dx}{\sqrt{x^{2}-a^{2}}}\\2\mathrm{I}=&x\sqrt{x^{2}-a^{2}}-a^{2}\int\frac{dx}{\sqrt{x^{2}-a^{2}}}\\mathrm{I}=&\int\sqrt{x^{2}-a^{2}}\ dx=\left.\frac{x}{2}\sqrt{x^{2}-a^{2}}-\frac{a^{2}}{2}\log\left|x+\sqrt{x^{2}-a^{2}}\right.\right|+C\end{aligned}Similarly, integrating other two integralsby parts taking constant function  a th 

$$

Similarly, integrating other two integralsby parts taking constant function a th second function, we get

(ii)

(i)

$$

\begin{aligned}\int\sqrt{x^{2}+a^{2}}dx&=\frac{1}{2}x\sqrt{x^{2}+a^{2}}+\frac{a^{2}}{2}\log\left|x+\sqrt{x^{2}+a^{2}}\right|+C\\int\sqrt{a^{2}-x^{2}}dx&=\frac{1}{2}x\sqrt{a^{2}-x^{2}}+\frac{a^{2}}{2}\sin^{-1}\frac{x}{a}+C\end{aligned}

$$

Alternatively, integrals (i), (ii) and (ii) can also be found by making trigonometric substitution $x=a$ secθ in $(\mathrm{i}),x=a$ tanθ in (ii) and $x=a$ sin θ in (iii) respectively.

Example 23 Find $\int_{}\sqrt{x^{2}+2x+5}dx$

Solution Note that

$$

\begin{aligned}\int&\sqrt[3]{x^{2}+2x+5}dx=\int\sqrt[3]{(x+1)^{2}+4}dx\\ \text{Put}x+1=y,&\text{so that}dx=dy.\text{Then}\\ \int&\sqrt[3]{x^{2}+2x+5}dx=\int\sqrt[3]{y^{2}+2^{2}}dy\\ &=\frac{1}{2}y\sqrt{y^{2}+4}+\frac{4}{2}\log\left|y+\sqrt{y^{2}+4}\right|+C\quad\text{[using}7.6.2\text{(ii)]}\\ &=\frac{1}{2}(x+1)\sqrt{x^{2}+2x+5}+2\log\left|x+1+\sqrt{x^{2}+2x+5}\right|+C\end{aligned}

$$

Example 24 Find $\int{\sqrt{3-2x-x^{2}}}d x$

Solution Note that $\int\sqrt{3-2x-x^{2}}dx=\int\sqrt{4-(x+1)^{2}}dx$

Put $x+1=y$ so that $dx=dy$

Thus

$$

\begin{aligned}\int\sqrt{3-2x-x^{2}}dx&=\int\sqrt{4-y^{2}}dy\\&=\frac{1}{2}y\sqrt{4-y^{2}}+\frac{4}{2}\sin^{-1}\frac{y}{2}+C\quad[using7]\\&=\frac{1}{2}(x+1)\sqrt{3-2x-x^{2}}+2\sin^{-1}\left(\frac{x+1}{2}\right)+C\end{aligned} .6.2 (iii)

$$

### EXERCISE 7.7

Integrate the functions in Exercises 1 to 9.

$$

\begin{array}{l}\underbrace{\sqrt[3]{4-x^{2}}}_{1\cdot\quad\sqrt{4-x^{2}}}\\underbrace{\sqrt[4]{x^{2}+4x+1}}_{4\cdot\quad\sqrt{x^{2}+4x+1}}\\underbrace{7\cdot\quad\sqrt{1+3x-x^{2}}}_{9\cdot\quad\sqrt{x^{2}+3x}}\\end{array}\quad\underbrace{\sqrt[2]{1-4x^{2}}}_{5\cdot\quad\sqrt{1-4x-x^{2}}}\quad\underbrace{\sqrt[3]{\cdot\sqrt{x^{2}+4x+6}}}_{6\cdot\quad\sqrt{x^{2}+4x-5}}

$$

Choose the correct answer in Exercises 10 to 11.

10.$\int\sqrt{1+x^{2}}$ dx is equal to

(A)

$$

\left[\frac{x}{2}\sqrt{1+x^2}+\frac{1}{2}\log\left|\left(x+\sqrt{1+x^2}\right)\right|+C\right]

$$

(B)

$$

\left[{\frac{2}{3}}(1+x^{2})^{\frac{3}{2}}+\mathbf{C}\right]

$$

(C)

$$

{\frac{2}{3}}x(1+x^{2})^{\frac{3}{2}}+\mathbf{C}

$$

(D)

$$

\left[\frac{x^{2}}{2}\sqrt{1+x^{2}}+\frac{1}{2}x^{2}\log\left|x+\sqrt{1+x^{2}}\right|+C\right]

$$

11.$\int\sqrt{x^{2}-8x+7}dx is equal to$

$$

\begin{aligned}&\left(\mathrm{A}\right)^{\prime}\frac{1}{2}(x-4)\sqrt{x^{2}-8x+7}+9\log\left|x-4+\sqrt{x^{2}-8x+7}\right|+\mathrm{C}\\ &\left(\mathrm{B}\right)^{\prime}\frac{1}{2}(x+4)\sqrt{x^{2}-8x+7}+9\log\left|x+4+\sqrt{x^{2}-8x+7}\right|+\mathrm{C}\\ &\left(\mathrm{C}\right)^{\prime}\frac{1}{2}(x-4)\sqrt{x^{2}-8x+7}-3\sqrt{2}\log\left|x-4+\sqrt{x^{2}-8x+7}\right|+\mathrm{C}\\ &\left(\mathrm{D}\right)^{\prime}\frac{1}{2}(x-4)\sqrt{x^{2}-8x+7}-\frac{9}{2}\log\left|x-4+\sqrt{x^{2}-8x+7}\right|+\mathrm{C}\\ \end{aligned}

$$

### 7.7 Definite Integral

In the previous sections, we have studied about the indefinite integrals and discussed few methods of finding them including integrals of some special functions. In this section, we shall study what is called definite integral of a function. The definite integral has a unique value. A definite integral is denoted by $\int_{a}^{b}f(x)dx$ : , where a is called the

lower limit of the integral and is called the upper limit of the integral. The definite integral is introduced either as the limit of a sum or if it has an anti derivative F in the interval [a, ], then its value is the difference between the values of F at the end points, i.e.,$\operatorname{F}(b)-\operatorname{F}(a)$ b. Here, we shall consider these two cases separately as discussed below:

#### 7.7.1 Definite integral as the limit of a sum

Let f be a continuous function defined on close interval [a, ]. Assume that all the values taken by the function are non negative, so the graph of the function is a curve above the x-axis.

The definite integral $\int_{a}^{b}f(x)$ dxis the area bounded by the curve $y=f(x)$ ,the ordinates $x=a,x=b$ ' and the x-axis. To evaluate this area, consider the region PRSQP between this curve, x-axis and the ordinates $x=a{\mathrm{~a n d~}}x=b{\mathrm{~(F i g~}}7.2{\mathrm{)}}$ "

<div style="text-align: center;"><img src="imgs/img_in_chart_box_327_922_829_1297.jpg" alt="Image" width="42%" /></div>

<div style="text-align: center;">Fig 7.2</div>

Dvid $[x_{0},x_{1}],[x_{1},x_{2}]$ + rh ,......,

$[x_{_{r-1}},x_{_{r}}],...,[x_{_{n-1}},x_{_{n}}]$ ,where $\begin{array}{r}{\stackrel{\leftrightarrow}{x_{_{0}}}=a,x_{_{1}}=a+h,x_{_{2}}=a+2h,\ldots,x_{_{r}}=a}\end{array}$

$x_{n}=b=a+n h{\mathrm{~o r~}}n={\frac{b-a}{h}}$ • We note that as $n\to\infty,h\to0$

The region PRSQP under consideration is the sum of n subregions, where each sub [T]$[x_{_{r-1}},x_{_r}],r=1,2,3,...,n$

From Fig 7.2, we have

area of the rectangle $\left(\mathrm{A B L C}\right)\mathrm{<a r e a}$ of the region $\left(\mathrm{ABDCA}\right)<$ area of the rectangle (ABDM)[D]a .. (1)

Evidently as $x_{r}-x_{r-1}\to0,\mathrm{i.e.,}h\to0$ all the )e all the three areas shown in(1) become ...(1)nearly equal to each other. Now we form the following sums.

$$

s_{n}=h\left[f(x_{0})+\ldots+f(x_{n-1})\right]=h\sum_{r=0}^{n-1}f(x_{r})

$$

and

$$

\mathrm{S}_{n}=h\left[f(x_{1})+f(x_{2})+\ldots+f(x_{n})\right]=h\sum_{r=1}^{n}f(x_{r})

$$

Here,$S_{n}$ and $\mathrm{S}_{n}$ doe raised over subintervals $[x_{_{r-1}},x_{_r}]\;\mathrm{f o r}\;r{=}1,2,3,{\ldots},n$ , respectively.

In view of the inequality (1) for an arbitrary subinterval $[x_{_{r-1}},x_{_r}]$ , we have

$$

s_{_n}<\mathrm{a r e a~o f~t h e~r e g i o n~P R S Q P}<\mathrm{S}_{_n} .

$$

Asi $n\rightarrow$ ∞strips become narrower and narrower, it is assumed that the limiting values of (2) and (3) are the same in both cases and the common limiting value is the required area under the curve.

Symbolically, we write

$$

\lim_{n\to\infty}S_n=\lim_{n\to\infty}s_n=area of the region PRSQP=\int_a^b f(x)dx 

$$

It follows that this area is also the limiting value of any area which is between that of the rectangles below the curve and that of the rectangles above the curve. For the sake of convenience, we shall take rectangles with height equal to that of the curve at the left hand edge of each subinterval. Thus, we rewrite (5) as

or

$$

\begin{aligned}\int_{a}^{b}f(x)dx=&\lim_{h\to0}h\left[f(a)+f(a+h)+\ldots+f(a+(n-1)h)\right]\\left[\int_{a}^{b}f(x)dx\right.=&\left.(b-a)\lim_{n\to\infty}\frac{1}{n}\left[f(a)+f(a+h)+\ldots+f(a+(n-1)h)\right]\right]\end{aligned}

$$

where

$$

h={\frac{b-a}{n}}\rightarrow0a s n\rightarrow\infty 

$$

The above expression (6) is known as the definition of definite integral as the limit of sum.

Remark The value of the definite integral of a function over any particular interval depends on the function and the interval, but not on the variable of integration that we

c t or u instead of x, we simply write the integral as $\int_{a}^{b}f(t)d t\mathrm{o r}\int_{a}^{b}f(u)$ du instead of $\int_{a}^{b}f(x)d x$ . Hence, the variable of integration is called a dummy variable.

Example 25 Find $\int_{0}^{2}\left(x^{2}+1\right)dx$ as the limit of a sum.

Solution By definition

$$

\begin{aligned}\int_{a}^{b}f(x)dx&=(b-a)\lim_{n\to\infty}\frac{1}{n}\left[f(a)+f(a+h)+\ldots+f(a+(n-1)h)\right],\\ where,\quad h&=\frac{b-a}{n}\end{aligned}

$$

司In this example,$a=0,b=2,f(x)=x^{2}+1,\ h=\frac{2-0}{n}=\frac{2}{n}$

Therefore,

$$

\begin{aligned}\int_{0}^{2}(x^{2}+1)dx&=\quad2\lim_{n\to\infty}\frac{1}{n}[f(0)+f(\frac{2}{n})+f(\frac{4}{n})+\ldots+f(\frac{2(n-1)}{n})]\\&=\quad2\lim_{n\to\infty}\frac{1}{n}[1+(\frac{2^{2}}{n^{2}}+1)+(\frac{4^{2}}{n^{2}}+1)+\ldots+\left(\frac{(2n-2)^{2}}{n^{2}}+1\right)]\\&=\quad2\lim_{n\to\infty}\frac{1}{n}[\underbrace{(1+1+\ldots+1)}_{n\leq terms}+\frac{1}{n^{2}}\left(2^{2}+4^{2}+\ldots+(2n-2)^{2}\right)]\\&=\quad2\lim_{n\to\infty}\frac{1}{n}[n+\frac{2^{2}}{n^{2}}\left(1^{2}+2^{2}+\ldots+(n-1)^{2}\right)]\\&=\quad2\lim_{n\to\infty}\frac{1}{n}[n+\frac{4}{n^{2}}\frac{(n-1)n\left(2n-1\right)}{6}]\\&=\quad2\lim_{n\to\infty}\frac{1}{n}[n+\frac{2}{3}\frac{(n-1)\ (2n-1)}{n}]\\&=\quad2\lim_{n\to\infty}\frac{1}{n}[1+\frac{2}{3}(1-\frac{1}{n})\ (2-\frac{1}{n})]=\quad2\ [1+\frac{4}{3}]=\frac{14}{3}\end{aligned}

$$

Example 26 Evaluate $\int_{0}^{2}e^{x}$ dx as the limit of a sum.

 Solution By definition

$$

\int_{0}^{2}e^{x}dx=(2-0)\lim_{n\to\infty}\frac{1}{n}\left[e^{0}+e^{\frac{2}{n}}+e^{\frac{4}{n}}+\ldots+e^{\frac{2n-2}{n}}\right]

$$

Using the sum to n terms of a G.P., where $a=1,\;r=e^{n}$ , we have

$$

\int_{0}^{2}e^{x}dx=2\lim_{n\to\infty}\frac{1}{n}\left[\frac{e^{\frac{2n}{n}}-1}{e^{\frac{2}{n}}-1}\right]=2\lim_{n\to\infty}\frac{1}{n}\left[\frac{e^{\frac{2}{n}}-1}{e^{\frac{2}{n}}-1}\right]\\=\frac{2(e^{2}-1)}{\lim\limits_{n\to\infty}\left[\frac{e^{\frac{2}{n}}-1}{\frac{2}{n}}\right]\cdot2}=e^{2}-1\quad[\text{using}\lim_{h\to0}\frac{(e^{h}-1)}{h}=1].

$$

### EXERCISE 7.8

Evaluate the following definite integrals as limit of sums.

$$

\begin{aligned}&1\text{.}\int_{a}^{b}x dx\quad&2\text{.}\int_{0}^{5}(x+1)dx\quad&3\text{.}\int_{2}^{3}x^2dx\\&4\text{.}\int_{1}^{4}(x^2-x)dx\quad&5\text{.}\int_{-1}^{1}e^x dx\quad&6\text{.}\int_{0}^{4}(x+e^{2x})dx\end{aligned}

$$

### 7.8 Fundamental Theorem of Calculus

#### 7.8.1 Area function

We have defined $\int_{a}^{b}f(x)$ d as the area of the region bounded by the curve $y=f\left(x\right)$ the ordinates $x=a$ and $x=b$ and -axis. Let be a given point in $[a,b]$ . Then $\int_{a}^{x}f(x)$ d X′←represents the area of the light shaded region

$$

\mathbf{A}(x)

$$

<div style="text-align: center;">Fig 7.3</div>

$$

y=f(x)

$$

in Fig 7.3 [Here it is assumed that $f(x)>0\;{\mathrm{f o r}}\;x\in[a,b]$ , the assertion made below is equally true for other functions as well]. The area of this shaded region depends upon the value of x.

In other words, the area of this shaded region is a function of x. We denote this function of x by A(x). We call the function (cid $\mathrm{A}(x)$ as Area function and is given by

$$

\mathbf{A}\left(x\right)=\int_{a}^{x}{f\left(x\right)dx}

$$

Based on this definition, the two basic fundamental theorems have been given.However, we only state them as their proofs are beyond the scope of this text book.

#### 7.8.2 First fundamental theorem of integral calculus

Theorem 1Letf be acontinuous function ontheclosed interval [, ] and letA () be the area function. Then $\mathbf{A}^{\prime}(x)=f(x)$ , for all $x\in[a,b]$ 」.

#### 7.8.3 Second fundamental theorem of integral calculus

We state below an important theorem which enables us to evaluate definite integrals by making use of anti derivative.

Theorem 2 Letf be continuous function defined on the closed interval [a, ] and F be an anti derivative of f. Then $\int_{a}^{b}f(x)d x=\left[\mathbf{F}(x)\right]_{a}^{b}=\mathbf{F}(b)-\mathbf{F}(a).$

## Remarks

(i) In words, the Theorem 2 tells us that $\int_{a}^{b}f(x)dx=$ (value of the anti derivative F of f at the upper limit – value of the same anti derivative at the lower limit a).(ii)This theorem is very useful, because it gives us a method of calculating the definite integral more easily, without calculating the limit of a sum.

(ii)The crucial operation in valuating a defiititgral isthat of inding a function whose derivative is equal to the integrand. This strengthens the relationship between differentiation and integration.

(iv) In $\int{}_{a}^{b}f(x)d x$ , the functionf needs to be well defined and continuous in [a, b].

For instanc,teconiderai of deii egral $\int_{-2}^{3}x(x^{2}-1)^{\frac{1}{2}}d x$ is erroneous

since the function f expressed by $f(x)=x(x^{2}-1)^{\frac{1}{2}}$ is not defined in a portion $-1<x<1$ of the closed interval $\left[-2,3\right]$

Steps for calculating $\int_{a}^{b}f(x)dx$

(i)Find the indefinite integral $\int f(x)$ dx . Let this be $\mathrm{F}(x)$ . There is no need to keep integrationcotbauei weconsider $\mathrm{F}(x)+\mathrm{C}$ instead of f $\mathrm{F}(x)$ , we get

$$

\int_{a}^{b}f(x)dx=\left[\mathrm{F}(x)+\mathrm{C}\right]_{a}^{b}=\left[\mathrm{F}(b)+\mathrm{C}\right]-\left[\mathrm{F}(a)+\mathrm{C}\right]=\mathrm{F}(b)-\mathrm{F}(a).

$$

Thus, the arbitrary constant disappears in evaluating the value of the definite integral.

(ii) Evaluate $\mathbb{F}(b)-\mathbb{F}(a)=\left[\mathbb{F}\left(x\right)\right]_{a}^{b}$ ,which is the value of $\int{}_{a}^{b}f(x)d x$

We now consider some examples

Example 27 Evaluate the following integrals:

(i)

$$

\int_{2}^{3}x^{2}\ dx 

$$

(ii)

$$

\int_{4}^{9}{\frac{\sqrt{x}}{(30-x^{\frac{3}{2}})^{2}}}d x 

$$

(ii)

$$

\int_{1}^{2}\frac{x dx}{(x+1)(x+2)}\quad(iv)\quad\int_{0}^{\frac{\pi}{4}}\sin^32t\cos2t dt 

$$

Solution

(i)

$$

\mathrm{L e t}\;\mathrm{I}=\int_{2}^{3}x^{2}\;d x\;.\;\mathrm{S i n c e}\;\int x^{2}\;d x=\frac{x^{3}}{3}=\mathrm{F}\left(x\right),

$$

Therefore, by the second fundamental theorem, we get

$$

\mathrm{I}=\mathrm{F}\left(3\right)-\mathrm{F}\left(2\right)=\frac{27}{3}-\frac{8}{3}=\frac{19}{3}

$$

(ii) Let $\int_{1}^{9}\frac{\sqrt{x}}{\left(30-x^{\frac{3}{2}}\right)^{2}}dx$ . We first find the anti derivative of the integrand.

$$

\mathrm{P u t}^{\prime}30-x^{\frac{3}{2}}=t.\mathrm{T h e n}-\frac{3}{2}\sqrt{x}d x=d t\mathrm{o r}\sqrt{x}d x=-\frac{2}{3}d t.

$$

Thus,

$$

\int\frac{\sqrt{x}}{\left(30-x^{\frac{3}{2}}\right)^{2}}dx=-\frac{2}{3}\int\frac{dt}{t^{2}}=\frac{2}{3}\left[\frac{1}{t}\right]=\frac{2}{3}\left[\frac{1}{\left(30-x^{\frac{3}{2}}\right)}\right]=\mathrm{F}(x)

$$

Therefore, by the second fundamental theorem of calculus, we have

$$

\begin{aligned}&\mathrm{I}=\mathrm{F}(9)-\mathrm{F}(4)=\frac{2}{3}\left[\frac{1}{\left(30-x^{\frac{3}{2}}\right)}\right]_{4}^{9}\\ &=\frac{2}{3}\left[\frac{1}{\left(30-27\right)}-\frac{1}{30-8}\right]=\frac{2}{3}\left[\frac{1}{3}-\frac{1}{22}\right]=\frac{19}{99}\\ \end{aligned}

$$

(ii) Let $\int_{1}^{2}\frac{x dx}{(x+1)(x+2)}$

Using partial fraction, we get $\frac{x}{\left(x+1\right)\left(x+2\right)}=\frac{-1}{x+1}+\frac{2}{x+2}$

So

$$

\int\frac{x dx}{(x+1)(x+2)}=-\log|x+1|+2\log|x+2|=F(x)

$$

Therefore, by the second fundamental theorem of calculus, we have

$$

\begin{aligned}\mathrm{I}=&\mathrm{F}(2)-\mathrm{F}(1)=[-\log3+2\log4]-[-\log2+2\log3]\\=&-3\log3+\log2+2\log4=\log\left(\frac{32}{27}\right)\end{aligned}

$$

$$

\mathrm{Let}\mathrm{I}=\int_{0}^{\frac{\pi}{4}}\sin^32t\cos2t dt.\mathrm{Consider}\int_{0}^{\frac{\pi}{4}}2t\cos2t dt.

$$

Put sin $2t=u$ so that 2 cos 2t $dt=du$ or cos 2t $d t={\frac{\dot{1}}{2}}d u$

So

$$

\begin{aligned}\int\sin^{3}2t\cos2t dt=&\frac{1}{2}\int u^{3}du\\=&\frac{1}{8}\left[u^{4}\right]=\frac{1}{8}\sin^{4}2t=\mathrm{F}(t)\mathrm{s}\mathrm{a}\mathrm{y}.\end{aligned}

$$

Therefore, by the second fundamental theorem of integral calculus

$$

\mathrm{I}=\mathrm{F}\left(\frac{\pi}{4}\right)-\mathrm{F}(0)=\frac{1}{8}\left[\sin^{4}\frac{\pi}{2}-\sin^{4}0\right]=\frac{1}{8}

$$

### EXERCISE 7.9

Evaluate the definite integrals in Exercises 1 to 20.

1.

$$

\int_{-1}^{1}(x+1)dx\quad\int_{-2}^{3}\frac{1}{x}dx\quad\int_{-3}^{2}(4x^3-5x^2+6x+9)dx 

$$

4.$\int_{0}^{\frac{\pi}{4}}\sin2x dx\quad 在 \quad\int_{0}^{\frac{\pi}{2}}\cos2x dx\quad 在 \quad\int_{4}^{5}e^{x}dx$ 7.$\int_{0}^{\frac{\pi}{4}}\tan x d x$

8.

$$

\int_{\frac{\pi}{6}}^{\frac{\pi}{4}}\cos\csc x dx\quad\int_{0}^{1}\frac{dx}{\sqrt{1-x^2}}dx\quad\int_{0}^{1}\frac{dx}{1+x^2}dx\quad\int_{\frac{\pi}{6}}^{\frac{\pi}{4}}\frac{dx}{x^2-1}dx 

$$

12.

$$

12.\int_{0}^{\frac{\pi}{2}}\cos^{2}x\ dx=\int_{0}^{\frac{\pi}{2}}\frac{x\ dx}{x^{2}+1}=\int_{0}^{\frac{\pi}{2}}\frac{2x+3}{5x^{2}+1}\ dx=\int_{0}^{\frac{\pi}{2}}\frac{1}{5}\ dx 

$$

16.

$$

\int_{1}^{2}\frac{5x^{2}}{x^{2}+4x+3}\quad17.\quad\int_{0}^{\frac{\pi}{4}}\left(2\sec^{2}x+x^{3}+2\right)dx\quad18.\quad\int_{0}^{\pi}\left(\sin^{2}\frac{x}{2}-\cos^{2}\frac{x}{2}\right)dx 

$$

19.

$$

\int_{0}^{2}\frac{6x+3}{x^{2}+4}dx\quad\geq0\quad\int_{0}^{1}\left(x e^{x}+\sin\frac{\pi x}{4}\right)dx 

$$

Choose the correct answer in Exercises 21 and 22.

21.$\int_{1}^{\sqrt[3]{3}}\frac{dx}{1+x^{2}}$ equals

(A)$\frac{\pi}{3}$ (B)$\frac{2\pi}{3}$ (C)$\frac{\pi}{6}$ (D)$\frac{\pi}{12}$

22.$\int_{0}^{\frac{2}{3}}{\frac{d x}{4+9x^{2}}}\quad\mathrm{e q u a l s}$

(A)$\frac{\pi}{6}$ (B)$\frac{\pi}{12}$ (C)$\frac{\pi}{24}$ (D)$\frac{\pi}{4}$

### 7.9 Evaluation of Definite Integrals by Substitution

Inthe previou ns, have dicued evl hod ee inte.of substitution.

To evaluate $\int_{a}^{b}f(x)dx$ : , by substitution, the steps could be as follows:

1. Consider the integral without limits and substitute,$y=f(x)\mathrm{o r}x=g(y)$ to reduce the given integral to a known form.

2. Integrate the new integrand with respect to the new variable without mentioning the constant of integration.

3. Resubstitute for the new variable and write the answer in terms of the original variable.

4. Find the value ofanswers btaied i (3) at the ive limts of itegral and find the difference of the values at the upper and lower limits.

Note]In order to quicken this method, we can proceed as follows: After performi1,,io,ialillb t wl,so that we can perform the last step.

Let us illustrate this by examples.

Example 28 Evaluate $\int_{-1}^{1}5x^{4}{\sqrt{x^{5}+1}}d x$

Solution Put $t=x^{5}+1$ ,then $d t=5x^{4}$ d.

Therefore,

$$

\int\int5x^{4}\sqrt{x^{5}+1}\ dx=\int\sqrt{t}\ dt=\frac{2}{3}t^{\frac{3}{2}}=\frac{2}{3}(x^{5}+1)^{\frac{3}{2}}

$$

Hence,

$$

\int_{-1}^{1}5x^4\sqrt{x^5+1}dx=\frac{2}{3}\left[(x^5+1)^{\frac{3}{2}}\right]_{-1}^{1}

$$

$$

={\frac{2}{3}}\left[\left(1^{5}+1\right)^{\frac{3}{2}}-\left(\left(-1\right)^{5}+1\right)^{\frac{3}{2}}\right]

$$

$$

\frac{2}{3}\left[2^{\frac{3}{2}}-0^{\frac{3}{2}}\right]=\frac{2}{3}(2\sqrt{2})=\frac{4\sqrt{2}}{3}

$$

with new limits.

Let Note that, when $\begin{array}{r l}&{t=x^{5}+1.\mathrm{~T h e n~}d t=5x^{4}d x.}\\ &{x=-1,t=0\mathrm{~a n d~w h e n~}x=1,t=2.}\end{array}$ Thus, as x varies from –1 to 1, t varies from 0 to 2

Therefore

$$

\begin{aligned}\int_{-1}^{1}5x^{4}\sqrt{x^{5}+1}\ dx&=\int_{0}^{2}\sqrt{t}\ dt\\&=\frac{2}{3}\left[t^{\frac{3}{2}}\right]_{0}^{2}=\frac{2}{3}\left[2^{\frac{3}{2}}-0^{\frac{3}{2}}\right]=\frac{2}{3}(2\sqrt{2})=\frac{4\sqrt{2}}{3}\end{aligned}

$$

Example 29 Evaluate $\int_{0}^{1}{\frac{\tan^{-1}x}{1+x^{2}}}d x$

Solution Let $t=\tan^{-1}x$ ,then $dt=\frac{1}{1+x^{2}}$ dx . The new limits are, when $x=0,t=0$ and when $x=1,\;t=\frac{\pi}{4}$ . Thus, as x varies from 0 to 1, t varies from $0to\frac{\pi}{4}$

Therefore

$$

\int_{0}^{1}\frac{\tan^{-1}x}{1+x^2}dx=\int_{0}^{\frac{\pi}{4}}t dt\left[\frac{t^2}{2}\right]_{0}^{\frac{\pi}{4}}=\frac{1}{2}\left[\frac{\pi^2}{16}-0\right]=\frac{\pi^2}{32}

$$

### EXERCISE 7.10

Evaluate the integrals in Exercises 1 to 8 using substitution.

$$

\begin{aligned}&1.\quad\int_{0}^{1}\frac{x}{x^{2}+1}dx\quad2.\quad\int_{0}^{\frac{\pi}{2}}\sqrt[3]{\sin\phi}\cos^{5}\phi d\phi\quad3.\quad\int_{0}^{1}\sin^{-1}\left(\frac{2x}{1+x^{2}}\right)dx\\&24.\quad\int_{0}^{2}x\sqrt{x+2}\quad(Put x+2=t^{2})\quad5.\quad\int_{0}^{\frac{\pi}{2}}\frac{\sin x}{1+\cos^{2}x}dx\\&6.\quad\int_{0}^{2}\frac{dx}{x+4-x^{2}}\quad7.\quad\int_{-1}^{1}\frac{dx}{x^{2}+2x+5}\quad8.\quad\int_{1}^{2}\left(\frac{1}{x}-\frac{1}{2x^{2}}\right)e^{2x}dx\\ \end{aligned}

$$

Choose the correct answer in Exercises 9 and 10.

9. The value of the integral $\int_{\frac{1}{3}}^{1}\frac{(x-x^{3})^{\frac{1}{3}}}{x^{4}}d x$ EM EM is

(A)6(B)0(C)3(D)4

10.$\operatorname{I f}f(x)=\int{}_{0}^{x}t$ sint dt , then $f^{\prime}(x)$ is

(A)$\mathrm{cos}x+x\;\mathrm{sin}\;x$ (B)$x\;{\mathrm{s i n}}x$ (C)$x{\tt c o s}x$ (D)$\mathrm{sin}x+x\mathrm{cos}x$ ### 7.10 Some Properties of Definite Integrals

We list below someimportantpropertiesof definiteintgrals.These will be useful in evaluating the definite integrals more easily.

$$

\begin{aligned}\mathbf{P}_{0}:\quad\int_{a}^{b}f(x)dx=&\int_{a}^{b}f(t)dt\\mathbf{P}_{1}:\quad\int_{a}^{b}f(x)dx=&-\int_{b}^{a}f(x)dx.In particular,\int_{a}^{a}f(x)dx=0\\mathbf{P}_{2}:\quad\int_{a}^{b}f(x)dx=&\int_{a}^{c}f(x)dx+\int_{c}^{b}f(x)dx\\mathbf{P}_{3}:\quad\int_{a}^{b}f(x)dx=&\int_{a}^{b}f(a+b-x)dx\\mathbf{P}_{4}:\quad\int_{a}^{c}f(x)dx=&\int_{0}^{a}f(a-x)dx\\&(Note that\mathrm{P}_{4}is a particular case of\mathrm{P}_{3})\\mathbf{P}_{5}:\quad\int_{0}^{2a}f(x)dx=&\int_{0}^{a}f(x)dx+\int_{0}^{a}f(2a-x)dx\\mathbf{P}_{6}:\quad\int_{0}^{2a}f(x)dx=&2\int_{0}^{a}f(x)dx,if f(2a-x)=f(x)\quad and\\&0if f(2a-x)=-f(x)\\mathbf{P}_{7}:\quad(i)\int_{-a}^{a}f(x)dx=&2\int_{0}^{a}f(x)dx,if f is an even function,i.e.,if f(-x)=f(x).\\&(ii)\int_{-a}^{a}f(x)dx=0,if f is an odd function,i.e.,if f(-x)=-f(x).\end{aligned}

$$

We give the proofs of these properties one by one.

Proof of f $\mathbf{P}_{\mathbf{o}}$ It follows directly by making the substitution $x=t$

Proof of $\mathbf{P}_{\mathrm{r}}$ LtF calculus, we have $\int_{a}^{b}f(x)dx=\mathrm{F}(b)-\mathrm{F}(a)=-\left[\mathrm{F}(a)-\mathrm{F}(b)\right]=-\int_{b}^{a}f(x)dx$ Here, we observe that, if $a=b$ ,then $\int_{a}^{a}f(x)d x=0$

Proof of $\mathbf{P}_{2}$ Let Fbe anti derivative of f. Then

and

$$

\begin{aligned}&\int_{a}^{b}f(x)dx=\mathrm{F}(b)-\mathrm{F}(a)\\&\int_{a}^{c}f(x)dx=\mathrm{F}(c)-\mathrm{F}(a)\\&\int_{c}^{b}f(x)dx=\mathrm{F}(b)-\mathrm{F}(c)\\ \end{aligned}

$$

Adding (2) and (3), we get $\int_{a}^{c}f(x)dx+\int_{c}^{b}f(x)dx=F(b)-F(a)=\int_{a}^{b}f(x)dx$ This proves the property $ P_{2}\cdot$

Proof of $\mathbf{P}_{3}$ Let $t=a+b-x$ . Then $d t=-d x$ . When $x=a,t=b$ and when $x=b,t=a$ Therefore

$$

\begin{aligned}\int_{a}^{b}f(x)dx&=\int_{b}^{a}f(a+b-t)dt\\&=\int_{a}^{b}f(a+b-t)dt\quad(by\mathrm{P}_1)\\&=\int_{a}^{b}f(a+b-x)dx by\mathrm{P}_0\end{aligned}

$$

Proof of $\mathbf{P}_{4}\operatorname{Put}t=a-x$ .Then $d t=-d x$ . When $x=0,t=a$ and when $x=a,t=0$ .Now proceed as in $\mathrm{P}_{3}$ .

Proof of f $\mathbf{P}_{5}$ Using $\mathrm{P}_{2}$ , we have $\int_{0}^{2a}f(x)dx=\int_{0}^{a}f(x)dx+\int_{a}^{2a}f(x)dx$

Let

$t=2a-x$ in the second integral on the right hand side. Then

$dt=-dx.\;\;\mathrm{When}\;x=a,\;t=a$ and when $x=2a,t=0.Also x=2a-t$ Therefore, the second integral becomes

Hence

$$

\begin{aligned}&\int_{a}^{2a}f(x)dx=-\int_{a}^{0}f(2a-t)dt=\int_{0}^{a}f(2a-t)dt=\int_{0}^{a}f(2a-x)dx\\ &\int_{0}^{2a}f(x)dx=\int_{0}^{a}f(x)dx+\int_{0}^{a}f(2a-x)dx\\ \end{aligned}

$$

Proof of $\mathbf{P}_{\boldsymbol{\epsilon}}$ Using $\mathrm{P}_{5^{\circ}}$ we have $\int_{0}^{2a}f(x)dx=\int_{0}^{a}f(x)dx+\int_{0}^{a}f(2a-x)dx$

Now, if

$f(2a-x)=f(x)$ , then (1) becomes

$$

\int_{0}^{2a}f(x)dx=\int_{0}^{a}f(x)dx+\int_{0}^{a}f(x)dx=2\int_{0}^{a}f(x)dx,

$$

and if

$f(2a-x)=-f(x)$ , then (1) becomes

$$

\int_{0}^{2a}f(x)dx=\int_{0}^{a}f(x)dx-\int_{0}^{a}f(x)dx=0Proof ofUsing _, we have 

$$

Proof of $\mathbf{P}_{7}$ Using $\mathrm{P}_{2}$ , we have

Let

$$

\begin{aligned}\int_{-a}^{a}f(x)dx&=\int_{-a}^{0}f(x)dx+\int_{0}^{a}f(x)dx_{.}Then\\t&=-x in the first integral on the right hand side.\\dt&=-dx.When x=-a,t=a and when\\x&=0,t=0.Also x=-t.\end{aligned}

$$

Therefore

$$

\begin{aligned}\int_{-a}^{a}f(x)dx=&-\int_{a}^{0}f(-t)dt+\int_{0}^{a}f(x)dx\\=&\int_{0}^{a}f(-x)dx+\int_{0}^{a}f(x)dx\end{aligned}

$$

(i) Now, if f is an even function, then $f(-x)=f(x)$ TaY

$$

\int_{-a}^{a}f(x)dx=\int_{0}^{a}f(x)dx+\int_{0}^{a}f(x)dx=2\int_{0}^{a}f(x)dx 

$$

(ii) If f is an odd function, then $f(-x)=-f(x)$ and so (1) becomes

$$

\int_{-a}^{a}f(x)dx=-\int_{0}^{a}f(x)dx+\int_{0}^{a}f(x)dx=0.

$$

Example 30 Evaluate $\int_{-1}^{2}\left|x^{3}-x\right|d x$

Solution We note that $x^{3}-x\geq0\mathrm{~o n~}[-1,0]$ and $x^{3}-x\leq0$ on [0, 1] and that $x^{3}-x\geq0$ on [1,2]. So by $ P_2$ we write

$$

\begin{aligned}\int_{-1}^{2}\left|x^3-x\right|dx&=\int_{-1}^{0}(x^3-x)dx+\int_{0}^{1}-(x^3-x)dx+\int_{1}^{2}(x^3-x)dx\\&=\int_{-1}^{0}(x^3-x)dx+\int_{0}^{1}(x-x^3)dx+\int_{1}^{2}(x^3-x)dx\\&=\left[\frac{x^4}{4}-\frac{x^2}{2}\right]_{-1}^{0}+\left[\frac{x^2}{2}-\frac{x^4}{4}\right]_{0}^{1}+\left[\frac{x^4}{4}-\frac{x^2}{2}\right]_{1}^{2}\\&=-\left(\frac{1}{4}-\frac{1}{2}\right)+\left(\frac{1}{2}-\frac{1}{4}\right)+\left(4-2\right)-\left(\frac{1}{4}-\frac{1}{2}\right)\\&=-\frac{1}{4}+\frac{1}{2}+\frac{1}{2}-\frac{1}{4}+2-\frac{1}{4}+\frac{1}{2}=\frac{3}{2}-\frac{3}{4}+2=\frac{11}{4}\end{aligned}

$$

Example 31 Evaluate $$

 T

Solution We observe that $\sin^{2}x$ is an even function.Therefore, b 

$$

$$

\int_{\frac{-\pi}{4}}^{\frac{\pi}{4}}\sin^{2}x d x=2\int_{0}^{\frac{\pi}{4}}\sin^{2}x d x 

$$

$$

\begin{aligned}&\stackrel{\pi}{=}2\int_{0}^{\frac{\pi}{4}}\frac{(1-\cos2x)}{2}dx=\int_{0}^{\frac{\pi}{4}}(1-\cos2x)dx\\ &=\left[x-\frac{1}{2}\sin2x\right]_{0}^{\frac{\pi}{4}}=\left(\frac{\pi}{4}-\frac{1}{2}\sin\frac{\pi}{2}\right)-0=\frac{\pi}{4}-\frac{1}{2}\\ \end{aligned}

$$

Example 32 Evaluate $\int_{0}^{\pi}\frac{x\sin x}{1+\cos^{2}x}dx$

Solution Let $\mathrm{I}=\int_{0}^{\pi}\frac{x\sin x}{1+\cos^2x}$ dx . Then, by $ P_{4^{\circ}}$ we have

or

or

$$

\begin{aligned}I&=\int_{0}^{\pi}\frac{(\pi-x)\sin(\pi-x)dx}{1+\cos^2(\pi-x)}\\&=\int_{0}^{\pi}\frac{(\pi-x)\sin x dx}{1+\cos^2x}=\pi\int_{0}^{\pi}\frac{\sin x dx}{1+\cos^2x}-I\\2I&=\pi\int_{0}^{\pi}\frac{\sin x dx}{1+\cos^2x}\\ I&=\frac{\pi}{2}\int_{0}^{\pi}\frac{\sin x dx}{1+\cos^2x}\end{aligned}

$$

Put cos $x=t$ so that – sin x $d x=d t$ . When $x=0,t=1$ and when $x=\pi,t=-1$ Therefore,$(\mathrm{by}\mathrm{P}_1)$ we get

$$

\begin{aligned}\mathrm{II}&=\frac{-\pi}{2}\int_{1}^{-1}\frac{dt}{1+t^2}=\frac{\pi}{2}\int_{-1}^{1}\frac{dt}{1+t^2}\\&=\pi\int_{0}^{1}\frac{dt}{1+t^2}\left(\mathrm{by}\mathrm{P}_{7},\mathrm{since}\frac{1}{1+t^2}\mathrm{is even function}\right)\\&=\pi\left[\tan^{-1}t\right]_{0}^{1}=\pi\left[\tan^{-1}1-\tan^{-1}0\right]=\pi\left[\frac{\pi}{4}-0\right]=\frac{\pi^2}{4}.\\ \end{aligned}

$$

Example 33 Evaluate $\int_{-1}^{1}\sin^{5}x\cos^{4}$ x dx

Solution Let $\mathrm{I}=\int_{-1}^{1}\sin^5x\cos^4x dx.\mathrm{Let}f(x)=\sin^5x\cos^4x.\mathrm{Then}$ 1

$f\left(-x\right)=\sin^{5}\left(-x\right)\cos^{4}\left(-x\right)=-\sin^{5}x\cos^{4}x=-f\left(x\right)$ , f is an odd function.Therefore, by $\mathrm{P}_{_7}(\mathrm{ii}),\mathrm{I}=0$

Example 34 Evaluate $\int_{0}^{\frac{\pi}{2}}\frac{\sin^{4}x}{\sin^{4}x+\cos^{4}x}dx$

Solution Let $\mathrm{I}=\int_{0}^{\frac{\pi}{2}}\frac{\sin^{4}x}{\sin^{4}x+\cos^{4}x}dx$

Then, by $\mathrm{P}_{4}$

$$

\int_{0}^{\frac{\pi}{2}}\frac{\sin^4(\frac{\pi}{2}-x)}{\sin^4(\frac{\pi}{2}-x)+\cos^4(\frac{\pi}{2}-x)}dx=\int_{0}^{\frac{\pi}{2}}\frac{\cos^4x}{\cos^4x+\sin^4x}dx 

$$

Adding (1) and (2), we get

$$

2\mathrm{I}=\int_{0}^{\frac{\pi}{2}}\frac{\sin^{4}x+\cos^{4}x}{\sin^{4}x+\cos^{4}x}d x=\int_{0}^{\frac{\pi}{2}}d x=\left[x\right]_{0}^{\frac{\pi}{2}}=\frac{\pi}{2}

$$

Hence

$$

\mathrm{I}=\frac{\pi}{4}

$$

Example 35 Evaluate $\int_{\frac{\pi}{6}}^{\frac{\pi}{3}}{\frac{d x}{1+{\sqrt{\tan x}}}}$

Solution $\mathrm{Let}\mathrm{I}=\int_{\frac{\pi}{6}}^{\frac{\pi}{3}}\frac{dx}{1+\sqrt{\tan x}}=\int_{\frac{\pi}{6}}^{\frac{\pi}{3}}\frac{\sqrt{\cos x}dx}{\sqrt{\cos x}+\sqrt{\sin x}}$

Then, by $ P_{3}$

$$

\begin{aligned}\mathrm{II}&=\int_{\frac{\pi}{6}}^{\frac{\pi}{3}}\frac{\sqrt{\cos\left(\frac{\pi}{3}+\frac{\pi}{6}-x\right)}\ dx}{\sqrt{\cos\left(\frac{\pi}{3}+\frac{\pi}{6}-x\right)}+\sqrt{\sin\left(\frac{\pi}{3}+\frac{\pi}{6}-x\right)}}\\&=\int_{\frac{\pi}{6}}^{\frac{\pi}{3}}\frac{\sqrt{\sin x}}{\sqrt{\sin x}+\sqrt{\cos x}}\ dx\end{aligned}

$$

Adding (1) and (2), we get

$$

2\mathrm{I}=\int_{\frac{\pi}{6}}^{\frac{\pi}{3}}d x=\left[x\right]_{\frac{\pi}{6}}^{\frac{\pi}{3}}=\frac{\pi}{3}-\frac{\pi}{6}=\frac{\pi}{6}.\mathrm{H e n c e}^{\mathrm{\scriptsize~\cdot~}}\mathrm{I}=\frac{\pi}{12}

$$

Example 36 Evaluate $\int_{0}^{\frac{\pi}{2}}\log\sin x d x$

Solution Let $\mathrm{I}=\int_{0}^{\frac{\pi}{2}}\log\sin x d x$

Then, by $\mathrm{P}_{4}$

$$

\mathrm{I}=\int_{0}^{\frac{\pi}{2}}\log\sin\left(\frac{\pi}{2}-x\right)d x=\int_{0}^{\frac{\pi}{2}}\log\cos x d x 

$$

Adding the two values of I, we get

$$

\begin{aligned}2I&=\int_{0}^{\frac{\pi}{2}}\left(\log\sin x+\log\cos x\right)dx\\&=\int_{0}^{\frac{\pi}{2}}\left(\log\sin x\cos x+\log2-\log2\right)dx\quad(by adding and subtracting\log2)\\&=\int_{0}^{\frac{\pi}{2}}\log\sin2x dx-\int_{0}^{\frac{\pi}{2}}\log2dx\quad(Why?)\end{aligned}

$$

Put $2x=t$ in the first integral. Then $2d x=d t$ , when $x=0,t=0$ and when $x=\frac{\pi}{2}$ ,

$t=\pi.$

$$

\begin{aligned}&Therefore\quad&2I=\frac{1}{2}\int_{0}^{\pi}\log\sin t dt-\frac{\pi}{2}\log2\\&\quad=\frac{1}{2}\int_{0}^{\frac{\pi}{2}}\log\sin t dt-\frac{\pi}{2}\log2\left[by P_6as sin(\pi-t)=\sin t\right]\\&\quad=\int_{0}^{\frac{\pi}{2}}\log\sin x dx-\frac{\pi}{2}\log2(by changing variable t to x)\\&\quad=I-\frac{\pi}{2}\log2\\&\quad\int_{0}^{\frac{\pi}{2}}\log\sin x dx=\frac{-\pi}{2}\log2.\end{aligned}

$$

### EXERCISE 7.11

Byusing e ropiodiiigls,vluateiglsinxeies 1o19.

1.$\int_{0}^{\frac{\pi}{2}}\cos^{2}x d x$ 2.$\int_{0}^{\frac{\pi}{2}}\frac{\sqrt{\sin x}}{\sqrt{\sin x}+\sqrt{\cos x}}dx$ 3.$\int_{0}^{\frac{\pi}{2}}{\frac{\sin^{\frac{3}{2}}x d x}{\sin^{\frac{3}{2}}x+\cos^{\frac{3}{2}}x}}$

4.

$$

\int_{0}^{\frac{\pi}{2}}{\frac{\cos^{5}x\;d x}{\sin^{5}x+\cos^{5}x}}

$$

5.

$$

\int_{-5}^{5}|x+2|dx 

$$

6.

$$

\int_{2}^{8}\left|x-5\right|dx 

$$

7.$\int_{0}^{1}x\left(1-x\right)^{n}dx$ 8$\int_{0}^{\frac{\pi}{4}}\log\left(1+\tan x\right)d x$ 9.$\int_{0}^{2}x{\sqrt{2-x}}d x$

10.$\int_{0}^{\frac{\pi}{2}}(2\log\sin x-\log\sin2x)d x$ 11.$\int_{\frac{-\pi}{2}}^{\frac{\pi}{2}}\sin^{2}x d x$

12.

$$

\int_{0}^{\pi}{\frac{x d x}{1+\sin x}}

$$

13.

$$

\int_{\frac{-\pi}{2}}^{\frac{\pi}{2}}\sin^{7}x d x 

$$

14.

$$

\int_{0}^{2\pi}\cos^{5}x dx 

$$

15.

$$

\int_{0}^{\frac{\pi}{2}}\frac{\sin x-\cos x}{1+\sin x\cos x}dx 

$$

$$

\int_{0}^{\pi}\log\left(1+\cos x\right)dx 

$$

$$

\int_{0}^{a}\frac{\sqrt{x}}{\sqrt{x}+\sqrt{a-x}}dx 

$$

18.$\int_{0}^{4}\left|x-1\right|dx$

19. Show that $\int_{0}^{a}f(x)g(x)dx=2\int_{0}^{a}f(x)dx$ ,if f and g are defined as $f(x)=f(a-x)$ and $g(x)+g(a-x)=4$

Choose the correct answer in Exercises 20 and 21.

20. The value of $\int_{\frac{-\pi}{2}}^{\frac{\pi}{2}}(x^{3}+x\cos x+\tan^{5}x+1)d x$ : is

(A)0(B)2(C)π(D)1

21. The value of $\int_{0}^{\frac{\pi}{2}}\log\left(\frac{4+3\sin x}{4+3\cos x}\right)dx$ 5

(A)2(B)$\left[\frac{3}{4}\right.]$ (C)0(D)-2

## Miscellaneous Examples

Example 37 Find $\int\cos6x{\sqrt{1+\sin6x}}d x$

Solution Put $t=1+\sin6x$ ,so that $d t=6\;{\cos}\;6x\;d x$

Therefore

$$

\begin{aligned}\int\cos6x\sqrt{1+\sin6x}dx&=\frac{1}{6}\int t^{\frac{1}{2}}dt\\&=\frac{1}{6}\times\frac{2}{3}(t)^{\frac{3}{2}}+C=\frac{1}{9}(1+\sin6x)^{\frac{3}{2}}+C.\end{aligned}

$$

Example 38 Find $\int{\frac{(x^{4}-x)^{\frac{1}{4}}}{x^{5}}}d x.$

Solution We have $\int_{\frac{(x^{4}-x)^{\frac{1}{4}}}{x^{5}}}^{\frac{(x^{4}-x)^{\frac{1}{4}}}{x^{5}}}d x=\int_{\frac{(1-\frac{1}{x^{3}})^{\frac{1}{4}}}{x^{4}}}^{\frac{(1-\frac{1}{x^{3}})^{\frac{1}{4}}}{x^{4}}}d x$

Put $1-\frac{1}{x^{3}}=1-x^{-3}=t,\quad\Rightarrow\quad\tan\frac{3}{x^{4}}dx=dt$

Therefore $\int_{\frac{\left(x^{4}-x\right)^{\frac{1}{4}}}{x^{5}}}^{\frac{\left(x^{4}-x\right)^{\frac{1}{4}}}{x^{5}}}dx=\frac{1}{3}\int_{\frac{\left(x^{4}-x\right)^{\frac{1}{4}}}{x^{5}}}^{\frac{\left(x^{4}-x\right)^{\frac{1}{4}}}{x^{5}}}dt=\frac{1}{3}\times\frac{4}{5}\times\frac{5}{4}+C=\frac{4}{15}\left(1-\frac{1}{x^{3}}\right)^{\frac{5}{4}}+C$

Example 39 Find $\int{\frac{x^{4}d x}{(x-1)(x^{2}+1)}}$

Solution We have

$$

\begin{aligned}\frac{x^{4}}{\left(x-1\right)\left(x^{2}+1\right)}&=\left(x+1\right)+\frac{1}{x^{3}-x^{2}+x-1}\\&=\left(x+1\right)+\frac{1}{\left(x-1\right)\left(x^{2}+1\right)}\end{aligned}

$$

Now express

$$

\frac{1}{\left(x-1\right)\left(x^{2}+1\right)}=\frac{\mathrm{A}}{\left(x-1\right)}+\frac{\mathrm{B}x+\mathrm{C}}{\left(x^{2}+1\right)}

$$

So

$$

\begin{aligned}\mathbf{I}&=\mathbf{A}(x^2+1)+(\mathbf{B}x+\mathbf{C})(x-1)\\&=(\mathbf{A}+\mathbf{B})x^2+(\mathbf{C}-\mathbf{B})x+\mathbf{A}-\mathbf{C}\end{aligned}

$$

Equating coefficients on both sides,$\mathrm{w e~g e t~A+B=0,~C-B=0~a n d~A-C=1~}$ which give $\mathbf{A}={\frac{1}{2}},\mathbf{B}=\mathbf{C}=-{\frac{1}{2}}$ . Substituting values of A, B and C in (2), we get

$$

\frac{1}{\left(x-1\right)\left(x^{2}+1\right)}=\frac{1}{2\left(x-1\right)}-\frac{1}{2}\frac{x}{\left(x^{2}+1\right)}-\frac{1}{2\left(x^{2}+1\right)}

$$

Again, substituting (3) in (1), we have

$$

\frac{x^{4}}{(x-1)(x^{2}+x+1)}=\frac{1}{(x+1)}+\frac{1}{2(x-1)}-\frac{1}{2}\frac{x}{(x^{2}+1)}-\frac{1}{2(x^{2}+1)}

$$

Therefore

$$

\begin{aligned}\int&\frac{x^{4}}{\left(x-1\right)\left(x^{2}+x+1\right)}dx=\frac{x^{2}}{2}+x+\frac{1}{2}\log\left|x-1\right|-\frac{1}{4}\log\left(x^{2}+1\right)-\frac{1}{2}\tan^{-1}x+C\\ \xlongequal{Example40}&Find\int\left\lbrack\log\left(\log x\right)+\frac{1}{\left(\log x\right)^{2}}\right\rbrack dx\\ \text{Solution Let}&\dot{\mathbf{I}}=\int\left\lbrack\log\left(\log x\right)+\frac{1}{\left(\log x\right)^{2}}\right\rbrack dx\\ &=\int\log\left(\log x\right)dx+\int\frac{1}{\left(\log x\right)^{2}}dx\end{aligned}

$$

In the first integral, let us take 1 as the second function. Then integrating it by parts, we get

$$

\begin{aligned}\mathrm{II}&=x\log\left(\log x\right)-\int\frac{1}{x\log x}dx+\int\frac{dx}{\left(\log x\right)^2}dx\\&=x\log\left(\log x\right)-\int\frac{dx}{\log x}+\int\frac{dx}{\left(\log x\right)^2}\end{aligned}

$$

Again, consider $\int_{\frac{dx}{\log x}}^{}$ , take 1 as the second function and integrate it by parts,

$$

\operatorname{w e}\operatorname{h a v e}\int{\frac{d x}{\log x}}=\left[{\frac{x}{\log x}}-\int x\left\{-{\frac{1}{(\log x)^{2}}}\left({\frac{1}{x}}\right)\right\}d x\right]

$$

Putting (2) in (1), we get

$$

\int\mathrm{I}=x\log\left(\log x\right)-\frac{x}{\log x}-\int\frac{dx}{\left(\log x\right)^2}+\int\frac{dx}{\left(\log x\right)^2}=x\log\left(\log x\right)-\frac{x}{\log x}+C.

$$

Example 41 Find $\int\left[\sqrt{\cot x}+\sqrt{\tan x}\right]dx$

Solution We have

$$

\int\left[\sqrt{\cot x}+\sqrt{\tan x}\right]dx=\int\sqrt{\tan x}(1+\cot x)dx 

$$

Put tan $x=t^{2}$ ,so that $\sec^{2}x d x=2t d t$

or

$$

dx=\frac{2t dt}{1+t^{4}}

$$

Then

$$

\mathrm{I}=\int t\left(1+{\frac{1}{t^{2}}}\right){\frac{2t}{(1+t^{4})}}d t.

$$

$$

2\int\frac{\left(t^{2}+1\right)}{t^{4}+1}dt=2\int\frac{\left(1+\frac{1}{t^{2}}\right)dt}{\left(t^{2}+\frac{1}{t^{2}}\right)}=2\int\frac{\left(1+\frac{1}{t^{2}}\right)dt}{\left(t-\frac{1}{t}\right)^{2}+2}

$$

Put $t-\frac{1}{t}=y,\mathrm{s o}\mathrm{t h a t}\left(1+\frac{1}{t^{2}}\right)d t=d y.$ . Then

$$

\begin{aligned}\mathrm{I}&=2\int\frac{dy}{y^{2}+\left(\sqrt{2}\right)^{2}}=\sqrt{2}\tan^{-1}\frac{y}{\sqrt{2}}+\mathrm{C}=\sqrt{2}\tan^{-1}\frac{\left(t-\frac{1}{t}\right)}{\sqrt{2}}+\mathrm{C}\\&=\sqrt{2}\tan^{-1}\left(\frac{t^{2}-1}{\sqrt{2}t}\right)+\mathrm{C}=\sqrt{2}\tan^{-1}\left(\frac{\tan x-1}{\sqrt{2}\tan x}\right)+\mathrm{C}\end{aligned}

$$

Example 42 Find $\int{\frac{\sin2x\cos2x d x}{\sqrt{9-\cos^{4}(2x)}}}$

Solution Let $\int\frac{\sin2x\cos2x}{\sqrt{9-\cos^{4}2x}}dx$

Put $\cos^{2}(2x)=t$ so that 4 sin 2x cos 2x $d x=-d t$

$$

$\begin{aligned}$&Therefore\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad 

$$

Integrating both integrals on righthand side, we get

$$

\begin{aligned}\left[\int_{-1}^{\frac{3}{2}}|x\sin\pi x|dx\right.&=\left[\frac{-x\cos\pi x}{\pi}+\frac{\sin\pi x}{\pi^2}\right]_{-1}^{1}-\left[\frac{-x\cos\pi x}{\pi}+\frac{\sin\pi x}{\pi^2}\right]_{-1}^{\frac{3}{2}}\\&=\left.\frac{2}{\pi}-\left[-\frac{1}{\pi^2}-\frac{1}{\pi}\right]=\frac{3}{\pi}+\frac{1}{\pi^2}\right.\end{aligned}]

$$

Example 44 Evaluate $\int_{0}^{\pi}\frac{x dx}{a^{2}\cos^{2}x+b^{2}\sin^{2}x}$

$$

\begin{aligned}Solution LetI&=\int_{0}^{\pi}\frac{x dx}{a^2\cos^2x+b^2\sin^2x}=\int_{0}^{\pi}\frac{(\pi-x)dx}{a^2\cos^2(\pi-x)+b^2\sin^2(\pi-x)}\quad(using P_4)\\&=\pi\int_{0}^{\pi}\frac{dx}{a^2\cos^2x+b^2\sin^2x}-\int_{0}^{\pi}\frac{x dx}{a^2\cos^2x+b^2\sin^2x}\\&=\pi\int_{0}^{\pi}\frac{dx}{a^2\cos^2x+b^2\sin^2x}-I\\ Thus\quad&2I=\pi\int_{0}^{\pi}\frac{dx}{a^2\cos^2x+b^2\sin^2x}\end{aligned}

$$

or

$$

\begin{aligned}&\mathrm{I}=\frac{\pi}{2}\int_{0}^{\frac{\pi}{2}}\frac{dx}{a^{2}\cos^{2}x+b^{2}\sin^{2}x}=\frac{\pi}{2}\cdot2\int_{0}^{\frac{\pi}{2}}\frac{dx}{a^{2}\cos^{2}x+b^{2}\sin^{2}x}\left(\mathrm{using~P}_{0}\right)\\ &=\pi\left[\int_{0}^{\frac{\pi}{4}}\frac{dx}{a^{2}\cos^{2}x+b^{2}\sin^{2}x}+\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\frac{dx}{a^{2}\cos^{2}x+b^{2}\sin^{2}x}\right]\\ &=\pi\left[\int_{0}^{\frac{\pi}{4}}\frac{\sec^{2}xdx}{a^{2}+b^{2}\tan^{2}x}+\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\frac{\cos\sec^{2}xdx}{a^{2}\cot^{2}x+b^{2}}\right]\\ &=\pi\left[\int_{0}^{1}\frac{dt}{a^{2}+b^{2}t^{2}}-\int_{1}^{0}\frac{du}{a^{2}u^{2}+b^{2}}\right]\left(\arctan x=\tan t\arctan x=u\right)\\ &=\frac{\pi}{ab}\left[\tan^{-1}\frac{bt}{a}\right]_{0}^{1}-\frac{\pi}{ab}\left[\tan^{-1}\frac{au}{b}\right]_{1}^{0}=\frac{\pi}{ab}\left[\tan^{-1}\frac{b}{a}+\tan^{-1}\frac{a}{b}\right]=\frac{\pi^{2}}{2ab}\\ \end{aligned}

$$

## Miscellaneous Exercise on Chapter 7

Integrate the functions in Exercises 1 to 24.

$$

\begin{aligned}&1.\quad\frac{1}{x-x^{3}}&2.\quad\frac{1}{\sqrt{x+a}+\sqrt{x+b}}\quad3.\quad\frac{1}{x\sqrt{ax-x^{2}}}[Hint:Put x=\frac{a}{t}]\\&2.\quad\frac{1}{x^{2}(x^{4}+1)^{\frac{3}{4}}}&5.\quad\frac{1}{x^{\frac{1}{2}}+x^{\frac{1}{3}}}\quad[Hint:\frac{1}{x^{\frac{1}{2}}+x^{\frac{1}{3}}}=\frac{1}{x^{\frac{1}{3}}\left(1+x^{\frac{1}{6}}\right)},put x=t^{6}]\\&3.\quad\frac{5x}{(x+1)\left(x^{2}+9\right)}&7.\quad\frac{\sin x}{\sin\left(x-a\right)}\quad8.\quad\frac{e^{5\log x}-e^{4\log x}}{e^{3\log x}-e^{2\log x}}\\&9.\quad\frac{\cos x}{\sqrt{-\sin^{2}x}}&10.\quad\frac{\sin^{8}-\cos^{8}x}{1-2\sin^{2}x\cos^{2}x}\quad11.\quad\frac{1}{\cos\left(x+a\right)\cos\left(x+b\right)}\\&12.\quad\frac{x^{3}}{\sqrt{1-x^{8}}}&13.\quad\frac{e^{x}}{\left(x^{2}+\right)\left(2+e^{x}\right)}\quad14.\quad\frac{1}{\left(x^{2}+1\right)\left(x^{2}+4\right)}\\&15.\quad\cos^{3x}e^{\log sin x}&16.\quad e^{3\log x}\left(x^{4}+1\right)^{-1}\quad17.\quad f^{\prime}\left(ax+b\right)[f(ax+b)]^{n}\\&18.\quad\frac{1}{\sqrt{\sin^{3}x\sin\left(x+\alpha\right)}}&19.\quad\frac{\sin^{-1}\sqrt{x}-\cos^{-1}\sqrt{x}}{\sin^{-1}\sqrt{x}+\cos^{-1}\sqrt{x}},x\in[0,1]\end{aligned}

$$

$$

20.\sqrt[3]{\frac{1-\sqrt{x}}{1+\sqrt{x}}}\quad\frac{21.\frac{2+\sin2x}{1+\cos2x}e^{x}\quad22.\frac{x^{2}+x+1}{(x+1)^{2}(x+2)^{2}}}{24.\frac{x^{2}+1}{x^{4}}}Evaluate the definite integrals in Exercises 25 to 33.

$$

Evaluate the definite integrals in Exercises 25 to 33.

25.

$$

\int_{\frac{\pi}{2}}^{\pi}e^{x}\left(\frac{1-\sin x}{1-\cos x}\right)dx\quad26。\quad\int_{0}^{\frac{\pi}{4}}\frac{\sin x\cos x}{\cos^{4}x+\sin^{4}x}dx\quad27。\quad\int_{0}^{\frac{\pi}{2}}\frac{\cos^{2}x}{\cos^{2}x+4\sin^{2}x}dx 

$$

28.

$$

\int_{\frac{\pi}{6}}^{\frac{\pi}{3}}\frac{\sin x+\cos x}{\sqrt{\sin2x}}dx\quad\stackrel{\sim}{\sim}\int_{0}^{1}\frac{dx}{\sqrt{1+x}-\sqrt{x}}dx\quad\stackrel{\sim}{\sim}\int_{0}^{\frac{\pi}{4}}\frac{\sin x+\cos x}{9+16\sin2x}dx 

$$

31.

$$

\int_{0}^{\frac{\pi}{2}}\sin2x\tan^{-1}(\sin x)d x 

$$

32.

$$

\int_{0}^{\pi}\frac{x\tan x}{\sec x+\tan x}dx 

$$

33.

$$

\int_{1}^{4}\left[x-1\right]+\left|x-2\right|+\left|x-3\right|dx 

$$

Prove the following (Exercises 34 to 39)

34.

$$

\int_{1}^{3}\frac{dx}{x^{2}(x+1)}=\frac{2}{3}+\log\frac{2}{3}

$$

35.

$$

\int_{0}^{1}x e^{x}dx=1

$$

36.

$$

\int_{-1}^{1}x^{17}\cos^4x dx=0

$$

37.

$$

\int_{0}^{\frac{\pi}{2}}\sin^{3}x dx=\frac{2}{3}

$$

38.

$$

\int_{0}^{\frac{\pi}{4}}2\tan^{3}x\ dx=1-\log2

$$

39.

$$

\int_{0}^{1}\sin^{-1}x d x=\frac{\pi}{2}-1

$$

40. Evaluate $\int_{0}^{1}e^{2-3x}d x$ as a limit of a sum.

Choose the correct answers in Exercises 41 to 44.

41.$\int_{\frac{}{e^{^x}+e^{^{-x}}}}^{}$ .is equal to

(A)

$$

\tan^{-1}\left(e^{x}\right)+\mathbf{C}

$$

(B)

$$

\tan^{-1}\left(e^{-x}\right)+\mathbf{C}

$$

(C)

$$

\log(e^{x}-e^{-x})+\mathbf{C}

$$

(D)

$$

\log(e^{x}+e^{-x})+\mathbf{C}

$$

42.$\int_{\frac{\cos2x}{\left(\sin x+\cos x\right)^2}}^{\cos2x}$ ·dx is equal to

(A)

(C)

$$

\frac{-1}{\sin x+\cos x}+C 

$$

$$

\log\left|\sin x-\cos x\right|+C 

$$

(B)

(D)

$$

\left[\log\left|\sin x+\cos x\right|+C\right]

$$

$$

\frac{1}{\left(\sin x+\cos x\right)^{2}}

$$

43.$\operatorname{I f}f\left(a+b-x\right)=f\left(x\right)$ ,then $\int_{a}^{b}x f(x)$ dx is equal to

(A)

$$

{\frac{a+b}{2}}\int_{a}^{b}f(b-x)d x 

$$

(B)

$$

\frac{a+b}{2}\int_{a}^{b}f(b+x)dx 

$$

(C)

$$

{\frac{b-a}{2}}\int{}_{a}^{b}f(x)d x 

$$

(D)

$$

\frac{a+b}{2}\int_{a}^{b}f(x)dx 

$$

44. The value of $\int_{0}^{1}\tan^{-1}\left(\frac{2x-1}{1+x-x^2}\right)dx$ is

(A)1(B)0(C) −1(D)$\frac{\pi}{4}$

## Summary

■

we are given a function and we have to find the derivative or differential of this function, but in the integral calculus, we are to find a function whose differential is given. Thus, integration is a process which is the inverse of differentiation.

Let $\left[{\frac{d}{d x}}\mathbb{F}(x)=f(x)\right]$ . Then we write $\int f(x)dx=\mathrm{F}(x)+C$ . These integrals are called indefinite integrals or general integrals,C is called constant of integration.All these integrals differ by a constant.cY ■Fml of curves, eachof which isobtained by translatingone of thecurves parallel to itself upwards or downwards along the y-axis.

■

$$

\left[\int\left[f(x)+g(x)\right]dx=\int f(x)dx+\int g(x)dx\right]

$$

2. For any real number k,$\int k f(x)dx=k\int f(x)dx$

More generally, if $f_{1},f_{2},f_{3},\ldots,f_{n}$ arefunctions and $k_{1},\;k_{2},\;...\;,k_{n}$ are real numbers.Then

$$

\begin{align*}\left[\int[k_1f_1(x)+k_2f_2(x)+\ldots+k_n f_n(x)]dx\right.\\=\left.k_1\int f_1(x)dx+k_2\int f_2(x)dx+\ldots+k_n\int f_n(x)dx\right]\end{align*}

$$

## 国Some standard integrals

(i)

$$

\int x^{n}dx=\frac{x^{n+1}}{n+1}+C,\;n\neq-1.\;Particularly,\;\int dx=x+C 

$$

(i)

$$

\int\cos x dx=\sin x+C 

$$

(i

$$

\int\sin x dx=-\cos x+C 

$$

(iv)

$$

\int\sec^{2}x dx=\tan x+C 

$$

(v)

$$

\int\cos\mathrm{ec}^{2}x dx=-\cot x+C 

$$

(vi)

$$

\int\sec x\tan x dx=\sec x+C 

$$

$$

(\mathrm{v i i})\int\cos\mathrm{e c}x\cot x d x=-\cos\mathrm{e c}x+C\quad(\mathrm{v i i i i})\int\frac{d x}{\sqrt{1-x^{2}}}=\sin^{-1}x+C 

$$

(ix)

$$

\int_{\frac{\sqrt{1-x^{2}}}{\sqrt{1-x^{2}}}}=-\cos^{-1}x+C 

$$

(x)

$$

\int\frac{dx}{1+x^{2}}=\tan^{-1}x+C 

$$

(xi)

$$

\int_{\frac{d x}{1+x^{2}}}^{\frac{d x}{1+x^{2}}}=-\cot^{-1}x+C 

$$

(xii)

$$

\int e^{x}dx=e^{x}+C 

$$

(xii)

$$

\int a^{x}d x=\frac{a^{x}}{\log a}+C 

$$

(xiv)

$$

\int\frac{dx}{x\sqrt{x^{2}-1}}=\sec^{-1}x+C 

$$

(xv)

$$

\int\frac{dx}{x\sqrt{x^{2}-1}}=-\cos\mathrm{e}^{-1}x+C 

$$

(xvi)

$$

\int\frac{1}{x}dx=\log|x|+C 

$$

## ■Integration by partial fractions

Recall that a rational function is ratio of two polynomials of the form $\frac{\mathbf{P}(x)}{Q(x)}$ where $\mathbf{P}(x)$ and $\mathrm{~Q~}(x)$ are polynomials in x and $\mathbb{Q}\left(x\right)\neq0$ .If degree of the polynomial $\operatorname{P}\left(x\right)$ is greater than the degree of the polynomial $\mathrm{~Q~}(x)$ , then we may divide $\operatorname{P}\left(x\right)$ by $\mathrm{Q}\left(x\right)$ sothat $\frac{\mathbf{P}(x)}{\mathbf{Q}(x)}=\mathbf{T}(x)+\frac{\mathbf{P}_{1}(x)}{\mathbf{Q}(x)}$ where $\mathrm{T}(x)$ is a polynomial in x and degree of $\mathrm{P}_{_1}(x)$ is less than the degree of $\mathbf{Q}(x)$ $\operatorname{T}\left(x\right)$ being polynomial can be easily integrated.$\left\{\frac{\mathbf{P}_{1}(x)}{\mathbf{Q}(x)}\right.}$ can be integrated by expressing $\frac{\mathbf{P}_{1}(x)}{\mathbf{Q}(x)}$ as the sum of partial fractions of the following type:

$$

(ci)

$$

$(ci)$

5

where $x^{2}+b x+c$ can not be factorised further.

## ■Integration bysubstitution

Achange in the variableof integration often reduces an integral to one of the fundamental integrals. The method in which we changethevariable to some other variable is called the method of substitution. When the integrand involves some trigonometric functions, we use some well known identities to find the integrals. Using substitution technique, we obtain the following standard integrals.

(i)

$$

\int\tan x dx=\log|\sec x|+C\quad(ii)\quad\int\cot x dx=\log|\sin x|+C 

$$

(i

$$

\int\sec x dx=\log|\sec x+\tan x|+C 

$$

(iv)

$$

\int\cos\epsilon x dx=\log|\cos\epsilon x-\cot x|+C 

$$

■Integrals of some special functions

(i)

$$

\int\frac{dx}{x^{2}-a^{2}}=\frac{1}{2a}\log\left|\frac{x-a}{x+a}\right|+C 

$$

(i)

$$

\int\frac{dx}{a^{2}-x^{2}}=\frac{1}{2a}\log\left|\frac{a+x}{a-x}\right|+C\quad(iii)\quad\int\frac{dx}{x^{2}+a^{2}}=\frac{1}{a}\tan^{-1}\frac{x}{a}+C 

$$

$$

\int\frac{dx}{\sqrt{x^{2}-a^{2}}}=\log\left|x+\sqrt{x^{2}-a^{2}}\right|+C\left(\mathrm{v}\right)\int\frac{dx}{\sqrt{a^{2}-x^{2}}}=\sin^{-1}\frac{x}{a}+C 

$$

## Integration by parts

For given functions ◼$f_{\mathrm{1}}$ and $f_{2^{\prime}}$ we have

$$

\int f_{1}(x)\cdot f_{2}(x)dx=f_{1}(x)\int f_{2}(x)dx-\int\left[\frac{d}{dx}f_{1}(x)\cdot\int f_{2}(x)dx\right]dx 

$$

integral of the product of two functions = first function × integral of the second function –integral of {differential coefficient of the first function ×integral of the second function}. Care must be taken in choosing the first function and the second function. Obviously, we must take that function as the second function whose integral is well known to us.

$$

\int e^{x}\left[f(x)+f^{\prime}(x)\right]dx=\int e^{x}f(x)dx+C 

$$

■Some special types of integrals

(i)

$$

\int\sqrt{x^{2}-a^{2}}\ dx=\frac{x}{2}\sqrt{x^{2}-a^{2}}-\frac{a^{2}}{2}\log\left|x+\sqrt{x^{2}-a^{2}}\right|+C 

$$

(ii)

$$

\int\sqrt{x^{2}+a^{2}}\ dx=\frac{x}{2}\sqrt{x^{2}+a^{2}}+\frac{a^{2}}{2}\log\left|x+\sqrt{x^{2}+a^{2}}\right|+C 

$$

(ii)

$$

\int\sqrt{a^{2}-x^{2}}\ dx=\frac{x}{2}\sqrt{a^{2}-x^{2}}+\frac{a^{2}}{2}\sin^{-1}\frac{x}{a}+C 

$$

(iv) Integrals of the types $\int\frac{dx}{ax^{2}+bx+c}or\int\frac{dx}{\sqrt{ax^{2}+bx+c}}can$ be transformed into standard form by expressing

$$

ax^{2}+bx+c=a\left[x^{2}+\frac{b}{a}x+\frac{c}{a}\right]=a\left[\left(x+\frac{b}{2a}\right)^{2}+\left(\frac{c}{a}-\frac{b^{2}}{4a^{2}}\right)\right]$$

(v) Integrals of the types $\int\frac{px+q dx}{ax^2+bx+c}or\int\frac{px+q dx}{\sqrt{ax^2+bx+c}}can$ be

transformed into standard form by expressing

$px+q=\mathbf{A}\frac{d}{dx}\left(ax^{2}+bx+c\right)+\mathbf{B}=\mathbf{A}\left(2ax+b\right)+\mathbf{B}$ , where A and B are ab

determined by comparing coefficients on both sides.

■We have defined $\int{}_{a}^{b}f(x)$ dx as the area of the region bounded by the curve $y=f(x),a\leq x\leq b$ , the x-axis and the ordinates $x=a{\mathrm{~a n d~}}x=b$ .Letx be a given point in $[a,b]$ Then $\int{}_{a}^{x}f(x)$ dxrepresents the Area function $\operatorname{A}\left(x\right)_{\cdot}$ This concept of area function leads to the Fundamental Theorems of Integral Calculus.

■First fundamental theorem of integral calculus

Let the area function be defined by $\mathrm{A}(x)=\int{}_{a}^{x}f(x)$ dx for all $x\geq a,$ where the functionf is assumed to be continuous on [a, b]. Then $\mathrm{A}^{\prime}(x)=f(x)$ forall

$x\in[a,b]$

■Second fundamental theorem of integral calculus

Letf be a continuous function of x defined on the closed interval $[a,b]$ and let F be another function such that ${\frac{d}{d x}}\operatorname{F}(x)=f(x)$ for all x in the domain of

f, then $\int_{a}^{b}f(x)dx=\left[\mathrm{F}(x)+\mathrm{C}\right]_{a}^{b}=\mathrm{F}(b)-\mathrm{F}(a)$

This is called the definite integral off over the range [a, b], where a and b arecalled the limits of integration,a being the lower limit and bthe upper limit.

