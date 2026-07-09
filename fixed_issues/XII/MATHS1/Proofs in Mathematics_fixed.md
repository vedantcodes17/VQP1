

# PROOFS IN MATHEMATICS

Proofs areto Mathematicswhatcalligraphyistopoetry.Mathematical works do consist of proofs just as poems do consist of characters.VLADIMIRARNOLD :ied

#### A.1.1 Introduction

In Classes IX,Xand XI, wehave learnt about theconcepts of a statement,compound statement, negation, converse and contrapositive of a statement; axioms, conjectures,theorems and deductive reasoning.

Here, we will discuss various methods of proving mathematical propositions.

#### A.1.2 What is a Proof?

Proof of a mathematical statement consists of sequence of statements, each statement being juidw iio r naxim rpioi viul tablished by the method of deduction using only the allowed logical rules.

Thus, each proof is a chain of deductive arguments each of which has its premises and conclusions.Many times we prove a propoition directlyrom what isgiven in the proposition. But some times it is easier to prove an equivalent proposition rather than proving the proposition itself. This leads to, two ways of proving a proposition directly or indirectly and the proofs obtained are called direct proof and indirect proof and further each has three different ways of proving which is discussed below.

Direct ProofItisthe proofofapropositioninwhich wedrectly startthe proof with what is given in the proposition.

(i)Straight orward approach It is chaiof arguments which leads directly from what is given or assumed, with the help of axioms, definitions or already proved theorems, to what is to be proved using rules of logic.

Consider the following example:

Example 1 Show that if $x^{2}-5x+6=0,\;then\;x=3\;or\;x=2$

Solution $x^{2}-5x+6=0\ (given)$

$(x-3)(x-2)=0$ (replacing an expression by an equal/equivalent expression)$x-3=0or x-2=0$ (from the established theorem $ab=0\Rightarrow either a=0$ or

$b=0,\mathrm{for}a,b\in\mathbb{R}$

$x-3+3=0+3or x-2+2=0+2$ (adding equal quantities on either side of the equation does not alter the nature of the equation)

$x+0=3or x+0=2$ (using the identity property of integers under addition)

$x=3or x=2$ (using the identity property of integers under addition)

Hence,$x^{2}-5x+6=0$ implies $x=3or x=2$

Explanation Let p be the given statement $x^{2}-5x+6=0$ and q be the conclusion statement $x=3or x=2$

From the statement p, we deduced the statement $r:\left(x-3\right)\left(x-2\right)=0$ by replacing the expression $x^{2}-5x+6$ in the statement p by another expression $(x-3)$ 1$(x-2)$ which is equal to $x^{2}-5x+6$

There arise two questions:

(i) How does the expression $(x-3)(x-2)$ ssion $x^{2}-5x+6?$

(ii)) How can we replace an expression with another expression which is equal to the former?

Thefrst one is proved inarlierclasses byfactorization,i.,

$$x^{2}-5x+6=x^{2}-3x-2x+6=x(x-3)-2(x-3)=(x-3)(x-2).$$

The second one is by valid form of argumentation (rules of logic)

Next this statement r becomes premises or given and deduce the statement s 66$x-3=0or x-2=0^{\circ}$ and the reasons are given in the brackets.

This process continues till we reach the conclusion.

The symbolic equivalent of the argument is to prove by deduction that $p\Rightarrow q$ is true.

Starting with p, we deduce $p\Rightarrow r\Rightarrow s\Rightarrow\ldots\Rightarrow q$ YtannY to $p\Rightarrow q$ is true.

Example 2 Prove that the function $f\colon\mathbb{R}\to\mathbb{R}$

defined by.$f(x)=2x+5is one-one$

Solution Note that a functionf is one-one if

$$f(x_{1})=f(x_{2})\Rightarrow x_{1}=x_{2}\quad(definition of one-one function)$$

Now, given that

$$f(x_{1})=f(x_{2}),i.e.,2x_{1}+5=2x_{2}+5$$

⇒

$2x_{1}+5-5=2x_{2}+5-5$ (adding the same quantity on both sides)

$$2x_{1}+0=2x_{2}+0$$

$2x_{1}=2x_{2}$ (using additive identity of real number)

$$\left\{\frac{2}{2}x_{1}=\frac{2}{2}x_{2}(dividing by the same non zero quantity)\right.}$$

$$x_{1}=x_{2}$$

Hence, the given function is one-one.

## (i) Mathematical Induction

Mathematical induction, is a strategy of proving a proposition which is deductive in nature. The whole basis of proof of this method depends on the following axiom:

For a given subset S of N, if

(i) the natural number $1\in\mathbb{S}$ and

(ii) the natural number $k+1\in\mathbb{S}$ whenever $k\in\mathrm{S}$ ,then $\mathbf{S}=\mathbf{N}$

According to the principle of mathematical induction, if a statement ${}^{\mathrm{{}^{\mathrm{{}^{\mathrm{{}^{\mathrm{{}^{\mathrm{}{S}}}}}}}}}}\mathrm{S}(n)$ is true for $n=1$ (or for some starting point j), and $\mathrm{if}\mathbb{S}(n)$ is true for $n=k^{n}$ implies that $ ``\mathrm{S}(n)$ is true for $n=k+1$ (whatever integer $k\geq j\mathrm{may be}$ , then the statement is true for any positive integer n, for all $n\geq j$ rep

We now consider some examples.

Example 3 Show that if

$$rep \mathrm{A}=\begin{bmatrix}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{bmatrix},\text{then}\mathrm{A}^{n}=\begin{bmatrix}\cos n\theta&\sin n\theta\\ -\sin n\theta&\cos n\theta\end{bmatrix}$$

Solution We have

$$\mathrm{P}(n):\mathrm{A}^{n}=\begin{bmatrix}\cos n\ \theta&\sin n\ \theta\\-\sin\ n\ \theta&\cos n\ \theta\end{bmatrix}$$

We note that

$$\mathrm{P}(1):\mathrm{A}^{1}=\begin{bmatrix}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{bmatrix}$$

Therefore,$\mathrm{P}(1)$ is true.

Assume that $\mathrm{P}(k)$ is true, i.e.,

$$\mathrm{P}(k):\mathrm{A}^{k}=\begin{bmatrix}\cos k\ \theta&\sin k\ \theta\\-\sin k\ \theta&\cos k\ \theta\end{bmatrix}$$

We want to prove that $\mathbb{P}(k+1)$ is true whenever $\mathrm{P}(k)$ is true, i.e.,

$$\mathrm{P}(k+1):\mathrm{A}^{k+1}=\left[\begin{aligned}\cos\left(k+1\right)\theta\quad\sin\left(k+1\right)\theta\\ -\sin(k+1)\theta\quad\cos\left(k+1\right)\theta\end{aligned}\right]$$

Now

$$\mathrm{A}^{k+1}=\mathrm{A}^k\cdot\mathrm{A}$$

Since $\mathrm{P}(k)$ is true, we have

$$\begin{aligned}\mathrm{A}^{\mathrm{k}+1}=&\begin{bmatrix}\cos k\;0&\sin k\;0\\-\sin k\;0&\cos k\;0\end{bmatrix}\begin{bmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{bmatrix}\\=&\begin{bmatrix}\cos k\;0\cos\theta-\sin k\;0\sin\theta&\cos k\;0\sin\theta+\sin k\;0\cos\theta\\-\sin k\;0\cos\theta-\cos k\;0\sin\theta&-\sin k\;0\sin\theta+\cos k\;0\cos\theta\end{bmatrix}\\&(by matrix multiplication)\\=&\begin{bmatrix}\cos(\;k+1)\;0&\sin(\;k+1)\;0\\-\sin(\;k+1)\;0&\cos\;(\;k+1\;0\;\end{bmatrix}\end{aligned})$$

Thus,$\mathbb{P}(k+1)$ is true whenever $\mathbb{P}(k)$ is true.

Hence,$\mathrm{P}(n)$ is true for all $n\geq1$ (by the principle of mathematical induction.

## (iii) Proof by cases or by exhaustion

This method of proving a statement $p\Rightarrow q$ is possible only when p can be split into several cases, , s, t (say) so that $p=r\lor s\lor l$ (where"v " is the symbol for "OR").If the conditionals $\begin{array}{l}r\Rightarrow q;\\s\Rightarrow q;\end{array}$

$$\begin{array}{l}r\Rightarrow q;\\s\Rightarrow q;\end{array}$$

and

$$t\Rightarrow\bar{q}$$

are proved, then $(r\lor s\lor t)\Rightarrow\bar{q}$ , is proved and so $p\rightrightarrows q$ is proved.

The method consists of examining every possible case of the hypothesis. It is practically convenient only when the number of possible cases are few.

Example 4 Show that in any triangle ABC,

$$a=b\cos C+c\cos B $$

Solution Let p be the statement "ABC is any triangle" and bethe statement

$$a=b\cos C+c\cos B $$

Let ABC be a triangle. From A draw AD a perpendicular to BC (BC produced if necessary).

As we know that any triangle has to be either acute or obtuse or right anled, we can split p into three statements r, s and , where

r: ABC is an acute angled triangle with $\angle\mathrm{C}$ is acute.

 : ABC is an obtuse angled triangle with $\angle\mathrm{C}$ is obtuse.

t: ABC is a right angled triangle with $\angle\mathrm{C}$ is right angle.

Hence, we prove the theorem by three cases.

Case (i) When $\angle\mathrm{C}$ is acute (Fig. A1.1).

From the right angled triangle AB,

i.e.

$$\begin{aligned}\frac{BD}{AB}&=\cos B\\ BD&=AB\cos B\\&=c\cos B\end{aligned}$$

From the right angled triangle ADC,

i.e.

Now

$$\begin{aligned}\frac{\mathrm{CD}}{\mathrm{AC}}&=\cos\mathrm{C}\\mathrm{CD}&=\mathrm{AC}\cos\mathrm{C}\\&=b\cos\mathrm{C}\\a&=\mathrm{BD}+\mathrm{CD}\\&=c\cos\mathrm{B}+b\cos\mathrm{C}\end{aligned}$$

Case (ii) When $\angle\mathrm{C}$ is obtuse (Fig A1.2).

From the right angled triangle ADB,

i.e.

$$\begin{aligned}\frac{\mathrm{BD}}{\mathrm{AB}}&=\cos\mathrm{B}\\mathrm{BD}&=\mathrm{AB}\cos\mathrm{B}\\&=c\cos\mathrm{B}\end{aligned}$$

From the right angled triangle ADC,

$$\begin{aligned}\frac{\mathrm{CD}}{\mathrm{AC}}&=\cos\angle\mathrm{ACD}\\&=\cos\left(180^{\circ}-\mathrm{C}\right)\\&=-\cos\mathrm{C}\end{aligned}$$

i.e.

$$\begin{aligned}CD&=-AC\cos C\\&=-b\cos C\end{aligned}$$

<div style="text-align: center;"><img src="imgs/img_in_image_box_562_900_883_1236.jpg" alt="Image" width="34%" /></div>

<div style="text-align: center;">Fig A1.2</div>

Now

i.e.

$$\begin{aligned}&a=BC=BD-CD\\&a=c\cos B-(-b\cos C)\\&a=c\cos B+b\cos C\\ \end{aligned}$$

Case (i) When $\angle\mathrm{C}$ is a right angle (Fig A1.3).

From the right angled triangle ACB,

i.e.

$$\left\{\begin{aligned}\frac{BC}{AB}&=\cos B\\ BC&=AB\cos B\\ a&=c\cos B,\end{aligned}\right.}$$

and

$$b\cos C=b\cos90^{0}=0$$

<div style="text-align: center;"><img src="imgs/img_in_image_box_599_162_903_465.jpg" alt="Image" width="32%" /></div>

<div style="text-align: center;">Fig A1.3</div>

Thus, we may write

$$\begin{aligned}a&=0+c\cos B\\&=b\cos C+c\cos B\end{aligned}$$

e BC

$$a=b\cos C+c\cos B $$

By case (i),$r\Rightarrow q$ is proved.

By case (ii),$s\rightrightarrows q$ is proved.

By case (iii),$t\Rightarrow q$ is proved.

Hence, from the proof by cases,$(r\lor s\lor t)\Rightarrow q$ is proved, i.e.,$p\Rightarrow q$ is proved.Indirect Proof Instead of proving the given proposition directly, we establish the proof of the propositionthrough proving a proposition which is equivalent to the given proposition.

(i) Proof by contradiction (Reductio Ad Absurdum) : Here, we start with the assumption that the given statement is false. By rules of logic, we arrive at a conclusion contradicting the assumption and hence it is inferred that the assumption is wrong and hence the given statement is true.

Let us illustrate this method by an example.

Example 5 Show that the set of all prime numbers is infinite.

Solution Let P be the set of all prime numbers. We take the negation of the statement "the set of all prime numbers is infinite",i.e., we assume the set of all prime numbers to be finite. Hence, we can list all the prime numbers as $\mathrm{P}_{1},\mathrm{P}_{2},\mathrm{P}_{3},\ldots,\mathrm{P}_{k}(\mathrm{say})$ . Note that we have assumed that there is no prime number other than $\mathrm{P}_{1},\mathrm{P}_{2},\mathrm{P}_{3},\ldots,\mathrm{P}_{k}$

Now consider $\mathrm{N}=\left(\mathrm{P}_{1}\mathrm{~P}_{2}\mathrm{~P}_{3}\cdots\mathrm{P}_{k}\right)+1\ldots(1)$

N is not in the list as N is larger than any of the numbers in the list.

N is either prime or composite.

IfN is a prime,thenby 1),there exits a prime number whichis not listed.

Onthe other hand,ifNiscomposit, it should have a prime diviorut none of the numbers in the list can divide N, because they all leave the remainder1.Hence, the prime divisor shouldbeotherthantheonenthelist.

Thus, in both thecases whetherNis a prime or a composite, we ended up with contradiction to the fact that we have listed all the prime numbers.

Hence, our assumption that set of all prime numbers is finite is false.

Thus, the set of all prime numbers is infinite.

NoteObserve that the above proofalsouses the methodof proof bycases.

## (i) Proof byusing contrapositive statementof the given statement

Instead of proving the conditional $p\Rightarrow q$ , we prove its equivalent, i.e.,$\sim q\Rightarrow\sim p$ .(students can verify).

Theoolin and the hypothesis and negating both.

Example 6 Prove that the function f $\mathtt{R}\rightarrow\mathtt{R}$ $f(x)=2x+5$ is $\scriptstyle{\mathrm{o n e-o n e}}$

Solution A function is one-one if $f(x_{1})=f(x_{2})\Rightarrow x_{1}=x_{2}.$

Using this we have to show that $2x_{1}+5=2x_{2}+5\Rightarrow x_{1}=x_{2}$ 'This is of the form $p\Rightarrow q.$ , where, p is $2x_{1}+5=2x_{2}+5$ and $q:x_{1}=x_{2}$ . We have proved this in Example 2of"direct method".

We can also prove the same by using contrapositive of the statement. Now contrapositive of this statement is $\sim q\Rightarrow\sim p,$ ,i.e., contrapositive of $\mathrm{if}f(x_1)=f(x_2)$ −1,then $x_{1}=x_{2}\quad is\quad\quad\{x_{1}\neq x_{2},\quad then\quad f(x_{1})\neq f(x_{2})\}$

$$\begin{array}{l}Now\quad x_{1}\neq x_{2}\\Rightarrow\quad2x_{1}\neq2x_{2}\\Rightarrow\quad2x_{1}+5\neq2x_{2}+5\\Rightarrow\quad f(x_{1})\neq f(x_{2}).\end{array}$$

Since $q\Rightarrow\sim p$ , is equivalent to $ ``p\rightrightarrows q''$ the proof is complete.

Example 7 Show that "if a matrix A is invertible, then A is non singular".

Solution Writing the above statement in symbolic form, we have

$p\rightrightarrows q$ ,where, p is "matrix A is invertible" and q is "A is non singular"

Instead of proving the given statement, we prove its contrapositive statement, i.e.,if A is not a non singular matrix, then the matrix A is not invertible.

If Ais not a non singular matrix, thenit means the matrixAis singular, i.e,

$$|\mathrm{A}|=0$$

Then

$$\mathrm{A}^{-1}=\frac{a d j\mathrm{A}}{|\mathrm{A}|}\text{does not exist as}|\mathrm{A}|=0$$

Hence, A is not invertible.

Thus, we have proved that if Ais not a non singular matrix, then Ais not invertible.

$\mathrm{i.e.},\sim q\Rightarrow\sim p$

Hence, if a matrix A is invertible, then A is non singular.

## (ii) Proof by a counter example

In the history of Mathematics, there are occasions when all attempts to find a valid proofof a tatement fail and the uncertainty ofthetruth valueof the statment remains unresolved.

In such a situation,it is beneficialif wefind an exampleto falsify the statement.The example to disprove the statement iscalled a counter example.Sincethe disproof of a proposition $p\Rightarrow q$ is merely a proof of the $\mathrm{proposition}\sim(p\Rightarrow q)$ . Hence, this is also a method of proof.

Example 8 For each $n,2^{2^{n}}+1\ is a prime\ (n\in\mathbf{N})$ This was once thought to be true on the basis that

$$2^{2^{1}}+1=2^{2}+1=5is a prime.\\ 2^{2^{2}}+1=2^{4}+1=17is a prime.\\ 2^{2^{3}}+1=2^{8}+1=257is a prime.$$

However,at fhteeralitin okstoeorrct.ut,vntually it was

shown that

$$2^{2^{5}}+1=2^{32}+1=4294967297$$

which is not a prime since $4294967297=641\times6700417$ (a product of two numbers).

So the generalisation "For each n,$2^{2^{n}}+1$ is a prime $(n\in\mathbf{N})^{\mathrm{w}}$ is false.

Just this one example $2^{2^{s}}+1$ is sufficient to disprove the gneraliation. This is the counter example.

Thus, we have proved that the generalisation "For each $n,2^{2^{n}}+1$ is a prime $(n\in\mathbf{N})$ is not true in general.

Example 9 Every continuous function is differentiable.

Proof We consider some functions given by

(i)

$$f(x)=x^{2}$$

(ii)

$$g(x)=e^x $$

(i $h\left(x\right)=\sin x$

These functions are continuous for all values of x. If we check for their differentlllf.is make s"s"may be true.But if wecheck thedifrentiabilityofthefunction given by $\phi(x)=|x|^{\infty}$ which is continuous, we find that it is not differentiable at $x=0$ .This means that the statement"Everycontinuousunctioisdfrentiable"isalse,igeneral.Justthis one function $\phi(x)=|x|$ 'is sufficient to disprove the statement. Hence.$\phi(x)=|x|^{\infty}$ iscalled xvuble".NCERT 