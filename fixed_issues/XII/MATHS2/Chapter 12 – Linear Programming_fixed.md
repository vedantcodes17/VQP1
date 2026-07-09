

# LINEAR PROGRAMMING

出The mathematical experienceof thestudent isincompleteif he never had the opportunitytosolvea problem invented byhimself.– G.POLYA

### 12.1 Introduction

In earlier classes, we have discussed systems of linear equations and their applications in day to day problems. In Class XI, we have studied linear inequalities and systems of linear inequalities in two variables and their solutions by graphical method. Many applications in mathematics involve systems of inequalities/equations. In this chapter,we shall apply the systems of linear inequalities/equations to solve some real life problems of the type as given below:

A furniture dealer deals in only two items–tables and chairs. He has Rs 50,000 to invest and has storage space of at most 60 pieces. A table costs Rs 2500 and a chair Rs 500. He estimates that from the sale of one table, he can make a profit of Rs 250 and that from the sale of one

<div style="text-align: center;"><img src="imgs/img_in_image_box_683_551_942_882.jpg" alt="Image" width="25%" /></div>

<div style="text-align: center;">L. Kantorovich </div>

chair a profit of Rs 75. He wants to know how many tables and chairs he should buy from the available money so as to maximise his total profit, assuming that he can sell all the items which he buys.

Such type of m k ii, i t, st) frm a general classof problems called optimisation problems. Thus, an optimisation problem may involve finding maximum profit, minimum cost, or minimum use of resources etc.

A problem.he above taed ptimiin problm i an exame oliar programming problem. Linear programming problems are of much interest because of their wide applicability in industry, commerce, management science etc.

In this chapter, we shall study some linear programming problems and their solutions by graphical method only, though there are many other methods also to solve such problems.

### 12.2 Linear Programming Problem and its Mathematical Formulation

We begin our discussion with the above example of furniture dealer which will further leadto a mmial rmulioe pobminti.Itis example, e observe

(i)The dealer can invest his money in buying tables or chairs or combination thereof.Further he would earn different profits by following different investment strategies.

(iThere recrtiveridnonditionoronstraintsviz.hisinvestment is limited to a maximum of Rs 50,000 and so is his storage space which is for a maximum of 60 pieces.

Suppose he decides to buy tables only and no chairs, so hecan buy $50000\div2500$ i.e., 20 tables. His profit in this case will be Rs $(250\times20)$ ), i.e., Rs 5000.

Suppose he chooses to buy chairs only and no tables. With his capital of Rs 50,000,he can buy $50000\div500$ ,i.e.100 chairs.But he can store only 60 pieces.Therefore, he is forced to buy only 60 chairs which will give him a total profit of Rs $(60\times75)$ ), i.e.,Rs 4500.

There are manyother possibilities,for instance, he maychoose to buy 10 tables and 50 chairs, as he can store only 60 pieces. Total profit in this case would be $\mathrm{Rs}(10\times250+50\times75)$ i.e.,Rs6250and so on.

We, thuvtw uld earn different profits by following diferent investment straties.

Now the problem is : How should he invest his money in order to get maximum profit? To answer this question, let us try to formulate the problem mathematically.

#### 12.2.1 Mathematical formulation of the problem

Ea

Obviously, x and y must be non-negative, i.e.,

$$\begin{array}{l}x\quad0\\y\quad0\end{array}\quad(Non-negative constraints)$$

The dealer is constrained by the maximum amount he can invest (Here it is $\mathrm{Rs}50,000$ and by the maximum number of items he can store (Here it is 60).

Stated mathematically,

or and

$$\begin{aligned}2500x+500y&\leq50000\quad(investment constraint)\\5x+y&\leq100\\x+y&\leq60\quad(storage constraint)\end{aligned}$$

The dealer wants to invest in such a way so as to maximise his profit, say, Z which stated as a function of x and y is given by

$Z=250x+75y$ , (called objective function)

Mathematically, the given problems now reduces to:

Maximise $Z=250x+75y$

subject to the constraints:

$$\begin{aligned}5x+y&\leq100\\x+y&\leq60\\x\geq0,y&\geq0\end{aligned}$$

So, we have to maimiete liarfunctionZ suject toerticondtions determined by a set oflinear inequalities with variables as non-negative.There are also some other problems where we have to minimise a linear function subject to certain conditions determined by a et oflinar inequalities with variables as non-negative.Such problems are called Linear Programming Problems.

Thus, a Linear Programming Problem is one that is concerned with finding the optimal value (maximum or minimum value) of a linear function (called objective function) of several variables (say x and y), subject to the conditions that the variables are non-negative and satisfy a set of linear inequalities (called linear constraints).The term linear implies that all the mathematical relations used in the problem are linear relations while the term programming refers to the method of determining a particular programme or plan of action.

Before we proceed further, we now formally define some terms (which have been used above) which we shall be using in the linear programming problems:

Objective function Linear function $Z=ax+by$ ', where a, b are constants, which has to be maximised or minimized is called a linear objective function.

In the above example,$Z=250x+75y$ is a linear objective function. Variables x and y are called decision variables.

Constraints The linear inequalities or equations or restrictions on the variables of a linear programming problem are called constraints. The conditions $x\geq0,y\geq0$ are called on-eative tictions.Inte above xample, et of inequalits 1) t (4)are constraints.

Optimisation problem A problem which seeks to maximise or minimise a linear function (say of two variables x and y) subject to certain constraints as determined by a set of linear inequalities is called an optimisation problem. Linear programming problems are special type of optimisation problems. The above problem of investing a

given umeripuhi adalsixmleoaimation problem as well as of a linear programming problem.

Wewill ow icusshwindlunt lar ammin roblem.Inthis chapter, we will be concerned only with the graphical method.

#### 12.2.2 Graphical method of solving linear programming problems

In Class XI, wehave learnthow to graph a ystemof linear inequalities involving two variables and and to find its solutions graphically.Let us refer to the problem of investment itableandchars dicusedi tion2.2.Wewill ow olvetis problem graphically. Let us graph the constraints stated as linear inequalities:

$$\begin{aligned}5x+y&\leq100\\x+y&\leq60\\x&\geq0\\y&\geq0\end{aligned}$$

Theraph ofm adofte mmotoll half planes determined by the inequalities (1) to (4) (Fig 12.1). Each point in this region represents a feasible choice open to the dealer for investing intables and chairs. The region, therefore, is called the feasible region for the problem. Every point of this region is called a feasible solution to the problem. Thus, we have,

Feasible region The common region determined by all the constraints including non-negative constraints x,$y\geq0$ f a linar i mild asible region (or solution region) for the problem. In Fig 12.1, the region OABC (shaded) is the feasible region for the problem. The region other than feasible region is called an

## infeasible region

Feasible solutions Points within and on the boundary of the feasible region represent feasible solutions of the constraints. In Fig 12.1, every point within and on the boundary of the feasible region OABC represents feasible solution to the problem.For example, the point (10, 50) is a feasible solution of the problem and so are the points (0, 60), (20, 0) etc.

Any point outside the feasible region is called an infeasible solution. For example,the point (25, 40) is an infeasible solution of the problem.

<div style="text-align: center;"><img src="imgs/img_in_chart_box_534_879_913_1287.jpg" alt="Image" width="37%" /></div>

<div style="text-align: center;">Fig 12.1</div>

Optimal (feasible) solution: Any point in the feassible region that gives the optimal value (maximum or minimum) of the objective function is called an optimal solution.

Now, we ethatevery point intheasible rgion OABC satisfs l theconstraints as given in (1) to (4), and since there areinfinitely many points, it is not evident how we should go about finding a point that gives a maximum value of the objective function $Z=250x+75$ y. To handle this situation, we use the following theorems which are fundamental in solving linear programming problems. The proofs of these theorems are beyond the scope of the book.

Theorem 1 Let R be the feasible region (convex polygon) for a linear programming problem and let $Z=ax+by$ be the objective function. When Z has an optimal value (maximum or minimum), where the variables x and y are subject to constraints described by lineariuli,ipimalaluutcuittex)fthe feasible region.

Theorem2Let R bethefeasibleregion for a linear programming problem, and let $Z=ax+by$ be the objective function.If R is bounded**,then the objective function Z has both a maximum and a minimum value on R and each of these occurs at a corner point (vertex) of R.

Remark If R is unbounded, then a maximum or a minimum value of the objective function may not exist. However, if it exists, it must occur at a corner point of R.(By Theorem 1).

In the abovexmr isoodil) egion are:,,ii,,,,)and (0,60)respectively.Let us nowcomputethevaluesofZatthese points.

We have

<div style="text-align: center;"><html><body><table border="1"><tr><td>Vertex of the Feasible Region</td><td>Corresponding value of Z (in Rs)</td></tr><tr><td>O (0,0) C (0,60) B(10,50) A (20,0)</td><td>0 4500 6250 5000</td></tr></table></body></html></div>

We observe that the maximum profit to the dealer results from the investment strategy (10,50),i.e.buying10tables and 50 chairs.

This method of solving linear programming problem is referred as Corner Point Method. The method comprises of the following steps:

1. Find the feasible region of the linear programming problem and determine its corner points (vertices) either by inspection or by solving the two equations of the lines intersecting at that point.

2. Evaluate the objective function $Z=ax+by$ at each corner point. Let M and m,respectively denote the largest and smallest values of these points.

3. (i) When the feasible region is bounded, M and m are the maximum and minimum values of Z.

(i) In case, the feasible region is unbounded, we have:

4. (a) M is the maximum value of Z, if the open half plane determined by $ax+by>M$ has no point in common with the feasible region. Otherwise, Z has no maximum value.

(b) Similarly, m is the minimum value of Z, if the open half plane determined by $ax+by<m$ has no point in common with the feasible region. Otherwise, Z has no minimum value.

We will now illustrate these steps of Corner Point Method by considering some examples:

Example 1 Solve the following linear programming problem graphically:

Maximise $Z=4x+y$

subject to the constraints:

$$\begin{aligned}x+y&\leq50\\3x+y&\leq90\\x\geq0,y&\geq0\end{aligned}$$

Solution The shaded region in Fig 12.2 is the feasible region determined by the system of constraints (2) to (4). We observe that the feasible region OABC is bounded. So,we now use Corner Point Method to determine the maximum value of Z.

The coordinates of the corner points O, A, B and C are (0, 0), (30, 0), (20, 30) and (0, 50) respectively. Now we evaluate $Z$ at each corner point.

$$3x+y=90$$

<div style="text-align: center;"><html><body><table border="1"><tr><td>Corner Point</td><td>Corresponding value ofZ</td></tr><tr><td>(0, 0) (30,0) (20,30) (0,50)</td><td>0 120 110 50</td></tr></table></body></html></div>

$$x+y=50$$

<div style="text-align: center;">Fig 12.2</div>

Hence, maximum value of Z is 120 at the point (30, 0).

raphll:

Minimise $Z=200x+500y$

subject to the constraints:

$$\begin{aligned}x+2y&\geq10\\3x+4y&\leq24\\x\geq0,y&\geq0\end{aligned}$$

Solo system),

$$x+2y=10$$

<div style="text-align: center;">Fig 12.3</div>

A, B and C are (0,5), (4,3) and (0,6) respectively. Now we evaluate $Z=200x+500y$ at these points.

Hence, minimum value of Z is 2300 attained at the point (4, 3)

添司添

Minimise and Maximise $Z=3x+9y$

subject to the constraints:$x+3y\leq60$

$$x+y\geq10$$

$$x\leq y $$

$$x\geq0,y\geq0$$

(2) to (5). The feasible region ABCD is shown in the Fig 12.4.Note that the region is bounded.The coordinates of the corner points A, B, C and D are (0, 10), (5, 5), (15,15)and (0, 20) respectively.

$$Z=3x+9y $$

$$x+3y=60$$

$$x+y=10$$

<div style="text-align: center;">Fig 12.4</div>

We now find the minimum and maximum value of Z. From the table, we find that the minimum value of Z is 60 at the point B (5, 5) of the feasible region.

The maximum value of Z on the feasible region occurs at the two corner points C (15, 15) and D (0, 20) and it is 180 in each case.

Remark Observe that in the above example, the problem has multiple optimal solutions at the corner points C and D, i.e. the both points produce same maximum value 180. In such cases, you can see that every point on the line segment CD joining the two corer points C and D also give the same maximum value. Same is also true in the case if the two points produce same minimum value.

Example 4 Determine graphically the minimum value of the objective function

$$Z=-50x+20y $$

subject to the constraints:

$$\begin{aligned}&\begin{aligned}\\ &2x-y\geq-5\\&3x+y\geq3\\&2x-3y\leq12\\&x\geq0,y\geq0\\ &\end{aligned}\\ \end{aligned}$$

Solution irtofl,t usraphteaiblegionofhesmofiequalities (2) to region is unbounded.(5). The feasible region (shaded) is shown in the Fig 12.5. Observe that the feasible ubli

We now evaluate Z at the corner points.

<div style="text-align: center;"><html><body><table border="1"><tr><td>Corner Point</td><td>$Z=-50x+20y$</td></tr><tr><td>(0,5) (0, 3) (1,0) (6, 0)</td><td>100 60 -50 -300</td></tr></table></body></html></div>

$$3x+y=3$$

<div style="text-align: center;">Fig 12.5</div>

From this table, we find that – 300 is the smallest value of Z at the corner point (6, 0). Can we say that minimum value of Z is – 300? Note that if the region would have been bounded, this smallest value of Z is the minimum value of Z (Theorem 2).But here we see that the feasible region is unbounded. Therefore, – 300 may or may not be the minimum value of Z. To decide this isue, we graph the inequality

$-50x+20y<-300$ (see Step 3(ii) of corner Point Method.)

i.e.,

$$-5x+2y<-30$$

and check whether the resulting open half plane has points in common with feasible region or not. If it has common points, then –300 will not be the minimum value of Z.Otherwise, –300 will be the minimum value of Z.

As shown in the Fig 12.5, it has common points. Therefore,$Z=-50x+20y$ ,has no minimum value subject to the given constraints.

In the above example, can you say whether $z=-50x+20y$ 'has the maximum value 100 at (0,5)? For this, check whether the graph $\begin{aligned}of-50x+20y>100\end{aligned}$ has points in common with the feasible region. (Why?)

Example 5 Minimise $Z=3x+2y$ 1

subject to the constraints:

$$\begin{aligned}x+y&\geq8\\3x+5y&\leq15\\x\geq0,y&\geq0\end{aligned}$$

Solutionet usgraphtheiequaliies (1)to) Fig2.).sthereanyaibleion Why is so?

<div style="text-align: center;"><img src="imgs/img_in_chart_box_472_588_915_946.jpg" alt="Image" width="43%" /></div>

<div style="text-align: center;">Fig 12.6</div>

From Fig 12.6, you can see that there is no point satisfying all the constraints simultaneously. Thus, the problem is having no feasible region and hence no feasible solution.

Remarks From the examples which we have discussed so far, we notice some general features of linear programming problems:

(i)The feasible region is always a convex region.

(ii)The maximum (or minimum)

solution of the objective function occurs at the vertex (corner) of the feasible region. If two corner points produce the same maximum (or minimum) value of the objective function, then every point on the line segment joining these points will also give the same maximum (or minimum) value.

### EXERCISE 12.1

Solve the following Linear Programming Problems graphically:

Maximise $Z=3x+4y$

subject to the constraints :$x+y\leq4,x\geq0,y\geq0$

2. Minimise $Z=-3x+4y$

subject to $x+2y\leq8,3x+2y\leq12,x\geq0,y\geq0.$

3. Maximise $Z=5x+3y$

subject to $3x+5y\leq15,5x+2y\leq10,x\geq0,y\geq0.$

Minimise $Z=3x+5y$

such that $x+3y\geq3,x+y\geq2,x,y\geq0.$ .

5. Maximise $Z=3x+2y$

subject to $$

6. Minimise $Z=x+2y$

subject tc $2x+y\ge3,x+2y\ge6,x,y\ge0.$ c

7. Minimise and Maximise $Z=5x+10y$

subject to $$

8. Minimise and Maximise $Z=x+2y$

subject to $$ ]

9. Maximise $Z=-x+2y$ , suc to he nstraints:不

$$x\geq3,x+y\geq5,x+2y\geq6,y\geq0.$$

10. Maximise $Z=x+y,$\mathrm{subject to}$x-y\leq-1,-x+y\leq0,x,y\geq0$ 司

### 12.3 Different Types of Linear Programming Problems

A few important linear programming problems are listed below:

1. Manufacturing problems In these problems, we determine the number of units of different products which should be produced and sold by a firm when each product requires a fixed manpower, machine hours, labour hour per unit of product, warehouse space per unit of the output etc., in order to make maximum profit.

2. Diet problems In these problems, we determine the amount of different kinds of constituents/nutrients which should be included in a diet so as to minimise the cost of the desired diet such that it contains a certain minimum amount of each constituent/nutrients.

3Transportation problems In these problems, we determine a transportation schedule in order to find the cheapest way of transporting a product from plants/factories situated at different locations to different markets.

Let us now solve some of these types of linear programming problems:

Example 6 (Diet problem): A dietician wishes to mix two typesof foods in such a way that vitamin contents of the mixture contain atleast 8 units of vitamin A and 10units of vitamin C.Food I'contains2 units/kg of vitaminAand 1 unit/kg of vitamin C.Food $ ``$\mathrm{II}$''$ contains 1 unit/kg of vitamin A and 2 units/kg of vitamin C. It costs R $ ``$\mathrm{II}$''$ .F m t this problem as a linear programming problem to minimise the cost of such a mixture.Solution Letthe mixturecontainkgofFoodI' andykgofFoodII.Clearly,$x\geq0$ $y\geq0$ . We make the following table from the given data:C

<div style="text-align: center;"><html><body><table border="1"><tr><td>Resources</td><td colspan="2">Food I I (x) (y)</td><td>Requirement</td></tr><tr><td>Vitamin A (units/kg) Vitamin C (units/kg)</td><td>2 1</td><td>1 2</td><td>8 10</td></tr><tr><td>Cost (Rs/kg)</td><td>50</td><td>70</td><td></td></tr></table></body></html></div>

Since the mixture must contain at least 8 units of vitamin A and 10 units of vitamin C, we have the constraints:

$$$\begin{aligned}\end{aligned}$&2x+y\geq8\\&x+2y$\geq10\end{aligned}$$

Total cost Z of purchasing x kg of food $ ``$\mathrm{I}$''$ and y kg of Food II' is

$$Z=50x+70y $$

Hence, the mathematical formulation of the problem is:

Minimise

$$Z=50x+70y $$

subject to the constraints:

$$2x+y\geq8$$

$$x+2y\geq10$$

$$x,y\geq0$$

Let us graph the inequalities (2) to (4). The feasible region determined by the system is shown in the Fig 12.7. Here again, observe that the feasible region is unbounded.

Let us evaluate Z at the corner points A(0,8), B(2,4) and $$\mathrm{C}(10,0)$

$$Z=50x+70y sn $$

$$2x+y=8$$

<div style="text-align: center;">Fig 12.7</div>

blis In the table, we find thatsmallest value ofZ is 380 atthe point(2,4). Can we say that the minimum value ofZis 380? Remember that the feasible region is unbounded.Therefore, we have to draw the graph of the inequality

$$50x+70y<380i.e.,5x+7y<38$$

tochck wible region. From the Fig 12.7, we se that it has no points in common.

Thus,the iimum aluofis30 aaid at te pit,4).c,te ptimal mixing strategyforthe ditician wouldbeto mix2kgofFoodI' and4kgofFood'II,and with this strategy,the minimumcostofthe mixture willbe Rs 380.

Example 7 (Allocation problem) A cooperative society of farmers has 50 hectare of land to grow two crops X and Y. The profit from crops X and Y per hectare are estimated as Rs 10,50 and Rs 9,000 respectively. To control weeds, a liquid herbicide has to be used forcropsX andYat ratesof20litres and 10litres perhectare.Further,no more than 800 litres of herbicide should be used in order to protect fish and wild life using a pond which collects drainage from this land. How much land should be allocated to each crop so as to maximise the total profit of the society?

Solution Let x hectare of land be allocated to crop X and y hectare to crop Y. Obviously,

$x\geq0,y\geq0$

Profit per hectare on crop $X=$\mathrm{Rs}10500$

Profit per hectare on crop $$\mathrm{Y}=\mathrm{Rs}9000$

Therefore, total profit $$\mathrm{Rs}\left(10500$x+9000y\right)$

The mathematical formulation of the problem is as follows:

Maximise

$$Z=10500x+9000y $$

subject to the constraints:

i.e.

$$$\begin{aligned}\end{aligned}$x+y&\leq50\quad(constraint related to land)\\20x+10y&\leq800\quad(constraint related to use of herbicide)\\2x+y&\leq80\\x\geq0,y&\geq0\quad(non negative constraint)$\end{aligned}$$

OABC is shown (shaded) in the Fig 12.8.Observe that the feasible region is bounded.

The coordinates of the corner points O, A, B and C are (0, 0), (40, 0), (30, 20) and (0, 50) respectively. Let us evaluate the objective function $Z=10500x+9000y$ at these vertices to find which one gives the maximum profit.

$$Z=10500x+9000y $$

$$2x+y=80$$

$$x+y=50$$

<div style="text-align: center;">Fig 12.8</div>

Hence, the society will get the maximum profit of Rs 4,95,00 by allocating 0hectares for crop X and 20 hectares for crop Y.

Example 8 (Manufacturing problem) A manufacturing company makes two models A and B of a product. Each piece of Model A requires 9 labour hours for fabricating and 1 labour hour for finishing. Each piece of Model B requires 12 labour hours for fabricating and 3 labour hours for finishing.For fabricating and finishing, the maximum labour hours available are 180 and 30 respectively. The company makes a profit of $$\mathrm{Rs}8000$ on each piece of model A and Rs 12000 on each piece of Model B. How many pieces of Model A and Model B should be manufactured per week to realise a maximum profit? What is the maximum profit per week?

Solution Suppose is the number of pieces of Model A and y is the number of pieces ofModel B.Then

Let

$$$\mathrm{Total}$\;$\mathrm{profit}$\;($\mathrm{in}$\;$\mathrm{Rs})=8000$\;x+12000\;y;\\Z=8000\;x+12000\;y.$$

We now have the following mathematical model for the given problem.

Maximise $Z=8000x+12000y$

subject to the constraints:

i.e.

$$$\begin{array}{ll}9$x+12y\leq180&(Fabricating constraint)\\3x+4y\leq60&(...(2))\\x+3y\leq30&(Finishing constraint)\\x\geq0,y\geq0&(non-negative constraint)\\$\end{array}$$

The feasible region (shaded) OABC determined by the linear inequalities (2) to (4)is shown in the Fig 12.9. Note that the feasible region is bounded.

$$3x+4y=60$$

<div style="text-align: center;">Fig 12.9</div>

Let us evaluate the objective function Z at each corner point as shown below:

<div style="text-align: center;"><html><body><table border="1"><tr><td>Corner Point</td><td>$Z=8000x+12000y$</td></tr><tr><td>0 (0, 0)</td><td>0</td></tr><tr><td>A(20,0)</td><td>160000</td></tr><tr><td>B(12,6)</td><td>168000</td></tr><tr><td>C (0, 10)</td><td>120000</td></tr></table></body></html></div>

We find that maximum value of Z is 1,68,000 at B (12, 6). Hence, the company should produce 12 pieces of Model A and 6 pieces of Model B to realise maximum profit and maximum profit then will be Rs 1,68,000.

### EXERCISE 12.2

1. Reshma wishes to mix two types of food P and Q in such a way that the vitamin contents of the mixture contain at least 8 units of vitamin A and 11 units of vitamin B. Food P costs Rs 60/kg and Food Q costs Rs 80/kg. Food P contains 3 units/kg of Vitamin A and 5 units / kg of Vitamin B while food Q contains 4units/kg ofVitamin A and 2 units/kg of vitamin B. Determine the minimum cost of the mixture.

2. Onekind ofcake requires200g offlour and 25g of fat, and another kind of cake requires 100g of flour and 50g of fat. Find the maximum number of cakes which can be made from 5kg of flour and 1 kg of fat assuming that there is no shortage of the other ingredients used in making the cakes.

3. A factory makes tennis rackets and cricket bats. A tennis racket takes 1.5 hours of machine time and 3 hours of craftman's time in its making while a cricket bat takes 3 hour of machine time and 1 hour of craftman's time. In a day, the factory has the availability of not more than 42 hours of machine time and 24 hours of craftsman's time.

(i) What number of rackets and bats must be made if the factory is to work at full capacity?

(ii) If the profit on a racket and on a bat is Rs 20 and Rs 10 respectively, find the maximum profit of the factory when it works at full capacity.

. A manufacturer produces nuts and bolts. It takes 1 hour of work on machine A and 3 hours on machine B to produce a package of nuts. It takes 3 hours on machine A and 1 hour on machine B to produce a package of bolts. He earns a profit of Rs17.50 per package on nuts and Rs 7.00 per package on bolts. How many packages of each should be produced each day so as to maximise his profit, if he operates his machines for at the most 12 hours a day?

5. A factory manufactures two types of screws, A and B. Each type of screw requires the use of two machines, an automatic and a hand operated. It takes 4 minutes on the automatic and 6 minutes on hand operated machines to manufacture a package of screws A, while it takes 6 minutes on automatic and 3 minutes on the hand operated machines to manufacture a package of screws B. Each machine is available for at the most 4 hours on any day. The manufacturer can sell a package of screws A at a profit of Rs 7 and screws B at a profit of Rs 10. Assuming that he can sell all the screws he manufactures, how many packages of each type should the factory owner produce in a day in order to maximise his profit? Determine the maximum profit.

6. A cottage industry manufactures pedestal lamps and wooden shades, each requiring the use of a grinding/cutting machine and a sprayer. It takes 2 hours on grinding/cutting machine and 3 hours on the sprayer to manufacture a pedestal lamp. It takes 1 hour on the grinding/cutting machine and 2 hours on the sprayer to manufacture a shade. On any day, the sprayer is available for at the most 20hours and the grinding/cutting machine for at the most 12 hours. The proffit from the sale of a lamp is Rs 5 and that from a shade is Rs 3. Assuming that the manufacturer can sell all the lamps and shades that he produces, how should he schedule his daily production in order to maximise his profit?

7. A company manufactures two types of novelty souvenirs made of plywood.Souvenirs of type A require 5 minutes each for cutting and 10 minutes each for assembling. Souvenirs of type B require 8 minutes each for cutting and 8 minutes each for assembling. There are 3 hours 20 minutes available for cutting and 4hours for assembling. The profit is Rs 5 each for type A and Rs 6 each for type B souvenirs. How many souvenirs of each type should the company manufacture in order to maximise the profit?

8. A merchant plans to sell two types of personal computers – a desktop model and a portable model that will cost Rs 25000 and Rs 40000 respectively. He estimates that the total monthly demand of computers will not exceed 250 units. Determine the number of units of each type of computers which the merchant should stock to get maximum profit if he does not want to invest more than Rs 70 lakhs and if his profit on the desktop model is Rs 4500 and on portable model is Rs 5000.

9. A diet is to contain at least 80 units of vitamin A and 100 units of minerals. Two foods 

$$\mathrm{F}_{1}^{\prime}$ and $$

\mathrm{F}_{2}$ are available. Food $$\mathrm{F}_{1}$ costs Rs 4 per unit food and 

$$\mathrm{F}_{2}$ costs Rs 6 per unit. One unit of food $$

\mathrm{F}_{1}$ contains 3 units of vitamin A and 4 units of minerals. One unit of food $$\mathrm{F}_{2}$ contains 6 units of vitamin A and 3 units of minerals.Formulate this as a linear programming problem. Find the minimum cost for diet that consists of mixture of these two foods and also meets the minimal nutritional requirements.

There are two types of fertilisers F, and 

$$\mathrm{F}_{2}.\mathrm{F}_{1}$ consists of 10\% nitrogen and 6\%phosphoric acid and $ F_2$ consists of 5\% nitrogen and 10\% phosphoric acid. After testing the soil conditions, a farmer finds that she needs atleast 14 kg of nitrogen and 14 kg of phosphoric acid for her crop. If $$

\mathrm{F}_{\mathrm{1}}$ costs Rs 6/kg and $ F_2$ costs Rs 5/kg, determine how much of each type of fertiliser should be used so that nutrient requirements are met at a minimum cost. What is the minimum cost?

11. The corner points of the feasible region determined by the following system of linear inequalities:

$2x+y\leq10,x+3y\leq15$ ,x,$y\geq0$ are (0, 0), (5, 0), (3, 4) and(0, 5). Let $Z=px+qy$ , where p,$q\geq0$ . Condition on p and q so that the maximum of Z occurs at both (3, 4) and (0, 5) is

(A)$p=q$ (B)$p=2q$ (C)$p=3q$ (D).$q=3p$

## Miscellaneous Examples

Example 9 (Diet problem) A dietician has to develop a special diet using two foods Pand Q.achacktoing)ofoodPcotauitofliums ofiron, nitofcholerol ndunitofviamiA.ach packtofte am aity offoo ofvitiof at most 300 units of cholesterol. How many packets of each food should be usd to minimise the amount of vitaminAinthe diet? What is the minimum amount of vitamiA?SolutionnteumofckofoPnptivlybouy [Tab]$x\geq0,y\geq0$ Mathelllow ab

Minimise $Z=6x+3y($\mathrm{v}\mathrm{t}\mathrm{a}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{A}$ EM

subject to the constraints

$$12x+3y\geq240\left(constraint on calculation\right),i.e.\quad4x+y\geq80 ab $$

$$4x+20y\geq460(constraint on iron),i.e.\quad x+5y\geq115 ab $$

$$6x+4y$\leq300\left(\mathrm{constrain\;on\;ch o l e s t e r o l}\right),\mathrm{i.e.}$\;3x+2y\leq150 ab $$

$$x\geq0,y\geq0$$

Let us graph the inequalities (1) to (4).

The feasible io (aded) drmied b econtts1)(4) is hown in Fig 12.10 and note that it is bounded.

$$$\overline{M}$$

$$4x+y=80$$

$$3x+2y=150$$

$$x+5y=115$$

<div style="text-align: center;">Fig 12.10</div>

The coordinates of the corner points L, M and N are (2, 72), (15, 20) and (40, 15)respectively. Let us evaluate Z at these points:

<div style="text-align: center;"><html><body><table border="1"><tr><td>Corner Point</td><td>$Z=6x+3y$</td></tr><tr><td>(2,72)</td><td>228</td></tr><tr><td>(15,20)</td><td>150←</td></tr><tr><td>(40,15)</td><td>285</td></tr></table></body></html></div>

From the table, we find that Z is minimum at the point (15,20). Hence, the amount ofvitamiimllium,5s offoodP and20 packets offood Qare udinthe spcial dit.The minimum amount of vitamin A will be 150 units.

Example 10 (Manufacturing problem) A manufacturer has three machines I, II andIII installed inhisfactory.MachinesI andII arecapableofbeingoperatd or at most 12 hours whereas machine III must be operated for atleast 5 hours a day. She produces only two items M and N each requiring the use of all the three machines.

The number of hours required for producing 1 unit of each of M and N on the three machines are given in the following table:

<div style="text-align: center;"><html><body><table border="1"><tr><td rowspan="2">Items</td><td colspan="3">Number of hours required on machines</td></tr><tr><td>I</td><td>II</td><td>III</td></tr><tr><td>M N</td><td>1 2</td><td>2 1</td><td>1 1.25</td></tr></table></body></html></div>

She makes a profit of Rs 600 and Rs 400 on items M and N respectively. How many ofeach item should she produce so as to maximiseher profit assuming that she can sell all the items that she produced? What will be the maximum profit?

Solution Lt andbethe numberof itemsMandNrespectively.

Total profit on the otalprontontne $$\mathrm{production}=\mathrm{Rs}\left(600$x+400y\right)$ c c

Total proint on ie

Maximise $Z=600x+400y$

subject to the constraints:

$$$\begin{array}{l}{x+2y\leq12\;(\mathrm{c o n s t r a i n t\;o n\;M a c h i n e\;I})}\end{array}$\\ {12x+y\leq12\;($\mathrm{c o n s t r a i n t\;o n\;M a c h i n e\;I I}$}$\end{array}$$

$$x+$\frac{5}{4}$y\geq5(constraint on Machine III)$$

$$x\geq0,y\geq0$$

Let us draw the graph of constraints (1) to (4). ABCDE is the feasible region (shaded) asshowninFig12.11determinedbytheconstraints(1)to(4).bee hat the feasible region is bounded, coordinates of the corner points A, B, C, D and E are (5, 0) (6, 0), (4, 4), (0, 6) and (0, 4) respectively.EM

<div style="text-align: center;"><img src="imgs/img_in_image_box_236_293_772_689.jpg" alt="Image" width="53%" /></div>

<div style="text-align: center;">Fig 12.11</div>

Let us evaluate $Z=600x+400$ y at these corner points.

<div style="text-align: center;"><html><body><table border="1"><tr><td>Corner point</td><td>$Z=600x+400y$</td></tr><tr><td>(5,0)</td><td>3000</td></tr><tr><td>(6, 0)</td><td>3600</td></tr><tr><td>(4, 4)</td><td>4000</td></tr><tr><td>(0,6)</td><td>2400</td></tr><tr><td>(0, 4)</td><td>1600</td></tr></table></body></html></div>

We see that the point (4, 4) is giving the maximum value of Z. Hence, the manufacturer has to produce 4 units of each item to get the maximum profit of Rs 4000.Example 11 (Transportation problem) There are two factories located one at place P and the other at place Q. From these locations, a certain commodity is to be delivered to each of the three depots situated at A, B and C. The weekly requirements of the depots are respectively 5,5 and 4 units of the commodity while the production capacity of the factories at P and Q are respectively 8 and 6 units. The cost of transportation per unit is given below:

<div style="text-align: center;"><html><body><table border="1"><tr><td rowspan="2">From/To</td><td colspan="3">Cost (in Rs)</td></tr><tr><td>A</td><td>B</td><td>C</td></tr><tr><td>P</td><td>160</td><td>100</td><td>150</td></tr><tr><td>Q</td><td>100</td><td>120</td><td>100</td></tr></table></body></html></div>

How many units should be transported from each factory to each depot in order that the transportation cost is minimum. What will be the minimum transportation cost?

Solution The problem can be explained diagrammatically as follows (Fig 12.12):

Let x units and units of the commodity be transported from the factory at P to the depots at A and B respectively. Then $(8-x-y)$ units will be transported to depot at C (Why?)Factory

<div style="text-align: center;"><img src="imgs/img_in_image_box_217_545_810_1029.jpg" alt="Image" width="58%" /></div>

<div style="text-align: center;">Fig 12.12</div>

#### Hence, we have i.e.

$$$\begin{aligned}$&x\geq0,y\geq0\quad and\quad8-x-y\geq0\\&x\geq0,y\geq0\quad and\quad x+y\leq8\\ $\end{aligned}$$

Now, the weekly requirement of the depot at A is 5 units of the commodity. Since x units are transported from the factory at P, the remaining $(5-x)$ units need to be transported from the factory at Q. Obviously,$5-x\geq0,i.e.x\leq5$

Similarly,$(5-y)$ and $6-(5-x+5-y)=x+y-4$ units are to be transported from

the factory at Q to the depots at B and C respectively.

Thus,

i.e.

$$$\begin{array}{r}{5-y\geq0\quad,\quad x+y-4\geq0}\end{array}$\\ {y\leq5\quad,\quad x+y\geq\quad4}$\end{array}$$

Total transportation cost Z is given by

$$$\begin{aligned}$Z&=160x+100y+100(5-x)+120(5-y)+100(x+y-4)+150(8-x-y)\\&=10(x-7y+190)$\end{aligned}$$

Therefore, the problem reduces to Minimise $Z=10(x-7y+190)$ subject to the constraints:

and

$$$\begin{array}{r l r l}{x\geq0,y\geq0}\end{array}$&{{}}&{}&{{}\dots(1)}\\ {x$^{\;+}$y\leq8}&{{}}&{}&{{}\dots(2)}\\ {x\leq5}&{{}}&{}&{{}\dots(3)}\\ {y\leq5}&{{}}&{}&{{}\dots(4)}\\ {x$^{\;+}$y\geq4}&{{}}&{}&{{}\dots(5)}$\end{array}$$

The shaded region ABCDEF represented by the constraints (1) to (5) is the feasible region (Fig 12.13).

$$x+y=4$$

$$$\mathbf{A}(0,4)$$

<div style="text-align: center;">Fig 12.13</div>

$$y=5$$

$$x+y=8$$

Observe that the feasible region is bounded. The coordinates of the corner points of the feasible region are (0, 4), (0,5), (3, 5), (5, 3), (5, 0) and (4, 0).Let us evaluate Z at these points.

<div style="text-align: center;"><html><body><table border="1"><tr><td>Corner Point</td><td>$Z=10\left(x-7y+190\right)$</td><td rowspan="2">Minimum</td></tr><tr><td>(0, 4)</td><td>1620</td></tr><tr><td>(0,5)</td><td>1550</td><td rowspan="3"></td></tr><tr><td>(3,5)</td><td>1580</td></tr><tr><td>(5,3)</td><td>1740</td></tr><tr><td>(5,0)</td><td>1950</td><td rowspan="2"></td></tr><tr><td>(4, 0)</td><td>1940</td></tr></table></body></html></div>

From the table, we see that the minimum value of Z is 1550 at the point (0, 5).

Hence, the optimal transportation strategy will be to deliver 0, 5 and 3 units from the factory atPand5,0and1unitsrom the factory attothe depots at A, B and C respecivl.on i getist ld e mum,i.e., Rs 1550.

## Miscellaneous Exercise on Chapter 12

Refer to Example 9. How many packets of each food should be used to maximise the amount of vitamin A in the diet? What is the maximum amount of vitamin A in the diet?

2. A farmer mixes two brands P and Q of catle feed. Brand P, costing Rs 250 per bag, contains 3 units of nutritional element A, 2.5 units of element B and 2 units of element C. Brand Q costing Rs 200 per bag contains 1.5 units of nutritional element A, 11.25 units of element B, and 3 units of element C. The minimum requiremout,neu,utnd4utsctivl.Determine the number of bags of each brand which should be mixed in order to produce a mixture having a minimum cost per bag? What is the minimum cost of the mixture per bag?

3. A dietician wishes to mix together two kinds of food X and Y in such a way that the mixture contains at least 10 units of vitamin A, 12 units of vitamin B and 8 units of vitamin C. The vitamin contents of one kg food is given below:

<div style="text-align: center;"><html><body><table border="1"><tr><td>Food</td><td></td><td></td><td>Vitamin C</td></tr><tr><td>X</td><td>1</td><td>2</td><td>3</td></tr><tr><td>Y</td><td>2</td><td>2</td><td>1</td></tr></table></body></html></div>

One kg of food X costs Rs 16 and one kg of foodY costs Rs 20. Find the least cost of the mixture which will produce the required diet?

.A manufacturer makes two types of toys A and B. Three machines are needed for this purpose and the time (in minutes) required for each toy on the machines is given below:

<div style="text-align: center;"><html><body><table border="1"><tr><td rowspan="2">Types of Toys</td><td colspan="3">Machines</td></tr><tr><td>I</td><td>II</td><td>III</td></tr><tr><td>A</td><td>12</td><td>18</td><td>6</td></tr><tr><td>B</td><td>6</td><td>0</td><td>9</td></tr></table></body></html></div>

Each machine is available for a maximum of 6 hours per day. If the profit on each toy of type A is Rs 7.50 and that on each toy of type B is Rs 5, show that 15toys of type A and 30 of type B should be manufactured in a day to get maximum profit.

5. An aeroplane can carry a maximum of 200 passengers. A profit of Rs 1000 is made on each executive class ticket and a profit of Rs 600 is made on each economy class ticket. The airline reserves at least 20 seats for executive class.However, at least 4 times as many passengers prefer to travel by economy class than by the executive class. Determine how many tickets of each type must be sold in order to maximise the profit for the airline. What is the maximum profit? 6. Two godowns A and B have grain capacity of 100 quintals and 50 quintals respectively. They supply to 3 ration shops, D, E and F whose requirements are 60, 50 and 40 quintals respectively. The cost of transportation per quintal from the godowns to the shops are given in the following table:

<div style="text-align: center;"><html><body><table border="1"><tr><td colspan="3">Transportation cost per quintal (in Rs)</td></tr><tr><td>From/To</td><td>A</td><td>B</td></tr><tr><td>D E F</td><td>6 3 2.50</td><td>4 2 3</td></tr></table></body></html></div>

How should the supplies be transported in order that the transportation cost is minimum? What is the minimum cost?

7. An oil company has two depots A and B with capacities of 7000 L and 4000 L respectively. The company is to supply oil to three petrol pumps, D, E and F whose requirements are 4500L, 3000L and 3500L respectively. The distances (in km) between the depots and the petrol pumps is given in the following table:

<div style="text-align: center;"><html><body><table border="1"><tr><td colspan="3">Distance in (km.)</td></tr><tr><td>From / To</td><td>A</td><td>B</td></tr><tr><td>D E F</td><td>7 6 3</td><td>3 4 2</td></tr></table></body></html></div>

Assuming that the transportation cost of 10 litres of oil is Re 1 per km, how should the delivery be scheduled in order that the transportation cost is minimum?What is the minimum cost?

8. Afruit grower can use two types offertilizer in his garden, brand P and brand Q.The amounts (in kg) of nitrogen, phosphoric acid, potash, and chlorine in a bag of each brand are given in the table. Tests indicate that the garden needs at least 240 kg of phosphoric acid, at least 270 kg of potash and at most 310 kg of chlorine.

If the grower wants to minimise the amount of nitrogen added to the garden,how many bags of each brand should be used? What is the minimum amount of nitrogen added in the garden?

<div style="text-align: center;"><html><body><table border="1"><tr><td colspan="3">kg per bag</td></tr><tr><td></td><td>Brand P</td><td>Brand Q</td></tr><tr><td>Nitrogen Phosphoric acid Potash Chlorine</td><td>3 1 3 1.5</td><td>3.5 2 1.5 2</td></tr></table></body></html></div>

9. Refer to Question 8. If the grower wants to maximise the amount of nitrogen added to the garden, how many bags of each brand should be added? What is the maximum amount of nitrogen added?

10. .Atoy company manufactures two types of dols, A and B.Market tests and available resources have indicated that the combined production level should not exced 1200dolls per week and the demand for dolls of type B is at most half of that for dolls of type A. Further, the production level of dolls of type A can exceed three times the production of dolls of other type by at most 600 units. If the company makes profit of Rs 12 and Rs 16 perdll sectivly on dlls Aand B, how many of ach shoul b produced weekly in order to maximise the profit?

## Summary

■A linear programming problm i onett i concred wihdingte optimal value (maximum or minimum) oa linear function of several variables (called objective function) subject to the conditions that the variables are non-negativeandatisfet o liarnqulities(clled larontraints).Variables are sometimes called decision variables and are non-negative.

A few important linear programming problems are:

(i)Diet problems

(i)Manufacturing problems

(ii Transportation problems

The common region detrmined by all theconstraints including te non-ngative constraints $x\geq0,y\geq0$ of a linear programming problem is called the feasible region 1 (or solution region) for the problem.

Points within and on the boundary of the feasible region represent feasible solutions of the constraints.

Any point outside the feasible region is an infeasible solution.

■Any point inthefasibleregionthat givestheoptimalvalue(maximumor minimum) of the objective function is called an optimal solution.

■The following Theorems are fundamental in solving linear programming problems:

Theorem 1 Let R be the feasible region (convex polygon) for a linear programming problem and let $Z=ax+by$ be the objective function. When Z has an optimal value (maximum or minimum), where the variables x and y are subject to constraints described by linear inequalities, this optimal value must occur at a corner point (vertex) of the feasible region.

Theorem 2 Let R be the feasible region for a linear programming problem,and let $Z=a x+b y$ be the objective function. If R is bounded,then the objective function Z has both a maximum andaminimumvalueon Rand each of these occurs at a corner point (vertex) of R.

国If the feasible region is unbounded, then a maximum or a minimum may not exist. However, if it exists, it must occur at a corner point of R.

■Corner point method for solving a linear programming problem. The method comprises of the following steps:

(i)Find the feasible region of the linear programming problem and determine its corner points (vertices).

(ii)Evaluate the objective function $Z=ax+by$ at each corner point. Let M and m respectively be the largest and smallest values at these points.(ii)If the feasible region is bounded, M and m respectively are the maximum and minimum values of the objective function.

If the feasible region is unbounded, then

(i)M is the maximum value of the objective function, if the open half plane determined by $ax+by>M$ has no point in common with the feasible region. Otherwise, the objective function has no maximum value.

(ii)m is the minimum value ofthe objective function, if the open half plane determined by $ax+by<m$ has no point in common with the feasible region. Otherwise, the objective function has no minimum value.

If two corner pointsof thefeasible region are bothoptimal solutions of the same type, i.e., both produce the same maximum or minimum, then any point onthelinegmetjoiieseopoitiloaoptimalolutioofhe same type.

## Historical Note

In the World War II, when the war operations had to be planned to economise expenditure, maximise damage to the enemy,linear programming problems came to the forefront.

The first problem in linear programming was formulated in 1941 by the Russian mathematician, L. Kantorovich and the American economist, F.L. Hitchcock,bothof whomworked at it independently of each other.This was the well known transportation problem.In11945, an English economist,G.Stigler,described yet another linear programming problem —that of determining an optimal diet.

In1947,the Americaneconomist, G.B.Dantzig sugested an eficient method known as the simplex method which is an iterative procedure to solve any linear programming problem in a finite number of steps.

L. Katorovich and American mathematical economist,T. C.Koopmans were awarded the nobel prize in the year 1975in economics for their pioneering work in linear programming. With the advent of computers and the necessary softwares, it has become possible to apply linearprogramming model to NCER increasingly complex problems in many areas.

