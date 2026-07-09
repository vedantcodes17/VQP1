

# VECTOR ALGEBRA

田In most sciencesonegenerationtearsdown whatanotherhasbuiltand what one hasestablished anotherundoes.In Mathematicsaloneeach generation builds a new story to the old structure. –HERMANHANKEL

### 10.1 Introduction

In our day to day life, we come across many queries such as – What is your height? How should a football player hit the ball to give a pass to another player of his team? Observe that a possible answer to the first query may be 1.6 meters,a quantity that involves only one value (magnitude) which is a real number. Such quantities are called scalars.However, an answer to the second query is a quantity (called force) which involves muscular strength (magnitude) and direction (in which another player is positioned). Such quantities are called vectors. In mathematics, physics and engineering, we frequently come across with both types of quantities, namely, scalar quantities such as length, mass,time, distance, speed, area, volume, temperature, work,

<div style="text-align: center;"><img src="imgs/img_in_image_box_668_591_916_908.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;">W.R. Hamilton (1805-1865)</div>

meyt acceleration, force, weight, momentum, electric field intensity etc.

In this chapter, we will study some of the basic concepts about vectors, various operations on vectors, and their algebraic and geometric propertis. These two type of properties,whenconieredtogether give fll aliationtotheconcpt of vectors,and lead to their vital applicability in various areas as mentioned above.

### 10.2 Some Basic Concepts

Let 'l' be any straight line in plane or three dimensional space. This line can be given two directions by means of arrowheads. A line with one of these directions prescribed is called a directed line (Fig 10.1 (i), (ii)).

<div style="text-align: center;"><img src="imgs/img_in_image_box_231_168_775_427.jpg" alt="Image" width="53%" /></div>

<div style="text-align: center;">Fig 10.1</div>

Now observethat if we restrict the line ltothe line segment AB, then a manitude is prescribed on the line l with one of the two directions, so that we obtain a directed line segment (Fig 10.1(ii)). Thus, a directed line segment has magnitude as well as direction.

Definition 1 A quantity that has magnitude as well as direction is called a vector.

Notice that a directed line segment is a vector (Fig 10.1(ii)), denoted as $\mathbf{\overline{A B}}$ or simply as $\vec{a}$ , and read as 'vector $\overrightarrow{\mathrm{A B}}$ or'vector $\left[{\vec{a}}\right]$

The point A from where the vector $\overrightarrow{\mathrm{A B}}$ starts is called its initial point, and the point B where it ends is called its terminal point. The distance between initial and terminal points of avector iscalled the magnitude or length)ofthe vector denoted as $|\overrightarrow{AB}|,\mathrm{or}|\vec{a}|,$ , or a. The arrow indicates the direction of the vector.

Noteeeisviotation $|\vec{a}|<0$ has no meaning.

## Position Vector

From Class XI, recall the three dimensional right handed rectangular coordinate system (Fig 10.2(i)). Consider a point P in space, having coordinates $(x,y,z)$ with respect to the origin $\mathrm{O}(0,0,0)$ 1. Then, the vector $\overrightarrow{\mathrm{O P}}$ having O and P as its initial and terminal points, respectively, is called the position vector of the point P with respect to O. Using distance formula (from Class XI), the magnitude of $\overrightarrow{\mathrm{O P}}(\mathrm{o r}\;\vec{r}\;)$ is given by

$$|\overrightarrow{OP}|=\sqrt{x^{2}+y^{2}+z^{2}}

$$

In practice, the position vectors of points A, B, C, etc., with respect to the origin O are denoted by $\left[\vec{a},\vec{b},\vec{c}\right.]$ , etc., respectively (Fig 10.2 (ii)).

<div style="text-align: center;"><img src="imgs/img_in_image_box_226_162_790_464.jpg" alt="Image" width="55%" /></div>

<div style="text-align: center;">Fig 10.2</div>

## Direction Cosines

Consider the position vector $\overrightarrow{OP}$ or $\vec{r}$ of a point $\mathbb{P}(x,y,z)$ as in Fig 10.3.The angles α,β, γ made by the vector $\left[\vec{r}\right.]$ with the positive directions of x, y and $z{\tt-a x e s}$ respectively,are called its direction angles. The cosine values of these angles, i.e., cos α, cosβ and cosγ are called direction cosines of the vector $\vec{r}$ , and usually denoted by l, m and n,respectively.Z

<div style="text-align: center;">Fig 10.3</div>

From Fig 10.3, one may note that the triangle OAP is right angled, and in it, we have cos $\alpha=\frac{x}{r}\left(r\mathrm{trans}\mathrm{for}|\vec{r}|\right)$ . Similarly, from the right angled triangles OBP and OCP, we may write cos $\beta=\frac{y}{r}\quad and\quad\cos\gamma=\frac{z}{r}$ . Thus, the coordinates of the point P may also be expressed as $(l r,m r,\stackrel{\cdot}{n r})$ 1. The numbers $l r.$ ,mr and nr, proportional to the direction cosines are called as direction ratios of vector $\left[\vec{r}\right.]$ , and denoted as $a$ , and $c,$ respectively. Note One may note that $l^{2}+m^{2}+n^{2}=1$ but $a^{2}+b^{2}+c^{2}\neq1$ , in general.

### 10.3 Types of Vectors

Zero Vector A vector whose initial and terminal points coincide, is called a zero vectorll,$\vec{0}$ .vc direction asithas zero magitue.$\mathrm{O r},$ alternativlrtarde s having any direction. The vectors $\overrightarrow{\mathrm{AA}},\overrightarrow{\mathrm{BB}}$ represent the zero vector,

unit vector in the directionof a given vector $\left[\vec{a}\right.]$ is denoted by $\hat{a}$

Coinitlesvl vectors.

Collinear Vectors Two or more vectors are said to be collinear if they are parallel to the same line, irrespective of their magnitudes and directions.

Equal Vectors Two vectors $\vec{a}$ and $\vec{b}$ are said to be equal, if they have the same magnitude and direction regardess of the positions of their initial points, and writen as $\vec{a}=\vec{b}$

Negative of a Vector A vector whose magnitude is the same as that of a given vector (say, AB), but direction is opposite to that of it, is called negative of the given vector.For example, vector $\overrightarrow{\mathrm{B A}}$ is negative of the vector $\overrightarrow{\mathrm{AB}}$ , and written as $\overrightarrow{BA}=-\overrightarrow{AB}$

Remark The vectors defined above are such that any of them may be subject to its parallel displacement without changing its magnitude and direction. Such vectors are called free vectors. Throughout this chapter, we will be dealing with free vectors only.Example 1 Represent graphically a displacement of 40 km, 30° west of south.

Solution The vector $\overrightarrow{\mathrm{O P}}$ represents the required displacement (Fig 10.4).

Example 2 Classify the following measures as scalars and vectors.

(i) 5 seconds

(ii)1000$\mathrm{c m}^{3}$

<div style="text-align: center;"><img src="imgs/img_in_image_box_582_1021_898_1321.jpg" alt="Image" width="31%" /></div>

<div style="text-align: center;">Fig 10.4</div>

## MATHEMATICS

(i) 10 Newton (iv) 30km/hr (v) 10 g/cm3

(vi) 20 m/s towards north

## Solution

(i) Time-scalar (i) Volume-scalar (iii) Force-vector (iv) Speed-scalar (v) Density-scalar (vi) Velocity-vector Example 3 In Fig 10.5, which of the vectors are:

(i) Collinear (ii)Equal (ii) Coinitial

## Solution

(i) Collinear vectors :$\vec{a}$ ,$\vec{c}$ and $\vec{d}$

(ii) Equal vectors :$\left[\vec{a}\right.]$ and c.

(i) Coinitial vectors :$\left[\vec{b},\vec{c}\right]$ and d.

<div style="text-align: center;"><img src="imgs/img_in_image_box_600_556_659_614.jpg" alt="Image" width="5%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_686_453_951_684.jpg" alt="Image" width="26%" /></div>

### EXERCISE 10.1

1. Represent graphically a displacement of 40 km, 30° east of north.

2. Classify the following measures as scalars and vectors.

(i)10kg (ii) 2 meters north-west (ii) 40

(iv)40 watt (v) 10-19 coulomb (vi) 20 m/s2

3. Classify the following as scalar and vector quantities.

(i) time period (ii) distance (i)force

(iv) velocity (v)work done

In Fig 10.6 (a square), identify the following vectors.

(i)Coinitial (ii) Equal

(i) Collinear but not equal

5. Answer the following as true or false.

(i)ā and $-\vec{a}$ are collinear.

(ii)Two collinear vectors are always equal in magnitude.

<div style="text-align: center;"><img src="imgs/img_in_image_box_667_945_921_1198.jpg" alt="Image" width="25%" /></div>

<div style="text-align: center;">Fig 10.6</div>

(ii) Two vectors having same magnitude are collinear.

(iv) Two collinear vectors having the same magnitude are equal.

### 10.4 Addition of Vectors

A vector $\overrightarrow{AB}$ simply means the displacement from a point A to the point B. Now consider a situation that a girl moves fromAtoBand then fromBtoC (Fig 10.7). The net displacement made by the girl from point A to the point C, is given by the vector $\overline{{\mathrm{A C}}}$ and expressed as

<div style="text-align: center;"><img src="imgs/img_in_image_box_640_164_917_350.jpg" alt="Image" width="27%" /></div>

<div style="text-align: center;">Fig 10.7</div>

$$

\overline{AC}=\overline{AB}+\overline{BC}

$$

This is known as the triangle law of vector addition.

In general, if we have two vectors $\left[\vec{a}\right.]$ and $\vec{b}$ (Fig 10.8 (i), then to addthem, they are positioned so that theinitial point of one coincides with theterminal point of the other (Fig 10.8(i)).E

<div style="text-align: center;"><img src="imgs/img_in_image_box_123_628_903_897.jpg" alt="Image" width="77%" /></div>

<div style="text-align: center;">Fig 10.8</div>

For example, in Fig 10.8 (ii), we have shifted vector $\vec{b}$ without changing its magnitude andiltiwil $\vec{a}$ . Then, the vector $\vec{a}+\vec{b}$ , represented by the third side AC of the triangle ABC, gives us the sum (or resultant) of the vectors $\vec{a}$ and $\left[\vec{b}\;i.e.\right.]$ ., in triangle ABC (Fig10.8 (i)), we have

$$

\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}

$$

Now again, since $\overrightarrow{AC}=-\overrightarrow{CA}$ , from the above equation, we have

$$

\overrightarrow{AB}+\overrightarrow{BC}+\overrightarrow{CA}=\overrightarrow{AA}=\overrightarrow{0}

$$

This means that when the sides of a triangle are taken in order, it leads to zero resultant as the initial and terminal points get coincided (Fig 10.8(iii)).

Now, construct a vector $\overrightarrow{\mathrm{B C^{\prime}}}$ so that its magnitude is same as the vector (ci)$\overrightarrow{BC}$ ,but the direction opposite tothat of it (Fig10.8(ii), i.e.,

$$

\overline{BC'}=-\overline{BC}

$$

Then,pll wmv

$$

\overrightarrow{AC'}=\overrightarrow{AB}+\overrightarrow{BC'}=\overrightarrow{AB}+(-\overrightarrow{BC})=\overrightarrow{a}-\overrightarrow{b}

$$

The vector $\overrightarrow{AC'}$ is said to represent the difference of $\vec{a}$ and $\vec{b}$ ,

Now, consider a boat in a river going from one bank of the river to the other in a direction perpendicular to the flow of the river. Then, it is acted upon by two velocity vectors—one is the velocity imparted to the boat by its engine and other one is the velocity of the flow of river water. Under the simultaneous influence of these two velocitieseboatictualtrtstavlling wihifrntlocity.Tohave reise idea about the effective speed and direction (i.e., the resultant velocity) oftheboa, we have the following law of vector addition.

If we have two vectors $\vec{a}$ and $\vec{b}$ represented by the two adjacent sides of a parallelogram in magnitude and direction (Fig 10.9), then their sum $\vec{a}+\vec{b}$ is represented in magnitude and direction by the diagonal of the parallelogram through their common point. This is known as the parallelogram law of vector addition.

$$

\vec{b}

$$

$$

\vec{a}

$$

<div style="text-align: center;">Fig 10.9</div>

$$

\vec{\overrightarrow{b}}

$$

Note] From Fig 10.9, using the triangle law, one may note that

$$

\overrightarrow{OA}+\overrightarrow{AC}=\overrightarrow{OC}

$$

or

$$

\overrightarrow{OA}+\overrightarrow{OB}=\overrightarrow{OC}

$$

(since $\overrightarrow{AC}=\overrightarrow{OB}$

which is parallelogram law. Thus, we may say that the two laws of vector addition are equivalent to each other.

## Properties of vector addition

Property 1 For any two vectors $\vec{a}$ and $\vec{b}$ ,

$$

\vec{a}+\vec{b}=\vec{b}+\vec{a}

$$

(Commutative property)

Proof Consider the parallelogram ABCD (Fig 10.10). Let $\overrightarrow{\mathrm{AB}}\quad\vec{a}$ and $\overline{\mathrm{BC}}\quad\vec{b}$ ,then using the triangle law, from triangle ABC, we have

$$

\overrightarrow{AC}=\overrightarrow{a}+\overrightarrow{b}

$$

<div style="text-align: center;"><img src="imgs/img_in_image_box_553_159_902_438.jpg" alt="Image" width="34%" /></div>

<div style="text-align: center;">Fig 10.10</div>

Now, since the opposite sides of a parallelogram are equal and parallel, from Fig 10.10, we have,$\overrightarrow{AD}=\overrightarrow{BC}=\overrightarrow{b}$ and $\overrightarrow{DC}=\overrightarrow{AB}=\overrightarrow{a}$ . Again using triangle law, from triangle ADC, we have

$$

\overrightarrow{AC}=\overrightarrow{AD}+\overrightarrow{DC}=\overrightarrow{b}+\overrightarrow{a}

$$

Hence $\vec{a}+\vec{b}=\vec{b}+\vec{a}$

Property 2 For any thre vectors $\vec{a}$ ,$\vec{b}$ andc

$$

(\vec{a}+\vec{b})+\vec{c}=\vec{a}+(\vec{b}+\vec{c})

$$

(Associative property)

Proof Let the vectors $\vec{a},\vec{b}$ and be represented by PQ, QRand yPO, OR and $$

 , respectively,, respectively,as shown in Fig 10.11(i) and (ii).

$$\vec{b}

$$

$$

\vec{b}

$$

$$

\left(\overrightarrow{a}+\overrightarrow{b}\right)+\overrightarrow{c}

$$

<div style="text-align: center;">(i)</div>

<div style="text-align: center;">(ii)</div>

<div style="text-align: center;">Fig 10.11</div>

Then

$$

\begin{aligned}\vec{a}+\vec{b}&=\overrightarrow{PQ}+\overrightarrow{QR}=\overrightarrow{PR}\\vec{b}+\vec{c}&=\overrightarrow{QR}+\overrightarrow{RS}=\overrightarrow{QS}\\left[(\vec{a}+\vec{b})+\vec{c}\right]&=\overrightarrow{PR}+\overrightarrow{RS}=\overrightarrow{PS}\end{aligned}

$$

and

Hence

$$

\left\{\begin{aligned}\vec{a}+(\vec{b}+\vec{c})&=\overrightarrow{PQ}+\overrightarrow{QS}=\overrightarrow{PS}\\ (\vec{a}+\vec{b})+\vec{c}&=\vec{a}+(\vec{b}+\vec{c})\end{aligned}\right.}

$$

Remark The associative property of vector addition enables us to write the sum of three vectors $\left[\vec{a},\vec{b},\vec{c}\mathrm{a s}\vec{a}+\vec{b}+\vec{c}\right]$ without using brackets.

Note that for any vector $\vec{a}$ , we have

$$

\vec{a}+\vec{0}=\vec{0}+\vec{a}=\vec{a}

$$

Here, the zero vector $\vec{0}$ iscalledeo.

### 10.5 Multiplication of a Vector by a Scalar

Let $\vec{a}$ beaivenλ.ocoftor (rd:$\vec{a}$ by the scalar $\lambda,$ denoted as $\lambda\vec{a}$ ,ialleo $\vec{a}$ by the scalar $\lambda$ . Note that,$\lambda\vec{a}$ is also a,ltco $\vec{a}$ . The vector $\lambda\vec{a}$ has the direction same (or opposite) to that of vector $\vec{a}$ b according as the value ofλ is positive (or negative.Also, the magnitude of vector $\lambda\vec{a}$ is $|\lambda|$ times the magnitude of the vector $\vec{a}$ , i.e.,

$$

|\lambda\vec{a}|=|\lambda||\vec{a}|

$$

A geometric visualisation of multiplication of a vector by a scalar is given in Fig 10.12.

<div style="text-align: center;"><img src="imgs/img_in_image_box_834_810_897_966.jpg" alt="Image" width="6%" /></div>

$$

\ncong 

$$

<div style="text-align: center;">Fig 10.12</div>

When $\lambda=-1$ , then $\lambda\vec{a}=-\vec{a}$ , which is a vector having magnitude equal to the magnitude of $\vec{a}$ $\vec{a}$ . The vector $-\vec{a}$ is cal)$\vec{a}$ and we always have

$$

\vec{a}+(-\vec{a})=(-\vec{a})+\vec{a}=\vec{0}

$$

Also, if $\lambda=\frac{1}{\left|\vec{a}\right|}$ , provided $\begin{array}{cc}\vec{a}&0\end{array}$ ,i.e.$\vec{a}$ is not a null vector, then

$$

\left|\lambda\vec{a}\right|=\left|\lambda\right|\left|\vec{a}\right|=\frac{1}{\left|\vec{a}\right|}\left|\vec{a}\right|

$$

$\mathrm{S}_{0}$ $\lambda\vec{a}$ represents the unit vector in the direction $o f\vec{a}$ . We write it as

$$

\hat{a}=\frac{1}{\left|\vec{a}\right|}\vec{a}

$$

NoteFor any scalar k,$k\vec{0}=\vec{0}$

#### 10.5.1 Components of a vector

Let us take the points A(1, 0, 0), B(0, 1, 0) and $\mathrm{C}(0,0,1)$ on the x-axis, y-axis and z-axis, respectively. Then, clearly

<div style="text-align: center;"><img src="imgs/img_in_image_box_706_423_914_631.jpg" alt="Image" width="20%" /></div>

<div style="text-align: center;">Fig 10.13</div>

$$

|\overrightarrow{OA}|=1,|\overrightarrow{OB}|=1and|\overrightarrow{OC}|=1

$$

The vectors $\overrightarrow{\mathrm{O A}}$ ,ob and $\overrightarrow{\mathrm{O C}}$ , each having magnitude 1,are called unit vectors along the axes OX, OY and $ OZ$ respectively, and denoted by $\left[\hat{i},\hat{j}\right.]$ and $\hat{k}$ ,respectively (Fig 10.13).

Now, consider the position vector $\overline{OP}$ of a point $\mathrm{P}(x,y,z)$ as in Fig 10.14. Let $ P_{1}$ SENE be the foot of the perpendicular from P on the plane XoY. We, thus, see that $\mathrm{P}_{1}\mathrm{P}$ is

$$

NCER \hat{z k}

$$

parallel to z-axis.$\mathrm{As}\quad\hat{i},\hat{j}$ and $\hat{k}$ are the unit vectorsalong the x,y and z-aes,respectively, and by the definition of the coordinates of $\mathrm{P},$ we have $\overrightarrow{P_{1}P}=\overrightarrow{OR}=z\hat{k}$ Similarly,$\overrightarrow{QP_{1}}=\overrightarrow{OS}=y\hat{j}and\overrightarrow{OQ}=x\hat{i}$

Therefore, it follows that

$$

\overrightarrow{OP_{1}}=\overrightarrow{OQ}+\overrightarrow{QP_{1}}=x\hat{i}+y\hat{j}

$$

and

$$

\overrightarrow{OP}=\overrightarrow{OP_1}+\overrightarrow{P_1P}=x\hat{i}+y\hat{j}+z\hat{k}

$$

Hence, the position vector of P with reference to O is given by

$$

\overrightarrow{\mathrm{O P}}(\mathrm{o r}\vec{r})=x\hat{i}+y\hat{j}+z\hat{k}

$$

This form of any vector is called its component form. Here,$x,y$ and $z\;\mathtt{a r e}$ called as the scalar components of $\vec{r}$ , and $x\hat{i},\;y\hat{j}$ and $z\hat{k}$ are called the vector components of $\vec{r}$ along the respective axes. Sometimes $x,$ y and z are also termed as rectangular components.

The length of any vector $\vec{r}=x\hat{i}+y\hat{j}+z\hat{k}$ , is readily determined by applying the Pythagoras theorem twice. We note that in the right angle triangle $\mathrm{\underline{O}\underline{Q}P_{1}}$ (Fig 10.14)

$$

\left|\overrightarrow{OP_{1}}\right|=\sqrt{\left|\overrightarrow{OQ}\right|^{2}+\left|\overrightarrow{QP_{1}}\right|^{2}}=\sqrt{x^{2}+y^{2}},

$$

and in the right angle triangle $\mathrm{OP_{1}P_{1}}$ , we have

$$

\overrightarrow{OP}=\sqrt{\left|\overrightarrow{OP_{1}}\right|^{2}\left|\overrightarrow{P_{1}P}\right|^{2}}\sqrt{\left(x^{2}\quad y^{2}\right)\quad z^{2}}

$$

Hence, the length of any vector $\vec{r}=x\hat{i}+y\hat{j}+z\hat{k}$ is given by

$$

|\vec{r}|=|x\hat{i}+y\hat{j}+z\hat{k}|=\sqrt{x^2+y^2+z^2}

$$

If $\vec{a}$ and $\vec{b}$ are any two vectors given in the component form $a_{1}\hat{i}+a_{2}\hat{j}+a_{3}\hat{k}$ and $b_{1}\hat{i}+b_{2}\hat{j}+b_{3}\hat{k}$ , respectively, then

(i)the sum (or resultant) of the vectors $\vec{a}$ and $\vec{b}$ is given by

$$

\vec{a}+\vec{b}=(a_1+b_1)\hat{i}+(a_2+b_2)\hat{j}+(a_3+b_3)\hat{k}

$$

(f $\vec{a}$ and $\vec{b}$ is given by

$$

\vec{a}-\vec{b}=(a_1-b_1)\hat{i}+(a_2-b_2)\hat{j}+(a_3-b_3)\hat{k}

$$

(ii) the vectors $\vec{a}$ and $\vec{b}$ are equal if and only if

$$

a_{1}=b_{1},a_{2}=b_{2}\quad and\quad a_{3}=b_{3}

$$

(iv)the multiplication of vector $\vec{a}$ by any scalar $\lambda$ is given by

$$

\vec{a}=(a_1)\hat{i}\quad(a_2)\hat{j}\quad(a_3)\hat{k}

$$

The addition of vectors and the multiplication of a vector by a scalar together give the following distributive laws:

(i)

、Let $$

 and 

$$ beany tw,balars. Then

$$

k\vec{a}+m\vec{a}=(k+m)\vec{a}

$$

(ii)

$$

k(m\vec{a})=(km)\vec{a}

$$

(i)$k({\vec{a}}\quad{\vec{b}})\quad k{\vec{a}}\quad k{\vec{b}}$

## Remarks

(iOne mayobveht whatvrbehvaluof $\lambda.$ the vector $\lambda\vec{a}$ is always collinear to the vector $\vec{a}$ . In fact, two vectors $\vec{a}$ and $\vec{b}$ are collinear if and only if there exists a nonzero scalar λ such that $\vec{b}=\lambda\vec{a}$ .If the vectors $\vec{a}$ and $\vec{b}$ are given in the component form, i.e.$\vec{a}=a_{1}\hat{i}+a_{2}\hat{j}+a_{3}\hat{k}$ and $\vec{b}=b_{1}\hat{i}+b_{2}\hat{j}+b_{3}\hat{k}$ then the two vectors are collinear if and only if

←

c

←→

$$

\begin{aligned}b_{1}\hat{i}+b_{2}\hat{j}+b_{3}\hat{k}&=\lambda(a_{1}\hat{i}+a_{2}\hat{j}+a_{3}\hat{k})\\b_{1}\hat{i}+b_{2}\hat{j}+b_{3}\hat{k}&=(\lambda a_{1})\hat{i}+(\lambda a_{2})\hat{j}+(\lambda a_{3})\hat{k}\\b_{1}&=\lambda a_{1},\quad b_{2}=\lambda a_{2},\quad b_{3}=\lambda a_{3}\\frac{b_{1}}{a_{1}}&=\frac{b_{2}}{a_{2}}=\frac{b_{3}}{a_{3}}=\lambda\end{aligned}

$$

(ii)If $\vec{a}\quad\overline{a_{1}\hat{i}}\quad\overline{a_{2}\hat{j}}\quad\overline{a_{3}\hat{k}}$ , then $a_{1},a_{2},a_{3}$ are also called direction ratios of $\vec{a}$ ,

(iii)Incase ifit is given that l, m, are directioncosines of avector, then $l\hat{i}+m\hat{j}+n\hat{k}$ $\left(\cos\alpha\right)\hat{i}+\left(\cos\beta\right)\hat{j}+\left(\cos\gamma\right)\hat{k}$ is the unit vector in the direction of that vector,where α, β and γ are the angles which the vector makes with $x,y{\mathrm{~a n d~}}z{\mathrm{~a x e s}}$ respectively.

Example 4 Find the values of , y and $z\mathrm{~s o~}$ that the vectors $\vec{a}=x\hat{i}+2\hat{j}+z\hat{k}$ and $\vec{b}=2\hat{i}+y\hat{j}+\hat{k}$ are equal.

Solution Note that two vectors are equal if and only if their corresponding components are equal. Thus, eiven vectors $\vec{a}$ and $\vec{b}$ will be equal if ad y i

$$

x=2,y=2,z=1

$$

Example 5 Let $\vec{a}=\hat{i}+2\hat{j}\quad and\quad\vec{b}=2\hat{i}+\hat{j}.\quad Is\quad|\vec{a}|=|\vec{b}|?$ Are the vectors $\vec{a}$ and $\vec{b}$ equal?

$$

\mathrm{S}_{\mathrm{O}\mathrm{I}\mathrm{u}\mathrm{f}\mathrm{i}\mathrm{O}\mathrm{B}}\text{We have}\left|\vec{a}\right|=\sqrt{1^{2}+2^{2}}=\sqrt{5}\text{and}\left|\vec{b}\right|\quad\sqrt{2^{2}-1^{2}}\quad\sqrt{5}

$$

So,are distinct.$|\vec{a}|=|\vec{b}|$ .u, ql ic me ,

Example 6 Find unit vector in the direction of vector $$

 a

Solution Theunit ector i the dirctionof avector $\vec{a}$ is given by is given by 

$$

Now

$$

|\vec{a}|=\sqrt{2^{2}+3^{2}+1^{2}}=\sqrt{14}

$$

Therefore

$$

\hat{a}=\frac{1}{\sqrt{14}}(2\hat{i}+3\hat{j}+\hat{k})=\frac{2}{\sqrt{14}}\hat{i}+\frac{3}{\sqrt{14}}\hat{j}+\frac{1}{\sqrt{14}}\hat{k}

$$

Example7Findavectorinthedirectionofvector ,$$

 that has magnitude that has magnitude 7 units.

Slu $\vec{a}$ is

$$\hat{a}=\frac{1}{\left|\vec{a}\right|}\vec{a}=\frac{1}{\sqrt{5}}\left(\hat{i}-2\hat{j}\right)=\frac{1}{\sqrt{5}}\hat{i}-\frac{2}{\sqrt{5}}\hat{j}

$$

$\vec{a}$ i

$$

7\hat{a}=7\left(\frac{1}{\sqrt{5}}\hat{i}-\frac{2}{\sqrt{5}}\hat{j}\right)=\frac{7}{\sqrt{5}}\hat{i}-\frac{14}{\sqrt{5}}\hat{j}

$$

Example 8 Find the unit vector in the direction of the sum of the vectors,

$\vec{a}=2\hat{i}+2\hat{j}-5\hat{k}and\vec{b}=2\hat{i}+\hat{j}+3\hat{k}$

Solution The sum of the given vectors is

$$

\vec{a}\quad\vec{b}\quad(\vec{c},\mathrm{say})=4\hat{i}\quad3\hat{j}\quad2\hat{k}

$$

and

$$

|\vec{c}|=\sqrt{4^2+3^2+(-2)^2}=\sqrt{29}

$$

Thus, the required unit vector is

$$

\hat{c}=\frac{1}{\left|\vec{c}\right|}\vec{c}=\frac{1}{\sqrt{29}}\left(4\hat{i}+3\hat{j}-2\hat{k}\right)=\frac{4}{\sqrt{29}}\hat{i}+\frac{3}{\sqrt{29}}\hat{j}-\frac{2}{\sqrt{29}}\hat{k}

$$

Example 9 Write the direction ratio's of the vector $\vec{a}=\hat{i}+\hat{j}-2\hat{k}$ and hence calculate its direction cosines.

Solution Note that the direction ratio's a, b, c of a vector $\vec{r}=x\hat{i}+y\hat{j}+z\hat{k}$ are just the respectivecomponents ,andofthe vector.$\mathrm{S o.}$ for the given vector, we have $a=1,b=1$ and $c=-2$ .Further, if l, m and n are the direction cosines of the given vector, then

$$

l=\frac{a}{\left|\vec{r}\right|}=\frac{1}{\sqrt{6}},\quad m=\frac{b}{\left|\vec{r}\right|}=\frac{1}{\sqrt{6}},\quad n=\frac{c}{\left|\vec{r}\right|}=\frac{-2}{\sqrt{6}}\quad as\left|\vec{r}\right|=\sqrt{6},

$$

Thus, the direction cosines are $\left[\left(\frac{1}{\sqrt{6}},\frac{1}{\sqrt{6}},-\frac{2}{\sqrt{6}}\right)\right.]$

#### 10.5.2 Vector joining two points

If $\mathrm{P}_{1}(x_{1},y_{1},z_{1})$ and $\mathrm{P}_{2}(x_{2},y_{2},z_{2})$ e $\mathrm{P}_{1}$ and $\mathrm{P}_{2}$ is the vector $\overrightarrow{\mathrm{P}_{1}\mathrm{P}_{2}}$ (Fig 10.15).z←$\mathbf{P}_{2}\left(x_{2},y_{2},z_{2}\right)$

$$

\mathbf{P}_{2}\left(x_{2},y_{2},z_{2}\right)

$$

Joining the points $\mathrm{P}_{1}$ and $\mathrm{P}_{2}$ with the origin O, and applying triangle law, from the triangle $\mathrm{OP}_{1}\mathrm{P}_{2}$ we have

$$

\overrightarrow{OP_{1}}+\overrightarrow{P_{1}P_{2}}=\overrightarrow{OP_{2}}.

$$

e er e crr

i.e.

$$

\begin{aligned}\overrightarrow{P_{1}P_{2}}&=\overrightarrow{OP_{2}}-\overrightarrow{OP_{1}}\\overrightarrow{P_{1}P_{2}}&=(x_{2}\hat{i}+y_{2}\hat{j}+z_{2}\hat{k})-(x_{1}\hat{i}+y_{1}\hat{j}+z_{1}\hat{k})\\&=(x_{2}-x_{1})\hat{i}+(y_{2}-y_{1})\hat{j}+(z_{2}-z_{1})\hat{k}\end{aligned}

$$

<div style="text-align: center;"></div>

 ee e $\overrightarrow{\mathbb{P}_{1}\mathbb{P}_{2}}$

$$

\overrightarrow{P_{1}P_{2}}=\sqrt{\left(x_{2}-x_{1}\right)^{2}+\left(y_{2}-y_{1}\right)^{2}+\left(z_{2}-z_{1}\right)^{2}}

$$

r eaee e re r e re $\mathrm{Q}(-1,-2,-4)$ directed from P to Q.

Solution Since the vector is to be directed from P to Q, clearly P is the initial point and Q is the terminal point. So, the required vector joining P and Q is the vector $\overrightarrow{\mathrm{P Q}}$ given by

i.e.

$$

\begin{aligned}\overrightarrow{PQ}&=(-1-2)\hat{i}+(-2-3)\hat{j}+(-4-0)\hat{k},\\overrightarrow{PQ}&=-3\hat{i}-5\hat{j}-4\hat{k}.\end{aligned}

$$

#### 10.5.3 Section formula

Let P and Q be two points represented by the position vectors $\overrightarrow{\mathrm{O P}}$ and $\overrightarrow{\mathrm{O Q}}$ , respectively,

with respect to the origin O. Then the line segment joining the points P and Q may be divided by a third point, say R, in two ways – internally (Fig 10.16)and externally (Fig 10.17). Here, we intend to find the position vector $\overrightarrow{OR}$ for the point R with respet t to the origin O. We take the two cases one by one.Case I When R divides PQ internally (Fig 10.16).

If R divides $\overrightarrow{PQ}$ such that $m\overrightarrow{\mathrm{RQ}}=n\overrightarrow{\mathrm{PR}}$

<div style="text-align: center;"><img src="imgs/img_in_image_box_607_562_927_769.jpg" alt="Image" width="31%" /></div>

<div style="text-align: center;">Fig 10.16</div>

where m and n are positive scalars, we say that the point R divides PQ internally in the ratio of m : n. Nowfrom triangles ORQ and OPR, we have

and

$$

\begin{aligned}\overrightarrow{\mathrm{RQ}}&=\overrightarrow{\mathrm{OQ}}-\overrightarrow{\mathrm{OR}}=\overrightarrow{b}-\overrightarrow{r}\\overrightarrow{\mathrm{PR}}&=\overrightarrow{\mathrm{OR}}-\overrightarrow{\mathrm{OP}}=\overrightarrow{r}-\overrightarrow{a}\end{aligned}

$$

Therefore, we have

$$

m\left(\vec{b}-\vec{r}\right)=n\left(\vec{r}-\vec{a}\right)\quad(\mathrm{Why?})

$$

or

$$

\vec{r}=\frac{m\vec{b}+n\vec{a}}{m+n}

$$

(on simplification)

Hence, the position vector of the point R which divides P and Q internally in the ratio of m : n is given by

$$

\overrightarrow{OR}=\frac{\overrightarrow{mb}+n\overrightarrow{a}}{m+n}

$$

Case II When R divides PQ externally (Fig 10.17).We leave it to the reader as an exercise to verify that the position vector of the point R which divides the line segment PQ externally in the ratio $m:n$ i.e.$\frac{\mathrm{PR}}{\mathrm{QR}}\quad\frac{m}{n}$ is given by

$$

\overrightarrow{OR}=\frac{m\vec{b}-n\vec{a}}{m-n}

$$

<div style="text-align: center;"><img src="imgs/img_in_image_box_601_160_905_405.jpg" alt="Image" width="30%" /></div>

<div style="text-align: center;">Fig 10.17</div>

midpoint R of Remarkf R i $\overrightarrow{\mathbb{P Q}}$ , will have its position vector as e midpoint of PQ , then $m=n$ fore, from Cae , the

$$

\overrightarrow{OR}=\frac{\vec{a}+\vec{b}}{2}

$$

Example 11 Consider two points P and Q with position vectors $$

 and $\overrightarrow{\mathrm{O Q}}\quad\vec{a}\quad\vec{b}$ .Findthe positin vctor o a poit R which divies te lie iingP and Q inthe ratio 2:1, (i) internally, and (ii) extrnally.

## Solution

(i)The position vector of the point R dividing the join ofP and Q internally in the ratio 2:1 is

$$\overline{OR}=\frac{2(\overline{a}+\overline{b})+(3\overline{a}-2\overline{b})}{2+1}=\frac{5\overline{a}}{3}

$$

(ii)The position vector of the point R dividing the join ofP and Q externally in the ratio 2:1 is

$$

\overrightarrow{OR}=\frac{2(\vec{a}+\vec{b})-(3\vec{a}-2\vec{b})}{2-1}=4\vec{b}-\vec{a}

$$

Example 12 Show that the points $\mathrm{A}(2\hat{i}\quad\hat{j}\quad\hat{k}),\;\mathrm{B}(\hat{i}\quad3\hat{j}\quad5\hat{k}),\;\mathrm{C}(3\hat{i}\quad4j\quad4\hat{k})\;\mathrm{a r c}$ e the vertices of a right angled triangle.

Solution We have

and

$$

\begin{aligned}\overrightarrow{AB}&=(1-2)\hat{i}+(-3+1)\hat{j}+(-5-1)\hat{k}\quad\hat{i}\quad2\hat{j}\quad6\hat{k}\\overrightarrow{BC}&=(3-1)\hat{i}+(-4+3)\hat{j}+(-4+5)\hat{k}=2\hat{i}-\hat{j}+\hat{k}\\overrightarrow{CA}&=(2-3)\hat{i}+(-1+4)\hat{j}+(1+4)\hat{k}=-\hat{i}+3\hat{j}+5\hat{k}\end{aligned}

$$

Further, note that

$$

\left|\overrightarrow{AB}\right|^{2}=41=6+35=\left|\overrightarrow{BC}\right|^{2}+\left|\overrightarrow{CA}\right|^{2}

$$

Hence, the triangle is a right angled triangle.

### EXERCISE 10.2

1. Compute the magnitude of the following vectors:

$$

\left[\vec{a}=\hat{i}+\hat{j}+k;\quad\vec{b}=2\hat{i}-7\hat{j}-3\hat{k};\quad\vec{c}=\frac{1}{\sqrt{3}}\hat{i}+\frac{1}{\sqrt{3}}\hat{j}-\frac{1}{\sqrt{3}}\hat{k}\right]U1S 

$$

2. Write two different vectors having same magnitude.

3. Write two different vectors having same direction.

U1S 4. Find the values of x and y so that the vectors $2\hat{i}+3\hat{j}and x\hat{i}+y\hat{j}$ are equal.

5. Find the scalar and vector components of the vector with initial point (2, 1) and terminal point $(-5,7)$

6. Find the sum of the vectors $\vec{a}=\hat{i}-2\hat{j}+\hat{k},\quad\vec{b}=-2\hat{i}+4\hat{j}+5\hat{k}and\quad\vec{c}=\hat{i}-6\hat{j}-7\hat{k}$

7. Find the unit vector in the direction of the vector $\vec{a}=\hat{i}+\hat{j}+2\hat{k}$

8. Find the unit vector in the direction of vector $\overrightarrow{\mathrm{P Q}}$ , where P and Q are the points (1, 2, 3) and (4, 5, 6), respectively.

9. For given vectors,$\vec{a}=2\hat{i}-\hat{j}+2\hat{k}$ and $\vec{b}=-\hat{i}+\hat{j}-\hat{k}$ , find the unit vector in the direction of the vector $\vec{a}+\vec{b}$

10. Find a vector in the direction of vector $5\hat{i}-\hat{j}+2\hat{k}$ which has magnitude 8 units.

11. Show that the vectors $2\hat{i}-3\hat{j}+4\hat{k}\ and-4\hat{i}+6\hat{j}-8\hat{k}$ are collinear.

12. Find the direction cosines of the vector $\hat{i}+2\hat{j}+3\hat{k}$

13. Find the direction cosines of the vector joining the points $ A\left(1,2,-3\right)$ and $\mathrm{B}(-1,-2,1)$ , directed from A to B.

14. Show that the vector $\left[\hat{i}+\hat{j}+\hat{k}\right]$ 添司添is equally inclined to the axes OX, OY and OZ.

.and Q whose position vectors are $\left[\hat{i}+2\hat{j}-\hat{k}\quad\mathrm{a n d}-\hat{i}+\hat{j}+\hat{k}\right]$ respectively, in the ratio 2:1

(i) internally (ii) externally

1. )and Q(4, 1, −2).

17. Show that the points A, B and C with position vectors,$\vec{a}=3\hat{i}-4\hat{j}-4\hat{k}$ $\vec{b}=2\hat{i}-\hat{j}+\hat{k}\mathrm{a n d}\vec{c}=\hat{i}-3\hat{j}-5\hat{k}$ , respectively form the vertices of a right angled triangle.

18. In triangle ABC (Fig 10.18), which of the following is not true:

(A)

$$

\overrightarrow{AB}+\overrightarrow{BC}+\overrightarrow{CA}=\overrightarrow{0}

$$

(B)

(C)

(D)

$$

\overrightarrow{AB}+\overrightarrow{BC}-\overrightarrow{AC}=\overrightarrow{0}

$$

$$

\overrightarrow{AB}+\overrightarrow{BC}-\overrightarrow{CA}=\overrightarrow{0}

$$

$$

\overrightarrow{AB}-\overrightarrow{CB}+\overrightarrow{CA}=\overrightarrow{0}

$$

<div style="text-align: center;"><img src="imgs/img_in_image_box_638_449_906_583.jpg" alt="Image" width="26%" /></div>

<div style="text-align: center;">Fig 10.18</div>

19. If $\vec{a}$ and $\vec{b}$ ae l st l owing are incorrect:

(A)$\vec{b}=\lambda\vec{a}$ ,for some scalar λ

(B)$\vec{a}=\pm\vec{b}$

(C) the respective components of $\vec{a}$ a $$

 are not proport ional

(D) both the vectors $\vec{a}$ and $\vec{b}$ have same direction, but diferent magnitudes.

### 10.6 Product of Two Vectors

So far we have studied about addition and subtraction of vectors. An other algebraic operation which we intend to discuss regarding vectors is their product. We may recall that product of two numbers is a number, product of two matrices is again a matrix. But in case of functions, we may multiply them in two ways, namely,multiplicoftouns oie ndmpooftoun.l multiplicationoftwo vectors is also defined in two ways,namely, scalar (or dot)product where the result is a scalar, and vector (or cross) product where the result is a vector. Based upon these two types of products for vectors, they have found various appliations inomety,mechanicsand ngiering.Inthis tion we will discuss these two types of products.

#### 10.6.1 Scalar (or dot) product of two vectors

Definition 2 The scalar product of two nonzero vectors $\vec{a}$ and $\vec{b}$ , denoted by $\vec{a}\cdot\vec{b}$ , is

defined as

$$\vec{a}\cdot\vec{b}=|\vec{a}||\vec{b}|\cos\theta,

$$

where,θis the alebetween $\vec{a}$ and $\vec{b},0$ (Fig 10.19).

If either $\vec{a}=\vec{0}or\vec{b}=\vec{0}$ , then θ is not defined, and in this case,we define $\vec{a}\quad\vec{b}\quad0$

## Observations

1.${\vec{a}}\cdot{\vec{b}}$ is a real number.

<div style="text-align: center;"><img src="imgs/img_in_image_box_723_168_910_276.jpg" alt="Image" width="18%" /></div>

<div style="text-align: center;">Fig 10.19</div>

2.$\vec{a}$ $\vec{b}$ ar to each other. i.r, $\vec{a}\cdot\vec{b}=0$ if and only if 。$\vec{a}$ (cid:2)不$\vec{b}$ 2

$$

\vec{a}\cdot\vec{b}=0\Leftrightarrow\vec{a}\perp\vec{b}

$$

3.$\mathrm{If}\;\theta=0,\mathrm{then}\;\vec{a}\cdot\vec{b}=|\vec{a}||\vec{b}|$

In particular,$\vec{a}\cdot\vec{a}=\left|\vec{a}\right|^2$ as θ in this case is (as θ in this case is 0.(cd

4. If $\Theta=\pi.$ ,then $\vec{a}\cdot\vec{b}=-\left|\vec{a}\right|\left|\vec{b}\right|$

In particular,$\vec{a}\left(\vec{a}\right)\quad\left|\vec{a}\right|^2$ ,as θ in this case is π.se is π.

ts-llssnerendie $\left[\hat{i},\hat{j}\right]$ and $\hat{k}$ we have

$$

\hat{i}\cdot\hat{i}=\hat{j}\cdot\hat{j}=\hat{k}\cdot\hat{k}=1,\quad\hat{i}\cdot\hat{j}=\hat{j}\cdot\hat{k}=\hat{k}\cdot\hat{i}\quad0

$$

6. The angle between two nonzero vectors $\vec{a}$ and $\vec{b}$ is given by

$$

\frac{\overline{\vec{a}\setminus\vec{b}}}{\left|\vec{a}\right|\left|\vec{b}\right|},\quad\mathrm{or}\quad\theta=\cos^{-1}\left(\frac{\vec{a}.\vec{b}}{\left|\vec{a}\right|\left|\vec{b}\right|}\right)

$$

7. The scalar product is commutative. i.e.

$$

\vec{a}\cdot\vec{b}=\vec{b}\cdot\vec{a}\quad(\mathrm{Why?})

$$

Two important properties of scalar product

Property1(Distributivityof scalarproductoveraddition) Let $\vec{a},\vec{b}$ and $\vec{c}$ be any three vectors, then

$$

\vec{a}\cdot(\vec{b}+\vec{c})=\vec{a}\cdot\vec{b}+\vec{a}\cdot\vec{c}

$$

Property 2 Let $\vec{a}$ and $\vec{b}$ be any two vectors, and $\lambda$ be any scalarr. Then

$$

\left[\left(\lambda\vec{a}\right)\cdot\vec{b}=\left(\vec{a}\right)\vec{b}\quad\left(\vec{a}\quad\vec{b}\right)\quad\vec{a}\quad\left(\vec{b}\right)\right]

$$

If two vectors $\vec{a}$ and $\vec{b}$ are given in component form as $a_{1}\hat{i}+a_{2}\hat{j}+a_{3}\hat{k}$ and $b_{1}\hat{i}+b_{2}\hat{j}+b_{3}\hat{k}$ , then their scalar product is given as

$$

Thu \begin{aligned}\vec{a}\cdot\vec{b}&=\left(a_{1}\hat{i}+a_{2}\hat{j}+a_{3}\hat{k}\right)\cdot\left(b_{1}\hat{i}+b_{2}\hat{j}+b_{3}\hat{k}\right)\\&=a_{1}\hat{i}\cdot\left(b_{1}\hat{i}+b_{2}\hat{j}+b_{3}\hat{k}\right)+a_{2}\hat{j}\cdot\left(b_{1}\hat{i}+b_{2}\hat{j}+b_{3}\hat{k}\right)+a_{3}\hat{k}\cdot\left(b_{1}\hat{i}+b_{2}\hat{j}+b_{3}\hat{k}\right)\\&=a_{1}b_{1}(\hat{i}\cdot\hat{i})+a_{1}b_{2}(\hat{i}\cdot\hat{j})+a_{1}b_{3}(\hat{i}\cdot\hat{k})+a_{2}b_{1}(\hat{j}\cdot\hat{i})+a_{2}b_{2}(\hat{j}\cdot\hat{j})+a_{2}b_{3}(\hat{j}\cdot\hat{k})\\&\quad+a_{3}b_{1}(\hat{k}\cdot\hat{i})+a_{3}b_{2}(\hat{k}\cdot\hat{j})+a_{3}b_{3}(\hat{k}\cdot\hat{k})\left(Using the above Proposition1and2\right)\\&=a_{1}b_{1}+a_{2}b_{2}+a_{3}b_{3}\quad\text{(Using Observeation5)}\\mathrm{s}\quad&\quad\vec{a}\cdot\vec{b}=a_{1}b_{1}+a_{2}b_{2}+a_{3}b_{3}\end{aligned}

$$

Thu $\begin{aligned}\vec{a}\cdot\vec{b}&=\left(a_{1}\hat{i}+a_{2}\hat{j}+a_{3}\hat{k}\right)\cdot\left(b_{1}\hat{i}+b_{2}\hat{j}+b_{3}\hat{k}\right)\\&=a_{1}\hat{i}\cdot\left(b_{1}\hat{i}+b_{2}\hat{j}+b_{3}\hat{k}\right)+a_{2}\hat{j}\cdot\left(b_{1}\hat{i}+b_{2}\hat{j}+b_{3}\hat{k}\right)+a_{3}\hat{k}\cdot\left(b_{1}\hat{i}+b_{2}\hat{j}+b_{3}\hat{k}\right)\\&=a_{1}b_{1}(\hat{i}\cdot\hat{i})+a_{1}b_{2}(\hat{i}\cdot\hat{j})+a_{1}b_{3}(\hat{i}\cdot\hat{k})+a_{2}b_{1}(\hat{j}\cdot\hat{i})+a_{2}b_{2}(\hat{j}\cdot\hat{j})+a_{2}b_{3}(\hat{j}\cdot\hat{k})\\&\quad+a_{3}b_{1}(\hat{k}\cdot\hat{i})+a_{3}b_{2}(\hat{k}\cdot\hat{j})+a_{3}b_{3}(\hat{k}\cdot\hat{k})\left(Using the above Proposition1and2\right)\\&=a_{1}b_{1}+a_{2}b_{2}+a_{3}b_{3}\quad\text{(Using Observeation5)}\\mathrm{s}\quad&\quad\vec{a}\cdot\vec{b}=a_{1}b_{1}+a_{2}b_{2}+a_{3}b_{3}\end{aligned}$

#### 10.6.2 Projection of a vector on a line

Suppose a vector $\overrightarrow{\mathrm{A B}}$ makes an angle θ with a given directed line l (say), in the anticlockwise direction (Fig 10.20). Then the projection of $\overrightarrow{\mathrm{A B}}$ on l is a vector $\vec{p}$ (say) with magnitude $|\overrightarrow{AB}|\cos\theta$ , and the direction of $\vec{p}$ being the same (or opposite)to that of the linel, depending upon whethercosθis positive or negative.The vector $\vec{p}$

<div style="text-align: center;"><img src="imgs/img_in_image_box_100_868_902_1337.jpg" alt="Image" width="79%" /></div>

$\left\lfloor{\vec{p}}\right\rfloor$ of the vector $\overrightarrow{\mathrm{A B}}$ on the directed line l.

For exam,flluig.), rjceto of $\overrightarrow{\mathrm{AB}}$ along the line l is vector $\overline{\mathrm{AC}}$

## Observations

1. If $\hat{p}$ i $\vec{a}$ on the line l is given by $\left[\vec{a}\quad\hat{p}\right.]$

2. Projection of a vector $\vec{a}$ on other vector $\left[\vec{b}\right.]$ , is given by

$$

\left[{\vec{a}}\cdot{\hat{b}},\quad{\mathrm{o r}}\quad{\vec{a}}\cdot\left({\frac{\vec{b}}{|{\vec{b}}|}}\right),{\mathrm{o r}}\quad{\frac{1}{|{\vec{b}}|}}({\vec{a}}\cdot{\vec{b}})\right]

$$

3. If $\Theta=0$ , then the projection vector of $\overrightarrow{\mathbf{A B}}$ will be $\overrightarrow{\mathrm{A B}}$ itself and if $\theta=\pi$ , then the projection vector of $\overrightarrow{AB}$ will be $\overline{{\mathrm{B A}}}$

4. If $\theta=\frac{\pi}{2}\quad or\quad\theta=\frac{3\pi}{2}$ , then the projection vector of $\overrightarrow{\mathrm{A B}}$ will be zero vector.

Remark If α, β and γ are the direction angles of vector $\vec{a}=a_{1}\hat{i}+a_{2}\hat{j}+a_{3}\hat{k}$ ,then its direction cosines may be given as

$$

\frac{\vec{a}\hat{i}}{\left\|\vec{a}\right\|\hat{i}\left\|\right.}\frac{a_{1}}{\left\|\vec{a}\right\|},\cos\frac{a_{2}}{\left\|\vec{a}\right\|},and\cos\frac{a_{3}}{\left\|\vec{a}\right\|}

$$

Also, note that $\left\lfloor{\vec{a}}\right\rfloor$ cos α, | |cosβ and $|\vec{a}$ cosye eilojections of āalong OX, OY and OZ. i.e., the scalar components $a_{1},a_{2}$ and $a_{_3}$ of the vector $\vec{a}$ ,are precisely the rojectio of $\vec{a}$ along -axiindaicivl.urther if $\vec{a}$ is a unit vector, then it may be expressed in terms of its direction cosines as

$$

\vec{a}=\cos\alpha\hat{i}+\cos\beta\hat{j}+\cos\gamma\hat{k}

$$

Example13Findtheanglebetween two vectors $\vec{a}$ and $\vec{b}$ with magnitudes 1 and 2respectively and when $\vec{a}\cdot\vec{b}=1$

Solution Given $\vec{a}\quad\vec{b}\quad1,\left|\vec{a}\right|\quad1\quad and\left|\vec{b}\right|\quad2$ . We have

$$

\cos^{1}\frac{\vec{a}\vec{b}}{\lfloor\vec{a}\rfloor\lfloor\vec{b}\rfloor}\quad\cos^{1}\frac{1}{2}\quad\frac{}{3}

$$

Example 14 Find angle $ ``\theta''$ between the vectors $\vec{a}=\hat{i}+\hat{j}-\hat{k}\quad and\quad\vec{b}=\hat{i}-\hat{j}+\hat{k}$

SolutoT $\vec{a}$ and $\vec{b}$ is given by

$$

\begin{aligned}&cos\theta=\frac{\vec{a}\cdot\vec{b}}{\mid\vec{a}\mid\mid\vec{b}\mid}\\ Now\quad&\vec{a}\cdot\vec{b}=(\hat{i}+\hat{j}-\hat{k})\cdot(\hat{i}-\hat{j}+\hat{k})=1-1-1=-1\\ Therefore,we have\quad&cos\theta=\frac{-1}{3}\\ hence the required angle is\quad&\theta=cos^1\quad\frac{1}{3}\end{aligned}

$$

Example 15 If $\vec{a}=5\hat{i}-\hat{j}-3\hat{k}\quad and\quad\vec{b}=\hat{i}+3\hat{j}-5\hat{k}$ , then showthat the vectors $\vec{a}+\vec{b}$ and $\vec{a}-\vec{b}$ are perpendicular.

Solution We know that two nonzero vectors are perpendicular if their scalar product is zero.

Here

and

So

$$

\begin{aligned}&\vec{a}+\vec{b}=(5\hat{i}-\hat{j}-3\hat{k})+(\hat{i}+3\hat{j}-5\hat{k})=6\hat{i}+2\hat{j}-8\hat{k}\\ &\vec{a}-\vec{b}=(5\hat{i}-\hat{j}-3\hat{k})-(\hat{i}+3\hat{j}-5\hat{k})=4\hat{i}-4\hat{j}+2\hat{k}\\ &\vec{a}(\vec{a}+\vec{b})\cdot(\vec{a}-\vec{b})=(6\hat{i}+2\hat{j}-8\hat{k})\cdot(4\hat{i}-4\hat{j}+2\hat{k})=24-8-16=0.\\ \end{aligned}

$$

Hence $\vec{a}+\vec{b}$ and $\vec{a}-\vec{b}$ are perpendicular vectors.

Example16 Findthe projection ofthe vector $\vec{a}=2\hat{i}+3\hat{j}+2\hat{k}$ on the vector

$\vec{b}=\hat{i}+2\hat{j}+\hat{k}$

Solution The projection of vector $\vec{a}$ on the vector $\left[\vec{b}\right.]$ is given by

$$

\frac{1}{\left|\vec{b}\right|}\left(\vec{a}\cdot\vec{b}\right)=\frac{\left(2\times1+3\times2+2\times1\right)}{\sqrt{\left(1\right)^{2}+\left(2\right)^{2}+\left(1\right)^{2}}}=\frac{10}{\sqrt{6}}=\frac{5}{3}\sqrt{6}.

$$

Example 17 Find $\left|\overline{\vec{a}}-\vec{b}\right|$ , if two vectors $\vec{a}$ and $\vec{b}$ are such that $|\vec{a}|\quad2,|\vec{b}|\quad3$ and $\vec{a}\cdot\vec{b}=4$

Solution We have

$$

\begin{aligned}\left|\vec{a}\quad\vec{b}\right|^2=&\left(\vec{a}-\vec{b}\right)\cdot\left(\vec{a}-\vec{b}\right)\\=&\left|\vec{a}\cdot\vec{a}-\vec{a}\cdot\vec{b}-\vec{b}\cdot\vec{a}+\vec{b}\cdot\vec{b}\right|\end{aligned}

$$

Therefore

$$

\begin{aligned}\vec{a}=&\left|\vec{a}\right|^2-2(\vec{a}\cdot\vec{b})+\left|\vec{b}\right|^2\\=&\left(2\right)^2-2(4)+\left(3\right)^2\\left|\vec{a}-\vec{b}\right|=&\sqrt{5}\end{aligned}

$$

Example 18$\mathrm{I f}^{'}\vec{a}$ is a unit vector and $\left[(\vec{x}-\vec{a})\cdot(\vec{x}+\vec{a})=8\right]$ , then find $\left[\left|\vec{x}\right|\right]$

Solution Since $\vec{a}$ is a unit vector, .$\mid\vec{a}\mid=1$ .Also,

or

or

$$

\left\{\begin{aligned}(\vec{x}-\vec{a})\cdot(\vec{x}+\vec{a})&=8\\ \vec{x}\cdot\vec{x}+\vec{x}\cdot\vec{a}-\vec{a}\cdot\vec{x}-\vec{a}\cdot\vec{a}&=8\\ \left|\vec{x}\right|^2\quad1&=8\quad i.e.\left|\vec{x}\right|^2=9\end{aligned}\right.}

$$

Therefore

$\left|\vec{x}\right|=3$ (as magnitude of a vector is non negative).

Example 19 For any two vectors $\vec{a}$ and $\vec{b}$ , we always have $|\vec{a}\cdot\vec{b}|\leq|\vec{a}||\vec{b}|$ (CauchySchwartz inequality).

Solution The inequality holds trivially when either $\vec{a}=\vec{0}\quad or\quad\vec{b}=\vec{0}$ . Actually, in such a situation we have $|\vec{a}\cdot\vec{b}|=0=|\vec{a}||\vec{b}|$ . So, let us assume that $|\vec{a}|\neq0\neq|\vec{b}|$ Then, we have

Therefore

$$

\frac{\left|\vec{a}\cdot\vec{b}\right|}{\left|\vec{a}\right|\left|\vec{b}\right|}=\left|\cos\theta\right|\leq1

$$

Example 20 For any two vectors $\vec{a}$ and $\vec{b}$ we always have $|\vec{a}+\vec{b}|\leq|\vec{a}|+|\vec{b}|(triangle inequality)$

Solution The inequality holds trivially in case either $\vec{a}=\vec{0}$ or $\vec{b}=\vec{0}$ (How?). So, let $\left|\begin{array}{ccc}\vec{a}\end{array}\right|\quad\vec{0}\quad\left|\begin{array}{c}\vec{b}\end{array}\right|$ .Then,

$$

\begin{aligned}\left|\vec{a}+\vec{b}\right|^2=&\left(\vec{a}+\vec{b}\right)^2=\left(\vec{a}+\vec{b}\right)\cdot\left(\vec{a}+\vec{b}\right)^2\\=&\left|\vec{a}\cdot\vec{a}+\vec{a}\cdot\vec{b}+\vec{b}\cdot\vec{a}+\vec{b}\cdot\vec{b}\right|\\=&\left|\vec{a}\right|^2+2\vec{a}\cdot\vec{b}+\left|\vec{b}\right|^2\\leq&\left|\vec{a}\right|^2+2\left|\vec{a}\cdot\vec{b}\right|+\left|\vec{b}\right|^2\\leq&\left|\vec{a}\right|^2+2\left|\vec{a}\right|\left|\vec{b}\right|+\left|\vec{b}\right|^2\\=&\left(\left|\vec{a}\right|\quad\left|\vec{b}\right|\right)^2\end{aligned}

$$

$$

\gtreqqless +\frac { }$ 

$$

<div style="text-align: center;">Fig 10.21</div>

(scalar product is commutative)(since $\left[x\leq|x|\forall x\in\mathbf{R}\right]$ 一(from Example 19) Hence

$$

\left|\begin{array}{l l l l}{\vec{a}}&{\vec{b}}\end{array}\right|\leq\left|\begin{array}{l l l}{\vec{a}}\end{array}\right|\quad\left|\begin{array}{l}{\vec{b}}\end{array}\right|

$$

RemrkIutiutiovex)

then

$$

\begin{aligned}|\vec{a}+\vec{b}|&=|\vec{a}|+|\vec{b}|,\\|\overrightarrow{AC}|&=|\overrightarrow{AB}|+|\overrightarrow{BC}|.\end{aligned}

$$

showing that the points A, B and C are collinear.

Example 21 Show that the points $\mathrm{A}(-2\hat{i}+3\hat{j}+5\hat{k}),\mathrm{B}(\hat{i}+2\hat{j}+3\hat{k})$ $C(7\hat{i}-k)$ are collinear.

Solution We have

Therefore

$$

\begin{aligned}\overrightarrow{AB}&=(1\quad2)\hat{i}\quad(2\quad3)\hat{j}\quad(3\quad5)\hat{k}\quad3\hat{i}\quad\hat{j}\quad2\hat{k},\\overrightarrow{BC}&=(7\quad1)\hat{i}\quad(0\quad2)\hat{j}\quad(1\quad3)\hat{k}\quad6\hat{i}\quad2\hat{j}\quad4\hat{k},\\overrightarrow{AC}&=(7\quad2)\hat{i}\quad(0\quad3)\hat{j}\quad(1\quad5)\hat{k}\quad9\hat{i}\quad3\hat{j}\quad6\hat{k},\\|\overrightarrow{AB}|&=\sqrt{14},|\overrightarrow{BC}|\quad2\sqrt{14}\quad and|\overrightarrow{AC}|\quad3\sqrt{14}\\|\overrightarrow{AC}|&=|\overrightarrow{AB}|+|\overrightarrow{BC}|\end{aligned}

$$

Hence the points A, B and C are collinear.

NoteIn Example 21, one may note that although $\overrightarrow{AB}+\overrightarrow{BC}+\overrightarrow{CA}=\overrightarrow{0}$ but the points A, B andC do not form the vertices of a triangle.

### EXERCISE 10.3

1. Findthea $\vec{b}$ with magnitudes $\sqrt{3}$ and 2 ,respectively having $\vec{a}\cdot\vec{b}=\sqrt{6}$

2. Find the angle between the vectors $\hat{i}-2\hat{j}+3\hat{k}\mathrm{a n d}3\hat{i}-2\hat{j}+\hat{k}$

3. Find the projection of the vector $\hat{i}-\hat{j}$ on the vector $\hat{i}+\hat{j}$

Find the projection of the vector $\hat{i}+3\hat{j}+7\hat{k}$ on the vector $7\hat{i}-\hat{j}+8\hat{k}$

Show that each of the given three vectors is a unit vector:

$$

\frac{1}{7}(2\hat{i}+3\hat{j}+6\hat{k}),\quad\frac{1}{7}(3\hat{i}-6\hat{j}+2\hat{k}),\quad\frac{1}{7}(6\hat{i}+2\hat{j}-3\hat{k})

$$

Also, show that they are mutually perpendicular to each other.

6. Find $\left\lfloor\vec{a}\right\rfloor$ and $\left|\vec{b}\right|,\mathrm{if}\left(\vec{a}+\vec{b}\right)\cdot\left(\vec{a}-\vec{b}\right)=8\mathrm{and}\left|\vec{a}\right|=8\left|\vec{b}\right|$

7. Evaluate the product $(3\vec{a}-5\vec{b})\cdot(2\vec{a}+7\vec{b})$

8. Find he magtudeoftwovectors $\vec{a}$ and $\vec{b}$ ,having the ame mit a such that the angle between them is $60^{\circ}$ and their scalar product is $\frac{1}{2}$

9. Find $\left[\left|\vec{x}\right|\right.\left.\right]$ , if for a unit vector $\vec{a}$ ,$\left[(\vec{x}-\vec{a})\cdot(\vec{x}+\vec{a})=12\right]$

10. If $\vec{a}=2\hat{i}+2\hat{j}+3\hat{k},\vec{b}=-\hat{i}+2\hat{j}+\hat{k}$ and $\vec{c}=3\hat{i}+\hat{j}$ are such that $\vec{a}+\lambda\vec{b}$ is perpendicular to $\left[\vec{c}\right.]$ , then find the value of λ.

11. Show that $\scriptstyle{\left|{\vec{a}}\right|{\vec{b}}+\left|{\vec{b}}\right|{\vec{a}}}$ is perpendicular to $\left|\vec{a}\right|\vec{b}-\left|\vec{b}\right|\vec{a}$ , for any two nonzero vectors $\vec{a}$ and $\vec{b}$ .

12. If $\vec{a}\cdot\vec{a}=0$ and $\vec{a}\cdot\vec{b}=0$ ,then what can be concluded about the vector $\vec{b}?$

13. If $\vec{a},\vec{b},\vec{c}$ are unit vectors such that $\vec{a}+\vec{b}+\vec{c}=\vec{0}$ ,find the value of

$\vec{a}\cdot\vec{b}+\vec{b}\cdot\vec{c}+\vec{c}\cdot\vec{a}$

14. If either vector $\vec{a}=\vec{0}\quad or\quad\vec{b}=\vec{0}.$ ,then $\vec{a}\cdot\vec{b}=0$ . But the converse need not be true. Justify your answer with an example.

15. If the vertices A, B, C of a triangle ABC are (1, 2, 3),$(-1,0,0)$ , (0, 1, 2),respectively, then find $\angle\mathrm{A B C}$ $\mathrm{[\angle ABC}]$ is the angle between the vectors $\overrightarrow{\mathrm{B A}}$ and $\overline{{\mathrm{B C}}}$ 」

16. Show that the points $A(1,2,7)$ , B(2, 6, 3) and $\mathrm{C}(3,10,-1)$ are collinear.

17. Show that the vectors $2\hat{i}-\hat{j}+\hat{k},\hat{i}-3\hat{j}-5\hat{k}\mathrm{a n d}3\hat{i}-4\hat{j}-4\hat{k}$ form the vertices of a right angled triangle.

18.$ If\vec{a}$ is a nonzero vector of magnitude (ci)$^{\ast}a^{\ast}$ and λ a nonzero scalar, then $\vec{\lambda}\vec{a}$ is unit vector if

$\lambda=1$ (B)$\lambda=-1$ (C)$a=|\lambda|$ (D)$a=1/|\lambda|$

#### 10.6.3 Vector (or cross) product of two vectors

In Section 10.2, we have discussed on the three dimensional right handed rectangular coordinate system. In this system, when the positive xaxis is rotatd counterclockwise into the positive y-axis, a right handed (standard) screw would advance inthe direction of the positive z-axis (Fig 10.22(i).

In a right handed coordinate system, the thumb of the right hand points in the direction of the positive z-axis when the fingers are curled in the direction away from the positive x-axis toward the positive y-axis (Fig 10.22(ii)).

<div style="text-align: center;"><img src="imgs/img_in_image_box_173_345_825_657.jpg" alt="Image" width="64%" /></div>

<div style="text-align: center;">Fig 10.22 (i), (ii)</div>

Dnt $\vec{b}$ , is denoted by $\vec{a}$ $\vec{b}$ and defined as

$$

\vec{a}\times\vec{b}=|\vec{a}||\vec{b}|\sin\theta\hat{n},

$$

where, θ is the angle between $\vec{a}$ and $\vec{b}$ $0\leq\theta\leq\pi$ and $\hat{n}$ is a unit vector perpendicular toboth $\vec{a}$ and $\vec{b}$ ,such that $\vec{a},\vec{b}$ and $\hat{n}$ form a right handed system (Fig 10.23). i.e., the right handedytmrotatedfrom $\vec{a}$ to $\vec{b}$ moves in the direction of $\hat{n}$

<div style="text-align: center;"><img src="imgs/img_in_image_box_722_781_915_980.jpg" alt="Image" width="19%" /></div>

<div style="text-align: center;">Fig 10.23</div>

If either $\vec{a}=\vec{0}or\vec{b}=\vec{0}$ , then θ is not defined and in this case, we define $\vec{a}\times\vec{b}=\vec{0}$

## Observations

1.$\vec{a}\times\vec{b}$ is a vector.

2. Let $\vec{a}$ and $\vec{b}$ be two nonzero vectors. Then $\vec{a}\times\vec{b}=\vec{0}$ if and only if $\vec{a}$ and $\vec{b}$ are parallel (or collinear) to each other, i.e.,

$$

\vec{a}\times\vec{b}=\vec{0}\Leftrightarrow\vec{a}\mid\vec{b}

$$

In particular,$\vec{a}\times\vec{a}=\vec{0}\quad and\quad\vec{a}\times(-\vec{a})=\vec{0}$ , since in the first situation,$\Theta=0$ and in the second one,$\Theta=\pi$ , making the value of sin θ to be 0.

3. If - then $\vec{a}\quad\vec{b}\quad\left|\vec{a}\right|\left|\vec{b}\right|.$ 2

4. In view of the Observations 2 and 3, for mutually perpendicular unit vectors $\hat{i},\hat{j}$ and $\hat{k}$ (Fig 10.24), we have

$$

\begin{aligned}&\hat{i}\times\hat{i}=\hat{j}\times\hat{j}=\hat{k}\times\hat{k}=\vec{0}\\ &\hat{i}\times\hat{j}=\hat{k},\quad\hat{j}\times\hat{k}=\hat{i},\quad\hat{k}\times\hat{i}=\hat{j}\\ \end{aligned}

$$

<div style="text-align: center;"><img src="imgs/img_in_image_box_760_286_900_456.jpg" alt="Image" width="13%" /></div>

<div style="text-align: center;">Fig 10.24</div>

5. In terms of vector product, the angle between two vectors $\vec{a}$ $\vec{b}$ may be given as

$$

\sin\theta=\frac{\left|\vec{a}\times\vec{b}\right|}{\left|\vec{a}\right|\left|\vec{b}\right|}

$$

6. It is always true that the vector product is not commutative, as $\vec{a}\times\vec{b}=-\vec{b}\times\vec{a}$ Indeed,$\vec{a}\times\vec{b}=\left|\vec{a}\right|\left|\vec{b}\right|$ sin $\uptheta\hat{n}$ ,where $\vec{a},\vec{b}$ and $\hat{n}$ form a right handed system,i.e., θ is traversed from $\vec{a}$ to $\vec{b}$ , Fig 10.25 (i). While,$\vec{b}\times\vec{a}=|\vec{a}||\vec{b}|\sin\theta\hat{n}_1$ , where $\left[\vec{b},\vec{a}\right.]$ and $\hat{n}_{1}$ form a right handed system i.e. θ is traversed from $\left[\vec{b}\right.]$ to $\vec{a}$ ,Fig 10.25(ii).

<div style="text-align: center;"><img src="imgs/img_in_image_box_171_880_427_1136.jpg" alt="Image" width="25%" /></div>

<div style="text-align: center;">(i)</div>

<div style="text-align: center;">Fig 10.25 (i), (ii)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_635_980_897_1106.jpg" alt="Image" width="25%" /></div>

<div style="text-align: center;">(ii)</div>

Thus, if we assume $\vec{a}$ and $\vec{b}$ toleo $\hat{n}$ and $\hat{n}_{1}$ both willt,$\left[\hat{n}\right.]$ being directed above the paper while $\hat{n}_{1}$ directed below the paper. i.e.$\hat{n}_{1}=-\hat{n}$

Hence

$$

\begin{aligned}\left\{\vec{a}\times\vec{b}\right\}&=\left|\vec{a}\right|\left|\vec{b}\right|\sin\hat{n}\\&=-\left|\vec{a}\right|\left|\vec{b}\right|\sin\theta\hat{n}_1=-\vec{b}\times\vec{a}\end{aligned}7.In view of the Observations 4 and 6, we have 

$$

$\begin{aligned}\left\{\vec{a}\times\vec{b}\right\}&=\left|\vec{a}\right|\left|\vec{b}\right|\sin\hat{n}\\&=-\left|\vec{a}\right|\left|\vec{b}\right|\sin\theta\hat{n}_1=-\vec{b}\times\vec{a}\end{aligned}$ 7. In view of the Observations 4 and 6, we have

$$

\hat{j}\times\hat{i}=-\hat{k},\quad\hat{k}\times\hat{j}=-\hat{i}\quad\mathrm{a n d}\quad\hat{i}\times\hat{k}=-\hat{j}.

$$

8. If $\vec{a}$ and $\vec{b}$ $\frac{1}{2}\left|\vec{a}\quad\vec{b}\right|.$ C

<div style="text-align: center;"><img src="imgs/img_in_image_box_653_425_916_581.jpg" alt="Image" width="26%" /></div>

<div style="text-align: center;">Fig 10.26</div>

By definition of the area of a triangle, we have from Fig 10.26,

Area of triangle $\mathrm{ABC}=\frac{1}{2}\mathrm{AB}\cdot\mathrm{CD}.$

But $\mathrm{AB}=|\vec{b}|$ (as given), and $\mathrm{CD}=\left|\vec{a}\right|\sin\theta$

Thus, Area of triangle $\mathrm{ABC}=\frac{1}{2}\left|\vec{b}\right|\left|\vec{a}\right|\sin\theta=\frac{1}{2}\left|\vec{a}\times\vec{b}\right|$

9. If $\vec{a}$ and $\vec{b}$ represent theajactdeofaparallogram,thenitsarea is given by $|\vec{a}\times\vec{b}|$ D C

From Fig 10.27, we have

Area of parallelogram $\mathrm{ABCD}=\mathrm{AB}.\mathrm{DE}$

$$

 凡

$$

But $AB=|\vec{b}|$ (as given), and

$$

\mathrm{DE}=|\vec{a}|\sin\theta 

$$

Thus,

<div style="text-align: center;">Fig 10.27</div>

Area of parallelogram $\mathrm{ABCD}=\left|\vec{b}\right|\left|\vec{a}\right|\sin\theta=\left|\vec{a}\times\vec{b}\right|$

We now state two important properties of vector product.

Property 3 (Distributivity of vector product over addition): If $\vec{a},\vec{b}$ and $\vec{c}$ are any three vectors and $\lambda$ be a scalar, then

(i)

$$

\vec{a}\times(\vec{b}+\vec{c})=\vec{a}\quad\vec{b}\quad\vec{a}\quad\vec{c}

$$

(ii)$\lambda(\vec{a}\times\vec{b})=(\lambda\vec{a})\times\vec{b}=\vec{a}\times(\lambda\vec{b})$

Let $\vec{a}$ and $\vec{b}$ be two vectors given in component form as $a_{1}\hat{i}+a_{2}\hat{j}+a_{3}\hat{k}$ and $b_{1}\hat{i}+b_{2}\hat{j}+b_{3}\hat{k}$ , respectively. Then their cross product may be given by

$$

\vec{a}\times\vec{b}=\left|\begin{matrix}{\hat{i}}&{\hat{j}}&{\hat{k}}\\ {a_{1}}&{a_{2}}&{a_{3}}\\ {b_{1}}&{b_{2}}&{b_{3}}\end{matrix}\right|

$$

Explanation We have

$$

\begin{aligned}\vec{a}\times\vec{b}&=(a_1\hat{i}+a_2\hat{j}+a_3\hat{k})\times(b_1\hat{i}+b_2\hat{j}+b_3\hat{k})\\&=a_1b_1(\hat{i}\times\hat{i})+a_1b_2(\hat{i}\times\hat{j})+a_1b_3(\hat{i}\times\hat{k})+a_2b_1(\hat{j}\times\hat{i})\\&\quad+a_2b_2(\hat{j}\times\hat{j})+a_2b_3(\hat{j}\times\hat{k})\\&\quad+a_3b_1(\hat{k}\times\hat{i})+a_3b_2(\hat{k}\times\hat{j})+a_3b_3(\hat{k}\times\hat{k})\quad(by Property1)\\&=a_1b_2(\hat{i}\times\hat{j})-a_1b_3(\hat{k}\times\hat{i})-a_2b_1(\hat{j}\times\hat{k})\\&\quad+a_2b_3(\hat{j}\times\hat{k})+a_3b_1(\hat{k}\times\hat{i})-a_3b_2(\hat{j}\times\hat{k})\\vec{b}&(as\hat{i}\times\hat{i}=\hat{j}\times\hat{j}=\hat{k}\times\hat{k}=0and\hat{i}\times\hat{k}=-\hat{k}\times\hat{i},\hat{j}\times\hat{i}=-\hat{i}\times\hat{j}and\hat{k}\times\hat{j}=-\hat{j}\times\hat{k})\\&=a_1b_2\hat{k}-a_1b_3\hat{j}-a_2b_2\hat{k}+a_2b_3\hat{i}+a_3b_1\hat{j}-a_3b_2\hat{i}\\&\quad(as\hat{i}\times\hat{j}=\hat{k},\hat{j}\times\hat{k}=\hat{i}and\hat{k}\times\hat{i}=\hat{j})\\&=(a_2b_3-a_3b_2)\hat{i}-(a_1b_3-a_3b_1)\hat{j}+(a_1b_2-a_2b_1)\hat{k}\\&=\begin{vmatrix}\hat{i}&\hat{j}&\hat{k}\\a_1&a_2&a_3\\b_1&b_2&b_3\end{vmatrix}\end{aligned}

$$

Example 22 Find $|\vec{a}\times\vec{b}|$ ,if $\vec{a}=2\hat{i}+\hat{j}+3\hat{k}$ and $\vec{b}=3\hat{i}+5\hat{j}-2\hat{k}$ Solution We have

Hence

$$

\begin{aligned}\vec{a}\times\vec{b}&=\left|\begin{matrix}\hat{i}&\hat{j}&\hat{k}\\2&1&3\\3&5&-2\end{matrix}\right|\\&=\hat{i}(-2-15)-(-4-9)\hat{j}+(10-3)\hat{k}=-17\hat{i}+13\hat{j}+7\hat{k}\\left|\vec{a}\cdot\vec{b}\right|&=\sqrt{(-17)^{2}+(13)^{2}+(7)^{2}}=\sqrt{507}\end{aligned}

$$

Example 23 Find a unit vector perpendicular to each of the vectors $(\vec{a}+\vec{b})$ and $(\vec{a}-\vec{b})$ J, where $\vec{a}=\hat{i}+\hat{j}+\hat{k},\quad\vec{b}=\hat{i}+2\hat{j}+3\hat{k}$

Solution We have $\vec{a}+\vec{b}=2\hat{i}+3\hat{j}+4\hat{k}and\vec{a}-\vec{b}=-\hat{j}-2\hat{k}$

A vector which is perpendicular to both $\vec{a}+\vec{b}and\vec{a}-\vec{b}$ is given by

$$

\left|\vec{a}+\vec{b}\right|\times\left(\vec{a}-\vec{b}\right)=\left|\begin{matrix}\hat{i}&\hat{j}&\hat{k}\\ 2&3&4\\ 0&-1&-2\end{matrix}\right|=-2\hat{i}+4\hat{j}-2\hat{k}\quad(=\vec{c},\quad xy) ublish 

$$

Now

$$

|\vec{c}|=\sqrt{4+16+4}=\sqrt{24}=2\sqrt{6} ublish 

$$

Therefore, the required unit vector is

$$

\frac{\vec{c}}{\left|\vec{c}\right|}=\frac{-1}{\sqrt{6}}\hat{i}+\frac{2}{\sqrt{6}}\hat{j}-\frac{1}{\sqrt{6}}\hat{k} ublish 

$$

NoteThere are two perpendicular directions to any plane. Thus, another unit ublish vector perpendicular to $\vec{a}+\vec{b}$ and $\vec{a}-\vec{b}$ will be $\frac{1}{\sqrt{6}}\hat{i}-\frac{2}{\sqrt{6}}\hat{j}+\frac{1}{\sqrt{6}}\hat{k}$ But that will be a consequence of $(\vec{a}-\vec{b})\times(\vec{a}+\vec{b})$

Example 24 Find the area of a triangle having the points A(1, 1, 1), B(1, 2, 3)and C(2, 3, 1) as its vertices.1

is S 。$$

 ve $\overrightarrow{AB}=\hat{j}+2\hat{k}and\overrightarrow{AC}=\hat{i}+2\hat{j}$ . The area of the given triangle

Now,

$$\overrightarrow{AB}\times\overrightarrow{AC}=\left|\begin{aligned}\hat{i}\quad&\hat{j}\quad&\hat{k}\\ 0\quad&1\quad&2\\ 1\quad&2\quad&0\end{aligned}\right|=-4\hat{i}+2\hat{j}-\hat{k}

$$

herefore

$$

\left|\overrightarrow{AB}\times\overrightarrow{AC}\right|=\sqrt{16+4+1}=\sqrt{21}

$$

Thus, the required area is $\frac{1}{2}\sqrt{21}$

Example 25 Find the area of a parallelogram whose adjacent sides are given by the vectors $\vec{a}=3\hat{i}+\hat{j}+4\hat{k}and\vec{b}=\hat{i}-\hat{j}+\hat{k}$

by So $|\vec{a}\times\vec{b}|$ The area of a parallelogram with $\vec{a}$ and $\vec{b}$ as its adaent dds iver as its adjacent sides is given

Now

$$

\vec{a}\times\vec{b}=\left|\begin{matrix}\hat{i}&\hat{j}&\hat{k}\\ 3&1&4\\ 1&-1&1\end{matrix}\right|=5\hat{i}+\hat{j}-4\hat{k}

$$

Therefore

$$

|\vec{a}\times\vec{b}|=\sqrt{25+1+16}=\sqrt{42}

$$

and hence, the required area is $\sqrt{42}$

### EXERCISE 10.4

1. Find $\left|\vec{a}\times\vec{b}\right|$ ,if $$

2. Find a unit vector perpendicular to each of the vector vector $$

 .and 

$$ , where

$\vec{a}=3\hat{i}+2\hat{j}+2\hat{k}and\vec{b}=\hat{i}+2\hat{j}-2\hat{k}$

3. If a unit vector $\vec{a}$ makes angles $\frac{\pi}{3}\mathrm{with}\hat{i},\frac{\pi}{4}$ with $\hat{j}$ and an acute angle θ with $\hat{k}$ , then find θ and hence, the components of $\vec{a}$

Show that

$$

\left(\vec{a}-\vec{b}\right)\times\left(\vec{a}+\vec{b}\right)=2\left(\vec{a}\times\vec{b}\right)

$$

5. Find λ and if $(2\hat{i}+6\hat{j}+27\hat{k})\times(\hat{i}+\lambda\hat{j}+\mu\hat{k})=\vec{0}$

Given that $\vec{a}\vec{b}\quad0$ and $\vec{a}\times\vec{b}=\vec{0}$ . What can you conclude about the vectors ā ann $\vec{b}?$

7. Let the vectors $\vec{a},\vec{b},\vec{c}$ be given as $a_{1}\hat{i}+a_{2}\hat{j}+a_{3}\hat{k},\;b_{1}\hat{i}+b_{2}\hat{j}+b_{3}\hat{k}$ $c_{1}\hat{i}+c_{2}\hat{j}+c_{3}\hat{k}$ . Then show that $\vec{a}\times(\vec{b}+\vec{c})=\vec{a}\times\vec{b}+\vec{a}\times\vec{c}$

8. If either $\vec{a}=\vec{0}\quad or\quad\vec{b}=\vec{0}$ ,then $\vec{a}\times\vec{b}=\vec{0}$ . Is the converse true? Justify your answer with an example.

9. Find theareaof thetriangle with vertices A(1,1,2), B(2,3,5) and C(1,5, 5.

10. Find the area of the parallelogram whose adjacent sides are determined by the

vectors $\vec{a}=\hat{i}-\hat{j}+3\hat{k}and\vec{b}=2\hat{i}-7\hat{j}+\hat{k}$

"

11. Let the vectors $\vec{a}$ and $\vec{b}$ be such that $\left|\vec{a}\right|=3$ and $\left|\vec{b}\right|=\frac{\sqrt{2}}{3}$ ,then $\vec{a}\times\vec{b}$ is a unit vector, if the angle between $\vec{a}$ and $\vec{b}$ is

(A)$\pi/6$ Ta (B)$\pi/4$ EM (C)$\pi/3$ EM (D)$\pi/2$ 2

12. Area of a rectangle having vertices A, B, C and D with position vectors $-\hat{i}+\frac{1}{2}\hat{j}+4\hat{k},\hat{i}+\frac{1}{2}\hat{j}+4\hat{k},\hat{i}-\frac{1}{2}\hat{j}+4\hat{k}\mathrm{a n d}-\hat{i}-\frac{1}{2}\hat{j}+4\hat{k}$ , respectively is S

(A)$\frac{1}{2}$ (B)1(C)2(D)4

## Miscellaneous Examples

Example 26 Write all the unit vectors in XY-plane.

Solution Let $\vec{r}=x\hat{i}+y\hat{j}$ be a unit vector in XY-plane (Eig 10 28) Then fromth b figure, we have $$

 and $y=\sin\theta\left(\operatorname{since}|\vec{r}|=1\right)$ b 1. So, we may write the vector $\left[\vec{r}\right.]$ as Clearly,

$$\vec{r}\left(=\overrightarrow{OP}\right)=\cos\hat{i}\sin\hat{j}

$$

$$

\overrightarrow{OP'}=\cos\theta\dot{i}

$$

$$

\mathrm{X^{\prime}\ll}

$$

$$

\overrightarrow{P^{\prime}P}=\sin\theta\hat{j}

$$

<div style="text-align: center;">80010</div>

Also, as θ varies from 0 to 2, the point P (Fig 10.28) traces the circle $x^{2}+y^{2}=1$ counterclockwise, and this covers all possible directions. So, 1) gives every unit vector in the XY-plane.

Example 27 If $\begin{array}{r}{\left[\hat{i}\quad\hat{j}\quad\hat{k},2\hat{i}\quad5\hat{j},3\hat{i}\quad2\hat{j}\quad3\hat{k}\quad\mathrm{a n d}\quad\hat{i}\quad6\hat{j}\quad\hat{k}\right.}\end{array}]$ arethe position vectors of points A, B, C and D respectively, then find the angle between $\overrightarrow{\mathbf{AB}}$ and $\overrightarrow{\mathrm{C D}}$ . Deduce that $\overrightarrow{\mathbf{A B}}$ and $\overrightarrow{\mathrm{C D}}$ are collinear.

Solution Note that if θ is the angle between AB and CD, then θ is also the angle between $\overrightarrow{\mathbf{A B}}$ and $\overrightarrow{\mathrm{C D}}$

Now

Therefore

Similarly

Thus

$$

\begin{aligned}\overrightarrow{AB}&=\overrightarrow{\mathrm{position}}\text{vector of B}-\overrightarrow{\mathrm{position}}\text{vector of}\\&=\left(2\hat{i}+5\hat{j}\right)-\left(\hat{i}+\hat{j}+\hat{k}\right)=\hat{i}+4\hat{j}-\hat{k}\\left|\overrightarrow{AB}\right|&=\sqrt{\left(1\right)^{2}+\left(4\right)^{2}+\left(-1\right)^{2}}=3\sqrt{2}\\overrightarrow{CD}&=-2\hat{i}-8\hat{j}+2\hat{k}\text{and}|\overrightarrow{CD}|=6\sqrt{2}\\cos\theta&=\frac{\overrightarrow{AB}\overrightarrow{CD}}{|\overrightarrow{AB}||\overrightarrow{CD}|}\\&=\frac{1(-2)+4(-8)+(-1)(2)}{(3\sqrt{2})(6\sqrt{2})}=\frac{-36}{36}=-1\end{aligned}

$$

Since $0\leq\theta\leq\pi$ , it follows that $\Theta=\pi$ . This shows that $\overrightarrow{A B}$ and $\overline{{\mathrm{C D}}}$ are collinear.

Alternatively,$\overrightarrow{AB}-\frac{1}{2}\overrightarrow{CD}$ which implies that $\overrightarrow{\mathrm{A B}}\mathrm{a n d}\overrightarrow{\mathrm{C D}}$ are collinear vectors.

Example 28 Let $\vec{a},\vec{b}$ and cbe three vectors such that $\left|\vec{a}\right|=3,\left|\vec{b}\right|=4,\left|\vec{c}\right|=5$ and $\scriptstyle|{\vec{a}}+{\vec{b}}+{\vec{c}}|$

Solution Given $\vec{a}\cdot(\vec{b}+\vec{c})=0,\vec{b}\cdot(\vec{c}+\vec{a})=0,\vec{c}\cdot(\vec{a}+\vec{b})=0.$

Now

Therefore

$$

\begin{aligned}\left|\vec{a}+\vec{b}+\vec{c}\right|^2=&\left(\vec{a}+\vec{b}+\vec{c}\right)^2=\left(\vec{a}+\vec{b}+\vec{c}\right)\cdot\left(\vec{a}+\vec{b}+\vec{c}\right)^2\\=&\left.\vec{a}\cdot\vec{a}+\vec{a}\cdot\left(\vec{b}+\vec{c}\right)+\vec{b}\cdot\vec{b}+\vec{b}\cdot\left(\vec{a}+\vec{c}\right)\right.\\&+\left.\vec{c}.\left(\vec{a}+\vec{b}\right)+\vec{c}.\vec{c}\right.\\=&\left.\left|\vec{a}\right|^2+\left|\vec{b}\right|^2+\left|\vec{c}\right|^2\right.\\=&\left.9+16+25=50\right.\\left|\vec{a}+\vec{b}+\vec{c}\right|=&\left.\sqrt{50}=5\sqrt{2}\right.\end{aligned}

$$

Example 29 Three vectors $\vec{a},\vec{b}$ and $\vec{c}$ satisfy the condition $\vec{a}+\vec{b}+\vec{c}=\vec{0}$ . Evaluate the quantity $\mu=\vec{a}\cdot\vec{b}+\vec{b}\cdot\vec{c}+\vec{c}\cdot\vec{a},\quad if\quad|\vec{a}|=1,\quad|\vec{b}|=4\quad and\quad|\vec{c}|=2$ Ta Solution Since $\vec{a}+\vec{b}+\vec{c}=\vec{0}$ , we have

$$

\vec{a}(\vec{a}\vec{b}\vec{c})=0

$$

or

$$

\vec{a}\cdot\vec{a}+\vec{a}\cdot\vec{b}+\vec{a}\cdot\vec{c}=0

$$

Therefore

$$

\left|\vec{a}\cdot\vec{b}+\vec{a}\cdot\vec{c}\right|=-\left|\vec{a}\right|^2=-1

$$

Again,

$$

\vec{b}\cdot\left(\vec{a}+\vec{b}+\vec{c}\right)=0

$$

or

$$

\left[\vec{a}\cdot\vec{b}+\vec{b}\cdot\vec{c}\right]=-\left|\vec{b}\right|^2=-16

$$

Similarly

$$

\vec{a}\cdot\vec{c}+\vec{b}\cdot\vec{c}=-4.

$$

Adding (1), (2) and (3), we have

or

$$

2\left(\vec{a}\cdot\vec{b}+\vec{b}\cdot\vec{c}+\vec{a}\cdot\vec{c}\right)=-21,\quad\frac{-21}{2}

$$

t handed sytem of mutully erdiclr unit vectors $\hat{i},\hat{j}$ and $\vec{k},\vec{\alpha}=3\hat{i}-\hat{j},\vec{\beta}=2\hat{i}+\hat{j}-3\hat{k}$ ,then express $\vec{\upbeta}$ in the form $\begin{array}{r}\rightarrow\quad\rightarrow\quad\rightarrow\\1\quad2\end{array}$ , where $\begin{array}{c}\rightarrow\\1\end{array}$ is parallel $to\quad and\quad2$ is perpendicular to $\vec{ 処 }$

Solution Let $\begin{array}{ccc}\rightarrow&&\\&1&\end{array}\rightarrow$ is a scalar, i.e.,$\vec{\beta}_{1}=3\lambda\hat{i}-\lambda\hat{j}$

Now

$$

\vec{\beta}_{2}=\vec{\beta}-\vec{\beta}_{1}=(2-3\lambda)\hat{i}+(1+\lambda)\hat{j}-3\hat{k}.

$$

Now, since $\vec{\beta}_{2}$ is to be perpendiculr o $\vec{\upalpha}$ , we should have $\vec{\alpha}\cdot\vec{\beta}_{2}=0$ .i.e.,

or

Therefore

$$

\begin{aligned}\sqrt{3}(2-3\lambda)-(1+\lambda)&=0\\lambda&=\frac{1}{2}\\vec{\beta}_{1}&=\frac{3}{2}\hat{i}-\frac{1}{2}\hat{j}\quad and\quad\vec{\beta}_{2}=\frac{1}{2}\hat{i}+\frac{3}{2}\hat{j}-3\hat{k}\end{aligned}

$$

## Miscellaneous Exercise on Chapter 10

1. WritewtiXY-plieof0wteitive direction of x-axis.

2. Find the scalar components and magnitude of the vector joining the points EM $\mathrm{P}(x_{1},y_{1},z_{1})and\mathrm{Q}(x_{2},y_{2},z_{2})$ 添司

3. Airl k4kmtwas ,thewkkmiirection $30^{\circ}$ east of north and stops. Determine the girl's displacementfrom her initial point of departure.

4. If $\vec{a}=\vec{b}+\vec{c}$ ,then is it true that $\left|\vec{a}\right|=\left|\vec{b}\right|+\left|\vec{c}\right|?$ Justify your answer.

5. Find the value of x for which $x(\hat{i}+\hat{j}+\hat{k})$ is a unit vector.

6. Find a vector of magnitude 5 units, and parallel to the resultant of the vectors

$\vec{a}=2\hat{i}+3\hat{j}-\hat{k}\quad and\quad\vec{b}=\hat{i}-2\hat{j}+\hat{k}$

7. If $\vec{a}=\hat{i}+\hat{j}+\hat{k},\quad\vec{b}=2\hat{i}-\hat{j}+3\hat{k}\quad and\quad\vec{c}=\hat{i}-2\hat{j}+\hat{k}$ ,find a unit vector parallel to the vector $2\vec{a}-\vec{b}+3\vec{c}$

8. Show that the points $\mathrm{A}(1,-2,-8)$ 1,$ B\left(5,0,-2\right)$ and C(11, 3, 7) are collinear, and find the ratio in which B divides AC.

9. Find the position vector of a point R which divides the line joining two points P and Q whose position vectors are $(2\vec{a}+\vec{b})\mathrm{a n d}(\vec{a}-3\vec{b})$ externally in the ratio 1 : 2. Also, show that P is the mid point of the line segment RQ.

10. The two adjacent sides of a parallelogram are $2\hat{i}-4\hat{j}+5\hat{k}\mathrm{a n d}\hat{i}-2\hat{j}-3\hat{k}$ Find the unit vector parallel to its diagonal. Also, find its area.

11. Show that the direction cosines of a vector equally inclined to the axes OX, OY and OZ are $\frac{1}{\sqrt{3}},\frac{1}{\sqrt{3}},\frac{1}{\sqrt{3}}$

12. Let $\vec{a}=\hat{i}+4\hat{j}+2\hat{k},\quad\vec{b}=3\hat{i}-2\hat{j}+7\hat{k}$ and $\vec{c}=2\hat{i}-\hat{j}+4\hat{k}$ .Findavector $\left[\vec{d}\right.]$ which is perpendicular to both $\vec{a}$ and $\vec{b}$ , and $\vec{c}\cdot\vec{d}=15$

13. The scalar product of the vector $\hat{i}+\hat{j}+\hat{k}$ with a unit vector along the sum of vectors $2\hat{i}+4\hat{j}-5\hat{k}\mathrm{a n d}\lambda\hat{i}+2\hat{j}+3\hat{k}$ is equal to one. Find the value of λ.

14. If $\vec{a},\vec{b},\vec{\mathfrak{c}}$ are mutually perpendicular vectors of equal magnitudes, show that the vector $\vec{a}+\vec{b}+\vec{c}$ is equally inclined to $\vec{a},\vec{b}$ and $\vec{c}$ .

15. Prove that $(\vec{a}+\vec{b})\cdot(\vec{a}+\vec{b})=|\vec{a}|^2+|\vec{b}|^2$ , if and only if $\vec{a},\vec{b}$ are perpendicular,given $\vec{a}\neq\vec{0},\vec{b}\neq\vec{0}$

Choose the correct answer in Exercises 16 to 19.

16. If $\vec{a}$ and $\vec{b}$ , then $\vec{a}\cdot\vec{b}\geq0$ only when

(A)$0<\theta<\frac{\pi}{2}$ (B)$0\leq\theta\leq\frac{\pi}{2}$ (C)$0<\theta<\pi$ (D)$0\leq\Theta\leq\pi$

$\vec{b}$

$\vec{a}+\vec{b}$

is a unit vector if

(A)$\theta=\frac{\pi}{4}$ (B)$\theta=\frac{\pi}{3}$ (C)$\theta=\frac{\pi}{2}$ (D)$\theta=\frac{2\pi}{3}$

18. The value of $\hat{i}.(\hat{j}\quad\hat{k})\quad\hat{j}\quad(\hat{i}\quad\hat{k})$ $kk$$

(\hat{i}\quad\hat{j})$ is

(A)0(B)-1(C) 1

19. If θ is the angle between any two vectors $\vec{a}$ $\vec{b}$ 1$|\vec{a}\cdot\vec{b}|=|\vec{a}\times\vec{b}|$ when θ is equal to

(A)0(B)$\frac{\pi}{4}$ $\frac{\pi}{2}$ (D)π

## Summary

Position vector of a point $\mathrm{P}(x,y,z)$ isgiven as $\overrightarrow{OP}(=\vec{r})=x\hat{i}+y\hat{j}+z\hat{k}$ , and its magnitude by $\sqrt{x^{2}+y^{2}+z^{2}}$

The scalar components of a vector are its direction ratios, and represent its projections along the respective axes.

The magntude(),diction ratios $(a,b,c)$ and direction cosines $(l,m,n)$ of any vector are related as:

$$l=\frac{a}{r},\quad m=\frac{b}{r},\quad n=\frac{c}{r}

$$

The vector sum of the three sides of a triangle taken in order is $\left[{\vec{0}}\right.]$

The vector sum of two coinitial vectors is given by the diagonal of the parallelogram whose adjacent sides are the given vectors.

❤The multiplicationofagivenvector by a scalar $\lambda,$ changes the magnitude of the vector by the multiple $|\lambda|$ and keeps the direction same (or makes it opposite) according as the value ofλ is positive (or negative).

❤For a given vector .$\vec{a}$ , the vector $\hat{a}=\frac{\vec{a}}{|\vec{a}|}$ gives the unit vector in the direction of $\vec{a}$

■The position vector of a point R dividing a line segment joining the points P and Q whose position vectors are $\vec{a}$ and $\vec{b}$ respectively, in the ratio m: n

(i)internally, is given by $\frac{n{\vec{a}}+m{\vec{b}}}{m+n}$

(i)externally, is given by $\frac{m{\vec{b}}-n{\vec{a}}}{m-n}$

■The scalar product of two given vectors $\vec{a}$ and $\vec{b}$ having angle θ between them is defined as

$$

\vec{a}\cdot\vec{b}=|\vec{a}||\vec{b}|\cos\theta.

$$

Also, when ${\vec{a}}\cdot{\vec{b}}$ is given, the angle $ ``\Theta''$ between the vectors $\vec{a}$ and $\vec{b}$ may be determined by

$$

\cos\theta=\frac{\vec{a}\cdot\vec{b}}{\left|\vec{a}\right|\left|\vec{b}\right|}

$$

Ifθis the angle betweentwovecors $\vec{a}$ and $\vec{b}$ , then their cross product is given as

$$

\vec{a}\times\vec{b}=|\vec{a}||\vec{b}|\sin\theta\hat{n}

$$

where $\hat{n}$ is a unit vecor prpdiculartohelanecoaiing $\vec{a}$ and $\vec{b}$ .Such that $\vec{a},\vec{b}$ , n form right handed system of coordinate axes.

If we have two vectors $\vec{a}$ and $\vec{b}$ ,given in component form as $\vec{a}=a_{1}\hat{i}+a_{2}\hat{j}+a_{3}\hat{k}$ and $\vec{b}=b_{1}\hat{i}+b_{2}\hat{j}+b_{3}\hat{k}$ and $\lambda$ any scalar,

$$

\begin{aligned}\text{then}\quad\vec{a}+\vec{b}&=\left(a_{1}+b_{1}\right)\hat{i}+\left(a_{2}+b_{2}\right)\hat{j}+\left(a_{3}+b_{3}\right)\hat{k};\\lambda\vec{a}&=\left(\lambda a_{1}\right)\hat{i}+\left(\lambda a_{2}\right)\hat{j}+\left(\lambda a_{3}\right)\hat{k};\\vec{a}.\vec{b}&=a_{1}b_{1}+a_{2}b_{2}+a_{3}b_{3};\\text{and}\quad\vec{a}\times\vec{b}&=\left|\begin{aligned}\hat{i}&\quad\hat{j}&\quad\hat{k}\\a_{1}&\quad b_{1}&\quad c_{1}\\a_{2}&\quad b_{2}&\quad c_{2}\end{aligned}\right|.\end{aligned}$$

## Historical Note

The word vector has been derived from a Latinword vectus,which means "to carry". The germinal ideas of modern vector theory date from around 1800whenCasparWessel(1745-1818) andJean Robert Argand (1768-1-1822)described that how a complex number $a+i b$ could be given ageometric interpretation with the help of a directed line segment in a coordinate plane.William R Rowen Hamilton (1805-1865) an Irish mathematician was the first to use the term vector for a directed line segment in his bookLectureson Quaternions (1853).Hamilton's method of quaternions(an ordered set of four real numbers given as:

$a+b\hat{i}+c\hat{j}+d\hat{k},\hat{i},\hat{j},\hat{k}$ following certain algebraic rules)was a solution to the problem of multiplying vectors in three dimensional space.Though,we must mention here that in practice,1the idea of vector concept and their addition was known much earlier ever since the time of Aristotle (384-322B.C.),a Greek philosophe,and pupl ofPlao (427-348B.C.).That time it was supposed to be known that the combined action of two or more forces could be seen by adding them according to parallelogram law.The correct law for the composition of forces, that forces add vectorially, had been discovered in the case of perpendicular forces by Stevin-Simon (1548-1620).In 1586A.D.,he analysed the principle of geometric addition of forces in his treatise DeBeghinselen der Weeghconst (“Principles of the Art of Weighing"),which caused a major bakough in the development ofmechanics.But it took another 200years for the general concept of vectors to form.

In the 1880,, Josaih Willard Gibbs (1839-1903), an American physicist and mathematician, and Oliver Havii(-), a glih gr, catd what we now know as vector analysis, essentially by separating the real (scalar) part ofquaternionfrom itsimaginary (vector)part.In188land1884,Gibbs nottoberepublishe theapplicatioovrsisduteD.HaviiandPG.Tat83-101)printed atreatiseentitled ElementofVectorAnalysis.Thisbookgaveasystematic and concise account of vectors. However, much of the credit for demonstrating who contributed significantly to this subject.

