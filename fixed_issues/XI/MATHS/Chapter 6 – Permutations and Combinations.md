

# PERMUTATIONS AND COMBINATIONS 

## 出Every bodyof discovery is mathematical in form because there is no other guidance we can have – DARWIN 田there is no 

### 6.1 Introduction 

Suppose you have a suitcase with a number lock. The number lock has 4 wheels each labelled with 10 digits from 0 to 9.The lock can be opened if 4 specific digits are arranged in a particular sequence with no repetition. Some how, you have forgotten this specific sequence of digits.You remember only the first digit which is 7.In order to open the lock, how many sequences of 3-digits you may have to check with? To answer this question, you may, immediately, start listing all possible arrangements of 9 remaining digits taken 3 at a time. But, this method will be tedious, because the number of possible sequences may be large. Here, in this Chapter,we shall learn some basic counting techniques which will 

<div style="text-align: center;"><img src="imgs/img_in_image_box_640_492_883_819.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">Jacob Bernoulli (1654-1705)</div>


enable us to answer this question without actually listing 3-digit arrangements. In fact,these techniques will be useful in determining the number of different ways of arranging and selecting objects without actually listing them. As a first step, we shall examine a principle which is most fundamental to the learning of these techniques.

### 6.2 Fundamental Principle of Counting 

Let us consider the following problem. Mohan has 3 pants and 2 shirts. How many different pairs of a pant and a shirt, can he dress up with? There are 3 ways in which a pant can be chosen, because there are 3 pants available. Similarly, a shirt can be chosen in 2 ways. For every choice of a pant, there are 2 choices of a shirt. Therefore,there are $3\times2=6$ pairs of a pant and a shirt.



Let us name the three pants as $\mathrm{P}_{1},\mathrm{P}_{2},\mathrm{P}_{3}$ and the two shirts as $ S_1,S_2$ . Then,theseixlli.



Let us consider another problem of the same type.



Sabnam has 2 school bags, 3 tiffin boxes and 2 water bottles. In how many ways can she carry these items (choosing one each).



A school bag can be chosen in 2different ways. After a school bag is chosen, a tiffin box can be chosen in 3different ways. Hence, there are $2\times3=6$ pairs of school bag and a tiffin box. For each of these pairs a water ciCintWayS.6 Possibilities 

<div style="text-align: center;"><img src="imgs/img_in_image_box_460_244_783_603.jpg" alt="Image" width="34%" /></div>


Hence, there are $6\times2=12$ f school. If we name the 2 school bags $\mathrm{asB_{1}^{-}B_{2}^{-}}$ ,the three tf in boxes as $\mathrm{T}_{1},\mathrm{T}_{2},\mathrm{T}_{3}$ , and the two water bottles as $\mathrm{W}_{1},\mathrm{W}_{2}$ ,te silites the Fig. 6.2.

12 Possibilities 

<div style="text-align: center;">Fig 6.2</div>


In fact, the problems of the above types are solved by applying the following principle known as the fundamental principle of counting, or, simply, the multiplication principle, which states that 



"If an event can occur in m different ways, following which another event can occur in n different ways, then the total number of occurrence of the events in the given order is $m\times n$ ''

The above principle can be generalised for any finite number of events. For example, for 3 events, the principle is as follows:

'If an event can occur in m different ways, following which another event can occur in n different ways, following which a third event can occur in p different ways,then the total number of occurrence to 'the events in the given order is $m\times n\times p$ 

In the first problem, the required number of ways of wearing a pant and a shirt was the number of different ways of the occurence of the following events in succession:

(i) the event of choosing a pant 

(ii) the event of choosing a shirt.

In the second problem, the equired number of ways was the umber of ifferet ways of the occurence of the following events in succession:

(i)the event of choosing a school bag 

(i)the event of choosing a tiffin box 

(i)the event of choosing a water bottle.

Here, in both the ae,the vnts i ach problemould ur in arius posible orders. But, we have to choose any one of the possible orders and count the number of different ways of the occurence of the events in this chosen order.

Example 1 Find the number of 4 letter words, with or without meaning, which can be formed out of the letters of the word ROSE, where the repetition of the letters is not allowed.



Solution There are as many words as there are ways of filling in 4 vacant places bythe  ers keeping in mind that the eptition is not allowd.The first place can be filled in 4diferent ways by anyone of the4 letters $\scriptstyle\mathbb{R},\mathrm{O},\mathrm{S},\mathrm{E}$ Following which, the second place can be filled in by anyone of the remaining 3 letters in 3different ays, llowing hihtetird plaecn e filld in2drnt ys; llowing which, the fourth place can be filled in 1 way. Thus, the number of ways in which the 4 places can be filled, by the multiplication principle, is $4\times3\times2\times1=24$ . Hence, the required number of words is 24.



Noeollw Onecals in 4 different ways. Hence, the required number of words $s=4\times4\times4\times4=256$ 

Example2Given4flagsofdifferentcolours,how manydifferent signals can be generated, i  signalrequiresthe useof2flagsonebelowtheother?

Solution Threwillbeamanialatereareayofllini2cantplaces 

<div style="text-align: center;"><img src="imgs/img_in_image_box_84_375_158_426.jpg" alt="Image" width="7%" /></div>


in succession by the 4flags of different colours.The upper vacant place can 

be filled in4 diferent ways by anyone of the 4flags; following which,the lower vacant place canbelledin3 diferent ways by anyoneoftheremaining3 differentflags.Hence, by the multiplication principle, the required numer of $\mathrm{signals}=4\times3=12$ 

Example 3 How many 2 digit even numbers can be formed from the digits 1,2, 3, 4,5 if the digits can be repeated?



Solution There will be as many waysasthereare waysof filling2vacant places 

<div style="text-align: center;"><img src="imgs/img_in_image_box_86_653_145_692.jpg" alt="Image" width="6%" /></div>


insucseiitliit's 

place, because the options for this place are2 and 4 only and this can be done in 2ways; following whichthetn's placecanbefled byanyofthe5digitsin5different ways s ed number of two digits even numbers is $2\times5,\mathrm{i}_{\mathrm{e}}$ , 10.



Example 4 Find the number of different signals that can be generated by arranging at st available.



Solution Asignalcanconsistofeither2flags,3flags,4flagsor5flags.Now,let us count the possiblenumberof signals consistingof2 flags,3flags,4flags and 5flags separately and then add the respective numbers.



There will be as many2flag signals asthere are ways offilling in2vacant places 

in succession by the 5 flags available. By Multiplication rule, the number of ways is $5\times4=20$ 



Similarly, there will be as many 3 flag signals as there are ways of filling in 3

vacant places 

<div style="text-align: center;"><img src="imgs/img_in_image_box_216_1191_304_1250.jpg" alt="Image" width="9%" /></div>


in succession by the 5 flags.

The number of ways is $5\times4\times3=60$ 

Continuing the same way, we find that 

Thenumberof4flag signals=5×4×3×2=120and the number of 5 flag $\mathrm{signals}=5\times4\times3\times2\times1=120$ Therefore, the required no of signals $20+60+120+120=320$ 

### EXERCISE 6.1

1.How many 3-digit numbers can be formed from the digits 1, 2,3, 4 and 5assuming that ed 

(i)repetition of the digits is allowed?

(ii)repetition of the digits is not llowed?

2.How many 3-digit even numbers can be formed from the digits 1, 2,3,4, 5, 6 if the digits can be repeated?



3.How many 4-letercodecan be formed using thefirst10letersofthe English alphabet, if no letter can be repeated?



How many 5-digit telephone numbers can be constructed using the digits 0 to 9 if each number starts with 67 and no digit appears more than once?

5.A coin is tossed 3 times and the outcomes are recorded. How many possible outcomes are there?



6.Given 5 flags of different colours, how many different signals can be generated if each signal requires the use of 2 flags, one below the other?

### 6.3 Permutations 

In Example 1 of the previous Section, we are actually counting the different possible arrangements of the letters such as ROSE, REOS, …, etc. Here, in this list, each arrangement is different from other. In other words, the order of writing the letters is important. Each arrangement is called a permutation of 4 diferent letters taken all at a time. Now, if we have to determine the number of 3-letter words, with or without meaning, which can be formed out of the letters of the word NUMBER, where the repetition of the letters is not allowed, we need to count the arrangements NUM,NMU, MUN, NUB, …, etc. Here, we are counting the permutations of 6 different letters taken 3 at a time. The required number of $\mathrm{word}s=6\times5\times4=120$ (by using multiplication principle).



If the repetition of the letters was allowed, the required number of words would be $6\times6\times6=216$ 



Definition1Apermutation is an arrangement in a definiteorderof a number of objects taken some or all at a time.



In the following sub-section, we shall obtain the formula needed to answer these questions immediately.



#### 6.3.1 Permutations whenall the objects are distinct 

Theorem 1 The number of permutations of n different objects taken r at a time,where $0\leq r\leq n$ and the objects do not repeat is n $(n-1)(n-2).\therefore(n-r+1)$ which is denoted by ${}^{n}\mathrm{P}_{i}$ r 



Proof There will be as many permutations as there are ways of filling in $r{\widehat{\mathtt{vacant}}}$ places by 



←r vacant places →

the n objects. The first place can be filled in n ways; following which, can be filled in $(n-1)$ ways, following which the third place can be filled in $(n-2)$ !$\mathtt{WayS},...,$ , the rth place can be filled in $(n-(r-1))$ ) ways. Therefore, the number of ways of filling in r vacant places in succession is $n(n-1)(n-2)\ldots(n-(r-1))$ or 

$n\;(n-1)\;(n-2)\ldots(n-r+1)$ 



This expression for $^{n}\mathrm{P}_{n}$ is cumbermend weoti hic illl reduce the size of this expression. The symbol n! (read as factorial n or  factorial)comes to our rescue.In the following text we will learn what actually n! means.

6.3.2Factorial notationThe notation n! represents the product of first n natural numbers, i.e., the product 1$2\times3\times(n-1)\times n$ is denoted as n!. We read this symbol as $^{\ast}n$ factorial'. Thus,$1\times2\times3\times4\ldots\times(n-1)\times n=n!$ 

$$\begin{array}{l}1=1!\\1\times2=2!\\1\times2\times3\times3!\\1\times2\times3\times4=4!and so on.\end{array}$$

We define $0!=1$ 

We can write 

$$\begin{aligned}&S_{1}=5\times4!=5\times4\times3!=5\times4\times3\times2!\\ &\quad=5\times4\times3\times2\times1!\\ \end{aligned}$$

Clearly, for a natural number n 

$$\begin{array}{rlrl}{n!}&{=n(n-1)!}\\ &{=n(n-1)(n-2)!}&&{[\mathrm{provided}(n\geq2)]}\\ &{=n(n-1)(n-2)(n-3)!}&&{[\mathrm{provided}(n\geq3)]}\end{array}$$

and so on.

Example 5 Evaluate (i) 5 !(ii) 7!(iii $7!-5!$ 

(i)

$$5!=1\times2\times3\times4\times5=120$$

(ii)

$$7!=1\times2\times3\times4\times5\times6\times7=5040$$

and 

(imi)

$$7!-5!=5040-120=4920.$$

Example 6 Compute (i)$\begin{array}{rl}{\overbrace{\frac{7!}{5!}}^{7!}}&{{}\mathrm{~(i i)~}\cfrac{12!}{\left(10!\right)\left(2!\right)}}\end{array}$ 

Solution (i) We have $$ −

and (ii)$$ 

Example 7 Evaluate $\frac{n!}{r!(n-r)!}$ , when $n=5,r=2$ .

Solution We have to evaluate $$ V 

We have 

$$V \frac{5!}{2!(5-2)!}=\frac{5!}{2!\times3!}=\frac{5\times4}{2}=10(C)
$$

(C)

Example 8$\frac{1}{8!}+\frac{1}{9!}=\frac{x}{10!}$ ,find x.

Solution We have $\frac{1}{8!}+\frac{1}{9\times8!}=\frac{x}{10\times9\times8!}$ 

So 

Therefore 

$$\frac{1}{1+\frac{1}{9}}=\frac{x}{10\times9}or\quad\frac{10}{9}=\frac{x}{10\times9}x=100.$$

$$\frac{1}{1+\frac{1}{9}}=\frac{x}{10\times9}or\quad\frac{10}{9}=\frac{x}{10\times9}x=100.
$$

EXERCISE 6.2

1.Evaluate 

(i) 8!

(ii)$4!-3!$ 

$$\mathrm{Is}3!+4!=7!?\quad\mathrm{Im}\quad\frac{8!}{6!\times2!}\quad\mathrm{IS}\quad\frac{1}{6!}+\frac{1}{7!}=\frac{x}{8!},\quad\mathrm{find}x $$

5.Evaluate $\frac{n!}{\left(n-r\right)!}$ ,when 

$$(\mathrm{i})n=6,r=2\quad(\mathrm{ii})n=9,r=5.$$

6.3.3 Derivation of the formula for ${}^{n}P_{j}$ 

$${}^{n}\mathrm{P}_{r}=\frac{n!}{(n-r)!},0\leq r\leq n $$

Let us now go back to the stage where we had determined the following formula:

$${}^{n}\mathrm{P}_{r}=n(n-1)(n-2)\ldots(n-r+1)$$

Multiplying numerator and denomirator by $(n-r)(n-r-1)\cdot3\times2\times1$ , we get 

$$\frac{n(n-1)(n-2)\ldots(n-r+1)(n-r)(n-r-1)\ldots3\times2\times1}{(n-r)(n-r-1)\ldots3\times2\times1}=\frac{n!}{(n-r)!}$$

Thus 

$$P_{r}=\frac{n!}{(n-r)!},\quad where0<r\leq n $$

This is a much more convenient expression for ${}^{n}\mathrm{P}_{n}$ than the previous one.

In particular whn $r=n,\quad P_n=\frac{n!}{0!}=n!$ 

Counting permutations is merely counting the number of ways in which some or all objects at atime are rearranged.Arranging noobjectatall is the sameas leaving behind all the objects and we know that there is only one way of doing so. Thus, we can have 



$$P_{0}=1=\frac{n!}{n!}=\frac{n!}{(n-0)!}$$

Therefore, the formula (1) is applicable for $r=0$ also.

Thus 

$${}^{n}\mathrm{P}_{r}=\frac{n!}{(n-r)!},0\leq r\leq n\text{}_{j}$$

Theorem 2 The number of permutations of n different objects taken r at a time,where repetition is allowed, is $n^{r}$ .



Proof is very similar to that of Theorem 1 and is left for the reader to arrive at.

Here, we are solving some of the problems of the pervious Section using the formula for $^{n}\mathrm{P}_{n}$ to illustrate its usflns.



In Example 1, the required number of words $={}^{4}\mathrm{P}_{4}=4!=24$ . Here repetition is not allowed.  If repetition is alowed, the required number of words would be $4^{4}=256$ 

The number of 3-letter words which can be formed by the letters of the word 

$\mathrm{NUMBER}=\frac{6}{3!}=\frac{6!}{3!}=4\times5\times6=120$ . Here, in this case also, the repetition is not 

allowed. If the repetition is allowed,the required number of words would be $\widetilde{6^{3}}=216$ 

The number of ways in which a Chairman and a Vice-Chairman can be chosen from amongst a groupof2 perons asuming that one peroncaothold more than one position, clearly $\mathrm{P}_{2}=\frac{12!}{10!}=11\times12=132.$ 

6.3.4Permutationswhenall the ob ct objects Suppose we have to find the number of ways of rearranging the letters of the word ROOT. In this case,the letters of the word are not all different.There are 2 Os, which are of the same kind.Let us treat, temporarily, the $2.0s$ as different, say,$\mathrm{O}_{1}$ and $\mathrm{O}_{2^{\circ}}$ Thenumber of permutations of $4{\scriptstyle-{\mathrm{different}}}$ :letters, in this case, taken all at a time is 4!. Consider one of these permutations say,$\mathrm{RO_{1}O_{2}T}$ . Corresponding to this permutation,we have 2 ! permutations R $\mathrm{O_{1}O_{2}T}$ and $\mathrm{RO}_{2}\mathrm{O}_{1}\mathrm{T}$ which will be exactly the same permutation if $\mathrm{O_{t}}$ and $\mathrm{O}_{2}^{+}$ are not treated as different, i., if $\mathrm{O}_{1}$ and $\mathrm{O}_{2}$ are the same O at both places.



Therefore, the required number of ]$permutations=\frac{4!}{2!}=3\times4=12$ 

```text
Permutations when O₁, O₂ are different      Permutations when O₁, O₂ are the same O

⎡ RO₁TO₂ ⎤   →   ROTO
⎣ RO₂TO₁ ⎦

⎡ TO₁RO₂ ⎤   →   TORO
⎣ TO₂RO₁ ⎦

⎡ RT O₁O₂ ⎤  →   RTOO
⎣ RT O₂O₁ ⎦

⎡ TR O₁O₂ ⎤  →   TROO
⎣ TR O₂O₁ ⎦

⎡ O₁O₂RT ⎤   →   OORT
⎣ O₂O₁TR ⎦

⎡ O₁RO₂T ⎤   →   OROT
⎣ O₂RO₁T ⎦

⎡ O₁TO₂R ⎤   →   OTOR
⎣ O₂TO₁R ⎦

⎡ O₁RTO₂ ⎤   →   ORTO
⎣ O₂RTO₁ ⎦

⎡ O₁TRO₂ ⎤   →   OTRO
⎣ O₂TRO₁ ⎦

⎡ O₁O₂TR ⎤   →   OOTR
⎣ O₂O₁TR ⎦
```

$$\begin{array}{ccc}\left[\begin{array}{c}\mathrm{RO}_{1}\mathrm{T}\mathrm{O}_{2}\\\mathrm{R}_{\mathrm{O}}\mathrm{T}\mathrm{O}_{1}\end{array}\right]&\xrightarrow{\quad}&\mathrm{R}\text{~0}\mathrm{T}\mathrm{O}_{1}\\\left[\begin{array}{c}\mathrm{T}\mathrm{O}_{1}\mathrm{R}\mathrm{O}_{2}\\\mathrm{R}_{\mathrm{O}}\mathrm{R}_{\mathrm{O}}\end{array}\right]&\xrightarrow{\quad}&\mathrm{T}\text{~0}\mathrm{R}\mathrm{~0}\\\left[\begin{array}{c}\mathrm{R}\mathrm{T}\mathrm{O}_{1}\mathrm{O}_{2}\\\mathrm{R}_{\mathrm{T}}\mathrm{O}_{2}\mathrm{O}_{1}\end{array}\right]&\xrightarrow{\quad}&\mathrm{R}\text{~0}\mathrm{~0}\\\left[\begin{array}{c}\mathrm{R}\mathrm{T}\mathrm{O}_{1}\mathrm{O}_{2}\\\mathrm{R}_{\mathrm{T}}\mathrm{R}_{\mathrm{O}}\mathrm{O}_{1}\end{array}\right]&\xrightarrow{\quad}&\mathrm{T}\mathrm{~0}\mathrm{~0}\\\left[\begin{array}{c}\mathrm{R}\mathrm{O}_{1}\mathrm{O}_{2}\mathrm{~R}\mathrm{T}\\\mathrm{O}_{2}\mathrm{~O}_{1}\mathrm{~R}\mathrm{T}\end{array}\right]&\xrightarrow{\quad}&\mathrm{O}\mathrm{~0}\mathrm{~R}\mathrm{~T}\\\left[\begin{array}{c}\mathrm{R}\mathrm{O}_{1}\mathrm{R}_{\mathrm{O}}\mathrm{T}\\\mathrm{O}_{2}\mathrm{R}_{\mathrm{O}}\mathrm{O}_{1}\mathrm{T}\end{array}\right]&\xrightarrow{\quad}&\mathrm{O}\mathrm{~R}\mathrm{~0}\mathrm{~T}\\\left[\begin{array}{c}\mathrm{R}\mathrm{O}_{1}\mathrm{T}\mathrm{O}_{2}\\\mathrm{R}_{\mathrm{T}}\mathrm{O}_{1}\mathrm{R}\end{array}\right]&\xrightarrow{\quad}&\mathrm{O}\mathrm{~0}\mathrm{~R}\mathrm{~0}\\\left[\begin{array}{c}\mathrm{R}\mathrm{T}\mathrm{O}_{2}\\\mathrm{O}_{2}\mathrm{~R}\mathrm{T}\mathrm{O}_{1}\end{array}\right]&\xrightarrow{\quad}&\mathrm{O}\mathrm{~R}\mathrm{~T}\mathrm{O}\\\left[\begin{array}{c}\mathrm{R}\mathrm{T}\mathrm{O}_{2}\\\mathrm{O}_{2}\mathrm{~R}\mathrm{T}\mathrm{O}_{1}\end{array}\right]&\xrightarrow{\quad}&\mathrm{O}\mathrm{~R}\mathrm{~0}\mathrm{~T}\\\left[\begin{array}{c}\mathrm{R}\mathrm{O}_{1}\mathrm{R}\mathrm{O}_{2}\\\mathrm{O}_{2}\mathrm{~R}\mathrm{T}\mathrm{O}_{1}\end{array}\right]&\xrightarrow{\quad}&\mathrm{O}\mathrm{~R}\mathrm{~0}\mathrm{~T}\mathrm{O}\end{array} $$

Let us now find the number of ways of rearranging the letters of the word INSTITUTE. In this case there are 9 letters, in which I appears2 times and T appears 3 times.



Temporarily, let us treat these letters different and name them as $\mathrm{I}_{1},\mathrm{I}_{2},\mathrm{T}_{1},\mathrm{T}_{2},\mathrm{T}_{3}$ Thenumberof permutationsof9 diferent etersinthiscase,takenall at time is 9!.Consider one such permutation, say,$\mathrm{I}_{1}\mathrm{NT}_{1}\mathrm{SI}_{2}\mathrm{T}_{2}\mathrm{UET}_{3}$ Here $ if\mathrm{I}_{1},\mathrm{I}_{2}$ are not same  and $\mathrm{T}_{1},\mathrm{T}_{2},\mathrm{T}_{3}$ are not same, then $ I_{1},I_{2}$ can be arranged in 2! ways and $\mathrm{T}_{1},\mathrm{T}_{2},\mathrm{T}_{3}$ can be arranged in 3! ways. Therefore,$2!\times3!$ permutations will be just the same permutation corresponding to this chosen permutation $\mathrm{I_{1}N T_{1}S I_{2}T_{2}U E T_{3}}$ . Hence, total number of different permutations will be $\frac{9!}{2!3!}$ 



We can state (without proof) the following theorems:

Theorem 3 The number of permutations of n objects, where p objects are of the same kind and rest are all $\mathrm{different}=\frac{n!}{p!}$ o 

In fact, we have a more general theorem.

Theorem 4 The number of permutations of n objects, where $p_{1}$ obj ,kind,kind is ,$p_{2}$ $\frac{n!}{p_{1}!p_{2}!\ldots p_{k}!}$ are of second kind,$...,p_{k}$ a of $$ thet,Ta 

Solution Here,there are9objects (letters)ofwhichthere are 4A's,2L's and rest are 

all different.



Therefore, the requied numbr of arrang $\frac{9!}{4!2!}=\frac{5\times6\times7\times8\times9}{2}=7560$ 

Example 10 How many 4-digit numbers can be formed by using the digits 1 to 9 if repetition of digits is not allowed?



Solution Here order matters for example 1234 and 1324 are two different numbers.Therefore, there will be as many 4 digit numbers as there are permutations of 9 different digits taken 4 at a time.



Therefore, the required 4 digit numbers ${}^{9}P_{4}=\frac{9!}{(9-4)!}=\frac{9!}{5!}=9\times8\times7\times6=3024.$ 

Example 11 How many numbers lying between 100 and 1000 can be formed with the digits 0, 1, 2,3,4,5, if the repetition of the digits is not allowed?

Solution Every number between 100 and 1000 is a 3-digit number. We, first, have to 

countthemutooaktimTiumber woulde $^6\mathrm{P}_{3}$ . But,these permutations will include those also where 0is at the100's place.For example,$092,042,\ldots,$ etc are such numbers which are actually 2-digit numbers and hence the number of such numbers has to be subtracted from $^6\mathrm{P}_{3}$ to get the required numbe. To get the number of such numbers, we fix 0 at the's place and rearrange the remaining 5 digits taking 2 at a time. This number is $^{5}\mathrm{P}_{2}$ . So 

$$\begin{aligned}&The required number\quad&={}^{6}P_{3}-{}^{5}P_{2}=\frac{6!}{3!}-\frac{5!}{3!}\\ &\quad&=4\times5\times6-4\times5=100\\ \end{aligned} bnshed $$

Example 12 Find the value of n such that 

$$\mathrm{(i)}\quad\mathrm{P}_{5}=42\mathrm{~P}_{3},\quad n>4\quad\mathrm{(ii)}\quad\frac{\mathrm{P}_{4}}{n-1}\mathrm{P}_{4}=\frac{5}{3},\quad n>4 以\mathrm{(i)}\quad\mathrm{P}_{5}=42\mathrm{~P}_{3},\quad n>4\quad\mathrm{(ii)}\quad\frac{\mathrm{P}_{4}}{n-1}\mathrm{P}_{4}=\frac{5}{3},\quad n>4 h-st θ$$

Solution (i) Given that 

or 

Since 

$$C bnshed \begin{array}{l}{}^{n}\mathrm{P}_{5}=42{}^{n}\mathrm{P}_{3}\\n\left(n-1\right)(n-2)(n-3)(n-4)=42n(n-1)(n-2)\\n>4\quad\text{so}n(\underline{n}-1)(n-2)\neq0\end{array}$$

Therefore, by dividing both sides by $n(n-1)(n-2)$ , we get 

or 

or 

or 

or 

or 

$$\begin{cases}(n-3(n-4))=42\\n^2-7n-30=0\\n^2-10n+3n-30\\(n-10)(n+3)=0\\n-10=0or\quad n+3=0\\n=10\quad or\quad n=-3\end{cases}$$

As n cannot be negative, so $n=10$ 

$$\mathrm{Given that}\frac{^nP_4}{^{n-1}P_4}=\frac{5}{3}$$

Therefore 

or 

or 

$$\begin{aligned}&3n\;(n-1)\;(n-2)\;(n-3)=5(n-1)\;(n-2)\;(n-3)\;(n-4)\\&3n=5\;(n-4)\qquad\left[\asymp(n-1)\;(n-2)\;(n-3)\neq0,n>4\right]\\&\quad n=10.\\ \end{aligned}$$

Example 13 Find r, if $5^{4}P_{r}=6^{5}P_{r-1}$ 

Solution We have 5$^4\mathrm{P}_{r}=6^{5}\mathrm{P}_{r-1}$ 

$$\begin{array}{ll}{{\mathrm{cor}}}&{{\begin{array}{l}{{5\times\cfrac{4!}{\left(4-r\right)!}=6\times\cfrac{5!}{\left(5-r+1\right)!}}}\\ {{5\times\cfrac{5!}{\left(4-r\right)!}=\cfrac{6\times5!}{\left(5-r+1\right)\left(5-r\right)\left(5-r-1\right)!}}}\end{array}}}\\ {{\mathrm{cor}}}&{{\begin{array}{l}{{\cfrac{5!}{\left(4-r\right)!}=\cfrac{6\times5!}{\left(5-r+1\right)\left(5-r\right)\left(5-r-1\right)!}}}\\ {{\mathrm{cor}}}\\ {{\mathrm{cor}}}\\ {{\mathrm{cor}}}\\ {{\mathrm{cor}}}\\ {{\mathrm{cor}}}\\ {{\mathrm{cor}}}\\ {{\mathrm{cor}}}\\ {{\mathrm{cor}}}\\ {{\mathrm{cor}}}\\ {{\mathrm{cor}}}\\ {{\mathrm{Hence}}}\end{array}}}\end{array}$$

Example14 Find the number of different8-letter arrang ished that can be made from the letters of the word DAUGHTER so that 

(i)all vowels occur together all yowels do notoccurtogether.

Solution (i) There are 8 different letters in the word DAUGHTER, in which there are 3 vowels, namely, A, U and E. Since the vowels have to occur together, we can for the time being, assume them as a single object (AUE).This single object together with 5 remaining letters (objects) will be counted as 6 objects. Then we count permutations of these 6 objects taken all at a time. This number would be ${}^{6}\mathrm{P}_{6}=6!$ . Corresponding to each of these permutations, we shall have 3! permutations of the three vowels A, U, E taken all at a time . Hence, by the multiplication principle the required number of permutati $\mathrm{ions}=6!\times3!=4320$ 



(ii) If we have to count those permutations in which all vowels are never together, we first have to find all possible arrangments of 8 letters taken all at a time,which can be done in 8! ways. Then, we have to subtract from this number, the number of permutations in which the vowels are always together.



$${\begin{array}{rl}{{\mathrm{Therefore}}_{*}{\mathrm{~t h e~t e q u i r e d~n u m b e r~}}}&{8!-6!\times3!=}&{6!(7\times8-6)}\\ {}&{=}&{2\times6!(28-3)}\\ {}&{=}&{50\times6!=50\times720=36000}\end{array}}$$

Example 15 In how many ways can 4 red, 3 yellow and 2 green discs be arranged in a row if the discs of the same colour are indistinguishable ?

Solution Total number of discs are $4+3+2=9$ . Out of 9 discs, 4 are of the first kind 

(red), 3 areofthe secondkind(yellow) and2 areofthethirdkind (gren)

Therefore, the number of arrangements $\frac{9!}{4!3!2!}=1260$ 

Example 16 Find the number of arrangements of the letters of the word INDEPENDENCE. In how many of these arrangements,

(i) do the words start with P 

(ii) do all the vowels always occur together 

(i) do the vowels never occur together 

(iv) do the words begin with I and end in P?

Solution There are 12 letters, of which N appears 3 times,E appears 4 times and appears 2 times and the rest are all different. Therefore 

The required number of arrangements $\frac{12!}{3!4!2!}=1663200$ 

(i))Let us fix P at the extreme let position, we,then, count the arrangements of the remaining1 ltrs.Therefore,the required umber of words starting wih P 

$$\frac{11!}{3!2!4!}=138600$$

(ii)There are 5 vowels in the given word, which are 4 Es and 1 I. Since, they have to always occur together, we treat them as a single object EEEI for the time being. This single object together with 7 remaining objects will account for 8objects. These 8 objects, in which there are 3Ns and 2 Ds, can be rearranged in 

$$ 



−ways. Corresponding to ach of these arrangements, the5 vowels E, E, E,

E and I can be rearranged in $\frac{5!}{4!}$ ways. Therefore, by multiplication principle.the required number of arrangements 



$$\frac{8!}{3!2!}\times\frac{5!}{4!}=16800$$

(i)The required number of arrangements 

$=\mathrm{the}$ total number of arrangements (without any restriction) – the number of arrangements where all the vowels occur together.

$$1663200-16800=1646400(iv)LetusfixIandPattheextremeends (IattheleftendandPattherightend).$$

(iv)LetusfixIandPattheextremeends (IattheleftendandPattherightend).We are left with 10 letters.



Hence, the required number of arrangements 

$$\frac{10!}{3!2!4!}=12600$$

### EXERCISE 6.3

1. How many 3-digit numbers can be formed by using the digits 1 to 9 if no digit is repeated?



2.How many 4-digit numbers are there with no digit repeated?

3.How many 3-digit even numbers can be made using  the digits 1, 2, 3,4, 6,7, ifno digit is repeated?



4.Find the number of 4-digit numbers thatcan be formed using the digits 1,2,3, 4,5 if no digit is repeated. How many of these will be even?

5. From a committee of 8 persons, in how many ways can we choose a chairman and a vice chairman assuming one person can not hold more than one position?6.Find n $\mathrm{if}^{n-1}P_{3}:^{n}P_{4}=1$ 



7. Find r if (i)$^5\mathrm{P}_{r}=2^{6}\mathrm{P}_{r-1}\quad(\mathrm{ii})^{5}\mathrm{P}_{r}=^{6}\mathrm{P}_{r}$ 

8.How many words, with or without meaning,can be formed using allthe letters of the word $\mathrm{EQUATION}$ using each letter exactly once?

9. How many words, with or without meaning can be made from the letters of the word MONDAY, assuming that no letter is repeated, if.

(i)4 letters are used at a time,(ii) all letters are used at a time,

(i) all letters are used but first letter is a vowel?

10. In how many of the distinct permutations of the letters in MISSiSSIPPI do the four I's not come together?



11.In how many ways can the letters of the word PERMUTATIONS be arranged if the (i) words start with P and end with S,(i) vowels are all together,

(ii) there are always 4 letters between P and S?

### 6.4 Combinations 

Let us now assume that there is a group of 3 lawn tennis players X, Y, Z. A team consisting of 2 players is to be formed. In how many ways can we do so? Is the team of X and Y different from the team ofY and X ? Here, order is not important.In fact, there are only 3 possible ways in which the team could be constructed. <div style="text-align: center;"><img src="imgs/img_in_image_box_97_141_851_276.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">Fig. 6.3</div>


These are XY, YZ and ZX (Fig 6.3).

Here,each selectioniscalledcombinationof3diferentobjectstaken2at time.In a combination, the order is not important.



Now consider some more illustrations.

Twelve persons meet in a room and each shakes hand with all the others. How do we determine the number of hand shakes. X shaking hands with Y and Y with X will not be two different hand shakes. Here, order is not important. There will be as many hand shakes as there are combinations of 12 different things taken2 at a time.

Seven points lie on a circle. How many chords can be drawn by joining these points pairwise? There will be asmanychordsas therearecombinationof7diferent things taken 2 at a time.



Now, we obtain the ormula or finding the umber ofcombinations o dferent objects taken r at a time, denoted by "C_



Suppose we have 4 dfferent objects A,$B.@\mathrm{andD}$ .Taking 2 at a time, if we have to make combiins,te ill b BC,,, D, D.Hre,B and A are the same combination as order does not alter the combination. This is why we have not included BA, CA, DA, CB,DB and DC in this list. There are as many as 6 combinations of 4 different objects taken2 at a time, ie.,$^{4}C_{2}=6$ 



Corresponding toach combination in the listwe can arrive at2! permutations as 2 objects in each combination can be rearranged in 2! ways. Hence, the number of 

$\mathrm{permutations}={^{4}C_{2}}\times2!$ 



On the other hand,the number of permutations of 4 different things taken 2 at a1$\mathrm{time}={^{4}\mathrm{P}_{2}}$ 



Therefore 

$$^4\mathrm{P}_{2}=^{4}\mathrm{C}_{2}\times2!\quad\mathrm{or}\quad\frac{4!}{(4-2)!2!}=^{4}\mathrm{C}_{2}$$

Now, let us suppose that we have 5 different objects A, B, C, D, E. Taking 3 at a time, if we have to make combinations, these will be ABC, ABD, ABE, BCD, BCE,CDE, ACE,ACD, ADE, BDE. Corresponding to each of these $^{5}\mathrm{C}_{3}$ combinations, there are 3! permutations, because, the three objects in each combination can be  rearranged in 3! ways. Therefore, the total of permutations $t={}^{5}C_{3}\times3!$ 

$$Therefore\quad^{5}\mathbf{P}_{3}=^{5}\mathbf{C}_{3}\times3!\quad or\quad\frac{5!}{(5-3)!3!}=^{5}\mathbf{C}_{3}$$

These examples suggest the following theorem showing relationship between permutaion and combination:

Theorem ${}^{5}\mathrm{P}_{r}={}^{n}\mathrm{C}_{r}\quad r!,\quad0<r\leq n.$ 

Proof ${}^{n}\mathrm{C}_{r},$ we haver!ermutations,cause Ta 

is $^{n}\mathrm{C}_{r}\times r!$ He . On the other hand, it is $^{n}\mathbf{P}_{r}$ . Thus tain  thns tn r a atime 

$${}^{n}\mathrm{P}_{r}={}^{n}\mathrm{C}_{r}\times r!,0<r\leq n.$$

Remarks s1.Fromabove $$ 

In particular, if $r=n$ ${}^{n}\mathrm{C}_{n}=\frac{n!}{n!0!}=1$ 

2.We define $^{n}\mathrm{C}_{0}=1,\mathrm{i.e.}$ , the number of combinations of n different things taken nothing at l is considered to be 1.Counting combinations is merely counting the number of ways in which some or all objects at a time are selected. Selecting nothing at all is the same as leaving behind all the objects and we know that there is only one way of doing so. This way we define $^{n}C_{0}=1$ 

3.As $\frac{n!}{0!(n-0)!}=1=C_{0}$ , the formula ${}^{n}\mathrm{C}_{r}=\frac{n!}{r!(n-r)!}$ is applicable for $r=0$ also.

Hence 

$$\bar{C}_{r}=\frac{n!}{r!(n-r)!},0\leq r\leq n.$$

4.

$${}^{n}C_{n-r}=\frac{n!}{(n-r)!(n-(n-r))!}=\frac{n!}{(n-r)!r!}={}^{n}C_{r},$$

i.e., selecting  objects out of n objects is same as rejecting $(n-r)$ objects.

5.${}^{n}\mathrm{C}_{a}={}^{n}\mathrm{C}_{b}\Rightarrow a=b or a=n-b,i.e.,n=a+b$ 

Theorem ${}^{\mathrm{~\scriptsize~\mathcal~{~G~}~}}{}^{n}\mathrm{C}_{r}+{}^{n}\mathrm{C}_{r-1}={}^{n+1}\mathrm{C}_{r}$ 

$$\begin{aligned}\mathrm{We}\quad\mathrm{have}\quad\mathrm{e}^{n}\mathrm{C}_{r}+\mathrm{e}^{n}\mathrm{C}_{r-1}=\frac{n!}{r!(n-r)!}+\frac{n!}{(r-1)!(n-r+1)!}\\ =\frac{n!}{r\times(r-1)!(n-r)!}+\frac{n!}{(r-1)!(n-r+1)(n-r)!}\\ =\frac{n!}{(r-1)!(n-r)!}\left[\frac{1}{r}+\frac{1}{n-r+1}\right]\\ =\frac{n!}{(r-1)!(n-r)!}\times\frac{n-r+1+r}{r(n-r+1)}=\frac{(n+1)!}{r!(n+1-r)!}=\mathrm{e}^{n+1}\mathrm{C}_{r}.\end{aligned} shed nub.$$

Example 17 If ${}^{n}\mathrm{C}_{9}={}^{n}\mathrm{C}_{8}$ ,find find $$ 仅

Solution We have $$ −

i.e.,

or 

$$nub.\frac{n!}{9!(n-9)!}=\frac{n!}{(n-8)!8!}\quad 和 \quad n=9\quad or\quad n=17$$

Therefore ${}^{n}\mathrm{C}_{17}={}^{17}\mathrm{C}_{17}=1$ 

Example 18 A committee of 3 persons is to be constituted from a group of 2 men and 3 women. In how many ways can this be done? How many of these committees would consist of 1 man and 2 women?



Solution Here, order does not matter. Therefore, we need to count combinations.There will be as many committees as there are combinations of 5 different persons taken 3 at a time. Hence, the required number of w $\mathrm{ays}={}^{5}\mathrm{C}_{3}=\frac{5!}{3!2!}=\frac{4\times5}{2}=10$ 

Now, 1 man can be selected from 2 men in (cid)${}^{2}\mathrm{C}_{1}$ ways and 2 women can be selected from 3 women in $^{3}C_{2}$ ways. Therefore,the required number of committees  $${}^{2}C_{1}\times{}^{3}C_{2}=\frac{2!}{1!1!}\times\frac{3!}{2!1!}=6$$

Example19 What is the number of ways of choosing 4 cards from a pack of 52playing cards? In how many of these 



(i)four cards are of the same suit,

(ii) four cards belong to four different suits,

(i)  are face cards,

(iv) two are red cards and two are black cards,

(v) cards are of the same colour?

combinations of 52 different things, taken 4 at a time. Therefore  



The required number of $$ c 

(i)There arefoursuits:diamond,club,spade,heartandtherear13cardsofeach suit. Therefore, there are $^{13}\mathrm{Cways}$ of choosing 4 diamonds. Similarly, there are $^{13}C_{4}$ ways of choosing 4 clubs,$\bar{^{13}}C_{4}$ ways of choosing 4 spades and $^{13}C_{4}$ ways of choosing 4 hearts. Therefore 



The required number of ways $^{43}C_{4}+^{13}C_{4}+^{13}C_{4}+^{13}C_{4}$ 

$$4\times\frac{13!}{4!9!}=2860$$

(ii) There are13 cards in each suit.

Therefore, there $\mathrm{are}^{-3}\mathrm{C}_{\mathrm{p}}$ ways of choosing 1 card from 13 cards of diamond.$^{13}C_{1}$ ways of choosing 1 card from 13 cards of hearts,$^{13}\mathrm{C}_{1}$ ways of choosing 1card from 13 cards of clubs,$^{13}\mathrm{C}_{1}$ ways of choosing 1 card from 13 cards of spades. Hence, by multiplication principle, the required number of ways 

$$={}^{13}C_{1}\times{}^{13}C_{1}\times{}^{13}C_{1}\times{}^{13}C_{1}=13^{4}$$

(i)Thereare12facecardsand4aretobeselectedoutofthese12cardsThiscab done in $^{12}\mathrm{C}_{4}\mathrm{ways}$ . Therefore, the required number of $\mathrm{ways}=\frac{12!}{4!8!}=495$ 

(iv) There are 26 red cards and 26 black cards. Therefore, the required number of 

$\mathrm{ways}=\mathrm{^{26}C_{2}}\times\mathrm{^{26}C_{2}}$ 



$$\left(\frac{26!}{2!24!}\right)^{2}=\left(325\right)^{2}=105625$$

(v) 4 red cards can be selected out of 26 red cards in ${}^{26}C_{4}$ ways.4 black cards can be selected out of 26 black cards in $^{26}C_{4}ways$ 

Therefore, the required number of way $s={}^{26}C_{4}+{}^{26}C_{4}$ 

$$2\times\frac{26!}{4!22!}=29900 lished $$

## EXERCISE 64

1.If ${}^{n}\mathrm{C}_{8}={}^{n}\mathrm{C}_{2},$ ,find ${}^{n}\mathrm{C}_{2}$ 

2.Determine n if 

(i)$^{2n}C_{3}:^{n}C_{3}=12:1$ 

(ii)

$$^{2n}C_{3}:^{n}C_{3}=11:1 lished $$

3.How many chords can be drawn th hrough 21 poinn a circle?

In how many ways can a team of 3 boys and 3 girls be selected from 5 boys and 4 girls?



5.Findtheumboobllomll,tblln blue balls if each selection consists of 3 balls of each colour.

6.Determine the number of 5 card combinations out of a deck of 52 cards if there is exactly one ace in each combination.



7.In how many ways can one select a cricket team of eleven from 17 players in which only 5 players can bowl if each cricket team of 1l must include exactly 4bowlers?



8.A bag contains 5 black and 6 red balls. Determine the number of ways in which 2 black and 3 red balls can be selected.



9.In how many ways can a student choose a programme of 5 courses if 9 courses are available and 2 specific courses are compulsory for every student?

## Miscellaneous Examples 

Example 20 How many words, with or without meaning, each of 3 vowels and 2consonants can be formed from the letters of the word INVOLUTE ?

SolutionIn the word INVOLUTE, there are 4 vowels, namely, I,O,E,Uand 4consonants, namely, N, V, L and T.



The number of ways of selecting 3 vowels out of $4={}^{4}C_{3}=4$ 

The number of ways of selecting 2 consonants out of $4={}^{4}C_{2}=6$ 

Therefore, the number of combinations of 3 vowels and 2 consonants is 

$4\times6=24$ 



Now, eachofthese24 combinations has5 letters whichcan bearranged among themselves in 5! ways. Therefore, the required number of different words is 

$24\times5:2880$ 



Example 21 A group consists of 4 girls and 7 boys. In how many ways can a team of 5 members be selected if the team has (i) no girl? (ii) at least one boy and one girl ?(iii) at least 3 girls ?



Solution (i) Since, the team will not include any girl, therefore, only boys are to be selected. 5 boys out of 7 boys can be selected in $^7\mathrm{C}_{5}$ ways. Therefore, the required number of ways ${}^{7}C_{5}=\frac{7!}{5!2!}=\frac{6\times7}{2}=21$ 

(ii)Since, at least one boy and one girl are to be there in every team. Therefore, the team can consist of 



(a) 1 boy and 4 girls (b)  2 boys and 3 girls 

(c) 3 boys and 2 girls (d) 4 boys and 1 grl.

1 boy and 4 girls can be selected in $\mathrm{e}_{1}\times\mathrm{^{4}C_{4}}$ ways.

2 boys and 3 girls can be selected in ${}^{7}\mathrm{C}_{2}\times{}^{4}\mathrm{C}_{3}$ ways.

3 boys and 2 girls can be selected in ${}^{7}\mathrm{C}_{3}\times{}^{4}\mathrm{C}_{2}$ ways.

4 boys and 1 girl can be selected in $^{7}\mathrm{C}_{4}\times^{4}\mathrm{C}_{1}$ ways.

Therefore, the required number of ways 

$$\begin{aligned}&={}^{7}C_{1}\times{}^{4}C_{4}+{}^{7}C_{2}\times{}^{4}C_{3}+{}^{7}C_{3}\times{}^{4}C_{2}+{}^{7}C_{4}\times{}^{4}C_{1}\\ &=7+84+210+140=441\\ \end{aligned}$$

(ii) Since, the team has to consist of at least 3 girls, the team can consist of (a) 3 girls and 2 boys, or(b) 4 girls and 1 boy.

Note that the team cannot have all 5 girls, because, the group has only 4 girls.

3 girls and 2 boys can be selected in ${}^{4}\mathrm{C}_{3}\times{}^{7}\mathrm{C}_{2}$ ways.

4 girls and 1 boy can be selected in ${}^{4}\mathrm{C}_{4}\times{}^{7}\mathrm{C}_{1}$ ways.

Therefore, the required number of ways 

$${}^{4}C_{3}\times{}^{7}C_{2}+{}^{4}C_{4}\times{}^{7}C_{1}=84+7=91$$

Example22 Find the number of words withor without meaning which can be made using all the ltersofhe word AGAIN.Ifthese wordsare writnasin adictionary,what will be the $50^{\mathrm{th}}$ word?



Solution Threare5rsintewordAGAIN, inwhichAppars2time.Therefore,the required number of $\mathrm{words}=\frac{5!}{2!}=60$ 



To get the number of words starting with A, we fix the letterA at the extreme left position, wethenrearrangetheremaining4 letterstakenall at atime.There will be as many arrangementsofthese4 leterstaken4at atime as therearepermutations of 4different things taken 4 at a time. Hence, the number of words starting with $A=4!=24$ . Then, starting with G, the number $\mathrm{of}\mathrm{words}=\frac{4!}{2!}=12\mathrm{as}$ after placing G at the extreme left position, we are left with the eters A,A,I and N.Similarly, there are 12 words starting with the next letter I. Total numberof words so far obtained 

$24+12+12=48$ 



The 49th word is NAAGI. The 50th word is NAAIG.

Example 23 How many numbers greater than 1000000 can be formed by using the digits 1,2,0,2, 4,2,4?



Solution i-diitumbdtumrofdiitstobedisalso 7.Therefore,the numbers tobecounted will be 7-digit only.Al, the numbers have to be greater than 100000, so they can begin either with 1, 2 or 4.

The number of numbers beginning with $\frac{6!}{3!2!}=\frac{4\times5\times6}{2}=60$ , as when 1 is fi tl,4, 4, in which there are 3, 2s and 2, 4s.



Total numbers begining with 2

$$\frac{6!}{2!2!}=\frac{3\times4\times5\times6}{2}=180$$

and total numbers begining with $4=\frac{6!}{3!}=4\times5\times6=120$ 

Therefore, the required number of numbers $60+180+120=360$ 

## Alternative Method 

The number of 7-digit arrangements, clearly,$\frac{7!}{3!2!}=420$ .But, this will include those numbers also,whichhave0at the extreme left position. The numberof such arrangements $\frac{6!}{3!\;2!}$ (by fixing 0 at the extreme left $\mathrm{position}=60$ 

Therefore, the required number of $\mathrm{numbers}=420-60=360$ 

Note Ifoneormorethanonedigitsgiveninthelistisrepeateditwillb understood that in any number, the digits can be used as many times as is given in the list,e.g,intheaboveexample1and0canbeusedolyoncewhereas2and 4can be used 3 times and 2 times, respectively.



Example24Inhow many ways can5girls and3boysbe seated in arow so that no two boys are together?



Solution Let us first seatthe5 girls.This can be donein 5! ways.Foreach such arrangement, the three boys can be seated only at the cross marked places.

$$\times\mathrm{G}\times\mathrm{G}\times\mathrm{G}\times\mathrm{G}\times $$

$^6\mathrm{P}_{3}$ ways.Hence, by multiplication principle, the total number of ways 

$$\begin{array}{l}=5!\times{}^{6}\mathrm{P}_{3}=5!\times\frac{6!}{3!}\\=4\times5\times2\times3\times4\times5\times6=14400.\end{array}$$

## Miscellaneous Exercise on Chapter 6

1. How many words, with or without meaning, each of2 vowels and 3 consonants can be formed from the letters of the word DAUGHTER ?

2. How many words, with or without meaning, can be formed using all the letters of the word EQUATION at a time so that the vowels and consonants occur together?3. A committee of 7 has to be formed from 9 boys and 4 girls. In how many ways can this be done when the committee consists of:

(i)exactly 3 girls? (ii) atleast 3 girls? (ii) atmost 3 girls?

4. If the different permutations of all the letter of the word EXAMINATION are 

listed as in a dictionary, how many words are there in this list before the first word starting with E?



5.How many 6-digit numbers can be formed from the digits 0, 1,3, 5,7 and 9which are divisible by 10 and no digit is repeated ?



6.The English alphabet has 5 vowels and 21 consonants. How many words with two different vowels and 2 different consonants can be formed fromthe alphabet ?



7.In an examination, a question paper consists of 12 questions divided into two parts i.e.,Part I andPartI, containing 5 and7 questions,respectively. Astudent is required to atempt 8 questions in all,selecting at least3from each part. In a how many ways can a student select the questions ?



8.Deermi Ta selection of 5 cards has exactly one king.



t a even places. How many such arrangements are possible ?

10.Fmasofu are 3 students who decide that either all of them will join or none of them will join. In how many ways can the excursion party be chosen ?

11. In how many ways can the letters of the word ASSASSINATION be arraned so that all the S's are together ?



## Summary 

ways, following which another event can occur in n different ways, then the total number of occurrence of the events in the given order is $m\times n$ 

The number of permutations of n different things taken r at a time, where 司

repetition is not allowed, is denoted by ${}^{n}\mathrm{P}_{n}$ and is given by $$ where $0\leq r\leq n$ 





$n!=1\times2\times3\times\ldots\times n$ 



$n!=n\times(n-1)!$ 

The number of permutations of n different things, taken r at a time, where repeatition is allowed, is $n^{r}$ 



Theumrl c $p_{1}$ objects 

are of first kind,$p_{2}$ ojts…$p_{k}$ objects are of the $k^{\mathrm{th}}$ kind and rest, if any, are all differet is $\frac{n!}{p_{1}!p_{2}!..p_{k}!}$ 



Theu ${}^{n}\mathrm{C}_{r}$ , is given by ${}^{n}\mathrm{C}_{r}=\frac{n!}{r!(n-r)!},0\leq r\leq n.$ 



## Historical Note 

<div style="text-align: center;"><img src="imgs/img_in_image_box_824_414_894_484.jpg" alt="Image" width="7%" /></div>


T of Jainism in India and perhaps even earlier. The credit Jains whotreated itssubject matteras a self-contained topicin mathematics,under the name Vikalpa.



AmongtheJainsMah the world's first mathematician credited with providing the general formulae for permutatios and combinations.



In the 6th century B.C., Sushruta, in his medicinal work, Sushruta Samhta,asserts that63combinationscan bemadeoutof6different tastes, takenone at a time, two at a time, etc. Pingala,a Sanskrit scholar around third century B.C.,gives the method of determining the number of combinations ofa given number of letters, taken one at a time, two at a time,etc.in his work Chhanda Sutra.Bhaskaracharya (born 1114)treated the subject matter of permutations and combinationsunderthenameAnkaPashainhisamousworkLilavati.Inaddition tothegeneral formulae for"C and ${}^{n}\mathrm{P}_{n}$ already provided by Mahavira,Bhaskaracharya gives several important theorems and results concerning the subject.



Outside India,thesubject matterof permutations andcombinations had its humble beginnings in China in the famous book I–King (Book of changes). It is difficultoiw.or hadrdelbdiotaly was not completely carried out.Greeks and later Latin writers also did some scattered work on the theory of permutations and combinations.Y 

Some Arabic and Hebrewwriters used theconceptsof permutations and combinations instudyingastronomRai $\bar{E}zra$ for instance, determined the number of combinations of known planets takentwo at a time, thre at a time and so on. This was around 1140.It appears that Rabbi ben Ezra did not kow  the formula for ${}^{n}\mathrm{C}_{n}$ . However, he was aware that ${}^{n}\mathrm{C}_{r}={}^{n}\mathrm{C}_{n-r}$ for specific values n and r.In1321,Levi Ben Gerson, another Hebrew writer came up with the formulae for CICeIOI $$ and the general formula for ${}^{n}\mathrm{C}_{n}$ 

EM 

permutationsandcombinationsis Ars ConjectandiwrittenbyaSwiss, Jacob Bernoulli(1654–1705),posthumously publishedin1713.Thisbookcontains essentialythethoryofpermutationsandcombinationsas isknown today.

<div style="text-align: center;"><img src="imgs/img_in_image_box_115_394_859_1136.jpg" alt="Image" width="79%" /></div>
