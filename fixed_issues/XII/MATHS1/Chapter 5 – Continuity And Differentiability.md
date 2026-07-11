

# CONTINUITY AND  DIFFERENTIABILITY 

出The whole of science is nothing more than a refinement of everyday thinking."ALBERTEINSTEIN :

### 5.1 Introduction 

This chapter is essentially a continuation of our study of differentiation of functions in Class XI. We had learnt to differentiate certain functions like polynomial functions and trigonometric functions. In this chapter, we introduce the very important concepts of continuity, differentiability and relations between them. We will also learn differentiation of inverse trigonometric functions. Further, we introduce a new class of functions called exponential and logarithmic functions. These functions lead to powerful techniques of differentiation. We illustrate certain geometrically obvious conditio l.Is,will learn some fundamental theorems in this area.

### 5.2 Continuity 

<div style="text-align: center;"><img src="imgs/img_in_image_box_637_475_881_808.jpg" alt="Image" width="26%" /></div>


<div style="text-align: center;">Sir Issac Newton (1642-1727)</div>


We start the section with two informal examples to get a feel of continuity. Consider the function 



$$f(x)=\left\{\begin{aligned}&1,if x\leq0\\ &2,if x>0\end{aligned}\right.$$

This function is of course defined at every point of the real line. Graph of this function is given in the Fig 5.1. One can deduce from the graph that the value of the function at nearby points on x-axis remain close to each other except at $x=0$ . At the points near and to the left of 0, i.e., at points like $-0.1,-0.01,-0.001$ 3the value of the function is 1.At the points near and to the right of 0, i.e., at points like 0.1, 0.01,

<div style="text-align: center;"><img src="imgs/img_in_image_box_519_950_871_1225.jpg" alt="Image" width="37%" /></div>


<div style="text-align: center;">Fig 5.1</div>


$0.001$ ,the valueoftefuntini2.ig telnuaeof tnd ithand limits may say thatthe left (respectively right) hand limitoff at 0is1 (respectively2).In particularthe leftand righthand limits donotcoincide.Wealsoobservethat thevalue of the function at $x=0$ concides with the left hand limit. Note that when we try to draw theahiei,paper, we can not draw the graph of this function.In fact, we need to lift the pen when w $x=0$ .

Now, consider the function defined as 

$$f(x)=\left\{\begin{aligned}&1,if x\neq0\\ &2,if x=0\end{aligned}\right.$$

are both equal to 1. But the value of the function at $x=0$ equals 2 which does not coincide with the common value of the left and right hand limits. Again, we note that we cannot draw the graph of the function without lifting the pen. This is yet another instance of a function being not continuous at $x=0$ 

Naively, we may say that a function is continuous at a fixed point if we can draw the graph of the function around that point without lifting the pen from the plane of the paper.

$$广西i y=1 ,$$

<div style="text-align: center;">Fig 5.2</div>


$$x=0$$

Mathematically, it may be phrased precisely as follows:

Definition 1 Suppose is a real function on a subset of the real numbers and let c be a point in the domain off. Thenf is continuous at c if 

$$\lim_{x\to c}f(x)=f(c)$$

More elaborately, if the left hand limit, right hand limit and the value of the function at $x=c$ exist and equal to each other, thenf is said to be continuous at $x=c$ .Recall that if the right hand and left hand limits at $x=c$ coincide, then we say that the common value is the limit of the function at $x=c$ . Hence we may also rephrase the definition of continuity as follows: a function is continuous at $x=c$ if the function is defined at $x=c$ and if the value of the function at $x=c$ equals the limit of the function at $x=c$ . Iff is not continuous at $c,$ we say is discontinuous at andiscalled a point of discontinuity of f.



Example 1 Check the continuity of the functionf given by $f(x)=2x+3at x=1$ 

Solution First note that the function is defined at the given point $x=1$ and its value is 5.Then find the limit of the function at…$x=1$ .Clearly 

Thus 

$$\begin{aligned}&\lim_{x\to1}f(x)=\lim_{x\to1}(2x+3)=2(1)+3=5\\&\lim_{x\to1}f(x)=5=f(1)\end{aligned}$$

Hence, f is continuous at $x=1$ 

Example 2 Examine whether the functionf given by $f(x)=x^{2}$ is continuous at $x=0$ 1

Then find the limit of the function at Solun     iis $x=0$ . Clearly ned at thegiven point   $$ and its value is 0. 

Thus 

$$\lim_{x\to0}f(x)=\lim_{x\to0}x^2=0^2=0$$

Hence,f is continuous at $x=0$ 

Solution By definition ep cYaGentowlb $$ 

$$f(x)=\left\{\begin{aligned}-x,&if x<0\\x,&if x\geq0\end{aligned}\right. ep $$

Clearly the function is defined at 0 and $f(0)=0$ .Left hand limit of f at 0 is 

$$\lim_{x\to0^{-}}f(x)=\lim_{x\to0^{-}}(-x)=0$$

Similarly, te riht hand limt of at 0 is 

$$\lim_{x\to0^{+}}f(x)=\lim_{x\to0^{+}}x=0$$

Thus, the lefthand limit, right hand limit and the value of the function coincide at $x=0$ . Hence,f is continuous at $x=0$ 1.



Example 4 Show that the functionf given by 

$$f(x)=\left\{\begin{aligned}&x^{3}+3,if x\neq0\\ &1,\quad if x=0\end{aligned}\right.$$

is not continuous at $x=0$ ~

Solution The function is defined at $x=0$ and its value at $x=0$ is 1. When $x\neq0$ ,the function is given by a polynomial. Hence,

$$\lim_{x\to0}f(x)=\lim_{x\to0}(x^3+3)=0^3+3=3$$

Since the limit $\mathrm{of}\mathrm{f}\mathrm{at}x=0$ does not coincide with $f(0)$ , the function is not continuous at $x=0$ .It may be noted that $x=0$ is the only point of discontinuity for this function.Example 5 Check the points where the constant function $f(x)=k$ is continuous.

Solution The function is defined at all real numbers and by definition,its value at any real number equals . Let c be any real number. Then 

$$\lim_{x\to c}f(x)=\lim_{x\to c}k=k $$

Since $f(c)=k=\lim_{x\to c}f(x)$ for any real number , the function  is continuous at every real number.



Example6Provethattheidentityfunctiononrealnumbersgivenby $f(x)=x$ is continuous at every real number.



Solution The function is clearly definedat every point ar $f(c)=c$ for every real number c. Also,

$$\lim_{x\to c}f(x)=\lim_{x\to c}x=c $$

Thus,$\lim_{x\to c}f(x)=c=f(c)$ and hence the function is continuous at every real number.

Having defined continuity of a function at a given point, now we make a natural extension of this definition to discuss continuity of a function.

Definition 2 A real functionf is said to be continuous ifit is continuous at every point in the domain off.



This definition requires a bit of elaboration. Suppose is a function defined on a closed interval [a, ], then forf to be continuous, it needs to be continuous at every point in [, ] including the end points a and b. Continuity off at a means 

$$\lim_{x\to a^{+}}f(x)=f(a)$$

and continuity off at b means 

$$\lim_{x\to b^{-}}f(x)=f(b)$$

Observe that $\mathrm*{lim}_{x\to a^{-}}f(x)\quad a n d\quad\mathrm*{lim}_{x\to b^{+}}f(x)$ do not make sense. As a consequence 

of this definition,ifisdefinedonly atone poin,itis continuousthere,i.e.,if the domain of f is a singleton, is a continuous function.



Example 7 Is the function defined by $f(x)=|x|$ ,a continuous function?Solution We may rewrite f as 



$$f(x)=\left\{\begin{aligned}-x,&if x<0\\x,&if x\geq0\end{aligned}\right.$$

By Example 3, we know that f is continuous at $x=0$ J.

Let c be a real number such that $c\leq0$ .Then $f(c)=-c$ . Also 

$$\lim_{x\to c}f(x)=\lim_{x\to c}(-x)=-c $$

Since $\lim_{x\to c}f(x)=f(c)$ , iscontinuoullativeealu mbers.

Now, let c be a real number such that $c\geq0$ .Then $f(c)=c$ .A s 

$$\lim_{x\to c}f(x)=\lim_{x\to c}x=c\quad(\mathrm{Why?})$$

Since $\lim_{x\to c}f(x)=f(c)$ iscontnuousltive 司a ,is continuous at all points.



Example 8 Discuss the continuity of the function f given by $f(x)=x^{3}+x^{2}-1$ 

Solution Clearly is defined at every real number  and its value at c is $c^{3}+c^{2}-1$ .We also know that 



$$\lim_{x\to c}f(x)=\lim_{x\to c}(x^3+x^2-1)=c^3+c^2-1$$

Thus $\lim_{x\to c}f(x)=f(c)$ , and hencef is continuous at every real number. This means f is a continuous function.



Example 9 Discuss the continuity of the functionf defined by $f(x)=\frac{1}{x},x\neq0$ 

 Solution Fix any non zero real number , we have 

$$\lim_{x\to c}f(x)=\lim_{x\to c}\frac{1}{x}=\frac{1}{c}$$

Also, since for $c\neq0$ $f(c)=\frac{1}{c}$ , we have $\lim_{x\to c}f(x)=f(c)$ and hence,f is continuous at every point in the domain off. Thusf is a continuous function.

Weake the function $f(x)=\frac{1}{x}\quad near x=0$ .To carry out this analysis we follow the usual trick of fiil findthetitoft.ill.

<div style="text-align: center;">Table 5.1</div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>x</td><td>1</td><td>0.3</td><td>0.2</td><td>$0.1=10^{-1}$</td><td>$0.01=10^{-2}$</td><td>$0.001=10^{-3}$</td><td>$10^{-n}$</td></tr><tr><td>$f(x)$</td><td>1</td><td>3.333...</td><td>5</td><td>10</td><td>$100=10^{2}$</td><td>$1000=10^{3}$</td><td>10″</td></tr></table></body></html></div>


We observe that as x gets closer to 0 from the right, the value of $f(x)$ shoots up higher.Thiaead ${\bf f}f(x)$ may be made lrger than any given number bychoosin apositiveralnumberverycloseto.Inymbols, wewi 

$$\lim_{x\to0^{+}}f(x)=+\infty $$

(to be read as: the right hand limit $\mathrm{of}f(x)$ at 0 is plus infinity).wish to emphasise that + ∞ is NOT a real number and hence the right hand limit off at 0 does not exist (as a real number).



Similarly, the left hand limit off at 0 may be found. The following table is self explanatory.



<div style="text-align: center;">Table 5.2</div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>x</td><td>-1</td><td>-0.3</td><td>-0.2</td><td>-10</td><td>$-~10^{-2}$</td><td>-10⁻3</td><td>-10−n</td></tr><tr><td>$f(x)$</td><td>-1</td><td>–3.333.</td><td>-5</td><td>-10</td><td>-10²</td><td>-10³</td><td>–10"</td></tr></table></body></html></div>


From the Table 5.2, we deduce that the value of $f(x)$ may be made smaller than any given number by choosing a negative real number very close to 0. In symbols,we write 



$$\lim_{x\to0}f(x)=-\infty $$

(to be read as: the left hand limit of $f(x)$ at 0 is minus infinity). Again, we wish to emphasise that – ∞ is NOT a real number and hence the left hand limit off at 0 does not exist (as a real number). The graph of the reciprocal function given in Fig 5.3 is a geometric representation of the above mentioned facts.



<div style="text-align: center;"><img src="imgs/img_in_image_box_503_859_887_1242.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">Fig 5.3</div>


Example10Discuss thecontinuity of the functionf defined by 

$$f(x)=\left\{\begin{aligned}x+2,&if x\leq1\\x-2,&if x>1\end{aligned}\right.$$

Solution Thefunctionis defned atall pointsofthe real line.

Case 1 If $c\leq1$ ,then $f(c)=c+2$ . Therefore,$\lim_{x\to c}f(x)=\lim_{x\to c}(x+2)=c+2$ 

Thus,f is continuous at all real numbers less than 1.

Case 2 If $c\geq1$ ,thn $f(c)=c-2$ .Therefore,

$$\lim_{x\to c}f(x)=\lim_{x\to c}(x-2)=c-2=f(c)$$

Thus,f is continuous at all points $x\geq1$ 

$x=1$ is If $c=1$ the te let han       a ”

$$\lim_{x\to1^{-}}f(x)=\lim_{x\to1^{-}}(x+2)=1+2=3$$

The right hand limit of f at $x=1$ _is 

$$\lim_{x\to1^{+}}f(x)=\lim_{x\to1^{+}}(x-2)=1-2=-1$$

do not coincide, is not continuous at Sincethe ltad it hadimof .$x=1$ $f\mathrm{at}x=1$ .. Hence T Hence 

<div style="text-align: center;"><img src="imgs/img_in_image_box_549_376_869_697.jpg" alt="Image" width="34%" /></div>


<div style="text-align: center;">Fig 5</div>


$x=1$ i      iven in Fig 5.4.

Example 11 Find al the points of discontinuity of the functionf defined by 

$$f(x)=\left\{\begin{aligned}x+2,&if x<1\\0,&if x=1\\x-2,&if x>1\end{aligned}\right.$$

Solution As in the previous example we find thatf is continuous at all real numbers $x\neq1$ . The left hand limit $\mathrm{of}\;\mathrm{at}\;x=1$ is 

$$\lim_{x\to1^{-}}f(x)=\lim_{x\to1^{-}}(x+2)=1+2=3$$

The right hand limit off at $x=1$ is 

$$\lim_{x\to1^{+}}f(x)=\lim_{x\to1^{+}}(x-2)=1-2=-1$$

Since, the left and right hand limits $\mathrm{of}\mathrm{f}\mathrm{at}x=1$ do not coincide,f is not continuous at $x=1$ .Hence $x=1$ is the only point of discontinuity of f. The graph of the function is given in the Fig 5.5.

<div style="text-align: center;"><img src="imgs/img_in_image_box_552_900_869_1228.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;">Fig 5.5</div>


Example 12 Discuss the continuity of the function defined by 

$$f(x)=\left\{\begin{aligned}x+2,&if x<0\\-x+2,&if x>0\end{aligned}\right.$$

Solution Observethatthefunctioisdefindatallalumbersxceptat.Domin of definition of this function is 

<div style="text-align: center;"><img src="imgs/img_in_image_box_557_328_864_650.jpg" alt="Image" width="32%" /></div>


<div style="text-align: center;">Fig 5.6</div>


$$\mathrm{D}_{1}\cup\mathrm{D}_{2}\text{where}\mathrm{D}_{1}=\{x\in\mathbf{R}:x<0\}\text{and}\mathrm{D}_{2}=\{x\in\mathbf{R}:x>0\}$$

Case1 If $c\in\mathrm{D}_{1}$ ,then $\lim_{x\to c}f(x)=\lim_{x\to c}(x+2)$ 

$c+2=f(c)$ and hencef is continuous in $ D_{r}$ 

Case 2 If $c\in\mathrm{D}_2$ ,then $\lim_{x\to c}f(x)=\lim_{x\to c}(-x+2)$ 

$-c+2=f(c)$ and hence f is continuous in $\mathrm{D}_{21}^{-}$ Sincef is continuous at all points in the domain off we deduce that $f$ is continuous. Graph of this function is given in the Fig 5.6. Note that to graph this function we need to lift the pen from the plane 

of the paper, but we need to do thatonly for those points where thefunction is ot defined.



Example 13 Discuss the continuity of the functionf given by 

$$f(x)=\left\{\begin{aligned}x,\quad&if x\geq0\\x^2,\quad&if x<0\end{aligned}\right.$$

Solution Clearly the function is defined at every real number. Graph of the function is given in Fig 5.7.By inspection, it seems prudent to partition the domain of definition of f into three disjoint subsets of the real line.

Let 

$$\begin{array}{l}\mathrm{D}_{1}=\{x\in\mathbf{R}:x<0\},\mathrm{D}_{2}=\{0\}\\ \mathrm{D}_{3}=\{x\in\mathbf{R}:x>0\}\end{array} and $$

<div style="text-align: center;"><img src="imgs/img_in_image_box_515_806_863_1075.jpg" alt="Image" width="37%" /></div>


<div style="text-align: center;">Fig 5.7</div>


Case 1 At any point in $\mathrm{D}_{\mathrm{r}}$ , we have $f(x)=x^{2}$ and it is easy to see that it is continuous there (see Example 2).



Case 2 At any point in 。$ D_{3}$ we have $f(x)=x$ and it is easy to see that it is continuous there (see Example 6).



Case 3 Now we analyse the function at $x=0$  The value of the function at 0 is $f(0)=0$ The left hand limit of f at 0 is 



$$\lim_{x\to0^{-}}f(x)=\lim_{x\to0^{-}}x^2=0^2=0$$

The right hand limit off at  is 

$$\lim_{x\to0^{+}}f(x)=\lim_{x\to0^{+}}x=0$$

Thus $\lim_{x\to0}f(x)=0=f(0)$ and hencef is continuous at 0. This means that f is 

continuous at every point in its domain and hence, is a continuous function.

Example 14 Show that every polynomial function is continuous.



Solution Recall that a function p is a polynomial function if it is defined by $p(x)=a_{0}+a_{1}x+\ldots+a_{n}x^{n}$ for some natural number n,$a_{n}\neq0$ and $a_{i}\in\mathbb{R}$ .Clearly this function is defined for every real number. For a fixed real number c, we have 

$$\lim_{x\to c}p(x)=p(c)$$

By definition, p is continuous at c. Since c is any real number, p is continuous at every real number and hence p is a continuous function.



Example15Find all the points of discontinuity of the greatest integer function defined by.$f(x)=[x]$ , where [x] denotes the greatest integer less than or equal to .

Solution First observe thatf is defined for all real numbers. Graph of the function is given in Fig 5.8.From the graph it looks like that is discontinuous at every integral cYanmaGaYGetYYYYtYowb 

<div style="text-align: center;"><img src="imgs/img_in_image_box_186_851_718_1239.jpg" alt="Image" width="56%" /></div>


<div style="text-align: center;">Fig 5.8</div>


Case 1 Letbe a real number whichis not equal to any integer.It isevident from the graph thatforall realnumbersclosetocthevalueofthefunctionisequalto[; ,$\lim_{x\to c}f(x)=\lim_{x\to c}[x]=[c].\quad\mathrm{Also}f(c)=[c]$ and hence the function is continuous at all real numbers not equal to integers.



Case 2 Let c be an integer. Then we can find a sufficiently small real number $r\geq0$ such that $[c-r]=c-1$ whereas $[c+r]=c$ 



This, in terms of limits mean that 

$$\lim_{x\to c^{-}}f(x)=c-1,\quad\lim_{x\to c^{+}}f(x)=c $$

Since these limits cannot be equal to each other for any c, the function is discontinuous at every integral point.



#### 5.2.1 Algebra of continuous functions 

In the previous class, after having understood the concept of limits, we learnt some algebra oflimits.Analogously,ow we will tudy ome algbraofcontinuous functios.Sincecontuityofuctiotpoitisntilytdbythelimitoftefunctiont that point, it is reasonable to expect results analogous to the case of limits.

Theorem 1 Suppose f and g be two real functions continuous at a real number c.Then rep 

(1).$f+g$ is continuous at $x=c$ 

(2)$f-g$ is continuous at $x=c$ 

(3) f . g is continuous at $x=c$ 

(4)$\left(\frac{f}{g}\right)$ is continuous at $x=c$ , (provided $g(c)\neq0$ ).

Proof We are investigating continuity of $(f+g)at x=c$ . Clearly it is defined at $x=c$  We have 



$$\begin{aligned}\lim_{x\to c}(f+g)(x)&=\lim_{x\to c}[f(x)+g(x)]&(by definition of f+g)\\&=\lim_{x\to c}f(x)+\lim_{x\to c}g(x)&(by the theorem on limits)\\&=f(c)+g(c)&(as f and g are continuous)\\&=(f+g)(c)&(by definition of f+g)\end{aligned}$$

Hence,$f+g$ is continuous at $x=c$ 

Proofs for the remaining parts are similar and left as an exercise to the reader.

## Remarks 

(iAsspcialcaseof)abovificontntfunctoi.$f(x)=\lambda$ . for some real number λ, then the function (λ . g) defined by $(\lambda_{\mathrm{~.~}}g)(x)=\lambda_{\mathrm{~.~}}g(x)$ is also continuous. In particular if $\lambda=-1$ , the continuity off implies continuity $ of-f.$ (ii)As a special case of (4) above,iff is the constant function $f(x)=\lambda$ ,then the function $\frac{\lambda}{g}$ defined by $\frac{\lambda}{g}(x)=\frac{\lambda}{g(x)}$ is also continuous wherever $g(x)\neq0$ In particular, the continuity ofg implies continuity of $\frac{1}{g}$ 



The above theorem can be exploited to generate many continuous functions. They alsoaid indecidingicertainfunctions arecontiuous ornot.Teollowing examples illustrate this:Ta 

tinuous.

by 

$$f(x)=\frac{p(x)}{q(x)},\;q(x)\neq0$$

where p and q are polynomial functions. The doma nfsalam points at whichi oice plynomialfunction areontinuous(Example),f is continuous by (4) of Theorem 1



Example 17 Discuss the continuity of sine function.

Solution To see this we use the following facts 

$$\lim_{x\to0}\sin x=0$$

We have not proved it, but is intuitively clear from the graph of sin x near 0.

Now, observe that $f(x)=\sin$ x is defined for every real number. Let c be a real number. Put not $x=c+h\mathrm{If}x\rightarrow c$ we know that $h\to0$ .Therefore 

$$not \begin{aligned}\lim_{x\to c}f(x)&=\lim_{x\to c}\sin x\\&=\lim_{h\to0}\sin(c+h)\\&=\lim_{h\to0}\left[\sin c\cos h+\cos c\sin h\right]\\&=\lim_{h\to0}\left[\sin c\cos h\right]+\lim_{h\to0}\left[\cos c\sin h\right]\\&=\sin c+0=\sin c=f(c)\end{aligned}$$

Thus $\lim_{x\to c}f(x)=f(c)$ and hence f is a continuous function.

Remark A similar proof may be given for the continuity of cosine function.

Example 18 Prove that the function defined by $f(x)=\tan x$ is a continuous function.

 Solution The function $f(x)=\tan x=\frac{\sin x}{\cos x}$ . This is defined for all real numbers such 

that cos $x\ne0,i.e.,x\ne(2n+1)\frac{\pi}{2}$ . We have just proved that both sine and cosine functions are continuous. Thus tan x being a quotient of two continuous functions is continuous wherever it is defined.



An interesting fact is the behaviour of continuous functions with respect to composition of functions. Recall that iff and g are two real functions, then 

$$(f\circ g)(x)=f(g(x))$$

is defined whenever the range $\mathrm{of}g$ is a subset of domain of f. The following theorem (stated without proof) captures the continuity of composite functions.

Theorem 2 Supposef and g are real valued functions such that $(f\mathrm{o}g)$ is defined at c.Ifg is continuous at c and iff is continuous at $\bar{g}(c)$ then $(f o g)$ is continuous at c.

The following examples illustrate this theorem.

Example 19 Show that the function defined by $f(x)=\sin(x^2)$ is a continuous function.

Solution Observe that the function is defined for every real number. The function f may be thought of as a composition $g^{\mathrm{~o~}}h$ of the two functions g and h, where $g\left(x\right)=\sin x\ and h\left(x\right)=x^{2}$ .Since both g and h are continuous functions, by Theorem 2,it can be deduced thatf is a continuous function.



Example 20 Show that the function f defined by 

$$f(x)=|1-x+|x||,$$

where x is any real number, is a continuous function.

Solution Define g by $g(x)=1-x+|x|$ andh by $h\left(x\right)=\left|x\right|$ for all real x. Then 

$$\begin{aligned}h\left(h\ \circ\ g\right)\left(x\right)&=h\left(g\left(x\right)\right)\\&=h\left(1-x+\left|x\right|\right)\\&=\left|1-x+\left|x\right|\right|=f\left(x\right)\end{aligned}$$

In Example 7, we have seen that h is a continuous function. Hence g being a sum of a polynomial function and the modulus function is continuous. But thenf being a composite of two continuous functions is continuous.



### EXERCISE 5.1

1. Prove that the function $f(x)=5x-3$ is continuous at $x=0$ ,at $x=-3$ and at $x=5$ 

2. Examine the continuity of the function $f(x)=2x^2-1at x=3$ 

3.Examinethellowing functions for continut 

(a)

$$(a)f(x)=x-5$$

(b)

$$f(x)=\frac{1}{x-5},x\neq5$$

$$f(x)=\frac{x^{2}-25}{x+5},x\neq-5\quad(d)\quad f(x)=|x-5|$$

4. Prove that the function $f(x)=x^n$ is continuous at $x=n$ , where n is a positive integer.



5. Is the functionf defined by 

$$f(x)=\left\{\begin{aligned}x,&if x\leq1\\ 5,&if x>1\end{aligned}\right.$$

continuous at $x=0?\mathrm{At}x=1?\mathrm{At}x=2?$ 

Find all points of discontinuity off, where f is defined by 

6.

$$f(x)=\left\{\begin{aligned}&2x+3,if x\leq2,\\ &2x-3,if x>2.\end{aligned}\right.$$

$$f(x)=\left\{\begin{aligned}&|x|+3,if x\leq-3\\ &-2x,if-3<x<3\\ &6x+2,if x\geq3\end{aligned}\right.$$

8.

$$f(x)=\left\{\begin{aligned}\frac{|x|}{x},&\text{if}x\neq0\\ 0,&\text{if}x=0\end{aligned}\right.$$

9

$$f(x)=\left\{\begin{aligned}&\frac{x}{|x|},if x<0\\&-1,if x\geq0\end{aligned}\right.$$

10.

$$f(x)=\left\{\begin{aligned}x+1,\ if x\geq1\\x^{2}+1,\ if x<1\end{aligned}\right. v f(x)=\left\{\begin{aligned}x+1,\ if x\geq1\\x^{2}+1,\ if x<1\end{aligned}\right.$$

1

$$f(x)=\left\{\begin{aligned}&x^{3}-3,\quad if x\leq2\\ &x^{2}+1,\quad if x>2\end{aligned}\right.$$

112.$f(x)=\begin{cases}x^{10}-1,&if x\leq1\\x^2,&if x>1\end{cases}$ 13. Is the function defined by 

$$f(x)=\left\{\begin{aligned}x+5,\quad&if x\leq1\\x-5,\quad&if x>1\end{aligned}\right.$$

a continuous function?

Discuss the continuity of the functionf, where f is defined by 

$$f(x)=\left\{\begin{aligned}&3,if0\leq x\leq1\\&4,if1<x<3\\&5,if3\leq x\leq10\end{aligned}\right.\quad 又.\quad f(x)=\left\{\begin{aligned}&2x,if x<0\\&0,\quad if0\leq x\leq1\\&4x,if x>1\end{aligned}\right.$$

.

$$f(x)=\left\{\begin{aligned}ax+1,\quad&if x\leq3\\bx+3,\quad&if x>3\end{aligned}\right.$$

is continuous at $x=3$ 

18. For what value ofλ is the function defined by 

$$f(x)=\left\{\begin{aligned}&\lambda(x^{2}-2x),&if x\leq0,\\&4x+1,&if x>0.\end{aligned}\right.$$

continuous at $x=0?$ What about continuity at $x=1?$ 

19. Show that the function defined by $g(x)=x-[x]$ is discontinuous at all integral points. Here [x] denotes the greatest integer less than or equal to .

20. Is the function defined by $f(x)=x^{2}-\sin x+5$ continuous at $x=\pi?$ 

21. Discuss the continuity of the following functions:

$$\begin{aligned}&(a)\ f(x)=\sin x+\cos x\quad(b)\ f(x)=\sin x-\cos x\\ &(c)\ f(x)=\sin x.\cos x\\ \end{aligned}$$

22. Discuss the continuity of the cosine, cosecant, secant and cotangent functions.

23. Find all points of discontinuity off, where 

$$f(x)=\left\{\begin{aligned}&\frac{\sin x}{x},\quad if x<0\\&x+1,\quad if x\geq0\end{aligned}\right.$$

24. Determine if f defined by 

$$f(x)=\left\{\begin{aligned}&x^{2}\sin\frac{1}{x},&if x\neq0\\ &0,&if x=0\end{aligned}\right.$$

is a continuous function?

25. Examine the continuity off, wheref is defined by 

$$f(x)=\left\{\begin{aligned}&\sin x-\cos x,\quad if x\neq0,\\&-1,\quad if x=0.\end{aligned}\right.$$

Find theofuuutd t inxies 26 to 29.



26.

$$f(x)=\left\{\begin{aligned}&\frac{k\cos x}{\pi-2x},\quad if x\neq\frac{\pi}{2}\\&3,\quad if x=\frac{\pi}{2}\end{aligned}\right.\quad at x=\frac{\pi}{2}$$

27.

$$f(x)=\begin{cases}kx^{2},&if x\leq2\\3,&if x>2\end{cases}\quad at x=2$$

28.

$$f(x)=\left\{\begin{aligned}kx+1,\quad&if x\leq\pi\\\cos x,\quad&if x>\pi\end{aligned}\right.$$

$$at x=\pi $$

29.

$$f(x)=\left\{\begin{aligned}kx+1,\quad if\quad x\leq5\\3x-5,\quad if\quad x>5\end{aligned}\right.$$

$$at x=5$$

30.Find the values of a and b such that the function defined by 

$$f(x)=\left\{\begin{aligned}&5,&if x\leq2\\ &ax+b,&if2<x<10\\ &21,&if x\geq10\end{aligned}\right.$$

is a continuous function.

31.Show that the function defined by $f(x)=\cos(x^2)$ is a continuous function.

32.Show that the function defined by $f(x)=|\cos x|$ is a continuous function.

33. Examine that sin $|x|$ is a continuous function.

34. Find all the points of discontinuity off defined by $f(x)=|x|-|x+1|$ 

#### 5.3. Differentiability 

Recall the following facts from previous class. We had defined the derivative of a real function as follows:

Suppose is a ral function andis a point in its domain. The derivativeof at c is defined by 



$$\lim_{h\to0}\frac{f(c+h)-f(c)}{h}$$

providedthis limtexits.Deivativeofatisdenotedy $f^{\prime}(c)\mathrm{or}\frac{d}{dx}(f(x))|_{c}$ . The function defined by 



$$f^{\prime}(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$$

wherever the limit exists is defined to be the derivative off. The derivative of f is denoted by $f^{\prime}(x)or\frac{d}{dx}(f(x))or if y=f(x)by\frac{dy}{dx}or y^{\prime}$ . The process of finding derivativeofafunction is called diferentiation. We also use the phrase differentiate $f(x)$ with respect to x to mean find $f^{\prime}(x)$ 



The following rules were established as a part of algebra of derivatives:olisi 

(1)

$$(u\pm v)^{\prime}=u^{\prime}\pm v^{\prime}$$

(2)

)$(u v)^{\prime}=u^{\prime}v+u v^{\prime}$ (Leibnitz or product rule)

(3)

$$\left(\frac{u}{v}\right)'=\frac{u'v-uv'}{v^2},wherever v\neq0(Quotient rule),$$

The following table givs a list of derivatives of rtain standardfunctions:

<div style="text-align: center;">Table 5.3</div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>$f(x)$</td><td>$x^{n}$</td><td>sinx</td><td>cosx</td><td>tanx</td></tr><tr><td>$f^{\prime}({\bar{x}})$</td><td>$n x^{n-1}$</td><td>cosx</td><td>−sin x</td><td>$\sec^{2}x$</td></tr></table></body></html></div>


Whenever we defined derivative, we had put a caution provided the limit exists.Nowthel uioi;titt?Teuiuitdis its answer. If $\lim_{h\to0}\frac{f(c+h)-f(c)}{h}$ does not exist, we say that  is not differentiable at c.Inother oreyttucioirtaltiiitsomaiifboth $\lim_{h\to0^-}\frac{f(c+h)-f(c)}{h}\quad and\quad\lim_{h\to0^+}\frac{f(c+h)-f(c)}{h}$ are finite and equal. A function is said tobeiil[]iir[, ].incasefitand limit,oion ataandspctily.imllyuctioiaidtobiftableiainterval $(a,b)$ iit is ier  of $(a,b)$ .



TheormIuitiiuu a point.



Proof Since  is differentiable at , we have 

$$\lim_{x\to c}\frac{f(x)-f(c)}{x-c}=f'(c)$$

But for $x\neq c.$ , we have 

Therefore 

or 

or 

$$\begin{aligned}f(x)-f(c)&=\frac{f(x)-f(c)}{x-c}.(x-c)\\\lim_{x\to c}[f(x)-f(c)]&=\lim_{x\to c}\left[\frac{f(x)-f(c)}{x-c}.(x-c)\right]\\\left[\lim_{x\to c}[f(x)]-\lim_{x\to c}[f(c)]\right]&=\lim_{x\to c}\left[\frac{f(x)-f(c)}{x-c}\right].\lim_{x\to c}[(x-c)]\\&=f(c).0=0\\\lim_{x\to c}f(x)&=f(c)\\&=f(c).0=0\end{aligned} ied $$

Hence f is continuous at $x=c$ 

Corollary 1 Every differentiable function is continuous.

We remark that the converse of the above statement is not true. Indeed we have seen that the function defined by $f(x)=|x|$ is a continuous function. Consider the left hand limit 



$$\lim_{h\to0^-}\frac{f(0+h)-f(0)}{h}=\frac{-h}{h}=-1$$

The right hand limit 

$$\lim_{h\to0^{+}}\frac{f(0+h)-f(0)}{h}=\frac{h}{h}=1$$

Since the above left and right hand limits at 0 are not equal,$\lim_{h\to0}\frac{f(0+h)-f(0)}{h}$ does not exist and hence $f$ is not differentiableat .Thus is nota diffentiable function.



#### 5.3.1 Derivatives of composite functions 

To study derivative ofcomposite functions, we start with an illustrative exampl. Say,we want to find the derivative $\mathrm{of}f_{z}$ where 

$$f(x)=(2x+1)^3$$

One way is to expand $(2x+1)^{3}$ using binomial theorem and find the derivative as a polynomial function as illustrated below.



Now, observe that 

$$\begin{aligned}\frac{d}{dx}f(x)&=\frac{d}{dx}\left[(2x+1)^3\right]\\&=\frac{d}{dx}\left(8x^3+12x^2+6x+1\right)^3\\&=24x^2+24x+6\\&=6(2x+1)^2\\f(x)&=(h\circ g)(x)\end{aligned}$$

where $g(x)=2x+1and h(x)=x^3$ .Put $t=g(x)=2x+1$ .Then $f(x)=h(t)=t^3$ 

$$\frac{df}{dx}=6(2x+1)^{2}=3(2x+1)^{2}.2=3t^{2}.2=\frac{dh}{dt}.\frac{dt}{dx}$$

Theadvataewthsuchbrvaioithitimlifietealculaioi fndig the derivative $\mathrm{of}_{z}$ say,$(2x+1)^{100}$ . We may formalise this observation in the following theorem called the chain rule.



Theorem 4 (Chain Rule) Letf be a real valued function which is a composite of two functions u and $v;\mathrm{i.e.},f=v0u\mathrm{Suppose}t=u(x)$ and if both $\frac{dt}{dx}\bmod\frac{dv}{dt}$ exist, we have 

<div style="text-align: center;"><img src="imgs/img_in_image_box_275_784_340_849.jpg" alt="Image" width="6%" /></div>


$$\frac{df}{dx}=\frac{dv}{dt}\cdot\frac{dt}{dx}$$

We skip the proof of this theorem. Chain rule may be extnded as folows. Suppose f is a real valued function whichis acompositeofthreefunctions u,v and w;i.,

$f=(w\circ u)\circ v.\mathrm{If}t=y(x)$ and $s=u\left(t\right)$ _, then 

$$\frac{df}{dx}=\frac{d(w\circ u)}{dt}\cdot\frac{dt}{dx}=\frac{dw}{ds}\cdot\frac{ds}{dt}\cdot\frac{dt}{dx}$$

provided alltherivativesinthetatemntexi.Raderisinvidtformulatechain rule for composite of more functions.



Example 21 Find the derivative of the function given by $f(x)=\sin(x^2)$ 

Solution Observe that the given function is a composite of two functions. Indeed, if $t=u(x)=x^2\mathrm{and}v(t)=\sin t,$ then 



$$f(x)=(v\circ u)(x)=v(u(x))=v(x^2)=\sin x^2$$

Put $t=u(x)=x^{2}$ . Observe that $\frac{dv}{dt}=\cos t\quad and\quad\frac{dt}{dx}=2x$ exist. Hence, by chain rule 

$$\frac{df}{dx}=\frac{dv}{dt}\cdot\frac{dt}{dx}=\cos t\cdot2x $$

It is normal practice to express the final result only in terms of x. Thus 

$$\frac{df}{dx}=\cos t\cdot2x=2x\cos x^{2}$$

### EXERCISE 5.2

ttoxinExercises to 8.

1. sin $(x^{2}+5)$ 2.$\cos\left(\sin x\right)$ T人3.sin (c $$ ,

4. sec $(\tan({\sqrt[]{x}}))$ 5.$\frac{\sin(ax+b)}{\cos(cx+d)}$ ？:$ x^3}.sin2(x5)(x()

7.$2\sqrt{\cot\left(x^{2}\right)}$ 8.$\cos(\sqrt{x})$ 

9.Prove that the functionf given by 

$$f(x)=|x-1|,x\in\mathbb{R}$$

is not differentiable at $x=1$ 

10.Prove that thegreatst integerfunction defined y 

$$f(x)=[x],\;0<x<3$$

is not differentiable at $x=1and x=2$ 

#### 5.3.2 Derivatives of implicit functions 

Until now we have been differentiating various functions given in the form $y=f(x)$ But it is not necessary that functions are always expressed in this form. For example,consider one of the following relationships between x and y:

$$\begin{aligned}x-y-\pi&=0,\\x+\sin xy-y&=0\end{aligned}$$

In the first case, we can solve for y and rewrite the relationship as $y=x-\pi$ .In the second case, it does not seem that there is an easy way to solve for y. Nevertheless,there is no doubt about the dependence of y on x in either of the cases. When a relationship between x and y is expressed in a way that it is easy to solve for y and write $y=f(x)$ ,we say that y is given as an explicit function ofx. In the latter case it  isimlcuofioce,aboveI functions.



Example 22 Find $\frac{dy}{dx}\quad if x-y=\pi$ 

Solution One way isto solveforandrewritethe above as 

But then 

$$\left\{\begin{aligned}y&=x-\pi\\ \frac{dy}{dx}&=1\end{aligned}\right.$$

x 

$$\frac{d}{dx}(x-y)=\frac{d\pi}{dx}$$

eve Recall that $\frac{d\pi}{dx}$ . Thus e0function taking valun 

$$\frac{d}{dx}(x)-\frac{d}{dx}(y)=0 EF -epub $$

which implies that 

$$\frac{dy}{dx}=\frac{dx}{dx}=1 -epub $$

Example 23 Find $\frac{dy}{dx},if y+\sin y=\cos x.$ 

Solution We diferentiatethe relationship directly with respect to x, i.e.,

$$\frac{dy}{dx}+\frac{d}{dx}(\sin y)=\frac{d}{dx}(\cos x)$$

which implies using chain rule 

$$\frac{dy}{dx}+\cos y\cdot\frac{dy}{dx}=-\sin x $$

This gives 

$$\frac{dy}{dx}=-\frac{\sin x}{1+\cos y}$$

where 

$$y\neq(2n+1)\;\pi $$

#### 5.3.3 Derivatives of inverse trigonometric functions 

We remark that inverse trigonometric functions are continuous functions, but we will notprovethis.Now we usechairuletofind derivativesoftheseuctions.

Example 24 Find the derivative off given by.$f(x)=\sin^{-1}$ x assuming it exists.

Solution Let.$y=\sin^{-1}$ . Then,$x=\sin y$ 

Differentiating both sides w.r.t. x, we get 

$$1=\cos y\frac{dy}{dx}$$

which impllies that 

$$\frac{dy}{dx}=\frac{1}{\cos y}=\frac{1}{\cos(\sin^{-1}x)}$$

Observe that this is defined only for cos $y\neq0,\mathrm{i.e.},\sin^{-1}x\neq-\frac{\pi}{2},\frac{\pi}{2},\mathrm{i.e.},x\neq-1,1$ -hed i.e.,$x\in(-1,1)$ 



To make this result a bit more attractive, we carry out the following manipulation.Recall that for $x\in(-1,1)$ ,sin $\left(\sin^{-1}x\right)=x$ and hence 

$$\cos^{2}y=1-(\sin y)^{2}=1-(\sin(\sin x))^{2}=1-x^{2}$$

Also, since $y\in\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$ , cos y is positive and hence cos $y=\sqrt{1-x^{2}}$ 

Thus, for $x\in(-1,1)$ 

$$\frac{dy}{dx}=\frac{1}{\cos y}=\frac{1}{\sqrt{1-x^{2}}}$$


<div style="text-align: center;"><html><body><table border="1"><thead><tr><td>R</td><td>(-1, 1)</td><td>(-1, 1)</td><td>Domain off</td></tr></thead><tbody><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></tbody></table></body></html></div>


### EXERCISE 5.3

Find $\frac{dy}{dx}$ in the following:

$$2x+3y=\sin x\quad2.\quad2x+3y=\sin y\quad3.\quad ax+by^{2}=\cos y\quad4.\quad xy+y^{2}=\tan x+y\quad5.\quad x^{2}+xy+y^{2}=100\quad6.\quad x^{3}+x^{2}y+xy^{2}+y^{3}=81$$

$$\sin^{2}y+\cos xy=\kappa\quad8.\quad\sin^{2}x+\cos^{2}y=1\quad9.\quad y=\sin^{-1}\left(\frac{2x}{1+x^{2}}\right)s republished $$

10.

$$y=\tan^{-1}\left(\frac{3x-x^3}{1-3x^2}\right),\quad-\frac{1}{\sqrt{3}}<x<\frac{1}{\sqrt{3}} s republished $$

11.

$$y=\cos^{-1}\left(\frac{1-x^{2}}{1+x^{2}}\right),0<x<1 CERT s republished $$

12.

$$y=\sin^{-1}\left(\frac{1-x^{2}}{1+x^{2}}\right),0<x<1 CERT s republished $$

13.

$$y=\cos^{-1}\left(\frac{2x}{1+x^{2}}\right),-1<x<1 CERT s republished $$

14.

$$y=\sin^{-1}\left(2x\sqrt{1-x^2}\right),\quad-\frac{1}{\sqrt{2}}<x<\frac{1}{\sqrt{2}} s republished $$

15.

$$y=\sec^{-1}\left(\frac{1}{2x^2-1}\right),\quad0<x<\frac{1}{\sqrt{2}} s republished $$

### 5.4 Exponential and Logarithmic Functions 

Till now we have learnt some aspects of different classes of functions like polynomial functions, rational functions and trigonometric functions. In this section, we shall learn about a new class of (related) functions called exponential functions and logarithmic functions. It needs to be emphasized that many statements made in this section are motivational and precise proofs of these are well beyond the scope of this text.

The Fig 5.9 gives a sketch of $y=f_{1}(x)=x,y=f_{2}(x)=x^{2},y=f_{3}(x)=x^{3}$ and $y=f_{4}(x)$ $=x^{4}$ . Observe that the curves get steeper as the power of x increases. Steeper the curve, faster is the rate of growth. What this means is that for a fixed increment in the value of $x\left(\geq1\right)$ ), the increment in the value of $y=f_{n}(x)$ increases as n increases for n $=1,2,3,4$ . It is conceivable that such a statement is true for all positive values of n,

where $f_{n}(x)=x^{n}$ . Essentially, this means that the graph of $y=f_{n}\left(x\right)$ leans more eeeerer eee eree ae e ir $f_{10}(x)=x^{10}$ u $f_{15}(x)$ $=x^{15}$ If x increases from 1 to 2,$f_{10}$ increases from l to (bi $2^{10}$ whereas $f_{15}$ increases from 1 to $2^{15}$ .Thus, for the same increment in $x,f_{15}$ grow faster than $f_{10^{\prime}}$ 

Upshot of the above discussion is that the growth of polynomial functions is dependent on the degree of the polynomial function – higher the degree, greater is the growth. The next natural question is:

<div style="text-align: center;"><img src="imgs/img_in_image_box_471_139_877_535.jpg" alt="Image" width="43%" /></div>


<div style="text-align: center;">Fig 5.9</div>


Is there a function which grows faster than any polynomial function.The answer is in affirmative and an example of such a function is 

$$y=f(x)=10^{x}.$$

Our claim is that this functionf grows faster than $f_{n}(x)=x^{n}$ for any positive integer n.For example, we can prove that 10* grows faster than $f_{100}(x)=x^{100}$ For large values of x like $x=10^{3}$ , note that $f_{100}(x)=(10^3)^{100}=10^{300}$ whereas $f(10^{3})=10^{10^{3}}=10^{1000}$ Clearly $f(x)$ is much greater than $f_{100}\left(x\right)$ It is not difficult to prove that for all $x>10^{3},f(x)>f_{100}(x)$ .But we will not atempt to give a proofof this here.Similarly b choosing large values of $x.$ one can verify that $f(x)$ grows faster than $f_{n}\left(x\right)$ for any positive integer n.



Definition 3 The exponential function with positive base $b\geq1$ is the function 

$$y=f(x)=b^{x}$$

The graph of $y=10^{x}$ is given in the Fig 5.9.

It is advised that the reader plots this graph for particular values of b like 2, 3 and 4Following are some of the salient features of the exponential functions:

(1)Domainoftheexponentialfunctionis R,thesetof all realnumbers.

(2)Raneofthexpotalfuctioisthetofall oitivealumbrs.

(3)Thepoit(,1)ialwayothaphofhexpotialuctiohii a restatement of the fact that $b^{0}=1$ for any real $b\geq1$ ).

(4)Exilcivinciiaveo graph rises above.



(5)For very largenegativevaluesofx,theexponential functionis verycloseto 0.In other words, in the second quadrant, the graph approaches x-axis (but never meets it).



Exponential function with base 10 is called the common exponential function. In the Appendix A.1.4 of Class XI, it was observed that the sum of the series 

$$1+\frac{1}{1!}+\frac{1}{2!}+\cdots $$

is a number between 2 and 3 and is denoted by e. Using this e as the base we obtain an extremely important exponential function.$y=e^{x}$ 



This is called natural exponential function.

It would be intereting to know if theinverse of the exponential function exiss and has nice interpretation. This search motivates the following definition.

Definition 4 Let $b\geq1$ bea real number.Then wesay logarithmof atobase bis if 

$b^{x}=a$ 



Logarithm of a to base b is denoted $by\log_{b}a$ ,Thus $\log_{b}a=x if b^{x}=a$ . Let us work with a few explicit examples to get a feel for this. We know $2^{3}=8$ . In terms of logarithms, we may rewrite this as log,$8=3.\mathrm{Similary},10^{4}=10000$ is equivalent to saying $\log_{10}10000=4$ .Also,$625=5^{2}=25^{2}$ is equivalent to saying $\log_{5}625=4$ or 

$\log_{25}625=2$ 



On a slightly more mature note, fixing a base $b\geq1$ , we may look at logarithm as a function from positive real numbers to all real numbers. This function,caled the logarithmic function, is defined by 

$$\log_{b}:\mathbf{R}\rightarrow\mathbf{R}\atop x\rightarrow\log_{b}x=y\quad if b^{y}=x ,we say it $$

As before if the base $b=10$ ,we say it is common logarithms and if $b=e$ ,then we say it is natural logarithms. Often natural logarithm is denoted by ln. In this chapter, log x denotes the logarithm function tobase e,i.e., lnx will be written as simply logx. The Fig 5.10 gives the plots of logarithm function to base 2, e and 10.

Some of the important observations about the logarithm function to any base $b>1$ are listed below:

<div style="text-align: center;"><img src="imgs/img_in_chart_box_480_907_866_1218.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">Fig 5.10</div>


(1)Wecaot mmgfuldioogtmof-itivenumbers E0M and henceem o o fuction is S $\mathbf{R}^{+}$ +



(2)EaM]Te 

(3)添Tab 

(i.e., as we move from left to right the graph rises above.



$$(y=e^{x})$$

(5) For x very near to zero, the value of log x can be made lesser than any given real number. In other words in the fourth quadrant the graph approaches $y\mathtt{-a x i s}$ (but never meets it).



(6) Fig 5.11 gives the plot of.$y=e^{x}$ and $y=ln x$ .It is of interest to observe that the two curves are the mirror images of each other reflected in the line 

<div style="text-align: center;">Fig 5.11</div>


Two properties of 'log' functions are proved below:

$$(y=x)$$

$$(y=\log_{e}x)ed $$

(1) There is a standard change of base rule to obtain $\log_{a}p$ in terms of $\log_{b}p$ .Let $\log_{a}p=\alpha,\log_{b}p=\beta\mathrm{and}\log_{b}a=\gamma,$ This means $a^{\alpha}=p,b^{\beta}=p\ and\ b^{\gamma}=a$ 

Substituting the third equation in the first one, we have 

$$(b^{\gamma})^{\alpha}=b^{\gamma\alpha}=p $$

Using this in the second equation, we get 

$$b^{\beta}=p=b^{\gamma\alpha}$$

which implies $\beta=\alpha\gamma or\alpha=\frac{\beta}{\gamma}$ .But then 

$$\log_{a}p=\frac{\log_{b}p}{\log_{b}a}$$

(2)Anotheinteretinpropertyofthlofunctioiitsefctonproducts.Let $\log_{b}p q=\alpha$ .Then $b^{a}=pq$ .If $\log_{b}p=\beta$ and $\log_{b}q=\gamma,$ ,then $b^{\beta}=p\mathrm{and}b^{\gamma}=q$ But then $b^{\alpha}=p q=b^{\beta}b^{\gamma}=b^{\beta+\gamma}$ 



which implies $\alpha=\beta+\gamma$ . , i.e.,

$$\log_{b}p q=\log_{b}p+\log_{b}q $$

A particularly interesting and important consequence of this is when $p=q$ .In this case the above may be rewritten as 

$$\log_{b}p^{2}=\log_{b}p+\log_{b}p=2\log p $$

An easy generalisation of this (left as an exercise!) is 

$$\log_{b}p^{n}=n\log p $$

for any positive integer n. In fact this is true for any real number n, but we will not attempt to prove this. On the similar lines the reader is invited to verify 

$$\log_{b}\frac{x}{y}=\log_{b}x-\log_{b}y $$

Example 25 Is it true that $x=e^{\log x}$ for all real ?

Slutilrs.ed So the above equation is not true for non-positive real numbers.$Now,let y=e^{\log x}$ .If $y>0$ , we may take logarithm which gives us log $y=\log\left(e^{\log x}\right)=\log x\log e=\log x$ .Thus $y=x$ .Hence $x=e^{\log x}$ is true only for positive values of x.



One of the striking properties of the natural exponential function in differential calculusittit'tcaeurterofrtion.Thiicar in the following theorem whose proof we skip.



Theorem $5^{\circ}$ 

(1) The derivative $\mathrm{of}\;e^{x}\;\mathrm{w.r.t.},\;x\;\mathrm{is}\;e^{x},\;\mathrm{i.e.},\;\frac{d}{dx}(e^{x})=e^{x}.$ 

(2) The derivative of log x $\mathrm{w.rt.,}\;x\;\mathrm{is}\;\frac{1}{x};\;\mathrm{i.e.,}\;\frac{d}{dx}(\log x)=\frac{1}{x}$ 

Example 26 Differentiate the following w.r.t. :

(i)$e^{-x}$ (ii)$\sin\left(\log x\right),x>0\quad\left(iii\right)\quad\cos^{-1}\left(e^x\right)$ (iv)$e^{\cos x}$ 

Solution 

(i)Let $y=e^{-x}.U\sin$ chain rule, we have 

$$\frac{dy}{dx}=e^{-x}\cdot\frac{d}{dx}(-x)=-e^{-x}$$

(ii) Let_$y=\sin(\log x)$ . Using chain rule, we have 

$$\frac{dy}{dx}=\cos(\log x)\cdot\frac{d}{dx}(\log x)=\frac{\cos(\log x)}{x}$$

(i) Let.$y=\cos^{-1}\left(e^x\right)$ . Using chain rule, we have 

$$\frac{dy}{dx}=\frac{-1}{\sqrt{1-\left(e^{x}\right)^{2}}}\cdot\frac{d}{dx}\left(e^{x}\right)=\frac{-e^{x}}{\sqrt{1-e^{2x}}}$$

(iv) Let.$y=e^{\cos x}$ . Using chain rule, we have 

$$\frac{dy}{dx}=e^{\cos x}\cdot(-\sin x)=-(\sin x)e^{\cos x}$$

### EXERCISE 5.4

Differentiate the following w.r.t. x:

$$.ed \begin{aligned}&1.\quad\frac{e^{x}}{\sin x}\quad&2.\quad e^{\sin^{-1}x}\quad&3.\quad e^{x^{3}}\\&4.\quad\sin\left(\tan^{-1}e^{-x}\right)\quad&5.\quad\log\left(\cos e^{x}\right)\quad&6.\quad e^{x}+e^{x^{2}}+\cdots+e^{x^{5}}\\&7.\quad\sqrt{e^{\sqrt{x}}},x>0\quad&8.\quad\log\left(\log x\right)x>1\quad&9.\quad\cos x\quad&x>0\end{aligned}$$

10.$\cos\left(\log x+e^{x}\right),x>0$ 

#### 5.5. Logarithmic Differentiation 

In this section, we will learn to differentiate rain special c ofion n n the form 



$$y=f(x)=[u(x)]^{\nu(x)}$$

By taking logarithm (to base e) the above may be rewritten as 

$$\log y=v(x)\log\left[u(x)\right]$$

Using chain rule we may differentiate this to get 

$$\frac{1}{y}\cdot\frac{dy}{dx}=v(x)\cdot\frac{1}{u(x)}\cdot u'(x)+v'(x)\cdot\log\left[u(x)\right]$$

which implies that 

$$\frac{dy}{dx}=y\left[\frac{v(x)}{u(x)}\cdot u^{\prime}(x)+v^{\prime}(x)\cdot\log[u(x)]\right]$$

The main point to be noted in this method is that $f(x)$ and $u(x)$ mustalwaysbe positive as otherwise their logarithms are not defined. This process of differentiation is known as logarithms differentiation and is illustrated by the following examples:

Example 27 Differentiate $\sqrt{\frac{(x-3)(x^2+4)}{3x^2+4x+5}}$ w.r.t..

Solution Let $y=\sqrt{\frac{(x-3)(x^2+4)}{(3x^2+4x+5)}}$ 

Taking logarithm on both sides, we have 

$$\log y=\frac{1}{2}\left[\log(x-3)+\log(x^2+4)-\log(3x^2+4x+5)\right] ad $$

Now, differentiating both sides w.r.t. x, we get 

or 

$$ad \begin{aligned}\frac{1}{y}\cdot\frac{dy}{dx}&=\frac{1}{2}\left[\frac{1}{(x-3)}+\frac{2x}{x^{2}+4}-\frac{6x+4}{3x^{2}+4x+5}\right]\\\frac{dy}{dx}&=\frac{y}{2}\left[\frac{1}{(x-3)}+\frac{2x}{x^{2}+4}-\frac{6x+4}{3x^{2}+4x+5}\right]\\&=\frac{1}{2}\sqrt{\frac{(x-3)(x^{2}+4)}{3x^{2}+4x+5}}\left[\frac{1}{(x-3)}+\frac{2x}{x^{2}+4}-\frac{6x+4}{3x^{2}+4x+5}\right]\end{aligned}$$

Example 28 Differentiate $a^{x}$ w.r.t. x, where a is a positive constant.

Solution Let.$y=a^{x}$ .Then 

$$\log y=x\log a Differentiating both sides w.r.t._we have $$

Diffrentiatw.$x_{s}$ we have 

or 

Thus 

not tr Alternatively 

$$not tr \begin{aligned}\frac{1}{y}\frac{dy}{dx}&=\log a\\\frac{dy}{dx}&=y\log a\\\left\{\frac{d}{dx}(a^x)\right.&=a^x\log a\\\left\{\frac{d}{dx}(a^x)\right.&=\left.\frac{d}{dx}(e^{x\log a})\right.=e^{x\log a}\frac{d}{dx}(x\log a)\\&=e^{x\log a}\cdot\log a=a^x\log a.\end{aligned}$$

Example 29 Differentiate $x^{\sin x},x>0$ w.r.t..

Solution Let $y=x^{\sin x}$ r. Taking logarithm on both sides, we have 

Therefore 

or 

or 

$$\begin{aligned}\log y&=\sin x\log x\\\left[\frac{1}{y}\cdot\frac{dy}{dx}\right.&=\left.\sin x\frac{d}{dx}\left(\log x\right)+\log x\frac{d}{dx}\left(\sin x\right)\right]\\\left[\frac{1}{y}\frac{dy}{dx}\right.&=\left.\left(\sin x\right)\frac{1}{x}+\log x\cos x\right.\\\left.\frac{dy}{dx}\right.&=\left.y\left[\frac{\sin x}{x}+\cos x\log x\right]\right.\\&=\left.x^{\sin x}\left[\frac{\sin x}{x}+\cos x\log x\right]\right.\\&=\left.x^{\sin x-1}\cdot\sin x+x^{\sin x}\cdot\cos x\log x\right.\end{aligned} ied ]$$

Example 30 Find $\frac{dy}{dx},\mathrm{if}y^{x}+x^{y}+x^{x}=a^{b}$ ,

Solution Given that $y^{x}+x^{y}+x^{x}=a^{b}$ 

Putting $u=y^{x},y=x^{y}$ and $w=x^{x}$ we get $$ 

Therefore 

$$\frac{du}{dx}+\frac{dv}{dx}+\frac{dw}{dx}=0$$

Now,$u=y^{x}$ .Taking logarithm on both sides, we have 

$$\log u=x\log y $$

Differentiating both sides wr.t. x, we have not 

$$\begin{aligned}\frac{1}{u}\cdot\frac{du}{dx}&=x\frac{d}{dx}(\log y)+\log y\frac{d}{dx}(x)\\&=x\frac{1}{y}\cdot\frac{dy}{dx}+\log y\cdot1\end{aligned}$$

So 

$$\left[\frac{du}{dx}=u\left(\frac{x}{y}\frac{dy}{dx}+\log y\right)=y^{x}\left[\frac{x}{y}\frac{dy}{dx}+\log y\right]\right]$$

Also $y=x^{y}$ 

Taking logarithm on both sides, we have 

$$\log v=y\log x $$

Differentiating both sides w.r.t. , we have 

So 

$$\begin{aligned}\frac{1}{v}\cdot\frac{dv}{dx}&=y\cdot\frac{d}{dx}(\log x)+\log x\frac{dy}{dx}\\&=y\cdot\frac{1}{x}+\log x\cdot\frac{dy}{dx}\\\frac{dv}{dx}&=v\left[\frac{y}{x}+\log x\frac{dy}{dx}\right]\\&=x^y\left[\frac{y}{x}+\log x\frac{dy}{dx}\right]\end{aligned} `ublished $$

Again 

$$w=x^{x}$$

Taking logarithm on both sides, we have 

$$\log w=x\log x. `ublished $$

Differentiating both sides w.r.t. x, we have 

i.e.

<div style="text-align: center;"><img src="imgs/img_in_image_box_282_788_347_853.jpg" alt="Image" width="6%" /></div>


$$`ublished \begin{aligned}\frac{1}{w}\cdot\frac{dw}{dx}&=x\frac{d}{dx}(\log x)+\log x\cdot\frac{d}{dx}(x)\\&=x\cdot\frac{1}{x}+\log x\cdot1\\\frac{dw}{dx}&=w(1+\log x)\\&=x^x(1+\log x)\end{aligned}$$

From (1), (2), (3), (4), we have 

Therefore 

or 

$$Therefore \begin{aligned}y^{x}\left(\frac{x}{y}\frac{dy}{dx}+\log y\right)+x^{y}\left(\frac{y}{x}+\log x\frac{dy}{dx}\right)+x^{x}\left(1+\log x\right)=0\\\left(x\cdot y^{x-1}+x^{y}\cdot\log x\right)\frac{dy}{dx}=-x^{x}\left(1+\log x\right)-y\cdot x^{y-1}-y^{x}\log y\\\frac{dy}{dx}=\frac{-\left[y^{x}\log y+y\cdot x^{y-1}+x^{x}(1+\log x)\right]}{x\cdot y^{x-1}+x^{y}\log x}\end{aligned}$$

### EXERCISE 5.5

Differentiatethe functions given in Exercises1toll w.r.t. .

1.cos x.cos 2x .cos 3

2.

$$\sqrt{\frac{(x-1)(x-2)}{(x-3)(x-4)(x-5)}}$$

3.$(\log x)^{\cos x}$ 



$x^{x}-2^{\sin x}$ 

5.

$$(x+3)^{2}\cdot(x+4)^{3}\cdot(x+5)^{4}$$

6.

$$\left(x+\frac{1}{x}\right)^{x}+x^{\left(1+\frac{1}{x}\right)}$$

7.$(\log x)^{x}+x^{\log x}$ 8.$$ [Ta]

9.

$$x^{\sin x}+(\sin x)^{\cos x}$$

10.

$$x^{x\cos x}+\frac{x^{2}+1}{x^{2}-1}$$

11.$(x\cos x)^{x}+(x\sin x)^{\frac{1}{x}}$ 

Find $\frac{dy}{dx}$ of the functions given in Exercise 15

12.$x^{y}+y^{x}=1$ 

13.

$$y^{x}=x^{y}$$

14.$(\cos x)^{y}=(\cos y)^{x}$ 15.$$ 

16. Find the derivative of the function given by $f(x)=(1+x)(1+x^{2})(1+x^{4})(1+x^{8})$ and hence find $f(1)$ 



17. Differentiate $(x^{2}-5x+8)(x^{3}+7x+9)$ in three ways mentioned below:

(i) by using product rule 

(ii)by expanding the product to obtain a single polynomial.

(iii) by logarithmic differentiation.

Do they all give the same answer?

18.If $u,$ v and arefuctionsof x,te shw ha 

$$\left\{\frac{d}{dx}\left(u\cdot v\cdot w\right)=\frac{du}{dx}v\cdot w+u\cdot\frac{dv}{dx}\cdot w+u\cdot v\cdot\frac{dw}{dx}\right\}$$

in two ways – first by repeated application of product rule, second by logarithmic differentiation.



### 5.6 Derivatives of Functions in Parametric Forms 

Sometimes the rlation betwen two variables is neither explicit nor implicit, but some link of a third ariable wih ach of thetwo varables, eparaly, etablishes a relation between the first two variables. In such a situation, we say that the relation between 

themxl.ore precisely, a relation expressed between two variables x and y in the form $x=f(t),y=g(t)$ is said to be parametric form with t as a parameter.

In order to find derivative of function in such form, we have by chain rule.

or 

$$\begin{aligned}\frac{dy}{dt}&=\frac{dy}{dx}\cdot\frac{dx}{dt}\\\frac{dy}{dx}&=\frac{dy}{dx}\cdot\frac{dx}{dt}\\\frac{dy}{dx}&=\frac{dy}{\frac{dx}{dt}}\left(whenever\frac{dx}{dt}\neq0\right)\end{aligned} apublished $$

Thus 

$$\frac{dy}{dx}=\frac{g^{\prime}(t)}{f^{\prime}(t)}\left(\frac{dy}{dt}=g^{\prime}(t)\ and\frac{dx}{dt}=f^{\prime}(t)\right) apublished $$

$$\left[\mathrm{provided}f^{\prime}(t)\neq0\right]$$

Example 31 Find $\frac{dy}{dx}$ ,i $\mathrm{f}x=a\cos\theta,y=a\sin\theta$ apublished 

Solution Given that 

$$x=a\cos\theta,y=a\sin\theta apublished $$

Therefore 

$$\frac{dx}{d\theta}=-a\sin\theta,\quad\frac{dy}{d\theta}=a\cos\theta apublished $$

Hence 

$$\frac{dy}{dx}=\frac{\frac{dy}{d\theta}}{\frac{dx}{d\theta}}=\frac{a\cos\theta}{-a\sin\theta}=-\cot\theta $$

Example 32$\mathrm{Find}\ \frac{dy}{dx},\mathrm{if}\ x=at^{2},y=2at.$ 

Solution Given that $x=at^{2},y=2at$ 

So 

$$\frac{dx}{dt}=2at\ and\ \frac{dy}{dt}=2a $$

Therefore 

$$\frac{dy}{dx}=\frac{\frac{dy}{dt}}{\frac{dx}{dt}}=\frac{2a}{2at}=\frac{1}{t}$$

Example 33 Find $\frac{dy}{dx},if x=a(\theta+\sin\theta),y=a(1-\cos\theta).$ 

Solution We have $\frac{dx}{d\theta}=a(1+\cos\theta),\frac{dy}{d\theta}=a(\sin\theta)$ 

Therefore 

$$\frac{dy}{dx}=\frac{\frac{dy}{d\theta}}{\frac{dx}{d\theta}}=\frac{a\sin\theta}{a(1+\cos\theta)}=\tan\frac{\theta}{2}$$

Note  It may be noted here that $\frac{dy}{dx}$ is expressed in terms of parameter only variabandy.

つubli 

Example 34 Find $$ (cid:)

Solution Let $x=a\cos^{3}$ θ,.$y=a\sin^{3}$ 0.Then Then 

$$つubli x^{\frac{2}{3}}+y^{\frac{2}{3}}=\left(a\cos^{3}\theta\right)^{\frac{2}{3}}+\left(a\sin^{3}\theta\right)^{\frac{2}{3}}=a^{\frac{2}{3}}\left(\cos^{2}\theta+\left(\sin^{2}\theta\right)=a^{\frac{2}{3}}\right)$$

Hence,,$$ is  parametric equatio of $x^{\frac{2}{3}}+y^{\frac{2}{3}}=a^{\frac{2}{3}}$ 

Now 

$$\frac{dx}{d\theta}=-3a\cos^{2}\theta\sin\theta\ and\frac{dy}{d\theta}=3a\sin^{2}\theta\cos\theta $$

fore 

$$\frac{dy}{dx}=\frac{\frac{dy}{d\theta}}{\frac{dx}{d\theta}}=\frac{3a\sin^{2}\theta\cos\theta}{-3a\cos^{2}\theta\sin\theta}=-\tan\theta=-\sqrt[3]{\frac{y}{x}}$$

### EXERCISE 5.6

If x andy are connected parametrically by the equations given in Exercises to 0,without eliminating the parameter, Find $\frac{dy}{dx}$ 



$$x=\sin t,y=\cos2t\quad4\quad x=4t,y=\frac{4}{t}$$

5.

$$x=\cos\theta-\cos2\theta,y=\sin\theta-\sin2\theta $$

$$x=a\left(0-\sin0\right),y=a\left(1+\cos0\right)\quad7.\quad x=\frac{\sin^{3}t}{\sqrt{\cos2t}},y=\frac{\cos^{3}t}{\sqrt{\cos2t}}$$

8.

$$x=a\left(\cos t+\log\tan\frac{t}{2}\right)y=a\sin t\quad\text{9.}x=a\sec\theta,y=b\tan\theta $$

$$x=a(\cos\theta+\theta\sin\theta),y=a(\sin\theta-\theta\cos\theta)$$

11. If $x=\sqrt{a^{\sin^{-1}t}},y=\sqrt{a^{\cos^{-1}t}}$ $$ 

### 5.7 Second Order Derivativ 

Let $y=f(x)$ . Then 

$$\frac{dy}{dx}=f^{\prime}(x)$$

$\mathrm{If}f^{\prime}(x)$ is dif.t side becomes $\frac{d}{dx}\left(\frac{dy}{dx}\right)$ which is called the second order derivative of y w.r.t. x and is denoted by $\frac{d^{2}y}{dx^{2}}$ . The second order derivative of $f(x)$ is denoted by $f''(x)$ .It is also denoted by $\mathrm{D}^{2}y\mathrm{~or}y^{\prime\prime}\mathrm{~or}y_{2}\mathrm{~if}y=f(x)$ . We remark that higher order derivatives may be defined similarly.



Example 35 Find $\frac{d^{2}y}{dx^{2}},\quad if\quad y=x^{3}+\tan x.$ 

Solution Given that.$y=x^{3}+\tan x$ . Then 

$$\frac{dy}{dx}=3x^{2}+\sec^{2}x $$

Therefore 

$$\frac{d^{2}y}{dx^{2}}=\frac{d}{dx}\left(3x^{2}+\sec^{2}x\right)$$

$6x+2\sec x$ .sec x tan sec x tan $$ tan x 

Example 36 If.$y=\mathrm{A}\sin x+\mathrm{B}$ cos x, then prove that t $$ ,

Solution We have 

$$\frac{dy}{dx}=A\cos x-B\sin x $$

and 

$$\frac{d^{2}y}{dx^{2}}=\frac{d}{dx}\left(A\cos x-B\sin x\right)$$

Hence 

$$\frac{d^{2}y}{dx^{2}}+y=0$$

Example 37 If [Tab $y=3e^{2x}+2e^{3x}$ 2$\frac{d^{2}y}{dx^{2}}-5\frac{dy}{dx}+6y=0$ 

Solution Given that.cYaentGaYetaYo $$ .Then 

$$\frac{dy}{dx}=6e^{2x}+6e^{3x}=6\left(e^{2x}+e^{3x}\right)$$

ore 

$$\frac{d^{2}y}{dx^{2}}=12e^{2x}+18e^{3x}=6\left(2e^{2x}+3e^{3x}\right)$$

Hence 

$$\frac{d^{2}y}{dx^{2}}-5\frac{dy}{dx}+6y=6\left(2e^{2x}+3e^{3x}\right)$$

$$-30\left(e^{2x}+e^{3x}\right)+6\left(3e^{2x}+2e^{3x}\right)=0$$

Example 38 If $y=\sin^{-1}$ x, show that $(1-x^{2})\frac{d^{2}y}{dx^{2}}-x\frac{dy}{dx}=0$ 

Solution We have.$y=\sin^{-1}x$ . Then 

$$\frac{dy}{dx}=\frac{1}{\sqrt{\left(1-x^{2}\right)}}$$

or 

$$\sqrt{(1-x^{2})}\frac{dy}{dx}=1 repu.lished $$

So 

$$\frac{d}{dx}\left(\sqrt{\left(1-x^{2}\right)}\cdot\frac{dy}{dx}\right)=0 repu.lished $$

or 

$$\sqrt{\left(1-x^{2}\right)}\cdot\frac{d^{2}y}{d x^{2}}+\frac{dy}{dx}\cdot\frac{d}{dx}\left(\sqrt{\left(1-x^{2}\right)}\right)=0 repu.lished $$

or 

$$\sqrt{\left(1-x^{2}\right)}\cdot\frac{d^{2}y}{d x^{2}}-\frac{dy}{dx}\cdot\frac{2x}{2\sqrt{1-x^{2}}}=0 repu.lished $$

Hence 

$$\left(1-x^{2}\right)\frac{d^{2}y}{d x^{2}}-x\frac{dy}{dx}=0 repu.lished $$

Alternatively, Given that $y=\sin^{-1}x$ ,we have Mote9

$$repu.lished y_{1}=\frac{1}{\sqrt{1-x^{2}}},\mathrm{i.e.},\left(1-x^{2}\right)y_{1}^{2}=1$$

So 

Hence 

$$\begin{array}{l}(1-x^{2}).2y_{1}y_{2}+y_{1}^{2}(0-2x)=0\\(1-x^{2})y_{2}-x y_{1}=0\end{array}$$

### EXERCISE 5.7

Find the second order derivatives of the functions given in Exercises 1 to 10.

1.$x^{2}+3x+2$ 2.$x^{20}$ 3.x.cosx 

4.logx 5.$x^{3}\log x$ 6.$e^{x}$ sin $5x$ 

7.$e^{6x}\cos3x$ 8.$\tan^{-1}x$ 9.log (logx)

10. sin (logx)

11.$\mathrm{If}y=5\cos x-3$ sin x, prove that $\frac{d^{2}y}{dx^{2}}+y=0$ 

12.$\mathrm{If}\;y=\cos^{-1}x,\;\mathrm{Find}\;\frac{d^2y}{d x^2}\;\mathrm{in}\;\mathrm{terms}\;\mathrm{of}\;y\;\mathrm{alone}.$ 

13.$\mathrm{If}y=3\cos(\log x)+4$ sin (log x), show that $x^{2}y_{2}+xy_{1}+y=0$ 

14.

.I $y=\mathrm{A}e^{mx}+\mathrm{B}e^{nx}$ ,show that $\frac{d^{2}y}{dx^{2}}-(m+n)\frac{dy}{dx}+mny=0$ 

15.$\mathrm{If}y=500e^{7x}+600e^{-7x}$ ,show that $\frac{d^{2}y}{dx^{2}}=49y$ 

16.I1$\mathrm{f}e^{y}(x+1)=1,\text{show that}\frac{d^{2}y}{d x^{2}}=\left(\frac{dy}{dx}\right)^{2}$ 

17. If $y=(\tan^{-1}x)^2$ ,show that $(x^{2}+1)^{2}y_{2}+2x(x^{2}+1)y_{1}=2$ 

## Miscellaneous Examples 

Example39Diferentiate w.r.t.x, thefollowing function:

(i)

$$\sqrt{3x+2}+\frac{1}{\sqrt{2x^2+4}}\quad(ii)\log_7(\log x)$$

Solution 

(i)

$$\mathrm{Let}y=\sqrt{3x+2}+\frac{1}{\sqrt{2x^2+4}}=(3x+2)^{\frac{1}{2}}+(2x^2+4)^{-\frac{1}{2}}$$

Note that this function is defined at all real numbers $x>-\frac{2}{3}$ . Therefore 

$$\frac{dy}{dx}=\frac{1}{2}\left(3x+2\right)^{\frac{1}{2}-1}\cdot\frac{d}{dx}\left(3x+2\right)+\left(-\frac{1}{2}\right)\left(2x^{2}+4\right)^{\frac{1}{2}-1}\cdot\frac{d}{dx}\left(2x^{2}+4\right)^{\frac{3}{2}}\\=\frac{1}{2}\left(3x+2\right)^{-\frac{1}{2}}\cdot\left(3\right)-\left(\frac{1}{2}\right)\left(2x^{2}+4\right)^{-\frac{3}{2}}\cdot4x\\=\frac{3}{2\sqrt{3x+2}}-\frac{2x}{\left(2x^{2}+4\right)^{\frac{3}{2}}}$$

This is defined for all real numbers $x>-\frac{2}{3}$ 

(ii)

$$\mathrm{Let}y=\log_7(\log x)=\frac{\log(\log x)}{\log7}(by change of base formula).$$

The function is defined for all real numbers $x\geq1$ . Therefore 

$$\begin{aligned}\frac{dy}{dx}&=\frac{1}{\log7}\frac{d}{dx}(\log(\log x))\\&=\frac{1}{\log7}\frac{1}{\log x}\cdot\frac{d}{dx}(\log x)\\&=\frac{1}{x\log7\log x}\end{aligned}$$

Example 40 Differentiate the following w.r.t. x.

$$\mathrm{(i)}\quad\cos^{-1}\left(\sin x\right)\quad\mathrm{(ii)}\quad\tan^{-1}\left(\frac{\sin x}{1+\cos x}\right)\quad\mathrm{(iii)}\quad\sin^{-1}\left(\frac{2^{x+1}}{1+4^x}\right) hed $$

Solution 

(i)L $\mathrm{et}f(x)=\cos^{-1}(\sin x)$ .Observethattis function idefined or all eal numbers.We may rewrite this function as 



$$\begin{aligned}f(x)&=\cos^{-1}(\sin x)\\&=\cos^{-1}\left[\cos\left(\frac{\pi}{2}-x\right)\right]\\&=\frac{\pi}{2}-x\end{aligned}$$

Thus 

$$f^{\prime}(x)=-1$$

(ii)$\mathrm{Let}f(x)=\tan^{-1}\left(\frac{\sin x}{1+\cos x}\right)$ . Observe that this function is defined for all real numbers, where cos $x\ne-1;i.e.$ ,at all odd multiplies of π. We may rewrite this function as 

nd 



$$f(x)=\tan^{-1}\left(\frac{\sin x}{1+\cos x}\right)=\tan^{-1}\left[\frac{2\sin\left(\frac{x}{2}\right)\cos\left(\frac{x}{2}\right)}{2\cos^2\frac{x}{2}}\right]$$

$$\tan^{-1}\left[\tan\left(\frac{x}{2}\right)\right]=\frac{x}{2}$$

Observe that we could cancel $\cos\left(\frac{x}{2}\right)$ in both numerator and denominator as it is not equal to zero. Thus $f^{\prime}(x)=\frac{1}{2}$ 



(iii)$\mathrm{Let}f(x)=\sin^{-1}\left(\frac{2^{x+1}}{1+4^x}\right)$ .To find the domain of this function we need to find all x such that $-1\leq\frac{2^{x+1}}{1+4^{x}}\leq1$ . Since the quantity in the middle is always positive,we need to find all x such that $\frac{2^{x+1}}{1+4^x}\leq1,i.e.,all x such that2^{x+1}\leq1+4^x.$ may rewrite this as $2\leq\frac{1}{2^{x}}+2^{x}$ which is true for all x. Hence the function is defined at every real number. By putting $2^{x}=\tan\theta$ ,this function may be rewritten as 



$$\begin{aligned}f(x)&=\sin^{-1}\left[\frac{2^{x}+1}{1+4^{x}}\right]\\&=\sin^{-1}\left[\frac{2^{x}\cdot2}{1+\left(2^{x}\right)^{2}}\right]\\&=\sin^{-1}\left[\frac{2\tan\theta}{1+\tan^{2}\theta}\right]\\&=\sin^{-1}\left[\sin2\theta\right]\\&=2\theta=2\tan^{-1}\left(2^{x}\right)\\f^{\prime}(x)&=2\cdot\frac{1}{1+\left(2^{x}\right)^{2}}\cdot\frac{d}{dx}\left(2^{x}\right)\\&=\frac{2}{1+4^{x}}\cdot\left(2^{x}\right)\log2\\&=\frac{2^{x}+1\log2}{1+4^{x}}\end{aligned}$$

Example 41 Find $f^{\prime}(x)\mathrm{if}f(x)=(\sin x)^{\sin x}\mathrm{for}\mathrm{all}0<x<\pi.$ 

Solution The function $y=(\sin x)^{\sin x}$ is defined for all positive real numbers. Taking logarithms, we have 



Then 

Thus 

$$\begin{aligned}\log y&=\log\left(\sin x\right)^{\sin x}=\sin x\log\left(\sin x\right)\\\frac{1}{y}\frac{dy}{dx}&=\frac{d}{dx}\left(\sin x\log\left(\sin x\right)\right)\\&=\cos x\log\left(\sin x\right)+\sin x\cdot\frac{1}{\sin x}\cdot\frac{d}{dx}\left(\sin x\right)\\&=\cos x\log\left(\sin x\right)+\cos x\\&=\left(1+\log\left(\sin x\right)\right)\cos x\\\frac{dy}{dx}&=y\left(\left(1+\log\left(\sin x\right)\right)\cos x\right)=\left(1+\log\left(\sin x\right)\right)\left(\sin x\right)^{\sin x}\cos x\end{aligned}$$

Example 42 For a positive constant a find $\frac{dy}{dx}$ ,whe 

$$y=a^{t+\frac{1}{t}},\mathrm{and}x=\left(t+\frac{1}{t}\right)^d $$

Slu rall roel $t\neq0$ 

$$\frac{dy}{dt}=\frac{d}{dt}\left(a^{t+\frac{1}{t}}\right)=a^{t+\frac{1}{t}}\frac{d}{dt}\left(t+\frac{1}{t}\right)\cdot\log a^{t}\cdot\frac{d}{dt}\left(1-\frac{1}{t^2}\right)\log a $$

Similarly 

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

$\frac{dx}{dt}\neq0only if t\neq\pm1$ --. Thus for $t\neq\pm1$ 

$$\frac{dy}{dx}=\frac{\frac{dy}{dt}}{\frac{dx}{dt}}=\frac{a^{t+\frac{1}{t}}\left(1-\frac{1}{t^2}\right)\log a}{a\left[t+\frac{1}{t}\right]^{a-1}\cdot\left(1-\frac{1}{t^2}\right)}\\=\frac{a^{t+\frac{1}{t}}\log a}{a\left(t+\frac{1}{t}\right)^{a-1}}$$

Example 43 Differentiate $\sin^{2}$  w.r.t.$e^{\cos x}$ 

Solution Let $u\left(x\right)=\sin^{2}x$ :and $v\left(x\right)=e^{\cos x}$ . We want to find $\frac{du}{dy}=\frac{du/dx}{dy/dx}.\ Clearly$ 

Thu $\frac{du}{dx}=2\sin x\cos x\mathrm{and}\frac{dv}{dx}=e^{\cos x}\left(-\sin x\right)=-\left(\sin x\right)e^{\cos x},\quad\frac{du}{dy}=\frac{2\sin x\cos x}{\sin xe^{\cos x}}=-\frac{2\cos x}{e^{\cos x}}$ 

$$Thu \frac{du}{dx}=2\sin x\cos x\mathrm{and}\frac{dv}{dx}=e^{\cos x}\left(-\sin x\right)=-\left(\sin x\right)e^{\cos x},\quad\frac{du}{dy}=\frac{2\sin x\cos x}{\sin xe^{\cos x}}=-\frac{2\cos x}{e^{\cos x}}$$

## Miscellaneous Exercise on Chapter 5

Differentiate w.r.t. x the function in Exercises 1 to 11.

$$\left(3x^{2}-9x+5\right)^{9}\quad2\cdot\sin^{3}x+\cos^{6}x\quad4\cdot\sin^{-1}\left(x\sqrt{x}\right),0\leq x\leq1$$

5.

$$\frac{\cos^{-1}\frac{x}{2}}{\sqrt{2x+7}},-2<x<2$$

6.

$$\cot^{-1}\left[\frac{\sqrt{1+\sin x}+\sqrt{1-\sin x}}{\sqrt{1+\sin x}-\sqrt{1-\sin x}}\right],0<x<\frac{\pi}{2}$$

7.$(\log x)^{\log x},x>1$ 

8.cos $(a\cos x+b\sin x)$ , for some constant a and b.

9.

$$\left(\sin x-\cos x\right)^{\left(\sin x-\cos x\right)},\quad\frac{\pi}{4}<x<\frac{3\pi}{4}$$

10.$x^{x}+x^{a}+a^{x}+a^{a}$ , for some fixed $a>0and x>0$ 

11.$x^{x^{2}-3}+(x-3)^{x^{2}}\text{,for}x>3$ 

12.$\mathrm{Find}\ \frac{dy}{dx},\ \mathrm{if}\ y=12\ (1-\cos t),\ x=10\ (t-\sin t),\ -\frac{\pi}{2}<t<\frac{\pi}{2}$ 

13.$\mathrm{Find}\ \frac{dy}{dx},\ \mathrm{if}\ y=\sin^{-1}x+\sin^{-1}\sqrt{1-x^{2}},\ 0<x<1$ 

14. If $x\sqrt{1+y}+y\sqrt{1+x}=0$ , for ,$-1\leq x\leq1$ , prove that 

$$\frac{dy}{dx}=-\frac{1}{\left(1+x\right)^{2}}$$

15. If $(x-a)^{2}+(y-b)^{2}=c^{2}$ ,for some$c\geq0$ ,prove that 

$$\frac{\left[1+\left(\frac{dy}{dx}\right)^{2}\right]^{\frac{3}{2}}}{\frac{d^{2}y}{dx^{2}}}$$

is a constant independent of a and b.

16. If cos $y=x\cos(a+y)$ with cos $a\neq\pm1$ prove that $$ ,

17. If $x=a\left(\cos t+t\sin t\right)$ and $y=a(\sin t-t\cos t)$ [Tae], find $\frac{d^{2}y}{dx^{2}}$ c 

18.$\mathrm{If}f(x)=|x|^3$ ,show that $f^{\prime\prime}(x)$ exists for all real x and find it.

19. Using the fact that sin $(\mathrm{A}+\mathrm{B})=\sin\mathrm{A}\cos\mathrm{B}+\cos\mathrm{A}$ sin B and the differentiation,obtain the sum formula for cosines.



20. Does there exist a function which is continuous everywhere but not differentiable at exactly two points? Justify your answer.



$$\mathrm{If}y=\left|\begin{matrix}f(x)&g(x)&h(x)\\ l&m&n\\ a&b&c\end{matrix}\right|,\mathrm{prove that}\frac{dy}{dx}=\left|\begin{matrix}f'(x)&g'(x)&h'(x)\\ l&m&n\\ a&b&c\end{matrix}\right|$$

22.$\mathrm{If}y=e^{a\cos^{-1}x},-1\leq x\leq1$ , show that $\left(1-x^{2}\right)\frac{d^{2}y}{d x^{2}}-x\frac{dy}{dx}-a^{2}y=0$ 

## Summary 

■A real valued function is continuous at a point in its domain if the limit of the function at that point equals the value of the function at that point.A function is continuous if it is continuous on the whole of its domain.

■Sum, difference, product and quotient of continuous functions are continuous.i.e., iff and g are continuous functions, then 

$(f\pm g)(x)=f(x)\pm g(x)$ is continuous.

$(f.g)(x)=f(x)$ $g(x)$ is continuous.

$\left(\frac{f}{g}\right)(x)=\frac{f(x)}{g(x)}\quad(where g(x)\neq0)$ is continuous.

国Every diferentiable function is continuous, but te converse s nt rue 

■Chain rule is rule to differentiate composites ffunctions.$\mathrm{If}f=y\mathrm{o}u,t=u(x)$ a and if both $\frac{dt}{dx}\bmod\frac{dv}{dt}$ 6

$$\frac{df}{dx}=\frac{dv}{dt}\cdot\frac{dt}{dx}$$

■atives(inappropri 

$$\begin{aligned}&\frac{d}{dx}\left(\sin^{-1}x\right)=\frac{1}{\sqrt{1-x^{2}}}\quad\frac{d}{dx}\left(\cos^{-1}x\right)=-\frac{1}{\sqrt{1-x^{2}}}\\&\frac{d}{dx}\left(\tan^{-1}x\right)=\frac{1}{1+x^{2}}\\&\frac{d}{dx}\left(e^{x}\right)=e^{x}\quad\frac{d}{dx}\left(\log x\right)=\frac{1}{x}\\ \end{aligned}$$

■Logarithmic differentiation is a powerful technique to diferentiate functions orm $f(x)=[u(x)]^{\nu(x)}$ Herel $f(x)$ and $u(x)$ nee epositivefor this technique to make sense.

