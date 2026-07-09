

<div style="text-align: center;"><img src="imgs/img_in_image_box_514_8_657_163.jpg" alt="Image" width="15%" /></div>


# MATRICES 

出The essence of Mathematics lies in its freedom.— CANTOR 出

### 3.1 Introduction 

The knowledge of matrices is necessary in various branches of mathematics. Matrices are one of the most powerful tools in mathematics. This mathematical tool simplifies our work to a great extent when compared with other straight forward methods. The evolution of concept of matrices is the result of an attempt to obtain compact and simple methods of solvin system of linearquations.Matices arenot only used as a representiooeeficitinytmo iaruaioutulityof matrices far exceedstuMaixtationdperationreudiltnicpradsheet programs for personal computer, which in turn is used in different areas of business an experiment etc. Also, many physical operations such as magnification, rotation and reflection through a plane can be represented mathematically by matrices. Matrices are also udinygahy.Timmilliotludnbachs of scieng gl management.



In this chapter, we shall find it interesting to become acquainted with the fundamentals of matrix and matrix algebra.



### 3.2 Matrix 

Suppose we wish to express the information that Radha has 15 notebooks. We may express it as [15] with the understanding that the number inside [] is the number of notebooks that Radha has. Now, if we have to express that Radha has 15 notebooks and 6 pens. We may express it as [15 6] with the understanding that first number inside [] is the number of notebooks while the other one is the number of pens possessed by Radha. Let us now suppose that we wish to express the information of possession 

of notebooks and pens by Radha and her two friends Fauzia and Simran which is as follows:

Radha has 15notebooks and 6 pens,Fauzia has 10notebooks and 2 pens,Simran has 13notebooks and 5 pens.Now this could be aranged in the tabular form as follows:


<div style="text-align: center;"><html><body><table border="1"><tr><td></td><td>Notebooks</td><td>Pens</td></tr><tr><td>Radha</td><td>15</td><td>6</td></tr><tr><td>Fauzia</td><td>10</td><td>2</td></tr><tr><td>Simran</td><td>13</td><td>5</td></tr></table></body></html></div>


and this can be expressed as 

<div style="text-align: center;"><img src="imgs/img_in_image_box_285_518_681_774.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_94_795_733_924.jpg" alt="Image" width="68%" /></div>


which can be expressed as:

<div style="text-align: center;"><img src="imgs/img_in_image_box_146_983_731_1170.jpg" alt="Image" width="62%" /></div>


In the first arangement the entries in the first column represent the number of notebooks ossed by Radha,Fauzia nd imran, epectivly and te ntris in t second column represent the number of pens possessed by Radha, Fauzia and Simran, respectively.imilarly in the econd aranement the ntries in the first row represent the number of notebooks possessed by Radha, Fauzia and Simran, respectively. The entries in the second row represent the number of pens possessed by Radha, Fauzia and Simran, respectively. An arrangement or display of the above kind is called a matrix. Formally, we define matrix as:

Definition 1 A matrix is an ordered rectangular array of numbers or functions. The numbers or functions are called the elements or the entries of the matrix.

We denote matrices by capital leters. The following are some examples of matrices:

$$\left[\mathrm{A}=\left[\begin{matrix}-2&5\\ 0&\sqrt{5}\\ 3&6\end{matrix}\right]\right],\mathrm{B}=\left[\begin{matrix}2+i&3&-\dfrac{1}{2}\\ 3.5&-1&2\\ \sqrt{3}&5&\dfrac{5}{7}\end{matrix}\right],\mathrm{C}=\left[\begin{matrix}1+x&x^{3}&3\\ \cos x&\sin x+2&\tan x\end{matrix}\right] o $$

In the above examples, the horizontal lines of lements are said to constitute, rows of the matrix and the vertical lines of elements are said toconstitute, columns of the matrix. Thus Ahas 3 rows and2columns,Bhas 3 rows and3columns whileChas 2rows and 3 columns.



#### 3.2.1 Order of a matrix 

Amatrix having m rows and n columns is called a matrix of order $m\times n$ or simply $m\times n$ matrix (read as an m by n matrix). So referring to the above examples of matrices, we have A as $3\times2matrix,Bas3\times3$ matrixan $\mathrm{C}$ as $2\times3$ matrix. We observe that A has $3\times2=6$ elements, B and C have 9 and 6 elements, respectively.

In general, an $m\times n$ matrix has the following rectangular array:

$$not t \begin{bmatrix}\underline{a}_{11}&a_{12}&a_{13}\cdots a_{1j}\cdots a_{1n}\\ \underline{a}_{21}&a_{22}&a_{23}\cdots a_{2j}\cdots a_{2n}\\ \vdots&\vdots&\vdots\\ \underline{a}_{i1}&\vdots&\vdots\\ \vdots&\vdots&\vdots\\ \underline{a}_{m1}&\vdots&\vdots\\ \end{bmatrix}_{m\times n}\mathrm{or}\quad\mathrm{A}=[a_{ij}]_{m\times n},\quad1\leq i\leq m,\quad1\leq j\leq n\quad i,j\in\mathrm{N} notf \mathrm{or}\quad\mathrm{A}=[a_{ij}]_{m\times n},\quad1\leq i\leq m,\quad1\leq j\leq n\quad i,j\in\mathrm{N}$$

Thus the $i^{\mathrm{th}}$ row consists of the elements $a_{i1},a_{i2},a_{i3},...,a_{in},$ , while the $j^{\mathrm{th}}$ column consists of the elements $a_{1j},a_{2j},a_{3j}...,a_{mj}$ 



In general $a_{ij^{+}}$ is an element lying in the $i^{\mathrm{th}}$ row and $j^{\mathrm{th}}$ column. We can also call it as the $(i,j)^{\mathrm{th}}$ element of A. The number of elements in an $m\times n$ matrix will be equal to mn.



## Note In this chapter 

1.We shall follow the notation, namely $A=\left[a_{ij}\right]_{m\times n}$ to indicate that A is a matrix of order $m\times n$ 



2.We shall consider only those matrices whose elements are real numbers or functions taking real values.



We can also represent any point $(x,y)$ in a plane by a matrix (column or row) as 

$\begin{bmatrix}x\\ y\end{bmatrix}\left(or\left[x,y\right]\right)$ .For example point $\mathbb{P}(0,1)$ as a matrix representation may be given as 

$$\mathbb{P}=\begin{bmatrix}0\\ 1\end{bmatrix}or[01].$$

Observe that in this way we can also express the verticesof aclosed rectilinear fiureine.  ices A (1, 0), B (3, 2), C (1, 3), D (−1, 2).



Now, quadrilateral ABCD in the matrix form, can be represented as 

$$\mathrm{X}=\begin{bmatrix}1&3&1&-1\\0&2&3&2\end{bmatrix}_{2\times4}\mathrm{~or~}\mathrm{Y}=\begin{bmatrix}1&0\\3&2\\1&3\\-1&2\end{bmatrix}_{4\times2}$$

Thus, matrices can be used as representation of vertices of geometrical figures in a plane.



Now, let us consider some examples.

Example 1 Consider the following information regarding the number of men and women workers in three factories I, II and III 




<div style="text-align: center;"><html><body><table border="1"><tr><td></td><td>Men workers</td><td>Women workers</td></tr><tr><td>I</td><td>30</td><td>25</td></tr><tr><td>II</td><td>25</td><td>31</td></tr><tr><td>III</td><td>27</td><td>26</td></tr></table></body></html></div>


Represent the above information in the form of a $3\times2$ matrix. What does the entry in the third row and second column represent?



Solution The information is represented in the form of a.$3\times2$ matrix as follows:

$$\mathrm{A}=\begin{bmatrix}30&25\\25&31\\27&26\end{bmatrix}$$

The entry in the third row and second column represents the number of women workers in factory III.



Example 2 If a matrix has 8 elements, what are the possible orders it can have?

Solution We know that if a matrix is of order $m\times n$ , it has mn elements. Thus, to find all posible orders of a matrix with 8 elements, we will find all ordered pairs of natural numbers, whose product is 8.

(cid:1)

Hence, possible orders are $1\times8,8\times1,4\times2,2\times4$ 

Example 3 Construct a $3\times2$ matrix whose elements are given by cYaea $a_{ij}=\frac{1}{2}\left|i-3j\right|$ 

Solution In general a $3\times2$ matrix is given by $\mathbf{A}=\begin{bmatrix}a_{11}&a_{12}\\ a_{21}&a_{22}\\ a_{31}&a_{32}\end{bmatrix}$ 

Now 

$$a_{ij}=\frac{1}{2}\left|i-3j\right|,i=1,2,3and j=1,2.$$

Therefore 

$$a_{11}=\frac{1}{2}\left|1-3\times1\right|=1\quad a_{12}=\frac{1}{2}\left|1-3\times2\right|=\frac{5}{2}a_{21}=\frac{1}{2}\left|2-3\times1\right|=\frac{1}{2}\quad a_{22}=\frac{1}{2}\left|2-3\times2\right|=2a_{31}=\frac{1}{2}\left|3-3\times1\right|=0\quad a_{32}=\frac{1}{2}\left|3-3\times2\right|=\frac{3}{2}$$

Hence the required matrix is given by $\left[\mathrm{A}=\begin{bmatrix}1&\dfrac{5}{2}\\ \dfrac{1}{2}&2\\ 0&\dfrac{3}{2}\end{bmatrix}\right]$ 

### 3.3 Types of Matrices 

In this section, we shall discuss different types of matrices.

## (i) Column matrix 

A matrix is said to be a column matrix if it has only one column.

For example,$\mathbf{A}=\begin{bmatrix}0\\ \sqrt{3}\\ -1\\ 1/2\end{bmatrix}$ is a column matrix of order $4\times1$ 

In general,司$A=\left[a_{ij}\right]_{m\times1}$ is a column matrix of order $m\times1$ 

## (i) Row matrix 

A matrix is said to be a row matrix if it has only oe row 

For example,$\left[-\frac{1}{2}\sqrt{5}23\right]_{1\times4}$ is a row matrix.

In general,$\mathrm{B}=\left[b_{ij}\right]_{1\times n}$ is a row matrix of ord $1\times n$ 

## (i) Square matrix 

A matrix in which the number of rows are equal to the number of columns, is said to be a square matrix. Thus an $m\times n$ matrix is said to be a square matrix if $m=n$ and is known as a square matrix of order $ ``n''$ 



For example $\mathrm{A}=\begin{bmatrix}3&-1&0\\ \frac{3}{2}&3\sqrt{2}&1\\ 4&3&-1\end{bmatrix}$ is a square matrix of order 3.

In general,$\mathrm{A}=[a_{ij}]_{m\times m}$ is a square matrix of order m.

$\mathrm{Note}\;\mathrm{If}\;\mathrm{A}=[a_{ij}]$ is a square matrix of order , then elements (entries)$a_{11},a_{22},...,a_{nn}$ are said to constitute the diagonal, of the matrix A. Thus, if $\mathrm{A}=\begin{bmatrix}1&-3&1\\ 2&4&-1\\ 3&5&6\end{bmatrix}$ Then the elements of the diagonal of A are 1, 4, 6.



## (iv) Diagonal matrix 

A square matrix $\mathrm{B}=\left[b_{ij}\right]_{m\times m}$ is said to be a diagonal matrix if all its non diagonal elements are zero, that is a matrix $\mathrm{B}=[b_{ij}]_{m\times m}$ is said to be a diagonal matrix if $b_{ij}=0$ ,when $i\ne j$ 



For example,$\mathrm{A}=[4],\mathrm{B}=\begin{bmatrix}-1&0\\0&2\end{bmatrix},\mathrm{C}=\begin{bmatrix}-1.1&0&0\\0&2&0\\0&0&3\end{bmatrix}$ , are diagonal matrices 一

of order 1, 2, 3, respectively.

## (v) Scalar matrix 

A diagonal matrix is said to be a scalar matrix if its diagonal elements are equal,that is, a square matrix $\mathrm{B}=\left[b_{ij}\right]_{n\times n}$ is said to be a scalar matrix 

$$\begin{array}{l}b_{ij}=0,\quad when i\neq j\\b_{ij}=k,\quad when i=j,for some constant k.\end{array}$$

For example 

$$A=[3],\mathrm{B}=\begin{bmatrix}-1&0\\ 0&-1\end{bmatrix},\quad\mathrm{C}=\begin{bmatrix}\sqrt{3}&0&0\\ 0&\sqrt{3}&0\\ 0&0&\sqrt{3}\end{bmatrix}$$

are scalar matrices of order 1, 2 and 3, respectively.

## (vi) Identity matrix 

A square matrix in which elements in the diagonal are all 1 and rest are all zero is called an identity matrix. In other words, the square matrix $A=\left[a_{ij}\right]_{n\times n}$ is an identity matrix, if $a_{ij}=\left\{\begin{aligned}1\quad if\quad i=j\\ 0\quad if\quad i\neq j\end{aligned}\right.}$ 

We denote the identity matrix of order n by $ I_{n}$ . When order is clear from the context, we simply write it as I.



For example [1],$\begin{bmatrix}\begin{bmatrix}1&0\\ 0&1\end{bmatrix},\begin{bmatrix}1&0&0\\ 0&1&0\\ 0&0&1\end{bmatrix}\end{bmatrix}$ are identity matrices of order 1, 2 and 3,

respectively.

Observe that a scalar matrix is an identity matrix when $k=1$ . But every identity matrix is clearly a scalar matrix.



## (vii) Zero matrix 

Amatrix is said to be zero matrix or null matrix if all its elements are zero.

For example, [0],$\begin{bmatrix}\begin{bmatrix}0&0\\ 0&0\end{bmatrix},\begin{bmatrix}0&0&0\\ 0&0&0\end{bmatrix}\end{bmatrix}$ , [0, 0] are all zero matrices. We denote zero matrix by O. Its order will be clear from the context.

#### 3.3.1 Equality of matrices 

Definition 2 Two matrices $A=[a_{ij}]$ and $\mathrm{B}=[b_{ij}]$ are said to be equal if (i) they are of the same order 



(i) each element of A is equal to the corresponding element of B, that is $a_{ij}=b_{ij}$ for all i and j.



 For example,$\begin{bmatrix}2&3\\ 0&1\end{bmatrix}\mathrm{and}\begin{bmatrix}2&3\\ 0&1\end{bmatrix}$are equal matrices but$\begin{bmatrix}3&2\\ 0&1\end{bmatrix}\mathrm{and}\begin{bmatrix}2&3\\ 0&1\end{bmatrix}$ are not equal matrices. Symbolically, if two matrices A and B are equal, we write $A=B$ 

$$\begin{aligned}\mathrm{If}\begin{bmatrix}x&y\\ z&a\\ b&c\end{bmatrix}=\begin{bmatrix}-1.5&0\\ 2&\sqrt{6}\\ 3&2\end{bmatrix},\mathrm{then}x=-1.5,y=0,z=2,a=\sqrt{6},b=3,c=2.\end{aligned}\mathrm{Example}4\mathrm{If}\begin{bmatrix}x+3&z+4&2y-7\\ -6&a-1&0\\ b-3&-21&0\end{bmatrix}=\begin{bmatrix}0&6&3y-2\\ -6&-3&2c+2\\ 2b+4&-21&0\end{bmatrix}$$

Find the values of a,$b,c,x,y and z.$ 

Solution As the givenmatrices are equal, therefore, their corresponding elements must be equal. Comparing the corresponding elements, we get 

$$\begin{aligned}x+3&=0,\quad&z+4&=6,\quad&2y-7&=3y-2\\a-1&=-3,\quad&0&=2c+2\quad&b-3&=2b+4,\end{aligned}$$

Simplifying, we get 

$$a=-2,b=-7,c=-1,x=-3,y=-5,z=2$$

Example5Findthe values of a b,$c,$ and from the following eqution:

$$\begin{bmatrix}2a+b&a-2b\\ 5c-d&4c+3d\end{bmatrix}=\begin{bmatrix}4&-3\\ 11&24\end{bmatrix}$$

Solution By equality of two matrices, equating the corresponding elements, we get 

$$\begin{aligned}2a+b&=4\quad&5c-d&=11\\a-2b&=-3\quad&4c+3d&=24\end{aligned}$$

Solving these equations, we get 

$$a=1,b=2,c=3and d=4$$

### EXERCISE 3.1

1.In the matrix $\mathbf{A}=\left[\begin{aligned}&2&5&19&-7\\ &35&-2&\frac{5}{2}&12\\ &\sqrt{3}&1&-5&17\end{aligned}\right]$ , write:

(i) The order of the matrix,(ii) The number of elements,hed 

(ii) Write the elements $a_{13},a_{21},a_{33},a_{24},a_{23}$ 

2.If a matrix has24 elements, whatare the possible orders it can have? What, if it has 13 elements?



3.If a matrix has 18 elements, what are the possible orders it can have? What, if it has 5 elements?



4. Construct a $2\times2matrix,A=[a_{ij}]$ , whose elements are given by:

$$a_{ij}=\frac{(i+j)^2}{2}\quad(ii)\quad a_{ij}=\frac{i}{j}\quad(iii)\quad a_{ij}=\frac{(i+2j)^2}{2}$$

5.Construct a $3\times4$ matrix, whose elements are given by:

$$a_{ij}=\frac{1}{2}\left|-3i+j\right|\quad(ii)\quad a_{ij}=2i-j $$

6. Find the values of x, y and z from the following equations:

$$\left(\mathrm{i}\right)\left[\begin{matrix}4&3\\ x&5\end{matrix}\right]=\left[\begin{matrix}y&z\\ 1&5\end{matrix}\right]\quad\left(\mathrm{ii}\right)\left[\begin{matrix}x+y&2\\ 5+z&xy\end{matrix}\right]=\left[\begin{matrix}6&2\\ 5&8\end{matrix}\right]\left(\mathrm{iii}\right)\quad\left[\begin{matrix}x+y+z\\ x+z\\ y+z\end{matrix}\right]=\left[\begin{matrix}9\\ 5\\ 7\end{matrix}\right]$$

7. Find the value of a, b, c and d from the equation:

$$\begin{bmatrix}a-b&2a+c\\ 2a-b&3c+d\end{bmatrix}=\begin{bmatrix}-1&5\\ 0&13\end{bmatrix}$$

8.$A=\left[a_{ij}\right]_{m\times n}$ is a square matrix, if 

(A)EM $m\leq n$ EM (B)−$m>n$ EM (C)−$m=n$ (D) None of these 

9

$\begin{bmatrix}3x+7&5\\ y+1&2-3x\end{bmatrix},\begin{bmatrix}0&y-2\\ 8&4\end{bmatrix}$ 



(A)$x=\frac{-1}{3},\quad y=7$ (B) Not possible to find 

(C)T $y=7,\quad x=\frac{-2}{3}$ T](D)

10.Theumboflibloforder $$ $3\times3$ with each entry 0 or l $$ 



(A)27(B)18(C)81(D)512

### 3.4 Operations on Matrices 

In matr 

#### 3.4.1 Addition of matrices 

Suppose Fatima has two factoriesat places A and B.Eachfactory produces sport shoes forboysandirlsithreediferentpicecatgorielablled1,and3.The quantities produced by each factory are represented as matrices given below:


<div style="text-align: center;"><html><body><table border="1"><tr><td rowspan="2">Boys</td><td colspan="4">Factory at A Girls</td></tr><tr><td>60</td><td></td><td>Factory at B Boys</td><td>Girls</td></tr><tr><td>1 2</td><td>80 75</td><td>2</td><td>90</td><td>50</td></tr><tr><td>3</td><td>90 85</td><td>3</td><td>70 75</td><td>55 75</td></tr></table></body></html></div>


Suppose Fatima wants to know the total production of sport shoes in each price category. Then the total production 



In category 1 : for boys $(80+90)$ ), for girls $(60+50)$ )

In category 2 : for boys $(75\pm70)$ ,for girls $(65+55)$ )

In category 3 :for boys $(90+75)$ ),for girls $(85\pm75)$ )

This can be represented in the matrix form as $\begin{bmatrix}80+90&&60+50\\ 75+70&&65+55\\ 90+75&&85+75\end{bmatrix}$ 

This new matrix is the sum of the above two matrices. We observe that the sum of two matrices is a matrix obtained by adding the corresponding elements of the given matrices. Furthermore, the two matrices have to be of the same order.

$$\mathrm{Thus},\mathrm{if}\mathrm{A}=\begin{bmatrix}a_{11}&a_{12}&a_{13}\\ a_{21}&a_{22}&a_{23}\end{bmatrix}\mathrm{is}\mathrm{a}2\times3\mathrm{matrix}\mathrm{matrix}\mathrm{a}\mathrm{B}=\begin{bmatrix}b_{11}&b_{12}&b_{13}\\ b_{21}&b_{22}&b_{23}\end{bmatrix}\mathrm{is}\mathrm{another}2\times3matrix.Then,we define A+B=\left[\begin{aligned}{a_{11}+b_{11}\quad a_{12}+b_{12}\quad a_{13}+b_{13}}\\ {a_{21}+b_{21}\quad a_{22}+b_{22}\quad a_{23}+b_{23}}\\ \end{aligned}\right].$$

In general, if $A=[a_{ij}]and B=[b_{ij}]$ are two matrices of the same order, say $m\times n$ Then, the sum of the two matrices A and B is defined as a matrix $\mathrm{C}=[c_{ij}]_{m\times n},$ where $c_{ij}=a_{ij}+b_{ij}$ , for all possible values of i and j.

_



$$ Example6Given A=\left[\begin{matrix}\sqrt{3}&1&-1\\ 2&3&0\end{matrix}\right]and B=\left[\begin{matrix}2&\sqrt{5}&1\\ -2&3&\frac{1}{2}\end{matrix}\right],find A+B $$

Since A, B are of the same order $2\times3$ . Therefore, addition of A and B is defined and is given by 



$$\left[\begin{aligned}&A+B=\left[\begin{aligned}2+\sqrt{3}&1+\sqrt{5}&1-1\\ 2-2&3+3&0+\frac{1}{2}\end{aligned}\right]=\left[\begin{aligned}2+\sqrt{3}&1+\sqrt{5}&0\\ 0&6&\frac{1}{2}\end{aligned}\right]\end{aligned}\right.]$$

## Note 

1. We emphasise that if A and B are not of the same order, then $\mathrm{A+B}$ is not defined. For example if $\left[\mathrm{A}=\begin{bmatrix}2&3\\ 1&0\end{bmatrix},\mathrm{B}=\begin{bmatrix}1&2&3\\ 1&0&1\end{bmatrix}\right]$ then $\mathrm{A}{\mathrm{+B}}$ is not defined.2.We may observe that addition of matrices is an example of binary operation on the set of matrices of the same order.



#### 3.4.2 Multiplicationof a matrix by a scalar 

Now suppose that Fatima has doubled the production at a factory A in all categories (refer to 3.4.1).



Previously quantities(in standard units) produced by factory A were 

$$\begin{array}{ccc}&Boys&\quad Girls\\&&\\12\left[\begin{array}{c}80\\75\\90\\end{array}\right.&&\left.\begin{array}{c}60\\65\\85\\end{array}\right]&\\end{array}$$

Revised quantities produced by factory A are as given below:

$$\begin{aligned}&\begin{bmatrix}\\ &\mathrm{Boys}&\mathrm{Girls}\\&1\begin{bmatrix}2\times80&2\times60\\ 2\times75&2\times65\end{bmatrix}\\&3\begin{bmatrix}2\times90&2\times85\end{bmatrix}\\ &\end{bmatrix}\\ \end{aligned}$$

shed This can be represented in the matrix rm as $\begin{bmatrix}160&120\\ 150&130\\ 180&170\end{bmatrix}$ .We observe that the new matrix is obtained by multiplying each element of the previous matrix by 2.

In general, we may define multiplication of a matrix by a scalar as follows: if $A=\left[a_{ij}\right]_{m\times n}$ is a matrix and k is a scalar, then kA is another matrix which is obtained by multiplying each element of A by the scalar k.



In other words,$k\mathrm{A}=k\left[a_{ij}\right]_{m\times n}=\left[k\left(a_{ij}\right)\right]_{m\times n},$ ,that is,$(i,j)^{\mathrm{th}}$ element of kA is $ka_{ij}$ for all possible values of i and j.



For example, if not $\mathrm{A}=\left[\begin{aligned}3&\quad1&\quad1.5\\ \sqrt{5}&\quad7&\quad-3\\ 2&\quad0&\quad5\end{aligned}\right]$ ,then 

$$not 3A=3\begin{bmatrix}3&1&1.5\\ \sqrt{5}&7&-3\\ 2&0&5\end{bmatrix}=\begin{bmatrix}9&3&4.5\\ 3\sqrt{5}&21&-9\\ 6&0&15\end{bmatrix}$$

Negativeof a matrix The negative of a matrix is denoted 1$\mathrm{b y-A}$ .Wedefine 

$-A=(-1)A$ 



For example, let 

$$\mathrm{A}=\begin{bmatrix}3&1\\ -5&x\end{bmatrix},\mathrm{then}-\mathrm{A}\mathrm{is given by}-A=(-1)A=(-1)\begin{bmatrix}3&1\\ -5&x\end{bmatrix}=\begin{bmatrix}-3&-1\\ 5&-x\end{bmatrix}$$

Difference of matrices If $A=[a_{ij}],B=[b_{ij}]$ are two matrices of the same order,$\mathtt{say}\;m\times n$ , then difference $\mathrm{A}-\mathrm{B}$ is defined as a matrix $\mathrm{D}=\left[d_{ij}\right]$ ,where $d_{ij}=a_{ij}-b_{ij}$ for all value of i andj. In other words,$\mathrm{D}=\mathrm{A}-\mathrm{B}=\mathrm{A}+(-1)\mathrm{B}$ ,that is sum of the matrix A and the $ matrix-B$ ama Example 7 If $\mathrm{A}=\left[\begin{aligned}1\quad2\quad3\\ 2\quad3\quad1\end{aligned}\right]\text{and}\mathrm{B}=\left[\begin{aligned}3-1\quad3\\ -1\quad0\quad2\end{aligned}\right]$ ,then find findd $$ 

Solution We have 

$$\begin{aligned}2\mathrm{A}-\mathrm{B}&=2\begin{bmatrix}1&2&3\\2&3&1\end{bmatrix}-\begin{bmatrix}3&-1&3\\-1&0&2\end{bmatrix}\\&=\begin{bmatrix}2&4&6\\4&6&2\end{bmatrix}+\begin{bmatrix}-3&1&-3\\1&0&-2\end{bmatrix}\\&=\begin{bmatrix}2-3&4+1&6-3\\4+1&6+0&2-2\end{bmatrix}=\begin{bmatrix}-1&5&3\\5&6&0\end{bmatrix}\end{aligned}$$

#### 3.4.3 Properties of matrix addition 

The addition of matrices satisfy the following properties:

(i) Commutative Law If $\mathrm{A}=[a_{ij}],\mathrm{B}=[b_{ij}]$ are matrices of the same order, say $m\times n.$ ,then $A+B=B+A$ 



Now 

$$\begin{aligned}\bar{A}+\bar{B}&=[a_{ij}]+[b_{ij}]=[a_{ij}+b_{ij}]\\&=[b_{ij}+a_{ij}](addition of numbers is commutative)\\&=([b_{ij}]+[a_{ij}])=\bar{B}+\bar{A}\end{aligned}$$

(i) Associative Law For any three matrices $A=[a_{ij}],B=[b_{ij}],C=[c_{ij}]$ of the same order, say $m\times n,(A+B)+C=A+(B+C)$ 



Now 

$$\begin{aligned}(A+B)+C&=([a_{ij}]+[b_{ij}])+[c_{ij}]\\&=[a_{ij}+b_{ij}]+[c_{ij}]=[(a_{ij}+b_{ij})+c_{ij}]\\&=[a_{ij}+(b_{ij}+c_{ij})]\quad(Why?)\\&=[a_{ij}]+[(b_{ij}+c_{ij})]=[a_{ij}]+([b_{ij}]+[c_{ij}])=A+(B+C)\end{aligned}$$

(i) Existence of additive identity Let $A=[a_{ij}]$ be an $m\times n$ matrix and Obe an $m\times n$ zero matrix, then $A+O=O+A^{2}=A$ . In other words, O is the additive identity for matrix addition.



(iv) The existence of additive inverse Let $A=\left[a_{ij}\right]_{m\times n}$ be any matrix, then we have another matrix a $s-A=\left[-a_{ij}\right]_{m\times n}$ such that $\widehat{A}+(-A)=(-A)+A=O$ .So –A is the additive inverse of A or negative of A.



#### 3.4.4 Propertiesof scalar multiplicationof a matrix 

$\mathrm{If}\;\mathrm{A}=[a_{ij}]\;\mathrm{and}\;\mathrm{B}=[b_{ij}]$ be two matrices of the same order, say $m\times n.$ , and k and l are scalars, then o 

(i)

(ii)

(im)

$$k(A+B)=kA+kB,\quad(ii)\quad(k+l)A=kA+lA o \begin{aligned}k\left(\mathrm{A}+\mathrm{B}\right)&=k\left(\left[a_{ij}\right]+\left[b_{ij}\right]\right)\\&=k\left[a_{ij}+b_{ij}\right]=\left[k\left(a_{ij}+b_{ij}\right)\right]=\left[\left(k\ a_{ij}\right)+\left(k\ b_{ij}\right)\right]\\&=\left[k\ a_{ij}\right]+\left[k\ b_{ij}\right]=k\left[a_{ij}\right]+k\left[b_{ij}\right]=k\mathrm{A}+k\mathrm{B}\\(k+l)\mathrm{A}&=(k+l)\left[a_{ij}\right]\\&=\left[(k+l)\ a_{ij}\right]+\left[k\ a_{ij}\right]+\left[l\ a_{ij}\right]=k\left[a_{ij}\right]+l\left[a_{ij}\right]=k\mathrm{A}+l\mathrm{A}\end{aligned}$$

Example8 If $\mathrm{A}=\left[\begin{aligned}&8&0\\ &4&-2\\ &3&6\end{aligned}\right]\text{and}\mathrm{B}=\left[\begin{aligned}&2&-2\\ &4&2\\ &-5&1\end{aligned}\right]$ then find the matrix X, such that 

$2A+3X=5B.$ 



Solution We have $2A+3X=5B$ 

or 

$$2A+3X-2A=5B-2A $$

or 

$$2A-2A+3X=5B-2A $$

or 

$$0+3X=5B-2A $$

or 

$$3X=5B-2A $$

or 

$$X=\frac{1}{3}(5B-2A)$$

(Matrix addition is commutative)(− 2A is the additive inverse of 2A)(O is the additive identity)

$$\left(\mathrm{X}=\frac{1}{3}\left(5\left[\begin{array}{cc}2&-2\\ 4&2\\ -5&1\end{array}\right]-2\left[\begin{array}{cc}8&0\\ 4&-2\\ 3&6\end{array}\right]\right)=\frac{1}{3}\left(\left[\begin{array}{cc}10&-10\\ 20&10\\ -25&5\end{array}\right]+\left[\begin{array}{cc}-16&0\\ -8&4\\ -6&-12\end{array}\right]\right)\right)\frac{1}{3}\left[\begin{matrix}10-16-10+0\\20-8&10+4\\-25-6&5-12\end{matrix}\right]=\frac{1}{3}\left[\begin{matrix}-6&-10\\12&14\\-31&-7\end{matrix}\right]=\left[\begin{matrix}-2&\frac{-10}{3}\\4&\frac{14}{3}\\frac{-31}{3}&\frac{-7}{3}\end{matrix}\right]$$

Example 9 Find X and Y, if $$ 

Solution We have $$ →

$$(X+X)+(Y-Y)=\begin{bmatrix}8&8\\ 0&8\end{bmatrix}\Rightarrow2X=\begin{bmatrix}8&8\\ 0&8\end{bmatrix}\mathrm{X}=\frac{1}{2}\begin{bmatrix}8&8\\ 0&8\end{bmatrix}=\begin{bmatrix}4&4\\ 0&4\end{bmatrix}$$

Also 

$$(X+Y)-(X-Y)=\begin{bmatrix}5&2\\ 0&9\end{bmatrix}-\begin{bmatrix}3&6\\ 0&-1\end{bmatrix}$$

or 

$$(X-X)+(Y+Y)=\begin{bmatrix}5-3&2-6\\ 0&9+1\end{bmatrix}\Rightarrow2Y=\begin{bmatrix}2&-4\\ 0&10\end{bmatrix}$$

or 

$$\mathrm{Y}=\frac{1}{2}\left[\begin{aligned}2&-4\\ 0&10\end{aligned}\right]=\left[\begin{aligned}1&-2\\ 0&5\end{aligned}\right]$$

Example10indthealueofandromtheollowinquation:nd 



$$2\begin{bmatrix}x&5\\ 7&y-3\end{bmatrix}+\begin{bmatrix}3&-4\\ 1&2\end{bmatrix}=\begin{bmatrix}7&6\\ 15&14\end{bmatrix}$$

Solution We have 

$$2\left[\begin{matrix}x&5\\7&y-3\end{matrix}\right]+\left[\begin{matrix}3&-4\\1&2\end{matrix}\right]=\left[\begin{matrix}7&6\\15&14\end{matrix}\right]\Rightarrow\left[\begin{matrix}2x&10\\14&2y-6\end{matrix}\right]+\left[\begin{matrix}3&-4\\1&2\end{matrix}\right]=\left[\begin{matrix}7&6\\15&14\end{matrix}\right]\begin{aligned}&for\quad&\begin{bmatrix}2x+3&10-4\\ 2x+1&2y-6+2\end{bmatrix}=\begin{bmatrix}7&6\\ 15&14\end{bmatrix}\Rightarrow\begin{bmatrix}2x+3&6\\ 15&2y-4\end{bmatrix}=\begin{bmatrix}7&6\\ 15&14\end{bmatrix}\\ &for\quad&2x+3=7\quad and\quad&2y-4=14\quad(Why?)\\ &for\quad&2x=7-3\quad and\quad&2y=18\\ &for\quad&x=\frac{4}{2}\quad and\quad&y=\frac{18}{2}\\ &i.e.\quad&x=2\quad and\quad&y=9.\\ \end{aligned}$$

Example11Twofarmers Ramkishanand Gurcharan Singhcultivatesonlythre varieties of rice namely Basmati, Permal and Naura. The sale (in Rupees) of these varieties of rice by both the farmers in the month of September and October are given by the following matrices A and B._siish 

$$\mathrm{A}=\left[\begin{array}{ccc}\text{Setup}&\text{Sales}(\text{in}\text{Rupes})&\\text{Basmati}&\text{Permal}&\text{Nara}\\10,000&20,000&30,000\\50,000&30,000&10,000\end{array}\right]\text{Rmkishan} siish O $$

October Sales (in Rupees)

$$O \mathrm{B}=\left[\begin{array}{ll}\text{Basmati}&\text{Permal}\quad\text{Naura}\\ 5000&10,000\quad6000\\ 20,000&10,000\quad10,000\end{array}\right]\text{Ramkishan}$$

(i)Find the combined sales in September and October for eachfarmer in each variety.



(ii)Find the decrease in sales from September to October.

(i)If both farmers receive 2%profit on gross sales, compute the profit for each farmer and for each variety sold in October.



## Solution 

(i) Combined sales in September and October for each farmer in each variety is given by 



$$\mathrm{A}+\mathrm{B}=\left[\begin{array}{ll}\text{Basmati}&\text{Permal}\quad\text{Naura}\\ 15,000&30,000\quad36,000\\ 70,000&40,000\quad20,000\end{array}\right]\text{Ramkishan}$$

(ii) Change in sales from September to October is given by 

(i)

$$(i)\begin{aligned}A-B=&\begin{bmatrix}Bassanii&Permal&Naura\\hline5000&10,000&24,000\\30,000&20,000&0\end{bmatrix}Ramkishan\\2\%of B=&\begin{bmatrix}\frac{2}{100}\times B=0.02\times B\\hline\end{bmatrix}\\=&\ 0.02\begin{bmatrix}Bassmi&Permal&Naura\\hline5000&10,000&6000\\hline20,000&10,000&10,000\end{bmatrix}Ramkishan\\&\begin{bmatrix}Bassmi&Permal&Naura\\hline\end{bmatrix}\\=&\begin{bmatrix}100&200&120\\hline400&200&200\\hline\end{bmatrix}Ramkishan\\end{aligned} ed $$

Thus, in October Ramkishan receives 100, 200 and 120 as profit in the sale of each variety of rice, respectively, and Grucharan Sinh receives profit of400,200 and 200 in the sale of each variety of rice, respectively.

#### 3.4.5 Multiplication of matrices 

Suppose Meera and Nadeem are two friends. Meera wants to buy 2 pens and 5 story books, while Nadeem needs 8 pens and 10 story books. They both go to a shop to enquire about the rates which are quoted as follows:

$$\mathrm{Pen}-\bar{\bar{x}}\;5\;\mathrm{each},\;\mathrm{story}\;\mathrm{book}-\bar{\bar{x}}\;50\;\mathrm{each}.$$

How much money does each need to spend? Clearly, Meera needs $(5\times2+50\times5)$ that is ₹ 260, while Nadeem needs $(8\times5+50\times10)$ ,that is540.In terms of matix representation, we can write the above information as follows:

Requirements Prices per piece (in Rupees) Money needed (in Rupees)

$$\left[\begin{aligned}2\quad5\\ 8\quad10\end{aligned}\right]$$

Suppose that they enquire about the rates from another shop, quoted as follows:

$\mathrm{pen}-\bar{\bar{x}}4\mathrm{each},\mathrm{story}\mathrm{book}-\bar{\bar{x}}40$ each.

Now, the money required by Meera and Nadeem to make purchases will be respectively $\bar{x}(4\times2+40\times5)=\bar{x}208and\bar{x}(8\times4+10\times40)=\bar{x}432$ 

doo 

RequiremetRupModues 

$$\begin{bmatrix}2&5\\ 8&10\end{bmatrix}\quad\begin{bmatrix}4\\ 40\end{bmatrix}\quad\begin{bmatrix}4\times2+40\times5\\ 8\times4+10\times40\end{bmatrix}=\begin{bmatrix}208\\ 432\end{bmatrix}$$

Now, the inormaioinbohaeabombid dxpdintrms of matrices as follows:

Requirements Prices per piece (in Rupees) Money needed (in Rupees)

-[810]$\begin{bmatrix}5&4\\ 50&40\end{bmatrix}\quad 緻 \quad\begin{bmatrix}5\times2+5\times50&4\times2+40\times5\\ 8\times5+10\times50&8\times4+10\times40\end{bmatrix}$ 

$$=\left[\begin{aligned}260\quad208\\ 540\quad432\end{aligned}\right]$$

The above is an example of multiplication of matrices.observe that, for multiplication of two matrices A and $\mathrm{B}_{i}$ the number of columns in A should be equal to thenumberofrowsin B.Futhermoreorintelemntsoftheproduct matrix,we take rows of A and columns of B,multiply them element-wise and take the sum.Formally, we define multiplication of matrices as follows:

The product oftwo matrices A and B is defined if the number of columns of A is equal to the number of rows of B. Let $A=[a_{ij}]$ be an $m\times n$ matrix and $\mathrm{B}=[b_{jk}]$ be an $n\times p$ matrix. Then the product of the matrices A and B is the matrix C of order $m\times p$ To get the $(i,k)^{\mathrm{th}}$ element $c_{ik}$ of the matrix C, we take the $i^{\mathrm{th}}$ row of A and $k^{\mathrm{th}}$ column of,uof.Ir rd if $\mathrm{A}=[a_{ij}]_{m\times n},\mathrm{B}=[b_{jk}]_{n\times p}$ ,then the $\bar{l}^{\mathrm{th}}$ row of A is $[a_{i1}a_{i2}\ldots a_{in}]$ and the $k^{\mathrm{th}}$ column of 

$$\mathrm{B}\mathrm{is}\begin{bmatrix}b_{1k}\\ b_{2k}\\ \vdots\\ b_{nk}\end{bmatrix},\text{then}c_{ik}=a_{i1}b_{1k}+a_{i2}b_{2k}+a_{i3}b_{3k}+\ldots+a_{in}b_{nk}=\sum_{j=1}^{n}a_{ij}b_{jk}$$

The matrix $\mathrm{C}=\left[c_{ik}\right]_{m\times p}$ is the product of A and B.

For example, if $\left[\mathrm{C}=\left[\begin{aligned}1\quad-1\quad2\\ 0\quad3\quad4\end{aligned}\right]\quad and\quad\mathrm{D}=\left[\begin{aligned}2\quad7\\ -1\quad1\\ 5\quad-4\end{aligned}\right]\right.]$ , then the product CD is defined 

and is given by $\mathrm{CD}=\left[\begin{aligned}1\quad-1\quad2\\ 0\quad3\quad4\end{aligned}\right]\left[\begin{aligned}2\quad7\\ -1\quad1\\ 5\quad-4\end{aligned}\right]$ . This is a $2\times2$ matrix in which each 

entry is the sum of the products across some row of C with the corresponding entries down some column of D. These four computations are 

$$\begin{array}{l}\text{Entry in}\\text{first row}\\text{first column}\end{array}\left[\begin{array}{cc}1&-1&2\\1&3&4\\0&3&4\end{array}\right]\left[\begin{array}{cc}2&7\\-1&1\\5&-4\end{array}\right]=\left[\begin{array}{cc}(1)(2)+(-1)(-1)+(2)(5)&?\\?&?\end{array}\right]o \begin{array}{l}\text{Entry in}\\text{first row}\\text{second column}\left[1-1+2\right]\left[-2+7\right]=\left[13\left(7\right)+\left(-1\right)(1)+2(-4)\right]\\text{second column}\left[0-3\right]=\left[-5-4\right]=-4\end{array}$$

Entry in second row first column $\left[\begin{array}{ccc}1&-1&2\\ &&\\ 0&3&4\end{array}\right]\left[\begin{array}{cc}2&7\\ -1&1\\ 5&-4\end{array}\right]=\left[\begin{array}{cc}13&-2\\ 0(2)+3(-1)+4(5)&?\end{array}\right]$ 

$$\begin{array}{l}\text{Entry in}\\text{second row}\\text{second column}\left[1-1\quad2\right]\left[\begin{array}{cc}2&7\\-1&1\\5&-4\end{array}\right]=\left[\begin{array}{cc}13&-2\\17&0(7)+3(1)+4(-4)\end{array}\right]\end{array}be Thus CD=\begin{bmatrix}13&-2\\ 17&-13\end{bmatrix}$$

be Example12 Find AB, if $\mathrm{A}=\begin{bmatrix}6&9\\ 2&3\end{bmatrix}\mathrm{and}\mathrm{B}=\begin{bmatrix}2&6&0\\ 7&9&8\end{bmatrix}.$ 

Solution The matrix A has 2 columns which is equal to the number of rows of B.Hence AB is defined. Now 



$$\begin{aligned}&\mathrm{AB}=\begin{bmatrix}6(2)+9(7)&6(6)+9(9)&6(0)+9(8)\\2(2)+3(7)&2(6)+3(9)&2(0)+3(8)\end{bmatrix}\\ &=\begin{bmatrix}12+63&36+81&0+72\\4+21&12+27&0+24\end{bmatrix}=\begin{bmatrix}75&117&72\\25&39&24\end{bmatrix}\\ \end{aligned}$$

Remark If AB is defined, then BA need not be defined. In the above example, AB is defined but BA is not defined because B has 3 column while A has only 2 (and not 3)rows. IfA, B are, respectively $m\times n,k\times l{\mathrm{matrices}}$ , then both AB and BA are defined if and only il $\mathrm{f}n=k\mathrm{and}l=m$ .In particular, if both A and B are square matrices of the same order, then both AB and BA are defined.



## Non-commutativity of multiplication of matrices 

Now, we shall see by an example that even if AB and BA are both defined, it is not necessary that $AB=BA$ 1



Example 13 If $\mathrm{A}=\left[\begin{aligned}1\quad-2\quad3\\ -4\quad2\quad5\end{aligned}\right]\text{and}\mathrm{B}=\left[\begin{aligned}2\quad3\\ 4\quad5\\ 2\quad1\end{aligned}\right]$ ,then find AB, BA. Show_that 

$$\mathrm{AB}\neq\mathrm{BA}.$$

Solution Since A is a $2\times3$ matrix and B is $3\times2\mathrm{matrix}$  Hence AB and BA are both defined and are matrices of order $2\times2$ and $3\times3$ respectively. Note that 

$$\left[\mathrm{AB}=\left[\begin{aligned}1-2&3\\ -4&2&5\end{aligned}\right]\right]=\left[\begin{aligned}2&3\\ 4&5\\ -8&+8&+10\end{aligned}\right]=\left[\begin{aligned}2&-8+6&3-10+3\\ -8&+8&+10&-12&+10+5\end{aligned}\right]=\left[\begin{aligned}0&-4\\ 10&3\end{aligned}\right]$$

and 

$$\mathrm{BA}=\begin{bmatrix}2&3\\4&5\\2&1\end{bmatrix}\begin{bmatrix}-2&3\\-4&2&5\end{bmatrix}=\begin{bmatrix}2-12&-4+6&6+15\\4-20&-8+10&12+25\\2-4&-4+2&6+5\end{bmatrix}=\begin{bmatrix}-10&2&21\\-16&2&37\\-2&-2&11\end{bmatrix}$$

Clearly $\mathrm{AB}\ne\mathrm{BA}$ 

In the above example both AB and BA are of different order and so $\mathrm{AB\ne BA}$ .But one may think that perhaps AB and BA could be the same if they were of the same order. But it is not so, here we give an example to show that even if AB and BA are of same order they may not be same.



$$\mathrm{Example}14\mathrm{If}\mathrm{A}=\left[\begin{aligned}1&\quad0\\ 0&\quad-1\end{aligned}\right]\mathrm{and}\mathrm{B}=\left[\begin{aligned}0&\quad1\\ 1&\quad0\end{aligned}\right],\mathrm{then}\mathrm{AB}=\left[\begin{aligned}0&\quad1\\ -1&\quad0\end{aligned}\right].$$

and 

$$ BA=\begin{bmatrix}0&-1\\ 1&0\end{bmatrix}.Clearly AB\neq BA.$$

Thus matrix multiplication is not commutative.

Note] This does not mean that $\mathrm{AB}\neq\mathrm{BA}$ for every pair of matrices A, B for which AB and BA, are defined. For instance,

$$\mathrm{A}=\begin{bmatrix}1&0\\ 0&2\end{bmatrix},\mathrm{B}=\begin{bmatrix}3&0\\ 0&4\end{bmatrix},\mathrm{then}\mathrm{AB}=\mathrm{BA}=\begin{bmatrix}3&0\\ 0&8\end{bmatrix}$$

Observetatutiliiooaoalrofameewillbommutative.

Zero matrix as the product of two non zero matrices 

We know that, for real numbers $a,b\mathrm{if}ab=0$ ,then either $a=0or b=0$ . This need not be true for matrices, we will observe this through an example.ished Example 15 Find AB, if $\mathrm{A}=\begin{bmatrix}0&-1\\0&2\end{bmatrix}\text{and}\mathrm{B}=\begin{bmatrix}3&5\\0&0\end{bmatrix}$ 

Solution We have $\mathrm{AB}=\begin{bmatrix}0&-1\\ 0&2\end{bmatrix}\begin{bmatrix}3&5\\ 0&0\end{bmatrix}=\begin{bmatrix}0&0\\ 0&0\end{bmatrix}.$ 

Thus,iftheuctofoioixistryhatoneof the matrices is a zero matrix.



#### 3.4.6 Properties of multiplication of matrices 

Theullfo proof.



1. The associative law For any three matrices A, B and C. We have 

(AB)$C=A(B C)$ , whenever both sides of the equality are defined.

2. The distributive law For three matrices A, B and C.

(i)$\mathrm{A}(\mathrm{B}+\mathrm{C})=\mathrm{AB}+\mathrm{AC}$ 

(ii)$(A+B)C=AC+BC$ , whenever both sides of equality are defined.

3. The existence of multiplicative identity For every square matrix A, there exist an identity matrix of same order such that $\mathrm{IA}=\mathrm{AI}=\mathrm{A}$ 

Now, we shall verify these properties by examples.

Example 16 If $\mathrm{A}=\left[\begin{aligned}1\quad1\quad-1\\ 2\quad0\quad3\\ 3\quad-1\quad2\end{aligned}\right],\mathrm{B}=\left[\begin{aligned}1\quad3\\ 0\quad2\\ -1\quad4\end{aligned}\right]\text{and}\mathrm{C}=\left[\begin{aligned}1\quad2\quad3\quad-4\\ 2\quad0\quad-2\quad1\end{aligned}\right]$ , find 

A(BC), (AB)C and show that $(AB)C=A(BC)$ 1.

$$\begin{aligned}&\text{Solution We have ABe}\mathrm{AB}=\begin{bmatrix}1&1&-1\\2&0&1\\1&0&1\\-1&1&0\end{bmatrix}\begin{bmatrix}1&2\\0&2\\1&0\\-1&4\end{bmatrix}=\begin{bmatrix}1+0+1&3+2-4\\0+1&0+1\\-1&0&2-9+2+8\end{bmatrix}=\begin{bmatrix}2&1\\-1&18\\-1&18\end{bmatrix}\\ &(\mathrm{AB})(\mathrm{C})=\begin{bmatrix}2&1\\-1&18\\1&18\end{bmatrix}\begin{bmatrix}1&2&3-4\\2&0&1\\1&0&2-1\end{bmatrix}=\begin{bmatrix}2+2&4+0&6-2&-8+1\\-1+36&-2+0&-3-36&4+18\\-1+30&2+0&3-30&-4+15\end{bmatrix}\\ &=\begin{bmatrix}4&4&4-7\\35&-2&-39&22\\31&2&-27&11\end{bmatrix}=\\ &\text{Now}\mathrm{BC}=\begin{bmatrix}1&3\\0&2\\0&2\\-1&4\end{bmatrix}\begin{bmatrix}1&2&3-4\\0&2\\2&0-2&1\end{bmatrix}=\begin{bmatrix}\frac{1+6}{0}&2+0&\frac{3-6}{0}&4+3\\0&4&0+\frac{3}{0}&0+\frac{3}{0}\\-1+8&-2+0&-3-8&4+4\end{bmatrix}\\ &=\begin{bmatrix}7&2&-3\\4&0&-4&2\\7-2&-11&8\end{bmatrix}\\ &\text{Therefore}\quad\mathrm{ABC}=\begin{bmatrix}1&1&-1\\2&0&3\\3&-1&2\end{bmatrix}\begin{bmatrix}7&2&-3&-1\\4&0&-4&2\\-2&-11&8\end{bmatrix}\\ &\text{Therefore}\quad\mathrm{ABC}=\begin{bmatrix}1&4-7&7+2&-3&-4+1&-1+2-8\\14+0+2&14+0-6&-6+0&-33&-2+0+24\\21-4+14&6+0-4&-9+4-22&-3+2+16\end{bmatrix}\\ &=\begin{bmatrix}4&4&4-7&2\\35-2&-39&22\\2&-27&11\end{bmatrix}.\\ \end{aligned} →\left[\mathrm{A}=\left[\begin{aligned}0\quad6\quad7\\ -6\quad0\quad8\\ 7\quad-8\quad0\end{aligned}\right],\mathrm{B}=\left[\begin{aligned}0\quad1\quad1\\ 1\quad0\quad2\\ 1\quad2\quad0\end{aligned}\right],\mathrm{C}=\left[\begin{aligned}2\\ -2\\ 3\end{aligned}\right]\right]$$

Calculate AC, BC and $(\mathrm{A}+\mathrm{B})\mathrm{C}$ . Also, verify that $(A+B)C=AC+BC$ 

Solution Now,$\left[\mathbf{A}+\mathbf{B}=\left[\begin{aligned}0\quad7\quad8\\ -5\quad0\quad10\\ 8\quad-6\quad0\end{aligned}\right]\right.]$ 

So 

$$\left(\mathrm{A}+\mathrm{B}\right)\mathrm{C}=\left[\begin{array}{ccc}0&7&8\\ -5&0&10\\ 8&-6&0\end{array}\right]\left[\begin{array}{c}2\\ -2\\ 3\end{array}\right]=\left[\begin{array}{c}0-14+24\\ -10+0+30\\ 16+12+0\end{array}\right]=\left[\begin{array}{c}10\\ 20\\ 28\end{array}\right] 'shed $$

Further 

$$'shed \mathrm{AC}=\left[\begin{array}{ccc}0&6&7\\-6&0&8\\7&-8&0\end{array}\right]\left[\begin{array}{c}2\\-2\\3\end{array}\right]=\left[\begin{array}{c}0-12+21\\-12+0+24\\14+16+0\end{array}\right]=\left[\begin{array}{c}9\\12\\30\end{array}\right]$$

and 

$$\mathrm{BC}=\begin{bmatrix}0&1&1\\1&0&2\\1&2&0\end{bmatrix}\begin{bmatrix}2\\-2\\3\end{bmatrix}=\begin{bmatrix}0-2+3\\2+0+6\\2-4+0\end{bmatrix}=\begin{bmatrix}1\\8\\-2\end{bmatrix}(
)$$

So 

Clearly,

$$AC+BC=\begin{bmatrix}9\\ 12\\ 30\end{bmatrix}+\begin{bmatrix}1\\ 8\\ -2\end{bmatrix}=\begin{bmatrix}10\\ 20\\ 28\end{bmatrix}$$

Example 18 If $A=\begin{bmatrix}1&2&3\\ 3&-2&1\\ 4&2&1\end{bmatrix}$ , then show that $A^{3}-23A-40I=O$ 

Solution We have $\left[\mathbf{A}^{2}=\mathbf{A}\mathbf{A}=\left[\begin{aligned}1\quad2\quad3\\ 3\quad-2\quad1\\ 4\quad2\quad1\end{aligned}\right]\left[\begin{aligned}1\quad2\quad3\\ 3\quad-2\quad1\\ 4\quad2\quad1\end{aligned}\right]=\left[\begin{aligned}19\quad4\quad8\\ 1\quad12\quad8\\ 14\quad6\quad15\end{aligned}\right]\right]$ 

So 

$$\mathrm{A}^{3}=\mathrm{AA}^{2}=\begin{bmatrix}1&2&3\\ 3&-2&1\\ 4&2&1\end{bmatrix}\begin{bmatrix}19&4&8\\ 1&12&8\\ 14&6&15\end{bmatrix}=\begin{bmatrix}63&46&69\\ 69&-6&23\\ 92&46&63\end{bmatrix}$$

Now 

$$\begin{aligned}A^{3}-23A-40I=&\begin{bmatrix}63&46&69\\69&-6&23\\92&46&63\end{bmatrix}-23\begin{bmatrix}1&2&3\\3&-2&1\\4&2&1\end{bmatrix}-40\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}\\=&\begin{bmatrix}63&46&69\\69&-6&23\\92&46&63\end{bmatrix}+\begin{bmatrix}-23&-46&-69\\-69&46&-23\\-92&-46&-23\end{bmatrix}+\begin{bmatrix}-40&0&0\\0&-40&0\\0&0&-40\end{bmatrix}\\=&\begin{bmatrix}63-23-40&46-46+0&69-69+0\\69-69+0&-6+46-40&23-23+0\\92-92+0&46-46+0&63-23-40\end{bmatrix}\\=&\begin{bmatrix}0&0&0\\0&0&0\\0&0&0\end{bmatrix}=0\end{aligned}$$

Example1In lgilative mblylctionolitcal grouphidpublicrlaion firm to promote its candidate in thre ways: telephone,house calls, and letters. The cost per contact (in paise) is given in matrix A as 

$$\begin{array}{r}{\mathrm{A}=\left[\begin{matrix}{\mathrm{C o s t\;p e r\;c o n t a c t}}\\ {40}\\ {100}\\ {50}\end{matrix}\right]\mathrm{Telephone}}\\ {\mathrm{Cossecall}}\\ {\mathrm{Letter}}\end{array}$$

The number of contacts of each type made in two cities X and Y is given by 

$\mathrm{B}=\begin{bmatrix}1000&500&5000\\3000&1000&10,000\end{bmatrix}\rightarrow\mathrm{Y}$ . Find the total amount spent by the group in the two 

cities X and Y.

Solution We have 

$$\begin{aligned}BA&=\left[40,000+50,000+250,000\right]\rightarrow X\\120,000+100,000+500,000\rightarrow Y\\&=\left[340,000\right]\rightarrow X\\&=Y\end{aligned}$$

So the total amount spent by the group in the two cities is 340,000 paise and 720,000 paise,i.e.,3400and7200,respectively.

3.2

1.公司添$$ [Tabl_][Tabl],

Find each of the following:

(i)

$$\mathrm{A}+\mathrm{B}$$

(i (ii)(i)$$ 

(ii)$$ 

(iv) AB 

(v)v)$$ 未

2.Compute the following:

$$(\begin{aligned}(i)\left[\begin{matrix}a&b\\ -b&a\end{matrix}\right]+\left[\begin{matrix}a&b\\ b&a\end{matrix}\right]&(ii)\left[\begin{matrix}a^{2}+b^{2}&b^{2}+c^{2}\\ a^{2}+c^{2}&a^{2}+b^{2}\end{matrix}\right]+\left[\begin{matrix}2ab&2bc\\ -2ac&-2ab\end{matrix}\right]\\ (iii)\left[\begin{matrix}-1&4&-6\\ 8&5&16\\ 2&8&5\end{matrix}\right]+\left[\begin{matrix}12&7&6\\ 8&0&5\\ 3&2&4\end{matrix}\right]&(iv)\left[\begin{matrix}\cos^{2}x&\sin^{2}x\\ \sin^{2}x&\cos^{2}x\end{matrix}\right]+\left[\begin{matrix}\sin^{2}x&\cos^{2}x\\ \cos^{2}x&\sin^{2}x\end{matrix}\right]\end{aligned}$$

3.Compute the indicated products.

$$\begin{aligned}(i)\begin{bmatrix}a&b\\ -b&a\end{bmatrix}&\begin{bmatrix}a&-b\\ b&a\end{bmatrix}&(ii)\begin{bmatrix}1\\ 2\\ 3\end{bmatrix}&[2\quad3\quad4]\quad(iii)\begin{bmatrix}1&-2\\ 2&3\end{bmatrix}&\begin{bmatrix}1&2&3\\ 2&3&1\end{bmatrix}\\ (iv)\begin{bmatrix}2&3&4\\ 3&4&5\\ 4&5&6\end{bmatrix}&\begin{bmatrix}1&-3&5\\ 0&2&4\\ 3&0&5\end{bmatrix}&(v)\begin{bmatrix}2&1\\ 3&2\\ -1&1\end{bmatrix}&\begin{bmatrix}1&0&1\\ -1&2&1\end{bmatrix}\\ (iv)\begin{bmatrix}3&-1&3\\ -1&0&2\end{bmatrix}&\begin{bmatrix}2&-3\\ 1&0\\ 3&1\end{bmatrix}\end{aligned}$$

4.If $\left[\mathrm{A}=\left[\begin{aligned}1&2&-3\\ 5&0&2\\ 1&-1&1\end{aligned}\right],\mathrm{B}=\left[\begin{aligned}3&-1&2\\ 4&2&5\\ 2&0&3\end{aligned}\right]\right.\text{and}\mathrm{C}=\left[\begin{aligned}4&1&2\\ 0&3&2\\ 1&-2&3\end{aligned}\right]]$ ,then compute 

(A+B) and (B – C). Also, verify that $\mathrm{A}+(\mathrm{B}-\mathrm{C})=(\mathrm{A}+\mathrm{B})-\mathrm{C}$ 

$$\mathrm{B}=\left[\begin{aligned}\frac{2}{3}\quad1\quad\frac{5}{3}\\ \frac{1}{3}\quad\frac{2}{3}\quad\frac{4}{3}\\ \frac{7}{3}\quad2\quad\frac{2}{3}\end{aligned}\right]\text{and}\mathrm{B}=\left[\begin{aligned}\frac{2}{5}\quad\frac{3}{5}\quad1\\ \frac{1}{5}\quad\frac{2}{5}\quad\frac{4}{5}\\ \frac{7}{5}\quad\frac{6}{5}\quad\frac{2}{5}\end{aligned}\right],\text{then compute}3\mathrm{A}-5\mathrm{B} published \cos\theta\left[\begin{matrix}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{matrix}\right]+\sin\theta\left[\begin{matrix}\sin\theta&-\cos\theta\\ \cos\theta&\sin\theta\end{matrix}\right] published $$

7. Find X and Y, if 

(i)

$$\mathrm{X}+\mathrm{Y}=\begin{bmatrix}7&0\\2&5\end{bmatrix}\text{and}\mathrm{X}-\mathrm{Y}=\begin{bmatrix}3&0\\0&3\end{bmatrix} published $$

(ii)

$$2X+3Y=\left[\begin{matrix}2&3\\ 4&0\end{matrix}\right]\quad and\quad3X+2Y=\left[\begin{matrix}2&-2\\ -1&5\end{matrix}\right] published $$

8.Find X, i $\mathrm{if}\mathrm{Y}=\begin{bmatrix}3&2\\ 1&4\end{bmatrix}\mathrm{and}2\mathrm{X}+\mathrm{Y}=\begin{bmatrix}1&0\\ -3&2\end{bmatrix}$ 

9.Find x and y, i $2\left[\begin{matrix}{1}&{3}\\ {0}&{x}\\ \end{matrix}\right]+\left[\begin{matrix}{y}&{0}\\ {1}&{2}\\ \end{matrix}\right]=\left[\begin{matrix}{5}&{6}\\ {1}&{8}\\ \end{matrix}\right]$ 

10. Solve the equation for ,$y,z{\mathrm{and}}$ t, if $2\begin{bmatrix}x&z\\ y&t\end{bmatrix}+3\begin{bmatrix}1&-1\\ 0&2\end{bmatrix}=3\begin{bmatrix}3&5\\ 4&6\end{bmatrix}$ 

11. If $x\left[\begin{aligned}2\\ 3\end{aligned}\right]+y\left[\begin{aligned}-1\\ 1\end{aligned}\right]=\left[\begin{aligned}1&0\\ 5\end{aligned}\right]$ , find the values of x and y.

12. Given $3\left[\begin{matrix}{x}&{y}\\ {z}&{w}\\ \end{matrix}\right]=\left[\begin{matrix}{x}&{6}\\ {-1}&{2w}\\ \end{matrix}\right]+\left[\begin{matrix}{4}&{x+y}\\ {z+w}&{3}\\ \end{matrix}\right]$ , find the values of x,$y,z\mathrm{and}w$ 

$$\mathrm{If}\mathrm{F}(x)=\begin{bmatrix}\cos x&-\sin x&0\\sin x&\cos x&0\\0&0&1\end{bmatrix},\mathrm{show that}\mathrm{F}(x)\mathrm{F}(y)=\mathrm{F}(x+y).$$

14. Show that 

(i)

$$\begin{bmatrix}5&-1\\ 6&7\end{bmatrix}\begin{bmatrix}2&1\\ 3&4\end{bmatrix}\neq\begin{bmatrix}2&1\\ 3&4\end{bmatrix}\begin{bmatrix}5&-1\\ 6&7\end{bmatrix}$$

(ii)

$$\left[\begin{aligned}1\quad2\quad3\\ 0\quad1\quad0\\ 1\quad1\quad0\end{aligned}\right]\left[\begin{aligned}-1\quad1\quad0\\ 0\quad-1\quad1\\ 2\quad3\quad4\end{aligned}\right]\neq\left[\begin{aligned}-1\quad1\quad0\\ 0\quad-1\quad1\\ 2\quad3\quad4\end{aligned}\right]\left[\begin{aligned}1\quad2\quad3\\ 0\quad1\quad0\\ 1\quad1\quad0\end{aligned}\right] LRT oished \left[\begin{aligned}1\quad2\quad3\\ 0\quad1\quad0\\ 1\quad1\quad0\end{aligned}\right]\left[\begin{aligned}-1\quad1\quad0\\ 0\quad-1\quad1\\ 2\quad3\quad4\end{aligned}\right]\neq\left[\begin{aligned}-1\quad1\quad0\\ 0\quad-1\quad1\\ 2\quad3\quad4\end{aligned}\right]\left[\begin{aligned}1\quad2\quad3\\ 0\quad1\quad0\\ 1\quad1\quad0\end{aligned}\right]$$

15.$\mathrm{Find}\;\mathrm{A}^2-5\mathrm{A}+6\mathrm{I}.$ ,if $A=\begin{bmatrix}2&0&1\\ 2&1&3\\ 1&-1&0\end{bmatrix}$ LRT 

$$LRT `blished \mathrm{If}\;\mathrm{A}=\begin{bmatrix}1&0&2\\ 0&2&1\\ 2&0&3\end{bmatrix},\;\mathrm{prove}\;\mathrm{that}\;\mathrm{A}^3-6\mathrm{A}^2+7\mathrm{A}+2\mathrm{I}=0$$

17.If $\mathrm{A}=\begin{bmatrix}3&-2\\ 4&-2\end{bmatrix}\quad\mathrm{and}\quad\mathrm{I}=\begin{bmatrix}1&0\\ 0&1\end{bmatrix}$ find k so that $\mathrm{A}^{2}=k\mathrm{A}-2\mathrm{I}$ 

18.$\mathrm{If}\;\mathrm{A}=\left[\begin{aligned}0&-\tan\frac{\alpha}{2}\\ \tan\frac{\alpha}{2}&0\end{aligned}\right]$ and I is the identity matrix of order 2, show that 

$$\mathrm{I}+\mathrm{A}=(\mathrm{I}-\mathrm{A})\begin{bmatrix}\cos\alpha&-\sin\alpha\\ \sin\alpha&\cos\alpha\end{bmatrix}$$

19. A trust fund has30,000 that must be invested in two different types of bonds.The first bond pays 5% interest per year, and the second bond pays 7% interest per year. Using matrix multiplication, determine how to divide τ30,000 among the two types of bonds. If the trust fund must obtain an annual total interest of:

(a)₹1800

(b)2000

20. The bookshop of a particular school has 10 dozen chemistry books, 8 dozen physics books, 10 dozen economics books. Their selling prices are₹80, 60 and 40 each respectively. Find the total amount the bookshop will receive from selling all the books using matrix algebra.



Assume X, Y, Z, W and P are matrices of order $2\times n,3\times k,2\times p,n\times3$ and $p\times k$ ,respectively. Choose the correct answer in Exercises 21 and 22.

21. The restriction on n, k and p so that $\mathrm{PY}+\mathrm{WY}$ will be defined are:

$$\begin{aligned}&(A)k=3,p=n\quad&(B)k is arbitrary,p=2\\&(C)p is arbitrary,k=3\quad&(D)k=2,p=3\end{aligned}$$

22. If $n=p$ ,thentheof the matrix $7\mathrm{X}-5\mathrm{Z}$ is:

(A) $p\times2$ (B)$2\times n$ (C)$n\times3$ (D) .$p\times n$ ed 

#### 3.5. Transpose of a Matrix 

Inthis scti wlrto randclty o atrices such as symmetric and skew symmetric matrices.



Definition 3$\mathrm{IfA=[a_{ij}]}$ |be an $m\times n$ matrix, then the matrix obtained by interchanging the rows and columns of A is called the transpose of A. Transpose of the matrix A is denoted by $\mathrm{A}'\mathrm{or}\left(\mathrm{A}^{\mathrm{T}}\right)$ 1. In other words, if $\mathrm{f}A=\left[a_{ij}\right]_{m\times n}$ then $\mathrm{A}'=\left[a_{ii}\right]_{n\times m}$ . For example,_



$$\mathrm{if}\mathrm{A}=\left[\begin{matrix}3&5\\ \sqrt{3}&1\\ 0&-1\\ \frac{-1}{5}\end{matrix}\right]_{3\times2},\mathrm{then}\mathrm{A}'=\left[\begin{matrix}3&\sqrt{3}&0\\ &&-1\\ 5&1&\frac{-1}{5}\end{matrix}\right]_{2\times3}$$

#### 3.5.1 Properties of transpose of the matrices 

We now state the following properties of transpose of matrices without proof. These may be verified by taking suitable examples.



For any matrices A and B of suitable orders, we have 

(i)

$$(\mathbf{A}')'=\mathbf{A}$$

(ii)$(k\mathrm{A})'=k\mathrm{A}'$ (where k is any constant)

(i))

$$(A+B)'=A'+B'$$

(iv)

$$(A B)'=B'A'$$

Example 20 If $\mathrm{A}=\begin{bmatrix}3&\sqrt{3}&2\\ 4&2&0\end{bmatrix}\text{and}\mathrm{B}=\begin{bmatrix}2&-1&2\\ 1&2&4\end{bmatrix}$ , verify that 

(i)$(A')'=A$ (ii)$(A+B)'=A'+B'.$ 

(i $(k\mathrm{B})'=k\mathrm{B}'$ ,where k is any constant.

 Solution 

(i) We have 

$$A=\begin{bmatrix}3&\sqrt{3}&2\\ 4&2&0\end{bmatrix}\Rightarrow A^{\prime}=\begin{bmatrix}3&4\\ \sqrt{3}&2\\ 2&0\end{bmatrix}\Rightarrow(A^{\prime})^{\prime}=\begin{bmatrix}3&\sqrt{3}&2\\ 4&2&0\end{bmatrix}=A $$

Thus $(A')'=A$ 

(i) We have 

$$\mathrm{A}=\begin{bmatrix}3&\sqrt{3}&2\\4&2&0\end{bmatrix},\mathrm{B}=\begin{bmatrix}2&-1&2\\1&2&4\end{bmatrix}\Rightarrow\mathrm{A}+\mathrm{B}=\begin{bmatrix}5&\sqrt{3}-1&4\\5&4&4\end{bmatrix} blished $$

Therefore 

Now 

So 

Thus 

We have 

Then 

Thus 

$$(A+B)'=\begin{bmatrix}5&5\\ \sqrt{3}-1&4\\ 4&4\end{bmatrix} blished blished \mathrm{A}^{\prime}=\left[\begin{aligned}3\quad&4\\ \sqrt{3}\quad&2\\ 2\quad&0\end{aligned}\right],\mathrm{B}^{\prime}=\left[\begin{aligned}2\quad&1\\ -1\quad&2\\ 2\quad&4\end{aligned}\right],\mathrm{A}'+\mathrm{B}'=\begin{bmatrix}5&5\\ \sqrt{3}-1&4\\ 4&4\end{bmatrix}(A+B)'=A'+B'k\mathrm{B}=k\left[\begin{aligned}2&-1&2\\ 1&2&4\end{aligned}\right]=\left[\begin{aligned}2k&-k&2k\\ k&2k&4k\end{aligned}\right](E 3)^{\prime}=\left[\begin{aligned}2k\quad k\\-k\quad2k\\2k\quad4k\end{aligned}\right]=k\left[\begin{aligned}2\quad1\\-1\quad2\\2\quad4\end{aligned}\right]=kB^{\prime}$$

(E $3^{\prime}=\left[\begin{aligned}2k\quad k\\-k\quad2k\\2k\quad4k\end{aligned}\right]=k\left[\begin{aligned}2\quad1\\-1\quad2\\2\quad4\end{aligned}\right]=kB^{\prime}$ 

(kB)$^{\prime}=k\mathrm{B}^{\prime}$ 

Example 21 If $A=\left[\begin{aligned}-2\\ 4\\ 5\end{aligned}\right],B=\left[\begin{aligned}1\quad3\quad-6\end{aligned}\right],\text{verify that}(A B)^{\prime}=B^{\prime}A^{\prime}.$ 

Solution We have 

$$A=\left[\begin{aligned}-2\\ 4\\ 5\end{aligned}\right],B=\left[\begin{aligned}1\quad3\quad-6\end{aligned}\right]$$

then 

$$\mathrm{AB}=\begin{bmatrix}-2\\ 4\\ 5\end{bmatrix}\begin{bmatrix}1&3&-6\end{bmatrix}=\begin{bmatrix}-2&-6&12\\ 4&12&-24\\ 5&15&-30\end{bmatrix} `ublished $$

Now 

$$\mathrm{A}^{\prime}=[-245],\mathrm{B}^{\prime}=\left[\begin{array}{l}1\\ 3\\ -6\end{array}\right]$$

Clearly 

$$`ublished \mathrm{B}^{\prime}\mathrm{A}^{\prime}=\left[\begin{array}{l}1\\ 3\\ -6\end{array}\right]\left[-2\quad4\quad5\right]=\left[\begin{array}{ccc}-2&4&5\\ -6&12&15\\ 12&-24&-30\end{array}\right]=(\mathrm{AB})^{\prime}$$

### 3.6 Symmetric and Skew Symmetric Matrices 

Definition 4 A square matrix $A=[a_{ij}]$ is said to be symmetric if $\mathrm{A}^{\prime}=\mathrm{A}$ ,that is,$\left[a_{ij}\right]=\left[a_{ji}\right]$ for all possible values of i and j.



$$ For example A=\left[\begin{aligned}\sqrt{3}\quad&2\quad&3\\ 2\quad&-1.5\quad&-1\\ 3\quad&-1\quad&1\end{aligned}\right]is a symmetric matrix as A'=A'$$

Definition 5 A square matrix $A=[a_{ij}]$ is said to be skew symmetric matrix if $A'=-A$ ,that is $a_{ji}=-a_{ij}$ for all possible values of i and j. Now, if we put $i=j,$ , we have $a_{ii}=-a_{ii}$ . Therefore $2a_{ii}=0or a_{ii}=0$ for all $i^{\prime}\mathrm{s}$ 



This means that all the diagonal elements of a skew symmetric matrix are zero.

For example, the matrix $\mathbf{B}=\left[\begin{matrix}{0}&{e}&{f}\\ {-e}&{0}&{g}\\ {-f}&{-g}&{0}\end{matrix}\right]$ is a skew symmetric matrix as $B'=-B$ 

Now, we are going to prove some resultsof symmetricand skew-symmetric matrices.



Theorem 1 For any square matrix A with real number entries,$\mathrm{A}+\mathrm{A}'$ is a symmetric matrix and E $\mathrm{A}-\mathrm{A}'$ is a skew symmetric matrix.sned Proof Let $\mathrm{B}=\mathrm{A}+\mathrm{A}'$ ,then 

Therefore 

Now let 

Therefore 

$$\begin{aligned}B'&=(A+A')'\\&=A'+(A')'(as(A+B)'=A'+B')\\&=A'+A(as(A')'=A)\\&=A+A'(as A+B=B+A)\\&=B\\ B&=A+A'is a symmetric matrix\\ C&=A-A'\\ C'&=(A-A')'=A'-(A')'\quad(Why?)\\&=A'-A\quad(Why?)\\&=-(A-A')=-C\\ C&=A-A'is a skew symmetric matrix\end{aligned} <.f  q $$

Theorem 2 Any square matrix can be expressed as the sum of a symmetric and a skew symmetric matrix.



Proof Let A be a square matrix, then we can write 

$$\mathrm{A}=\frac{1}{2}(\mathrm{A}+\mathrm{A}^{\prime})+\frac{1}{2}(\mathrm{A}-\mathrm{A}^{\prime})$$

From the Theorem 1, we know that $\left(\mathrm{A}^{+}\mathrm{A}^{\prime}\right)$ is a symmetric matrix and $(\mathrm{A}-\mathrm{A}^{\prime})$ is a skew symmetric matrix. Since for any matrix A,$(kA)^{\prime}=kA^{\prime}$ , it follows that $\frac{1}{2}(A+A')$  is symmetric matrix and $\left[\frac{1}{2}\left(\mathrm{A}-\mathrm{A}'\right)\right]$ is skew symmetric matrix. Thus, any square matrixcanbeexpresd asthesumofsymmticndskew symmetric matrix.

Example 22 Express the matrix $\mathbf{B}=\left[\begin{aligned}2\quad-2\quad-4\\ -1\quad3\quad4\\ 1\quad-2\quad-3\end{aligned}\right]$ as the sum of a symmetric and a skew symmetric matrix.

ied 

Solution Here 

Let 

Now 

Thus 

Also, let nc 

$$\begin{aligned}\mathrm{B}^{\prime}&=\left[\begin{matrix}2&-1&1\\-2&3&-2\\-4&4&-3\end{matrix}\right]\\mathrm{P}&=\frac{1}{2}(\mathrm{B}+\mathrm{B}^{\prime})=\frac{1}{2}\left[\begin{matrix}4&-3&-3\\-3&6&2\\-3&2&-6\end{matrix}\right]=\left[\begin{matrix}2&\frac{-3}{2}&\frac{-3}{2}\\frac{-3}{2}&3&1\\frac{-3}{2}&1&-3\end{matrix}\right],\\mathrm{P}^{\prime}&=\left[\begin{matrix}2&\frac{-3}{2}&\frac{-3}{2}\\frac{-3}{2}&3&1\\frac{-3}{2}&1&-3\end{matrix}\right]=\mathrm{P}\end{aligned} ied $$

$\mathrm{p}=\frac{1}{2}(\mathrm{B}+\mathrm{B}^{\prime})$ is a symmetric matrix.

$\mathrm{Q}=\frac{1}{2}(\mathrm{B}-\mathrm{B}^{\prime})=\frac{1}{2}\left[\begin{aligned}0&\quad-1&\quad-5\\ 1&\quad0&\quad6\\ 5&\quad-6&\quad0\end{aligned}\right]=\left[\begin{aligned}0&\quad\frac{-1}{2}&\quad\frac{-5}{2}\\ \frac{1}{2}&\quad0&\quad3\\ \frac{5}{2}&\quad-3&\quad0\end{aligned}\right]$ 

$$\mathrm{p}=\frac{1}{2}(\mathrm{B}+\mathrm{B}^{\prime})
nc \mathrm{Q}=\frac{1}{2}(\mathrm{B}-\mathrm{B}^{\prime})=\frac{1}{2}\left[\begin{aligned}0&\quad-1&\quad-5\\ 1&\quad0&\quad6\\ 5&\quad-6&\quad0\end{aligned}\right]=\left[\begin{aligned}0&\quad\frac{-1}{2}&\quad\frac{-5}{2}\\ \frac{1}{2}&\quad0&\quad3\\ \frac{5}{2}&\quad-3&\quad0\end{aligned}\right]$$ Then 

$$Q^{\prime}=\left[\begin{aligned}0&\quad\frac{1}{2}&\quad\frac{5}{3}\\ \frac{-1}{2}&\quad0&\quad-3\\ \frac{-5}{2}&\quad3&\quad0\end{aligned}\right]=-Q $$

Thus 

$Q=\frac{1}{2}(B-B')$ is a skew symmetric matrix.

Now 

$$\left[\mathrm{P}+\mathrm{Q}=\left[\begin{aligned}2&\quad\frac{-3}{2}&\quad\frac{-3}{2}\\ \frac{-3}{2}&\quad3&\quad1\\ \frac{-3}{2}&\quad1&\quad-3\end{aligned}\right]+\left[\begin{aligned}0&\quad\frac{-1}{2}&\quad\frac{-5}{2}\\ \frac{1}{2}&\quad0&\quad3\\ \frac{5}{2}&\quad-3&\quad0\end{aligned}\right]=\left[\begin{aligned}2&\quad-2\quad-4\\ -1&\quad3&\quad4\\ 1&\quad-2&\quad-3\end{aligned}\right]=\mathrm{B}\right] 9$$

Thus, B is represented as the sum of a symmetric and a skew symmetric matrix 

### EXERCISE 3.3

1. Find the transpose of each of the following matrices:

$$\left(\mathrm{i}\right)\begin{bmatrix}5\\ \dfrac{1}{2}\\ -1\end{bmatrix}\quad\left(\mathrm{ii}\right)\begin{bmatrix}1&-1\\ 2&3\end{bmatrix}\quad\left(\mathrm{iii}\right)\begin{bmatrix}-1&5&6\\ \sqrt{3}&5&6\\ 2&3&-1\end{bmatrix}$$

2.If $\mathrm{A}=\left[\begin{aligned}-1&2&3\\ 5&7&9\\ -2&1&1\end{aligned}\right]\text{and}\mathrm{B}=\left[\begin{aligned}-4&1&-5\\ 1&2&0\\ 1&3&1\end{aligned}\right]$ , then verify that 

(i)$(A+B)'=A'+B'$ (ii)$(A-B)'=A'-B'$ 

3.1$\mathrm{If}\mathrm{A}^{\prime}=\left[\begin{aligned}3\quad4\\ -1\quad2\\ 0\quad1\end{aligned}\right]\text{and}\mathrm{B}=\left[\begin{aligned}-1\quad2\quad1\\ 1\quad2\quad3\end{aligned}\right]$ , then verify that 

(i)

$$(A+B)'=A'+B'$$

(ii)

$$(ii)(A-B)'=A'-B'$$

4.Ⅱ1$\mathrm{f}\mathrm{A}^{\prime}=\left[-2\quad3\right]\text{and}\mathrm{B}=\left[-1\quad0\right],\text{then find}(\mathrm{A}+2\mathrm{B})^{\prime}$ 

5.For the matrices A and B, verify that $(AB)^{\prime}=B^{\prime}A^{\prime}$ ', where 

6. If (i)$\mathbf{A}=\begin{bmatrix}\cos\alpha&\sin\alpha\\ -\sin\alpha&\cos\alpha\end{bmatrix}$ , then verify that $A^{\prime}A=I$ 

(i)

$$\mathrm{A}=\begin{bmatrix}1\\ -4\\ 3\end{bmatrix},\mathrm{B}=\begin{bmatrix}-1&2&1\end{bmatrix}\quad(\mathrm{ii})\quad\mathrm{A}=\begin{bmatrix}0\\ 1\\ 2\end{bmatrix},\mathrm{B}=\begin{bmatrix}1&5&7\end{bmatrix}$$

(i)If $\mathrm{A}=\begin{bmatrix}\sin\alpha&\cos\alpha\\ -\cos\alpha&\sin\alpha\end{bmatrix}$ , then verify that $A^{\prime}A=\mathrm{I}$ (cd:1)

7.(i) Show that the matrix $A=\begin{bmatrix}1&-1&5\\ -1&2&1\\ 5&1&3\end{bmatrix}$   mmetric matrix.

(ii) Show that the matrix $A=\left[\begin{matrix}{0}&{1}&{-1}\\ {-1}&{0}&{1}\\ {1}&{-1}&{0}\\ \end{matrix}\right]$ ）is a skew symmetric matrix.

8.For the matrix $A=\begin{bmatrix}1&5\\ 6&7\end{bmatrix}$ , verify that 

(i)$\left(\mathrm{A}+\mathrm{A}'\right)$ is a symmetric matrix 

(ii)$\left(\mathrm{A}-\mathrm{A}'\right)$ is a skew symmetric matrix 

9.$\mathrm{Find}\frac{1}{2}(\mathrm{A}+\mathrm{A}^{\prime})\mathrm{and}\frac{1}{2}(\mathrm{A}-\mathrm{A}^{\prime})$ , when $\left[\begin{aligned}\mathbf{A}=\left[\begin{aligned}0\quad a\quad b\\ -a\quad0\quad c\\ -b\quad-c\quad0\end{aligned}\right]\end{aligned}\right.]$ 

10. Express the following matrices as the sum of a symmetric and a skew symmetric matrix:

(i)$\begin{bmatrix}3&5\\ 1&-1\end{bmatrix}$ 

(i)

$$\left[\begin{aligned}6\quad-2\quad2\\ -2\quad3\quad-1\\ 2\quad-1\quad3\end{aligned}\right]$$

(im)

$$\begin{pmatrix}3&3&-1\\-2&-2&1\\-4&-5&2\end{pmatrix}$$

(iv)$\begin{pmatrix}1&5\\ -1&2\end{pmatrix}$ 

Choose the correct answer in the Exercises 1l and 12.

11. IfA, B are symmetric matrices of same order, then $\mathrm{A B-B A}$ 

(A) Skew symmetric matrix 



(C) Zero matrix (D) Identity matrix 

12.If $\mathbf{A}=\left[\begin{aligned}\cos\alpha\quad-\sin\alpha\\ \sin\alpha\quad\cos\alpha\end{aligned}\right]$ (ci),and $$ Y ,then t   vue f  is  ae f 

(A)$\frac{\pi}{6}$ C Y (B)c $$ 

(C)π2(p)(D)$$ 不

### 3.7 Invertible Matrices 

Definition 6 If A is a square matrix of order m, and if there exists another square matrix B of the same order m, such that $AB=BA=I$ , then B is called the inverse matrix olAanditisdenoted by $\mathrm{A^{-1}}$ In that case Ais said to be invertible.



$A=\left[\begin{aligned}2\quad3\\ 1\quad2\end{aligned}\right]and B=\left[\begin{aligned}2\quad-3\\ -1\quad2\end{aligned}\right]$ be two matrices.

Now 

$$\mathrm{AB}=\left[\begin{aligned}2\quad3\\ 1\quad2\end{aligned}\right]\left[\begin{aligned}2\quad-3\\ -1\quad2\end{aligned}\right]\begin{bmatrix}4-3&-6+6\\ 2-2&-3+4\end{bmatrix}=\begin{bmatrix}1&0\\ 0&1\end{bmatrix}=I $$

Also $\mathrm{BA}=\begin{bmatrix}1&0\\ 0&1\end{bmatrix}=\mathrm{I}$ . Thus B is the inverse of A, in other words $\mathbf{B}=\mathbf{A}^{-1}$ and A is inverse of B, i.e.,$\mathrm{A}=\mathrm{B}^{-1}$ 



## Note 

1. Arectangular matrix does not possess inverse matrix, since for products BA and AB to be defined and to be equal, it is necessary that matrices A and B should be square matrices of the same order.



2.If B is the inverse of A, then A is also the inverse of B.

Theorem 3 (Uniqueness of inverse) Inverse of a square matrix, if it exists, is unique.Proof Let ives $A=[a_{ij}]$ hall show that be a square m $\mathrm{B}=\mathrm{C}$ of order m.If possib      ,Since B is the inverse of A 

$$AB=BA=I $$

Since C is also the inverse of A 

$$AC=CA=I $$

Thus 

$$\mathrm{B}=\mathrm{BI}=\mathrm{B}(\mathrm{AC})=(\mathrm{BA})\mathrm{C}=\mathrm{IC}=\mathrm{C}$$

Theorem 4 If A and B are invertible matrices of the same order, then $(AB)^{-1}=B^{-1}A^{-1}$ Proof From the definition of inverse of a matrix, we have 

or 

or 

or 

or 

or 

or 

Hence 

$$(AB)(AB)^{-1}=1A^{-1}\left(AB\right)\left(AB\right)^{-1}=A^{-1}(A^{-1}A)\cdot B(A\bar{B})^{-1}=A^{-1}C 
C \mathrm{IB}(\mathrm{AB})^{-1}=\mathrm{A}^{-1}B(AB)^{-1}=A^{-1}not tc B^{-1}\ B\ (AB)^{-1}=B^{-1}\ A^{-1}not tc \Gamma(AB)^{-1}=B^{-1}A^{-1}not tc (AB)^{-1}=B^{-1}A^{-1}$$

(Pre multiplying both sides by $\mathrm{A^{-1}}$ cd)

$$(\mathrm{S i n c e~A^{-1}~I}=\mathrm{A^{-1}})$$

### EXERCISE 3.4

1. Matrices A and B will be inverse of each other only if not tc 

(A)$AB=BA(B)AB=BA=0$ 

$$(\mathrm{C})\mathrm{AB}=0,\mathrm{BA}=\mathrm{I}(\mathrm{D})\mathrm{AB}=\mathrm{BA}=\mathrm{I}$$

## Miscellaneous Examples 

Example 23 If $\mathbf{A}=\left[\begin{matrix}{\cos\theta}&{\sin\theta}\\ {-\sin\theta}&{\cos\theta}\end{matrix}\right]$ , then prove that $\mathbf{A}^{n}=\begin{bmatrix}\cos n\theta&\sin n\theta\\-\sin n\theta&\cos n\theta\end{bmatrix},n\in\mathbf{N}$ 

Solution Wllvltuileofmluti.

We have 

$$\begin{aligned}&P(n):If A=\begin{bmatrix}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{bmatrix},then A^n=\begin{bmatrix}\cos n\theta&\sin n\theta\\ -\sin n\theta&\cos n\theta\end{bmatrix},n\in N\\&P(1):A=\begin{bmatrix}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{bmatrix},so A^1=\begin{bmatrix}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{bmatrix}\\ \end{aligned}$$

Therefore,the result is true for $n=1$ 

Let the result be true for $n=k$ .So 

$$人
\mathrm{P}(k):\mathrm{A}=\left[\begin{aligned}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{aligned}\right],\text{then}\mathrm{A}^{k}=\left[\begin{aligned}\cos k\theta&\sin k\theta\\ -\sin k\theta&\cos k\theta\end{aligned}\right]$$

Now, we prove that the result holds for $n=k+1$ 

Now 

$$\begin{aligned}\mathrm{A}^{k+1}=\mathrm{A}\cdot\mathrm{A}^k=\begin{bmatrix}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{bmatrix}\begin{bmatrix}\cos k\theta&\sin k\theta\\ -\sin k\theta&\cos k\theta\end{bmatrix}\\=\begin{bmatrix}\cos\theta\cos k\theta-\sin\theta\sin k\theta&\cos\theta\sin k\theta+\sin\theta\cos k\theta\\ -\sin\theta\cos k\theta+\cos\theta\sin k\theta&-\sin\theta\sin k\theta+\cos\theta\cos k\theta\end{bmatrix}\\=\begin{bmatrix}\cos(\theta+k\theta)&\sin(\theta+k\theta)\\ -\sin(\theta+k\theta)&\cos(\theta+k\theta)\end{bmatrix}=\begin{bmatrix}\cos(k+1)\theta&\sin(k+1)\theta\\ -\sin(k+1)\theta&\cos(k+1)\theta\end{bmatrix}\end{aligned}$$

Therefore, the result is true for $n=k+1$ . Thus by principle of mathematical induction,

we have $\mathbf{A}^{n}=\left[\begin{matrix}\cos n\theta&\sin n\theta\\-\sin n\theta&\cos n\theta\end{matrix}\right]$ , holds for all natural numbers._



Example2Idemmeofteamhowhat is symmetric if and only if A and B commute, that is $AB=BA$ 

Solution Since A and B are both symmetric matrices, therefore $\mathrm{A}'=\mathrm{A}and\mathrm{B}'=\mathrm{B}$ 

Let AB be symmetric, then $(AB)^{\prime}=AB$ 

But 

$$(AB)'=B'A'=BA(Why?)$$

Therefore 

$$BA=AB $$

Conversely, if $AB=BA$ , then we shall show that AB is symmetric.

Now 

$$\begin{aligned}(AB)^{\prime}&=B^{\prime}A^{\prime}\\&=B A(as A and B are symmetric)\\&=AB\\ \end{aligned}$$

Hence AB is symmetric.

Example 25 Let $\mathrm{A}=\begin{bmatrix}2&-1\\3&4\end{bmatrix},\mathrm{B}=\begin{bmatrix}5&2\\7&4\end{bmatrix},\mathrm{C}=\begin{bmatrix}2&5\\3&8\end{bmatrix}$ . Find a matrix uchthat 

$\mathrm{CD}-\mathrm{AB}=\mathrm{O}$ 



$\mathrm{C D-A B}$ is well defined, D must be a square matrix of order 2.



Let 

$$\mathrm{D}=\begin{bmatrix}a&b\\ c&d\end{bmatrix}.\;\mathrm{Then}\;\mathrm{CD}-\mathrm{AB}=0\;\mathrm{gives}\begin{bmatrix}2&5\\ 3&8\end{bmatrix}\begin{bmatrix}a&b\\ c&d\end{bmatrix}-\begin{bmatrix}2&-1\\ 3&4\end{bmatrix}\begin{bmatrix}5&2\\ 7&4\end{bmatrix}=0$$

or 

$$\begin{bmatrix}2a+5c&2b+5d\\ 3a+8c&3b+8d\end{bmatrix}-\begin{bmatrix}3&0\\ 43&22\end{bmatrix}=\begin{bmatrix}0&0\\ 0&0\end{bmatrix}$$

or 

$$\begin{bmatrix}2a+5c-3&2b+5d\\ 3a+8c-43&3b+8d-22\end{bmatrix}=\begin{bmatrix}0&0\\ 0&0\end{bmatrix}$$

By equality of matrices, we get not 

and 

$$\begin{aligned}2a+5c-3&=0\\3a+8c-43&=0\\2b+5d&=0\\3b+8d-22&=0\end{aligned}$$

Solving (1) and (2), we get $a=-191,c=77$ . Solving (3) and (4), we get $b=-110$ 1,

$d=44$ 



Therefore 

$$\mathrm{D}=\left[\begin{aligned}a&\quad b\\c&\quad d\end{aligned}\right]=\left[\begin{aligned}-191&\quad-110\\77&\quad44\end{aligned}\right]$$

## Miscellaneous Exercise on Chapter 3

1.IfA and B are symmetric matrices, prove that $\mathrm{AB}-\mathrm{BA}$ is a skew symmetric matrix.



2.Show that the matrix B'AB is symmetric or skew symmetric according as A is symmetric or skew symmetric.



3.Find the values of x,$y,z\;\mathrm{if}$ the matrix $A=\begin{bmatrix}0&2y&z\\ x&y&-z\\ x&-y&z\end{bmatrix}$ 



A'A = I.

4.For what values of x :$\left[\begin{matrix}{1}&{2}&{1}\\ \end{matrix}\right]\left[\begin{matrix}{1}&{2}&{0}\\ {2}&{0}&{1}\\ {1}&{0}&{2}\\ \end{matrix}\right]\left[\begin{matrix}{0}\\ {2}\\ {x}\\ \end{matrix}\right]=0\$ 

5. If $\mathrm{A}=\begin{bmatrix}3&1\\ -1&2\end{bmatrix}$ ,show that $A^{2}-5A+7I=0$ 

6.Findx, if $\begin{bmatrix}x&-5&-1\end{bmatrix}\begin{bmatrix}1&0&2\\ 0&2&1\\ 2&0&3\end{bmatrix}\begin{bmatrix}x\\ 4\\ 1\end{bmatrix}=0$ 

7. A manufacturer produces three products x, y, z which he sells in two markets.Annual sales are indicated below:


<div style="text-align: center;"><html><body><table border="1"><tr><td>Market</td><td colspan="3">Products</td></tr><tr><td>I</td><td>10,000</td><td>2,000</td><td>18,000</td></tr><tr><td>II</td><td>6,000</td><td>20,000</td><td>8,000</td></tr></table></body></html></div>


(a) If unit sale prices of x, y and z are $2.50,\bar{x}1.50$ and 1.00, respectively,find the total revenue in each market with the help of matrix algebra.

(b) If the unit costs of the above three commodities are $2.00,\ 1.00$ and 50 paise respectively. Find the gross profit.



8.Find the matrix X so that $\mathrm{X}\begin{bmatrix}1&2&3\\ 4&5&6\end{bmatrix}=\begin{bmatrix}-7&-8&-9\\ 2&4&6\end{bmatrix}$ 

Choose the correct answer in the following questions:

9.If $\mathrm{A}=\begin{bmatrix}\alpha&\beta\\ \gamma&-\alpha\end{bmatrix}$ is such that $\mathrm{A}^{2}=\mathrm{I}$ ,then 

(C)$1-\alpha^{2}-\beta\gamma=0$ $1+\alpha^{2}+\beta\gamma=0$ (B)$1+\alpha^{2}-\beta\gamma=0$ $1+\alpha^{2}-\beta\gamma=0$ $1-\alpha^{2}+\beta\gamma=0$ c 

10.If the matrix A is both symmetric and skew symmetric,then 

(A) A is a diagonal matrix matrix 

(C) A is a square matrix None of these 

11. IfA is square matrix such that $A^{2}=A$ ,then $(\mathrm{I}+\mathrm{A})^{3}-7$ A is equal to 

(A)A (B)$\mathrm{I}-\mathrm{A}$ (D)3A 

## Summary 

A matrix is an ordered rectangular array ofnumbers or functions.

A matrix having m rows and n columns is called a matrix of order $m\times n$ 

$[a_{ij}]_{m\times1}$ is a column matrix.

$[a_{ij}]_{1\times n}$ is a row matrix.

$\mathrm{An}\;m\times n$ matrix is a square matrix if $m=n$ 

$A=\left[a_{ij}\right]_{m\times m}$ is a diagonal matrix if $a_{ij}=0$ when $i\neq j$ 

■$A=\left[a_{ii}\right]_{n\times n}$ is a scalar matrix if $a_{ij}=0$ when $i\ne j,a_{ij}=k,$ (k is some constant), when $i=j$ 



■$A=\left[a_{ij}\right]_{n\times n}$ is an identity matrix, if $a_{ij}=1$ , when $i=j,a_{ij}=0$ when $i\neq j.$ 

A zero matrix has all its elements as zero.

■$\mathrm{A}=\left[a_{ij}\right]=\left[b_{ij}\right]=\mathrm{B}$ if (i) A and B are of same order, (ii)$a_{ij}=b_{ij}$ for all possible values of i and j.



$$kA=k[a_{ij}]_{m\times n}=[k(a_{ij})]_{m\times n}-\mathrm{A}=(-1)\mathrm{A}$$



$A-B=A+(-1)B$ 



$\mathbf{A}+\mathbf{B}=\mathbf{B}+\mathbf{A}$ 

$(\mathrm{A}+\mathrm{B})+\mathrm{C}=\mathrm{A}+(\mathrm{B}+\mathrm{C})$ , where A, B and C are of same order.

$k(\mathrm{A}+\mathrm{B})=k\mathrm{A}+k\mathrm{B}$ , where A and B are of same order, k is constant.

$(k+l)\mathrm{A}=k\mathrm{A}+l\mathrm{A}$ , where k and l are constant.

$\mathrm{If}\;\mathrm{A}=[a_{ij}]_{m\times n}\;\mathrm{and}\;\mathrm{B}=[b_{jk}]_{n\times p}$ 9, then $\mathrm{AB}=\mathrm{C}=\left[c_{ik}\right]_{m\times p},$ 1ooorbtire.where $$ 

(i)\mathrm{A}(\mathrm{BC})=(\mathrm{AB})\mathrm{C},\quad(\mathrm{ii})\quad\mathrm{A}(\mathrm{B}+\mathrm{C})=\mathrm{AB}+\mathrm{AC}. 111(A+B)C=AC+BC 司

$$\mathrm{If}\;\mathrm{A}=[a_{ij}]_{m\times n^*}\;\mathrm{then}\;\mathrm{A}'\;\mathrm{or}\;\mathrm{A}^{\mathrm{T}}=[a_{ji}]_{n\times m}$$

(i)$(\mathrm{A}')'=\mathrm{A}$ (ii)$(k\mathrm{A})'=k\mathrm{A}'$ (iii)$(A+B)'=A'+B',\quad(iv)\quad(AB)'=B'A'$ 

A is a symmetric matrix if $\mathbf{A}^{\prime}=\mathbf{A}$ 

A is a skew symmetric matrix if $A^{\prime}=-A$ 

■Any square matrix can be represented as the sum of a symmetric and a skew symmetric matrix.



■If A and B are two square matrices such that $AB=BA=I$ 

inverse matrix ofAandisdenotedby $\mathbf{A}^{-1}$ and A is the inverse of B.



Inverse of a square matrix, if it exists, is unique.not to be 

