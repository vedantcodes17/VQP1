

# RELATIONS AND FUNCTIONS 

### 出Mathematics isthe indispensable instrument of all physical research. – BERTHELOT 出

### 2.1 Introduction 

Much of mathematics is about finding a pattern – a recognisable link between quantities that change. In our daily life, we come across many patterns that characterise relations such asbrother and sister,ather and son,acher and student. In mathematics also, we come across many relations such as number m is less than number n, line l is parallel toline, etAis asubsetofetB.Inallthese,w notice that a relation involves pairs of objects in certain order. In this Chapter, we will learn how to link pairs of objects from two ts and then introduce relations between the two objects in the pair, Finally, we will learn about special relations which will qualify tobe functions. he 

<div style="text-align: center;"><img src="imgs/img_in_image_box_622_454_863_765.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">G.W.Leibnitz (1646–1716)</div>


concept of function is very important in mathematics since it captures the idea of a mathematically precise correspondence between one quantity with the other.

### 2.2 Cartesian Products of Sets 

Suppose A is a set of 2 colours and B is a set of 3 objects, i.e.,

$$\mathrm{A}=\{\mathrm{red},\mathrm{blue}\}\mathrm{and}\mathrm{B}=\{b,c,s\},$$

where b, c and s represent a particular bag, coat and shirt, respectively.How many pairs of coloured objects can be made from these two sets?Proceeding in a very orderly manner, we can see that there will be 6distinct pairs as given below:

(red, b), (red, c), (red, ), (blue, b), (blue, ), (blue, ).

Thus, we get 6 distinct objects (Fig 2.1).

Let us recall from our earlier classes that an ordered pair of elements taken from any two sets P and Q is a pair of elements written in small 

<div style="text-align: center;"><img src="imgs/img_in_image_box_736_1052_858_1198.jpg" alt="Image" width="13%" /></div>


<div style="text-align: center;">Fig 2.1</div>


brackets and grouped together in a particular order, i.e.,$(p,q),p\in\mathrm{P}\mathrm{~a n d~}q\in\mathrm{Q}$ .This leads to the following definition:

Definition 11 Given two non-empty sets P and Q. The cartesian product $\mathbb{P}\times\mathbb{Q}$ is the set of all ordered pairs of elements from P and Q, i.e.,

$$\mathrm{P}\times\mathrm{Q}=\{(p,q):p\in\mathrm{P},q\in\mathrm{Q}\}$$

If either P or Q is the null set, then $\mathbb{P}\times\mathbb{Q}$ ,will also be empty set, i.e.,$\mathrm{P}\times\mathrm{Q}=\phi$ 

From the ilustration given above we note that 

$$\mathrm{A}\times\mathrm{B}=\{(\mathrm{red},b),(\mathrm{red},c),(\mathrm{red},s),(\mathrm{blue},b),(\mathrm{blue},c),(\mathrm{blue},s)\}$$

Again, consider the two sets:

$\mathrm{A}=\{\mathrm{DL},\ \mathrm{MP},\ \mathrm{KA}\}$ , where DL, MP, KA represent Delhi,Madhya Pradesh and Karnataka, respectively and $\mathrm{B}=\{01,02\}$ 03}representing codes for the licence plates of vehicles issued by DL, MP and KA .



Ifthe three states, Delhi, Madhya Pradesh and Karnataka were making codes for the licence plates of vehicles, with the restriction that the code begins with an element from set A which are the pairs availablefromthesesets and how many such pairs will there be (Fig 2.2)?



<div style="text-align: center;"><img src="imgs/img_in_image_box_670_394_862_585.jpg" alt="Image" width="20%" /></div>


<div style="text-align: center;">Fig 2.2</div>


The available pairs are:(DL,01), (DL,02),$(\mathrm{DL},03),(\mathrm{MP},01)$ 1, (MP,02), (MP,03),(KA,01), (KA,02), (KA,03) and the product of set A and set B is given by $\mathrm{A}\times\mathrm{B}=\{(\mathrm{DL},01)$ ), (DL,02), (DL,03),$(\mathrm{MP},01),(\mathrm{MP},02)$ ), (MP,03), (KA,01), (KA,02),(KA,03)}.



It can easily be seen that there will be 9 such pairs in the Cartesian product, since there are 3 elements in each of the sets A and B. This gives us 9 possible codes. Also note that theordr in whichtheselement are paied is crucia.For exampl, the code (DL, 01) will not be the same as the code (01, DL).



As a final illustration, consider the two sets $\mathrm{A}=\left\{a_{1},a_{2}\right\}$ and 

$$\begin{array}{l}\mathrm{B}=\{b_{1},b_{2},b_{3},b_{4}\},(\mathrm{Fig}2.3).\\\mathrm{A}\times\mathrm{B}=\{(a_{1},b_{1}),(a_{1},b_{2}),(a_{1},b_{3}),(a_{1},b_{4}),(a_{2},b_{1}),(a_{2},b_{2}),\\\quad(a_{2},b_{3}),(a_{2},b_{4})\}.\end{array}$$

The 8 ordered pairs thus formed can represent the position of points in the plane if A and B are subsets of the set of real numbers and it is obvious that the point in the position $(a_{1},b_{2})$ will be distinct from the point in the position $(b_{2},a_{1})$ 1.



## Remarks 

<div style="text-align: center;"><img src="imgs/img_in_image_box_749_915_865_1115.jpg" alt="Image" width="12%" /></div>


<div style="text-align: center;">Fig 2.3</div>


(i)Two ordered pairs are equal, if and only if thecorrespondingfirst lements are equal and the second elements are also equal.



(i)IftherearepelementsinAandelements in B,thenthere willbe q elements in $\mathrm{A}\times\mathrm{B},\mathrm{i.e.}$ ., if $n(\mathrm{A})=p and n(\mathrm{B})=q,$ _,then $n(\mathrm{A}\times\mathrm{B})=pq$ 

)InBeo-mtndiaintis 

$\mathrm{A}\times\mathrm{B}.$ 



(iv)$\mathrm{A}\times\mathrm{A}\times\mathrm{A}=\{(a,b,c):a,b,c\in\mathrm{A}\}$ . Here $(a,b,c)$ is called an ordered triplet.



Example 1 If $(x+1,y-2)=(3,1)$ , find the values of x and y.

 Solution Since the ordered pairs are equal, the corresponding elements are equal.

Therefore $x+1=3and y-2=1.$ 

Solving we get $x=2and y=3$ 

Example 2 If $\mathbb{P}=\{a,b,c\}$ and $\mathrm{Q}=\{r\}$ , form the sets $\mathrm{P}\times\mathrm{Q}_{\cdot}\mathrm{and}\mathrm{Q}\times\mathrm{P}$ 

Are these two products equal?

Solution By the definition of the cartesian product,

$$\mathbf{P}\times\mathbf{Q}=\{(a,r),(b,r),(c,r)\}\quad and\quad\mathbf{Q}\times\mathbf{P}=\{(r,a),(r,b),(r,c)\}S $$

S $(r,a)$ ,we conclude that $\mathrm{P}\times\mathrm{Q}\neq\mathrm{Q}\times\mathrm{P}$ 



However, the number of elements in each set will be the same.

Example 3 Let $\mathrm{A}=\{1,2,3\},\mathrm{B}=\{3,4\}\mathrm{and}\mathrm{C}=\{4,5,6\}$ .Find 

c (i))(i)$\begin{array}{l}\mathrm{A}\times(\mathrm{B}\cap\overline{\mathrm{C}})\\\mathrm{A}\times(\mathrm{B}\cup\mathrm{C})\end{array}$ (ii)$(\mathrm{A}\times\mathrm{B})\cap(\mathrm{A}\times\mathrm{C})$ $(\mathrm{A}\times\mathrm{B})\cup(\mathrm{A}\times\mathrm{C})$ 

Solution (i) By the definition of the intersection of two sets,$(B\cap C)=\{4\}$ 

Therefore,$\mathrm{A}\times(\mathrm{B}\cap\mathrm{C})=\{(1,4),(2,4),(3,4)\}$ 

$$\mathrm{Now}(\mathrm{A}\times\mathrm{B})=\{(1,3),(1,4),(2,3),(2,4),(3,3),(3,4)\}$$

$$\mathrm{and}_{\bar{C}}(\mathrm{A}\times\bar{\mathrm{C}})=\{(1,4),(1,5),(1,6),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6)\}$$

Therefore,$\left(\mathrm{A}\times\mathrm{B}\right)\cap\left(\mathrm{A}\times\mathrm{C}\right)=\left\{(1,4),(2,4),(3,4)\right\}$ 

(iii) Since,$(B\cup C)=\{3,4,5,6\}$ , we have 

$$\begin{array}{l}\mathrm{A}\times(\mathrm{B}\cup\mathrm{C})=\{(1,3),(1,4),(1,5),(1,6),(2,3),(2,4),(2,5),(2,6),(3,3),\\ \{(3,4),(3,5),(3,6)\}.\end{array}$$

(iv) Using the sets $ A\times B$ and $\mathrm{A}\times\mathrm{C}$ from part (ii) above, we obtain 

$$(\mathrm{A}\times\mathrm{B})\cup(\mathrm{A}\times\mathrm{C})=\{(1,3),(1,4),(1,5),(1,6),(2,3),(2,4),(2,5),(2,6),$$

(3,3), (3,4), (3,5), (3,6)}.

Example 4 If $\mathrm{P}=\{1,2\}$ , form the set $\mathrm{P}\times\mathrm{P}\times\mathrm{P}$ 

Solution We have,$\mathrm{P}\times\mathrm{P}\times\mathrm{P}=\{(1,1,1)$ ,, (1,1,2), (1,2,1), (1,2,2), (2,1,1), (2,1,2), (2,2,1),司(2,2,2)}.



ExampleIfRiset ofal a $\mathbf{R}\times\mathbf{R}$ and $\mathbf{R}\times\mathbf{R}\times\mathbf{R}$ represent?



Solution The Cartesian product $\mathbf{R}\times\mathbf{R}$ represents the set $\mathbf{R}\times\mathbf{R}=\{(x,y):x,y\in\mathbf{R}\}$ which represents the coordinates of all the points in two dimensional space and the cartesian product $\mathbf{R}\times\mathbf{R}\times\mathbf{R}$ represents the set $\mathbf{R}\times\mathbf{R}\times\mathbf{R}=\{(x,y,z):x,y,z\in\mathbf{R}\}$ which represents the coordinates of all the points in three-dimensional ie Example $\mathrm{If}\mathrm{A}\times\mathrm{B}=\{(p,q),(p,r),(m,q),(m,r)\}$ c)id A and .

$$\begin{array}{l}\mathrm{A}=\mathrm{set of first elements}=\{p,m\}\\\mathrm{B}=\mathrm{set of second elements}=\{q,r\}\end{array}$$

## 1 

1.If $\left(\frac{x}{3}+1,y-\frac{2}{3}\right)=\left(\frac{5}{3},\frac{1}{3}\right)$ find the values of x f x and y.

2.If the set A has 3 elements and the set $\mathbf{B}=\{3,4,5\}$ , then find the number of elements in $(\mathrm{A}{\times}\mathrm{B})$ ).



3.$\mathrm{If}\;\mathrm{G}=\{7,8\}and\mathrm{H}=\{5,4,2\},\;\mathrm{find}\mathrm{G}\times\mathrm{H}and\mathrm{H}\times\mathrm{G}.$ 

4..State whether eachof thefollowing statements are trueor false.Ifthe statement is false, rewrite the given statement correctly.



(i)$\mathrm{If}\mathrm{P}=\{m,n\}$ and $Q=\{n,m\}$ ,then $\mathbb{P}\times\mathbb{Q}=\{(m,n),(n,m)\}$ 

(i) If A and B are non-empty sets, then $ A\times B$ is a non-empty set of ordered pairs $(x,y)$ such that $x\in\mathrm{A}\mathrm{and}y\in\mathrm{B}$ 



(i)$\mathrm{If}\;\mathrm{A}=\{1,2\},\;\mathrm{B}=\{3,4\}$ ,then $\mathrm{A}\times(\mathrm{B}\cap\phi)=\phi$ I 

5.$\mathrm{If}\;\mathrm{A}=\{-1,1\},\;\mathrm{find}\;\mathrm{A}\times\mathrm{A}\times\mathrm{A}.$ 

6.$\mathrm{If}\mathrm{A}\times\mathrm{B}=\{(a,x),(a,y),(b,x),(b,y)\}$ . Find A and B.

7. Let $A=\{1,2\}$ $\mathrm{B}=\{1,2,3,4\},\mathrm{C}=\{5,6\}$ and $\mathrm{D}=\{5,6,7,8\}$ . Verify that 

(i)$\mathrm{A}\times(\mathrm{B}\cap\mathrm{C})=(\mathrm{A}\times\mathrm{B})\cap(\mathrm{A}\times\mathrm{C}).(\mathrm{ii})\mathrm{A}\times\mathrm{C}$ is a subset of $\mathrm{B}\times\mathrm{D}$ 

8.Let $A=\{1,2\}$ and $\mathrm{B}=\{3,4\}$ .Write $\mathrm{A}\times\mathrm{B}$ . How many subsets will $\mathrm{A\times B\:have?}$ List them.



9.Let A and B be two sets such that $n(A)=3and n(B)=2.If(x,1),(y,2),(z,1)$ are in $\mathrm{A}\times\mathrm{B}$ , find A and B, where .$x,y$ and $z\;{\mathrm{are}}$ distinct elements.

10. The Cartesian product $ A\times A$ has 9 elements among which are found $(-1,0)$ and (0,1). Find the set A and the remaining elements of $ A\times A$ 

### 2.3 Relations 

Consider the two sets $\mathrm{P}=\{a,b,c\}$ and $\mathrm{Q}=\{\mathrm{Ali}$ , Bhanu, Binoy, Chandra, Divya}.

The cartesian product of 

P and Q has 15 ordered pairs which 

can be listed as $\mathbb{P}\times\mathbb{Q}=\{(a,\mathrm{Ali})\}$ 1,

(a, Bhanu),$(a,\mathrm{Binoy}),...,(c,\mathrm{Divya})\}$ 

We can now obtain a subset of $ P\times Q$ by introducing a relation R between the first element x and the second element y of each ordered pair $(x,y)$ as 



<div style="text-align: center;"><img src="imgs/img_in_image_box_442_287_862_512.jpg" alt="Image" width="44%" /></div>


$\mathbb{R}=\left\{(x,y)\right.$ :T ame y $x\in\mathrm{P},y\in\mathrm{Q}\}$ 

Then $\mathbb{R}=\{(a,\mathrm{Ali})\}$ , (b, Bhanu), (b, Binoy),$(c,{\mathrm{Chandra}})\}$ 1

A visual representation of this relation R (called an ar diagram) is shown in Fig 2.4.



Definition 22Arelation Rfrom a non-emptysetAto a non-empty setBis a subset of the cartesian product $\mathrm{A}\times\mathrm{B}$ .The subset is derived by describing a rlationship between the first element and the second element of the ordered pairs in $\mathrm{A}\times\mathrm{B}$ . The second element is called the image of the first element.



Definition 33he setofalirstlementsoftheorderedpairsinrlationRrom a set A to a set B is called the domain of the relation R.



DefinitionTheetofllcondlemetsinarelationRomaetAtoset Bis called the range of the relation R.The wholeset B is called thecodomain of the relation R. Note that range C codomain.



Remarks (i)ArelationmayberepresentealgebraicallyitherbytheRoser method or by the Set-builder method.



(i)An arrow diagram is a visual representation of a relation.

Example 7$\mathrm{LetA}=\{1,2,3,4,5,6\}$ .Define a relation R from A to A by 

$$\mathbb{R}=\{(x,y):y=x+1\}$$

(i)Depict this relation using an arrow diagram.

(ii) Write down the domain, codomain and range of R.

Solution(i)Bythe definitionoftherelation,

$$\mathbb{R}=\left\{(1,2),(2,3),(3,4),(4,5),(5,6)\right\}.$$

The corresponding arrow diagram is shown in Fig 2.5.



(ii) We can see that the 

$\mathrm{domain}=\{1,2,3,4,5,\}$ 

Similarly, the $\mathrm{range}=\{2,3,4,5,6\}$ and the codomair $\mathbf{n}=\{1,2,3,4,5,6\}$ 

Example 8 The Fig 2.6 shows a relation 

<div style="text-align: center;"><img src="imgs/img_in_image_box_488_137_897_325.jpg" alt="Image" width="43%" /></div>


<div style="text-align: center;">Fig 2.5</div>


between the sets P and Q.Writethis relation (i) in set-builderform, (ii) in roser form What is its domain and range?P 

<div style="text-align: center;"><img src="imgs/img_in_image_box_484_412_865_617.jpg" alt="Image" width="40%" /></div>


<div style="text-align: center;">ig2.6</div>


Solution It is obvious that the relation R is $^{\ast}x$  is the square of $ y^{\text{"}}$ .



(i) In set-builder form,$\mathbb{R}=\{(x,y):x$ is the square of $\{y,x\in\mathbb{P},y\in\mathbb{Q}\}$ (ii) In roster form,$\mathbb{R}=\{(9,3)$ 

(9, −3), (4, 2), (4,−2), (25, 5) (25

The domain of this relation is {4, 9, 25

The range of this relation is $\{-2,2,-3,3,-5,5\}$ 

Note thattheelement1 is notrelatedto any eleme in set P.

The set Q is the codomain of this relation.

Notehetotal numbrofrlations thatcanbedefined om asetAto a set B is the number of possible subsets $\mathrm{A}\times\mathrm{B}.\mathrm{If}n(\mathrm{A})=p\mathrm{and}n(\mathrm{B})=q$ then $n\left(\mathrm{A}\times\mathrm{B}\right)=pq$ and the total numberofrelations is 2

Example 9 Let $\mathrm{A}=\{1,2\}$ and $\mathrm{B}=\{3,4\}$ . Find the number of relations from A to B. Solution We have,

$$\mathrm{A}\times\mathrm{B}=\{(1,3),(1,4),(2,3),(2,4)\}.$$

Since $n(A\times B)=4$ the number of subsets of $\mathrm{A}\times\mathrm{B}$ is 24. Therefore, the number of relations from A into B will be 24.



Remark  A relation R from A to A is also stated as a relation on A.

### EXERCISE 2.2

1.Let $\mathrm{A}=\{1,2,3,\ldots,14\}$ Define a relation Rfrom AtoAby $\mathbb{R}=\{(x,y):3x-y=0$ , where x,$y\in\mathrm{A}\}$ . Write down its domain, codomain and range.



2.Define a relation R on the set N of natural numbers by $\mathbb{R}=\{(x,y):y=x+5$ x is a natural number less than $4;x,y\in\mathbf{N}\}$ . Depict this relationship using roster form. Write down the domain and the range.



3.$\mathrm{A}=\{1,2,3,5\}$ and $\mathrm{B}=\{4,6,9\}$ . Define a relation R from A to B by $\mathbb{R}=\{(x,y)$ : the difference between x and y is odd;$x\in\mathrm{A},y\in\mathrm{B}\}$ J. Write R in roster form.E 

<div style="text-align: center;"><img src="imgs/img_in_image_box_467_327_856_537.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">Fig </div>


The Fig2.7 shows a relationship between the sets P and Q. Write this relation 



(i) in set-builder form (i) roster form.What is its domain and range?

5.Let $\mathrm{A}=\{1,2,3,4,6\}$ .Let R be the relation on A defined by EM 

$\{(a,b):a,b\in\mathrm{A}$ , b is exactly divisible by ivisible by a}

(i)Write R in roster form 

(ii)Find the domain of R 

(ii)Find the range of R.

6.Determine the domain and range the relation R defined by $\mathbb{R}=\left\{(x,x+5):x\in\{0,1,2,3,4,5\}\right\}$ a..7.$\mathrm{Write}the relation\mathbb{R}=\{(x,\bar{x}^3)$ :x is a prime number less than 10} in roster form 8.Let $\mathrm{A}=\{x,y,z\}\text{and}\mathrm{B}=\{1,2\}$ . Find the number of relations from A to B.

9.Let R be the relation on Z defined by $\mathbb{R}=\{(a,b):a,\;b\in\mathbb{Z},a-b$ is an integer}.Find the domain and range of R.



### 2.4 Functions 

In this Section, we study a special type of relation called function. It is one of the most important concepts in mathematics. We can, visualise a function as a rule, which produces new elements out of some given elements. There are many terms such as 'map'or 'mapping'used to denote a function.



Definition 5relation  from a set A to a set B is said to be a function if every element of set A has one and only one image in set B.



In other words, a function f is a relation from a non-empty set A to a non-empty set B such that the domain of f is A and no two distinct ordered pairs inf have the same first element.



Iff is a function from A to B and $(a,b)\in f,$ then $f(a)=b$ ,where b is called the image of a under  and a is called the preimage of b under f.

Tefuco Ta $ A\Rightarrow B$ ,

not a function because the element 6 has no image.



Again, the relation in Example 8 is not a function because the elements in the domain are connectedto more than one images.Similarly, the relation in Example 9 is also not a function. (Why?) In the examples given below, we will see many more relations some of which are functions and others are not.



Example 10 Let N be the set of natural numbers and the relation R be defined on N such that $\mathbb{R}=\{(x,y):y=2x,x,y\in\mathbf{N}\}$ 



What is the domain, codomain and range of R? Is this relation a function?

Solution The domain of R is the set of natural numbers N. The codomain is also N.The range is the set of even natural numbers.



Since every natural number  has one and only one image,this relation is a function.



Example11Examineeachofthefollowingrelationsgivenbelowand state in each case, giving reasons whether it is a function or not?



$$\begin{array}{ll}(\mathrm{i})&\mathrm{R}=\{(2,1),(3,1),(4,2)\},(\mathrm{ii})\mathrm{R}=\{(2,2),(2,4),(3,3),(4,4)\}\\ (\mathrm{iii})&\mathrm{R}=\{(1,2),(2,3),(3,4),(4,5),(5,6),(6,7)\}\end{array}$$

Solution (i)Since 2, 3, 4 are the elements of domain of R having their unique images,this relation R is a function.



(ii)Since the same first element 2 corresponds to two different images 2and 4, this relation is not a function.



(i)Since every element hasone and only one image, this relation is a function.



Definition 6Afunction which haseither R or one of its subsets as its range is called a real valued function. Further, if its domain is also either R or a subset of R, it is called a real function.



<div style="text-align: center;">Example 12 Let N be the set of natural numbers. Define a real valued function $f:\mathrm{N}\rightarrow\mathrm{N}\ by f(x)=2x+1$ . Using this definition, complete the table given below.</div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>x</td><td></td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>y</td><td>|f (1)=</td><td>$f(2)=\ldots$</td><td>f (3) = .</td><td>|f (4) = ..</td><td>$f(5)=\ldots$</td><td>$f(6)=\ldots$</td><td>$f(7)=\ldots$</td></tr></table></body></html></div>


<div style="text-align: center;">Solution The completed table is given by </div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>x</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>y</td><td>$f(1)=3$</td><td>$f(2)=5$</td><td>$f(3)=7$</td><td>$f(4)=9$</td><td>$f(5)=11$</td><td>$f(6)=13$</td><td>$f(7)=15$</td></tr></table></body></html></div>


#### 2.4.1 Some functions  and their graphs 

(i)Identity function Let R be the set of real numbers. Define the real valued function $f:\mathbf{R}\rightarrow\mathbf{R}by y=f(x)=x$ for each $x\in\mathbb{R}$ . Such a function is called the identity function. Here the domain and range $\mathrm{of}f\mathrm{are}\mathbb{R}$ . The graph is a straight line as shown in Fig 2.8. It passes through the origin.



<div style="text-align: center;"><img src="imgs/img_in_image_box_260_301_660_726.jpg" alt="Image" width="42%" /></div>


(ii)Constant function Define the function f.$$ where where c is a constant and each 2$x\in\mathbb{R}$ Here domain of is R and its range is $\{c\}$ 

$$f(x)=3$$

The graph is a line parallel to x-axis. For example,$\mathrm{if}f(x)=3$ for each $x\in\mathbb{R}$ ,then its graph will be a line as shown in the Fig 2.9.



(i) Polynomial function A function_$f\colon\mathbb{R}\to\mathbb{R}$ is said to be polynomial function if for each x in $\mathbf{R},y=f(x)=a_{0}+a_{1}x+a_{2}x^{2}+\ldots+a_{n}x^{n}$ , where n is a non-negative integer and $a_{0},a_{1},a_{2},...,a_{n}\in\mathbb{R}$ -F 

The functions defined by $f(x)=x^{3}-x^{2}+2$ , and $g(x)=x^4+\sqrt{2}$ x are some examples 

of polynomial functions, whereas the function h defined by $h(x)=x^{\frac{2}{3}}+2x$ is not a polynomial function.$(Why?)$ 



Example13 Define the function $f:\mathbf{R}\rightarrow\mathbf{R}\text{by}y=f(x)=x^{2},x\in\mathbf{R}$ . Complete the Tableon Draw the graph of f.




<div style="text-align: center;"><html><body><table border="1"><tr><td>x</td><td>-4</td><td>-3</td><td>-2</td><td>-1</td><td>0</td><td>1</td><td>2</td><td></td><td></td></tr><tr><td>$y=f(x)=x^{2}$</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table></body></html></div>


Solution The completed Table is given below:


<div style="text-align: center;"><html><body><table border="1"><tr><td>x</td><td>-4</td><td>-3</td><td>-2</td><td></td><td>0</td><td></td><td>2</td><td>3</td><td>4</td></tr><tr><td>$y=f(x)=x^{2}$</td><td>16</td><td>9</td><td></td><td>1</td><td>0</td><td></td><td>4</td><td>9</td><td>16</td></tr></table></body></html></div>


by Fig 2.10Domain of ,$f=\{x:x\in\mathbb{R}\}$ . Range of f $\{x\in\mathbb{R}\}$ The graph of f is given 

$$f(x)=x^{2}$$

Example 14 Draw the graph of the function $\boldsymbol{f}:\mathbb{R}\rightarrow\mathbb{R}$ defined by $f(x)=x^{3},x\in\mathbf{R}$ Solution We have 





$f(0)=0,f(1)=1,f(-1)=-1,f(2)=8,f(-2)=-8,f(3)=27;f(-3)=-27,\mathrm{etc}.$ (ci)$f=\{(x,x^3):x\in\mathbb{R}\}$ .

Y 

The graph of is given in Fig 2.1.

$$CERT f(x)=x^3$$

(iv) Rational functions are functions of 1CERX ${\frac{f(x)}{g(x)}}$ ,where $f(x)$ and $g(x)$ are polynomial functions of x defined in a domain, where $g(x)\neq0$ 

Example 15 Define the real valued function $f\colon\mathbf{R}-\{0\}\to\mathbf{R}$ defined by $f(x)=\frac{1}{x}$ $x\in\mathbb{R}-\{0\}$ Complete the Table givenbelow using this definition.What isthe domain and range of this function 




<div style="text-align: center;"><html><body><table border="1"><tr><td>x</td><td>>-2</td><td>-1.5</td><td>-1</td><td>-0.5</td><td>0.25</td><td>0.5</td><td>1</td><td>1.5</td><td>2</td></tr><tr><td>$y=\frac{1}{x_{0}}$</td><td></td><td></td><td></td><td>…</td><td>…</td><td>…</td><td>…</td><td></td><td>.</td></tr></table></body></html></div>


<div style="text-align: center;">Solution The completed Table is given by </div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>x</td><td>-2</td><td>-1.5</td><td>-1</td><td>-0.5</td><td>0.25</td><td>0.5</td><td>1</td><td>1.5</td><td>2</td></tr><tr><td>$y={\frac{1}{x}}$</td><td>-0.5</td><td>-0.67</td><td>-1</td><td>-2</td><td>4</td><td>2</td><td>1</td><td>0.67</td><td>0.5</td></tr></table></body></html></div>


The domainiallrealnumbersexceptanditangeisaloallreal numbers except 0. The graph off is given in Fig 2.12.



<div style="text-align: center;"><img src="imgs/img_in_image_box_249_195_643_597.jpg" alt="Image" width="42%" /></div>


$$f(x)=\frac{1}{x}$$

<div style="text-align: center;">Fig2.12</div>


$f_{\cdot}\mathbb{R}{\rightarrow}\mathbb{R}$ $x\in\mathbb{R}$ (v)non-neg $f_{\cdot}\mathbb{R}{\rightarrow}\mathbb{R}$ is defined by ,$f(x)=|x|$ $x,f(x)$ is equal to x.$f(x)=|x|$ hef befmetion for dc 有But for negative values of x, the value of $f(x)$ is the negative of the value of x, i.e,

$$f(x)=\left\{\begin{aligned}x,&x\geq0\\ -x,&x<0\end{aligned}\right.$$

The graph of the modulus function is given in Fig 2.13



(vi) Signum function The function $f_{:}\mathbf{R}{\rightarrow}\mathbf{R}$ defined by 



$$f(x)=\left\{\begin{aligned}&1,if x>0\\ &0,if x=0\\ &-1,if x<0\end{aligned}\right.$$

$$f(x)=|x|$$

<div style="text-align: center;">Fig 2.13</div>


the set s $\{-1,0,1\}$ 

$$y=1$$

$$f(x)=\frac{\left|x\right|}{x},x\in\mathbf{0}and\mathbf{0}for x=0$$

<div style="text-align: center;">Fig 2.14</div>


by The function $f(x)=[x],x\in\mathbf{R}$ ction.$f_{\cdot}\;\mathbb{R}\rightarrow\mathbb{R}$ as assum uch a fu  d ,..

can see that x], we 

$$\begin{aligned}&\left[x\right]=-1\ for\ -1\leq x<0\\&\left[x\right]=\ 0\ for\ 0\leq x<1\\&\left[x\right]=\ 1\ for\ 1\leq x<2\\&\left[x\right]=\ 2\ for\ 2\leq x<3\ and\\ \end{aligned}$$

so on.

The graph of the function is shown in Fig $2.15$ 



$$f(x)=[x]$$

<div style="text-align: center;">Fig 2.15</div>


2.4.2Algebraof real functions In this Section, we shall learn how to add two real functions, subtract a real function from another, multiply a real function by a scalar (here by a scalar we mean a real number), multiply two real functions and divide one real function by another.



(i)Addition of two real functions Let $f\colon\mathrm{X}\to\mathbb{R}$ and $g:\mathrm{X}\to\mathbb{R}$ .be any two real functions, where $X\subset\mathbb{R}$ . Then, we define $(f^{+}g)\colon\mathrm{X}\to\mathbb{R}$ by 

$(f+g)(x)=f(x)+g(x)$ ,for all $x\in\mathrm{X}$ 

(ii) Subtraction of a real function from another $\mathrm{Let}f:\mathrm{X}\to\mathbb{R}\ and\ g:\mathrm{X}\to\mathbb{R}$ be any two real functions, where $\vec{X}\subset\mathbb{R}$ .. Then, we define $(f-g):\mathrm{X}\to\mathbb{R}$ by $(f-g)(x)=f(x)-g(x)$ ,for all $x\in\mathrm{X}$ 



(imi) Multiplication by a scalar Let f :$\mathtt{X}\rightarrow\mathbf{R}$ be a real valued function and α be a scalar. Here by scalar, we mana real number.Then the product $\alpha f$ is a function from X to R defined by $(\alpha f)(x)=\alpha f(x),x\in\mathrm{X}$ 



(iv) Multilication of two ral functions The product (or mulilicatio) oftwo real functions $f_{:}\mathrm{X}{\rightarrow}\mathbb{R}$ and $g{:}\mathbb{X}{\to}\mathbb{R}$ is a function $f_{}{g}{:}\mathrm{{X}{\to}\mathbb{R}}$ defined by $(f g)(x)=f(x)g(x)$ ,for all $x\in X$ O 

This is also called pointwise multiplication.

(v) Quotient of two real functions Let and g be two real functions defined from 

$\mathrm{X}\to\mathbb{R}$ , where $\vec{X}\subset\mathbb{R}$ $\left[\frac{f}{g}\right.]$ is a function defined by ,ubli 

$$\left(\frac{f}{g}\right)(x)=\frac{f(x)}{g(x)}\quad\text{provided}g(x)\neq0,x\in X $$

Example 16 Let $f(x)=x^{2}\mathrm{and}\;g(x)=2x+1$ be two real functions.Find 

$$(f+g)(x),(f-g)(x),(f-g)(x),\left(\frac{f}{g}\right)(x).Solution We have.(U)
$$

Solution We have.(U)

$$Solution We have.(U)
\begin{aligned}&f(x)=x^{2}+2x+1,\quad(f-g)(x)=x^{2}-2x-1,\\&f(f)(x)=x^{2}(2x+1)=2x^{3}+x^{2},\quad\left(\frac{f}{g}\right)(x)=\frac{x^{2}}{2x+1},\quad x\neq-\frac{1}{2}.\\ \end{aligned}$$

Example 17$\mathrm{Let}f(x)=\sqrt{x}\mathrm{and}g(x)=x$ be two functions defined over the set of non



$(f+g)(x),(f-g)(x),(fg)(x)\bmod\left(\frac{f}{g}\right)(x).$ 

Solution Wehave 

$$(f+g)(x)=\sqrt{x}+x,\quad(f-g)(x)=\sqrt{x}-x,\quad(f\cdot g)(x)=\sqrt{x}\cdot x\bmod\left(\frac{f}{g}\right)(x).$$

### EXERCISE 2.3

1.Which of the following relations are functions? Give reasons. If it is a function,determine its domain and range.



(i){(2,1), (5,1), (8,1), (11,1), (14,1), (17,1)}

(ii) {(2,1), (4,2), (6,3), (8,4), (10,5), (12,6), (14,7)}

(i) {(1,3), (1,5), (2,5}.

2.Find the domain and range of the following real functions:

(i)

$$f(x)=-\left|x\right|$$

(ii)

$$f(x)=\sqrt{9-x^{2}}.$$

3.A function  is defined by $f(x)=2x-5$ . Write down the values of 

(i)$f(0)$ ,(ii)$f(7)$ ,(ii)$f(-3)$ 

4.$^{\ast}t^{\ast}$ 

degree Fahrenheit is defined by $t(C)=\frac{9C}{5}+32$ 



Find (i)(0)(ii)  t(28) (ii)$t(-10)\ (\mathrm{iv})$ The value o of C, when $t(C)=212$ 

5.Find the range of each of the following functions.

(i)

$$f(x)=2-3x,x\in\mathbb{R},x>0.$$

(ii)$f(x)=x^{2}+2$ ,x is a real number.

(ii)$f(x)=x$ ,x is a real number.

## Miscellaneous Examples 

Example18 Let R be the set of real numbers.

Define the real function 

$$f_{\cdot}\mathbf{R}\rightarrow\mathbf{R}\mathrm{by}f(x)=x+10$$

and sketch the graph of this function.

Solution Here $f(0)=10,f(1)=11,f(2)=12,$ 

$f(10)=20,\quad\mathrm{e}^{\frac{\pi}{2}}=\frac{\pi}{2}$ 



$$f(-1)=9,f(-2)=8,\ldots,f(-10)=0and so on.$$

e e ee ae ee e eeeee aee e e se e re a r e 

a ee e ar $f(x)=mx+c$ $x\in\mathbf{R}$    r r e  r re   e  r e  n function.



$$f(x)=x+10$$

<div style="text-align: center;">Fig 2.16</div>


Example19 Let R be a relation from Q to Q defined by $\mathbb{R}=\{(a,b):a,b\in\mathbb{Q}$ and $a-b\in\mathbf{Z}\}$ J. Show that 



(i)$(a,a)\in\mathbb{R}\;{\mathrm{for}}\;{\mathrm{all}}\;a\in\mathbb{O}$ 

(ii)$(a,b)\in\mathbb{R}$ implies that $(b,a)\in\mathbb{R}$ 

(ii)$(a,b)\in\mathbb{R}\;\mathrm{and}\;(b,c)\in\mathbb{R}$ implies that $(a,c)\in\mathbb{R}$ 

Solution (i) Since,$a-a=0\in\mathbf{Z}$ , if follows that $(a,a)\in\mathbb{R}$ 

(ii)$(a,b)\in\mathbb{R}implies that a-b\in\mathbb{Z}.So,b-a\in\mathbb{Z}$ . Therefore,

$(b,a)\in\mathbb{R}$ 



(im)$(a,b)and(b,c)\in\mathbb{R}$ implies that $a-b\in\mathbf{Z}.b-c\in\mathbf{Z}$ So,

$$a-c=(a-b)+(b-c)\in\mathbf{Z}.Therefore,(a,c)\in\mathbf{R}$$

Example 20$\mathrm{Let}f=\{(1,1),(2,3),(0,-1),(-1,-3)\}$ be a linear function from Z into Z.Find $f(x)$ .



Solution Since f is a linear function,$f(x)=mx+c$ . Also, since $(\mathbb{L},\mathbb{I})_{s}(0,-1)\in\mathbb{R}$ 

$$f(1)=m+c=1and f(0)=c=-1.This gives m=2and f(x)=2x-1$$

Example 21 Find the domain of the function $f(x)=\frac{x^{2}+3x+5}{x^{2}-5x+4}$ 

Solution Since $x^{2}-5x+4=(x-4)(x-1)$ , the function  is defined for all real numbers except at $x=4and x=1$ . Hence the domain $\mathrm{of}f\mathrm{is}\mathbb{R}-\{1,4\}$ 

Example 22 The function is defined by 

$$f(x)=\begin{cases}1-x,\;x<0\\1-x>0\end{cases}O $$

Draw the graph of $f(\underline{x})_{\bar{x}}$ 

Solution Here,$f(x)=1-x,x<0$ ,this gives 

$$f(-4)=1-(-3)=4,\quad f(-2)=1-(-2)=3$$

$$f(-1)=1-(-1)=2;\mathrm{e}^{-1}$$

and $f(1)=2,f(2)=3,f(3)=4$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_515_797_865_1209.jpg" alt="Image" width="37%" /></div>


<div style="text-align: center;">Fig 2.17</div>


$f(4)=5$ and so on for $f(x)=x+1,x>0$ 

Thus, the graph off is as shown in Fig 2.17

## Miscellaneous Exercise on Chater 2

1. The relation  is defined y $f(x)=\left\{\begin{aligned}x^{2},0\leq x\leq3\\3x,3\leq x\leq10\end{aligned}\right.$ 

The relation g is defined by $g(x)=\left\{\begin{aligned}x^{2},&0\leq x\leq2\\3x,&2\leq x\leq10\end{aligned}\right.$ 

Show thatf is a function and g is not a function.

2.$\mathrm{If}f(x)=x^2$ , find $\frac{f(1.1)-f(1)}{(1.1-1)}$ 

3. Find the domain of the function $f(x)=\frac{x^{2}+2x+1}{x^{2}-8x+12}$ 

d c $f(x)=\sqrt{(x-1)}$ ,

5.Find the domain and the rangeof the real function defined by $f(x)=\left|x-1\right|$ 

6. Let $f=\left\{\left(x,\frac{x^{2}}{1+x^{2}}\right):x\in\mathbf{R}\right\}$ a function om R into R. Determine the range of f.



7. Let $f,g:\mathbb{R}\to\mathbb{R}$ be defined, respectively by $f(x)=x+1,\;g(x)=2x-3$ . Find 

$f+g,f-g{\mathrm{~a n d~}}{\frac{f}{g}}$ 



8.Let $f=\left\{(1,1),(2,3),(0,-1),(-1,-3)\right\}$ be a function from Z to Z defined by $f(x)=ax+b$ , for some integers a, b. Determine a, b.

9. Let R be a relation fromN to N defined by $\mathbb{R}=\left\{(a,b):a,b\in\mathbb{N}\text{and}a=b^{2}\right\}$ .Are the following true?



(i)$(a,a)\in\mathbb{R},for all a\in\mathbb{N}$ (ii)$(a,b)\in\mathbb{R}, 须项 (b,a)\in\mathbb{R}$ (iii)$(a,b)\in\mathbb{R},(b,c)\in\mathbb{R}$ implies $(a,c)\in\mathbb{R}$ 



Justify your answer in each case.

10. Le1$\mathrm{tA}=\{1,2,3,4\},\mathrm{B}=\{1,5,9,11,15,16\}$ and $f=\left\{(1,5),(2,9),(3,1),(4,5),(2,11)\right\}$ Are the following true?



(i)f is a relation from A to B (ii)  is a function from A to B.Justify your answer in each case.



11. Let f be the subset of $\mathbf{Z}\times\mathbf{Z}$ defined by $f=\{(ab,a+b):a,b\in\mathbf{Z}\}$ .Is $f\textsf{a}$ (c function from Z to Z? Justify your answer.



12. Let $\mathrm{A}=\{9,10,11,12,13\}$ and letf :$\mathrm{A}{\rightarrow}\mathbf{N}$ be defined by.$f(n)=\mathrm{the}$ highest prime factor of n. Find the range of f.



## Summary 

In this Chapter, we studied about relations and functions.The main features of this Chapter are as follows:

 Ordered pairApairofelements grouped togetherina particular order.

Cartesian product $\mathbf{A}\times\mathbf{B}$ of two sets A and B is given by 

$$\mathrm{A}\times\mathrm{B}=\left\{(a,b):a\in\mathrm{A},b\in\mathrm{B}\right\}$$

In particular $\mathbf{R}\times\mathbf{R}=\{(x,y):x,y\in\mathbf{R}\}$ 

and $\mathbf{R}\times\mathbf{R}\times\mathbf{R}=\{(x,y,z):x,y,z\in\mathbf{R}\}$ 

$\mathrm{If}(a,b)=(x,y)$ then $a=x$ and $b=\bar{y}.$ 

If $n(\mathrm{A})=p$ and $n(\mathrm{B})=q$ then $n(A\times B)=pq$ 

$$\mathbf{A}\times\mathbf{\phi}=\mathbf{\phi}$$

In general,$\mathrm{A}\times\mathrm{B}\neq\mathrm{B}\times\overline{{\mathrm{A}}}$ 

Relation A relation R from a set $\mathrm{\bar{t}\mathbf{o},\mathbf{a}}$ set B is a subset of the cartesian product $\mathbf{A}\times\mathbf{B}$ obtained by describing a relationship between the first element x and the second element y of the ordered pairs in $\mathrm{A}\times\mathrm{B}$ 

cY 

Teao $$ relation R.



The range of the relation R is the set of all second elements of the ordered pairs in a relation R.



Function A functionffrom a setAto a setBis a specific typeofrelation for which every element x of set A has one and only one image y in set B.

We write f:$\mathrm{A{\rightarrow}B}$ , where $f(x)=y$ 

A is the domain and B is the codomain off.

The range ofthe functionis theset ofimages.

A real function has the set of real numbers or one of its subsets both as its domain and as its range.



Algebra of functions For functions $f\colon\mathrm{X}\to\mathbb{R}\mathrm{~a n d~}g\colon\mathrm{X}\to\mathbb{R}$ we have 

$$\begin{aligned}&f(f+g)(x)=f(x)+g(x),x\in X\\&f(f-g)(x)=f(x)-g(x),x\in X\\&f(f.g)(x)\quad=f(x).g(x),x\in X\\&g(kf)(x)\quad=k(f(x)),x\in X,where k is a real number.\\&\left(\frac{f}{g}\right)(x)=\frac{f(x)}{g(x)},x\in X,g(x)\neq0\\ \end{aligned}$$

## Historical Note 

The word FUNCTIONfirst appears in a Latin manuscript““Methodus tangentium inversa, seu de fuctionibus" written by Gottfried Wilhelm Leibitz (1646-1716) in 1673; Leibnitz used the word in the non-analytical sense. He considered a function in terms of"mathematical job"the “employee”being just a curve.



OnJuly5,698,ohanBernoulliinaleter to]Leibnitz,for the first time deliberately assigned a specialised use of the term function in the analytical sense. At the end of that month, Leibnitz replied showing his approval.

Function is found in English in 1779in Chambers'Cyclopaedia:“The term functionis used in algbra,for ananalytical exprssionany waycompounded avariablequantityandom quantities".

<div style="text-align: center;"><img src="imgs/img_in_image_box_141_937_527_1143.jpg" alt="Image" width="41%" /></div>
