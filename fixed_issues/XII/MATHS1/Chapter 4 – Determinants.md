

# DETERMINANTS 

出All Mathematical truths are relative and conditional. — C.P. STEINMETZ :

### 4.1 Introduction 

In the previous chapter, we have studied about matrices and algebra of matrices. We have also learnt that a system of algebraic equations can be expressed in the form of matrices. This means, a system of linear equations like 

$$\begin{array}{l}a_{1}x+b_{1}y=c_{1}\\a_{2}x+b_{2}y=c_{2}\end{array}$$

can be represented as $\begin{bmatrix}a_{1}&b_{1}\\ a_{2}&b_{2}\end{bmatrix}\begin{bmatrix}x\\ y\end{bmatrix}=\begin{bmatrix}c_{1}\\ c_{2}\end{bmatrix}$ . Now, this 

system of equations has a unique solution or not, is determined by the number $a_{1}b_{2}-a_{2}b_{1}$ (Recall that if $\frac{a_{1}}{a_{2}}\neq\frac{b_{1}}{b_{2}}\quad or,\quad a_{1}b_{2}-a_{2}b_{1}\neq0.$ , then the system of linear equations has a unique solution). The number $a_{1}b_{2}-a_{2}b_{1}$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_637_442_877_776.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">P.S. Laplace (1749-1827)</div>


which determines uniqueness of solution is associated with the matrix $\mathrm{A}=\begin{bmatrix}a_{1}&b_{1}\\ a_{2}&b_{2}\end{bmatrix}$ 

and is called the determinant of A or det A. Determinants have wide applications in Engineering, Science, Economics, Social Science, etc.



In this chapter, we shall study determinants up to order three only with real entries.Also, we will study various properties of determinants, minors, cofactors and applications of determinants in finding the area of a triangle, adjoint and inverse of a square matri,consistency and inconsistency of system of linear equations and solution of linear equations in two or three variables using inverse of a matrix.

### 4.2 Determinant 

To every square matrix $A=[a_{ij}]$ of order n, we can associate a number (real or complex) called determinant of the square matrix A, where $a_{ij}=(i,j)^{\mathrm{th}}$ element of A. This may be thoughtof as a function which associates each square matrix with a unique number (real or complex). If M is the set of square matrices, K is the set of numbers (real or complex) and $f\colon\mathbb{M}\to\mathbb{K}$ is defined by $f(\mathrm{A})=k$ , where $\mathrm{A}\in\mathrm{M}$ and $k\in\mathrm{K},\mathrm{then}f(\mathrm{A})$ scllt $\left|\mathrm{A}\right|$ or det A or ∆.

$$\mathrm{If}\;\mathrm{A}=\begin{bmatrix}a&b\\ c&d\end{bmatrix},\;\mathrm{then}\;\mathrm{determinant}\;\mathrm{of}\;\mathrm{A}\;\mathrm{is}\;\mathrm{written}\;\mathrm{as}\;|\mathrm{A}|=\begin{vmatrix}a&b\\ c&d\end{vmatrix}=\mathrm{det}\;(\mathrm{A}).$$

## Remarks 

(i)For matrix A,$|\mathrm{A}|$ is read as detmtofAandot modulus ofA.

(i) Only square matrices have determinants.

#### 4.2.1 Determinant of a matrix of order one 

Let 4.2.$A=[a]$ ee1erminant of a matrixof order two vbi stie ual to a 

Let 

$$\mathrm{A}=\begin{bmatrix}a_{11}&a_{12}\\ a_{21}&a_{22}\end{bmatrix}be a matrix of order2\times2, ublish $$

then the i ded as:

$$\det\left(\mathrm{A}\right)=\left|\mathrm{A}\right|=\Delta=\left|\frac{a_{11}}{a_{21}}-a_{12}\right|=a_{11}a_{22}-a_{21}a_{12} ublish $$

Example 1 Evaluate $\left|\begin{matrix}2&4\\ -1&2\end{matrix}\right|$ 

Solution We have $\left|\begin{matrix}2&4\\ -1&2\end{matrix}\right|=2(2)-4(-1)=4+4=8.$ 

Example 2 Evaluate $\left|\begin{matrix}x&x+1\\ x-1&x\end{matrix}\right|$ 

Solution We have 

$$\left|\begin{array}{c}x\\ x-1\end{array}\right|=x(x)-(x+1)(x-1)=x^2-(x^2-1)=x^2-x^2+1=1$$

#### a 4.2.3Determinant of a matrix of order $3\times3$ 

Dtermifxrf second order determinants. This is known as expansion of a determinant along a row (or a column). There are six ways of expanding a determinant of order  3correspottreerows $\left(\mathbb{R}_{1},\mathbb{R}_{2}\right.)$ and $\mathbb{R}_{3}$ and three columns $(C_1,C_2)$ and $ C_{3}$ giving the same value as shown below.



Consider the determinant of square matrix $A=\left[a_{ij}\right]_3$ ×3

i.e.,

$$|\mathrm{A}|=\left|\begin{aligned}{}&{{}\boldsymbol{a}_{\mathbf{11}}}&{\boldsymbol{a}_{\mathbf{12}}}&{}&{\boldsymbol{a}_{\mathbf{13}}}\\ {}&{{}\boldsymbol{a}_{21}}&{\boldsymbol{a}_{22}}&{}&{\boldsymbol{a}_{23}}\\ {}&{{}\boldsymbol{a}_{31}}&{\boldsymbol{a}_{32}}&{}&{\boldsymbol{a}_{33}}\end{aligned}\right|.$$

## Expansion along first Row (R)

Step 1 Multiply first element $a_{11}$ of $\mathbb{R}_{1}\;\mathrm{by}\;(-1)^{(1\;+\;1)}\;[(-1)^{\mathrm{s u m\;o f\;s u f f i x e s\;i n\;}a_{11}}]$ and with the second order determinant obtained by deleting the elements of first row $(\mathrm{R}_{\mathrm{f}})$ and first column $(\mathrm{C}_{1})\;\mathrm{of}\;|\;\mathrm{A}\;|\;\mathrm{as}\;a_{11}$ lies in $\mathbb{R}_{1}$ and $\mathrm{C}_{\mathrm{r}}$ ,

i.e.,

$$(-1)^{1+1}a_{11}\left|\begin{matrix}{a_{22}}&{a_{23}}\\ {a_{32}}&{a_{33}}\end{matrix}\right|$$

Step 2 Multiply 2nd element $a_{12}$ of $\mathbb{R}_{t}$ by $(-1)^{1+2}\left[(-1)^{\mathrm{sum}\mathrm{off}\mathrm{ixes}\mathrm{in}a_{12}}\right]$ and the second order determinant obtained by deleting elements of first row $\textcircled{R}$ and 2nd column $\left(C_{2}\right)$ of $|\mathrm{A}|\mathrm{as}a_{12}$ lies in $\mathbb{R}_{\mathrm{r}}$ and $\mathrm{C}_{23}$ 



i.e.,

$$(-1)^{1+2}a_{12}\left|\begin{matrix}a_{21}&a_{23}\\ a_{31}&a_{33}\end{matrix}\right|$$

Step 3 Multiply third element $a_{13}$ of $$ ]$$ and the second order determiant btaedby ltinglemets offirst row $\left(\mathbb{R}_{1}\right)$ and third column $(\mathrm{C}_{3})$ of $|\mathrm{A}|\mathrm{as}a_{13}$ lies in $\mathbb{R}_{i}^{1}$ and $\mathrm{C}_{v}$ 



i.e.,

$$(-1)^{1+3}a_{13}\left|\begin{matrix}a_{21}&a_{22}\\ a_{31}&a_{32}\end{matrix}\right|$$

Step 4 Now the expansion of determinant of A, that is,$\lfloor\mathrm{A}\rfloor$ written as sum of all three terms obtained in steps 1, 2 and 3 above is given by 

or 

$$\det A=\left|A\right|=\left(-1\right)^{1+1}a_{11}\left|\begin{matrix}a_{22}&a_{23}\\ a_{32}&a_{33}\end{matrix}\right|+\left(-1\right)^{1+2}a_{12}\left|\begin{matrix}a_{21}&a_{23}\\ a_{31}&a_{33}\end{matrix}\right|\\ +\left(-1\right)^{1+3}a_{13}\left|\begin{matrix}a_{21}&a_{22}\\ a_{31}&a_{32}\end{matrix}\right|\\ \left|A\right|=a_{11}\left(a_{22}a_{33}-a_{32}a_{23}\right)-a_{12}\left(a_{21}a_{33}-a_{31}a_{23}\right)\\ +a_{13}\left(a_{21}a_{32}-a_{31}a_{22}\right)$$

$$\begin{aligned}=a_{11}a_{22}a_{33}-a_{11}a_{32}a_{23}-a_{12}a_{21}a_{33}+a_{12}a_{31}a_{23}+a_{13}a_{21}a_{32}\\-a_{13}a_{31}a_{22}\quad\ldots\end{aligned}$$

NoteWeshall applyall fourstpstogether.

Expansion along second row $(\mathbb{R}_{2})$ 

$$|\mathbf{A}|=\left|\begin{aligned}{}&{{}\mathbf{a}_{11}}&{\mathbf{a}_{12}}&{}&{\mathbf{a}_{13}}\\ {}&{{}\mathbf{a}_{2I}}&{\mathbf{a}_{22}}&{}&{\mathbf{a}_{23}}\\ {}&{{}\mathbf{a}_{31}}&{\mathbf{a}_{32}}&{}&{\mathbf{a}_{33}}\end{aligned}\right|$$

Expanding along $\mathbb{R}_{2},$ we et 

$$d \begin{aligned}\left|\mathbf{A}\right|=&\left.(-1)^{2+1}a_{21}\begin{vmatrix}a_{12}&a_{13}\\ a_{32}&a_{33}\end{vmatrix}+(-1)^{2+2}a_{22}\begin{vmatrix}a_{11}&a_{13}\\ a_{31}&a_{33}\end{vmatrix}\right.\\&+(-1)^{2+3}a_{23}\begin{vmatrix}a_{11}&a_{12}\\ a_{31}&a_{32}\end{vmatrix}\\=&-a_{21}(a_{12}a_{33}-a_{32}a_{13})+a_{22}(a_{11}a_{33}-a_{31}^3a_{13})\\&-a_{23}(a_{11}a_{32}-a_{31}a_{12})\\\left|\mathbf{A}\right|=&-a_{21}a_{12}a_{33}+a_{21}a_{32}a_{13}+a_{22}a_{11}a_{33}-a_{22}a_{31}a_{13}-a_{23}a_{11}a_{32}\\&+a_{23}a_{31}a_{12}\\=&a_{11}a_{22}a_{33}-a_{11}a_{23}a_{32}-a_{12}a_{21}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}\\&-a_{13}a_{31}a_{22}\\&-a_{13}a_{31}a_{22}\end{aligned} 2$$

Expansion along first Column $(\mathbf{C}_{1})$ 

$$|\mathbf{A}|=\left|\begin{aligned}{}&{{}\mathbf{a_{11}}}&{a_{12}}&{a_{13}}\\ {}&{{}\mathbf{a_{21}}}&{a_{22}}&{a_{23}}\\ {}&{{}\mathbf{a_{31}}}&{a_{32}}&{a_{33}}\end{aligned}\right|.$$

By expanding along $\mathrm{C}_{1}$ , we get 

$$\begin{aligned}\left|\AA\right|=&a_{11}(-1)^{1+1}\left|\begin{matrix}a_{22}&a_{23}\\ a_{32}&a_{33}\end{matrix}\right|+a_{21}(-1)^{2+1}\left|\begin{matrix}a_{12}&a_{13}\\ a_{32}&a_{33}\end{matrix}\right|\\&+a_{31}(-1)^{3+1}\left|\begin{matrix}a_{12}&a_{13}\\ a_{22}&a_{23}\end{matrix}\right|\\=&a_{11}(a_{22}a_{33}-a_{23}a_{32})-a_{21}(a_{12}a_{33}-a_{13}a_{32})+a_{31}(a_{12}a_{23}-a_{13}a_{22}).\end{aligned}$$

$$\begin{aligned}\left|\mathrm{A}\right|=&a_{11}a_{22}a_{33}-a_{11}a_{23}a_{32}-a_{21}a_{12}a_{33}+a_{21}a_{13}a_{32}+a_{31}a_{12}a_{23}\\&-a_{31}a_{13}a_{22}\\=&a_{11}a_{22}a_{33}-a_{11}a_{23}a_{32}-a_{12}a_{21}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}\\&-a_{13}a_{31}a_{22}\quad\ldots\quad(\end{aligned} (3), (2) and (3) are equal. It is left as an exercise to the )$$

Clearly, values of $\left[\left|A\right|\ln\left(1\right)\right.]$ , (2) and (3) are equal. It is left as an exercise to the reader to verify that the values of |A| by expanding along $\mathrm{R}_{3},\mathrm{C}_{2}\text{and}\mathrm{C}_{3}$ are equal to the value of $|\mathrm{A}|$ obtained in (1), (2) or (3).



Hence, expanding a determinant along any row or column gives same value.

## Remarks 

(i)For ialulati,whll expandtedrmintalontatwor column which contains maximum number of zeros.



(ii)While expanding, instead of multiplying by $(-1)^{i+j}$ , we can multiply $\mathrm{by}+1\ \mathrm{or}-1$ according as $(i+j)$ is even or odd.



(i)$\mathrm{Let}\mathrm{A}=\left[\begin{aligned}2&\quad2\\ 4&\quad0\end{aligned}\right]\mathrm{and}\mathrm{B}=\left[\begin{aligned}1&\quad1\\ 2&\quad0\end{aligned}\right]$ h   erifythat $A=2B$ .Also 

$|A|=0-8=-8and|B|=0-2=-2.$ 



Observe that,$|A|=4(-2)=2^2|B|\mathrm{or}|A|=2^n|B|$ 0where $n=2$ is the order of square matrices A and B.



In general, if $A=k B$ where A and B are square matrices of order n, then $|\mathrm{A}|=k^n$ 

$|B|,where n=1,2,3$ 



Example 3 Evaluate the determinan $\Delta=\left|\begin{aligned}1\quad&2\quad&4\\ -1\quad&3\quad&0\\ 4\quad&1\quad&0\end{aligned}\right|.$ 

Solution Notethat inthethird column,two nties are ero.So expandingalonghird column $\left(C_{3}\right)$ , we get 1E 



$$\Delta=4\left|\begin{matrix}-1&3\\ 4&1\end{matrix}\right|-0\left|\begin{matrix}1&2\\ 4&1\end{matrix}\right|+0\left|\begin{matrix}1&2\\ -1&3\end{matrix}\right|$$

$$\mathrm{E x a m p l e4E v a l u a t e}\Delta=\left|\begin{matrix}{0}&{\sin\alpha}&{-\cos\alpha}\\ {-\sin\alpha}&{0}&{\sin\beta}\\ {\cos\alpha}&{-\sin\beta}&{0}\\ \end{matrix}\right|.$$

Solution Expanding along $\mathbb{R}_{\mathrm{r}}$ , we get 

$$\begin{aligned}\Delta&=0\left|\begin{matrix}0&\sin\beta\\-\sin\beta&0\end{matrix}\right|-\sin\alpha\left|\begin{matrix}-\sin\alpha&\sin\beta\\\cos\alpha&0\end{matrix}\right|-\cos\alpha\left|\begin{matrix}-\sin\alpha&0\\\cos\alpha&-\sin\beta\end{matrix}\right|\\&=0-\sin\alpha\left(0-\sin\beta\cos\alpha\right)-\cos\alpha\left(\sin\alpha\sin\beta-0\right)\\&=\sin\alpha\sin\beta\cos\alpha-\cos\alpha\sin\alpha\sin\beta=0\end{aligned}$$

Example 5 Find values of x for which  $\begin{bmatrix}3&x\\ x&1\end{bmatrix}=\begin{bmatrix}3&2\\ 4&1\end{bmatrix}$ .

Solution We have $$ −

i.e.b $$ 

i.e.

$$x^{2}=8$$

Hence 

$$x=\pm2\sqrt{2}$$

### EXERCISE 4.1

Exercises 1 and 2.



$\begin{pmatrix}2&4\\-5&-1\end{pmatrix}$ 

2. (i)$\begin{bmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{bmatrix}$ me (ii)$$ 

3.If $$ [Tab_]

4.If $\mathrm{A}=\begin{bmatrix}1&0&1\\ 0&1&2\\ 0&0&4\end{bmatrix}$ , tl $\mathrm{then~show~that~}|3\mathrm{A}|=27|\mathrm{A}|$ 

5. Evaluate the determinants 

(i)

$$\begin{pmatrix}3&-1&-2\\0&0&-1\\3&-5&0\end{pmatrix}$$

(ii)

$$\begin{pmatrix}3&-4&5\\1&1&-2\\2&3&1\end{pmatrix}$$

(i)$\begin{aligned}&\begin{bmatrix}0&1&2\\ -1&0&-3\\ -2&3&0\end{bmatrix}\\ \end{aligned}$ (iv)$\begin{bmatrix}2&-1&-2\\ 0&2&-1\\ 3&-5&0\end{bmatrix}$ 

6.

$\mathrm{If}\mathrm{A}=\left[\begin{aligned}1\quad&1\quad&-2\\ 2\quad&1\quad&-3\\ 5\quad&4\quad&-9\end{aligned}\right]$ $\mathrm{find}\left|\mathrm{A}\right|$ 

7. Find values of x, if 

(i)$\begin{aligned}\left|\begin{vmatrix}2&4\\5&1\end{vmatrix}\right|=\left|\begin{matrix}2x&4\\6&x\end{matrix}\right|\end{aligned}$ (ii)$$ 

8.If $\begin{vmatrix}x&2\\ 18&x\end{vmatrix}=\begin{vmatrix}6&2\\ 18&6\end{vmatrix}$ , then x is equal to 

(A)6(B)$\pm6$ $-6$ (D)0

### 4.3 Area of a Triangle 

In earlier classes, we have studied that the area of a trianglewhoseverticesare $(x_{1},y_{1}),(x_{2},y_{2})$ and $(x_{3},y_{3})$ 1, is given by the expression $\frac{1}{2}\left[x_{1}(y_{2}-y_{3})+x_{2}(y_{3}-y_{1})+\right.]$ $x_{3}\left(y_{1}-y_{2}\right)$ |. Now this expression can be writen in the form of a determinant as 

$$\Delta=\frac{1}{2}\left|\begin{matrix}x_{1}&y_{1}&1\\ x_{2}&y_{2}&1\\ x_{3}&y_{3}&1\end{matrix}\right|$$

## Remarks 

(i) Since area is a positive quantity, we always take the absolute value of the determinant in (1).



(ii)If area is given, use both positive and negative values of the determinant for calculation.



(i) The area of the triangle formed by three collinear points is zero.

Example 6 Find the area of the triangle whose vertices are (3, 8), (− 4, 2) and (5, 1)Solution The area of triangle is given by 



$$\Delta=\frac{1}{2}\left|\begin{matrix}3&8&1\\ -4&2&1\\ 5&1&1\end{matrix}\right|$$

$$\frac{1}{2}\left[3(2-1)-8(-4-5)+1(-4-10)\right]$$

Example 7 Find the equation of the line joining A(1, 3) and B (0, 0) using determinants and find  if D(k, 0) is a point such that area of triangle ABD is 3sq units.

Solution LetP (x, ) be any point on AB. Then, area of triangle ABP is zero (Why?). So 

This gives 

$$\begin{aligned}&\left\{\begin{aligned}\frac{1}{2}\left|\begin{matrix}0&0&1\\ 1&3&1\\ x&y&1\end{matrix}\right|=0\\ \frac{1}{2}(y-3x)&=0or y=3x,\end{aligned}\right.\\ \end{aligned}$$

which is the equation of required line AB.

Also, since the area of the triangle ABD is 3 sq. units, we have 

$$\frac{1}{2}\left|\begin{matrix}1&3&1\\ 0&0&1\\ k&0&1\end{matrix}\right|=\pm3$$

This gives,$\frac{-3k}{2}=\pm3,i.e.,k=\mp2$ 

### EXERCISE 4.2

1.Find areaofthetriangle withverticesat the point giveninachofthefollowing :(i)c $(1,0),(6,0),(\overline{4,3})$ (ii) (2, 7), (1, 1), (10, 8)

(ii)$(-2,-3),(3,2),(-1,-8)$ 

2. Show that points 

A $(a,b+c),\mathrm{B}(b,c+a),\mathrm{C}(c,a+b)$ are collinear.

3.Findvloioliuderices are 

(i)[Ta]EM $(k,0),(4,0),(0,2)$ 司司(ii)$(-2,0),(0,4),(0,k)$ (ci)c 

a 

aa 

(A)12(B)-2(C)$-12,-2$ (D)$12,-2$ 

### 4.4 Minors and Cofactors 

Inthis tillxotimpct orm using minors and cofactors.



Definition 1 Minor of an element $a_{ij}$ of a determinat is the determiant obtained deleting itihw anlumiwic ement $a_{ij}$ lies. Minor of an element $a_{ij}$ is denoted by $\mathbf{M}_{ij^{'}}$ 



Remark Minor of an element of a determinant of order $n(n\geq2)$  is a determinant of order $n-1$ 

$$Example8Find the minor of element$6$in the determinant$\Delta=\left|\begin{matrix}{1}&{2}&{3}\\ {4}&{5}&{6}\\ {7}&{8}&{9}\\ \end{matrix}\right|$ $$

Solution Since 6 lies in the second row and third column, its minor $\mathrm{M}_{23}$ 

$$M_{23}=\left|\begin{matrix}1&2\\ 7&8\end{matrix}\right|=8-14=-6(obtained by deflecting R_2and C_3in\Delta).$$

Definition2 Cofactor of anelement $a_{ij}$ , denoted by $\Lambda_{ij}$ is defined by 

$$A_{ij}=(-1)^{i+j}M_{ij},where M_{ij}is minor of a_{ij}.$$

Example 9 Find minors and cofactors of all the elements of the determinant $\begin{aligned}&\begin{vmatrix}\\ &1&-2\\&4&3\\ &\end{vmatrix}\\ \end{aligned}$ 

$$\begin{array}{l}\text{Soluition Minor of the element}a_{ij}\text{is}\bar{\mathrm{M}}_{ij}\\\quad\text{Here}a_{11}=1.\mathrm{~So}\mathrm{~M}_{11}=\mathrm{Minor}\text{of}a_{11}=3\\\quad\mathrm{M}_{12}=\mathrm{Minor}\text{of the element}a_{12}=4\\\quad\mathrm{M}_{21}=\mathrm{Minor}\text{of the element}a_{21}=-2\\\quad\mathrm{M}_{22}=\mathrm{Minor}\text{of the element}a_{22}=1\\\quad\mathrm{Now},\text{cofactor}\text{of}a_{ij}\text{is}\mathrm{A}_{ij}.\mathrm{~So}\\\quad\mathrm{A}_{11}=\left(-1\right)^{1+1}\mathrm{~M}_{11}=\left(-1\right)^{2}(3)=3\\\quad\mathrm{A}_{12}=\left(-1\right)^{1+2}\mathrm{~M}_{12}=\left(-1\right)^{3}(4)=-4\\\quad\mathrm{A}_{21}=\left(-1\right)^{2+1}\mathrm{~M}_{21}=\left(-1\right)^{3}(-2)=2\\\quad\mathrm{A}_{22}=\left(-1\right)^{2+2}\mathrm{~M}_{22}=\left(-1\right)^{4}(1)=1\end{array}$$

Example 10 Find minors and cofactors of the elements $a_{11},a_{21}$ in the determinant 

$$\Delta=\left|\begin{aligned}&a_{11}&a_{12}&a_{13}\\ &a_{21}&a_{22}&a_{23}\\ &a_{31}&a_{32}&a_{33}\end{aligned}\right|$$

Solution By definition of minors and cofactors, we have 

$$\begin{aligned}&\text{Minor of}a_{11}=\mathrm{M}_{11}=\begin{vmatrix}a_{22}&a_{23}\\a_{32}&a_{33}\end{vmatrix}=a_{22}a_{33}-a_{23}a_{32}\\ &\text{Cofactor of}a_{11}=\mathrm{A}_{11}=(-1)^{_{1+1}}\mathrm{~M}_{11}=a_{22}a_{33}-a_{23}a_{32}\\ &\text{Minor of}a_{21}=\mathrm{M}_{21}=\begin{vmatrix}a_{12}&a_{13}\\a_{32}&a_{33}\end{vmatrix}=a_{12}a_{33}-a_{13}a_{32}\\ \end{aligned}$$

Cofactor of $a_{21}=A_{21}=(-1)^{2+1}\quad M_{21}=(-1)(a_{12}a_{33}-a_{13}a_{32})=a_{12}a_{33}+a_{13}a_{32}$ -hed Remark Expanding the determinant ∆, in Example 21, along R, we have 

$$\Delta=(-1)^{1+1}a_{11}\left|\begin{matrix}a_{22}&a_{23}\\ a_{32}&a_{33}\end{matrix}\right|+(-1)^{1+2}a_{12}\left|\begin{matrix}a_{21}&a_{23}\\ a_{31}&a_{33}\end{matrix}\right|+(-1)^{1+3}a_{13}\left|\begin{matrix}a_{21}&a_{22}\\ a_{31}&a_{32}\end{matrix}\right|$$

$a_{11}A_{11}+a_{12}A_{12}+a_{13}A_{13}$ where $ A_{ij}$ is cofactor of $a_{ij}$ 

= sum of product of elements of $\mathbb{R}_{\mathrm{r}}$ with their corresponding cofactors 

$C_{1},C_{2}$ i and $ C_{3}$ $\mathbb{R}_{2},\mathbb{R}_{3}$ 

Hence $\Delta=sum$ of the product of elements of any row (or column) with their corresponding cofactors.



Notemowoludwo other row(or column), then their sum is zero.For example,

$$\begin{aligned}&\Delta=a_{11}^{1}A_{21}^{1}+a_{12}A_{22}+a_{13}A_{23}\\&\quad=a_{11}^{1}(-1)^{1+1}\left|\begin{matrix}a_{12}&a_{13}\\a_{32}&a_{33}\end{matrix}\right|+a_{12}^{1}(-1)^{1+2}\left|\begin{matrix}a_{11}&a_{13}\\a_{31}&a_{33}\end{matrix}\right|+a_{13}^{1}(-1)^{1+3}\left|\begin{matrix}a_{11}&a_{12}\\a_{31}&a_{32}\end{matrix}\right|\\&\quad=\left|\begin{matrix}a_{11}&a_{12}&a_{13}\\a_{11}&a_{12}&a_{13}\\a_{31}&a_{32}&a_{33}\end{matrix}\right|=0(since R_{1}and R_{2}are identical)\\ \end{aligned}$$

Similarly, we can try for other rows and columns.

Example 11 Find minors and cofactors of the elements of the determinant 

$$\begin{vmatrix}2&-3&5\\6&0&4\\1&5&-7\end{vmatrix} + a_{a_{12}}A_{a_{32}}+a_{a_{13}}A_{a_{33}}=0$$

### EXERCISE 4.3

Write Minors and Cofactors of the elements of following determinants:

$$\begin{aligned}&1\text{.}(i)\left|\begin{matrix}2&-4\\ 0&3\end{matrix}\right|\quad&(ii)\left|\begin{matrix}a&c\\ b&d\end{matrix}\right|\\&2\text{.}(i)\left|\begin{matrix}1&0&0\\ 0&1&0\\ 0&0&1\end{matrix}\right|\quad&(ii)\left|\begin{matrix}1&0&4\\ 3&5&-1\\ 0&1&2\end{matrix}\right|\end{aligned}$$

3. Using Cofactors of elements of second row, evaluate $\Delta=\left|\begin{matrix}5&3&8\\ 2&0&1\\ 1&2&3\end{matrix}\right|$ ed 

$\Delta=\begin{vmatrix}1&x&yz\\ 1&y&zx\\ 1&z&xy\end{vmatrix}$ 

5.If $\Delta=\left|\begin{aligned}&a_{11}&a_{12}&a_{13}\\ &a_{21}&a_{22}&a_{23}\\ &a_{31}&a_{32}&a_{33}\end{aligned}\right|$ and $\mathrm{A}_{ij}$ isCo ctors $a_{ij}$ then value of ∆ is given by 

(A)

(C)

$$\begin{array}{l}a_{11}A_{31}+a_{12}A_{32}+a_{13}A_{33}\quad(B)\quad a_{11}A_{11}+a_{12}A_{21}+a_{13}A_{31}\\a_{21}A_{11}+a_{22}A_{12}+a_{23}A_{13}\quad(D)\quad a_{11}A_{11}+a_{21}A_{21}+a_{31}A_{31}\end{array}$$

### 4.5 Adjoint and Inverse of a Matrix 

In the previous chapter, we have studied inverse of a matrix.In this section, we shall discuss the condition for existence of inverse of a matrix.



To find inverse of a matrix A, i.e.,$\mathrm{A}^{-1}$ we shall first define adjoint of a matrix.

#### 4.5.1 Adjoint of a matrix 

Definition 3 The adjoint of a square matrix $A=\left[a_{ij}\right]_{n\times n}$ is defined as the transpose of the matrix $\left[\mathbf{A}_{ij}\right]_{n\times n^{2}}$ ,where $\mathrm{A}_{ij}$ is the cofactor of the element $a_{ij}$ . Adjoint of the matrix A is denoted by adj A.



Let 

$$\mathbf{A}=\begin{bmatrix}a_{11}&a_{12}&a_{13}\\ a_{21}&a_{22}&a_{23}\\ a_{31}&a_{32}&a_{33}\end{bmatrix}$$

Then 

$$a d j\mathrm{A}=\mathrm{Transposeof}\left[\begin{aligned}\mathrm{A}_{11}&\quad\mathrm{A}_{12}&\quad\mathrm{A}_{13}\\ \mathrm{A}_{21}&\quad\mathrm{A}_{22}&\quad\mathrm{A}_{23}\\ \mathrm{A}_{31}&\quad\mathrm{A}_{32}&\quad\mathrm{A}_{33}\end{aligned}\right]=\left[\begin{aligned}\mathrm{A}_{11}&\quad\mathrm{A}_{21}&\quad\mathrm{A}_{31}\\ \mathrm{A}_{12}&\quad\mathrm{A}_{22}&\quad\mathrm{A}_{32}\\ \mathrm{A}_{13}&\quad\mathrm{A}_{23}&\quad\mathrm{A}_{33}\end{aligned}\right]$$

Example 12  Find adj A for $A=\begin{bmatrix}2&3\\ 1&4\end{bmatrix}$ 

Solution We have $A_{11}=4,A_{12}=-1,A_{21}=-3,A_{22}=2$ 

Hence 

$$A_{11}=4,A_{12}=-1,A_{21}=-3,A_{22}=2 \begin{bmatrix}adj\;A=\begin{bmatrix}A_{11}&A_{21}\\ A_{12}&A_{22}\end{bmatrix}=\begin{bmatrix}4&-3\\ -1&2\end{bmatrix}\end{bmatrix} lished $$

Remark For a square matrix of order 2, given by 

$$\mathrm{A}=\begin{bmatrix}a_{11}&a_{12}\\ a_{21}&a_{22}\end{bmatrix}$$

The adj Aa alobobaind by iterchanging $a_{11}$ and ,$a_{22}$ and by changing signs i d of $a_{12}$ and $a_{21}$ , i.e.,

$$a d j\mathrm{A}=\left[\begin{matrix}{\left(\overline{{a_{11}}}\right)}&{\overline{{a_{12}}}}\\ {\left(\overline{{a_{21}}}\right)}&{\overline{{a_{22}}}}\\ {\downarrow}&{\overline{{a_{21}}}}\\ \end{matrix}\right]=\left[\begin{matrix}{\overline{{a_{22}}}}&{-\overline{{a_{12}}}}\\ {-\overline{{a_{21}}}}&{\overline{{a_{11}}}}\\ \end{matrix}\right]Change sign Interchange $$

<div style="text-align: center;">Change sign Interchange </div>


We state the following theorem without proof.

Theorem 1 If A be any given square matrix of order , then 

$$\mathrm{A}(a d j\mathrm{~A})=(a d j\mathrm{~A})\mathrm{~A}=|\mathrm{~A}|\mathrm{~I}$$

where I is the identity matrix of order n 

Verification 

Let 

$$\mathrm{A}=\begin{bmatrix}a_{11}&a_{12}&a_{13}\\ a_{21}&a_{22}&a_{23}\\ a_{31}&a_{32}&a_{33}\end{bmatrix},\quad\mathrm{then}\quad adj\quad\mathrm{A}=\begin{bmatrix}\mathrm{A}_{11}&\mathrm{A}_{21}&\mathrm{A}_{31}\\ \mathrm{A}_{12}&\mathrm{A}_{22}&\mathrm{A}_{32}\\ \mathrm{A}_{13}&\mathrm{A}_{23}&\mathrm{A}_{33}\end{bmatrix}$$

Since sum of product of elements of a row (or a column) with corresponding cofactors is equal to $|\mathrm{A}|$ and otherwise zero, we have 

$$\mathrm{A}\left(a d j\mathrm{A}\right)=\left[\begin{matrix}\left|\mathrm{A}\right|&0&0\\ 0&\left|\mathrm{A}\right|&0\\ 0&0&\left|\mathrm{A}\right|\end{matrix}\right]=\left|\mathrm{A}\right|\left[\begin{matrix}1&0&0\\ 0&1&0\\ 0&0&1\end{matrix}\right]=\left|\mathrm{A}\right|\mathrm{I}$$

Similarly, we can show $(adj\;A)\;A=\left|A\right|\;I$ 

Hence A $(adj\;A)=(adj\;A)\;A=\left|A\right|$ 

Definition 4 A square matrix A is said to be singular if $$ ，

For example, the determinat of matrix $\mathrm{A}=\begin{bmatrix}1&2\\ 4&8\end{bmatrix}$ is 

Hence A is a singular matrix.

DefinitionquaremixAiaidtobo-singular if if $$ ,

Let 

$$\mathrm{A}=\begin{bmatrix}1&2\\3&4\end{bmatrix}.\mathrm{Then}\left|\mathrm{A}\right|=\begin{vmatrix}1&2\\3&4\end{vmatrix}=4-6=-2\neq0.$$

Hence A is a nonsingular matrix 

We state the following theorems without proof.

Theorem 2 If A and B are nonsingular matrices of the same order, then AB and BA are also nonsingular matrices of the same order.



Theorem 3 The determinant of the product of matrices is equal to product of their respective determinants, that is,$|AB|=|A||B|$ , where A and B are square matrices of the same order 



$$\mathrm{Re}_{\mathrm{CH}_{\mathrm{H}}}\mathrm{K}\mathrm{We}\text{know that}(a d j\mathrm{A})\mathrm{A}=\left|\mathrm{A}\right|\mathrm{I}=\left[\begin{matrix}\left|\mathrm{A}\right|&0&0\\ 0&\left|\mathrm{A}\right|&0\\ 0&0&\left|\mathrm{A}\right|\end{matrix}\right],|\mathrm{A}|\neq0$$

Writing determinants of matrices on both sides, we have 

$$\left|(a d j\mathbf{A})\mathbf{A}\right|=\left|\begin{matrix}{\left|\mathbf{A}\right|}&{0}&{0}\\ {0}&{\left|\mathbf{A}\right|}&{0}\\ {0}&{0}&{\left|\mathbf{A}\right|}\end{matrix}\right|$$

i.e.

$$|(a d j\;\mathrm{A})|\;|\mathrm{A}|=\left|\mathrm{A}\right|^{3}\left|\begin{matrix}1&0&0\\ 0&1&0\\ 0&0&1\end{matrix}\right|$$

i.e.

$$|(a d j\mathrm{A})||\mathrm{A}|=|\mathrm{A}|^3$$

(1)

i.e 

$$|(a d j\mathrm{A})|=|\mathrm{A}|^2$$

E $|a d j(\mathrm{A})|=|\mathrm{A}|^{n-1}$ 

Theorem 4 A square matrix A is invertible if and only if A is nonsingular matrix.Proof Let A be invertible matrix of order n and I be the identity matrix of order n.Then, there exists a square matrix B of order n such that $AB=BA=I$ 

Now 

$$\mathrm{AB}=\mathrm{I}.\ \mathrm{So}\ |\mathrm{AB}|=|\mathrm{I}|\quad\mathrm{or}\ |\mathrm{A}|\ |\mathrm{B}|=1\quad(\mathrm{since}\ |\mathrm{I}|=1,|\mathrm{AB}|=|\mathrm{A}||\mathrm{B}|)$$

This gives 

$\left|\mathbf{A}\right|\neq0$    guiur.

Conversely, let A be nonsingular. Then $$ 

Now 

$$\mathrm{A}(a d j\mathrm{A})=(a d j\mathrm{A})\mathrm{A}=|\mathrm{A}|\mathrm{I}$$

(Theorem 1)

or 

$$\mathrm{A}\left(\frac{1}{|\mathrm{A}|}\mathrm{a}d j\mathrm{A}\right)=\left(\frac{1}{|\mathrm{A}|}\mathrm{a}d j\mathrm{A}\right)\mathrm{A}=\mathrm{E}$$

or 

$$\mathrm{AB}=\mathrm{BA}=\mathrm{I},\quad\mathrm{where}\quad\mathrm{B}=\frac{1}{|\mathrm{A}|}\mathrm{adj}\mathrm{A}$$

Thus $\mathrm{A}is invertible and\mathrm{A}^{-1}=\frac{1}{|\mathrm{A}|}adj\mathrm{A}$ 

Example 13 If $A=\begin{bmatrix}1&3&3\\ 1&4&3\\ 1&3&4\end{bmatrix}$ , then verify that A adj $A=|A|\;{\mathrm{I}}.$ . Also find $\mathbf{A}^{-1}$ 

Solution $\mathrm{We have}\left|\mathrm{A}\right|=1\left(16-9\right)-3\left(4-3\right)+3\left(3-4\right)=1\neq0$ 

Now $\mathbf{A}_{11}=7$ $A_{12}=-1,A_{13}=-1,A_{21}=-3,A_{22}=1,A_{23}=0,A_{31}=-3,A_{32}=0$ 

$A_{33}=1$ 



Therefore 

$$a d j\mathrm{A}=\left[\begin{aligned}7\quad-3\quad-3\\ -1\quad1\quad0\\ -1\quad0\quad1\end{aligned}\right]$$

Now 

$$\begin{aligned}A(adj A)&=\begin{bmatrix}1&3&3\\1&4&3\\1&3&4\end{bmatrix}\begin{bmatrix}7&-3&-3\\-1&1&0\\-1&0&1\end{bmatrix}\\&=\begin{bmatrix}7-3-3&-3+3+0&-3+0+3\\7-4-3&-3+4+0&-3+0+3\\7-3-4&-3+3+0&-3+0+4\end{bmatrix}\\&=\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}=(1)\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}=\left|A\right|.\end{aligned} D $$

Also 

$$\mathrm{A}^{-1}=\frac{1}{|\mathrm{A}|}adj\mathrm{A}=\frac{1}{1}\left[\begin{aligned}7\quad-3\quad-3\\ -1\quad1\quad0\\ -1\quad0\quad1\end{aligned}\right]=\left[\begin{aligned}7\quad-3\quad-3\\ -1\quad1\quad0\\ -1\quad0\quad1\end{aligned}\right]$$

Example 14$\mathrm{If}\;\mathrm{A}=\begin{bmatrix}2&3\\ 1&-4\end{bmatrix}\;\mathrm{and}\;\mathrm{B}=\begin{bmatrix}1&-2\\ -1&3\end{bmatrix},\;\mathrm{then}\;\mathrm{verify}\;\mathrm{that}\;(\mathrm{AB})^{-1}=\mathrm{B}^{-1}\mathrm{A}^{-1}$ 

Solution We have $\mathrm{AB}=\begin{bmatrix}2&3\\ 1&-4\end{bmatrix}\begin{bmatrix}1&-2\\ -1&3\end{bmatrix}=\begin{bmatrix}-1&5\\ 5&-14\end{bmatrix}$ 刀



Since,$\left|\mathrm{AB}\right|=-11\neq0,\left(\mathrm{AB}\right)^{-1}$ exists and is given by 

$$\left(\mathrm{AB}\right)^{-1}=\frac{1}{\left|\mathrm{AB}\right|}\mathrm{adj}\left(\mathrm{AB}\right)=-\frac{1}{11}\left[-14-5\right]^{-1}=\frac{1}{11}\left[\frac{14}{5}\right]^{-1}$$

Further,$$ .Therefore,$\mathrm{A^{-1}\;a n d\;B^{-1}}$ both exist and are given by 

$$\mathrm{A}^{-1}=-\frac{1}{11}\begin{bmatrix}-4&-3\\ -1&2\end{bmatrix},\mathrm{B}^{-1}=\begin{bmatrix}3&2\\ 1&1\end{bmatrix}$$

fore 

$$\mathrm{B}^{-1}\mathrm{A}^{-1}=-\frac{1}{11}\left[\begin{matrix}3&2\\1&1\end{matrix}\right]\left[\begin{matrix}-4&-3\\-1&2\end{matrix}\right]=-\frac{1}{11}\left[\begin{matrix}-14&-5\\-5&-1\end{matrix}\right]=\frac{1}{11}\left[\begin{matrix}14&5\\5&1\end{matrix}\right]$$

Hence $(AB)^{-1}=B^{-1}A^{-1}$ 

Example 15 Show that the matrix $A=\begin{bmatrix}2&3\\ 1&2\end{bmatrix}$ satisfies the equation $A^{2}-4A+I=O$ where I is $2\times2$ identity matrix and O is $2\times2$ zero matrix. Using this equation, find $\mathrm{A^{-1}}$ Solution We have $\left[\mathrm{A}^{2}=\mathrm{A}.\mathrm{A}=\left[\begin{aligned}2\quad3\\ 1\quad2\end{aligned}\right]\left[\begin{aligned}2\quad3\\ 1\quad2\end{aligned}\right]=\left[\begin{aligned}7\quad12\\ 4\quad7\end{aligned}\right]\right.]$ 

Hence 

$$\left[\mathrm{A}^{2}-4\mathrm{A}+\mathrm{I}=\left[\begin{aligned}7&\quad12\\ 4&\quad7\end{aligned}\right]-\left[\begin{aligned}8&\quad12\\ 4&\quad8\end{aligned}\right]+\left[\begin{aligned}1&\quad0\\ 0&\quad1\end{aligned}\right]\right]=\left[\begin{aligned}0&\quad0\\ 0&\quad0\end{aligned}\right]=\mathrm{O} lisi.ed $$

Now 

$$A^{2}-4A+I=O $$

Therefore $\mathrm{AA}-4\mathrm{A}=-\mathrm{I}$ 

or 

$$\mathrm{A}\mathrm{A}\left(\mathrm{A}^{-1}\right)-4\mathrm{A}\mathrm{A}^{-1}=-\mathrm{I}\mathrm{A}^{-1}\left(\text{Post multiplying by}\mathrm{A}^{-1}\text{because}|\mathrm{A}|\neq0\right) lisi.ed $$

or 

$$\mathrm{A}\left(\mathrm{A}\mathrm{A}^{-1}\right)-4\mathrm{I}=-\mathrm{A}^{-1}$$

or 

$$\mathrm{AI}-4\mathrm{I}=-\mathrm{A}^{-1}$$

or 

$$\mathrm{A}^{-1}=4\mathrm{I}-\mathrm{A}=\begin{bmatrix}4&0\\0&4\end{bmatrix}-\begin{bmatrix}2&3\\1&2\end{bmatrix}=\begin{bmatrix}2&-3\\-1&2\end{bmatrix} lisi.ed $$

Hence 

$$\mathbf{A}^{-1}=\begin{bmatrix}2&-3\\ -1&2\end{bmatrix}$$

EXERCISE 4.4

Find adjoint of each of the matrices in Exercises 1 and 2.

$$\begin{aligned}&1.\begin{bmatrix}1&2\\ 3&4\end{bmatrix}\quad&2\quad\begin{bmatrix}1&-1&2\\ 2&3&5\\ -2&0&1\end{bmatrix}\end{aligned}$$

Verify A $(adj\;A)=(adj\;A)\;A=|A|\;I$ in Exercises 3 and 4

$$\begin{aligned}13.\ \begin{bmatrix}2&3\\ -4&-6\end{bmatrix}\quad4.\ \begin{bmatrix}1&-1&2\\ 3&0&-2\\ 1&0&3\end{bmatrix}\end{aligned}$$

Find the inverse of each of the matrices (if it exists) given in Exercises 5 to 11.

5.$\begin{bmatrix}2&-2\\ 4&3\end{bmatrix}$ 

6.$\begin{bmatrix}-1&5\\ -3&2\end{bmatrix}$ 

7.

$$\begin{bmatrix}1&2&3\\ 0&2&4\\ 0&0&5\end{bmatrix}$$

8.$\begin{bmatrix}1&0&0\\ 3&3&0\\ 5&2&-1\end{bmatrix}$ 9.$\begin{bmatrix}2&1&3\\ 4&-1&0\\ -7&2&1\end{bmatrix}$ 10.$\begin{bmatrix}1&-1&2\\ 0&2&-3\\ 3&-2&4\end{bmatrix}$ 

11.

$$\begin{pmatrix}\left[\begin{matrix}1&0&0\\0&\cos\alpha&\sin\alpha\\0&\sin\alpha&-\cos\alpha\end{matrix}\right]\end{pmatrix}$$

12.$\mathrm{Let}\;\mathrm{A}=\begin{bmatrix}3&7\\ 2&5\end{bmatrix}\;\mathrm{and}\;\mathrm{B}=\begin{bmatrix}6&8\\ 7&9\end{bmatrix}$ . Verify that $(AB)^{-1}=B^{-1}A^{-1}$ 

13. If $A=\begin{bmatrix}3&1\\ -1&2\end{bmatrix}$ , show that $A^{2}-5A+7I=O$ . Hence find $\mathrm{A}^{-1}$ 

14. For the matrix $\mathrm{A}=\begin{bmatrix}3&2\\1&1\end{bmatrix}$ $A^{2}+aA+bI=O$ 

15. For the matrix $A=\begin{bmatrix}1&1&1\\ 1&2&-3\\ 2&-1&3\end{bmatrix}$ 

Show that $A^{3}-6A^{2}+5A+11I=O.Hence$ ,find $\mathrm{A}^{-1}$ 

16.1$\mathrm{f}\mathrm{A}=\begin{bmatrix}2&-1&1\\ -1&2&-1\\ 1&-1&2\end{bmatrix}$ 

Verify that $A^{3}-6A^{2}+9A-4I=O$ and hence find $\mathrm{A^{-1}}$ 

17. Let A be a nonsingular square matrix of order $3\times3$ .Then $|a d j\mathrm{A}|$ is equal to (A)$|\mathrm{A}|$ (B)$|\mathbf{A}|^{2}$ (C)$|\mathrm{A}|^{3}$ (D)$3|\mathrm{A}|$ 

18. IfA is an invertible matrix of order 2, then det $(\mathrm{A^{-l}})$ is equal to 

(A) det (A)(B)$\frac{1}{\det\left(\mathrm{A}\right)}$ (C)1(D)0

### 4.6 Applications of Determinants and Matrices 

Inthis section,we shall dicuss appliaioofdtrmiats and matricsor olving th system of linar quaions intwoor threariables and forchecking theconsiny of the system of linear equations.



Consistent system A system ofequations is said to beconsistent if its solution (one or more) exists.



Inconsistent system A system of equations is said to be inconsistent if its solution does not exist.



NotIawulmoion having unique solutions only.



4.6.1Solution of system of linear equations using inverseof a matrix Let us expressthe systemof linearquations as matrixequations and solvehm using inverse of the coefficient matrix.a 

Consider the system of equations 

Let 

$$\begin{array}{c}a_{1}x+b_{1}y+c_{1}z=d_{1}\\a_{2}x+b_{2}y+c_{2}z=d_{2}\\a_{3}x+b_{3}y+c_{3}z=d_{3}\\\mathrm{A}=\begin{bmatrix}a_{1}&b_{1}&c_{1}\\a_{2}&b_{2}&c_{2}\\a_{3}&b_{3}&c_{3}\end{bmatrix},\mathrm{X}=\begin{bmatrix}x\\y\\z\end{bmatrix}\mathrm{and}\mathrm{B}=\begin{bmatrix}d_{1}\\d_{2}\\d_{3}\end{bmatrix}\end{array}$$

T as,$$ , i.e.,, i.e.,

$$Then, the system of equations can be written as,\begin{bmatrix}a_{1}&b_{1}&c_{1}\\ a_{2}&b_{2}&c_{2}\\ a_{3}&b_{3}&c_{3}\end{bmatrix}\begin{bmatrix}x\\ y\\ z\end{bmatrix}=\begin{bmatrix}d_{1}\\ d_{2}\\ d_{3}\end{bmatrix}$$

Case I IfAis a nonsingular matrix,then its inverse exists. Now 

or 

or 

or 

or 

$$\begin{aligned}\bar{\mathrm{AX}}&=\mathrm{B}\\\mathrm{A}^{-1}(\mathrm{AX})&=\mathrm{A}^{-1}\mathrm{B}\\(\mathrm{A}^{-1}\mathrm{A})\mathrm{X}&=\mathrm{A}^{-1}\mathrm{B}\\\mathrm{I}\mathrm{X}&=\mathrm{A}^{-1}\mathrm{B}\\\mathrm{X}&=\mathrm{A}^{-1}\mathrm{B}\end{aligned}$$

(premultiplying by $\mathrm{A}^{-1}$ (cid)(by associative property)

This matrix equation provides unique solution for the given system of equations as inverse of a matrix is unique. This method of solving system of equations isknown as Matrix Method.



Case II IfA is a singular matrix, then $|A|=0$ 

In this case, we calculate (adj A) B.

If $(a d j\;\mathrm{A})\;\mathrm{B}\neq\mathrm{O},$ , (O being zero matrix), then solution does not exist and the system of equations is called inconsistent.



If $(adj\mathrm{A})\mathrm{B}=\mathrm{O}$ , then system may be either consistent or inconsistent according as the system have either infinitely many solutions or no solution.

Example 16 Solve the system of equations 

$$\begin{aligned}2x+5y&=1\\3x+2y&=7\end{aligned}$$

Solution The system of equations can be written in the form $\mathrm{AX}=\mathrm{B}$ , where 

$$\mathrm{A}=\begin{bmatrix}2&5\\3&2\end{bmatrix},\mathrm{X}=\begin{bmatrix}x\\y\end{bmatrix}\text{and}\mathrm{B}=\begin{bmatrix}1\\7\end{bmatrix}$$

Now,$|A|=-11\neq0$ 



Note that 

$$\mathrm{A}^{-1}=-\frac{1}{11}\left[\begin{aligned}2&-5\\ -3&2\end{aligned}\right]$$

Therefore 

$$\mathrm{X}=\mathrm{A}^{-1}\mathrm{B}=-\frac{1}{11}\left[\begin{aligned}2&-5\\-3&2\end{aligned}\right]\left[\begin{aligned}1\\7\end{aligned}\right]$$

i.e.

Hence 

$$\left[\begin{aligned}x\\ y\end{aligned}\right]=-\frac{1}{11}\left[\begin{aligned}-33\\ 11\end{aligned}\right]=\left[\begin{aligned}3\\ -1\end{aligned}\right]$$

Example 17 Solve the following system of equations by matrix method.

$$\begin{align*}3x-2y+3z&=8,\\2x+y-z&=1,\\4x-3y+2z&=4.\end{align*}$$

Solution The system of equations can be written in the form $\mathrm{AX}=\mathrm{B}$ ,where 

$$\left[\mathrm{A}=\begin{bmatrix}3&-2&3\\ 2&1&-1\\ 4&-3&2\end{bmatrix},\mathrm{X}=\begin{bmatrix}x\\ y\\ z\end{bmatrix}\text{and}\mathrm{B}=\begin{bmatrix}8\\ 1\\ 4\end{bmatrix}\right]$$

We see that 

$$\left|\bar{A}\right|=3(2-3)+2(4+4)+3(-6-4)=-17\neq0$$

Hence, A is nonsingular and so its inverse exists. Now 

$$\begin{array}{rlrlrl}&{\mathrm{A}_{11}=-1,}&&{\mathrm{A}_{12}=-8,}&&{\mathrm{A}_{13}=-10}\\ &{\mathrm{A}_{21}=-5,}&&{\mathrm{A}_{22}=-6,}&&{\mathrm{A}_{23}=1}\\ &{\mathrm{A}_{31}=-1,}&&{\mathrm{A}_{32}=9,}&&{\mathrm{A}_{33}=7}\end{array}$$

Therefore 

$$\mathrm{A}^{-1}=-\frac{1}{17}\begin{bmatrix}-1&-5&-1\\-8&-6&9\\-10&1&7\end{bmatrix}$$

So 

$$\mathrm{X}=\mathrm{A}^{-1}\mathrm{B}=-\frac{1}{17}\begin{bmatrix}-1&-5&-1\\-8&-6&9\\-10&1&7\end{bmatrix}\begin{bmatrix}8\\1\\4\end{bmatrix}$$

i.e.

$$\left[\begin{aligned}x\\ y\\ z\end{aligned}\right]=-\frac{1}{17}\left[\begin{aligned}-17\\ -34\\ -51\end{aligned}\right]=\left[\begin{aligned}1\\ 2\\ 3\end{aligned}\right]$$

Hence 

$$x=1,y=2and z=3.$$

Example18 The sum ofthree numbers is6.If we multiply third number by3 and add second number to it, we et 11.By adding first and third numbers, we et double ofthe second number. Represent it algebraically andfind the numbers using matrix metod.Solution Letfirs,second and thirdnumbers be denoted by , and z,respectively.Then, according to given conditions, we have 

$$\begin{aligned}x+y+z&=6\\y+3z&=11\\x+z&=2y or x-2y+z=0\end{aligned}, where $$

This system can be written as A $X=B$ , where 

$$\mathrm{A}=\begin{bmatrix}1&1&1\\0&1&3\\1&2&1\end{bmatrix},\mathrm{X}=\begin{bmatrix}x\\y\\z\end{bmatrix}\text{and}\mathrm{B}=\begin{bmatrix}6\\11\\0\end{bmatrix}$$

Here $\left|\mathrm{A}\right|=1\left(1+6\right)-\left(0-3\right)+\left(0-1\right)=9\neq0$ . Now we find adj A 

Hence 

$$\begin{array}{l}\mathrm{A}_{11}=1\text{(1+6)}=7,\\\mathrm{A}_{22}=\text{(1+2)}=-3,\\\mathrm{A}_{31}=\text{(3-1)}=2,\\a d j\mathrm{~A}=\left[\begin{array}{ccc}7&-3&2\\-1&3&-3\\-1&3&1\end{array}\right]\end{array}\begin{array}{l}\mathrm{A}_{13}=-1\\\mathrm{A}_{23}=-\text{(-2-1)}=3,\\\mathrm{A}_{33}=\text{(1-0)}=1\\\end{array}$$

Thus 

$$\mathrm{A}^{-1}=\frac{1}{\left|\mathrm{A}\right|}\text{adj}(\mathrm{A})=\frac{1}{9}\left[\begin{matrix}7&-3&2\\ 3&0&-3\\ -1&3&1\end{matrix}\right]$$

Since 

$$\mathrm{X}=\mathrm{A}^{-1}\mathrm{B}$$

$$\mathrm{X}=\frac{1}{9}\left[\begin{aligned}7\quad-3\quad2\\ 3\quad0\quad-3\\ -1\quad3\quad1\end{aligned}\right]\left[\begin{aligned}6\\ 11\\ 0\end{aligned}\right]$$

or 

Thus 

$$\begin{bmatrix}x\\ y\\ z\end{bmatrix}=\frac{1}{9}\begin{bmatrix}42-33+0\\ 18+0+0\\ -6+33+0\end{bmatrix}=\frac{1}{9}\begin{bmatrix}9\\ 18\\ 27\end{bmatrix}=\begin{bmatrix}1\\ 2\\ 3\end{bmatrix} x=1,y=2,z=3 \begin{bmatrix}x\\ y\\ z\end{bmatrix}=\frac{1}{9}\begin{bmatrix}42-33+0\\ 18+0+0\\ -6+33+0\end{bmatrix}=\frac{1}{9}\begin{bmatrix}9\\ 18\\ 27\end{bmatrix}=\begin{bmatrix}1\\ 2\\ 3\end{bmatrix} IS,$$

$$x=1,y=2,z=3$$

### EXERCISE 4.5

Examine the consistency of the system of equations in Exercises 1 to 6.

$$\begin{aligned}&1.\quad x+2y=2\quad2.\quad2x-y=5\quad3\quad x+3y=5\\&2x+3y=3\quad x+y=4\quad2x+6y=8\\&4.\quad x+y+z=1\quad5.\quad3x-y-2z=2\quad6.\quad5x-y+4z=5\\&2x+3y+2z=2\quad2y-z=-1\quad2x+3y+5z=2\\&\quad ax+ay+2az=4\quad3x-5y=3\quad5x-2y+6z=-1\end{aligned}$$

Solve systemof lir quations,uing matrix mthod, i Exercies 7 .

$$\begin{aligned}&7.5x+2y=4\quad&8.2x-y=-2\quad&9.4x-3y=3\\&7x+3y=5\quad&3x+4y=3\quad&3x-5y=7\\&0.5x+2y=3\quad&11.2x+y+z=1\quad&12.x-y+z=4\\&3x+2y=5\quad&x-2y-z=\frac{3}{2}\quad&2x+y-3z=0\\&3y-5z=9\quad&x+y+z=2\end{aligned}$$

13.

$$\begin{array}{l}2x+3y+3z=5\quad14.\quad x-y+2z=7\\x-2y+z=-4\quad3x+4y-5z=-5\\3x-y-2z=3\quad2x-y+3z=12\end{array}$$

15. If $A=\left[\begin{aligned}2\quad-3\quad5\\ 3\quad2\quad-4\\ 1\quad1\quad-2\end{aligned}\right]$ , find $\mathrm{A}^{-1}$ . Using $\mathrm{A}^{-1}$ solve the sysmof equations 

$$\begin{aligned}2x-3y+5z&=11\\3x+2y-4z&=-5\\x+y-2z&=-3\end{aligned}$$

16.Thecost of4kg onion,3kg wheat and2kg rice is60.Thecost of2kgonion,4kg wheat and6kg rice is90.Thecost of6 kg onion 2 kg wheat and 3 kg rice is₹ 70. Find cost of each item per kg by matrix method.

## Miscellaneous Examples 

$$\begin{aligned}&\text{Example19Use product}\begin{bmatrix}1&1&2\\0&2&3\\3&2&4\end{bmatrix}\begin{bmatrix}2&0&1\\9&2&3\\6&1&2\end{bmatrix}\text{to solve the system of equations}\\&\quad x-y+z=1\\&\quad2y-3z=1\\&\quad3x-2y+4z=2\\&\quad\text{Solution Consider the product}\begin{bmatrix}1&-1&2\\0&2&-3\\3&2&4\end{bmatrix}\begin{bmatrix}-2&0&1\\9&2&-3\\6&1&-2\end{bmatrix}\\&=\begin{bmatrix}-2-9+12&0-2+2&1+3-4\\0+18-18&0+4-3&0-6+6\\-6-18+24&0-4+4&3+6-8\end{bmatrix}=\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}\\&\text{Hence}\begin{bmatrix}1&-1&2\\0&2&-3\\3&-2&4\end{bmatrix}^{\circ}=\begin{bmatrix}-2&0&1\\9&2&-3\\6&1&-2\end{bmatrix}\end{aligned}$$

Now, given system of equations can be writen, in matrix form, as follows 

$$\begin{bmatrix}1&-1&2\\ 0&2&-3\\ 3&-2&4\end{bmatrix}\begin{bmatrix}x\\ y\\ z\end{bmatrix}=\begin{bmatrix}1\\ 1\\ 2\end{bmatrix}$$

or 

Hence 

$$\begin{aligned}x&=\left[\begin{matrix}1&-1&2\\ 0&2&-3\\ 3&-2&4\end{matrix}\right]^{-1}\left[\begin{matrix}1\\ 1\\ 2\end{matrix}\right]=\left[\begin{matrix}2&0&1\\ 9&2&3\\ 6&1&2\end{matrix}\right]\left[\begin{matrix}1\\ 1\\ 2\end{matrix}\right]\\&=\left[\begin{matrix}-2+0+2\\ 9+2-6\\ 6+1-4\end{matrix}\right]=\left[\begin{matrix}0\\ 5\\ 3\end{matrix}\right]\\x&=0,y=5and z=3\end{aligned}ea $$

Miscellaneous Exercises on Chapter 4

*[Formula could not be recovered from OCR — see source PDF]* Using properties of determinants in Exercises 11 to 15, prove that:

7. Solve the system of equations 

$$\begin{aligned}&\left\{\begin{aligned}\frac{2}{x}+\frac{3}{y}+\frac{10}{z}=4\end{aligned}\right.\\ &\left\{\begin{aligned}\frac{4}{x}-\frac{6}{y}+\frac{5}{z}=&1\end{aligned}\right.\\ &\left\{\begin{aligned}\frac{6}{x}+\frac{9}{y}-\frac{20}{z}=&2\end{aligned}\right.\\ \end{aligned}$$

Choose the correct answer in Exercise 17 to 19.

hed 8.If $x,y,z\mathrm{are}\mathrm{non}\mathrm{Zero}$ real numbers, then the inverse of matrix $\mathrm{A}=\begin{bmatrix}x&0&0\\ 0&y&0\\ 0&0&z\end{bmatrix}\mathrm{is}$ 

(A)

$$\begin{aligned}\left[\begin{matrix}x^{-1}&0&0\\0&y^{-1}&0\\0&0&z^{-1}\end{matrix}\right]\end{aligned}\quad(B)\quad xyz\begin{bmatrix}x^{-1}&0&0\\0&y^{-1}&0\\0&0&z^{-1}\end{bmatrix}(C)
$$

(C)

(C)$\frac{1}{xyz}\begin{bmatrix}x&0&0\\0&y&0\\0&0&z\end{bmatrix}$ 6(D)$\frac{1}{xyz}\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}$ 9.Let $\mathrm{A}=\left[\begin{array}{ccc}1&\sin\theta&1\\-\sin\theta&1&\sin\theta\\-1&-\sin\theta&1\end{array}\right]$ [Tabl , where $0\leq\theta\leq2\pi$ .Then _



(A)$\mathrm{Det}(\mathrm{A})=0$ (B)$\mathrm{Det}\left(\mathrm{A}\right)\in\left(2,\infty\right)$ (C)$\mathrm{Det}(\mathrm{A})\in(2,4)$ (D)$\mathrm{Det}\left(\mathrm{A}\right)\in[2,4]$ 

## Summary 

Determinant of a matrix $\mathrm{A}=\left[a_{11}\right]_{1\times1}$ is given by $|a_{11}|=a_{1}$ 

Determinant of a matrix $\mathbf{A}=\left[\begin{matrix}{a_{11}}&{a_{12}}\\ {a_{21}}&{a_{22}}\end{matrix}\right]$ is given by 

$$\left|\mathbf{A}\right|=\left|\begin{matrix}a_{11}&a_{12}\\ a_{21}&a_{22}\end{matrix}\right|=a_{11}a_{22}-a_{12}a_{21}$$

■Determinant of a matrix $\mathbf{A}=\left[\begin{aligned}{a_{1}\quad b_{1}\quad c_{1}}\\ {a_{2}\quad b_{2}\quad c_{2}}\\ {a_{3}\quad b_{3}\quad c_{3}}\end{aligned}\right].$ 



$$\left|\mathbf{A}\right|=\left|\begin{matrix}a_{1}&b_{1}&c_{1}\\ a_{2}&b_{2}&c_{2}\\ a_{3}&b_{3}&c_{3}\end{matrix}\right|=a_{1}\left|\begin{matrix}b_{2}&c_{2}\\ b_{3}&c_{3}\end{matrix}\right|-b_{1}\left|\begin{matrix}a_{2}&c_{2}\\ a_{3}&c_{3}\end{matrix}\right|+c_{1}\left|\begin{matrix}a_{2}&b_{2}\\ a_{3}&b_{3}\end{matrix}\right|$$

For any square matrix A, the |A| satisfy following properties.

■Area of a triangle with vertices $(x_{1},y_{1}),(x_{2},y_{2})$ and $(x_{3},y_{3})$ is given by 

<div style="text-align: center;"><img src="imgs/img_in_image_box_240_802_315_869.jpg" alt="Image" width="8%" /></div>


$$\Delta=\frac{1}{2}\left|\begin{matrix}x_{1}&y_{1}&1\\ x_{2}&y_{2}&1\\ x_{3}&y_{3}&1\end{matrix}\right|$$

■Minor of an element $a_{ij}$ of the determinant of matrix A is the determinant obtained by deleting $i^{\mathrm{th}}$ row and $j^{th}$ column and denoted by $\mathbf{M}_{ij}$ 

■Cofactor of $a_{ij}$ of given by $\mathbf{A}_{ij}=(-1)^{i+j}\mathbf{M}_{ij}$ 

■Value of determinant of a matrix Ais obtained by sum of product of elements of a row (or a column) with corresponding cofactors. For example,

$$\left|\mathbf{A}\right|=a_{11}\mathbf{A}_{11}+a_{12}\mathbf{A}_{12}+a_{13}\mathbf{A}_{13}.$$

7If elements of one row (or column) are multiplied with cofactors of elements of any other row (or column), then their sum is zero. For example,$a_{11}A_{21}+a_{12}$ 

$A_{22}+a_{13}A_{23}=0$ 



If $\mathbf{A}={\left[\begin{aligned}{a_{11}\quad a_{12}\quad a_{13}}\\ {a_{21}\quad a_{22}\quad a_{23}}\\ {a_{31}\quad a_{32}\quad a_{33}}\end{aligned}\right]},$ then adj $\mathbf{A}=\left[\begin{aligned}{\mathbf{A}_{11}\quad\mathbf{A}_{21}\quad\mathbf{A}_{31}}\\ {\mathbf{A}_{12}\quad\mathbf{A}_{22}\quad\mathbf{A}_{32}}\\ {\mathbf{A}_{13}\quad\mathbf{A}_{23}\quad\mathbf{A}_{33}}\end{aligned}\right]$ ,where $\mathrm{A}_{ij}$ $\mathrm{A}_{ij}$ is cofactor of cofactor of $a_{ij}$ 



■$\mathrm{A}(a d j\mathrm{A})=(a d j\mathrm{A})\mathrm{A}=|\mathrm{A}|\mathrm{I}$ where A is square matrix of order n.

■A square matrix A is said to be singular or non-singular according as 

$|\mathrm{A}|=0\mathrm{or}|\mathrm{A}|\neq0$ 



■If $\mathrm{fAB=BA=I}$ , where B is square matrix, then B is called inverse of A.Also $\mathbf{A}^{-1}=\mathbf{B}or\mathbf{B}^{-1}=\mathbf{A}$ and hence $(\mathbf{A}^{-1})^{-1}=\mathbf{A}$ 



■A square matrix A has inverse if and only ifA is non-singular.

$$\mathrm{A}^{-1}=\frac{1}{\left|\mathrm{A}\right|}\left(a d j\mathrm{A}\right)$$

$$\begin{array}{l}a_{1}x+b_{1}y+c_{1}z=d_{1}\\a_{2}x+b_{2}y+c_{2}z=d_{2}\\a_{3}x+b_{3}y+c_{3}z=d_{3}\\\end{array}$$

then theseequationcabritns 人$AX=B$ ,

$$\mathrm{A}=\begin{bmatrix}a_{1}&b_{1}&c_{1}\\ a_{2}&b_{2}&c_{2}\\ a_{3}&b_{3}&c_{3}\end{bmatrix},\mathrm{X}=\begin{bmatrix}x\\ y\\ z\end{bmatrix}\text{and}\mathrm{B}=\begin{bmatrix}d_{1}\\ d_{2}\\ d_{3}\end{bmatrix}$$

Unique solution of equation $AX=B$ is given by $X=A^{-1}B$ , where $\left|\mathbf{A}\right|\neq0$ 

A systemof equation isconsistent or inconsistent according as its solution exists or not.



■For a square matrix A in matrix equation $\mathrm{AX}=\mathrm{B}$ 

(i)$|\mathbf{A}|\neq0.$ , there exists unique solution 

(ii)$|A|=0$ and $(a d j\mathrm{A})\mathrm{B}\neq0$ then there exists no solution 

(ii)$|A|=0$ and $(adj\mathrm{A})\mathrm{B}=0$ , then system may or may not be consistent.

## Historical Note 

several linear equations by discovery of simple method of elimination.that of the numri idea of The subtracting Chinese method in adeterminant.columns of representing using rods and rows The on a as Chinese,. The arrangement of rods was precisely calculating board naturaly ed to the the in coefficients of the unknowns of simplification ee of a evelope determinant Mikami,China, pp 30,93.

Seki Kowa,the greatest of the Japanese Mathematicians of seventeenth century i in his work Kai Fukudai ino Ho'in 1683showed I that he had the idea of determinants and of their expansion..But he used this device onlyi in eliminating a quantity from two equations and not directly in the：solution ofaset tofsimultaneous linear equations.T.Hayashi,“The Fakudoi and Determinants in Japanese Mathematics,in the proc.of the Tokyo Math.Soc.,V.

Vendermonde was the first to recognise determinants asindepedent unctions.He may be called the formal founder.Laplace (1772),gavegeneral r method of expanding adetermnnt in erms ofits complemearymios.I7ane treated determinants of the second and third orders and used them for rpurpose other than the solution of equations. In 1801,Gauss used determinants in his theory of numbers.



The next greatcotributor was JacquesPhilippe- Marieint,82)who stated the theorem relating to the product of twomatrices of m-columns and nrows, which for the special case of $m=n$ reduces to themultiplication theorem.

Also on the same day,Cauchy (1812) presented one onthe same subject. He use theorem more satisfactory than Binet's.



The greatest contributor to the theory was Carl Gustav Jacob Jacobi, after this the word determinant received its final acceptance.

