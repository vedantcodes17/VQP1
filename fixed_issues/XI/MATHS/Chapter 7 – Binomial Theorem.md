

# BINOMIAL THEOREM 

…Mathematics is a most exact science and its conclusions are capable of absolute proofs. - C.P  STEINMETZ 0

### 7.1 Introduction 

In earlier classes, we have learnt how to find the squares and cubes of binomials like $a+b\bmod{a}-b$ . Using them, we could evaluate the numerical values of numbers like $(98)^{2}=(100-2)^{2},(999)^{3}=(1000-1)^{3}$ However, for higher powers ike8),101)  te calculations become difficult by using repated multiplication. This difculty was overcomebytoemkowabiomialtormtives an easier way to expand $(a+b)^{n}$ where n is an integer or a rational number. In this Chapter, we study binomial theorem for positive integral indices only.



### 7.2 Binomial Theorem for Positive Integral Indices 

Let us have a look at the following identities done earlier:

<div style="text-align: center;"><img src="imgs/img_in_image_box_637_480_864_796.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;">Blaise Pascal (1623-1662)</div>


$$Let us have a look at the following identities done earlier:\begin{array}{l}(a+b)^{0}=1\quad a+b\neq0\\(a+b)^{1}=a+b\quad a+b\neq0\\(a+b)^{2}=a^{2}+2a b+b^{2}\\(a+b)^{3}=a^{3}+3a^{2}b+3a b^{2}+b^{3}\\(a+b)^{4}=(a+b)^{3}(a+b)=a^{4}+4a^{3}b+6a^{2}b^{2}+4a b^{3}+b^{4}\end{array}$$

In these expansions, we observe that 

(i) The total number of terms in the expansion is one more than the index. For example, in the expansion of $(a+b)^{2}$ ,number of terms is 3 whereas the index of $(a+b)^{2}$ is 2.



($^{\ast}a^{\ast}$ n EMY second quantity $$ increase by 1, in the successive term 司(

is equal to the index of $a+b$ 



We now arrange the coefficients in these expansions as follows (Fig 7.1):

<div style="text-align: center;"><img src="imgs/img_in_image_box_278_171_668_448.jpg" alt="Image" width="41%" /></div>


Do we observe any pattern in this table that will help us to write the next row? Yes we do.Itcoix forindex2.Teo,ew theow r u 

Wecanexndvi72bing more rows.

<div style="text-align: center;">Fig 7.2</div>


## Pascal's Triangle 

The structure given in Fig 7.2  looks like a triangle with 1 at the top vertex and running down the two slanting sides. This array of numbers is known as Pascal's triangle,after the name of French mathematician Blaise Pascal. It is also known as Meru Prastara by Pingla.



Expansions for the higher powers of a binomial are also possible by using Pascal's triangle. Let us expand $(2x+3y)^{5}$ by using Pascal's triangle. The row for index 5 is 

$1\quad5\quad10\quad10\quad5\quad1$ 



Using this row and our observations (i), (ii) and (iii), we get 

$$\begin{array}{rl}{\widetilde{(2x+3y)^{s}}}&{=(2x)^{s}+5(2x)^{4}(3y)+10(2x)^{3}(3y)^{2}+10(2x)^{2}(3y)^{3}+5(2x)(3y)^{4}+(3y)^{5}}\\ &{=32x^{s}+240x^{4}y+720x^{3}y^{2}+1080x^{2}y^{3}+810x y^{4}+243y^{5}.}\end{array}$$

Now, if we want to find the expansion of $(2x+3y)^{12}$ , we are first required to get the row for index 12. This can be done by writing all the rows of the Pascal's triangle till index 2.This is a slightly lengthy procs.The process, as you oberve, will become more dificultifweed thexpansionsivolving stll larer powers.

We thus try to find a rule that will help us to find the expansion of the binomial for any power without writing all the rows of the Pascal's triangle, that come before the row of the desired index.



For this, we make use of the concept of combinations studied earlier to rewrite 

the numbers in the Pascal's triangle. We know that $^{n}\mathrm{C}_{r}=\frac{n!}{r!(n-r)!},0\leq r\leq n$ 

n is a non-negative integer. Also,$^{n}\mathrm{C}_{0}=1=^{n}\mathrm{C}_{n}$ =1

HoWoW1itCnUS(



<div style="text-align: center;"><img src="imgs/img_in_image_box_149_516_840_944.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">Fig7.3Pascal's triangle </div>


Observing this pattern, we can now write the row of the Pascal's triangle for any index without writing the earlier rows. For example, for the index 7 the row would be 

$$^7\mathrm{C}_{0}\;^{7}\mathrm{C}_{1}\;^{7}\mathrm{C}_{2}\;^{7}\mathrm{C}_{3}\;^{7}\mathrm{C}_{4}\;^{7}\mathrm{C}_{5}\;^{7}\mathrm{C}_{6}\;^{7}\mathrm{C}_{7}$$

Thus, using this row andthe observations (), (ii) and (iii), we have 

$$(a+b)^{7}=7C_{0}a^{7}+7C_{1}a^{6}b+7C_{2}a^{5}b^{2}+7C_{3}a^{4}b^{3}+7C_{4}a^{3}b^{4}+7C_{5}a^{2}b^{5}+7C_{6}ab^{6}+7C_{7}b^{7}$$

An expansion of a binomial to any positive integral index say n can now be visualised using these observations. We are now in a position to write the expansion of a binomial to any positive integral index.



#### 7.2.1 Binomial theoremfor any positive integer n,

$$(a+b)^{n}={}^{n}C_{0}a^{n}+{}^{n}C_{1}a^{n-1}b+{}^{n}C_{2}a^{n-2}b^{2}+\ldots+{}^{n}C_{n-1}a.b^{n-1}+{}^{n}C_{n}b^{n}$$

Proof The proof is obtained by aplying principle of mathematical induction.

Let the given statement be 

$$\mathrm{P}(n):(a+b)^{n}=\mathrm{^{n}C_{0}}a^{n}+\mathrm{^{n}C_{1}}a^{n-1}b+\mathrm{^{n}C_{2}}a^{n-2}b^{2}+\ldots+\mathrm{^{n}C_{n-1}}a.b^{n-1}+\mathrm{^{n}C_{n}}b^{n}$$

For $n=1$ , we have 

$$\mathrm{P}\left(1\right):\left(a+b\right)^{1}={}^{1}\mathrm{C}_{0}a^{1}+{}^{1}\mathrm{C}_{1}b^{1}=a+b $$

Thus, P (1) is true.

Suppose $\mathrm{P}\left(k\right)$ is true or omeitiveiteer $k,$ i.e.Vished 

(1)

$$(a+b)^{k}={}^{k}C_{0}a^{k}+{}^{k}C_{1}a^{k-1}b+{}^{k}C_{2}a^{k-2}b^{2}+\ldots+{}^{k}C_{k}b^{k} lished $$

We shall prove tato $\mathbb{P}(k+1)$ is also true, i.e.,

$$
P(k+1):\;
(a+b)^{k+1}
= {}^{k+1}C_{0}a^{k+1}
+
{}^{k+1}C_{1}a^{k}b
+
{}^{k+1}C_{2}a^{k-1}b^{2}
+\cdots+
{}^{k+1}C_{k}ab^{k}
+
{}^{k+1}C_{k+1}b^{k+1}
$$

Nov Expanding $(a+b)^{k+1}$ using the induction hypothesis $P(k)$:

$$
\begin{aligned}
(a+b)^{k+1}
&=(a+b)(a+b)^k\\
&=(a+b)\left(
{}^{k}C_{0}a^{k}
+{}^{k}C_{1}a^{k-1}b
+{}^{k}C_{2}a^{k-2}b^{2}
+\cdots
+{}^{k}C_{k}b^{k}
\right)
\end{aligned}
$$

Distributing $a$ and $b$ separately over the sum:

$$
\begin{aligned}
&={}^{k}C_{0}a^{k+1}
+{}^{k}C_{1}a^{k}b
+{}^{k}C_{2}a^{k-1}b^{2}
+\cdots
+{}^{k}C_{k-1}a^{2}b^{k-1}
+{}^{k}C_{k}ab^{k}\\
&\quad
+{}^{k}C_{0}a^{k}b
+{}^{k}C_{1}a^{k-1}b^{2}
+{}^{k}C_{2}a^{k-2}b^{3}
+\cdots
+{}^{k}C_{k-1}ab^{k}
+{}^{k}C_{k}b^{k+1}
\end{aligned}
$$

Regrouping like terms:

$$
\begin{aligned}
&={}^{k}C_{0}a^{k+1}
+\left({}^{k}C_{1}+{}^{k}C_{0}\right)a^{k}b
+\left({}^{k}C_{2}+{}^{k}C_{1}\right)a^{k-1}b^{2}
+\cdots\\
&\quad
+\left({}^{k}C_{k}+{}^{k}C_{k-1}\right)ab^{k}
+{}^{k}C_{k}b^{k+1}
\end{aligned}
$$

Applying Pascal's identity, ${}^{k}C_{r}+{}^{k}C_{r-1}={}^{k+1}C_{r}$, to each grouped pair:

$$
\begin{aligned}
&={}^{k+1}C_{0}a^{k+1}
+{}^{k+1}C_{1}a^{k}b
+{}^{k+1}C_{2}a^{k-1}b^{2}
+\cdots
+{}^{k+1}C_{k}ab^{k}
+{}^{k+1}C_{k+1}b^{k+1}.
\end{aligned}
$$ 

Thus, it has been proved that P $(k+1)$ is true whenever $\mathbb{P}(k)$ is true. Therefore, by principle of mathematical induction,$\mathrm{P}(n)$ is true for evry poitive integer .

We illustrate this theorem by expanding $(x+2)^{6}$ 

$$Thus \begin{align*}(x+2)^{6}&={}^{6}C_{0}x^{6}+{}^{6}C_{1}x^{5}.2+{}^{6}C_{2}x^{4}2^{2}+{}^{6}C_{3}x^{3}.2^{3}+{}^{6}C_{4}x^{2}.2^{4}+{}^{6}C_{5}x.2^{5}+{}^{6}C_{6}.2^{6}.\\&=x^{6}+12x^{5}+60x^{4}+160x^{3}+240x^{2}+192x+64\\(x+2)^{6}&=x^{6}+12x^{5}+60x^{4}+160x^{3}+240x^{2}+192x+64\end{align*}$$

## Observations 

1. The notation $\sum_{k=0}^{n}{}^{n}\mathrm{C}_{k}a^{n-k}b^{k}$ stands for 

$${}^{n}\mathrm{C}_{0}a^{n}b^{0}+{}^{n}\mathrm{C}_{1}a^{n-1}b^{1}+\ldots+{}^{n}\mathrm{C}_{r}a^{n-r}b^{r}+\ldots+{}^{n}\mathrm{C}_{n}a^{n-n}b^{n},\mathrm{where}b^{0}=1=a^{n-r}.$$

Hence the theorem can also be stated as 

$$(a+b)^n=\sum_{k=0}^{n}{}^{n}C_k a^{n-k}b^k $$

2.The coefficients ${}^{n}\mathrm{C}_{n}$ occuring in the binomial theorem are knownas binomial coefficients.



3.There are $(n+1)$ terms in the expansion of $(a+b)^n$ ', i.e., one more than the index.In the successive terms of the expansion the index of a goes on decreasing by unity. It is n in the first term,$(n{-}1)$ in the second term, and so on ending with zero in the last term. At the same time the index of increases by unity, starting with zero in thefirst term,1 in the second and so on ending with n inthe last term.

5.In the expansion of $(a+b)^{n}$ , the sum of the indices of a and  is $n+0=n$ in the first term,$(n-1)+1=n$ in the second term and so on $0+n=n$ in the last term.Tusitd $\bar{b}$ is n in every term of the expansion.



7.2.2Some special cases In the expansion $(a+b)^{\prime}$ 

(i)Taking $a=x\bmod b=-y,$ .,we obtain 

$$\begin{aligned}(x-y)^{n}&=[x+(-y)]^{n}\\&={}^{n}C_{0}x^{n}+{}^{n}C_{1}x^{n-1}(-y)+{}^{n}C_{2}x^{n-2}(-y)^{2}+{}^{n}C_{3}x^{n-3}(-y)^{3}+\cdots+{}^{n}C_{n}(-y)^{n}\\&={}^{n}C_{0}x^{n}-{}^{n}C_{1}x^{n-1}y^{n}+{}^{n}C_{2}x^{n-2}y^{2}-{}^{n}C_{3}x^{n-3}y^{3}+\cdots+(-1)^{n}C_{n}y^{n}\end{aligned}$$

$$(x-y)^{n}={}^{n}C_{0}x^{n}-{}^{n}C_{1}x^{n-1}y+{}^{n}C_{2}x^{n-2}y^{2}+\ldots+(-1)^{n}C_{n}y^{n}$$

$$\begin{align*}(x-2y)^{5}&=^{5}\mathrm{C}_{0}x^{5}-^{5}\mathrm{C}_{1}x^{4}(2y)+^{5}\mathrm{C}_{2}x^{3}(2y)^{2}-^{5}\mathrm{C}_{3}x^{2}(2y)^{3}+\\&\quad^{5}\mathrm{C}_{4}x(2y)^{4}-^{5}\mathrm{C}_{5}(2y)^{5}\\&=x^{5}-10x^{4}y+40x^{3}y^{2}-80x^{2}y^{3}+80xy^{4}-32y^{5}.\end{align*}$$

(ii)$a=1,b=x$ , we obtain 

Thus 

$$\begin{aligned}&(1+x)^{n}={}^{n}C_{0}(1)^{n}+{}^{n}C_{1}(1)^{n-1}x+{}^{n}C_{2}(1)^{n-2}x^{2}+\ldots+{}^{n}C_{n}x^{n}\\ &\quad={}^{n}C_{0}+{}^{n}C_{1}x+{}^{n}C_{2}x^{2}+{}^{n}C_{3}x^{3}+\ldots+{}^{n}C_{n}x^{n}\\ &(1+x)^{n}={}^{n}C_{0}+{}^{n}C_{1}x+{}^{n}C_{2}x^{2}+{}^{n}C_{3}x^{3}+\ldots+{}^{n}C_{n}x^{n}\\ \end{aligned}$$

In particular, for $x=1$ ,we have 

$$2^{n}=^{n}C_{0}+^{n}C_{1}+^{n}C_{2}+\ldots+^{n}C_{n}.$$

(i)Taking $a=1,b=-x,$ we obtain 

$$(1-x)^{n}={}^{n}C_{0}-{}^{n}C_{1}x+{}^{n}C_{2}x^{2}-\ldots+(-1)^{n}C_{n}x^{n}$$

In particular, for $x=1$ , we get 

$$0={}^{n}\mathrm{C}_{0}-{}^{n}\mathrm{C}_{1}+{}^{n}\mathrm{C}_{2}-\ldots+(-1){}^{n}{}^{n}\mathrm{C}_{n}$$

Example 1 Expand $\left(x^{2}+\frac{3}{x}\right)^{4},x\neq0$ 

Solution By using binomial theorem, we have 

$$`ed \begin{aligned}x^{2}+\frac{3}{x}^{4}&=4C_{0}(x^{2})^{4}+4C_{1}(x^{2})^{3}\left(\frac{3}{x}\right)+4C_{2}(x^{2})^{4}\left(\frac{3}{x}\right)^{2}+4C_{3}(x^{2})\left(\frac{3}{x}\right)^{3}+4C_{4}\left(\frac{3}{x}\right)^{4}\\&=x^{8}+4x^{6}\cdot\frac{3}{x}+6x^{4}\cdot\frac{9}{x^{2}}+4x^{2}\cdot\frac{27}{x^{3}}+\frac{81}{x^{4}}\\&=x^{8}+12x^{5}+54x^{2}+\frac{108}{x}\cdot\frac{81}{x^{4}}.\end{aligned}$$

## Example 2 Compute (98)

Solution We express $98\mathrm{as}$ the sum or difference of two numbers whose powers are easier to calculate, and then use Binomial Theorem.



Write $98=100-2$ 

$$Therefon \begin{aligned}\mathrm{e},(98)^{5}&=(100-2)^{5}\\&={^{5}\mathrm{C}}_{0}(100)^{5}-{^{5}\mathrm{C}}_{1}(100)^{4}.2+{^{5}\mathrm{C}}_{2}(100)^{3}2^{2}\\&={^{5}\mathrm{C}}_{3}(100)^{2}(2)^{3}+{^{5}\mathrm{C}}_{4}(100)(2)^{4}-{^{5}\mathrm{C}}_{5}(2)^{5}\\&=10000000000-5\times10000000\times2+10\times1000000\times4-10\times100000\\&\times8+5\times100\times16-32\\&=10040008000-1000800032=9039207968\end{aligned}$$

Example 3 Which is larger (1.01)00000or 10,000?

Solution Splitting 1.01 and using binomial theorem to write the first few terms we have 



$$\begin{aligned}(1.01)^{1000000}&=(1+0.01)^{100000}\\&=1^{1000000}C_{0}+1^{100000}C_{1}(0.01)+other positive terms\\&=1+1000000\times0.01+other positive terms\\&=1+10000+other positive terms\\&=1+100000+100000+100000+100000+100000+100000+100000+100000+100000+100000+100000+100000+100000+100000+100000+100000+100000+100000+100000+100000+100000+100000+100000+100000+10000+100000+10000+10000+10000+10000+10000+10000+10000+10000+1000+10000+1000+1000+1000+1000+1000+100+1000+100+100+1000+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100+100++1000+100+100+100++1000+100++1000+100++1000+100++10000++1000++1000+100++1000++1000++1000++10000++1000++1000++1000++1000++1000++1000++1000++1000++1000++1000++1000+++10000++100++1000++1000+++10000+++10000+++1000++1000+++1000++100++000++1000+++1000+++1000+++100++100++00++100++0+10+00++0+10+0+0+0+0+10+0++00+0+0+10+0++00+0++0+10+0+0+0++0+0+0+0+1+0+0+0+0+0++0+0+0+0+00++0+0++0+00++0+0+0+0+0++0++0+0+0+0+0+0++0+0++0++00++0+0++0+0+0++0+0++0+0++0++00++0++0++00+++0+0++0++0+0+0++0++00+++0+0++0++0++00+++0++0+0+++0+0+0+++++0+0++0+0++0+++0+0+++0++0+0+++0+0++++00++++0++00++++++0++0++0+++00++++0++0++0++++0++0+0+++++0+0++0++0+++0+++0++0+++0++++0+0+++++++0++0+0++++0+++0+0+++++0++++0++0++++0+++0+++0++++0++0+++0++++0++0++++0+++++0+++++0+++0+++++0+++0+++++++0+0+++++0++0+++++++++0+++++0+++++++00++++++++0+++0++++0++++++0+++++++0++++0++0+++++++++0++++++++0+0+0++++++0++0++++++0+++0+0+++++++++0++++0++++++00+++0++0+++++00+0++0+++++++000+0+++++00++++000++++0++00+0++00+++++000\end{aligned}$$

Hence $(1.01)^{100000}>10000$ 

Example 4 Using binomial theorem, prove that $6^{n}-5n$ always leaves remainder 1 when divided by 25.



Solution For two numbers a and b if we can find numbers $q_{\circ}$ and r such that $a=b q+r,$ ,then we say that b divides a with  as quotient and r as remainder. Thus, in order to show that $6^{n}-5n$ leaves remainder 1 when divided by 25, we prove that $6^{n}-5n=25k+1$ , where k is some natural number.



We have 

$$(1+a)^{n}={}^{n}C_{0}+{}^{n}C_{1}a+{}^{n}C_{2}a^{2}+\cdots+{}^{n}C_{n}a^{n}$$

For $a=5$ , we get 

i.e.

i.e.

or 

or 

$$\begin{aligned}&(1+5)^{n}={}^{n}C_{0}+{}^{n}C_{1}5+{}^{n}C_{2}5^{2}+\ldots+{}^{n}C_{n}5^{n}\\ &(6)^{n}=1+5n+5^{2}\cdot{}^{n}C_{2}+5^{3}\cdot{}^{n}C_{3}+\ldots+5^{n}\\ &6^{n}-5n=1+5^{2}\left({}^{n}C_{2}+{}^{n}C_{3}5+\ldots+5^{n-2}\right)\\ &6^{n}-5n=1+25\left({}^{n}C_{2}+5\cdot{}^{n}C_{3}+\ldots+5^{n-2}\right)\\ &6^{n}-5n=25k+1\quad where k={}^{n}C_{2}+5\cdot{}^{n}C_{3}+\ldots+5^{n-2}\\ \end{aligned}$$

This shows that when divided by 25,$6^{n}-5n$ leaves remainder 1.

EXERCISE 7.1

Expand each of the expressions in Exercises 1 to 5.

1$(1{-}2x)^{s}$ 

2.$\left(\frac{2}{x}-\frac{x}{2}\right)^{5}$ 

3.$(2x-3)^{6}$ 

$\left(\frac{x}{3}+\frac{1}{x}\right)^{5}$ 5.$\left(x+\frac{1}{x}\right)^6$ 

Using binomial theorem, evaluate each of the following:

6.(96)37.(102)58.(101)4

9.(99)5

Y_Binomial Theorem, indicate which number is larger $(1.1)^{10000}or1000$ 

11.Find $(a+b)^{4}-(a-b)^{4}$ . Hence, evaluate $\left[\left(\sqrt{3}+\sqrt{2}\right)^{4}-\left(\sqrt{3}-\sqrt{2}\right)^{4}\right]$ 

12.Find $(x+1)^{6}+(x-1)^{6}$ . Hence or otherwise evaluate $(\sqrt{2}+1)^{6}+(\sqrt{2}-1)^{6}$ 

13.Show that $9^{n+1}-8n-9$ is divisible by 64, whenever n is a positive integer.

14. Prove that $\sum_{r=0}^{n}3^{r}\ ^{n}C_{r}=4^{n}$ 

## Miscellaneous Exercise on Chapter 7

1.If a and b are distinct integers, prove that $a-b\mathrm{i}s$ a factor of $a^{n}-b^{n}$ ,whenever n is a positive integer.



[Hint write $a^{n}=(a-b+b)$ 



2. Evaluate $$ [_]$$ 

3. Find the value of $\left(a^{2}+\sqrt{a^{2}-1}\right)^{4}+\left(a^{2}-\sqrt{a^{2}-1}\right)^{4}$ 

4.Find an approximation of (0.99)5 using the first three terms of its expansion.

5.Expand using Binomial Theorem $\left(1+\frac{x}{2}-\frac{2}{x}\right)^{4},x\neq0$ 

6.Find the expansion of $(3x^{2}-2a x+3a^{2})^{3}$ using binomial theorem.

## Summary 

The expansionofabinomialforany positiveintegralisgivenby Binomial Theorem, which is $(a+b)^{n}={}^{n}C_{0}a^{n}+{}^{n}C_{1}a^{n-1}b+{}^{n}C_{2}a^{n-2}b^{2}+\cdots+$ $^{n}C_{n-1}a.b^{n-1}+^{n}C_{n}b^{n}$ Y 

Thecoefficientsoftheexpansionsarearrangedinanarray.Thisarrayis called Pascal's triangle.



## Historical Note 

The ancient Indian mathematicians knew about the coefficients in the expansions of $(x+y)^n,0\leq n\leq7$ The arrangement of these coefficients was in the form of a diagram called Meru-Prastara, provided by Pingla in his book Chhanda shastra (200B.C.. This triangular arrangement is also found in the work of Chinese mathematician Chu-shi-kie in 1303. The term binomial coefficients was first intodudbytheGrman maematician,Michal tipl4-7)in approximatly14.omblli 7) also ave thecoefcints in the expanion of $(a+b)^{n}$ $n=1,2\ldots,7$ and Oughtred (1631) gave them for $n=1,2,\ldots,10$ The arithmetic triangle, popularly known as Pascal's triangle and similar to the MeruPrastaraofPinglawasconstructedby the1Frenc laisePascal (1623-1662) in 1665.



The present form of the binomial theorem for integral y appeared in 1665.Trate du triange arithmetic, written by not tobe repub NCERY Pascaland ously 