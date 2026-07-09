

# INFINITE SERIES

#### A.1.1 Introduction

As discussed in the Chapter 9 on Sequences and Series, a sequence $a_{1},a_{2},\cdots,a_{n}$ having infinite number of terms is called infinite sequence and its indicated sum, i..,$a_{1}+a_{2}+a_{3}+\ldots+a_{n}+$ ... is called an infinte series associated with infinite sequence.This series can also be expressed in abbreviated form using the sigma notation, i.e.,

$$a_{1}+a_{2}+a_{3}+\ldots+a_{n}+\ldots=\sum_{k=1}^{\infty}a_{k}

$$

Inthis Chapr,w shalltudabout omespcialtypeofriewhichmay required in different problem situations.

#### A.1.2 Binomial Theorem for any Index

In Chapter 8, we discussed the Binomial Theorem in which the index was a positive integer. In this Section, we state a more general form of the theorem in which the index is not necessarily a whole number.It gives us a particular type of infinite series,called Binomial Series. We illustrate few applications, by examples.

We know the formula

$$

(1+x)^{n}=\frac{x}{n}C_{0}+\frac{x}{n}C_{1}x+\cdots+\frac{x}{n}C_{n}x^{n}

$$

Here, n is non-negative integer. Observe that if we replace index n by negative integer or a fraction, then the combinations ${}^{n}\mathrm{C}_{r}$ do not make any sense.

We now state (without proof), the Binomial Theorem, giving an infinite series in which the index is negative or a fraction and not a whole number.

Theorem The formula

$$

\left(1+x\right)^{m}=1+m x+\frac{m(m-1)}{1.2}x^{2}+\frac{m(m-1)(m-2)}{1.2.3}x^{3}+\ldots 

$$

holds whenever $\left|x\right|<1$

Remark 1.Note carefully the condition $|x|<1,i.e.,-1<x<1$ is necessary when m is negative integer or a fraction. For example, if we take $x=-2and m=-2$ , we obtain

$$

\left(1-2\right)^{-2}=1+\left(-2\right)\left(-2\right)+\frac{\left(-2\right)\left(-3\right)}{1.2}\left(-2\right)^{2}+\cdots 

$$

or

$$

1=1+4+12+\cdots 

$$

This is not possible

2. Note that there are infinite number of terms in the expansion of $(1+x)^{m}$ ',when m is a negative integer or a fraction shed Consider

$$

\begin{align*}\left[(a+b)^m\right.&=\left[a\left(1+\frac{b}{a}\right)\right]^m=a^m\left(1+\frac{b}{a}\right)^m\\&=a^m\left[1+m\frac{b}{a}+\frac{m(m-1)}{1.2}\left(\frac{b}{a}\right)^2+\cdots\right]^m\\&=a^m+m a^{m-1}b+\frac{m(m-1)}{1.2}a^{m-2}b^2+\cdots\end{align*} shed ]

$$

This expansion is valid when $\left|\frac{b}{a}\right|<1or equivalently when|b|<|a|.$

The general term in the expansion of $(a+b)^{m}$ is

$$

\frac{m(m-1)(m-2)\ldots(m-r+1)a^{m-r}b^{r}}{1.2.3\ldots r}

$$

We give below certain particular cases of Binomial Theorem, when we assume $\left|x\right|<1$ , these are left to students as exercises:

$$

\begin{align*}1.\quad&(1+x)^{-1}=1-x+x^2-x^3+\ldots\\2.\quad&(1-x)^{-1}=1+x+x^2+x^3+\ldots\\3.\quad&(1+x)^{-2}=1-2x+3x^2-4x^3+\ldots\\4.\quad&(1-x)^{-2}=1+2x+3x^2+4x^3+\ldots\end{align*}

$$

Example 1 Expand $\left(1-\frac{x}{2}\right)^{-\frac{1}{2}}$ , when $|x|<2$

Solution We have

$$

\left(1-\frac{x}{2}\right)^{-\frac{1}{2}}=\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{1}{2}}+\cdots+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\frac{2}{2}}+\cdots+\cdots+\left(\frac{-\frac{1}{2}}{1}\right)^{-\cdots+\cdots+\left(\frac{1}{2}}\right)^{-\cdots+\cdots+\left(\frac{1}{2}\right)^{-\cdots+\cdots+\cdots+\left(\frac{2}{2}}\right)^{-\cdots+\cdots+\cdots+\left(\cdots+\cdots+\left(\frac{2}{2}\right)^{-\cdots+\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots\cdots++\cdots\cdots+\cdots+\cdots+\cdots\cdots++\cdots\cdots++\cdots\cdots++\cdots\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots+\cdots\cdots++\cdots+\cdots+\cdots\cdots++\cdots\cdots++\cdots\cdots+\cdots+\cdots\cdots+\cdots++\cdots+\cdots\cdots++\cdots\cdots++\cdots+\cdots\cdots++\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots+\cdots\cdots++\cdots\cdots+\cdots++\cdots\cdots+\cdots+\cdots++\cdots\cdots++\cdots\cdots\cdots++\cdots+\cdots+\cdots+\cdots\cdots+++\cdots\cdots+\cdots\cdots+\cdots+\cdots+\cdots++\cdots\cdots\cdots++\cdots\cdots++\cdots+\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots\cdots+\cdots++\cdots\cdots+\cdots+\cdots+\cdots++\cdots\cdots+\cdots\cdots++\cdots\cdots++\cdots\cdots+\cdots+\cdots+\cdots+\cdots\cdots++\cdots+\cdots\cdots+\cdots+\cdots+\cdots++\cdots\cdots\cdots+\cdots+++\cdots+\cdots\cdots+\cdots+\cdots\cdots++\cdots\cdots+\cdots++\cdots+\cdots\cdots+\cdots+\cdots+\cdots+\cdots\cdots+\cdots+++\cdots\cdots\cdots+\cdots\cdots++\cdots+\cdots\cdots+++\cdots\}}})

$$

#### A.1.3 Infinite Geometric Series

From Chapter 9, Section 9.5, a sequence $a_{1},\;a_{2},\;a_{3},\;...,\;a_{n}$ is called $\widehat{G.P.}\ if$ $\frac{a_{k+1}}{a_{k}}=r\left(\arctan\right)\quad for k=1,2,3,\ldots,n-1$ . Particularly, if we take $a_{1}=a_{1}\mathrm{then}$ the resulting sequence a,$ar,ar^{2},...,ar^{n-1}$ is taken as the standard form of G.P., where a is first term and r, the common ratio of G.P.

sum of finite series $a+ar+ar^{2}+\ldots+ar^{n-1}$ which is given by to t

$$

S_{n}=\frac{a\left(1-r^{n}\right)}{1-r}

$$

$a+ar+ar^{2}+\ldots+ar^{n-1}$ .and illustrate the same by examples.

Let us consider the G.P. 1,$\frac{2}{3},\frac{4}{9}$

Here $a=1,r=\frac{2}{3}$ We have

$$

S_{n}=\frac{1-\left(\frac{2}{3}\right)^{n}}{1-\frac{2}{3}}=3\left[1-\left(\frac{2}{3}\right)^{n}\right]

$$

Let us study the behaviour of $\left(\frac{2}{3}\right)^{n}$ as n becomes larger and larger.

<div style="text-align: center;"><html><body><table border="1"><tr><td>n</td><td>1</td><td>5</td><td>10</td><td>20</td></tr><tr><td>$\left(\frac{2}{3}\right)^{n}$</td><td>0.6667</td><td>0.1316872428</td><td>0.01734152992</td><td>0.00030072866</td></tr></table></body></html></div>

We observe that as n becomes larger and larger,$\left(\frac{2}{3}\right)^{n}$ becomes closer and closer to

zero. Mathematically, we say that as n becomes sufficiently large,$\left(\frac{2}{3}\right)^{n}$ becomes

sufficiently small. In other words, as $n\to\infty,\left(\frac{2}{3}\right)^n\to0$ . Consequently, we find that the sum of infinitely many terms is given by $s=3$

Thus, for infinite geometric progression a, ar,$a\bar{r}^{2}...,$ if numerical value of common ratio r is less than 1, then

$$

S_{n}=\frac{a\left(1-r^{n}\right)}{1-r}=\frac{a}{1-r}-\frac{ar^{n}}{1-r}

$$

In this case,$r^{n}\rightarrow0\text{as}n\rightarrow\infty$ $\mathrm{since}\mid r\mid<1$ and then $\frac{ar^{n}}{1-r}\rightarrow0$ . Therefore,

$$

S_{n}\rightarrow\frac{a}{1-n}\quad as\quad n\rightarrow\infty.

$$

olically, sum to infinit

we have

$$

S=\frac{a}{1-r}

$$

(ci)

(i)

$$

\frac{1}{2}+\frac{1}{2^2}+\frac{1}{2^3}+\ldots=\frac{1}{1-\frac{1}{2}}=2

$$

(ii)

$$

\left[1-\frac{1}{2}+\frac{1}{2^2}-\frac{1}{2^3}+\ldots\right]=\frac{1}{1-\left(-\frac{1}{2}\right)}=\frac{1}{1+\frac{1}{2}}=\frac{2}{3}

$$

Example 2 Find the sum to infinity of the G.P.;

$$

\left[\frac{-5}{4},\frac{5}{16},\frac{-5}{64},\ldots\right]

$$

Solution Here $a=\frac{-5}{4}$ and $r=-\frac{1}{4}$ .Also $\left|r\right|<1$

Hence, the sum to infinity is $\frac{\frac{-5}{4}}{1+\frac{1}{4}}=\frac{\frac{-5}{4}}{\frac{5}{4}}=-1$

#### A.1.4 Exponential Series

.ed circle.

s

$$

1+\frac{1}{1!}+\frac{1}{2!}+\frac{1}{3!}+\frac{1}{4!}+\cdots 

$$

The sum of ) t

Let us estimate the value of the number e.

S Consider the two sums

and

$$

\begin{aligned}&\frac{1}{3!}+\frac{1}{4!}+\frac{1}{5!}+\cdots+\frac{1}{n!}+\cdots\\ &\frac{1}{2^2}+\frac{1}{2^3}+\frac{1}{2^4}+\cdots+\frac{1}{2^{n-1}}+\cdots\\ \end{aligned}

$$

Observe that

$$

\begin{aligned}&\frac{1}{3!}=\frac{1}{6}and\frac{1}{2^2}=\frac{1}{4},which gives\frac{1}{3!}<\frac{1}{2^2}\\&\frac{1}{4!}=\frac{1}{24}and\frac{1}{2^3}=\frac{1}{8},which gives\frac{1}{4!}<\frac{1}{2^3}\\&\frac{1}{5!}=\frac{1}{120}and\frac{1}{2^4}=\frac{1}{16},which gives\frac{1}{5!}<\frac{1}{2^4}\\ \end{aligned}

$$

Therefore, by analogy, we can say that

$$

\left\{\frac{1}{n!}<\frac{1}{2^{n-1}},when n>2\right\}

$$

We observe that ach term in (2) is less than the corresponding term in (3)

$$

Therefore \begin{aligned}\mathrm{e}^{\frac{1}{2}}&\left(\frac{1}{3!}+\frac{1}{4!}+\frac{1}{5!}+\ldots+\frac{1}{n!}\right)<\left(\frac{1}{2^2}+\frac{1}{2^3}+\frac{1}{2^4}+\ldots+\frac{1}{2^{n-1}}+\ldots\right)\\ &\left(\left(1+\frac{1}{1!}+\frac{1}{2!}\right)\text{on both sides of}(4),\mathrm{we get},\right.\\ &\left.\left(\left(1+\frac{1}{1!}+\frac{1}{2!}\right)+\left(\frac{1}{3!}+\frac{1}{4!}+\frac{1}{5!}+\ldots+\frac{1}{n!}+\ldots\right)\right.\right.\\ &\left.\left.<\left\{\left(1+\frac{1}{1!}+\frac{1}{2!}\right)+\left(\frac{1}{2^2}+\frac{1}{2^3}+\frac{1}{2^4}+\ldots+\frac{1}{2^{n-1}}+\ldots\right)\right\}\right.\right.\\ &\left.=\left\{1+\left(1+\frac{1}{2}+\frac{1}{2^2}+\frac{1}{2^3}+\frac{1}{2^4}+\ldots+\frac{1}{2^{n-1}}+\ldots\right)\right\}\right.\\ &\left.=1+\frac{1}{1-\frac{1}{2}}=1+2\geq3\right.\end{aligned} uned ))

$$

Therefore $\begin{aligned}\mathrm{e}^{\frac{1}{2}}&\left(\frac{1}{3!}+\frac{1}{4!}+\frac{1}{5!}+\ldots+\frac{1}{n!}\right)<\left(\frac{1}{2^2}+\frac{1}{2^3}+\frac{1}{2^4}+\ldots+\frac{1}{2^{n-1}}+\ldots\right)\\ &\left(\left(1+\frac{1}{1!}+\frac{1}{2!}\right)\text{on both sides of}(4),\mathrm{we get},\right.\\ &\left.\left(\left(1+\frac{1}{1!}+\frac{1}{2!}\right)+\left(\frac{1}{3!}+\frac{1}{4!}+\frac{1}{5!}+\ldots+\frac{1}{n!}+\ldots\right)\right.\right.\\ &\left.\left.<\left\{\left(1+\frac{1}{1!}+\frac{1}{2!}\right)+\left(\frac{1}{2^2}+\frac{1}{2^3}+\frac{1}{2^4}+\ldots+\frac{1}{2^{n-1}}+\ldots\right)\right\}\right.\right.\\ &\left.=\left\{1+\left(1+\frac{1}{2}+\frac{1}{2^2}+\frac{1}{2^3}+\frac{1}{2^4}+\ldots+\frac{1}{2^{n-1}}+\ldots\right)\right\}\right.\\ &\left.=1+\frac{1}{1-\frac{1}{2}}=1+2\geq3\right.\end{aligned}))$

Left handof)).herefore $e<3$ and also $e\geq2$ and hence $2\leq e\leq3$

Remark The exponential series involving variable x can be expressed as

$$

e^{x}=1+\frac{x}{1!}+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\ldots+\frac{x^{n}}{n!}+\ldots 

$$

Example 3 Find the coefficient of $x^{2}$ in the expansion of $e^{2x+3}$ as a series in powers $\mathrm{o f}x.$

Solution In the exponential series

$$

e^{x}=1+\frac{x}{1!}+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\cdots 

$$

replacing by $(2x+3)$ , we get

$$

e^{2x+3}=1+\frac{(2x+3)}{1!}+\frac{(2x+3)^2}{2!}+\cdots 

$$

Here, the general term is $\frac{(2x+3)^n}{n!}=\frac{(3+2x)^n}{n!}$ . This can be expanded by the Binomial Theorem as

$$

\frac{1}{n!}\left[3^{n}+^{n}C_{1}3^{n-1}(2x)+^{n}C_{2}3^{n-2}(2x)^{2}+\ldots+(2x)^{n}\right].

$$

Here, the coefficient of $x^{2}$ is $\frac{^{n}\mathrm{C}_{2}3^{n-2}2^{2}}{n!}$ . Therefore, the cefficient of $x^{2}$

series is

$$

\begin{aligned}\sum_{n=2}^{\infty}\frac{n^{2}C_{2}3^{n-2}2^{2}}{n!}&=2\sum_{n=2}^{\infty}\frac{n(n-1)3^{n-2}}{n!}\\&=2\sum_{n=2}^{\infty}\frac{3^{n-2}}{(n-2)!}\quad[using n!=n\quad(n-1)\quad(n-2)!]\\&=2\left[\frac{1+\frac{3}{1!}+\frac{3^{2}}{2!}+\frac{3^{3}}{3!}+\cdots}{2e^{3}}\right]\\&=2e^{3}\end{aligned}

$$

Thus $2e^{3}$ is the coeficient of in the expansion of $e^{2x+3}$ Alternatively $e^{2x+3}=e^{3}$ $e_{-}^{2x}$

$$

e^{3}\left[1+\frac{2x}{1!}+\frac{(2x)^{2}}{2!}+\frac{(2x)^{3}}{3!}+\cdots\right]

$$

Thus, the coefficient of $x^{2}$ in the expansion of $e^{2x+3}\ \mathrm{i}s\ e^{3}\ .\frac{2^{2}}{2!}=2e^{3}$

Example 4 Find the value of $e^{2}$ , rounded off to one decimal place.

Solution Using the formula of exponential series involving x, we have

$$

e^{x}=1+\frac{x}{1!}+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\ldots+\frac{x^{n}}{n!}+\ldots 

$$

Putting $x=2$ , we get

$$

\begin{aligned}e^{2}=1+\frac{2}{1!}+\frac{2^{2}}{2!}+\frac{2^{3}}{3!}+\frac{2^{4}}{4!}+\frac{2^{5}}{5!}+\frac{2^{6}}{6!}+\ldots\\ \quad\vdots\\ =1+2+2+\frac{4}{3}+\frac{2}{3}+\frac{4}{15}+\frac{4}{45}+\ldots\\ \quad\vdots\\ the sum of first seven terms\geq7.35\end{aligned} 5.

$$

On the other hand, we have

$$

e^{2}<\left(1+\frac{2}{1!}+\frac{2^{2}}{2!}+\frac{2^{3}}{3!}+\frac{2^{4}}{4!}\right)+\frac{2^{5}}{5!}\left(1+\frac{2}{6}+\frac{2^{2}}{6^{2}}+\frac{2^{3}}{6^{3}}+\cdots\right) hed 

$$

$$

hed 7+\frac{4}{15}\left(1+\frac{1}{3}+\left(\frac{1}{3}\right)^{2}+\cdots\right)=7+\frac{4}{15}\left(\frac{1}{1-\frac{1}{3}}\right)=7+\frac{2}{5}=7.4

$$

$e^{2}$ $e^{2}$

decimal place, is 7.4.

#### A.1.55LogarithmicSeries

Another very important series is logarithmic series which is also in the form of infinite series. We state the following result without proofand illustrate its application with an example.Ea

Theorem $\mathrm{I f}|x|<1$ ,then

$$

\log_{e}(1+x)=x-\frac{x^{2}}{2}+\frac{x^{3}}{3}-\cdots 

$$

ree eae r e r e r r e rse re

H $\log_{e}\left(1+x\right)$ $x=1$ e $x=1$ e $\mathrm{g}_{e}\left(1+x\right)$

$$

\log_{e}2=1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\ldots 

$$

Example 5 If α, β are the roots of the equation $x^{2}-px+q=0$ ', prove that

$$

\left[\log_{e}\left(1+p x+q x^{2}\right)=\left(\alpha+\beta\right)x-\frac{\alpha^{2}+\beta^{2}}{2}x^{2}+\frac{\alpha^{3}+\beta^{3}}{3}x^{3}-\ldots\right]

$$

$$

\begin{aligned}SolutiOB Right hand side&=\left[\alpha x-\frac{\alpha^2x^2}{2}+\frac{\alpha^3x^3}{3}-\ldots\right]+\left[\beta x-\frac{\beta^2x^2}{2}+\frac{\beta^3x^3}{3}-\ldots\right]\\&=\log_e\left(1+\alpha x\right)+\log\left(1+\beta x\right)\\&=\log_e\left(1+\left(\alpha+\beta\right)x+\alpha\beta x^2\right)\\&=\log_e\left(1+p x+q x^2\right)=\mathrm{Left hand side}.\end{aligned}$$

Here, we have used the facts $\alpha+\beta=p\mathrm{and}\alpha\beta=q$

$|\beta x|<1$ ven rots ofoffthe uadrar e a i euation e have als o assumed that both to asmed that $|\alpha x|<1$ and

<div style="text-align: center;"><img src="imgs/img_in_image_box_126_645_657_1123.jpg" alt="Image" width="56%" /></div>
