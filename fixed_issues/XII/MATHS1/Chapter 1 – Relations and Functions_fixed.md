

# RELATIONS AND FUNCTIONS

.There is no permanent place in the world for ugly mathematics ... . It may be very hard todefine mathematical beauty but that is just as true of beauty of any kind, we may not know quite what we mean by a beautiful poem, but that does not prevent us from recognising one when we read it. — G. H. HARDY :

### 1.1 Introduction

Recall that the notion of relations and functions, domain,co-domain and range have been introduced in Class XI along with different types of specific real valued functions and their graphs. The concept of the term 'relation'in mathematics has been drawn from the meaning of relation in English language, according to which two objects or quantities are related if there is a recognisable connection or link between the two objects or quantities. Let A be the set of students of Class XII of a school and B be the set of students of Class XI of the same school. Then some of the examples of relations from A to B are

(i)$\{(a,b)\in A\times B}$ : a is brother of b},

(ii)$\{(a,b)\in\mathrm{A}\times\mathrm{B}}$ : a is sister of b},

<div style="text-align: center;"><img src="imgs/img_in_image_box_633_518_884_857.jpg" alt="Image" width="26%" /></div>

<div style="text-align: center;">Lejeune Dirichlet (1805-1859)</div>

(i)$\{(a,b)\in\mathrm{A}\times\mathrm{B}}$ :age of a is greater than age of b},

(iv)$\{(a,b)\in\mathrm{A}\times\mathrm{B}}$ : total marks obtained by a in the final examination is less than the total marks obtained by b in the final examination},

(v)$\{(a,b)\in\mathbf{A}^{\times}\mathbf{B}\}$ a lives in the same locality as b}. However, abstracting from this, we define mathematically a relation R from A to B as an arbitrary subset of $\mathbf{A}\times\mathbf{B}$ .

If $(a,b)\in\mathbb{R}$ , we say that a is related to b under the relation R and we write as a Rb.Ingeneral,$(a,b)\in\mathbb{R}$ , we do not bother whether there is a recognisable connection or link between a and b. As seen in Class XI, functions are special kind of relations.

In this chapter, we will study diferent types ofrelations and functions, composition of functions, invertible functions and binary operations.

## MATHEMATICS

### 1.2 Types of Relations

In this section, we would liketostudy dferent typesof relations.Weknowthat a relation in a set A is a subset of $\mathrm{A}\times\mathrm{A}$ . Thus, the empty set φ and $\mathrm{A}\times\mathrm{A}$ are two extreme relations. For ilustration, consider a relation R in the set $A=\{1,2,3,4\}$ given by $\mathbb{R}=\left\{(a,b):a-b=10\right\}$ .This is the empty set, as no pair $(a,b)$ satisfies the condition $a-b=10$ .Similarly,$\mathbb{R}'=\{(a,b):|a-b|\geq0\}$ is the whole set $\mathbf{A}\times\mathbf{A}$ , as all pairs (a, b) in $\mathrm{A}\times\mathrm{A}$ satisfy $\left|\;a-b\;\right|\geq0$ . These two extreme examples lead us to the following definitions.

Definition 1 A relation R in a set A is called empty relation, if no element of A is related to any element of A, i.e.,$\mathbb{R}=\phi\subset\mathbb{A}\times\mathbb{A}$

Definition 2 Arelation R in a set A is called universal relation, if each element of A is related to every element of A, i.e.,$\mathbb{R}=\mathbb{A}\times\mathbb{A}$

Both the empty relation and the universal relation are some times called trivial relations.

Example 1 Let A be the set of all students of a boys school. Show that the relation R in A given by $\mathbb{R}=\{(a,b)}$ : a is sister of $\left.b\right\$ is the empty relation and $\mathbb{R}^{\prime}=\{(a,b)}$ :the differencebetweenheightsofaandis lessthan3meters}is theuniversal relation.Solution incetheschool isboyschoolostudentofthechoolcanbesisterof any student of the school. Hence,$R=\phi$ showing that R is the empty relation. It is also obvious tt teetwitoanotdt ote hl has o b less than 3 meters. This shows that $\mathbb{R}'=\mathbb{A}\times\mathbb{A}$ is the universal relation.

Remark In Class XI, we have seen two ways of representing a relation, namely raster methodandtbuildrmethod.Howeve,rlationRinteet{1,2,3,4}defi $\{(a,b):b=a+1\}$ is also expressed as a R b if and only if $b=a+1$ by many authors. We may also use this notation, as and when convenient.

If $(a,b)\in\mathbb{R}$ , we say that a is related to b and we denote it as a R b.

One of the most important relation, which plays a significant role in Mathematics,is an equivalence relation. To study equivalence relation, we first consider three types of relations, namely reflexive, symmetric and transitive.

Definition 3 A relation R in a set A is called

(i)reflexive, if $(a,a)\in\mathbb{R}$ , for every $a\in\mathrm{A}$ ,

(ii) symmetric, if $(a_{1},a_{2})\in\mathbb{R}$ . implies that $(a_{2},a_{1})\in\mathbb{R}$ , for all $a_{1},a_{2}\in\mathrm{A}$

(i) transitive, if $\left(a_{1},a_{2}\right)\in\mathbb{R}\mathrm{and}\left(a_{2},a_{3}\right)\in\mathbb{R}$ implies that $(a_{1},a_{3})\in\mathbb{R}$ , for all $a_{_1},a_{_2},$

$a_{_3}\in\mathrm{A}$

Definition 4 A relation R in a set A is said to be an equivalence relation if R is reflexive, symmetric and transitive.

Example2etTbthesetofalltriangleiaplaewithRrelationinTiveny $\mathbb{R}=\left\{\left(\mathrm{T}_{1},\mathrm{T}_{2}\right):\mathrm{T}_{1}\right.}$ is congruent to $\left.\mathrm{T}_{2}\right\$ .Show that R is an equivalence relation.

Solution R is reflexive, since every triangle is congruent to itself. Further,$\left(\mathrm{T}_{1},\mathrm{T}_{2}\right)\in\mathbb{R}\Rightarrow\mathrm{T}_{1}$ is congruent to $\mathrm{T}_{2}\rightrightarrows\mathrm{T}_{2}$ is congruent to $\mathrm{T}_{1}\rightrightarrows\left(\mathrm{T}_{2},\mathrm{T}_{1}\right)\in\mathbb{R}$ . Hence,R is symmetric. Moreover,$\left(\mathrm{T}_{1},\mathrm{T}_{2}\right),\left(\mathrm{T}_{2},\mathrm{T}_{3}\right)\in\mathbb{R}\Rightarrow\mathrm{T}_{1}$ is congruent to $\mathrm{T}_{2}$ and $ T_{2}$ is congruent to $\mathrm{T}_{3}\rightrightarrows\mathrm{T}_{1}$ is congruent to $\mathrm{T}_{3}\rightrightarrows\left(\mathrm{T}_{1},\mathrm{T}_{3}\right)\in\mathbb{R}$ .Therefore, R is an equivalence relation.

ExampleetLbthesetofall lineinaplaneandRbetherelationinLdefed as $\mathbb{R}=\{(\mathrm{L}_1,\mathrm{L}_2):\mathrm{L}_1}$ is perpendicular to $\left.\mathrm{L}_{2}\right\$ . Show that R is symmetric but neither reflexive nor transitive.

$ L_{t}$ $(\mathrm{L}_{1},\mathrm{L}_{1})$ $\notin\mathbb{R}.$ . R is symmetric as $(\mathrm{L}_1,\mathrm{L}_2)\in\mathbb{R}$ $\mathbf{L}_{3}$ $\begin{array}{ccc}\Rightarrow&&L_1is perpendicular to L_2\\Rightarrow&&L_2is perpendicular to L_1\\Rightarrow&&(L_2,L_1)\in\mathbb{R}.\end{array}$ $\mathbf{L}_{2}$

$\mathbf{L}_{t}$

R is not transitive. Indeed,$\mathrm{if}\underline{{\mathrm{L}}}_{1}$ is perpendicular to $\mathrm{L}_{2}$ and $ L_{2}$ is perpendicular to $ L_{3}$ then $\mathrm{L}_{\mathrm{r}}$ can never be perpendicular to

<div style="text-align: center;">Fig 1.1</div>

$ L_{3}$ .In fact,$\mathrm{L}_{\mathrm{r}}$ is parallel to $\mathrm{L}_{3}$ , i.e.,$(\mathrm{L}_{1},\mathrm{L}_{2})\in\mathrm{R},(\mathrm{L}_{2},\mathrm{L}_{3})\in\mathrm{R}\mathrm{but}(\mathrm{L}_{1},\mathrm{L}_{3})\notin\mathrm{R}$

Example 4 Show that the relation R in the set {1, 2, 3} given by $\mathbb{R}=\{(1,1),(2,2)}$ $(3,3),(1,2),(2,3)\$ is reflexive but neither symmetric nor transitive.

Slt as $(1,2)\in\mathbb{R}\;\mathrm{but}(2,1)\notin\mathbb{R}$ .Similarly, R is not transitive, as $(1,2)\in\mathbb{R}\;\mathrm{and}(2,3)\in\mathbb{R}$ but $(1,3)\notin\mathbb{R}$

Example 5 Show that the relation R in the set Z of integers given by

$$\mathbb{R}=\{(a,b):2\text{divides}a-b\}$$

is an equivalence relation.

Solution R is reflexive, as 2 divides $(a-a)$ for all $a\in\mathbf{Z}$ . Further, if $(a,b)\in\mathbb{R}$ ,then 2 divides $a-b$ . Therefore, 2 divides $b-a$ . Hence,$(b,a)\in\mathbb{R}$ , which shows that R is symmetric. Similarly, if $(a,b)\in\mathbb{R}$ .and $(b,c)\in\mathbb{R},$ ,then $a-b$ and $b-c$ are divisible by 2. Now,$a-c=(a-b)+(b-c)$ is even (Why?). So,$(a-c)$ is divisible by 2. This shows that R is transitive. Thus, R is an equivalence relation in Z.

In Example 5, note that all even integers are related to zero, as $(0,\pm2),(0,\pm4)$ etc., lie in R and no odd integer is related to 0, as $(0,\pm1),(0,\pm3)$ etc., do not lie in R.Similarly, all odd integers are relatedto one and no even integer is related to one.Therefore,the et Eofall evenintegers andthe etOofallodd integers are subsets of Z satisfying following conditions:

(i)All elementsofEarerelatedtoachother and alllementsofOare elaed to each other.

(ii)NoelementofEisrlatedtoanyelementofOandvicevera.

(i) E and O are disjoint and $\mathbf{Z}=\mathbf{E}\cup\mathbf{O}$

The subset E is called the equivalence class containing zero and is denoted by ].il $[0]\neq[1],[0]=[2r]\mathrm{and}[1]=[2r+1],r\in\mathbf{Z}$ . Infact, what we have seen above is true for an arbitrary equivalence relation R in a set X. Given an arbitrary equivalence rlall $ A_{i}$ called partitions or subdivisions of X satisfying:

(i) all elements of $\mathrm{^{i}A}_{i}$ are related to each other, for $\mathrm{all}i_{i}$

(ii) no element of $\mathrm{^{i}A_{i}}$ is related to any element of $\mathrm{A}_{i},\bar{i}\neq\bar{j}.$

(iii)$\cup\mathrm{A}_{i}=\mathrm{X}\text{and}\mathrm{A}_{i}\cap\mathrm{A}_{j}=\phi_{i}i\neq j.$

The subsets $ A_{_{i}}$ reall is that we can go reverse also. For example, consider a subdivision of the set Z given by three mutually disjoint subsets $\mathrm{A}_{1},\mathrm{A}_{2}$ and $\underline{{\mathrm{A}}}_{3}$ whose union is Z with

$$\begin{aligned}&\mathrm{A}_{1}=\{x\in\mathbf{Z}:x\text{is a multiple of}3\}=\{\ldots,-6,-3,0,3,6,\ldots\}\\&\mathrm{A}_{2}=\{x\in\mathbf{Z}:x-1\text{is a multiple of}3\}=\{\ldots,-5,-2,1,4,7,\ldots\}\\&\mathrm{A}_{3}=\{x\in\mathbf{Z}:x-2\text{is a multiple of}3\}=\{\ldots,-4,-1,2,5,8,\ldots\}\\ \end{aligned}$$

Define a relation R in Z given by $\mathbb{R}=\{(a,b)}$ : 3 divides $\left.\begin{aligned}a-b\end{aligned}\right\$ .Following the arguments similar to those used in Example 5, we can show that R is an equivalence relation.$\mathrm{Also},\mathrm{A}_{\mathrm{i}}$ coincides with the set of all integers in Z which are related to zero,$ A_{2}$ coincides with thesetofallintegers whicharerelatedo1 and $ A_{3}$ coincides with the set of all integers in Z which are related to 2. Thus,$A_{1}=[0],A_{2}=[1]and A_{3}=[2]$ In fact,$A_{1}=[3r],A_{2}=[3r+1]\text{and}A_{3}=[3r+2]$ ,for all $r\in\mathbf{Z}$

Example 6 Let R be the relation defined in the set $\mathrm{A}=\{1,2,3,4,5,6,7\}$ by $\mathbb{R}=\{(a,b)}$ :both a and b are either odd or even}. Show that R is an equivalence relation. Further, show that all the elements of the subset $\{1,3,5,7\}$ are related to each other and all the elements of the subset{2, 4, 6} are related to each other, but no elementofthesubset{1,,5,7}isrlatedtoanylementoftheubset{2,,6

Solution Given any element a in A, both a and a must be either odd or even, so that $(a,a)\in\mathbb{R}$ .Further,$(a,b)\in\mathbb{R}\Rightarrow$ both a and b must be either odd or even $\Rightarrow(b,a)\in\mathbb{R}$ .Similarly,$(a,b)\in\mathbb{R}$ and $(b,c)\in\mathbb{R}\Rightarrow$ all elements a, , , must be either even or odd simultaneousl $\mathrm{y}\rightrightarrows(a,c)\in\mathbb{R}$ .. Hence, R is an equivalence relation.Further,allthelementsof{1,3,5,7}arerelatedtoeachother,asalltheelements ofthis subsetareodd.Similarly,alltheelementsofthesubset{2,4,6} arerelatedto each other, as allofthem are even.Also,no elementof the subset {1,3,5,7} can be relatedtoanyelementof{2,4,6}, aselementsof{1,3,5,7} areodd,whileelements of {2, 4, 6} are even.

### EXERCISE 1.1

1. Determine whether each of the following relations are reflexive, symm trind transitive:

(i) Relation R in the set $A=\{1,2,3,\ldots,13,14\}$ defined as

$$\mathbb{R}=\left\{(x,y):3x-y=0\right\}$$

(ii) Relation R in the set N of natural numbers defined as

$$R=\{(x,y):y=x+5and x<4\}$$

(i) Relation R in the set $\mathrm{A}=\{1,2,3,4,5,6\}\text{as}$

$$\mathrm{R}=\left\{(x,y):y\text{is divisible by}x\right\}$$

(iv) Relation R in the set Z of all integers defined as

$$\mathbb{R}=\{(x,y):x-y is an integer\}$$

(

(a)$\mathbb{R}=\{(x,y)}$ : x and y work at the same place}

(b)$\mathbb{R}=\{(x,y)}$ :x and y live in the same locality}

(c)$\mathbb{R}=\{(x,y):x}$ is exactly 7 cm taller than y}

(d)$\mathbf{R}=\{(x,y)}$ : x is wife of y}

(e)$\mathbb{R}=\{(x,y):x is rather of y\}$

2. Show thattherlationRin the set Rof real numbers,defined as

$\mathbb{R}=\left\{(a,b):a\leq b^{2}\right\}$ is neither reflexive nor symmetric nor transitive.

3. CheckwhrtherlationRdefinedintheet{1,,3,45,}a

$\mathbb{R}=\left\{(a,b):b=a+1\right\}$ is reflexive, symmetric or transitive.

4. Show that the relation R in R defined as $\mathbb{R}=\{(a,b):a\leq b\}$ , is reflexive and transitive but not symmetric.

5. Check whether the relation R in Rdefined by $\mathbb{R}=\left\{(a,b):a\leq b^{3}\right\}$ is reflexive,symmetric or transitive.

6. ShowthattherelationRintheset{1,2,3}gvenby $\mathbb{R}=\left\{(1,2),(2,1)\right\}$ is symmetric but neither reflexive nor transitive.

7. Show thattherlationRinthe setAof allthebooks inalibraryofacollege,given by $\mathbb{R}=\{(x,y)}$ :x and y have same number of pages} is an equivalence relation.

8. Showthat telation Rin te et $\mathrm{A}=\{1,2,3,4,5\}$ given by

$\mathbb{R}=\{(a,b):|a-b|}$ is even}, is an equivalence relation. Show that all the elements of $\{1,3,5\}$ are related to each other and all the elements of {2, 4} are related toeachother.But noelementof{1,3,5} is related to any elementof {2, 4}9.Show that each of the relation R in the set $\mathrm{A}=\{x\in\mathbf{Z}:0\leq x\leq12\}$ ,given by

(i)$\mathbb{R}=\{(a,b):|a-b|}$ is a multiple of 4}

(ii)$\mathbb{R}=\{(a,b):a=b\}$

is an equivalence relation. Find the set of all elements related 1ineach case.

10. Give an example of a relation. Which is

(i)Symmetric but neither reflexive nor transitive.

(i) Transitive but neither reflexive nor symmetric

(ii) Reflexive and symmetric but not transitive.

(iv) Reflexive and transitive but not symmetric.

(v) Symmetric and transitive but not reflexive.

11. Show that the relation R in the set A of points in a plane givenby $\mathbb{R}=\{(\mathbb{P},\mathbb{Q})}$ :distance of the point P from the origin is same as the distance of the point Qfromtheorigin},is an equivalence relation.Further, show thatthe set of all points related to a point $\mathbb{P}\neq(0,0)$ is the circle passing through P with origin as centre.

12. Show that the relation R defined in the set A of all triangles as $\mathbb{R}=\{(\mathrm{T}_1,\mathrm{T}_2):\mathrm{T}_1}$ 1is similar to $\{\mathrm{T}_2\}$ ,is equivalence relation. Consider three right angle triangles $\mathrm{T}_{\mathrm{r}}$ with sides 3, 4, 5,$\mathrm{T}_{2}$ with sides 5, 12, 13 and $\mathrm{T}_{3}$ with sides 6, 8, 10.Which triangles among $ T_{1},T_{2}$ and $ T_{3}$ are related?

13. Show that the relation R defined in the set A of all polygons as $\mathbb{R}=\left\{\left(\mathrm{P}_{1},\mathrm{P}_{2}\right)\right.}$ $\mathrm{P}_{\mathrm{~l~}}$ and $\mathrm{P}_{2}$ have same number of sides}, is an equivalence relation. What is the set of all elements in A related to the right angle triangle T with sides 3,4 and 5?14. Let L be the set of all lines in XY plane and R be the relation in L defined as $\mathbb{R}=\left\{\left(\mathrm{L}_{1},\mathrm{L}_{2}\right):\mathrm{L}_{1}\right\}$ is parallel to $ L_{2}\$ .Show that R is an equivalence relation. Find the set of all lines related to the line $y=2x+4$ "

15. Let Rbtherlationintheet{1,,3,4}ivn $\mathbb{R}=\left\{(1,2),(2,2),(1,1),(4,4)\right\}$ (1, 3), (3, 3), (3, 2)}.Choose thecorect answer.

(A) R is reflexive and symmetric but not transitive.

(B) R is reflexive and transitive but not symmetric.

(C) R is symmetric and transitive but not reflexive.

(D)R is an equivalence relation.

16. Let R be the relation in the set N given by $\mathbb{R}=\left\{(a,b):a=b-2,b>6\right\}$ J. Choose the correct answer.

$$\left(A\right)(2,4)\in R\quad\left(B\right)(3,8)\in R\quad\left(C\right)(6,8)\in R\quad\left(D\right)(8,7)\in R $$

### 1.3 Types of Functions

The notiono a funi alog wth ome spial funns lie iity functi tion, constant function,olomlun,aldium.along with their graphs have been given in Class XI.

Addition, subtraction, multiplication and division oftwo functions have also been studied. As the concept of function is of paramount importance in mathematics and among other disciplines as wll, we wouldliketoextendour study aboutfunctiofom where we finished earlier. In this section, we would like to study different types of functions.

Consider the functions $f_{1},f_{2},f_{3}$ and $f_{4}$ given by the following diagrams.

InFi2,eo o $\mathrm{{^{\prime}X_{\tau}}}$ under the function $f_{1}$ are distinct,uheimaeofwoditictlmetsand2of $\mathrm{X}_{\mathrm{r}}$ under $f_{2}$ is same,namely $b$ . Further, there are some elements like e and $f\mathrm{in}\mathrm{X}_{2}$ which are not images of any element of $\mathrm{X}_{\mathrm{r}}$ under $f_{1}$ ,while all elements of $\mathrm{X}_{3}$ are images of some elements of $\mathrm{{^{\prime}X}_{\mathrm{_t}}}$ |under $f_{3}$ . The above observations lead to the following definitions:

Definition 5 A function $f:\mathrm{X}\to\mathrm{Y}$ is defined to be one-one (or injective), if the images of distinct elements of X under $f$ are distinct, i.e., for every $x_{1},x_{2}\in\mathrm{X},f(x_{1})=f(x_{2})$ implies $x_{1}=x_{2}$ Otherwise,f is called many-one.

The function $f_{4}$ and $f_{4}$ in Fig 1.2 (i) and (iv) are one-one and the function $f_{2}$ and $f_{3}$ in Fig 1.2 (ii) and (iii) are many-one.

Definition 6 A function f :$\mathrm{X}{\rightarrow}\mathrm{Y}$ is said to be onto (or surjective), if every element of Y is the image of some element of X under $f_{z}$ i.e., for every $y\in\mathrm{Y},$ , there exists an element x in X such that $f(x)=y$

The function $f_{3}$ and $f_{4}$ in Fig 1.2 (iii), (iv) are onto and the function $f_{1}$ in Fig 1.2 (i) is not onto as elements $e,f\mathrm{in}\mathrm{X}_{_2}$ are not the image of any element in $\mathrm{X}_{\mathrm{_1}}$ under $f_{1}$ .

<div style="text-align: center;"><img src="imgs/img_in_image_box_66_141_857_673.jpg" alt="Image" width="84%" /></div>

<div style="text-align: center;">Fig </div>

Remark $f\colon\mathrm{X}\to\mathrm{Y}$ is onto if and only if Range $f=\mathrm{Y}$

Definition7 A function $f\colon\mathrm{X}\to\mathrm{Y}$ is said to be one-one and onto (or bijective), if f is both one-one and onto

The function $f_{4}$ in Fig 1.2(iv) is one-one and ono.

Example7Let Abethe setofall50 students of Class Xin a school. Let $f:\mathrm{A}\rightarrow\mathrm{N}$ be function defined by $f(x)=\mathrm{roll}$ number of the student x. Show that is one-one but not onto.

 Solution No two different students of the class can have same roll number. Therefore,f must be one-one. We can assume without any loss of generality that roll numbers of students are from 1 to 50.This implies that 51 in Nis not roll number of any student of the class, so that 5l can not be image of any element of X under f. Hence, f is not onto.Example 8 Show that the function $f\colon\mathbf{N}\rightarrow\mathbf{N},$ given by $f(x)=2x$ , is one-one but not onto.

Solution The functionf is one-one, for $f(x_{1})=f(x_{2})\Rightarrow2x_{1}=2x_{2}\Rightarrow x_{1}=x_{2}$ .Further,f is not onto, as for $1\in\mathbf{N}$ ,there does not exist any x in N such that $f(x)=2x=1$

Example 9 Prove that the functionf:$\mathbf{R}\rightarrow\mathbf{R},\text{given by}f(x)=2x$ , is one-one and onto.Solution f is one-one, as $f(x_{1})=f(x_{2})\Rightarrow2x_{1}=2x_{2}\Rightarrow x_{1}=x_{2}$ . Also, given any real number y in R, there exists $\frac{y}{2}$ in R such that $f(\frac{y}{2})=2\cdot(\frac{y}{2})=y$ . Hence, f is onto.

$$y=f(x)=2x $$

<div style="text-align: center;">Fig Fig1.31.3</div>

for every Example $x>2$ ,is onto but not one-one.how that the functionf:$\mathbf{N}\rightarrow\mathbf{N}$ ,$$ 不

Solution f is not one-one, as $f(1)=f(2)=1$ -Butf is onto, as given any.$$ we can choose x as $y\pm1$ such that $f(y+1)=y+1-1=y$ .Also for $1\in\mathbf{N},$ we have $f(1)=1$

Example 11 Show that the functionf:$\mathbb{R}\rightarrow\mathbb{R}$ defined as $f(x)=x^{2}$ , is neither one-one nor onto.Solution Since $f(-1)=1=f(1)$ ,f is not oneone. Also, the element – 2 in the co-domain R is not image of any element x in the domain R $(\mathrm{W h y?})$ . Therefore f is not onto.

Example 12 Show that $f\colon\mathbf{N}\to\mathbf{N}$ ,given by

$$f(x)=\begin{aligned}&x+1,if x is odd,\\ &x-1,if x is even.\end{aligned}$$

is both one-one and onto.

$$f(x)=x^{2}$$

$$\mathrm{X}\stackrel{f(-1)=1}{\longleftarrow}$$

$$x=-1$$

<div style="text-align: center;">The image of 1 and −1 under f is 1.</div>

<div style="text-align: center;">Fig 1.4</div>

Solution Suppose $f(x_{1})=f(x_{2})$ .Note that $\mathrm{if}x_{1}$ is odd and (cid:1)$x_{2}$ is even, then we will have $x_{1}+1=x_{2}-1,i.e.,x_{2}-x_{1}=2$ which is impossible. Similarly, the possibility $\mathrm{of}x_{\mathrm{t}}$ being even and $x_{2}$ being odd can also be ruled out, using the similar argument. Therefore,both $x_{\mathrm{r}}$ and $x_{2}$ must be either odd or even. Suppose both $x_{\mathrm{r}}$ and $x_{2}$ are odd. Then $f(x_{1})=f(x_{2})\Rightarrow x_{1}+1=x_{2}+1\Rightarrow x_{1}=x_{2}$ . Similarly, if both $x_{\mathrm{r}}$ and $x_{2}$ are even, then also $f(x_{1})=f(x_{2})\Rightarrow x_{1}-1=x_{2}-1\Rightarrow x_{1}=x_{2}$ . Thus, f is one-one. Also, any odd number $2r\dot{+}1$ in the co-domain N is the image of $\bar{2}r+2$ in the domain N and any even number 2r in the co-domain N is the image of $2r-1$ in the domain N. Thus,f is onto.

Example 13 Show that an onto function $f\colon\{1,2,3\}\to\{1,2,3\}$ is always one-one.

Solution Supposef is not one-one. Then there exists two elements, say 1 and 2 in the domain whose image in the co-domain is same. Also, the image of 3 under f can be only one element. Therefore, the range set can have at the most two elements of the co-domain {1,2,3}, showingthatf is not onto, a contradiction.Hence,must be one-one.Example 14 Show that a one-one function $f:\{1,2,3\}\to\{1,2,3\}$ must be onto.

Solution Since f is one-one, three elements of $\{1,2,3\}$ must be taken to 3 different elements of the co-domain {1, 2, 3} under f. Hence, has to be onto.

Remark The results mentioned in Examples 13 and 14 are also true for an arbitrary finite set X, i.e., a one-one function $f:X\to X$ is necessarily onto and an onto map $f\colon X\to X$ is necessarily one-one,for every finite set X. In contrast to this, Examples 8and 10 showthat for aninfinite ,this may not betrue.Infacthis is a characteristic difference between a finite and an infinite set.

### EXERCISE 1.2

1. Show that the function $f:\mathbb{R}_{\bullet}\rightarrow\mathbb{R}_{\bullet}$ defined by $f(x)=\frac{1}{x}$ is one-one and onto,where $\mathbb{R}_{\bullet}$ isl $\mathbf{R}_{\bullet}$ is replaced byN with co-domain being same as $\mathbf{R}_{\bullet}?$

2. Check the injectivity and surjectivity of the following functions:

(i)$f\colon\mathbf{N}\to\mathbf{N}$ given by $f(x)=x^{2}$

(ii) $f\mathbf{:Z}\rightarrow\mathbf{Z}$ given by $f(x)=x^{2}$

(ii $f:\mathbf{R}\to\mathbf{R}given by f(x)=x^2$

(iv)$f:\mathbf{N}\rightarrow\mathbf{N}given by f(x)=x^3$

(v) .$f\colon\mathbf{Z}\to\mathbf{Z}$ given by $f(x)=x^{3}$

3. Prove that the Greatest Integer Functionf :$\mathbb{R}\rightarrow\mathbb{R}$ , given by $f(x)=[x]$ , is neither one-one nor onto, where [x] denotes the greatest integer less than or equal to x. 4. Show that the Modulus Function $f\colon\mathbb{R}\to\mathbb{R}$ ,given by $f(x)=|x|$ ,is neither oneone nor onto, where $\left\|x\right\|$ isx,if istiver0n $\left|x\right|\mathrm{is}-x,$ ,if x is negative.5. Show that the Signum Function $f\colon\ensuremath{\mathbb{R}}\to\ensuremath{\mathbb{R}},$ , given by

$$f(x)=\left\{\begin{aligned}&1,if x>0\\ &0,if x=0\\ &1,if x<0\end{aligned}\right.}$$

is neither one-one nor onto.

6. Let $\mathrm{A}=\{1,2,3\},\mathrm{B}=\{4,5,6,7\}$ and let $f=\left\{(1,4),(2,5),(3,6)\right\}$ be a function from A to B. Show thatf is one-one.

7. Ineachoftheollowincases,state whetherthefunctionisone-oneonor bijective. Justify your answer.

$$(i)$f\colon\mathbf{R}\to\mathbf{R}$defined by$f(x)=3-{\bar{4}}x$ $$

(ii) $f\colon\mathbf{R}\to\mathbf{R}$ defined by $f(x)=1+x^{2}$

8. Let A and B be sets. Show that $f:\mathrm{A}\times\mathrm{B}\rightarrow\mathrm{B}\times\mathrm{A}$ $f(a,b)=(b,a)$ is bijective function.

9. Let $f\colon\mathbf{N}\to\mathbf{N}$ be defined by.$f(n)=\left\{\begin{aligned}&\frac{n+1}{2},if n is odd\\&\frac{n}{2},if n is even\end{aligned}\right.for all n\in\mathbf{N}}$

State whether the function f is bijective. Justify your answer.

10. Let $\mathrm{A}=\mathrm{R}-\{3\}and\mathrm{B}=\mathrm{R}-\{1\}$ .Consider the function $f\colon\mathrm{A}\to\mathrm{B}$ defined by $f(x)=\left(\frac{x-2}{x-3}\right)$ . Is f one-one and onto? Justify your answer.

11. Let $f:\mathbb{R}\rightarrow\mathbb{R}$ be defined as $f(x)=x^4$ . Choose the correct answer.

(A) f is one-one onto (B) f is many-one onto

(C) f is one-one but not onto (D) f is neither one-one nor onto.

12. Let $f\colon\mathbf{R}\to\mathbf{R}$ be defined as $f(x)=3x$ . Choose the correct answer.

(A) f is one-one onto (B) f is many-one onto

(C) f is one-one but not onto (D) f is neither one-one nor onto.

### 1.4 Composition of Functions and Invertible Function

Definition 8$\mathrm{Let}f\colon\mathrm{A}\to\mathrm{B}$ and $g:\mathrm{B}\rightarrow\mathrm{C}$ be two functions. Then the composition of f and g, denoted by gof, is defined as thefunction gof:$ A\rightarrow C$ given by

$$g o f(x)=g(f(x)),\forall x\in\mathrm{A}.$$

<div style="text-align: center;"><img src="imgs/img_in_image_box_96_321_851_495.jpg" alt="Image" width="80%" /></div>

<div style="text-align: center;">Fig 1.5</div>

Example 15 Letf :functions defined as $\{2,3,4,5\}\rightarrow\{3,4,5,9\}$ $f(2)=3,f(3)=4,f(4)=f(5)=5$ and $g:\{3,4,5,9\}\to\{7,11}$ $f(2)=3,f(3)=4,f(4)=f(5)=5$ $g(3)=g(4)=7$ 5},and $g(5)=g(9)=11$ . Find gof.

Solution We have $g o f(2)=g(f(2))=g(3)=7,g o f(3)=g(f(3))=g(4)=7$

$g o f(4)=g(f(4))=g(5)=11\mathrm{and}g o f(5)=g(5)=11$

Example 16 Find gof and fog,$\mathrm{if}f:\mathbb{R}\rightarrow\mathbb{R}$ and $g:\mathbb{R}\to\mathbb{R}$ are given by $f(x)=\cos x$ and $g(x)=3x^2$ Show that $g o f\neq f o g$

Solution We have $g o f(x)=g(f(x))=g(\cos x)=3(\cos x)^2=3\cos^2$ x. Similarly,$f o g(x)=f(g(x))=f(3x^2)=\cos(3x^2)$ D.Note that $3\cos^{2}x\ne\cos3x^{2},\quad for x=0$ . Hence,

$\it{g o f}\neq\it{f o g}$

Definition 9 A fuctionf:$\mathrm{X\rightarrow Y}$ is defined to be invertible, if there exists a function $g\colon\mathrm{Y}\to\mathrm{X}$ such that $g o f=\mathrm{I}_{\mathrm{x}}\mathrm{and}f o g=\mathrm{I}_{\mathrm{y}}$ . The function g is called the inverse of f and is denoted by $if^{-1}$

Thus, if f is invertible, then f must be one-one and onto and conversely, if f is one-one and onto, thenf must be invertible. This fact significantly helps for proving a functionf to be invertible by showing thatf is one-one and onto, specially when the actual inverse off is not to be determined.

Example $\mathbb{17}\mathrm{Let}f:\mathbf{N}\to\mathbb{Y}$ be a function defined as $f(x)=4x+3$ , where,

$\mathbf{Y}=\{y\in\mathbf{N}:y=4x+3}$ for some $x\in\mathbf{N}\$ . Show that f is invertible. Find the inverse.

Solution Consider an arbitrary element y of Y. By the definition of $y=4x+3$ 3

for some x in the domain N. This shows that $x=\frac{(y-3)}{4}$ Define $g:\mathrm{Y}\rightarrow\mathbf{N}$ by

$$g\left(y\right)=\frac{\left(y-3\right)}{4}.\;\;\mathrm{Now},\;\;\mathrm{go}f\left(x\right)=g\left(f\left(x\right)\right)=g\left(4x+3\right)=\frac{\left(4x+3-3\right)}{4}=x\;\;\mathrm{and}\;$$

$$f\left(g\left(y\right)=f\left(g\left(y\right)\right)=f\left(\frac{\left(y-3\right)}{4}\right)=\frac{4\left(y-3\right)}{4}+3=y-3+3=y\right) . This shows that $$

$$gf=\mathrm{I}_{\mathrm{N}} ,$$

and $\mathrm{I}f o g=\mathrm{I}_{\mathrm{v}}$ which imlithtiiianitein

## Miscellaneous Examples

Example 18 If $\mathbb{R}_{\mathrm{r}}$ and $ R_{2}$ a $R_{1}\cap R_{2}$ is also an equivalence relation.

Solution Since $\mathbb{R}_{\mathrm{r}}$ and $\mathbb{R}_{2}$ are equivalence relations,$(a,a)\in\mathbb{R}_1,\mathrm{and}(a,a)\in\mathbb{R}_2\forall a\in\mathbb{A}$ This implies that $(a,a)\in\mathbb{R}_1\cap\mathbb{R}_2$ $\forall a$ ,showing $\mathbb{R}_{1}\cap\mathbb{R}_{2}$ is reflexive. Further,$(a,b)\in\mathbb{R}_{1}\cap\mathbb{R}_{2}\Rightarrow(a,b)\in\mathbb{R}_{1}$ and $(a,b)\in\mathbb{R}_2\Rightarrow(b,a)\in\mathbb{R}_1$ and $(b,a)\in\mathbb{R}_2\Rightarrow$ $(b,a)\in\mathbb{R}_1\cap\mathbb{R}_2$ ,hence,$\mathbb{R}_{1}\cap\mathbb{R}_{2}$ is symmetric. Similarly,$(a,b)\in\mathbb{R}_1\cap\mathbb{R}_2$ and $(b,c)\in\mathbb{R}_{1}\cap\mathbb{R}_{2}\Rightarrow(a,c)\in\mathbb{R}_{1}$ and $(a,c)\in\mathbb{R}_2\Rightarrow(a,c)\in\mathbb{R}_1\cap\mathbb{R}_2$ . This shows that $\mathbb{R}_{1}\cap\mathbb{R}_{2}$ is transitive. Thus,$\mathbb{R}_{1}\cap\mathbb{R}_{2}$ is an equivalence relation.

Example19 Let R be a relation on the set A of ordered pairs of positive integers defined by $(x,y)\mathbb{R}(u,v)$ if and only $\mathrm{if}xv=vu_{\mathrm{c}}\mathrm{Show}$ that R is an equivalence relation.Solution Clearly,$(x,y)\mathbb{R}(x,y),\forall(x,y)\in\bar{A},$ ,since $x y=y x$ . This shows that R is reflexive. Further,$(x,y)\mathbb{R}(u,v)\Rightarrow xy=yu\Rightarrow uy=vx$ :and hence $(u,v)\mathrel{\mathrm{R}}(x,y)$ . This shows that R is symmetric. Similarly,$(x,y)\mathrm{R}\left(u,v\right)$ and $(u,v)\mathbb{R}(a,b)\Rightarrow xv=yu$ and $ub=via\Rightarrow xv\frac{a}{u}=yu\frac{a}{u}\Rightarrow xv\frac{b}{v}=yu\frac{a}{u}\Rightarrow xb=ya$ and hence $(x,y)\mathrm{\mathbb{R}}\left(a,b\right)$ .Thus, R is transitive. Thus, R is an equivalence relation.

Example20 Let $\mathrm{X}=\{1,2,3,4,5,6,7,8,9\}$ . Let $\mathbb{R}_{\mathrm{r}}$ be a relation in X given by $\mathbf{R}_{1}=\left\{(x,y):x-y\right.}$ is divisible by 3} and $\mathrm{R}_{2}$ be another relation on X given by $\mathrm{R}_{2}=\left\{(x,y):\left\{x,y\right\}\subset\{1,4,7\}\right\}\text{or}\{x,y\}\subset\{2,5,8\}\text{or}\{x,y\}\subset\{3,6,9\}\$ Show that 2

$\mathbb{R}_{1}=\mathbb{R}_{2}$

Solution Notethatthe characteristic of sets{1,4, 7},{2,5, 8} and{3,6,9}is that difference between any two elements of these sets is a multiple of 3. Therefore,$(x,y)\in\mathbb{R}_{1}\Rightarrow x-y$ is a multiple of $3\Rightarrow\{x,y\}\subset\{1,4,7\}{\mathrm{~o r~}}\{x,y\}\subset\{2,5,8\}$ or $\{x,y\}\subset\{3,6,9\}\Rightarrow(x,y)\in\mathbb{R}_{2}$ . Hence,$\mathbb{R}_{1}\subset\mathbb{R}_{2}$ . Similarly,$\{x,y\}\in\mathbb{R}_{2}\rightrightarrows\{x,y\}$ $\subset\{1,4,7\}or\{x,y\}\subset\{2,5,8\}or\{x,y\}\subset\{3,6,9\}\Rightarrow x-y$ is divisible by $3\Rightarrow\{x,y\}\in\mathbb{R}_{1}$ . This shows that $\mathbb{R}_{2}\subset\mathbb{R}_{1}$ . Hence,$\mathbb{R}_{1}=\mathbb{R}_{2}$ *

Example 21 Let f :$\mathrm{X}\to\mathrm{Y}$ be a function. Define a relation R in X given by $\mathbb{R}=\left\{(a,b):f(a)=f(b)\right\}$ Examine whether R is an equivalence relation or not.

Solution For every $a\in\mathrm{X},(a,a)\in\mathbb{R}$ , since $f(a)=f(a)$ , showing that R is reflexive.Similarly,$(a,b)\in\mathbb{R}\Rightarrow f(a)=f(b)\Rightarrow f(b)=f(a)\Rightarrow(b,a)\in\mathbb{R}$ . Therefore, R is symmetric. Further,$(a,b)\in\mathbb{R}$ .and $(b,c)\in\mathbb{R}\Rightarrow f(a)=f(b)$ and $f(b)=f(c)\Rightarrow f(a)$ $=f(c)\Rightarrow(a,c)\in\mathbb{R}$ , which implies that R is transitive. Hence, R is an equivalence relation.

Example 22 Find the number of all one-one functions from set $\mathrm{A}=\{1,2,3\}$ to itself.

Solution One-one function from {1, 2,3}to itself is simply a permutationon three symbols 1,2,3.Therefore, total numberofone-one maps from{1,2,3} to itself is same as total number of permutations on three symbols 1, 2, 3 which is $3!=6$

Example 23 Let $A=\{1,2,3\}$ |. Then show that the number of relations containing (1, 2)and (2,3)whicharerelexive andtranitivebutot ymmetristhr.

Solution ThesmallestrelationRcontaining(1,2)and(2,3)whichis relexive and trasie,,,,,,1,the pair (2, 1) to $\mathbb{R}_{\mathrm{r}}$ to get $\mathrm{R}_{2}$ hentherelation $\underline{{\mathbb{R}}}_{2}^{\circ}$ will be reflexive, transitive but not s $\mathbb{R}_{\mathrm{r}}$ to get the desird eltion.Howev, $\mathbb{R}_{\mathrm{_1}}$ at a time, as by doing ,will beordtoaddtemaiing pi itomitaiativity andinthe procss,thelaion will come symmric alsohichisot requi.hus,the total number of desired relations is three.

Example24Showthatthenumberofequivalencerelationintheset {1,2,}containing (1, 2) and (2, 1) is two.

Solution The smallest equivalence relation $\mathrm{R}_{\mathrm{r}}$ containing1,2)and(2,1)is{(1, 1),(2, 2), (3, 3),(1,2), (2, 1}.Now weare let withonly4 pairsnamely(2, 3), (3, 2),(1,)an,.I e,)$\mathbb{R}_{1},$ then for symmetry we must add (3,2) alsoand nowortranitivity wearefocedtoadd(1,3)and(3,1).Thus, thenly equivalencer $\mathbb{R}_{\mathrm{r}}$ i number of equivalence relations containing (1, 2) and (2, 1) is two.

Example 25 Consider the identity function $\mathrm{I}_{\mathrm{{}_{N}}}:\mathbf{N}\rightarrow\mathbf{N}$ defined as $\mathrm{I}_{\mathrm{N}}(x)=x\forall x\in\mathbf{N}$ Show that although $\mathrm{I}_{\mathrm{N}}$ is onto but $\mathrm{I}_{\mathrm{N}}+\mathrm{I}_{\mathrm{N}}:\mathrm{N}\rightarrow\mathrm{N}$ defined as

$$\left(\mathrm{I}_{\mathrm{N}}+\mathrm{I}_{\mathrm{N}}\right)(x)=\mathrm{I}_{\mathrm{N}}(x)+\mathrm{I}_{\mathrm{N}}(x)=x+x=2x is not onto $$

Solution Clearly $\mathrm{I}_{\mathrm{N}}$ is onto. But $ I_{N}+I_{N}$ is not onto, as we can find an element 3in the co-domain N such that there does not exist any x in the domain N with

$\left(\mathrm{I}_{\mathrm{N}}+\mathrm{I}_{\mathrm{N}}\right)(x)=2x=3$

Example 26 Consider a function $f:\left[0,\frac{\pi}{2}\right]\to\mathbf{R}$ given by $f(x)=\sin x$ and $g:\left[0,\frac{\pi}{2}\right]\rightarrow\mathbf{R}\text{given by}g(x)=\cos x$ . Show that f and g are one-one, but $f+g$ is not one-one.

Solutioiomts $x_{1}$ and $x_{2}\ln\left[0,\frac{\pi}{2}\right]$ , sin $x_{1}\ne\sin x_{2}$ and cos $x_{1}\neq\cos x_{2}$ , both f and g must be one-one. But $(f+g)(0)=\sin0+\cos0=1$ and $(f+g)\left(\frac{\pi}{2}\right)=\sin\frac{\pi}{2}+\cos\frac{\pi}{2}=1$ . Therefore,$f+g$

## Miscellaneous Exercise on Ch

1. Show that the function f:$\mathbf{R}\rightarrow\{x\in\mathbf{R}:-1<x<1\}$ defined by $f(x)=\frac{x}{1+|x|}$ $x\in\mathbb{R}$ is one one and onto function.

2. Show that the function $f:\mathbf{R}\rightarrow\mathbf{R}given by f(x)=x^3$ is injective.

3. Given a non empty set $\mathbf{X},$ consider $\mathbb{P}(\mathrm{X})$ which is the set of all subsets of X.Define the relation R in P(X) as follows:

For subsets A, B in P(X), ARB if and only $\mathrm{ifA\subset B}$ . Is R an equivalence relation on $\mathrm{P(X)?}$ Justify your answer.

4. Find the number of all onto functions from the set $\{1,2,3,\ldots\ldots,n\}$ to itself.

5. Let $\mathrm{A}=\{-1,0,1,2\},\mathrm{B}=\{-4,-2,0,2\}$ and $f,g:\mathrm{A}\to\mathrm{B}$ be functions defined by $f(x)=x^{2}-x,\;x\in A\;and\;\;g(x)=2\left|x-\frac{1}{2}\right|-1,\;x\in A$ . Are f and g equal?Justify your answer. (Hint: One may note that two functions $f\colon\mathrm{A\to B}$ and $g:\mathrm{A}\to\mathrm{B}$ such that $f(a)=g(a)\forall a\in\mathrm{A}$ , are called equal functions).

6. Let $A=\{1,2,3\}$ . Then number of relations containing (1, 2) and (1, 3) which are reflexive and symmetric but not transitive is

(B)2(C)3(D)4

7. Let $\mathrm{A}=\{1,2,3\}$ Teuoaons T (A)1(B)2(C)3(D)4

## Summary

In this chapter, we studied different typesof relations and equivalence relation,composition of functions, invertible functions and binary operations. The main f of this chapter are as follows:The main features

■Empty relation is the relation R in X given by $\mathbb{R}=\phi\subset\mathbb{X}\times\mathbb{X}$

Universal relation is the relation R in Xgiven by $\mathbb{R}=\mathbb{X}\times\mathbb{X}$

Reflexive relation R in X is a relation with $(a,a)\in\mathbb{R}\setminus\forall a\in\bar{X}.$

Symmetric relationRinXiarlationsatisfyng $(a,b)\in\mathbb{R}\text{implies}(b,a)\in\mathbb{R}$

国Transitive relation R in X is a relation satisfying $(a,b)\in\mathbb{R}$ and $(b,c)\in\mathbb{R}$ implies that $(a,c)\in\mathbb{R}$

■Equivalence relation RinX is a relation which is reflexive, symmetric and transitive.

■Equivalence class [a] containing $a\in\mathrm{X}$ for an equivalence relation R in X is the subset ofX containing all elements b related to a.

■A function $f:\mathrm{X}\rightarrow\mathrm{Y}$ is one-one (or injective) if

$$f(x_{1})=f(x_{2})\Rightarrow x_{1}=x_{2}\forall x_{1},x_{2}\in X.A functionf :$$

■A functionf :$X\to\mathrm{Y}$ isonto (or surjective) ifgiven any $y\in\mathrm{Y},\exists x\in\mathrm{X}$ such that $f(x)=y$

■A function $f\colon\mathrm{X}\to\overline{{\mathrm{Y}}}$ is one-one and onto (or bijective), iff is both one-one and onto.

■Given a finite set X, a function $f\mathrm{:X\to X}$ is one-one (ptivlonto) i d only iffisotivl-o).Tisiseaaiiroperty ofa finite set.This is nottruefor infinite set

## Historical Note

Theconceptoffunctionhasvolvedoverlonperiodotimetartingfrom R. Descartes (1596-1650),who used the word 'function'in his manuscript “Geometrie”in 1637to mean some positive integral power x" of a variable x while studying geometrical curves like hyperbola,parabolaandellipse.James Gregory (1636-1675)in nhis work “Vera Circuli et Hyperbolae Quadratura"(1667)considered function as a quantity obtained from other quantities by successive use of algebraic operations orbyany other operations.Later G.W.Leibnitz (1646-1716)in his manuscript "Methodus tangentium 1inversa,seu de functionibus"written in 1673used the word 'function'to mean a quantity varying from point to point on curve such as the coordinates f a e slope of the curve,the tangent and the normal to the curve at a point.1However,in his manuscript Historia (1714),Leibnitz used the word 'function' to mean quantities that depend on a vari riable.He was the first touse the phrase 'function ofx'.John Bernoulli 1667-748used notation φx for the first time in 1718 to indicate a function ofx.But the general adoption of symbols like f, F, φ, Ψ ... to represent functions was made by Leonhard Euler (1707-1783)in1734 in the first part of his manuscript Analysis Infinitorium"Later on, Joeph Loui aga (1736-1813)published his manuscripts “Theorie des functions analytiques" in 1793,where he discussed about analytic function ),(),φ(x)etc.for different function of t Subsequently,Lejeunne Dirichlet (1805-1859)gave the definition of function which was being used till the set theoretic definition of function presently used,was given after set theory was developed by Georg Cantor (1845-1918).The set theoretic definition of function known to us presently is simply an abstraction of the definitiongiven by Dirichlet in a rigorous manner.

