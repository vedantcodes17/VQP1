

# PROBABILITY 

.

quantitatively treated. - C.S. PEIRCE …



### 13.1 Introduction 

In earlier Classes, we have studied the probability as a measure of uncertainty of events in a random experiment.We discussed the axiomatic approach formulated by Russian Mathematician, A.N. Kolmogorov (1903-1987)and treated probability as a function of outcomes of the experiment. We have also established equivalence between the axiomatic theory and the classical theory of probability in case of equally likely outcomes. On the basis of this relationship, we obtained probabilities of events associated with discrete sample spaces. We have also studied the addition ruleof probabiity.Inthis chaptr, e shal dicuss the important concept of conditional probability of an event given that another event has occurred, which will be helpful in understanding the Bayes' theorem, multiplication rule of probability and independence of events.We shall also learn 

<div style="text-align: center;"><img src="imgs/img_in_image_box_673_567_919_890.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;">Pierre de Fermat (1601-1665)</div>


section of the chapter, we shall study animportant discrete probability distribution calle having equally likely outcomes, unless stated otherwise.



### 13.2 Conditional Probability 

events. If we have two events from the same sample space, does the information about the occurrence of one of the events affect the probability of the other event? Let us try to answer this question by taking up a random experiment in which the outomes are equally likely to occur.C_0ConsiderhxiofssiheaconThamlspaceofthe experiment is 

$\mathrm{S}=\{\mathrm{HHH}$ , HHT, HTH, THH, HTT, THT, TTH, TTT}

S $\left[\frac{1}{8}\right.]$ to each sample point. Let Ebetheanwl Then 



and 

Therefore 

and 

Also 

with 

$$\mathrm{P}(\mathrm{E}\cap\mathrm{F})=\mathrm{P}(\{\mathrm{THH}\})=\frac{1}{8} \begin{aligned}E&=\{HHH,HHT,HTH,THH\}\\ F&=\{THH,THT,TTH,TTT\}\\ P(E)&=P\left(\{HHH\}\right)+P\left(\{HHT\}\right)+P\left(\{HTH\}\right)+P\left(\{THH\}\right)\\&=\frac{1}{8}+\frac{1}{8}+\frac{1}{8}+\frac{1}{8}=\frac{1}{2}(Why?)\\ P(F)&=P\left(\{THH\}\right)+P\left(\{THT\}\right)+P\left(\{TTH\}\right)+P\left(\{TTT\}\right)\\&=\frac{1}{8}+\frac{1}{8}+\frac{1}{8}+\frac{1}{8}=\frac{1}{2}\\ E\cap F&=\{THH\}\\ P\cap F&=P(\{THH\})=\frac{1}{8}\end{aligned}$$

Now, suppose we are given that the first coin shows tail, ie.F occurs, then what is the probability of occurrence of E? With the information of occurrence of F, we are sure that the cases in which first coin does not result into a tail should not be considered while finding the probability of E. This information reduces our sample space from the set S to its subset F for the event E. In other words, the additional information really amounts to telling us that the situation may be considered as being that of a new random experiment for which the sample space consists of all those outcomes only which are favourable to the occurrence of the event F.



Now, the sample point of F which is favourable to event E is THH.

Thus, Probability of E considering F as the sample $\mathrm{space}=\frac{1}{4}$ 

or 

$$\mathrm{Probability of E given that the event F has occurred}=\frac{1}{4}$$

This probability of the event E is called the conditional probability of E given that F has already occurred, and is denoted by P (E|F).



Thus 

$$\mathrm{P}(\mathrm{E}|\mathrm{F})=\frac{1}{4}$$

Note that the elements of F which favour the event E are the common elements of E and F, i.e. the sample points of E∩ F.



Thus, we can also write the conditional probability ofE given that F has occurred as 

$$\begin{aligned}\mathrm{P}(\mathrm{E}|\mathrm{F})&=\frac{\text{Number of elementary events favorable to E}\cap\mathrm{F}}{\text{Number of elementary events which are favorable to F}}\\&=\frac{\mathrm{~}n(\mathrm{E}\cap\mathrm{F})}{n(\mathrm{F})}\end{aligned}$$

of the sample space, we see that P(E|F) can also be writen as Dividing the numerator and the denominator by total number of elementary events 

$$\mathrm{P}(\mathrm{E}|\mathrm{F})=\frac{\frac{n(\mathrm{E}\cap\mathrm{F})}{n(\mathrm{S})}}{\frac{n(\mathrm{F})}{n(\mathrm{S})}}=\frac{\mathrm{P}(\mathrm{E}\cap\mathrm{F})}{\mathrm{P}(\mathrm{F})}$$

Note that (1) is valid only when $$ 

lows:

Definition 1 If E and F are two events associated with the same sample space of a random experiment, the conditional probability of the event E given that F has occurred,i.e. P (E|F) is given by 



$$\mathrm{P}(\mathrm{E}|\mathrm{F})=\frac{\mathrm{P}(\mathrm{E}\cap\mathrm{F})}{\mathrm{P}(\mathrm{F})}\text{provided}\mathrm{P}(\mathrm{F})\neq0$$

#### 13.2.1 Propertiesof conditional probability 

Let E and F be events of a sample space S of an experiment, then we have Property 1$\mathrm{P}(\mathrm{S}|\mathrm{F})=\mathrm{P}(\mathrm{F}|\mathrm{F})=1$ 



We know that tto 

$$\mathrm{P}(\mathrm{S}|\mathrm{F})=\frac{\mathrm{P}(\mathrm{S}\cap\mathrm{F})}{\mathrm{P}(\mathrm{F})}=\frac{\mathrm{P}(\mathrm{F})}{\mathrm{P}(\mathrm{F})}=1$$

Also 

$$\mathrm{P}(\mathrm{F}|\mathrm{F})=\frac{\mathrm{P}(\mathrm{F}\cap\mathrm{F})}{\mathrm{P}(\mathrm{F})}=\frac{\mathrm{P}(\mathrm{F})}{\mathrm{P}(\mathrm{F})}=1$$

Thus 

$$\mathrm{P}(\mathrm{S}|\mathrm{F})=\mathrm{P}(\mathrm{F}|\mathrm{F})=1$$

Property 2 If A and B are any two events of a sample space S and F is an event of S such that $\mathrm{P}(\mathrm{F})\neq0$ ,then 



$$\mathrm{P}((\mathrm{A}\cup\mathrm{B})|\mathrm{F})=\mathrm{P}(\mathrm{A}|\mathrm{F})+\mathrm{P}(\mathrm{B}|\mathrm{F})-\mathrm{P}((\mathrm{A}\cap\mathrm{B})|\mathrm{F})$$

In particular, if A and B are disjoint events, then 

$$\mathrm{P}((\mathrm{A}\cup\mathrm{B})|\mathrm{F})=\mathrm{P}(\mathrm{A}|\mathrm{F})+\mathrm{P}(\mathrm{B}|\mathrm{F}):$$

We have 

$$\begin{aligned}\mathrm{P}((\mathrm{A}\cup\mathrm{B})|\mathrm{F})&=\frac{\mathrm{P}[(\mathrm{A}\cup\mathrm{B})\cap\mathrm{F}]}{\mathrm{P}(\mathrm{F})}\\&=\frac{\mathrm{P}[(\mathrm{A}\cap\mathrm{F})\cup(\mathrm{B}\cap\mathrm{F})]}{\mathrm{P}(\mathrm{F})}\\(\mathrm{by}&\text{distributive law of union of sets over intersection})\\&=\frac{\mathrm{P}(\mathrm{A}\cap\mathrm{F})+\mathrm{P}(\mathrm{B}\cap\mathrm{F})-\mathrm{P}(\mathrm{A}\cap\mathrm{B}\cap\mathrm{F})}{\mathrm{P}(\mathrm{F})}\\&=\frac{\mathrm{P}(\mathrm{A}\cap\mathrm{F})+\mathrm{P}(\mathrm{B}\cap\mathrm{F})-\mathrm{P}[(\mathrm{A}\cap\mathrm{B})\cap\mathrm{F}]}{\mathrm{P}(\mathrm{F})}\\&=\mathrm{P}(\mathrm{A}|\mathrm{F})+\mathrm{P}(\mathrm{B}|\mathrm{F})-\mathrm{P}((\mathrm{A}\cap\mathrm{B})|\mathrm{F})\end{aligned}ep $$

When A and B are disjoint events, then 

$$\begin{aligned}\mathrm{P}((\mathrm{A}\cap\mathrm{B})|\mathrm{F})&=0\\\mathrm{P}((\mathrm{A}\cup\mathrm{B})|\mathrm{F})&=\mathrm{P}(\mathrm{A}|\mathrm{F})+\mathrm{P}(\mathrm{B}|\mathrm{F})\end{aligned} ep $$

Property 3$\mathrm{P}(\mathrm{E}'|\mathrm{F})=1-\mathrm{P}(\mathrm{E}|\mathrm{F})$ 

From Property 1, we know that $\mathrm{P}(\mathrm{S}|\mathrm{F})=1$ 

Thus,

$$\begin{array}{ccc}\mathrm{P}(\mathrm{E}\cup\mathrm{E}^{\prime}|\mathrm{F})&=1&\text{since}\mathrm{S}=\mathrm{E}\cup\mathrm{E}^{\prime}\\\mathrm{P}(\mathrm{E}|\mathrm{F})+\mathrm{P}(\mathrm{E}^{\prime}|\mathrm{F})&=1&\text{since E and}\mathrm{E}^{\prime}\text{are disjoint events}\\\mathrm{P}(\mathrm{E}^{\prime}|\mathrm{F})&=1-\mathrm{P}(\mathrm{E}|\mathrm{F})\end{array}$$

Let us now take up some examples.

$$\mathrm{Example}\mathbb{I}\mathrm{If}\mathrm{P}(\mathrm{A})=\frac{7}{13},\mathrm{P}(\mathrm{B})=\frac{9}{13}\text{and}\mathrm{P}(\mathrm{A}\cap\mathrm{B})=\frac{4}{13},\mathrm{evaluate}\mathrm{P}(\mathrm{A}|\mathrm{B}).$$

SolutionWe have $\mathrm{P}(\mathrm{A}|\mathrm{B})=\frac{\mathrm{P}(\mathrm{A}\cap\mathrm{B})}{\mathrm{P}(\mathrm{B})}=\frac{\frac{4}{13}}{\frac{9}{13}}=\frac{4}{9}$ 

Exampleamilastlre.What ieprobalttatbhtechildren are boys given that at least one of them is a boy ?



Solution Let b stand for boy and g for girl. The sample space of the experiment is 

$$\mathrm{S}=\left\{(b,b),(g,b),(b,g),(g,g)\right\}$$

Let E and F denote the following events :

E : 'both the children are boys'

F : 'at least one of the child is a boy'

Then 

Now 

Thus 

$$\mathrm{E}=\{(b,b)\}\text{and}\mathrm{F}=\{(b,b),(g,b),(b,g)\}bli $$

Therefore 

$$\mathrm{P}(\mathrm{E}|\mathrm{F})=\frac{\mathrm{P}(\mathrm{E}\cap\mathrm{F})}{\mathrm{P}(\mathrm{F})}=\frac{\frac{1}{4}}{\frac{3}{4}}=\frac{1}{3}$$

Example 3 Ten cards  numbered 1 to 10 are placed in a box, mixed up thoroughly and bli then one card is drawn randomly. If it is known that the number on the drawn card is more than 3, what is the probability that it is an even number?

Solution Let A be the event the number on the card drawn is even'and B be the event 'the number on the card drawn is greater than 3'.We have to find P(A|B).

Now, the sample space of the experiment is $\mathrm{S}=\{1,2,3,4,5,6,7,8,9,10\}$ 

Then 

$$\mathrm{A}=\{2,4,6,8,10\},\mathrm{B}=\{4,5,6,7,8,9,10\}$$

and 

$$\mathrm{A}\cap\mathrm{B}=\{4,6,8,10\}$$

Also 

$$\mathrm{P}(\mathrm{A})=\frac{5}{10},\mathrm{P}(\mathrm{B})=\frac{7}{10}\text{and}\mathrm{P}(\mathrm{A}\cap\mathrm{B})=\frac{4}{10}$$

Then 

$$\mathrm{P}(\mathrm{A}|\mathrm{B})=\frac{\mathrm{P}(\mathrm{A}\cap\mathrm{B})}{\mathrm{P}(\mathrm{B})}=\frac{\frac{4}{10}}{\frac{7}{10}}=\frac{4}{7}$$

Example 4 In a school, there are 1000 students, out of which 430 are girls. It is known that out of 430, 10% of the girls study in class XII. What is the probability that a student chosen randomly studies in Class XII given that the chosen student is a girl?

Solution Let E denote the event that a student chosen randomly studies in Class XII and Fbetheeventtht therandomlychosen studentis a grl.Wehave toindP(|F). Now 

$$\mathrm{P}(\mathrm{F})=\frac{430}{1000}=0.43\text{and}\mathrm{P}(\mathrm{E}\quad\mathrm{F})=\frac{43}{1000}\quad0.043\quad(\mathrm{Why}?)$$

Then 

$$\mathrm{P}(\mathrm{E}|\mathrm{F})=\frac{\mathrm{P}(\mathrm{E}\cap\mathrm{F})}{\mathrm{P}(\mathrm{F})}=\frac{0.043}{0.43}=0.1$$

Example $5\ A$ die is thrown three times. Events A and B are defined as below:

A : 4 on the third throw 

B : 6 on the first and 5 on the second throw 

Find the probability of A given that B has already occurred.

Solution The sample space has 216 outcomes.

Now 

$$\mathrm{A}=\left\{\begin{aligned}&(1,1,4)(1,2,4)\ldots(1,6,4)(2,1,4)(2,2,4)\ldots(2,6,4)\\&(3,1,4)(3,2,4)\ldots(3,6,4)(4,1,4)(4,2,4)\ldots(4,6,4)\\&(5,1,4)(5,2,4)\ldots(5,6,4)(6,1,4)(6,2,4)\ldots(6,6,4)\end{aligned}\right\}$$

$$\mathrm{B}=\left\{\left(6,5,1\right),\left(6,5,2\right),\left(6,5,3\right),\left(6,5,4\right),\left(6,5,5\right),\left(6,5,6\right)\right\}$$

and $\mathrm{A}\cap\mathrm{B}=\{(6,5,4)\}.$ 

Now 

$$\mathrm{P}(\mathrm{B})=\frac{6}{216}\text{and}\mathrm{P}(\mathrm{A}\cap\mathrm{B})=\frac{1}{216}$$

Then 

$$\mathrm{P}(\mathrm{A}|\mathrm{B})=\frac{\mathrm{P}(\mathrm{A}\cap\mathrm{B})}{\mathrm{P}(\mathrm{B})}=\frac{\frac{1}{216}}{\frac{6}{216}}=\frac{1}{6}$$

Example 6 A die is thrown twice and the sum of the numbers appearing is observed to be 6. What is the conditional probability that the number 4 has appeared at least once?



Solution Let E be the event that 'number 4 appears at least once' and F be the event that 'the sum of the numbers appearing is 6.



Then,

and 

$$\begin{aligned}&\mathrm{E}=\left\{(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(1,4),(2,4),(3,4),(5,4),(6,4)\right\}\\ &\mathrm{F}=\left\{(1,5),(2,4),(3,3),(4,2),(5,1)\right\}\\ \end{aligned}$$

We have 

$$\mathrm{P}(\mathrm{E})=\frac{11}{36}\text{and}\mathrm{P}(\mathrm{F})=\frac{5}{36}$$

Also 

$$\mathrm{E}\cap\mathrm{F}=\{(2,4),(4,2)\}$$

Therefore 

$$\mathrm{P}(\mathrm{E}\cap\mathrm{F})=\frac{2}{36}$$

Hence, the required probability 

$$\mathrm{P}(\mathrm{E}|\mathrm{F})=\frac{\mathrm{P}(\mathrm{E}\cap\mathrm{F})}{\mathrm{P}(\mathrm{F})}=\frac{\frac{2}{36}}{\frac{5}{36}}=\frac{2}{5}$$

For the conditional probability discussed above, we have considered the elementary events of the experiment to be equally likely and the corresponding definition of the probability of an event was used. However, the same definition can also be used in the general case where the elementary events of the sample space are not equally likely, the probabilities P(E∩F) and P(F) being calculated accordingly. Let us take up the following example.



Example 7 Consider the experiment of tossing a coin. If the coin shows head, toss it again but if it shows tail, then throw a die. Find the conditional probability of the event that 'the die shows a number greater than $4^{\circ}$ given that 'there is at least one tail'.



Solution The outcomes of the experiment can be represented in following diagrammatic manner called the 'tree diagram'

The sample space of the experiment may be described as 



<div style="text-align: center;"><img src="imgs/img_in_image_box_623_672_910_931.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;">Fig 13.1</div>


$$\mathrm{S}=\left\{(\mathrm{H},\mathrm{H}),(\mathrm{H},\mathrm{T}),(\mathrm{T},1),(\mathrm{T},2),(\mathrm{T},3),(\mathrm{T},4),(\mathrm{T},5),(\mathrm{T},6)\right\}$$

where (H, H) denotes that both the tosses result into head and T, i) dnotethefrst tos sutinto aal and the number i appeared on the die for $i=1,2,3,4,5,6$ 

Thus, the probabilities assigned to the 8 elementary events 





$\left(\mathrm{H},\mathrm{H}\right),\left(\mathrm{H},\mathrm{T}\right),\left(\mathrm{T},1\right),\left(\mathrm{T},2\right),\left(\mathrm{T},3\right)\left(\mathrm{T},4\right),\left(\mathrm{T},5\right),\left(\mathrm{T},6\right)$ $\mathrm{are}\frac{1}{4},\frac{1}{4},\frac{1}{12},\frac{1}{12},\frac{1}{12},\frac{1}{12},\frac{1}{12},\frac{1}{12}$ respectively which is clear from the Fig 13.2.



$$\widehat{V_{4}}^{\prime}(\mathrm{H},\mathrm{T}) 1$$

$$\gamma_{12}$$

$$\bar{\underline{{\underline{\gamma}}}}_{12} (T,3)$$

$$(T,3)\overline{\gamma}_{12}(T,4)$$

$$\overline{{y_{12}}} (T,4)$$

<div style="text-align: center;">Fig 13.2</div>


LetFbetheeventthatthereisatlastonetail'andEbetheeventthedieshows a number greater than 4'. Then 



Now 

$$\begin{aligned}\mathrm{F}&=\{(\mathrm{H},\mathrm{T}),(\mathrm{T},1),(\mathrm{T},2),(\mathrm{T},3),(\mathrm{T},4),(\mathrm{T},5),(\mathrm{T},6)\}\\\mathrm{E}&=\{(\mathrm{T},5),(\mathrm{T},6)\}\quad and\quad\mathrm{E}\cap\mathrm{F}=\{(\mathrm{T},5),(\mathrm{T},6)\}\\\mathrm{P}(\mathrm{F})&=\mathrm{P}(\{(\mathrm{H},\mathrm{T})\})+\mathrm{P}\left(\{(\mathrm{T},1)\}\right)+\mathrm{P}\left(\{(\mathrm{T},2)\}\right)+\mathrm{P}\left(\{(\mathrm{T},3)\}\right)\\&\quad+\mathrm{P}\left(\{(\mathrm{T},4)\}\right)+\mathrm{P}(\{(\mathrm{T},5)\})+\mathrm{P}(\{(\mathrm{T},6)\})\\&=\frac{1}{4}\cdot\frac{1}{12}\cdot\frac{1}{12}\cdot\frac{1}{12}\cdot\frac{1}{12}\cdot\frac{1}{12}\cdot\frac{1}{12}\cdot\frac{3}{4}\end{aligned}$$

and 

$$\mathrm{P}(\mathrm{E}\cap\mathrm{F})=\mathrm{P}\left(\{(\mathrm{T},5)\}\right)+\mathrm{P}\left(\{(\mathrm{T},6)\}\right)=\frac{1}{12}\cdot\frac{1}{12}\cdot\frac{1}{6}$$

Hence 

$$\mathrm{P}(\mathrm{E}|\mathrm{F})=\frac{\mathrm{P}(\mathrm{E}\cap\mathrm{F})}{\mathrm{P}(\mathrm{F})}=\frac{\frac{1}{6}}{\frac{3}{4}}=\frac{2}{9}$$

### E13.1

1.$\mathrm{P}(\mathrm{E}\cap\mathrm{F})=0.2$ , find P(E|F) and P(F|E)and F are events such that h a $$ and 

2. Compute $\mathrm{P}(\mathrm{A}|\mathrm{B})$ $\mathrm{if}\mathrm{P}(\mathrm{B})=0.5and\mathrm{P}(\mathrm{A}\cap\mathrm{B})=0.32$ 

3.If $\mathrm{P}(\mathrm{A})=0.8,\mathrm{P}(\mathrm{B})=0.5\text{and}\mathrm{P}(\mathrm{B}|\mathrm{A})=0.4$ , find 

(i)$\mathbb{P}(\mathrm{A}\cap\mathrm{B})$ $\mathbb{P}(\mathbb{A}|\mathbb{B})$ (iii)$\mathrm{P(A\cup B)}$ 

Evaluate $\mathbb{P}(\mathrm{A}\cup\mathrm{B})$ if $2\mathrm{P}(\mathrm{A})=\mathrm{P}(\mathrm{B})=\frac{5}{13}\text{and}\mathrm{P}(\mathrm{A}|\mathrm{B})=\frac{2}{5}$ 

$\mathrm{If}\;\mathrm{P}(\mathrm{A})=\frac{6}{11},\mathrm{P}(\mathrm{B})=\frac{5}{11}\;\mathrm{and}\;\mathrm{P}(\mathrm{A}\cup\mathrm{B})\quad\frac{7}{11}$ , find 

(i)$\mathrm{P}(\mathrm{A}\cap\mathrm{B})$ (ii)$\mathrm{P}(\mathrm{A}|\mathrm{B})$ (mi)$\mathrm{P}(\mathrm{B}|\mathrm{A})$ 

Determine $\mathbb{P}(\mathrm{E}|\mathrm{F})$ in Exercises 6 to 9.

A coin is tossed three times, where 

(i) E : head on third toss ,F : heads on first two tosses 

(ii)) E : at least two heads,F: at most two heads 

(ii) E : at most two tails,F : at least one tail 

7. Two coins are tossed once, where 

(i) E : tail appears on one coin,F : one coin shows head 

(i) E : no tail appears,F : no head appears 

8.A die is thrown three times,

E: 4 appears on the third toss,F : 6 and 5 appears respectively on first two tosses 

9.Mother, father and son line up at random for a family picture E : son on one end,F: father in middle 

10. A black and a red dice are rolled.

that the black die resulted in a 5.



(indofue resulted in a number less than 4.



11. A fair die is rolled. Consider events $\mathrm{E}=\{1,3,5\}$ },$\mathrm{F}=\{2,3\}\text{and}\mathrm{G}=\{2,3,4,5\}$ Find 



(i)$\mathbb{P}(\mathrm{E}|\mathrm{F})$ and P(F|E)(ii)$\mathbb{P}(\mathrm{E}|\mathrm{G})$  and P(G|E)

(ii)$\mathbb{P}((\mathbb{E}\cup\mathbb{F})|\mathbb{G})$  and P ((E ∩ F)|G)

12.AssumetchbrildisqullyliklytobboyolIffamlyhas two children, whatis the conditional probabilitythat bothare girls given that (i) the youngest is a girl, (ii) at least one is a girl?



13.An instructorhas a questionbank consisting of300easy True/False questions,200 difficult True/ False questions, 500 easy multiple choice questions and 400difficult multiple choice questions. If a question is selected at random from the question bank, what is the probability that it will be aneasy question given that it is a multiple choice question?



14.Given that the two numbers appearing on throwing two dice are different. Find the probability of the event 'the sum of numbers on the dice is $4^{\circ}$ 

15.Consider the experiment of throwing a die if a multiple of3 comes up,throw the dieagain iyr urm .enial lity oftheeventthecoin shows atailgiventhatat leastone dieshows a3.

In each of the Exercises 16 and 17 choose the correct answer:

16. If $\mathrm{P}(\mathrm{A})=\frac{1}{2},\mathrm{P}(\mathrm{B})=0$ ,then $\mathbb{P}(\mathrm{A}|\mathrm{B})$ is 

(A) 0(B)$\left[\frac{1}{2}\right.]$ (C) not defined 

(D) 1 17. If A and B are events such that $\mathrm{P}(\mathrm{A}|\mathrm{B})=\mathrm{P}(\mathrm{B}|\mathrm{A})$ .,then 

$$\begin{align*}\left(A\right)A&\subset B but A\neq B\quad&\left(B\right)A=B\\\left(C\right)A&\cap B=\varnothing\quad&\left(D\right)P(A)&=P(B)\end{align*}$$

### 13.3 Multiplication Theorem on Probability 

Let E and F be two events associated with a sample space S. Clearly, the set E ∩ F denotes the event that both E and F have occurred. In other words, E ∩F denotes the simultaneous occurrence of the events E and F. The event E ∩F is also written as EF.

Very often we need to find the probability of the event EF. For example, in the experiment of drawing two cards one after the other, we may be interested in finding the probability of the event 'a king and a queen'. The probability of event EF is obtained by using the conditional probability as obtained below :

We know that the conditional probability of event E given that F has occurred is denoted by P(E|F) and is given by 



$$\mathrm{P}(\mathrm{E}|\mathrm{F})=\frac{\mathrm{P}(\mathrm{E}\cap\mathrm{F})}{\mathrm{P}(\mathrm{F})},\mathrm{P}(\mathrm{F})\neq0$$

From this result, we can write 

$$ER \mathrm{P}(\mathrm{E}\cap\mathrm{F})=\mathrm{P}(\mathrm{F}).\mathrm{P}(\mathrm{E}|\mathrm{F})$$

Also, we know that ER 

$$ER \mathrm{P}(\mathrm{F}|\mathrm{E})=\frac{\mathrm{P}(\mathrm{F}\cap\mathrm{E})}{\mathrm{P}(\mathrm{E})},\mathrm{P}(\mathrm{E})\neq0$$

or 

$$ER \mathrm{P}(\mathrm{F}|\mathrm{E})=\frac{\mathrm{P}(\mathrm{E}\cap\mathrm{F})}{\mathrm{P}(\mathrm{E})}\quad(\mathrm{since}\mathrm{E}\cap\mathrm{F}=\mathrm{F}\cap\mathrm{E})$$

Thus,

$$ER 
\mathrm{P}(\mathrm{E}\cap\mathrm{F})=\mathrm{P}(\mathrm{E}).\mathrm{P}(\mathrm{F}|\mathrm{E})$$

Combining (1) and (2), we find that 

$$\begin{aligned}\mathrm{P}(\mathrm{E}\cap\mathrm{F})&=\mathrm{P}(\mathrm{E})\mathrm{P}(\mathrm{F}|\mathrm{E})\\&=\mathrm{P}(\mathrm{F})\mathrm{P}(\mathrm{E}|\mathrm{F})\end{aligned} \mathrm{P}(\mathrm{F})\mathrm{P}(\mathrm{E}|\mathrm{F})\text{provided}\mathrm{P}(\mathrm{E})\neq0\text{and}\mathrm{P}(\mathrm{F})\neq0$$

$$\begin{aligned}\mathrm{P}(\mathrm{E}\cap\mathrm{F})&=\mathrm{P}(\mathrm{E})\mathrm{P}(\mathrm{F}|\mathrm{E})\\&=\mathrm{P}(\mathrm{F})\mathrm{P}(\mathrm{E}|\mathrm{F})\end{aligned} \mathrm{P}(\mathrm{F})\mathrm{P}(\mathrm{E}|\mathrm{F})\text{provided}\mathrm{P}(\mathrm{E})\neq0\text{and}\mathrm{P}(\mathrm{F})\neq0$$

The above result is known as the multiplication rule of probability.

Let us now take up an example.

Example 8 An urn contains 10 black and 5 white balls. Two balls are drawn from the urn one after the other without replacement. What is the probability that both drawn balls are black?



Solution Let E and F denote respectively the events thatfirst and second ball drawn are black. We have to find $\mathbb{P}(\mathrm{E}\cap\mathrm{F})$ or P (EF).



Now 

$$\mathrm{P}(\mathrm{E})=\mathrm{P}(\mathrm{black}\mathrm{ball}in first draw)=\frac{10}{15}$$

Also given that the first ball drawn is black, i.e., event E has occurred, now there are9black balls and five white balls left in the urn.Therefore, the probability that the second ball drawn is black, given that the ball in the first draw is black, is nothing but the conditional probability of F given that E has occurred.



i.e.

$$\mathrm{P}(\mathrm{F}|\mathrm{E})=\frac{9}{14}$$

By multiplication rule of probability, we have 

$$\begin{aligned}P(E\cap F)&=P(E)P(F|E)\\&=\frac{10}{15}\quad\frac{9}{14}\quad\frac{3}{7}\end{aligned}$$

Multiplication rule of probability for more than two events If E, F and G are three events of sample space, we have 



$$\mathrm{P}(\mathrm{E}\cap\mathrm{F}\cap\mathrm{G})=\mathrm{P}(\mathrm{E})\mathrm{P}(\mathrm{F}|\mathrm{E})\mathrm{P}(\mathrm{G}|(\mathrm{E}\cap\mathrm{F}))=\mathrm{P}(\mathrm{E})\mathrm{P}(\mathrm{F}|\mathrm{E})\mathrm{P}(\mathrm{G}|\mathrm{E}\mathrm{F})$$

Similarly, the multiplication rule of probability can be extended for four or more events.



The following example illustrates the extension of multiplication rule of probability for three events.



Example 9 Three cards are drawn successively, without replacement from a pack of 52 well shuffled cards. What is the probability that first two cards are kings and the third card drawn is an ace?



Solution Let K denote the event that the card drawn is king and A be the event that the card drawn is an ace. Clearly, we have to find P (KKA)

Now 

$$\mathrm{P}(\mathrm{K})=\frac{4}{52}$$

Also,$\mathbb{P}\left(\mathbb{K}|\mathbb{K}\right)$ is the probability of second king with the condition that one king has already been drawn. Now there are three kings in $(52-1)=51$ cards.

Therefore 

$$\mathrm{P}(\mathrm{K}|\mathrm{K})=\frac{3}{51}$$

Lastly, P(AKK) is the probability of third drawcard to be an ace, with thecondition that two kings have already been drawn. Now there are four aces in left 50 cards.

Therefore 

$$\mathrm{P}(\mathrm{A}|\mathrm{KK})=\frac{4}{50}$$

By multiplication law of probability, we have 

$$\begin{aligned}\mathrm{P}(\mathrm{KKA})&=\mathrm{P}(\mathrm{K})\quad\mathrm{P}(\mathrm{K}|\mathrm{K})\quad\mathrm{P}(\mathrm{A}|\mathrm{KK})\\&=\frac{4}{52}\quad\frac{3}{51}\quad\frac{4}{50}\quad\frac{2}{5525}\end{aligned}$$

### 13.4 Independent Events 

Consider the experiment of drawing a card from a deck of 52 playing cards, in which the elementary events are assumed to be equally likely. If E and F denote the events 'the card drawn is a spade' and 'the card drawn is an ace' respectively, then 

$$\mathrm{P}(\mathrm{E})=\frac{13}{52}\quad\frac{1}{4}\text{and}\quad\mathrm{P}(\mathrm{F})\quad\frac{4}{52}\quad\frac{1}{13}$$

Also E and F is the event'the card drawn is the ace of spades' so that 

$$\mathbb{P}(\mathbb{E}\cap\mathbb{F})=\frac{1}{52}$$

Hence 

$$\mathrm{P}(\mathrm{E}|\mathrm{F})=\frac{\mathrm{P}(\mathrm{E}\quad\mathrm{F})}{\mathrm{P}(\mathrm{F})}\quad\frac{\frac{1}{52}}{\frac{1}{13}}\quad\frac{1}{4}$$

Since $\mathrm{P}(\mathrm{E})=\frac{1}{4}=\mathrm{P}$ (E|F), we can say that the occurrence of event F has not affected the probability of occurrence of the event E.



We also have 

$$\mathrm{P}(\mathrm{F}|\mathrm{E})=\frac{\mathrm{P}(\mathrm{E}\quad\mathrm{F})}{\mathrm{P}(\mathrm{E})}\quad\frac{\frac{1}{52}}{\frac{1}{4}}\quad\frac{1}{13}\quad\mathrm{P}(\mathrm{F})$$

Again,$\mathrm{P}(\mathrm{F})=\frac{1}{13}=\mathrm{P}(\mathrm{F}|\mathrm{E})$ shows that occurrence of event E has not affected the probability of occurrence of the event F.



Thus, E and F are two events such that the probability of occurrence of one of them is not affected by occurrence of the other.



Such events are called independent events.

Definition2 Two events E and F are said to be independent, if 

$$\mathrm{P}(\mathrm{F}|\mathrm{E})=\mathrm{P}(\mathrm{F})\text{provided}\mathrm{P}(\mathrm{E})\neq0$$

and 

$$\mathrm{P}(\mathrm{E}|\mathrm{F})=\mathrm{P}(\mathrm{E})\text{provided}\mathrm{P}(\mathrm{F})\neq0$$

Thus, in this definition we need to have $\mathrm{P}(\mathrm{E})\neq0\text{and}\mathrm{P}(\mathrm{F})\neq0$ 

Now, by the multiplication rule of probability, we have 

$$\mathrm{P}(\mathrm{E}\cap\mathrm{F})=\mathrm{P}(\mathrm{E}).\mathrm{P}(\mathrm{F}|\mathrm{E})$$

IfE and F are independent, then (1) becomes 

$$\mathrm{P}(\mathrm{E}\cap\mathrm{F})=\mathrm{P}(\mathrm{E}).\mathrm{P}(\mathrm{F})$$

Thus, using (2), the independence of two events is also defined as follows:

Definition 3 Let E and F be two events associated with the same random experiment,then E and F are said to be independent if 



$$\mathrm{P}(\mathrm{E}\cap\mathrm{F})=\mathrm{P}(\mathrm{E}).\mathrm{P}(\mathrm{F})$$

## Remarks 

(i)Two eventsE and F are said tobe dependent if theyarenotindependent, i.e if 

$$\mathbb{P}(\mathbb{E}\cap\mathbb{F})\neq\mathbb{P}(\mathbb{E}).\mathbb{P}(\mathbb{F})$$

(ii) Sometimes there is a confusion between independent events and mutually exclusive events.Term indepndent' is defined intermsof'probability of events'whereas mutually exclusive is defined in term of events (subset of sample space).Moreover, mutually exclusive events never have an outcome common, but independent events, may have common outcome. Clearly, independent' and 'mutually exclusive' do not have the same meaning.



In other words, two independent events having nonzero probabilities of occurrence can not be mutually exclusive, and conversely, i.e. two mutually exclusive events having nonzero probabilities of occurrence can not be independent.

(ii)Two experiments are said to be independent if for every pair of events E and F,where E is associated with the first experiment and F with the second experiment,the probability of the simultaneous occurrence of the events E and F when the two experiments are performed is the product of P(E) and P(F) calculated separately on the basis of two experiments, i.e.,$\mathrm{P}(\mathrm{E}\cap\mathrm{F})=\mathrm{P}(\mathrm{E}).\mathrm{P}(\mathrm{F})$ 

(iv)Three events A, B and C are said to be mutually independent, if 

and 

$$\begin{aligned}P(A\cap B)&=P(A)P(B)\\ P(A\cap C)&=P(A)P(C)\\ P(B\cap C)&=P(B)P(C)\\ P(A\cap B\cap C)&=P(A)P(B)P(C)\end{aligned}$$

If at least one of the above is not true for three given events, we say that the events are not independent.



Example 10 A die is thrown. If E is the event 'the number appearing is a multiple of $3^{\circ}$ and F be the event 'the number appearing is even'then find whether E and F are independent ?



Solution We know that the sample space is $\mathrm{S}=\{1,2,3,4,5,6\}$ 

Now $\mathrm{E}=\{3,6\},\mathrm{F}=\{2,4,6\}\text{and}\mathrm{E}\cap\mathrm{F}=\{6\}$ 

Then 

$$\mathrm{P}(\mathrm{E})=\frac{2}{6}=\frac{1}{3},\mathrm{P}(\mathrm{F})=\frac{3}{6}=\frac{1}{2}\text{and}\mathrm{P}(\mathrm{E}\cap\mathrm{F})=\frac{1}{6}$$

Clearly $\mathrm{P}(\mathrm{E}\cap\mathrm{F})=\mathrm{P}(\mathrm{E}).\mathrm{P}(\mathrm{F})$ 

Hence E and F are independent events.

Example 11 An unbiased die is thrown twice. Let the event A be 'odd number on the first throw' and B the event 'odd number on the second throw'.Check the independence of the events A and B.



Solution If all the 36 elementary events of the experiment are considered to be equally likely, we have cYnaGentaent 



$$\mathrm{P}(\mathrm{A})=\frac{18}{36}=\frac{1}{2}\text{and}\mathrm{P}(\mathrm{B})\setminus\frac{18}{36}\setminus\frac{1}{2}$$

Also 

$$ (odd number on both throws)

$$\frac{9}{36}=\frac{1}{4}$$

Now 

$$\mathrm{P}(\mathrm{A})\mathrm{P}(\mathrm{B})=\frac{1}{2}\times\frac{1}{2}=\frac{1}{4}$$

Clearly 

$$\mathrm{P}(\mathrm{A}\cap\mathrm{B})=\mathrm{P}(\mathrm{A})\times\mathrm{P}(\mathrm{B})$$

Thus,A and B are independent events 

Example 12 Three coins are tossed simultaneously. Consider the event E 'three heads or three tails, F 'at least two heads' and $\mathrm{G}$ 'at most two heads'. Of the pairs (E,F)$\left(\mathrm{E,G}\right)$ and $\left(\mathrm{F},\mathrm{G}\right)$ , which are independent? which are dependent?

Solution The sample space of the experiment is given by 

$\mathrm{S}=\{\mathrm{HHH},\mathrm{HHT}\}$ ,HTH, THH, HTT, THT, TTH, TTT}

Clearly 

$$\mathrm{E}=\{\mathrm{HHH},\mathrm{TTT}\},\mathrm{F}=\{\mathrm{HHH},\mathrm{HHT},\mathrm{HTH},\mathrm{THH}\}$$

and 

$$\mathrm{G}=\{\mathrm{HHT},\mathrm{HTH},\mathrm{THH},\mathrm{HTT},\mathrm{THT},\mathrm{TTH},\mathrm{TTT}\}$$

Also 

$$\mathrm{E}\cap\mathrm{F}=\{\mathrm{HHH}\},\mathrm{E}\cap\mathrm{G}=\{\mathrm{TTT}\},\mathrm{F}\cap\mathrm{G}=\{\mathrm{HHT},\mathrm{HTH},\mathrm{THH}\}$$

Therefore 

$$\mathrm{P}(\mathrm{E})=\frac{2}{8}=\frac{1}{4},\mathrm{P}(\mathrm{F})=\frac{4}{8}=\frac{1}{2},\mathrm{P}(\mathrm{G})=\frac{7}{8}$$

and 

$$\mathrm{P}(\mathrm{E}\cap\mathrm{F})=\frac{1}{8},\mathrm{P}(\mathrm{E}\cap\mathrm{G})=\frac{1}{8},\mathrm{P}(\mathrm{F}\cap\mathrm{G})=\frac{3}{8} ublish $$

Also 

$$\mathrm{P}(\mathrm{E}).\mathrm{P}(\mathrm{F})=\frac{1}{4}\quad\frac{1}{2}\quad\frac{1}{8},\mathrm{P}(\mathrm{E})\quad\mathrm{P}(\mathrm{G})\quad\frac{1}{4}\quad\frac{7}{8}\quad\frac{7}{32} ublish $$

and 

$$\mathrm{P}(\mathrm{F}).\mathrm{P}(\mathrm{G})=\frac{1}{2}\quad\frac{7}{8}\quad\frac{7}{16}$$

Thus 

and 

$$\begin{aligned}\mathrm{P}(\mathrm{E}\cap\mathrm{F})&=\mathrm{P}(\mathrm{E}).\mathrm{P}(\mathrm{F})\\\mathrm{P}(\mathrm{E}\cap\mathrm{G})&\neq\mathrm{P}(\mathrm{E}).\mathrm{P}(\mathrm{G})\\\mathrm{P}(\mathrm{F}\cap\mathrm{G})&\neq\mathrm{P}(\mathrm{F}).\mathrm{P}(\mathrm{G})\end{aligned}$$

Hence, the events (E and F) are independent, and the events (E and G) and ublish (F and G) are dependent.



Example13 Prove that if E and F are independent events, then so are the events E and $\mathrm{F^{\prime}}$ 



Solution Since E and F are independent, we have 

$$\mathrm{P}(\mathrm{E}\cap\mathrm{F})=\mathrm{P}(\mathrm{E}).\mathrm{P}(\mathrm{F})$$

From the venn diagram in Fig 13.3, it is clear that E∩ F andE $\cap\mathrm{F}'$ are mutually exclusive events and also $\mathrm{E}=(\mathrm{E}\cap\mathrm{F})\cup(\mathrm{E}\cap\mathrm{F})$ 



Therefore 

$$\mathrm{P}(\mathrm{E})=\mathrm{P}(\mathrm{E}\cap\mathrm{F})+\mathrm{P}(\mathrm{E}\cap\mathrm{F}')$$

or 

$$\begin{aligned}\mathrm{P}(\mathrm{E}\cap\mathrm{F}^{\prime})&=\mathrm{P}(\mathrm{E})-\mathrm{P}(\mathrm{E}\cap\mathrm{F})\\&=\mathrm{P}(\mathrm{E})-\mathrm{P}(\mathrm{E}).\mathrm{P}(\mathrm{F})\\&\quad(\mathrm{by}(1))\\&=\mathrm{P}(\mathrm{E})(1-\mathrm{P}(\mathrm{F}))\\&=\mathrm{P}(\mathrm{E}).\mathrm{P}(\mathrm{F}^{\prime})\end{aligned}$$

Hence, E and $\mathrm{F}^{\prime}$ are independent 

$$(\mathbf{E}^{\prime}{\cap}\mathbf{F}^{\prime})$$

<div style="text-align: center;">Fig 13.3</div>


NoteInasimilarmanner,itcanbeshownthatiftheeventsEandFare independent, then 

(a)$\mathrm{E}^{\prime}$ and F are independent,(b)$\mathrm{E^{\prime}}$ and $\mathrm{F^{\prime}}$ are independent of at least one of A and B is given by Example14IfBeindp $1-\mathrm{P}(\mathrm{A}^{\prime})\mathrm{P}(\mathrm{B}^{\prime})$  ,

## Solution We have 

P(at least one of A ;$$ c)

### EXERCISE 13.2

1.$\mathrm{If~P(A)\quad\frac{3}{5}~and~P(B)\quad\frac{1}{5}~}$ , find $\mathrm{P}(\mathrm{A}\cap\mathrm{B})$ if A and B are independent events.

2. Two cards are drawn at random and without replacement from a pack of 52playing cards. Find the probability that both the cards are black.

3.. A box of oranges is inspected by examining three randomly selected oranges drawn without replacement. If all the thre oranges are good, the box is approved for sale, otherwise, it is rejected. Find the probability that a box containing 15oranges out of which 12 are good and 3 are bad ones will be approved for sale.

A fair coin and an unbiased die are tossed. Let A be the event head appears on the coin'and B be the event $^{\circ}3$ on the $\mathrm{die}^{\prime}$ .Check whether Aand Bare independent events or not.



5.Adie marked 1, 2,3 in red and 4, 5,6 in green is tossed.Let A be the event,the number is even,'and B be the event,the number is red'. Are A and B independent?



Let E and F be events with P(E)$\frac{3}{5},\mathrm{P}(\mathrm{F})=\frac{3}{10}and\mathrm{P}(\mathrm{E}\cap\mathrm{F})=\frac{1}{5}$ . Are E and F independent?



7. Given that the events A and B are such that $\mathrm{P}(\mathrm{A})=\frac{1}{2},\mathrm{P}(\mathrm{A}\cup\mathrm{B})=\frac{3}{5}$ and [Ta $P(B)=p$ i a 

8.L Ta and B e p  $\mathrm{P}(\mathrm{A})=0.3\mathrm{~and~P}(\mathrm{B})=0.4$ . Find 

(i)[Tab]$\mathrm{P}(\mathrm{A}\cap\mathrm{B})$ (ii)$\mathrm{P}(\mathrm{A}\cup\mathrm{B})$ 

(ii)$\mathrm{P(A|B)}$ E]$\mathrm{P}(\mathrm{B}|\mathrm{A})$ 

9.If A and B are two events such that $\mathrm{P}(\mathrm{A})=\frac{1}{4},\mathrm{P}(\mathrm{B})=\frac{1}{2}\text{and}\mathrm{P}(\mathrm{A}\cap\mathrm{B})=\frac{1}{8}$ find P (not A and not B).



10. Events A and B are such that $\mathrm{P}(\mathrm{A})=\frac{1}{2},\mathrm{P}(\mathrm{B})=\frac{7}{12}\text{and}\mathrm{P}(\mathrm{not}\mathrm{A}\text{or not}\mathrm{B})=\frac{1}{4}$ State whether A and B are independent ?



11. Given two independent events A and B such that $\mathrm{P}(\mathrm{A})=0.3,\mathrm{P}(\mathrm{B})=0.6$ Find 



(i) P(A and B)(i) P(A and not B)(iii) P(A or B)(iv) P(neither A nor B)

12.Ae.lofmtc 

13.Twoleatdmthplemetomoxaii1ba and 8 red balls.Find the probability that 

(i)both balls are red.

(ii) first ball is black and second is red.

(im) one of them is black and other is red.

14. Probability of solving specific problem independently by Aand B are $\left[\frac{1}{2}\bmod\frac{1}{3}\right.]$ respecilty that 



(i)the problem is solved (ii) exactly one of them solves the problem.

15.One card is drawn at random from a well shuffled deck of 52 cards. In which of the following cases are the events E and F independent ?

(i) E : 'the card drawn is a spade'

F :'the card drawn is an ace'

(ii) E : 'the card drawn is black'

F :'the card drawn is a king 

(i) E : 'the card drawn is a king or queen"

F:'the card drawn is a queen or jack'.

16.In a hostl,60%ofthe students read Hindiews papr, 40%read English news paper and 20% read both Hindi and English news papers. A student is selected at random.



(a) Find the probability that she reads neither Hindi nor English news papers.

(b) If she reads Hindi news paper, find the probability that she reads English news paper.



(c) If she reads English news paper, find the probability that she reads Hindi news paper.



Choose the correct answer in Exercises 17 and 18.

dice is rolled is 



(A)0(B)$\frac{1}{3}$ (C)$\frac{1}{12}$ $\frac{1}{36}$ 

if 

(A) A and B are mutually exclusive 

(B)$\mathrm{P}(\mathrm{A}^{\prime}\mathrm{B}^{\prime})=[1-\mathrm{P}(\mathrm{A})][1-\mathrm{P}(\mathrm{B})]$ 

(C)$\mathrm{P}(\mathrm{A})=\mathrm{P}(\mathrm{B})$ 

(D)$\mathrm{P}(\mathrm{A})+\mathrm{P}(\mathrm{B})=1$ 

### 13.5 Bayes' Theorem 

L contains 2 white and.BagII contains 4 white and 5 red balls. One ball is drawn at random from one of the bags. Wecan find the probability of selecting any ofthe bags $(\mathrm{i.e.}\frac{1}{2})$ ) or probability of drawing a ball of a particular colour (say white) from a particular bag (say Bag I). In other words,wecan find the probabilitythattheball drawnisof a particular colour, if wearemclllthat the ball drawn is from a particular bag (say Bag II), if the colour ofthe ball drawn is given? Here, we have to find the reverse probability of Bag II to be selected when an event occurred afer it is known.Famous mathematician, John ayessolved the problem offidl .ervloped by him is known as 'Bayes theorem' which was published posthumously in 1763.Beforestatingand proving the Bayes'theorem, letufirsttake upa definition and some preliminary results.



#### 13.5.1 Partition of a sample space 

A set of events $\mathrm{E}_{1},\mathrm{E}_{2},...,\mathrm{E}_{\mathrm{n}}$ is said to represent a partition of the sample space S if 

(a)

$$\mathrm{E}_{i}\cap\mathrm{E}_{j}=\varnothing,i\neq j,i,j=1,2,3,\ldots,n $$

$$\begin{aligned}&\left(\mathrm{b}\right)\mathrm{E}_{1}\cup\mathrm{E}_{2}\cup\ldots\cup\mathrm{E}_{n}=\mathrm{S}and\\&\left(\mathrm{c}\right)\mathrm{P}(\mathrm{E}_{i})>0for all i=1,2,\ldots,n.\\ \end{aligned}$$

In other words, the events $\mathrm{E}_{1},\mathrm{E}_{2},...,\mathrm{E}_{n}$ represent a partition of the sample space Sifthey erej,auivendave obabilities.

Asanexamwelement $\mathrm{E^{\prime}}$ form a partition of the sample space S since they satisfy E $\mathrm{E}\cap\mathrm{E}'=\varnothing and\mathrm{E}\cup\mathrm{E}'=\mathrm{S}$ 

From the Venn diagram in Fig13.3, onecan easily observe that ifE and F are any two events associated with a sample space S, then the set $\{\mathrm{E}\cap\mathrm{F}^{\prime},\mathrm{E}\cap\mathrm{F},\mathrm{E}^{\prime}\cap\mathrm{F},\mathrm{E}^{\prime}\underline{{\cap\mathrm{F}^{\prime}}}\}$ is a partition of the sample space S. It may be mentioned that the partition of a sample space is not unique. There can be several partitions of the same sample space.

We shall now prove a theorem known as Theorem of total probability.

#### 13.5.2 Theorem of total probability 

Let $\{\mathrm{E}_{1},\mathrm{E}_{2},...,\mathrm{E}_{n}\}$ be a partitionof the sample space S,and suppose that each of the events $\mathrm{E}_{1},\mathrm{E}_{2},...,\mathrm{E}_{n}$ has nonzero probability of occurrence. LetAbe any event associated with $\mathrm{S}.$ then 



$$\begin{align*}\mathrm{P}(\mathrm{A})&=\mathrm{P}(\mathrm{E}_1)\mathrm{P}(\mathrm{A}|\mathrm{E}_1)+\mathrm{P}(\mathrm{E}_2)\mathrm{P}(\mathrm{A}|\mathrm{E}_2)+\ldots+\mathrm{P}(\mathrm{E}_n)\mathrm{P}(\mathrm{A}|\mathrm{E}_n)\\&=\sum_{j=1}^{n}\mathrm{P}(\mathrm{E}_j)\mathrm{P}(\mathrm{A}|\mathrm{E}_j)\end{align*}$$

Proof Given that $\mathrm{E}_{1},\mathrm{E}_{2},\ldots,\mathrm{E}_{n}$ is a partition of the sample space S (Fig 13.4). Therefore,

and 

$$\begin{array}{c}\mathrm{S}=\mathrm{E}_{1}\cup\mathrm{E}_{2}\cup\ldots\cup\mathrm{E}_{n}\\\mathrm{E}_{i}\cap\mathrm{E}_{j}=\varnothing,i\neq j,i,j=1,2,\ldots,n\end{array}$$

Now, we know that for any event A,

$$\begin{aligned}\mathrm{A}&=\mathrm{A}\cap\mathrm{S}\\&=\mathrm{A}\cap\left(\mathrm{E}_{1}\cup\mathrm{E}_{2}\cup\ldots\cup\mathrm{E}_{n}\right)\\&=\left(\mathrm{A}\cap\mathrm{E}_{1}\right)\cup\left(\mathrm{A}\cap\mathrm{E}_{2}\right)\cup\ldots\cup\left(\mathrm{A}\cap\mathrm{E}_{n}\right)\end{aligned}$$

$$\mathrm{E}_{3}$$

<div style="text-align: center;">Fig 13.4</div>


Also $\mathrm{A}\cap\mathrm{E}_{i}and\mathrm{A}\cap\mathrm{E}_{j}$ are respectively the subsets of $\mathrm{E}_{i}$ and $\mathrm{E}_{j}$ . We know that $\mathrm{E}_{i}$ and $\mathrm{E}_{j}$ are disjoint, for $i\ne j$ ,therefore,$ A\cap E_i$ and $\mathrm{~A~}\cap\mathrm{E}_{j}$ are also disjoint for all 

$i\ne j,i,j=1,2,\ldots,n$ 



Thus,

$$\begin{aligned}\mathrm{P}(\mathrm{A})&=\mathrm{P}\left[(\mathrm{A}\cap\mathrm{E}_{1})\cup(\mathrm{A}\cap\mathrm{E}_{2})\cup\ldots\cup(\mathrm{A}\cap\mathrm{E}_{n})\right]\\&=\mathrm{P}\left(\mathrm{A}\cap\mathrm{E}_{1}\right)+\mathrm{P}\left(\mathrm{A}\cap\mathrm{E}_{2}\right)+\ldots+\mathrm{P}\left(\mathrm{A}\cap\mathrm{E}_{n}\right)\end{aligned}$$

Now, by multiplication rule of probability, we have 

$$\mathrm{P}(\mathrm{A}\cap\mathrm{E}_{i})=\mathrm{P}(\mathrm{E}_{i})\mathrm{P}(\mathrm{A}|\mathrm{E}_{i})\text{as}\mathrm{P}(\mathrm{E}_{i})\neq0\forall i=1,2,\ldots,n $$

Therefore,

or 

$$\begin{align*}\mathrm{P}(\mathrm{A})&=\mathrm{P}(\mathrm{E}_1)\mathrm{P}(\mathrm{A}|\mathrm{E}_1)+\mathrm{P}(\mathrm{E}_2)\mathrm{P}(\mathrm{A}|\mathrm{E}_2)+\ldots+\mathrm{P}(\mathrm{E}_n)\mathrm{P}(\mathrm{A}|\mathrm{E}_n)\\\mathrm{P}(\mathrm{A})&=\sum_{j=1}^{n}\mathrm{P}(\mathrm{E}_j)\mathrm{P}(\mathrm{A}|\mathrm{E}_j)\end{align*}$$

Example 15 A person has undertaken a construction job. The probabilities are 0.65that there wll be,.tt teontutin b ill eompledtimeif tee isno strike, and 0.32 thattheconstruction job will becompleted ontime if there is a strike.Determine the probabilitythat theconstruction job will becompleted on time.Solution Let A be the event that the construction job will be completed on time, and B be the event that there will be a strike. We have to find $\mathrm{P}(\mathrm{A})$ 

$$\mathrm{P}(\mathrm{B})=0.65,\mathrm{P}(\mathrm{no}\ \mathrm{strike})=\mathrm{P}(\mathrm{B}^{\prime})=1-\mathrm{P}(\mathrm{B})=1-0.65=0.35,\mathrm{P}(\mathrm{A}|\mathrm{B})=0.32,\mathrm{P}(\mathrm{A}|\mathrm{B}^{\prime})=0.80$$

Since events B and B' form a partition of the sample space S, therefore, by theorem on total probability, we have 



$$\begin{aligned}\mathrm{P}(\mathrm{A})&=\mathrm{P}(\mathrm{B})\mathrm{P}(\mathrm{A}|\mathrm{B})+\mathrm{P}(\mathrm{B}^{\prime})\mathrm{P}(\mathrm{A}|\mathrm{B}^{\prime})\\&=0.65\times0.32+0.35\times0.8\\&=0.208+0.28=0.488\end{aligned}$$

Thus, the probability that the construction job will becomleted in time is 0.48.

We shall now state and prove the Bayes' theorem.

Bayes' Theorem If $\underline{{\mathrm{E}}}_{1},\underline{{\mathrm{E}}}_{2},...,\underline{{\mathrm{E}}}_{n}$ are n non empty events which constitute a partition of sample space S,$\mathrm{i.e.E_{1},E_{2},\ldots,E_{n}}$ are pairwise disjoint and $\mathrm{E}_{1}\cup\mathrm{E}_{2}\cup\ldots\cup\mathrm{E}_{n}=\mathrm{S}$ and A is any event of nonzero probability, then 



$$\mathrm{P}(\mathrm{E}_{i}|\mathrm{A})=\frac{\mathrm{P}(\mathrm{E}_{i})\mathrm{P}(\mathrm{A}|\mathrm{E}_{i})}{\sum_{j=1}^{n}\mathrm{P}(\mathrm{E}_{j})\mathrm{P}(\mathrm{A}|\mathrm{E}_{j})}\quad\text{for any}i=1,2,3,\ldots,n $$

Proof By formula of conditional probability, we know that 

$$not \begin{aligned}\mathrm{P}(\mathrm{E}_{i}\mathrm{A})&=\frac{\mathrm{P}(\mathrm{A}\cap\mathrm{E}_{i})}{\mathrm{P}(\mathrm{A})}\\&=\frac{\mathrm{P}(\mathrm{E}_{i})\mathrm{P}(\mathrm{A}|\mathrm{E}_{i})}{\mathrm{P}(\mathrm{A})}(\mathrm{by multiplication rule of probability})\\&=\frac{\mathrm{P}(\mathrm{E}_{i})\mathrm{P}(\mathrm{A}|\mathrm{E}_{i})}{\displaystyle\sum_{j=1}^{n}\mathrm{P}(\mathrm{E}_{j})\mathrm{P}(\mathrm{A}|\mathrm{E}_{j})}(\mathrm{by the result of theorem of total probability})\end{aligned}$$

Remark The following terminology is generally used when Bayes' theorem is applied.

The events $\mathrm{E}_{1},\mathrm{E}_{2},...,\mathrm{E}_{n}$ are called hypotheses.

The probability $\mathrm{P}(\mathrm{E}_i)$ is called the priori probability of the hypothesis $\mathrm{E}_{i}$ 

The conditional probability $\mathbb{P}(\mathrm{E}_{{}_{i}}\left|\mathrm{A}\right)$ is called a posteriori probability of the hypothesis $\mathrm{E}_i$ 



Bayes' theorem is also called the formula for the probability of"causes". Since the $\mathrm{E_{i}^{'s}}$ e $\mathrm{E}_{i}$ occurs (i.e.one of the events $\mathrm{E}_{i}$ mustc.eul gs $\mathrm{E}_i$ (ie occurred.



TheBayes'theorem hasits applicationsin varietyof situations,fewof which are illustrated in following examples.



Example16BagIcotainredandblackbllswleanoeragIIcontins5red and6blackbll.Oneball isdrawnatrandomfromoneofthebaganditisfound to be red. Find the probability that it was drawn from Bag II.



Solution Let $\mathrm{E_1}$ be the event of choosin t $ E_2$ the event of choosing the bag II and A be the event of drawing a red ball.



Then 

Also 

and 

$$\mathrm{P}(\mathrm{E}_{1})=\mathrm{P}(\mathrm{E}_{2})=\frac{1}{2}$$

Now, the probability of drawing a ball from Bag II, being given that it is red,

$\mathrm{P}(\mathrm{E}_{2}|\mathrm{A})$ 



By using Bayes' theorem, we have 

$$\mathrm{P}(\mathrm{E}_{2}|\mathrm{A})=\frac{\mathrm{P}(\mathrm{E}_{2})\mathrm{P}(\mathrm{A}|\mathrm{E}_{2})}{\mathrm{P}(\mathrm{E}_{1})\mathrm{P}(\mathrm{A}|\mathrm{E}_{1})+\mathrm{P}(\mathrm{E}_{2})\mathrm{P}(\mathrm{A}|\mathrm{E}_{2})}=\frac{\frac{1}{2}\times\frac{5}{11}}{\frac{1}{2}\times\frac{3}{7}+\frac{1}{2}\times\frac{5}{11}}=\frac{35}{68}$$

Example 17 Given three identical boxes I, II and III, each containing two coins. In box I, both coins are gold coins, in box II, both are silver coins and in the box III, there is one gold and one silver coin. A person chooses a box at random and takes out a coin.If the coin is of gold, what is the probability thatthe other coin inthe box is also of gold? Solution Let $ E_1,E_2$ and $\mathrm{E}_{3}$ l 

Then 

$$\mathrm{P}(\mathrm{E}_{1})=\mathrm{P}(\mathrm{E}_{2})=\mathrm{P}(\mathrm{E}_{3})=\frac{1}{3}$$

Also, let A be the event that 'the coin drawn is of gold'

Then 

*[Formula could not be recovered from OCR — see source PDF]*

Now, the probability that te oter coin in the box is of gold 'lishe 

$$\begin{aligned}&\mathrm{I}=\mathrm{the probability that gold coin is drawn from the box I}_{4}\\ &=\mathrm{P}(\mathrm{E}_{1}|\mathrm{A})\\ \end{aligned} 'lishe $$

By Bayes' theorem, we know that 

$$'lishe \begin{aligned}\mathrm{P}(\mathrm{E}_{1}|\mathrm{A})&=\frac{\mathrm{P}(\mathrm{E}_{1})\mathrm{P}(\mathrm{A}|\mathrm{E}_{1})}{\mathrm{P}(\mathrm{E}_{1})\mathrm{P}(\mathrm{A}|\mathrm{E}_{1})+\mathrm{P}(\mathrm{E}_{2})\mathrm{P}(\mathrm{A}|\mathrm{E}_{2})+\mathrm{P}(\mathrm{E}_{3})\mathrm{P}(\mathrm{A}|\mathrm{E}_{3})}\\&=\frac{\frac{1}{3}\times1}{\frac{1}{3}\times1+\frac{1}{3}\times0+\frac{1}{3}\times\frac{1}{2}}=\frac{2}{3}\end{aligned}$$

Example 18 Suppose that the reliability of a HIV test is specified as follows:

Of people having HIV, 90% of the test detect the disease but 10% go undetected. Of people free of HIV, 99% of the test are judged HIV-ive but 1% are diagnosed as showing $\mathrm{HIV}+\mathrm{ive}$ . From a large population of which only 0.1% have HIV, one person is selected at random, given the HIV test, and the pathologist reports him/her as $\mathrm{HIV+ive}$ . What is the probability that the person actually has HIV?

Solution Let E denote the event that the person selected is actually having HIV and A the event that the person's HIV test is diagnosed as +ive. We need to find P(E|A).Also $\mathrm{E}^{\prime}$ denotes the event that the person selected is actually not having HIV.

Clearly, {E,$\mathrm{E^{\prime}\}}$ isroofll.We are given that 



$$\mathrm{P}(\mathrm{E})=0.1\%\quad\frac{0.1}{100}\quad0.001$$

$$\mathrm{P}(\mathrm{E}')=1-\mathrm{P}(\mathrm{E})=0.999$$

and 

Now, by Bayes' theorem 

$$\begin{aligned}P(A|E)&=P(Pearson tested as HIV+ive given that he/shell)\\&\quad is actually having HIV\\&=90\%\quad\frac{90}{100}\quad0.9\end{aligned}lish $$

P(A|E′) = P(Person tested as HIV +ive given that he/she is actually not having HIV)lish 

$$1\%=\frac{1}{100}=0.01$$

$$\mathrm{P}(\mathrm{E}|\mathrm{A})=\frac{\mathrm{P}(\mathrm{E})\mathrm{P}(\mathrm{A}|\mathrm{E})}{\mathrm{P}(\mathrm{E})\mathrm{P}(\mathrm{A}|\mathrm{E})+\mathrm{P}(\mathrm{E})\mathrm{P}(\mathrm{A}|\mathrm{E})}=\frac{0.001\times0.9}{0.001\times0.9+0.999\times0.01}=\frac{90}{1089} lish $$

Thus, the probability that a person selected at random is actually having HIV given that he/she is tested $\mathrm{HIV+ive}$ is 0.083.



Example 19 In a factory which manufactures bolts, machines A, B and C manufacture respectively25%,35%and40%ofthebolts.Oftheiroutputs,5,4and2 percent a respectively defective bolts. A bolt is drawn at random from the product and is found to be defective. What is the probability that it is manufactured by the machine B?

Solution Let events $\mathrm{B}_{1},\mathrm{B}_{2},\mathrm{B}_{3}$ be the following :

$\mathrm{B_{t}}$ : the bolt is manufactured by machine A 

$ B_2$ : the bolt is manufactured by machine B 

$\mathrm{B}_{3}$ : the bolt is manufactured by machine C 

Clearly,$\overline{B}_{1},\overline{B}_{2},\overline{B}_{3}$ are mutually exclusive and exhaustive events and hence, they represent a partition of the sample space.



Let the event E be 'the bolt is defective'.

The event E occurs with $\mathrm{B_{t}}$ or with $\mathrm{B}_{2}$ or with $\mathrm{B}_{3}$ . Given that,

$$\mathrm{P}(\mathrm{B}_{1})=25\%=0.25,\ \mathrm{P}(\mathrm{B}_{2})=0.35\ \mathrm{and}\ \mathrm{P}(\mathrm{B}_{3})=0.40$$

Again $\mathrm{P}(\mathrm{E}|\mathrm{B}_1)=\mathrm{Probability}$ 'that the bolt drawn is defective given that it is manufactured by machine $A=5\%=0.05$ 



Similarly,$\mathrm{P}(\mathrm{E}|\mathrm{B}_2)=0.04,\ \mathrm{P}(\mathrm{E}|\mathrm{B}_3)=0.02$ 

Hence, by Bayes' Theorem, we have 

$$\mathrm{P}(\mathrm{B}_{2}|\mathrm{E})=\frac{\mathrm{P}(\mathrm{B}_{2})\mathrm{P}(\mathrm{E}|\mathrm{B}_{2})}{\mathrm{P}(\mathrm{B}_{1})\mathrm{P}(\mathrm{E}|\mathrm{B}_{1})+\mathrm{P}(\mathrm{B}_{2})\mathrm{P}(\mathrm{E}|\mathrm{B}_{2})+\mathrm{P}(\mathrm{B}_{3})\mathrm{P}(\mathrm{E}|\mathrm{B}_{3})}$$

Example 20 A doctor is to visit a patient.From the past experience,it is known that 司添are respectively b $\left[\frac{3}{10},\frac{1}{5},\frac{1}{10}\bmod\frac{2}{5}\right]$ (ci).The probabilitiesthat he will be late are $$ if he comes by train, bus and scooter respectively, but if he comes by other means of transport,thenhe will not belate.When he arrives,heis late.Whatis theprobability that he comes by train?



Solution LetE betheeventthatthedoctor visits the patient late and let $\mathrm{T}_{1},\mathrm{T}_{2},\mathrm{T}_{3},\mathrm{T}_{4}$ bethe evntthat thedoctorcomesbytain, bus cooter, andother mans of transort respectively.



Then 

$$\mathrm{P}(\mathrm{T}_{1})=\frac{3}{10},\mathrm{P}(\mathrm{T}_{2})=\frac{1}{5},\mathrm{P}(\mathrm{T}_{3})=\frac{1}{10}\text{and}\mathrm{P}(\mathrm{T}_{4})=\frac{2}{5}$$

$$\mathrm{P}(\mathrm{E}[\mathrm{T}_{1}])=\mathrm{Probability that the detector arrivaling late comes by train}=\frac{1}{4}$$

Similarly,$\mathrm{P}(\mathrm{E}|\mathrm{T}_2)=\frac{1}{3},\mathrm{P}(\mathrm{E}|\mathrm{T}_3)=\frac{1}{12}$ and $\mathrm{P}(\mathrm{E}|\mathrm{T}_4)=0$ , since he is not late if he comes by other means of transport.



Therefore, by Bayes' Theorem, we have 

$$\begin{aligned}\mathrm{P}(\mathrm{T}_{1}|\mathrm{E})&=\mathrm{Probability}+\mathrm{lat}-\mathrm{div}\text{driving late comes by train}\\&=\frac{\mathrm{P}(\mathrm{T}_{1})\mathrm{P}(\mathrm{E}|\mathrm{T}_{1})}{\mathrm{P}(\mathrm{T}_{1})\mathrm{P}(\mathrm{E}|\mathrm{T}_{1})+\mathrm{P}(\mathrm{T}_{2})\mathrm{P}(\mathrm{E}|\mathrm{T}_{2})+\mathrm{P}(\mathrm{T}_{3})\mathrm{P}(\mathrm{E}|\mathrm{T}_{3})+\mathrm{P}(\mathrm{T}_{4})\mathrm{P}(\mathrm{E}|\mathrm{T}_{4})}\\&=\frac{\frac{3}{10}\cdot\frac{1}{4}}{\frac{3}{10}\cdot\frac{1}{4}\cdot\frac{1}{5}\cdot\frac{1}{3}\cdot\frac{1}{10}\cdot\frac{1}{12}\cdot\frac{2}{5}\cdot0}=\frac{3}{40}\times\frac{120}{18}=\frac{1}{2}\end{aligned}$$

Hence, the required probability is $\frac{1}{2}$ 

Example 21 A man is known to speak truth 3 out of 4 times. He throws a die and reports that it is a six. Find the probability that it is actually a six.

Solution Let E be the event that the man reports that six occurs in the throwing of the die and let $\mathrm{S}_{\mathrm{r}}$ be the event that six occurs and $\mathrm{S}_{2}$ be the event that six does not occur.Then 

$$\mathrm{P}(\mathrm{S}_{1})=\mathrm{Probability that}six occurs=\frac{1}{6}$$

$$\mathrm{P}(\mathrm{S}_{2})=\mathrm{Probability}\quad\mathrm{that}\quad\mathrm{disc}\quad\mathrm{not}\quad\mathrm{occur}=\frac{5}{6}$$

P(E|S) = Probability that the man reports that six occurs when six has actually occurred on the die 

$$\mathrm{Probability}\;\mathrm{that}\;\mathrm{the}\;\mathrm{man}\;\mathrm{peaks}\;\mathrm{the}\;\mathrm{truth}=\frac{3}{4}$$

P(E|S2) = Probability that the man reports that six occurswhen six has not actually occurred on the die 

= Probability that the man does not speak the truth $1\quad\frac{3}{4}\quad\frac{1}{4}$ 

Thus, by Bayes' theorem, we get 

P(SE) = Probability that the report of the man that six has occurred is actually a six 



$$\begin{aligned}&=\frac{\mathrm{P}(\mathrm{S}_{1})\mathrm{P}(\mathrm{E}|\mathrm{S}_{1})}{\mathrm{P}(\mathrm{S}_{1})\mathrm{P}(\mathrm{E}|\mathrm{S}_{1})+\mathrm{P}(\mathrm{S}_{2})\mathrm{P}(\mathrm{E}|\mathrm{S}_{2})}\\&=\frac{\frac{1}{6}\quad\frac{3}{4}}{\frac{1}{6}\quad\frac{3}{4}\quad\frac{5}{6}\quad\frac{1}{4}}\quad\frac{1}{8}\quad\frac{24}{8}\quad\frac{3}{8}\end{aligned}$$

Hence, the required probability $\mathrm{is}\overbrace{\frac{3}{8}}^{3}.$ 

### EXERCISE 13.3

Anurn contains5redand5blackballs.Aball isdrawnatrandom,itscolour is noted aduovoeuwn are put in the urn and then a ball is drawn at random. What is the probability that the second ball is red?



2.A bag contains 4 red and 4 black balls, another bag contains 2 red and 6 black balls. One of the two bags is selected at random and a ball is drawn from the bag which is found to be red. Find the probability that the ball is drawn from the first bag.



3.Ofthe students in a college, it is known that 60% reside in hostel and 40% are day scholars (not residing in hostel). Previous year results report that 30% of all students who reside in hostel attain A grade and 20% of day scholars attain A grade in their annual examination. At the end of the year, one student is chosen at random from the college and he has an A grade, what is the probability that the student is a hostlier?



In answering a question on a multiple choice test, a student either knows the answer or guesses. Let $\frac{3}{4}$ be the probability that he knows the answer and $\frac{1}{4}$ be the probability that he guesses. Assuming that a student who guesses at the answer will be correct with probability $\frac{1}{4}$ . What is the probability that the student knows the answer given that he answered it correctly?

5.A laboratory blood test is 99% effective in detecting a certain disease when it is in fact, present. However, the test also yields a false positive result for 0.5% of thehealthy perontstd (i.i ahalthy prson issted, thn, with probability 0.005, the test will imply he has the disease). If 0.1 percent of the population actually has the disease, what is the probability that a person has the disease given that his test result is positive ?



6There are three coins. One is a two headed coin (having head on both faces),another is a biased coin that comes up heads 75% of the time and third is an unbiased coin. One of the three coins is chosen at random and tossed, it shows heads, what is the probability that it was the two headed coin?

7.An insurance company insured 2000 scooter drivers, 4000 car drivers and 6000truck drivers. The probability of an accidents are 0.01, 0.03 and 0.15 respectively.One of the insured persons meets with an accident. What is the probability that he is a scooter driver?



8.Afactory has two machines A and B. Past record shows that machine A produced 60% of the items of output and machine B produced 40% of the items. Further,2% of the items produced by machine A and 1% produced by machine B were defective. All the items are put into one stockpile and then one item is chosen at random from this and is found to be defective. What is the probability that it was produced by machine B?



9Two groups are competing for the position on the Board of directors of a corporation. The probabilities that the first and the second groups will win are  0.6 and 0.4 respectively. Further, if the first group wins, the probability of introducing a new product is 0.7 and the corresponding probability is 0.3 if the second group wins. Find the probability that the new product introduced was by the second group.



10.Suppose a girl throws a die. If she gets a 5 or 6, she tosses a coin three times and notes the number of heads. If she gets 1, 2, 3 or 4, she tosses a coin once and notes whether a head or tail is obtained. If she obtained exactly one head, what is the probability that she threw 1, 2, 3 or 4 with the die?

11.A manufacturer has three machine operators A, Band C. The first operator A produces 1% defective items, where as the other two operators B and C produce 5% and 7% defective items respectively. A is on the job for 50% of the time, B is on the job for 30% of the time and C is on the job for 20% of the time.A defective item is produced, what is the probability that it was produced by A?12.A card from a pack of 52 cards is lost. From the remaining cards of the pack,two cards are drawn and are found to be both diamonds. Find the probability of the lost card being a diamond.



13.Probability that A speaks truth is $\frac{4}{5}$ . Acoin is tossed.Areports that a hed appears. The probability that actually there was head is 

(A)$\frac{4}{5}$ (B)$\frac{1}{2}$ $\frac{1}{5}$ (D)$\frac{2}{5}$ 

14. IfA and B are two events such that $\mathrm{A}\subset\mathrm{B}$ and $\mathrm{P(B)}\neq0$ , then which of the following is correct?



(A)$\mathrm{P}(\mathrm{A}\mid\mathrm{B})\quad\frac{\mathrm{P}(\mathrm{B})}{\mathrm{P}(\mathrm{A})}$ (B)$\mathrm{P}(\mathrm{A}|\mathrm{B})<\mathrm{P}(\mathrm{A})$ (C)$\mathrm{P}(\mathrm{A}|\mathrm{B})\geq\mathrm{P}(\mathrm{A})$ (D) None of these 

### 13.6 Random Variables and its Probability Distributions 

We have already learnt about random experiments and formation of sample spaces. In most of these experiments, we were not only interested in the particular outcome that occurs but rather in some number associated with that outcomes as shown in following examples/experiments.

(i)Inssi two dice.



(iIni,dained 

()In heexpimtof takiut ourrticloneatetr) at andom from a lot of 20 articles in which 6 are defective, we want to know the number of defectives in the sample of four and not in the particular sequence of defective and nondefective articles.



In all of the above experiments, we have a rule which assigns to each outcome of the experiment a single real number.This single real number may vary with different outcomes of the experiment. Hence, it is a variable. Also its value depends upon the outcome of a random experiment and, hence, is called random variable. A random variable is usually denoted by X.



Ifyourecll eitiooffuctionou will lieatadomaab is really speaking a function whose domain is the set of outcomes (or sample space) of a random experiment. A random variable can take any real value, therefore, its co-domain is the set of real numbers. Hence, a random variable can be defined as follows :

DefinitionArandom variable is a real valued function whose domain is the sample space of a random experiment.



For example, let us consider the experiment of tossing a coin two times in succession.The sample space of the experiment is $\mathrm{S}=\{\mathrm{HH},\mathrm{HT},\mathrm{TH},\mathrm{TT}\}$ 

If X denotes the number of heads obtained, then X is a random variable and for each outcome, its value is as given below :

$$X(HH)=2,X(HT)=1,X(TH)=1,X(TT)=0.$$

More than one random variables can be defined on the same sample space. For example, letY denote the number of heads minus the number of tails for each outcome of the above sample space S.



Then 

$$\mathrm{Y}(\mathrm{HH})=2,\mathrm{Y}(\mathrm{HT})=0,\mathrm{Y}(\mathrm{TH})=0,\mathrm{Y}(\mathrm{TT})=-2.$$

Thus, X and Y are two different random variables defined on the same sample space S.



Example22 A person plays a game of tossing a coin thrice. For each head, he is givenRs2byheorairofthegameandorachta,hehatogiveR1.50tothe organiser. Let X denote the amount gained or lost by the person. Show that X is a random variable and exhibit it as a function on the sample space of the experiment.

Solution X is a number whose values are defined on the outcomes of a random experiment. Therefore, X is a random variable.



Now, sample space of the experiment is 

S = {HHH, HHT, HTH, THH, HTT, THT, TTH, TTT}

Then 

and 

$$\begin{aligned}&\mathrm{X}(\mathrm{HHH})=\mathrm{Rs}(2\times3)=\mathrm{Rs}6\\&\mathrm{X}(\mathrm{HHT})=\mathrm{X}(\mathrm{HTH})=\mathrm{X}(\mathrm{THH})=\mathrm{Rs}(2\times2-1\times1.50)=\mathrm{Rs}2.50\\&\mathrm{X}(\mathrm{HTT})=\mathrm{X}(\mathrm{THT})=(\mathrm{TTH})=\mathrm{Rs}(1\times2)-(2\times1.50)=-\mathrm{Re}1\\&\mathrm{X}(\mathrm{TTT})=-\mathrm{Rs}(3\times1.50)=-\mathrm{Rs}4.50\\ \end{aligned}$$

where, minus sign shows the loss to the player. Thus, for each element of the sample space, X takes a unique value, hence,X is a function on the sample space whose range is 



$$\{-1,2.50,-4.50,6\}$$

Example23Abagcontains2 white and1 redballs.Oneball is drawn at random and then put back in thebox after noting itscolour.The process is repeatedagain.If X denotes the number of red balls recorded in the two draws, describe X.

Solution Let the balls in the bag be denoted by $w_{1},w_{2},r$ . Then the sample space is 

Now, for 

$$\begin{aligned}\mathrm{S}&=\{w_{1}w_{1},w_{1}w_{2},w_{2}w_{2},w_{2}w_{1},w_{1}r,w_{2}r,r w_{1},r w_{2},r r\}\\\omega&\in\mathrm{S}\\\mathrm{X}(\omega)&=number of red balls\end{aligned} \mathrm{S}=\left\{w_{1}w_{1},w_{1}w_{2},w_{2}w_{2},w_{2}w_{1},w_{1}r,w_{2}r,r,w_{1},r,w_{2},r\right\}$$

Therefore 

$$\begin{aligned}\mathrm{X}(\{w_{1}w_{1}\})&=\mathrm{X}(\{w_{1}w_{2}\})=\mathrm{X}(\{w_{2}w_{2}\})=\mathrm{X}(\{w_{2}w_{1}\})=0\\\mathrm{X}(\{w_{1}r\})&=\mathrm{X}(\{w_{2}r\})=\mathrm{X}(\{r w_{1}\})=\mathrm{X}(\{r w_{2}\})=1\text{and}\mathrm{X}(\{r r\})=2\end{aligned}$$

Thus, X is a random variable which can take values 0, 1 or 2.

#### 13.6.1 Probability distribution of a random variable 

Let us look at the experiment of selecting one family out of ten families $f_{1},f_{2},\ldots,f_{10}$ in such amatachamiliqullylkltobelctd.theamilies $f_{1},f_{2},$ $\cdots,f_{10}$ have 3,4,3,2,5,4,3,6,4,5 members, respectively.



Let us select a family and note down the number of members in the family denoting X. Clearly, X is a random variable defined as below :

$$\begin{array}{l}\mathrm{X}(f_{1})=3,\mathrm{X}(f_{2})=4,\mathrm{X}(f_{3})=3,\mathrm{X}(f_{4})=2,\mathrm{X}(f_{5})=5,\\\mathrm{X}(f_{6})=4,\mathrm{X}(f_{7})=3,\mathrm{X}(f_{8})=6,\mathrm{X}(f_{9})=4,\mathrm{X}(f_{10})=5\end{array}$$

Thus, X can take any value 2,3,4,5 or 6 depending upon which family is selected 

Now, Xwilltakeelue2wmily $I f_{4}$ is selected. Xcan take the value 3 when any one of the families $f_{1},f_{3},f_{7}$ is selected.



Similarly,

$X=4$ ,when family $f_{2},f_{6}\mathrm{or}f_{9}$ is selected,

$X=5$ ,when family $f_{5}$ or $f_{10}$ is selected 

and 

$X=6$ , when family $f_{8}$ is selected.

Since l lity that family $f_{4}$ is selected is $\frac{1}{10}$ 



Thus,eeealue Also,ls $2\;is\;\frac{1}{10}$ ,$$ .We write is selected is i ste $$ 

$$\mathbb{P}(\{f_1,f_3,f_7\})=\frac{3}{10}$$

Thus, the probability that X can take the value $$ .

We write 

$$\mathrm{P}(\mathrm{X}=3)=\frac{3}{10}$$

Similarly, we obtain 

and 

$$\mathrm{P}(\mathrm{X}=4)=\mathrm{P}(\{f_{2},f_{6},f_{9}\})=\frac{3}{10}$$

Such a description giving the values of the random variable along with the corresponding probabilities is called the probability distribution of the random variable X.



In general, the probability distribution of a random ariable X is defined as follow:DefinitionTeprobaity ditbuioofadmaabeie mofumers where,

$$\begin{array}{ccc}X&:&x_{1}\quad x_{2}\quad\ldots\quad x_{n}\\ P(X)&:&p_{1}\quad p_{2}\quad\ldots\quad p_{n}\\&&\\p_{i}\quad0,&\underset{i1}{\overset{n}{\mathop{\quad}}}p_{i}=1,i=1,2,\ldots,n\\\end{array}$$

The real numbers $x_{1},x_{2},...,x_{n}$ are the possible values of the random variable X and $p_{i}\;(i=1,2,\ldots,n)$ is the probability of the random variable X taking the value $x_{i}i.e.$ 

$\mathrm{P}(\mathrm{X}=x_i)=p_i$ 



Note $\mathrm{If}x_{i}$ is one ofthe possiblevaluesof a random variable X, the statement $X=x_{i}$ iula X takes value $x_{i}$ is always nonzero, i.e.$\mathrm{P}(\mathrm{X}=x_{i})\neq0$ 



Also for all possible values of the random variable X, all elements of the sample space arev.Hcumoflbalitsioblitibution must be one.



Example 24 Two cards are drawn successively with replacement from a well-shuffled deck of 52 cards. Find the probability distribution of the number of aces.

Solution The number of aces is a random variable. Let it be denoted by X.Clearly, X can take the values 0, 1, or 2.



Now, since the draws are done with replacement, therefore, the two draws form independent experiments.



Therefore,

$$\begin{aligned}P(X=0)&=P(non-acc and non-acc)\\&=P(non-acc)\times P(non-acc)\\&=\frac{48}{52}\times\frac{48}{52}=\frac{144}{169}\end{aligned}$$

$$\begin{aligned}P(X=1)&=P(ace and non-acc or non-acc and acc)\\&=P(face and non-acc)+P(non-acc and acc)\\&=P(face)\cdot P(non-acc)+P(non-acc)\cdot P(acc)\\&=\frac{4}{52}\times\frac{48}{52}+\frac{48}{52}\times\frac{4}{52}=\frac{24}{169}\end{aligned}$$

and 

$$\begin{aligned}\mathrm{P}(\mathrm{X}=2)&=\mathrm{P}(\mathrm{acc}\text{and}\mathrm{acc})\\&=\frac{4}{52}\cdot\frac{4}{52}\cdot\frac{1}{169}\end{aligned}$$

T  l 


<div style="text-align: center;"><html><body><table border="1"><tr><td>X</td><td>0</td><td>1</td><td>2</td></tr><tr><td>P(X)</td><td>144 169</td><td>24 169</td><td>1 169</td></tr></table></body></html></div>


Example 5 Find the probability distribution of number of doublets in three throws of a pair of dice.



Solution Let X denote the number of doublets. Possible doublets are 

(1,1) , (2,2), (3,3), (4,4), (5,5), (6,6)

Clearly, X can take the value 0, 1, 2, or 3.

Probability of getting a doublet $\frac{6}{36}\quad\frac{1}{6}$ 

Probability of not getting a doublet $1\quad\frac{1}{6}\quad\frac{5}{6}$ 

Now 

$$\begin{aligned}\mathrm{P}(\mathrm{X}=0)&=\mathrm{P}\left(\mathrm{no}\text{doublet}\right)=\frac{5}{6}\quad\frac{5}{6}\quad\frac{5}{6}\quad\frac{125}{216}\\\mathrm{P}(\mathrm{X}=1)&=\mathrm{P}\left(\text{one}\text{doublet and two non-dubits}\right)\\&=\frac{1}{6}\quad\frac{5}{6}\quad\frac{5}{6}\quad\frac{5}{6}\quad\frac{1}{6}\quad\frac{5}{6}\quad\frac{5}{6}\quad\frac{5}{6}\quad\frac{1}{6}\\&=\frac{1}{6}\quad\frac{1}{6}\quad\frac{5^{2}}{6^{2}}\quad\frac{75}{216}\end{aligned} ublishe $$

$$ublishe \begin{aligned}\mathrm{P}(\mathrm{X}=2)&=\mathrm{P}\left(\mathrm{two}\text{doublets and one non-doublet}\right)\\&=\frac{1}{6}\quad\frac{1}{6}\quad\frac{5}{6}\quad\frac{1}{6}\quad\frac{5}{6}\quad\frac{1}{6}\quad\frac{5}{6}\quad\frac{1}{6}\quad\frac{1}{6}\quad\frac{1}{6}\quad3\quad\frac{1}{6^2}\quad\frac{5}{6}\quad\frac{15}{216}\end{aligned}$$

and 

$$\begin{aligned}\mathbb{P}(X=3)&=\mathbb{P}\left(three doublet\right)\\&=\frac{1}{6}\quad\frac{1}{6}\quad\frac{1}{6}\quad\frac{1}{216}\end{aligned}$$

Thus, the required probability distribution is 


<div style="text-align: center;"><html><body><table border="1"><tr><td>X</td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>$\mathbb{P}(\mathrm{X})$</td><td>125 216</td><td>75 216</td><td>15 216</td><td>1 216</td></tr></table></body></html></div>


Verification Sum of the probabilities 

$$\sum_{i=1}^{n}p_{i}=\frac{125}{216}\quad\frac{75}{216}\quad\frac{15}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{1}{216}\quad\frac{21}{216}\quad\frac{21}{216}\quad\quad\frac{1}{216}\quad\frac{21}{216}\quad\quad\frac{1}{216}\quad\frac{21}{216}\quad\quad\frac{1}{216}\quad\frac{21}{216}\quad\quad\frac{21}{216}\quad\quad\frac{21}{216}\quad\quad\frac{21}{216}\quad\quad\frac{21}{216}\quad\quad\frac{21}{216}\quad\quad\frac{21}\quad\frac{21}{216}\quad\quad\frac{21}{216}\quad\quad\frac{21}\quad\frac{21}{216}\quad\quad\frac{21}\quad\frac{21}{216}\quad\quad\quad\frac{21}{21}\quad\quad\frac{21}\quad\quad\frac{21}{21}\quad\quad\frac{21}\quad\quad\frac{21}{21}\quad\quad\quad\frac{21}{21}\quad\quad\quad\frac{21}\quad\quad\frac{21}{21}\quad\quad\quad\frac{21}\quad\quad\frac{21}{21}\quad\quad\quad\frac{21}\quad\quad\quad\frac{21}{21}\quad\quad\quad\quad\frac{21}\quad\quad\frac{21}{21}\quad\quad\quad\quad\quad\frac{21}\quad\quad\frac{21}\quad\quad\quad\frac{21}{21}\quad\quad\quad\quad\quad\quad\frac{21}\quad\quad\quad\frac{2}{21}\quad\quad\quad\quad\frac{21}\quad\quad\quad\quad\frac{21}\quad\quad\quad\quad\frac{2}\quad\quad\quad\frac{2}\quad\quad\frac{2}\quad\quad\quad\frac{2}{21}\quad\quad\quad\quad\quad\quad\quad\frac{2}\quad\quad\quad\quad\quad\frac{2}\quad\quad\quad\frac{2}\quad\quad\quad\quad\quad\frac{2}\quad\quad\quad\quad\quad\frac{2}\quad\quad\quad\quad\quad\quad\frac{2}\quad\quad\quad\quad\quad\quad\quad\quad\frac{2}\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad $$

Example 26 Let X denote the number of hours you study during a randomly selected school day. The probability that X can take the values x, has the following form, where k is some unknown constant.



$$\mathrm{P}(\mathrm{X}=x)=\left\{\begin{aligned}&0.1,\text{if}x=0\\&kx,\text{if}x=1\text{or}2\\&k(5-x),\text{if}x=3\text{or}4\\&0,\text{otherwise}\end{aligned}\right.$$

(a) Find the value of k.

(b)What isthe probability that youstudy at east twohours?Exactlytwohours? At most two hours?



Solution The probability distribution of X is 


<div style="text-align: center;"><html><body><table border="1"><tr><td>X</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>P(X)</td><td>0.1</td><td>$k$</td><td>2k</td><td>2k</td><td>k</td></tr></table></body></html></div>


(a) We know that 

$$\sum_{i=1}^{n}p_{i}=1$$

Therefore 

$$0.1+k+2k+2k+k=1$$

i.e.

$$\begin{aligned}&\mathrm{P}k=0.15\\&=\mathrm{P}(\mathrm{X}\geq2)\\&=\mathrm{P}(\mathrm{X}=2)+\mathrm{P}\left(\mathrm{X}=3\right)+\mathrm{P}\left(\mathrm{X}=4\right)\\&=2k+2k+k=5k=5\times0.15=0.75\\&=\mathrm{P}(\mathrm{X}=2)\\&=2k=2\times0.15=0.3\\&=\mathrm{P}(\mathrm{X}\leq2)\\&=\mathrm{P}\left(\mathrm{X}=0\right)+\mathrm{P}(\mathrm{X}=1)+\mathrm{P}(\mathrm{X}=2)\\&=0.1+k+2k=0.1+3k=0.1+3\times0.15\\&=0.55\\ \end{aligned}$$

(b) P(you study at least two hours)$\begin{aligned}&\mathrm{P}k=0.15\\&=\mathrm{P}(\mathrm{X}\geq2)\\&=\mathrm{P}(\mathrm{X}=2)+\mathrm{P}\left(\mathrm{X}=3\right)+\mathrm{P}\left(\mathrm{X}=4\right)\\&=2k+2k+k=5k=5\times0.15=0.75\\&=\mathrm{P}(\mathrm{X}=2)\\&=2k=2\times0.15=0.3\\&=\mathrm{P}(\mathrm{X}\leq2)\\&=\mathrm{P}\left(\mathrm{X}=0\right)+\mathrm{P}(\mathrm{X}=1)+\mathrm{P}(\mathrm{X}=2)\\&=0.1+k+2k=0.1+3k=0.1+3\times0.15\\&=0.55\\ \end{aligned}$ 

P(you study exactly two hours)

P(you study at most two hours)

#### 13.6.2 Mean of a random variable 

In many problems, it is desirable to describe some feature of the random variable by means of a single number that can be computed from its probability distribution. Few such numbers are mean, median and mode. In this section, we shall discuss mean only.Mean is a measure of location or central tendency in the sense that it roughly locates a middle or average value of the random variable.



Definition 6 Let X be a random variable whose possible values $x_{1},x_{2},x_{3},...,x_{n}$ occur with probabilities $p_{1},p_{2},p_{3},...,p_{n}$ , respectively. The mean of X, denoted by , is the number $\sum_{i=1}^{n}x_{i}p_{i}$ i.e. the mean of X is the weighted average of the possible values of X,

each value being weighted by its probability with which it occurs.

The mean of a random variable X is also called the expectation of X, denoted by E(X).



Thus,

$$\mathrm{E}(\mathrm{X})=\mu=\underset{i1}{\overset{n}{\mathrm{E}}}x_{i}p_{i}=x_{1}p_{1}+x_{2}p_{2}+\ldots+x_{n}p_{n}.$$

In other words, the mean or expectation of a random variable X is the sum of the products ofall possiblevaluesofXbythirrespective probabilities.

Example 27 Let a pair of dice be thrown and the random variable X be the sum of the numbers that appear on the two dice. Find the mean or expectation of X.

Solution The sample space of the experiment consists of 36lementary events in the form of ordered pairs HoiOlucrcupuhs $(x_{i},y_{i})$ , where $x_{i}=1,2,3,4,5,6and y_{i}=1,2,3,4,5,6$ .Theneuou values 2,3,4,5,6,7,8,9,10,11or12.



Now 

$$not \begin{aligned}&P(X=2)=P(\{(1,1),(2,1),(3,2),(4,1)\})\quad\frac{4}{36}\\ &P(X=2)=P(\{(1,1)\})\quad\frac{1}{36}\\ &P(X=3)=P(\{(1,2),(2,1)\})\quad\frac{2}{36}\\ &P(X=4)=P(\{(1,3),(2,2),(3,1)\})\quad\frac{3}{36}\\ &P(X=5)=P(\{(1,4),(2,3),(3,2),(4,1)\})\quad\frac{4}{36}\\ &P(X=6)=P(\{(1,5),(2,4),(3,3),(4,2),(5,1)\})\quad\frac{5}{36}\\ &P(X=7)=P(\{(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)\})\quad\frac{6}{36}\\ &P(X=8)=P(\{(2,6),(3,5),(4,4),(5,3),(6,2)\})\quad\frac{5}{36}\\ \end{aligned}

$$

$$\mathrm{P}(\mathrm{X}=9)=\mathrm{P}(\{(3,6),(4,5),(5,4),(6,3)\})\quad\frac{4}{36}$$

The probability distribution of X is 


<div style="text-align: center;"><html><body><table border="1"><tr><td>Xor $x_{i}$</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td rowspan="2">P(X) or pi</td><td>1 36</td><td>2 36</td><td>3 36</td><td>4 36</td><td>5 36</td><td>6 36</td><td>5 36</td><td>4 36</td><td>3 36</td><td>2 36</td><td>1 36</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table></body></html></div>


Therefore,

$$\begin{aligned}\mu=\mathrm{E}(\mathrm{X})=\sum_{i=1}^{n}x_i p_i=2\times\frac{1}{36}+3\times\frac{2}{36}+4\times\frac{3}{36}+5\times\frac{4}{36}\\6\quad\frac{5}{36}\quad7\quad\frac{6}{36}\quad8\quad\frac{5}{36}\quad9\quad\frac{4}{36}\quad10\quad\frac{3}{36}\quad11\quad\frac{2}{36}\quad12\quad\frac{1}{36}\\=\frac{2\quad6\quad12\quad20\quad30\quad42\quad40\quad36\quad30\quad22\quad12}{36}=7\end{aligned}$$

Thus, the mean of the sum of the numbers that appear on throwing two fair dice is 7.

#### 13.6.3 Variance of a random variable 

The mean of a random variable does not give us information about the variability in the values of the random variable. In fact, if the variance is small, then the values of the random variable are close to the mean. Also random variables with different probability distributions can have equal means, as shown in the following distributions of X and Y.


<div style="text-align: center;"><html><body><table border="1"><tr><td>X</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>P(X)</td><td>1 -∞</td><td>2 8</td><td>3 8</td><td>2 8</td></tr></table></body></html></div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>Y</td><td>-1</td><td>0</td><td>4</td><td>5</td><td>6</td></tr><tr><td>$\mathrm{P(Y)}$</td><td>1 -8</td><td>2 8</td><td>3 8</td><td>1 8</td><td>1 8</td></tr></table></body></html></div>


Clearly 

$$\mathrm{E}(\mathrm{X})=1\times\frac{1}{8}+2\times\frac{2}{8}+3\times\frac{3}{8}+4\times\frac{2}{8}=\frac{22}{8}=2.75$$

and 

$$\mathrm{E}(\mathrm{Y})=-1\times\frac{1}{8}+0\times\frac{2}{8}+4\times\frac{3}{8}+5\times\frac{1}{8}=6\times\frac{1}{8}=\frac{22}{8}=2.75$$

The variables X and Y are different, however their means are same. It is also easily observable from the diagramatic representation of these distributions (Fig 13.5).

<div style="text-align: center;"><img src="imgs/img_in_chart_box_87_530_918_856.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">Fig 13.5</div>


To distinguish X from Y, we require a measure of the extent to which the values of the random variables spread out. In Statistics, we have studied that the variance is a measure of the spread or scatter in data. Likewise, the variability or spread in the values of a random variable may be measured by variance.



Definition 7 Let X be a random variable whose possible values $x_{1},x_{2},...,x_{n}$ occur with probabilities $p(x_{1}),p(x_{2}),\ldots,p(x_{n})$ respectively.



Let $\mu=\mathrm{E}\left(\mathrm{X}\right)$ be the mean of X. The variance of X, denoted by Var (X) or $_{x}^{2}$ is defined as 



$$\sigma_{x}^{2}=\mathrm{Var}(X)=\sum_{i=1}^{n}(x_{i}-\mu)^{2}p(x_{i})$$

or equivalently 

$${\bf\Pi}_{x}^{2}=\mathrm{E}(\mathrm{X}-\mu)^{2}$$

The non-negative number 

$$\sigma_{x}=\sqrt{\mathrm{Var}(X)}=\sqrt{\sum_{i=1}^{n}(x_{i}-\mu)^{2}p(x_{i})}$$

is called the standard deviation of the random variable X.

Another formula to find the variance of a random variable. We know that,

or 

or 

$${\begin{aligned}{\mathrm{Var}\left(\mathrm{X}\right)}&{{}=\sum_{i=1}^{n}(x_{i}-\mu)^{2}\;p(x_{i})}\\ &{{}=\sum_{i=1}^{n}(x_{i}^{2}\quad\mu^{2}\quad2\mu x_{i})\;p(x_{i})}\\ &{{}=\sum_{i=1}^{n}x_{i}^{2}\;p(x_{i})+\sum_{i=1}^{n}\mu^{2}\;p(x_{i})-\sum_{i=1}^{n}2\mu x_{i}p(x_{i})}\\ &{{}=\sum_{i=1}^{n}x_{i}^{2}\;p(x_{i})+\mu^{2}\;\sum_{i=1}^{n}p(x_{i})-2\mu\sum_{i=1}^{n}x_{i}p(x_{i})}\\ &{{}=\sum_{i=1}^{n}x_{i}^{2}\;p(x_{i})+\mu^{2}-2\mu^{2}\left[\mathrm{since}\sum_{i=1}^{n}p\;(x_{i}){=}1\mathrm{and}\mu{=}\sum_{i=1}^{n}x_{i}p(x_{i})\right]}\\ &{{}=\sum_{i=1}^{n}x_{i}^{2}\;p(x_{i}){-}\mu^{2}}\\ &{{}\mathrm{Var}\left(\mathrm{X}\right)=\sum_{i=1}^{n}x_{i}^{2}\;p(x_{i}){-}\left(\sum_{i=1}^{n}x_{i}\;p(x_{i})\right)^{2}}\\ &{{}\mathrm{Var}\left(\mathrm{X}\right)=\mathrm{E}(\mathrm{X}^{2})-[\mathrm{E}(\mathrm{X})]^{2},\mathrm{where}\;\mathrm{E}(\mathrm{X}^{2}){=}\sum_{i=1}^{n}x_{i}^{2}\;p(x_{i})}\end{aligned}}$$

Example 28 Find the variance of the number obtained on a throw of an unbiased die.

Solution The sample space of the experiment is $\mathrm{S}=\{1,2,3,4,5,6\}$ 

Let X denote the number obtained on the throw. Then X is a random variable which can take values 1, 2, 3, 4, 5, or 6.



Also 

$$\mathrm{P}(1)=\mathrm{P}(2)=\mathrm{P}(3)=\mathrm{P}(4)=\mathrm{P}(5)=\mathrm{P}(6)=\frac{1}{6}$$

Therefore, the Probability distribution of X is 


<div style="text-align: center;"><html><body><table border="1"><tr><td>X</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>P(X)</td><td>1 6</td><td>\1 *[Formula could not be recovered from OCR — see source PDF]* 6</td><td>1 -6</td></tr></table></body></html></div>


Now 

Also 

Thus,

$$\mathrm{E}(\mathrm{X})=\frac{\mathrm{E}_{x_{i}}}{\mathrm{E}_{x_{i}}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{E}_{x_{i}}\mathrm{P}(x_{i})\mathrm{P}(x_{i})\mathrm{E}_{i}\mathrm{P}(x_{i})\mathrm{E}_{P}(x_{i})\mathrm{P}(x_{i})\mathrm{E}_{i}\mathrm{P}(x_{i})\mathrm{P}_{P}(x_{i})\mathrm{P}(x_{i})\mathrm{P}(x_{i})\mathrm{E}_{P}(x_{i})\mathrm{P}(x_{i})\mathrm{P}_{P}(x_{i})\mathrm{P}(x_{i})\mathrm{P}(x_{i})\mathrm{P}_{P}(x_{i})\mathrm{P}(x_{i})\mathrm{P}\mathrm{P}(x_{P}(x_{i})\mathrm{P}_{P}(x_{i})\mathrm{P}(x_{i})\mathrm{P})\mathrm{P}_{P}(x_{P}(x_{i})\mathrm{P}(x_{i})\mathrm{P}_{P}(x_{i})\mathrm{P}\mathrm{P}(x_{P})\mathrm{P}_{P}(x_{P}(x_{i})\mathrm{P}(x_{P})\mathrm{P}_{P}(x_{i})\mathrm{P}_{P}(x_{i})\mathrm{P})\mathrm{P}_{P}(x_{P}(x_{i})\mathrm{P}\mathrm{P}_{P}(x_{P})(x_{P})\mathrm{P}_{P}(x_{P})\mathrm{P}_{P}(x_{P})\mathrm{P}(x_{PP}(x_{i})\mathrm{P})\mathrm{P}_{P}(x_{P})\mathrm{P}_{PP}(x_{P})\mathrm{P}_{P}(x_{P})\mathrm{P}_{P}(x_{PP}(x_{P})\mathrm{P}(x_{P})\mathrm{P}_{PP}(x_{P})\mathrm{P}_{P}(x_{P})\mathrm{P}_{PP}(x_{P})_{P}(x_{P})\mathrm{P}_{PP}\mathrm{P}_{P}(x_{P})_{P}(x_{PP})_{P}\mathrm{P}_{P}(x_{PP}(x_{P})\mathrm{P}\mathrm{P}_{PPP}(x_{PP})(x_{P})\mathrm{P}_{PP}(x_{PP}\mathrm{P}_{P}\mathrm{P}_{P}(x_{P})\mathrm{P}_{P}(x_{PPP}\mathrm{}))))))$$

Example 29 Two cards are drawn simultaneously (or successively without replacement)from a well shuffled pack of 52 cards. Find the mean, variance and standard deviation of the number of kings.



Solution Let X denote the numberof kings in a draw of two cards. X is a random variable which can assume the values 0, 1 or 2.



Now 

$$\mathrm{P}(\mathrm{X}=0)=\mathrm{P}(\mathrm{no}\text{king})\quad\frac{^{48}C_{2}}{^{52}C_{2}}\quad\frac{\overline{2!(48\quad2)!}}{\overline{52!}}\quad\frac{48\quad47}{52\quad51}\quad\frac{188}{221}not 
$$

$$not \mathrm{P}(\mathrm{X}=1)=\mathrm{P}(\text{one king and one non-king})=\frac{4\mathrm{C}_{1}\mathrm{~}^{48}\mathrm{C}_{1}}{\mathrm{~}^{52}\mathrm{~}^{48}\mathrm{C}_{2}}=\frac{4\times48\times2}{52\times51}=\frac{32}{221}$$

and 

$$\mathrm{P}(\mathrm{X}=2)=\mathrm{P}(\mathrm{two}\mathrm{kg})=\frac{^{4}C_{2}}{^{52}C_{2}}=\frac{4\times3}{52\times51}=\frac{1}{221}$$

Thus, the probability distribution of X is 


<div style="text-align: center;"><html><body><table border="1"><tr><td>X</td><td>0</td><td>1</td><td>2</td></tr><tr><td rowspan="2">P(X)</td><td>188 221</td><td>32 221</td><td>1 221</td></tr><tr><td></td><td></td><td></td></tr></table></body></html></div>


Now 

(cid:12)

,

efore 

$$\begin{aligned}Mean of\quad\mathrm{X}&=\mathrm{E}(\mathrm{X})=\underset{i}{\overset{n}{\mathop{\mathrm{E}}}}x_{i}p(x_{i})\\&=0\times\frac{188}{221}+1\times\frac{32}{221}+2\times\frac{1}{221}=\frac{34}{221}\end{aligned} olishe $$

$$olishe \mathrm{E}(\mathrm{X}^{2})=\sum_{i=1}^{n}x_{i}^{2}p(x_{i})\quad 为 \quad0^{2}\times\frac{188}{221}+1^{2}\times\frac{32}{221}+2^{2}\times\frac{1}{221}=\frac{36}{221}$$

$$\begin{aligned}\mathrm{Var}(\mathrm{X})&=\mathrm{E}(\mathrm{X}^2)-[\mathrm{E}(\mathrm{X})]^2\\&=\frac{36}{221}-\left(\frac{34}{221}\right)^2=\frac{6800}{(221)^2}\end{aligned}$$

$$\sigma_{x}=\sqrt{\mathrm{Var}(X)}=\frac{\sqrt{6800}}{221}=0.37$$

### EXERCISE 13.4

1.State whichoftheollowing arenot theprobabilitydistributionsofa random variable. Give reasons for your answer.



(i)


<div style="text-align: center;"><html><body><table border="1"><tr><td>X</td><td>0</td><td>1</td><td>2</td></tr><tr><td>P(X)</td><td>0.4</td><td>0.4</td><td>0.2</td></tr></table></body></html></div>


(ii)


<div style="text-align: center;"><html><body><table border="1"><tr><td>X</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>P(X)</td><td>0.1</td><td>0.5</td><td>0.2</td><td>|−0.1</td><td>0.3</td></tr></table></body></html></div>


(i)


<div style="text-align: center;"><html><body><table border="1"><tr><td>Y</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P(Y)</td><td>0.6</td><td>0.1</td><td>0.2</td></tr></table></body></html></div>


(iv)


<div style="text-align: center;"><html><body><table border="1"><tr><td>Z</td><td>3</td><td>2</td><td>1</td><td>0</td><td>-1</td></tr><tr><td>[P(Z)</td><td>0.3</td><td>0.2</td><td>0.4</td><td>0.1</td><td>0.05</td></tr></table></body></html></div>


2.An urncontains5 red and2 blackballs.Twoballsare randomly drawn. Let X represent the number of black balls. What are the possible values of X? Is X a random variable ?



3. Let X represent the difference between the number of heads and the number of tails obtained when a coin is tossed 6 times. What are possible values of X?

4. Find the probability distribution of 

(i) number of heads in two tosses of a coin.

(ii) number of tails in the simultaneous tosses of three coins.

(i) number of heads in four tosses of a coin.

5.Findthe probaility ditributionoftheumberofsucssintwotossof ,where a success is defined as 



(i)number greater than 4

(ii) six appears on at least one die 

From a lot of 30 bulbs which include 6 defectives, a sample of 4 bulbs is drawn at random with replacement. Find the probability distribution of the number of defective bulbs.



7.Ainibadehaitim liklytccuraIcinis tossedtwie,ind the probability ditributionofumber ails.

8.Arandom variableXhas the following probability distribution:


<div style="text-align: center;"><html><body><table border="1"><tr><td>X</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>P(X)</td><td>0</td><td>k</td><td>2k</td><td>2k</td><td>3k</td><td>$k^{2}$</td><td>2k²</td><td>$7k^{2}+k$</td></tr></table></body></html></div>


Determine 

(i)k 

(i $\mathrm{P}(\mathrm{X}<3)$ 

(ii)$\mathbb{P}(\mathbb{X}\geq6)$ (iv)$\mathrm{P}(0<\mathrm{X}<3)$ 

9.The random ariable Xhas a probability ditibutionP(X) ofthe following form,where k is some number :

$$\mathrm{P}(\mathrm{X})=\left\{\begin{aligned}&k,\ if\ x=0\\&2k,\ if\ x=1\\&3k,\ if\ x=2\\&0,\ otherwise\end{aligned}\right.$$

(a) Determine the value of k.

(b) Find $\mathrm{P}(\mathrm{X}<2),\mathrm{P}(\mathrm{X}\leq2),\mathrm{P}(\mathrm{X}\geq2)$ 

10.Find the mean number of heads in three tosses of a fair coin.

11.Two dice are thrown simultaneously.If X denotes the number of sixes, find the expectation of X.



12. Two numbers are selected at random (without replacement) from the first six positive integers. Let X denote the larger of the two numbers obtained. Find E(X).



13. Let X denote the sum of the numbers obtained when two fair dice are rolled.Find the variance and standard deviation of X.



14.Aclass has15 students whose ages are14,17,15,14,21,17,19,20,16,18,20,17,16, 19 and 20 years. One student is selected in such a manner that each has the same chance of being chosen and the age X of the selected student is recorded. What is the probability distribution of the random variable X? Find mean, variance and standard deviation of X.



15.In a meeting, 70% of the members favour and 30% oppose a certain proposal.A member is selected at random and we take $X=0$ if he opposed, and $X=1$ if he is in favour. Find E(X) and Var (X).



Choose the correct answer in each of the following:

16. The mean of the numbers obtained on throwing a die having written 1 on three faces, 2 on two faces and 5 on one face is 

(A)1(B)2(C)5(D)$\left[\frac{8}{3}\right.]$ 

17. Suppose that two cards are drawn at random from a deck of cards. Let X be the number of aces obtained. Then the value of E(X) is 

(A)$\frac{37}{221}$ (B)$\frac{5}{13}$ (C)$\frac{1}{13}$ (D)$\frac{2}{13}$ 

### 13.7 Bernoulli Trials and Binomial Distribution 

#### 13.7.1 Bernoulli trials 

Many experiments are dichotomous in nature. For example, a tossed coin shows a 'head'or'taila manufactured item canbe'defective' ornon-defective,the response to a question might be'yes'orno,an egg hashatched or'nothatched',the decision is 'yes' or 'no' etc. In such cases, it is customary to call one of the outcomes a'success'andthe other'notsuccessorfailure'.For example, in tossing acoin,ifthe occurrence of the head is considered a success, then occurrence of tail is a failure.

Each time we toss a coin or roll adie or perform any other experiment, we call it a trial.If aoini td,a,timtheumerofrialsis4achhavingxactlytw outcomes,namely,successor failure.Theoutcome of any trial is independent of the outcome of anyothertrial.Inachofsuchtrials,the probabilityof success or failure remains constant. Such independent trials which have only two outcomes usually referred as success'or failure'are called Bernoulli trials.

Definition 8 Trials of a random experiment are called Bernoulli trials, if they satisfy the following conditions :

(i)There shouldbefiitnumberofals.

(ii))The trials should be independent.

(ii)Each trial has exactly two outcomes : success or failure.

(iv) The probability of success remains the same in each trial.

For example, throwing a die 50 times is a case of 50 Bernoulli trials, in which each trial results in success (say an even number) or failure (an odd number) and the probability of success (p) is same for all 50 throws.Obviously, the successive throws of the die are independent experiments. If the die is fair and have six numbers 1 to 6written on six faces, then $p=\frac{1}{2}and q=1-p=\frac{1}{2}=probability$ 'of failure.

Examplexlilyomuii7dnac balls.llollellach draw the ball drawn is 



(i) replaced (i) not replaced in the urn.

## Solution 

(i)The number of trials is finite. When the drawing is done with replacement, the probability of success (say, red ball) is $p=\frac{7}{16}$ which is same for all six trials (draws). Hence, the drawing of balls with replacements are Bernoulli trials.

(i) When the drawing is done withoutreplacement,theprobabilityof success (i..,ll)$\frac{7}{16}$ , in 2nd trial is $\frac{6}{15}$ ifthe first ball drawn is red or $\frac{7}{15}$ if the first ball drawn is black and so on.Clearly,the probability of success is not same for all trials, hence the trials are not Bernoulli trials.

#### 13.7.2 Binomial distribution 

Consider the experiment of tossing a coin in which each trial results in success (say,heads) or failure (tails).LetS andF denote respectively success andfailure in each trial. Suppose we are interested in finding the ways in which wehave one success in six trials.



Clearly, six different cases are there as listed below:

SFFFFF,FSFFFF,FFSFFF,FFFSFF,FFFFSF,FFFFFS.

Similarly, two successes and four failures can have $\frac{6!}{4!\ 2!}$ combinations. It will be 

lengthy obto listallosewys.Treorealculionofprobilitiof,1,2,…,n number of successes may be lengthy and time consuming. To avoid the lengthy calculations and listing of all the possible cases, for the probabilitiesof number of successes in n-Bernoullitrials,aformulais derived.Forthis purpose, let us take the experiment made up of three Bernoulli trials with probabilities p and $q=1-p$ for success and failure respectively in each trial. The sample space of the experiment is the set 



$$\mathrm{S}=\{\mathrm{SSS},\mathrm{SSF},\mathrm{SFS},\mathrm{FSS},\mathrm{SFF},\mathrm{FSF},\mathrm{FFS},\mathrm{FFF}\}$$

The number of successes is a random variable X and can take values 0, 1, 2, or 3.The probability distribution of the number of successes is as below :

$$\begin{aligned}P(X=0)&=P(no success)\\&=P(\{FFF\})=P(F)P(F)P(F)\\&=q.q-q^3since the trials are independent\\ P(X=1)&=P(one successes)\\&=P(\{SFF,FSF,FFS\})\\&=P(\{SFF\})+P(\{SFF\})+P(\{FFS\})\\&=P(S)P(F)P(F)+P(F)P(S)P(F)+P(F)P(F)P(S)\\&=p.q.q+q.p.q.q.p=3pq^2\\ P(X=2)&=P(two successes)\\&=P(\{SSF,FSF,FSS\})\\&=P(\{SSF\})+P(\{SFS\})+P(\{FSS\})\end{aligned}$$

and 

$$\begin{aligned}&=\mathrm{P}(\mathrm{S})\mathrm{P}(\mathrm{S})\mathrm{P}(\mathrm{F})+\mathrm{P}(\mathrm{S})\mathrm{P}(\mathrm{F})\mathrm{P}(\mathrm{S})+\mathrm{P}(\mathrm{F})\mathrm{P}(\mathrm{S})\mathrm{P}(\mathrm{S})\\&=p.p.q.+p.q.p+q.p.p=3p^{2}q\\\mathrm{P}(\mathrm{X}=3)&=\mathrm{P}(\text{three success})=\mathrm{P}(\{\mathrm{SSS}\})\\&=\mathrm{P}(\mathrm{S}).\mathrm{P}(\mathrm{S}).\mathrm{P}(\mathrm{S})=p^{3}\end{aligned}$$

Thus, the probability distribution of X is 


<div style="text-align: center;"><html><body><table border="1"><tr><td>X</td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>$\mathbb{P}(\mathrm{X})$</td><td>$q^{3}$</td><td>$3q^{2}p$</td><td>$3q p^{2}$</td><td>$p^{3}$</td></tr></table></body></html></div>


Also, the binominal expansion of $(q+p)^{3}$ is 

$$q^{3}+3q^{2}p+3qp^{2}+p^{3}$$

Note that the probabilities of 0, 1,2 or 3 successes are respectively the 1st,2nd,3rd and 4th term in the expansion of $(q+p)^{3}$ 



Also, since $q+p=1$ , it follows that the sum of these probabilities, as expected, is 1.

Thus, we yludei xpimto-ollileaiities of $0,1,2,...,n$ successes can be obtained as lst,$2nd,\ldots,(n+1)^{\mathrm{H}}$ terms in the expansion of $(q+p)^n$ Toproveti ati (l, t uind e probiit of -uc in an experiment of n-Bernoulli trials.



Clearly, in case of x successes (S), there will be $(n-x)$ failures (F).

Now, x successes (S) and $(n-x)$ failures (F) can be obtained in $\frac{n!}{x!(n\setminus x)!}$ ways.

In each of these ways, the probability of x successes and $(n-x)$ failures is 

$$\begin{aligned}&\mathrm{P}(x\text{successes}).\mathrm{P}(n-x)\text{failures is}\\ &=\underbrace{\mathrm{P}(\mathrm{S}).\mathrm{P}(\mathrm{S})...\mathrm{P}(\mathrm{S})}_{x\text{times}}\quad\underbrace{\mathrm{P}(\mathrm{F}).\mathrm{P}(\mathrm{F})...\mathrm{P}(\mathrm{F})}_{(n-x)\text{times}}=p^{x}q^{n-x}\\ \end{aligned}$$

Thus, the probability of x successes in n-Bernoulli trials is $\frac{n!}{x!(n-x)!}p^{x}q^{n-x}$ or $^{n}\mathrm{C}_{x}p^{x}q^{n-x}$ 



Thus 

$$\mathrm{P}(x\mathrm{success})={}^{n}\mathrm{C}_{x}p^{x}q^{n-x},\quad x=0,1,2,\ldots,n.(q=1-p)$$

Clearly, P(x successes), i.e.$^{n}\mathrm{C}_{x}p^{x}q^{n-x}$ is the $(x+1)^{th}$ term in the binomial expansion of $(q+p)^n$ 



Thus,he ixti of n Bernoulli trials may be obtained by the binomial expansion of $(q+p)^{n}$ '. Hence, this  distribution of number of successes X can be written as 


<div style="text-align: center;"><html><body><table border="1"><tr><td>X</td><td>0</td><td>1</td><td>2</td><td>…</td><td>x</td><td>.</td><td>n</td></tr><tr><td>P(X)</td><td>${}^{n}\mathrm{C}_{0}q^{n}$</td><td>nC, 1 qn−1p1</td><td>q"-²p²</td><td></td><td>$^{n}\mathrm{C}_{x}q^{_{n-x}}p^{_{x}}$</td><td></td><td>${}^{n}\mathrm{C}_{{}_{n}}p^{n}$</td></tr></table></body></html></div>


The above probability distribution is known as binomial distribution with parameters n and p, because for given values of n and p, we can find the complete probability distribution.



The probability of x successes $\mathrm{P}(\mathrm{X}=x)$ is also denoted by $\mathbb{P}(x)$ and is given by 

$$\mathrm{P}(x)={}^{n}\mathrm{C}_{x}q^{n-x}p^{x},\quad x=0,1,\ldots,n.(q=1-p)$$

This $\mathbb{P}\left(x\right)$ is called the probability function of the binomial distribution.

A binomial distribution with n-Bernoulli trials and probability of success in each trial as p, is denoted by $\mathrm{B}\left(n,p\right)$ 



Let us now take up some examples.

Example 31 If a fair coin is tossed 10 times, find the probability of 

(i) exactly six heads 

(ii) at least six heads 

(i) at most six heads 

Solution The repeated tosses of a coin are Bernoulli trials. Let X denote the number op of heads in an experiment of 10 trials.



Clearly, X has the binomial distribution with $n=10and p=\frac{1}{2}$ 

Therefore 

$$\mathrm{P}(\mathrm{X}=x)=\mathrm{^{n}C_{x}}q^{n-x}p^{x},x=0,1,2,\ldots,n $$

Here 

$$n=10,\ p\ \frac{1}{2}\ ,\ q=1-p=\frac{1}{2}$$

Therefore 

$$\mathrm{P}(\mathrm{X}=x)=\mathrm{P}\left(\frac{1}{2}\right)^{10-x}\left(\frac{1}{2}\right)^{x}=\mathrm{P}\left(\frac{1}{2}\right)^{10}$$

Now 

(i)

$$\mathrm{P}(\mathrm{X}=6)=^{10}\mathrm{C}_{6}\left(\frac{1}{2}\right)^{10}=\frac{10!}{6!\times4!}\frac{1}{2^{10}}=\frac{105}{512}$$



$\mathrm{P}(\mathrm{at least six heads})=\mathrm{P}(\mathrm{X}\geq6)$ 

$$\mathrm{P}(\mathrm{X}=6)+\mathrm{P}(\mathrm{X}=7)+\mathrm{P}(\mathrm{X}=8)+\mathrm{P}(\mathrm{X}=9)+\mathrm{P}(\mathrm{X}=10)$$

$$\begin{aligned}&={}^{10}C_6\Bigg(\frac{1}{2}\Bigg)^{10}+{}^{10}C_7\Bigg(\frac{1}{2}\Bigg)^{10}+{}^{10}C_8\Bigg(\frac{1}{2}\Bigg)^{10}+{}^{10}C_9\Bigg(\frac{1}{2}\Bigg)^{10}+{}^{10}C_{10}\Bigg(\frac{1}{2}\Bigg)^{10}\\&=\frac{10!}{6!\quad4!}\quad\frac{10!}{7!\quad3!}\quad\frac{10!}{8!\quad2!}\quad\frac{10!}{9!\quad1!}\quad\frac{10!}{10!}\quad\frac{1}{2^{10}}=\frac{193}{512}\\(iii)\quad P(at most six heads)&=P(X\leq6)\\&=P\left(X=0\right)+P\left(X=1\right)+P\left(X=2\right)+P\left(X=3\right)\\&\quad+P\left(X=4\right)+P\left(X=5\right)+P\left(X=6\right)\\&=\left(\frac{1}{2}\right)^{10}+{}^{10}C_1\Bigg(\frac{1}{2}\Bigg)^{10}+{}^{10}C_2\Bigg(\frac{1}{2}\Bigg)^{10}+{}^{10}C_3\Bigg(\frac{1}{2}\Bigg)^{10}\\&\quad+{}^{10}C_4\Bigg(\frac{1}{2}\Bigg)^{10}+{}^{10}C_5\Bigg(\frac{1}{2}\Bigg)^{10}+{}^{10}C_6\Bigg(\frac{1}{2}\Bigg)^{10}\\&=\frac{848}{1024}=\frac{53}{64}\end{aligned}$$

Example 32 Ten eggs are drawn successively with replacement from a lot containing 10% defective eggs. Find the probability that there is at least one defective egg.

Solution Let X denote the number of defective eggs in the 10 eggs drawn. Since the drawing is done with replacement, the trials are Bernoulli trials. Clearly, X has the binomial distribution with $n=10\mathrm{~and~}p\quad\frac{10}{100}\quad\frac{1}{10}$ 

Therefore 

$$q=1-p=\frac{9}{10}$$

Now 

P(at least one defective egg)$\mathrm{P}(\mathrm{X}\geq1)=1-\mathrm{P}(\mathrm{X}=0)$ 

$$1-\frac{10}{10}\left(\frac{9}{10}\right)^{10}=1-\frac{9^{10}}{10^{10}}$$

### EXERCISE 13.5

1. A die is thrown 6 times. Ifgetting an odd number'is a success, what is the probability of 



(i)5 successes?(i) at least 5 successes?

(iii)at most 5 successes?

2. A pair of dice is thrown 4 times. If getting a doublet is considered a success, find the probability of two successes.



3.There are 5% defective items in a large bulk of items. What is the probability that a sample of 10 items will include not more than one defective item?

Five cards are drawn successively with replacement from a well-shuffled deck of 52 cards. What is the probability that 

(i) all the five cards are spades?

(ii) only 3 cards are spades?

(ii) none is a spade?

5.The probabilitythat a bulb produced by afactory will fuse after150days of use is 0.05. Find the probability that out of 5 such bulbs 

(i)none 

(ii) not more than one 

(i) more than one 

(iv) at least one 

will fuse after 150 days of use.

6. A bag consists of10 balls each marked with one of the digits 0 to 9.If four balls are drawn successively with replacement from the bag, what is the probability that none is marked with the digit 0?



7. In an examination, 20 questions of true-false type are asked. Suppose a student tosses a fair coin to determine his answer to each question. If the coin falls heads, he answers 'true'; if it falls tails, he answers 'false'. Find the probability that he answers at least 12 questions correctly.



8.Suppose X has a binomial distribution $ B\ 6,\frac{1}{2}$ . Show that $X=3$ is the most likely outcome.



(Hint :$P(X=3)$ is the maximum among all $\mathrm{P}(x_{i}),x_{i}=0,1,2,3,4,5,6$ 

9. On a multiple choice examination with three possible answers for each of the five questions, what is the probability that a candidate would get four or more correct answers just by guessing ?



10. A person buys a lottery ticket in 50 lotteries, in each of which his chance of winning a prize is $\frac{1}{100}$ . What is the probability that he will win a prize 

(a) at least once (b) exactly once (c) at least twice?

11.Find the probabilityof getting5exactly twicein7throws of a die.

12.Fndebiofatt2sintwole die.

13.Itisknow%ocailemanuactudeectiv.Wtiste 

probability that in a random sample of12 such articles,9 are defective?

In each of the following, choose the correct answer:



14.In a box containing 100 bulbs, 10 are defective. The probability that out of a sample of 5 bulbs, none is defective is 

(A)$10^{-1}$ (B)$\left(\frac{1}{2}\right)^{5}$ (C)$\left(\frac{9}{10}\right)^{5}$ (D)$\frac{9}{10}$ 

15Tes $\frac{1}{5}$ Te e roli out of five students, four are swimmers is 

(A)

$${}^{5}\mathrm{C}_{4}\left(\frac{4}{5}\right)^{4}\frac{1}{5}$$

(B)$\left(\frac{4}{5}\right)^{4}\frac{1}{5}$ 

(C)${}^{5}C_{1}\frac{1}{5}\left(\frac{4}{5}\right)^{4}$ 

(D) None of these 

## Miscellaneous Examples 

Example 33 Coloured balls are distributed in four boxes as shown in the following table:


<div style="text-align: center;"><html><body><table border="1"><tr><td colspan="5">Box Colour</td></tr><tr><td></td><td>Black</td><td>White</td><td>Red</td><td>Blue</td></tr><tr><td>I</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>II</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>III</td><td>1</td><td>2</td><td>3</td><td>1</td></tr><tr><td>IV</td><td>4</td><td>3</td><td>1</td><td>5</td></tr></table></body></html></div>


Abox is selected at random andthen aball israndomly drawnfrom the selcted box.Thecolouroftheball is black,what is the probabilitythatball drawn is from the box III?



Solution Let A,$\mathrm{E}_{1},\mathrm{E}_{2},\mathrm{E}_{3}$ and $ E_4$ be the events as defined below :

A : a black ball is selected $ E_1$ : box I is selected $\mathrm{E}_{2}$ : box II is selected $ E_3$ : box III is selected $\mathrm{E}_{4}$ : box IV is selected 

Since the boxes are chosen at random,

Therefore 

Also 

$$\mathrm{P}(\mathrm{E}_{1})=\mathrm{P}(\mathrm{E}_{2})=\mathrm{P}(\mathrm{E}_{3})=\mathrm{P}(\mathrm{E}_{4})=\frac{1}{4}\quad\text{P}(\mathrm{A}|\mathrm{E}_{1})=\frac{3}{18},\mathrm{P}(\mathrm{A}|\mathrm{E}_{2})=\frac{2}{8},\mathrm{P}(\mathrm{A}|\mathrm{E}_{3})=\frac{1}{7}\text{and}\mathrm{P}(\mathrm{A}|\mathrm{E}_{4})=\frac{4}{13}$$

P(box III is selected, given that the drawn ball is $\mathrm{black}=\mathrm{P}(\mathrm{E}_3|\mathrm{A})$ $\mathrm{B a y e s^{\prime}}$ theorem,

$$\begin{aligned}\mathrm{P}(\mathrm{E}_{3}|\mathrm{A})=\frac{\mathrm{P}(\mathrm{E}_{3})\mathrm{P}(\mathrm{A}|\mathrm{E}_{3})}{\mathrm{P}(\mathrm{E}_{1})\mathrm{P}(\mathrm{A}|\mathrm{E}_{1})\mathrm{P}(\mathrm{E}_{2})\mathrm{P}(\mathrm{A}|\mathrm{E}_{2})+\mathrm{P}(\mathrm{E}_{3})\mathrm{P}(\mathrm{A}|\mathrm{E}_{3})\mathrm{P}(\mathrm{A}|\mathrm{E}_{4})}\\=\frac{\frac{1}{4}\times\frac{1}{7}}{\frac{1}{4}\times\frac{3}{18}+\frac{1}{4}\times\frac{1}{4}+\frac{1}{4}\times\frac{1}{7}+\frac{1}{4}\times\frac{4}{13}}=0.165\end{aligned}$$

Example 34 Find the mean of the Binomial distribution B $\frac{1}{4},\frac{1}{3}$ 

Solution LetXbetherandomvariabl whose probability ditribution is B $4,\frac{1}{3}$ 

Here 

We know that 

$$n=4,p=\frac{1}{3}\quad and\quad q=1-\frac{1}{3}=\frac{2}{3}$$

i.e. the distribution of X is 


<div style="text-align: center;"><html><body><table border="1"><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></table></body></html></div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>2</td><td>ΔC2 2- 2 1 2 -3 3</td><td>ΔC₂ 2-3 2 1 2 2 -3</td></tr><tr><td>3</td><td>aC3 2 3 1 3 3</td><td>2-3 1 3 3 4 C3 3</td></tr><tr><td>4</td><td>1 4 ΔCa 3</td><td>ΔCs 1 4 4 -3</td></tr></table></body></html></div>


$$\begin{aligned}Now Mean(\mu)&=\sum_{i=1}^{4}x_i p(x_i)\\&=0+{}^{4}C_1\left(\frac{2}{3}\right)^3\left(\frac{1}{3}\right)+2\cdot{}^{4}C_2\left(\frac{2}{3}\right)^2\left(\frac{1}{3}\right)^2+3\cdot{}^{4}C_3\cdot\frac{2}{3}\cdot\frac{1}{3}\cdot\frac{1}{3}\cdot\frac{4}{3}\cdot\frac{4}{3}\cdot\frac{1}{3}\cdot\frac{4}{3}\\&=4\times\frac{2^3}{3^4}+2\times6\times\frac{2^2}{3^4}+3\times4\times\frac{2}{3^4}+4\times1\times\frac{1}{3^4}\\&=\frac{32+48+24+4}{3^4}=\frac{108}{81}=\frac{4}{3}\end{aligned}$$

Exampleolooorets $\left[\frac{3}{4}\right.]$ . How many minimum number of times must he/she fire so that the probability of hitting the target at least once is more than 0.99?



Solution Let the shooter fire n times. Obviously, n fires are n Bernoulli trials. In ach trial,$p=\mathrm{probability}$ y of hitting the ta $\mathrm{arget}=\frac{\dot{3}}{4}$ and $q=\mathrm{probability}$ of not hitting the 

$$ target=\frac{1}{4}.Then P(X=x)={}^{n}C_{x}q^{n-x}p^{x}={}^{n}C_{x}\left(\frac{1}{4}\right)^{n-x}\left(\frac{3}{4}\right)^{x}={}^{n}C_{x}\frac{3^{x}}{4^{n}}.$$

Now, given that,

P(hitting the target at least $\mathrm{once}>0.99$ 

i.e.

$$\mathbb{P}(x\geq1)>0.99$$

Therefore,

$$1-\mathrm{P}(x=0)>0.99$$

or 

$$1-{}^{n}\mathrm{C}_{0}\frac{1}{4^{n}}>0.99$$

or 

$$\left\{\begin{aligned}{}&{{}^{n}\mathrm{C}_{0}\frac{1}{4^{n}}\quad0.01\quad\mathrm{i.e.}\quad\frac{1}{4^{n}}<0.01}\end{aligned}\right.$$

or 

$$4^{n}>\frac{1}{0.01}=100$$

The minimum value of  to satisfy the inequality (1) is 4.

Thus, the shooter must fire 4 times.

Example 36 A and B throw a die alternatively till one of them gets a $^{\ast}6^{\ast}$ and wins the game. Find their respective probabilities of winning, if A starts frst.

Solution Let S denote the success (getting $ a``6''$ and F denote the failure (not getting $a^{\prime}6^{\prime}$ 1



Thus,

$$\mathrm{P}(\mathrm{S})=\frac{1}{6},\mathrm{P}(\mathrm{F})=\frac{5}{6}$$

$$\mathrm{P}(\mathrm{A}\text{wins in the first through})=\mathrm{P}(\mathrm{S})=\frac{1}{6}$$

A failures.



Therefore,P(A wins in the 3rd throw $\mathrm{P}(\mathrm{FFS})=\mathrm{P}(\mathrm{F})\mathrm{P}(\mathrm{F})\mathrm{P}(\mathrm{S})=\frac{5}{6}\quad\frac{5}{6}\quad\frac{1}{6}$ 

$$\left(\frac{5}{6}\right)^{2}\times\frac{1}{6}$$

$$\mathrm{P}(\mathrm{A}\text{wins in the}5\mathrm{th}\text{through})=\mathrm{P}\left(\mathrm{FFFS}\right)\quad\frac{5}{6}\quad\frac{4}{6}\text{and so on.}$$

Hence,

$$\begin{aligned}\mathrm{P}(\mathrm{A}\mathrm{wins})&=\frac{1}{6}\quad\frac{5}{6}\quad\frac{1}{6}\quad\frac{5}{6}\quad\frac{4}{6}\quad\cdots\\&=\frac{\frac{1}{6}}{1-\frac{25}{36}}=\frac{6}{11}\end{aligned}$$

$$\mathrm{P}(\mathrm{B}\mathrm{wins})=1-\mathrm{P}(\mathrm{A}\mathrm{wins})=1\frac{6}{11}\frac{5}{11}$$

Remark If $a+a r+a r^{2}+...+a r^{n-1}+...,$ where $|r|\leq1$ , then sum of this infinite G.P.is given by $\frac{a}{1-r}$ · (Refer A.1.3 of Class XI Text book).



ExampleIfmachineisoctlytupitproduces%acceptableitems.Ifitis incorrectly set up, it produces only 40% acceptable items. Past experience shows that 80% of the set ups are correctly done. If after a certain set up, the machine produces 2 acceptable items, find the probability that the machine is correctly setup.

Solution Let A be the event that the machine produces 2 acceptable items.

Also let $\mathrm{B_{1}}$ represent the event of correct set up and $ B_2$ represent the event of incorrect setup.



Now 

Therefore 

$$\begin{aligned}P(B_1)&=0.8,P(B_2)=0.2\\ P(A|B_1)&=0.9\times0.9and P(A|B_2)=0.4\times0.4\\ P(B_1|A)&=\frac{P(B_1)P(A|B_1)}{P(B_1)P(A|B_1)+P(B_2)P(A|B_2)}\\&=\frac{0.8\times0.9\times0.9}{0.8\times0.9\times0.9+0.2\times0.4\times0.4}=\frac{648}{680}=0.95\end{aligned}$$

## Miscellaneous Exercise on Chapter 13

1. A and B are two events such that $\mathbb{P}\left(\mathrm{A}\right)\neq0$ Find $\mathrm{P(B|A)}$ , if 

(i)A is a subset of B (ii)$A\cap B=\phi$ 

A couple has two children,

(i) Find the probability that both children are males, if it is known that at least one of the children is male.



(ii) Find the probability thatbothchildre are males,iit is known that the elder child is a female.



3.Suppose that 5% of men and 0.25% of women have grey hair. A grey haired person is selected at random. What is the probability of this person being male?Assume that there are equal number of males and females.

Suppose that 90% of people are right-handed. What is the probability that at most 6 of a random sample of 10 people are right-handed?

5.An urn contains25balls ofwhich10balls bear a mark'X andtheremaining 15bear a mark 'Y'.Aball is drawn at random from the urn, its mark is noted down and it is replaced.Iballs are drawn in this way,findte probability that 

(i)all will bear 'X' mark.

(ii) not more than 2 will bear 'Y' mark.

(ii)at least one ball will bear $\mathrm{Y}$ mark.

(iv) the number of balls with 'X' mark and 'Y' mark will be equal.

6.In a hurdle race, a player has to cross 10 hurdles. The probability that he will clear each hurdle is $\frac{5}{6}$ . What isthe probailitythathe willkock dow fwer than 2 hurdles?



7.A die is thrown again and again until three sixes are obtained. Find the probability of obtaining the third six in the sixth throw of the d.

8.If a leap year is selected at random, what is the chance that it will contain 53tuesdays?



9.An experiment succeeds twice as often as it fails. Find the probability that in the next six trials, there will be atleast 4 successes.



10. How many times must a man toss a fair coin so that the probability of having at least one head is more than 90%?



11.In a game, a man wins a rupee for a six and loses a rupee for any other number when a fair die is thrown. The man decided to throw a die thrice but to quit as and when he gets a six. Find the expected value of the amount he wins / loses.12. Suppose we have four boxes A,B,C and D containing coloured marbles as given below.




<div style="text-align: center;"><html><body><table border="1"><tr><td>Box</td><td colspan="3">Marble colour</td></tr><tr><td></td><td>Red</td><td>White</td><td>Black</td></tr><tr><td>A</td><td>1</td><td>6</td><td>3</td></tr><tr><td>B</td><td>6</td><td>2</td><td>2</td></tr><tr><td>C</td><td>8</td><td>1</td><td>1</td></tr><tr><td>D</td><td>0</td><td>6</td><td>4</td></tr></table></body></html></div>


One of the boxes has been selected at random and a single marble is drawn from it. If the marble is red, what is the probability that it was drawn from box A?, box B?,box C?



13.Assume that the chances of a patient having a heart attack is 40%. It is also assumed that a meditation and yoga course reduce the risk of heart attack by 30% and prescription of certain drug reduces its chances by 25%. At a time a patient can choose any one of the two options with equal probabilities. It is given that after going through one of the two options the patient selected at random suffers a heart attack. Find the probability that the patient followed a course of meditation and yoga?



14. If each element of a second order determinant is either zero or one, what is the probability that the value of the determinant is positive? (Assume that the individual entries of the determinant are chosen independently, each value being assumed with probability $\frac{1}{2}$ 1.



15.Anlcoimblyoitotwubyms,a,AndB.From evioustesting pcedures, thelowing probablie are asumedtobekown:

$$\begin{aligned}P(A fails)&=0.2\\ P(B fails alone)&=0.15\\ P(A and B fail)&=0.15\end{aligned}$$

Evaluate the following probabilities 

(i) P(A fails|B has failed)P(A fails alone)

16.BagIcontains3redand4blackballsandBagIIcontains4redand5black balls.Oneball is transferred from Bag I to BagII and then a ball is drawn from Bag II.The ball so drawn is found to be red in colour.Find the probability that the transferred ball is black.



Choose the correct answer in each of the following:

17. If A and B are two events such that $\mathrm{P}(\mathrm{A})\neq0\text{and}\mathrm{P}(\mathrm{B}\mid\mathrm{A})=1$ ,then 

(A)$\mathrm{A}\subset\mathrm{B}$ (B)$ B\subset A$ (C)$\mathrm{B}=\phi$ (D)$\mathbf{A}=\mathbf{\boldsymbol{\phi}}$ 

18.If $\mathrm{P}(\mathrm{A}\mid\mathrm{B})>\mathrm{P}(\mathrm{A})$ ,then which of the following is correct :

(A)

$$\mathrm{P}(\mathrm{B}|\mathrm{A})<\mathrm{P}(\mathrm{B})$$

(B)

$$\mathrm{P}(\mathrm{A}\cap\mathrm{B})<\mathrm{P}(\mathrm{A}).\mathrm{P}(\mathrm{B})$$

(C)

$$\mathrm{P(B|A)>P(B)}$$

(D)

$$\mathrm{P}(\mathrm{B}|\mathrm{A})=\mathrm{P}(\mathrm{B})$$

19. If A and B are any two events such that $\mathrm{P}(\mathrm{A})+\mathrm{P}(\mathrm{B})-\mathrm{P}(\mathrm{A}\text{and}\mathrm{B})=\mathrm{P}(\mathrm{A})$ |,then 

(A)

$$\mathrm{P}(\mathrm{B}|\mathrm{A})=1$$

(B)

$$\mathrm{P}(\mathrm{A}|\mathrm{B})=1$$

(C)

$$\mathrm{P}(\mathrm{B}|\mathrm{A})=0$$

(D)

$$\mathrm{P}(\mathrm{A}|\mathrm{B})=0$$

## Summary 

The salient features of the chapter are–

■The conditional probability of an event E, given the occurrence of the event F 

is given by $\mathrm{P}(\mathrm{E}\mid\mathrm{F})=\frac{\mathrm{P}(\mathrm{E}\cap\mathrm{F})}{\mathrm{P}(\mathrm{F})},\mathrm{P}(\mathrm{F})\neq0$ 

$$0\leq\mathrm{P}(\mathrm{E}|\mathrm{F})\leq1,\quad\mathrm{P}(\mathrm{E}'|\mathrm{F})=1-\mathrm{P}(\mathrm{E}|\mathrm{F}) ublish $$

$$\mathrm{P}\left((\mathrm{E}\cup\mathrm{F})|\mathrm{G}\right)=\mathrm{P}\left(\mathrm{E}|\mathrm{G}\right)+\mathrm{P}\left(\mathrm{F}|\mathrm{G}\right)-\mathrm{P}\left((\mathrm{E}\cap\mathrm{F})|\mathrm{G}\right) ublish $$

■$\mathrm{P}(\mathrm{E}\cap\mathrm{F})=\mathrm{P}(\mathrm{E})\mathrm{P}(\mathrm{F}|\mathrm{E}),\mathrm{P}(\mathrm{E})\neq0$ 

$$\mathrm{P}(\mathrm{E}\cap\mathrm{F})=\mathrm{P}(\mathrm{F})\mathrm{P}(\mathrm{E}|\mathrm{F}),\mathrm{P}(\mathrm{F})\neq0$$

If E and F are independent, then 

$$\begin{aligned}&P\left(E\cap F\right)=P\left(E\right)P\left(F\right)\\ &P\left(E|F\right)=P\left(E\right),P\left(F\right)\neq0\\ &P\left(F|E\right)=P\left(F\right),P(E)\neq0\\ \end{aligned}$$

■Theorem of total probability 

Let $\left\{\mathrm{E}_{1},\mathrm{E}_{2},\ldots,\mathrm{E}_{n}\right\}$ be a partition of a sample space and suppose that each of ublish $E_{1},E_{2},...,\bar{E}_{n}$ has nonzero probability. Let A be any event associated with S then 



$$\mathrm{P}(\mathrm{A})=\mathrm{P}(\mathrm{E}_{1})\mathrm{P}\left(\mathrm{A}|\mathrm{E}_{1}\right)+\mathrm{P}\left(\mathrm{E}_{2}\right)\mathrm{P}\left(\mathrm{A}|\mathrm{E}_{2}\right)+\cdots+\mathrm{P}\left(\mathrm{E}_{n}\right)\mathrm{P}\left(\mathrm{A}|\mathrm{E}_{n}\right)$$

■Bayes'theorem If $\mathrm{E}_{1},\mathrm{E}_{2},\ldots,\mathrm{E}_{n}$ are events which constitute a partition of sample space S, i.e.$\mathrm{E}_{1},\mathrm{E}_{2},\ldots,\mathrm{E}_{n}$ are pairwise disjoint and $\mathrm{E}_{1}4\ \mathrm{E}_{2}4\ \ldots4\ \mathrm{E}_{n}=\mathrm{S}$ and A be any event with nonzero probability, then 

$$\mathrm{P}(\mathrm{E}_{i}\mid\mathrm{A})\quad\frac{\mathrm{P}(\mathrm{E}_{i})\mathrm{P}(\mathrm{A}\mid\mathrm{E}_{i})}{n}\quad\mathrm{P}(\mathrm{E}_{j})\mathrm{P}(\mathrm{A}\mid\mathrm{E}_{j})$$

A random variable is a real valued function whose domain is the sample space of a random experiment.



The probability distribution of a random variable X is the system of numbers 

$$\begin{array}{llll}X&:&\quad x_{1}\quad&x_{2}\quad&\ldots\quad&x_{n}\\ P(X)&:&\quad p_{1}\quad&p_{2}\quad&\ldots\quad&p_{n}\\\end{array}$$

where,$p_{i}>0,\sum_{i=1}^{n}p_{i}=1,i=1,2,...,n$ 

■Let X be a random variable whose possible values $x_{1},x_{2},x_{3},...,x_{n}$ occur with probabilities $p_{1},p_{2},p_{3},\ldots p_{n}$ respectively. The mean of X, denoted by μ, is 

the number $_{i,1}x_{i}p_{i}$ 

The mean of a random variable X is also called the expectation ofX, denoted by E (X).



■Let X be a random variable whose possible values $x_{1},x_{2},...,x_{n}$ occur with ]probabilities $p(x_{1}),p(x_{2}),\ldots,p(x_{n})$ respectively.Y 

Let $\mu=\mathrm{E}(X)$  he   X.Y of X, denoted by Var (X) or 

$$\sigma_{x}^{2},is defined as\quad\sigma_{x}^{2}\quad Var(X)=\underset{i,1}{\overset{n}{\sigma}}(x_{i}\quad\mu)^{2}p(x_{i})$$

or equivalently Y $\sigma_{x}^{2}=\mathrm{E}\left(\mathrm{X}-\mu\right)^{2}$ 

The non-negative number 

$$\sqrt{\mathrm{Var}(\mathbf{X})}=\sqrt{\sqrt{n}\left(x_{i}\quad\mu\right)^{2}p(x_{i})}$$

is called the standard deviation of the random variable X.

❤Var $\mathrm{(X)=E(X^2)-[E(X)]^2}$ 

Trials of a random experiment are called Bernoulli trials, if they satisfy the following conditions :

There should be a finite number of trials.

(i)The trials should be independent.

(iii)Each trial has exactly two outcomes : success or failure.

(iv)The probability of success remains the same in each trial.

For Binomial distribution B $(n,p)$ $P\left(X=x\right)={}^{n}C_{x}q^{n-x}p^{x},x=0,1,\ldots,n$ 

$(q=1-p)$ 



## Historical Note 

The earliest indication on measurement of chances in game of dice appeared in 1477 in a commentary on Dante's Divine Comedy. A treatise on gambling named liber de Ludo Alcae, by Geronimo Carden (1501-1576) was published posthumously in 1663. In this treatise, he gives the number of favourable cases for each event when two dice are thrown.



Galileo (1564-1642)gave casual emarkscorig the correct evaluation of chance in a game of three dice.Galileo analysed that when three dice are thrown,the sum of the number that appear is more likely to be 10than the sum 9,because the number of cases favourable to 10are more than the number of cases for the appearance of number 9.



Apart from these early contributions,it is generally acknowledged that the true origin of the science of probability lies in the correspondence between two great men of the seventeenth century,Pascal (1623-1662)and Pierre de Fermat (1601-1665).A French gambler,Chevalier de Metre asked Pascal to explain some seeming contradiction between his theoretical reasoning and the observation gathered from gambling.In series of letters written around 1654,Pascal and F Fermatlaid the first foundation of proba ability.Pascals solved the problem in algebraic manner while erm nat used the meth nod of combinations.

Great Dutch Scientist,Huygens (1629-1695),became acquainted with the content of the correspondence between Pascal and Fermat and published a first book on probability,"De Ratiociniis in Ludo Aleae'containing solution of many interesting rather than difficult problems on probability in games of chances.

The next t great work on probability theory is by Jacob Bernoulli (1654-1705),in the form of a great book,'Ars Conjectendi'published posthumously in 1713by his nephew,Nicholes Bernoulli To him is due the discovery of one of the most important probability distribution known as Binomial distribution.The next remarkable work on probability lies in 1993.A.N.Kolmogorov (1903-1987)is credited with the axiomatic theory of probability.His book,'Foundations of probability published in 1933,introduces probability as a set function and is considered a classic!'.

