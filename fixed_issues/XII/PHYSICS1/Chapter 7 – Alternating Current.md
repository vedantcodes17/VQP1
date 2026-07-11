

# Chapter Seven  ALTERNATING  CURRENT blished 

## (cd:1)

T sources. These currents do not change direction with time. But voltages and currents that vary with time are very common. The electric mains supply in our homes and offices is a voltage that varies like a sine function with time. Such a voltage is called alternating voltage (ac voltage) and the current driven by it in a circuit is called the alternating current (ac current)*. Today, most of the electrical devices we use require ac voltage.This is mainly because most of the electrical energy sold by power companies is transmitted and distributed as alternating current. The main reason for preferring use of ac voltage over dc voltage is that ac voltages can be easily and efficiently converted from one voltage to the other by means of transformers. Further, electrical energy can also be transmitted economically over long distances. AC circuits exhibit characteristics which are exploited in many devices of daily use. For example, whenever we tune our radio to a favourite station, we are taking advantage of a special property of ac circuits – one of many that you will study in this chapter.

<div style="text-align: center;"><img src="imgs/img_in_image_box_126_213_405_498.jpg" alt="Image" width="22%" /></div>


Nicola Tesla (18561943)Serbian -American scientist,inventor and genius.He conceived the idea of the rotating magnetic field,which is the basis of practically all alternating current machinery,and which helped usher in the age of electric power.He also invented among other things the induction motor,the polyphase system of ac power,and the high frequency induction coil (the Tesla coil)used in radio and television sets and other electronic equipment.The SI unit of magnetic field is named in his honour.

### 7.2 AC VOLTAGE APPLIED TO A RESiSTOR 

Figure 7.1 shows a resistor connected to a source ε of ac voltage. The symbol for an ac source in a circuit diagram is . We consider a source which produces sinusoidally varying potential difference across its terminals. Let this potential difference, also called ac voltage, be given by 



$$v=v_{m}\sin\omega t is the amplitude of the oscillating potential $$

where $\upsilon_{m}$ is the amplitude of the oscillating potential difference and ω is its angular frequency.angular fquncy 

<div style="text-align: center;"><img src="imgs/img_in_image_box_566_479_1042_719.jpg" alt="Image" width="38%" /></div>


<div style="text-align: center;"> FIGURE 7.1 AC voltage applied to a resistor.</div>


To find the value of current through the resistor, we apply Kirchhoff s loop rule $\sum\varepsilon(t)=0$ (refer to Section 3.12), to the circuit shown in Fig. 7.1 to get 

$$v_{m}\sin\omega t=i R $$

$$i=\frac{v_m}{R}\sin\omega t $$

Since Ris a constant, we can write this equation as 

$$i=i_{m}\sin\omega t $$

<div style="text-align: center;"><img src="imgs/img_in_image_box_64_1080_382_1311.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">FIGURE 7.2 In a pure resistor, the voltage and current are in phase. The minima, zero and maxima occur at the same respective times.</div>


where the current amplitude $i_{m}$ is given by 

$$i_{m}=\frac{v_{m}}{R}$$

Equation (7.3) is Ohm's law, which for resistors, works equally well for both ac and dc voltages. The voltage across a pure resistor and the current through it, given by Eqs. (7.1) and (7.2) are plotted as a function of time in Fig. 7.2. Note, in particular that both v and i reach zero, minimum and maximum values at the same time. Clearly, the voltage and current are in phase with each other.



We see that, like the applied voltage, the current varies sinusoidally and has corresponding positive and negative values during each cycle. Thus, the sum of the instantaneous current values over one complete cycle is zero, and the average current is zero. The fact that the average current is zero, however, does 

not mean that the average power consumed is zero and that there is no dissipation of electrical energy. As you know,e $i^{2}R$ an depends on $i^{2}$ (which is always positive whether iis positive or negative)and not on i. Thus, there is Joule heating and dissipation of electrical energy when an ac current passes through a resistor.

T 

The instantaneous power dissipated in the resistor is 

$$p=i^{2}R=i_{m}^{2}R\sin^{2}\omega t $$

The average value of p over a cycle is 

$$\stackrel{-}{p}=<i^{2}R>=<i_{m}^{2}R\sin^{2}\omega t>$$

whee      erae value and $<\ldots\ldots>$ denotes taking average of the quantity inside the bracket. Since,$i_{m}^{2}$ and $R$ are constants,

$$\overline{p}=i_m^2R<\sin^2\omega t>$$

and since $1/2\left(1–\cos2\omega t\right)$ $\mathrm{e}<\cos2\omega t>=0^{\frac{1}{2}}$ , we have ion $\mathrm{{:\leq sin^{2}}}$ $\mathrm{e}<\cos2\omega t>=0^{\frac{1}{2}}$ ω$$ identity,ave,tity,$$ 

$$<\sin^{2}\omega t>=\frac{1}{2}$$

Thus,

$$\stackrel{-}{p}=\frac{1}{2}i_m^2R $$

oase pewr $(P=I^{2}R)$ J, a special value of current is defined and used.It is called, root mean square (rms) or effective current (Fig. 7.3) and is denoted by $I_{rms}\bar{o}r I$ 



<div style="text-align: center;"><img src="imgs/img_in_chart_box_266_1006_606_1276.jpg" alt="Image" width="27%" /></div>


<div style="text-align: center;">FIGURE 7.3 The rms current I is related tothe </div>


peak current $i_{m}$ by $I=\dot{i}_{m}/\sqrt{2}=0.707\ \dot{i}_{m}$ ,

$$\cos2\omega t>=\frac{1}{T}\int_{0}^{\tau}\cos2\omega t dt=\frac{1}{T}\left[\frac{\sin2\omega t}{2\omega}\right]_{0}^{\tau}=\frac{1}{2\omega T}\left[\sin2\omega T-0\right]=0$$

<div style="text-align: center;"><img src="imgs/img_in_image_box_838_206_1127_496.jpg" alt="Image" width="23%" /></div>


Y George Westin gh ouse $(\mathbf{1846\mathrm{~-~}1914})$ A leading proponent of the use of technology the He Company alternating he with an current.was current direct founded came advocate Thomas convinced electrical current.was named West into of current the Alva the alternating tin of that after famous future.con flict ghouse Edison,key Thus,direct him over the to and enlisted the services of Nicola Tesla and other inventors in the development of alternating current motors and apparatus for the transmission of high tension current,pioneering in large scale lighting.

It is defined by 

$$\left\{\begin{aligned}I=&\sqrt{\overline{i^{2}}}=\sqrt{\frac{1}{2}i_{m}^{2}}=\frac{i_{m}}{\sqrt{2}}\\ &=0.707i_{m}\end{aligned}\right.$$

In terms of I, the average power, denoted by Pis 

$$P=\overline{p}=\frac{1}{2}i_m^2R=I^2R Similarly, we define the rms voltage or effective voltage by $$

Similarly, we define the rms voltage or effective voltage by shed 

$$V=\frac{v_m}{\sqrt{2}}=0.707v_m $$

From Eq. (7.3), we have 

$$v_{m}=i_{m}R $$

or,

$$\frac{v_{m}}{\sqrt{2}}=\frac{i_{m}}{\sqrt{2}}R $$

or,E 

01,$$ n.)    and is similar to that in the dc case. This shows the advantage of introducing the concept of rms values. In terms of rms values, the equation for power7.] and enurnt nd e in a ircuits  i     



example, the household line voltage of 220 V is an rms value with a peak voltage of 



$$v_{m}=\sqrt{2}\ V=(1.414)(220\ V)=311\ V In fact, the I or rms current is the equivalent dc current that would $$



$v_{m}=\sqrt{2}\ V=(1.414)(220\ V)=311\ V$ 

In fact, the I or rms current is the equivalent dc current that would produce the same average power loss as the alternating current. Equation (7.7) can also be written as 



$$(7.7) can also be written as P=V^{2}/R=I V\quad(since V=IR)$$

Example 7.1 A light bulb is rated at 100W for a 220V supply. Find (a) the resistance of the bulb; (b) the peak voltage of the source; and (c) the rms current through the bulb.



## Solution 

(a) We are given $P=100\mathrm{~W~}$ and $V=\:220\:\mathrm{~V~}$ .Theresistance ofthe bulb is 



$$R=\frac{V^{2}}{P}=\frac{(220V)^{2}}{100W}=484\Omega $$

(b) The peak voltage of the source is 

$$v_{\mathrm{m}}={\sqrt{2}}V=311\mathrm{V}$$

(c)Since,$P=I\;V$ 

$$I=\frac{P}{V}=\frac{100W}{220V}=0.454A $$

### 7.3 REPRESENTATION OF AC CURRENT AND VOLTAGE BY ROTaTING VECToRS — PHASORS 

In the previous section, we learnt that the current through a resistor is in phase with the ac voltage. But this is not so in the case of an inductor,

phase relationship betwen voltage and current in an ac circuit, we use the notion of phasors.The analysis of an ac circuit is facilitated by the use of a phasor diagram. A phasor* is a vector which rotates about the origin with angular speed ω, as shown in Fig. 7.4. The vertical components of phasors V and I represent the sinusoidally varying quantities v and i. The e ee e   eee e amplitudes or the peak values $v_{m}$ and $i_{m}$ of these e e ee e ra sr  eee relationship at time $t_{1}$ for the case of an ac source connected to a resistor i.e., corresponding to the circuit shown in Fig. 7.1. The projection of 

$$\omega t_{i} T $$

<div style="text-align: center;"> e  e  ere circuit in Fig 7.1. (b) Graph of v and i versus ωt. </div>


voltage and current phasors on vertical axis,$\mathrm{i}.\mathrm{e}_{\omega},v_{m}\sin\omega t\mathrm{and}i_{m}\sin\omega t,$ respectively represent the value of voltage and current at that instant. As they rotate with frequency ω, curves in Fig. 7.4(b) are generated.

From Fig. 7.4(a) we see that phasors V and I for the case of a resistor are in the same direction. This is so for all times. This means that the phase angle between the voltage and the current is zero.



### 7.4 AC VOLTaGE APpLieD TO AN InDUCTOR 

Figure 7.5 shows an ac source connected to an inductor. Usually,inductors have appreciable resistance in their windings, but we shall Thus, the circuit is a purely inductive ac circuit. Let the voltage across the source be $v=v_{m}$ sinω t. Using the Kirchhoff 's loop rule,$\sum\varepsilon(t)=0$ ,and since there is no resistor in the circuit,

$$v-L\frac{\mathrm{d}i}{\mathrm{d}t}=0$$

where the second term is the self-induced Faraday emf in the inductor; and L is the self-inductance of 

<div style="text-align: center;"><img src="imgs/img_in_image_box_708_1023_1143_1234.jpg" alt="Image" width="35%" /></div>


<div style="text-align: center;">FIGURE 7.5 An ac source connected to an inductor.</div>


the inductor. The negative sign follows from Lenz's law (Chapter 6).Combining Eqs. (7.1) and (7.10), we have 

$$\frac{\mathrm{d}i}{\mathrm{d}t}=\frac{v}{L}=\frac{v_m}{L}\sin\omega t $$

Equation (7.11) implies that the equation for i(t), the current as a function of time, must be such that its slope di/dt is a sinusoidally varying quantity, with the same phase as the source voltage and an amplitude given by $v_{m}/L.$ . To obtain the current, we integrate di/dt with respect to time:

$$\int\frac{\mathrm{d}i}{\mathrm{d}t}\mathrm{d}t=\frac{v_m}{L}\int\sin(\omega t)\mathrm{d}t $$

and get,

$$i=-\frac{v_m}{\omega L}\cos(\omega t)+\mathrm{constant}$$

ed The integration constant has the dimension of current and is timeindependent. Since the source has an emf which oscillates symmetrically about zero, the current it sustains also oscillates symmetrically about zero, so that no constant or time-independent component of the current exists. Therefore, the integration constant is zero.



Using 

$$-\cos(\omega t)=\sin\left(\omega t-\frac{\pi}{2}\right)$$

$$i=i_m\sin\left(\omega t-\frac{\pi}{2}\right)$$

where $i_{m}=\frac{v_{m}}{\omega L}$ isthe amplitude of the current. The quantity ω L is analogous to the resistance and is called inductive reactance, denoted by $X_{r}$ ：

$$X_{L}=\omega L $$

The amplitude of the current is, then 

$$i_{m}=\frac{v_{m}}{X_{L}}$$

ot and its SI unit is ohm (Ω). The inductive reactance limits the current in a The dimension of inductive reactance is the same as that of resistance purely inductive circuit in the same way as the resistance limits the current in a purely resistive circuit. The inductive reactance is directly A comparison of Eqs. (7.1) and (7.12) for the source voltage and the $\pi/2$ or one-quarter $(1/4)$ cycle. Figure 7.6 (a) shows the voltage and the current $t_{1}$ $\pi/2$ (7.12), respectively and as shown in Fig. 7.6(b).



<div style="text-align: center;">(b)</div>


<div style="text-align: center;">FIGURE 7.6 (a) A Phasor diagram for the circuit in Fig. 7.5.(b) Graph of v and i versus ωt.</div>


We see that the current reaches its maximum value later than the voltage by one-fourth of a period $\left[\frac{T}{4}=\frac{\pi/2}{\omega}\right]$ . You have seen that an inductor has reactance that limits current similar to resistance in a find out.E 

 o t ur s.

$$\begin{aligned}p_{L}=i v&=i_{m}\sin\left(\omega t-\frac{\pi}{2}\right)\times v_{m}\sin(\omega t)\\&=-i_{m}v_{m}\cos(\omega t)\sin(\omega t)\\&=-\frac{i_{m}v_{m}}{2}\sin(2\omega t)\end{aligned}$$

So, the average power over a complete cycle is 

$$\left\{\begin{aligned}P_{\mathrm{L}}=\left\langle-\frac{i_{m}v_{m}}{2}\sin(2\omega t)\right\rangle\\ =-\frac{i_{m}v_{m}}{2}\left\langle\sin(2\omega t)\right\rangle=0,\end{aligned}\right.$$

since the average of sin (2ωt) over a complete cycle is zero.

Thus, the average power supplied to an inductor over one complete cycle is zero.



Example 7.2 A pure inductor of 25.0 mH is connected to a source of 220 V. Find the inductive reactance and rms current in the circuit if the frequency of the source is 50 Hz.



Solution The inductive reactance,

$$\left\{\begin{aligned}X_{L}=2\pi\nu L=2\times3.14\times50\times25\times10^{-3}\Omega\\ =7.85\Omega\end{aligned}\right.$$

The rms current in the circuit is 

$$I=\frac{V}{X_{L}}=\frac{220V}{7.85\Omega}=28A $$

### 7.5 AC VOLTAGE APPLIED To a CaPaCIToR 

Figure 7.7 shows an ac source ε generating ac voltage $v=v_{m}$ sin ωt connected to a capacitor only, a purely capacitive ac circuit.

<div style="text-align: center;"><img src="imgs/img_in_image_box_47_295_500_518.jpg" alt="Image" width="37%" /></div>


<div style="text-align: center;">FIGURE 7.7An ac source connected to a capacitor.</div>


When a capacitor is connected to a voltage source in a dc circuit, current will flow for the short time required to charge the capacitor. As charge accumulates on the capacitor plates, the voltage across them increases, opposing the current. That is,a capacitor in a dc circuit will limit or oppose the current as it charges. When the capacitor is fully charged, the current in the circuit falls to zero.

When the capacitor is connected to an ac source,as in Fig. 7.7, it limits or regulates the current, but does not completely prevent the flow of charge. The capacitor is alternately charged and discharged as the current reverses each half cycle. Let q be the charge on the capacitor at any time t. The instantaneous voltage v across the capacitor is 



$$v=\frac{q}{C}$$

From the Kirchhoff s loop rule, the voltage across the source and the capacitor are equal,

$$v_{m}\sin\omega t=\frac{q}{C}$$

To find the current, we use the relation $i=\frac{\mathrm{d}q}{\mathrm{d}t}$ 

$$i=\frac{\mathrm{d}}{\mathrm{d}t}\left(v_m C\sin\omega t\right)=\omega C v_m\cos(\omega t)$$

Using the relation, cos $\mathbf{s}(\omega t)=\sin\left(\omega t+\frac{\pi}{2}\right)$ , we have 

$$i=i_{m}\sin\left(\omega t+\frac{\pi}{2}\right)$$

where the amplitude of the oscillating current is it as $i_{m}=\omega C v_{m^{\prime}}$ . We can rewrite 

$$i_{m}=\frac{v_{m}}{\left(1/\omega C\right)}$$

Cor $i_{m}=v_{m}/R$ for a purely resistive circuit, we find that (1/ωC) plays the role of resistance. It is called capacitive reactance and is denoted by $X_{c^{\prime}}$ 



$$X_{c}^{}=1/\omega C $$

so that the amplitude of the current is 

$$i_{m}=\frac{v_{m}}{X_{C}}$$

The dimension of capacitive reactance is the same as that of resistance and its SI unit is ohm (Ω). The capacitive reactance limits the amplitude of the current in a purely capacitive circuit in the same way as the resistance limits the current in a purely resistive circuit. But it is inversely proportional to the frequency and the capacitance.



A comparison of Eq.(7.16) with the equation of source voltage, Eq. (7.1) shows that the current is 司$\pi/2$ ahead of voltage.

<div style="text-align: center;"><img src="imgs/img_in_image_box_623_154_1128_382.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">FIGURE 7.8 (a) A Phasor diagram for the circuit in Fig. 7.7. (b) Graph of ν and i versus ωt.</div>


Figure 7.8(a) shows te phasor iagram t an instant $$ . Here the current phasor I is $\pi/2$ ahead of the voltage phasor V as they rotate counterclockwise. Figure 7.8(b) shows the variation of voltage and current with time. We see that the current reaches its maximum value earlier than the voltage by one-fourth of a period.



The instantaneous power supplied to the capacitor is 

$$\begin{array}{rl}{p_{c}=i\upsilon=i_{m}\cos(\omega t)\nu_{m}\sin(\omega t)}\\ {=i_{m}\nu_{m}\cos(\omega t)\sin(\omega t)}\\ {\stackrel{\cdot}{=}\frac{i_{m}v_{m}}{2}\sin(2\omega t)}\end{array}$$

So, asine o u,e ae ower 

$$P_{C}=\left\langle\frac{i_{m}v_{m}}{2}\sin(2\omega t)\right\rangle=\frac{i_{m}v_{m}}{2}\left\langle\sin(2\omega t)\right\rangle=0$$

since <sin $\left(2\omega t\right)>=0$ over a complete cycle.

Thus, we see that in the case of an inductor, the current lags the voltage by c $\pi/2$ $\pi/2$ 

Example 7.3 A lamp is connected in series with a capacitor. Predict your observations for dc and ac connections. What happens in each case if the capacitance of the capacitor is reduced?

Solution When a dc source is connected to a capacitor, the capacitor gets charged and after charging no current flows in the circuit and the lamp will not glow.There will be no changeevenifCis reduced.With ac source, the capacitor offers capacitative reactance $\left(1/\omega C\right)$ and the current flows in the circuit. Consequently, the lamp will shine.Reducing Cwill icaseacacendteampwillhiesbihty than before.



Example 7.4A15.0 μFcapacitor is connected to a220V,50 Hz source.Find the capacitive reactance and the current (rms and peak) in the circuit. If the frequency is doubled, what happens to the capacitive reactance and the current?



Solution Thecapacitivereactanceis 

$$X_{c}=\frac{1}{2\pi\gamma C}=\frac{1}{2\pi(50Hz)(15.0\times10^{-6}F)}=212\Omega $$

The rms current is 

$$I=\frac{V}{X_{c}}=\frac{220V}{212\Omega}=1.04A $$

The peak current is 

$$i_{m}=\sqrt{2}I=(1.41)(1.04A)=1.47A $$

Thiscurrent oscillates between +l.47Aand -l.47 A, and is aheadof the voltage by $\pi/2$ 



If the frequency is doubled, the capacitive reactance is halved and consequently,the current is doubled.



Example 7.5 A light bulb and an open coil inductor areconnectedto an ac source through a key as shown in Fig. 7.9.

<div style="text-align: center;"><img src="imgs/img_in_image_box_587_535_851_748.jpg" alt="Image" width="21%" /></div>


The switch is closed and after sometime, an iron rod is inserted into the interior of the inductor. The glow of the light bulb (a) increases; (b)decreases; (c) is unchanged, as the iron rod is inserted. Give your answer with reasons.



As the iron rod is inserted, the magnetic field inside the coil magnetizes the iron increasing the magnetic field inside it. Hence,the inductance of the coil increases. Consequently,the inductive reactanceof the coil increases.As a result,a larger fraction of the applied ac voltage appears across the inductor, leaving less voltage across the bulb. Therefore, the glow of the light bulb decreases.

### 7.6 AC VoLTAGE APPLIeD To A SERies LcR CIrcUIT 

Figure 7.10 shows a series LCR circuit connected to an ac source ε. As usual, we take the voltage of the source to be 公$v=v_{m}$ sin ωt.添

<div style="text-align: center;"><img src="imgs/img_in_image_box_68_1190_565_1425.jpg" alt="Image" width="40%" /></div>


<div style="text-align: center;">FIGURE 7.10 A series LCR circuit connected to an ac source.</div>


If q is the charge on the capacitor and i the current, at time t, we have, from Kirchhoff's loop rule:

$$L\frac{\mathrm{d}i}{\mathrm{d}t}+i R+\frac{q}{C}=v $$

We want to determine the instantaneous current i and its phase relationship to the applied alternating voltage v. We shall solve this problem by two methods. First, we use the technique of phasors and in the second method, we solve Eq. (7.20) analytically to obtain the timedependence of i.



#### 7.6.1 Phasor-diagram solution 

From the circuit shown in Fig. 7.10, we see that the resistor, inductor and capacitor are in series. Therefore, the ac current in each element is the same at any time, having the same amplitude and phase. Let it be 

$$the same at any time, having the same amplitude and phase. Let it be i=i_{m}\sin(\omega t+\phi)$$

here $$ se the current in the circuit. On the basis of what we have learnt in the previous 

The length of these phasors or the amplitude of $\mathbf{v_{\mathrm{R}}},\mathbf{v_{\mathrm{c}}}$ and $\mathbf{v}_{\mathbf{v}}$ are:

$$v_{Rm}=i_{m}R,v_{Cm}=i_{m}X_{C},v_{Lm}=i_{m}X_{L}$$

The voltage Equation (7.20) for the circuit can be written as 



$$v_{\mathrm{L}}+v_{\mathrm{R}}+v_{\mathrm{C}}=v $$

The phasor relation whose vertical component gives the above equation is 

$$\mathbf{V}_{\mathbf{L}}+\mathbf{V}_{\mathbf{R}}+\mathbf{V}_{\mathbf{C}}=\mathbf{V}$$

This relation is represented in Fig. 7.11(b). Since c $\mathbf{v_{c}}$ and $\mathbf{v}_{\nu}$ are always along the same line and in 

$$v_{c_m}-v_{L_n}$$

relations.Eq. (7.21). Fu Eq. (7.21). Further, let ection, e d $\mathbf{v_{\mathrm{_L}}}\mathrm{is}\pi/2$ $\mathbf{v_{\mathrm{_R}}}$ $\mathbf{v}_{\mathrm{_L}},\mathbf{v}_{\mathrm{_R}},\mathbf{v}_{\mathrm{_C}}$ ahead of I.,llel to I,(ci $\mathbf{v}_{\mathtt{L}},\mathbf{v}_{\mathtt{R}},\breve{\mathbf{v}_{\mathbf{c}}}$ $\mathbf{v_{c}}$ is $\mathbf{v}_{\mathtt{L}},\mathbf{v}_{\mathtt{R}},\breve{\mathbf{v}_{\mathbf{c}}}$ c a $\pi/2$ .iid:2I biu@em 

$$\mathbf{v}_{\mathbf{R}}$$

$$\mathbf{\widehat{v_{R}}}$$

$$\mathbf{V}_{\mathrm{c}}+\mathbf{V}_{\mathrm{L}}$$

<div style="text-align: center;">IGURE 7.11 (a) Relation between the phasors $\mathbb{V}_{\mathrm{L}},\mathbb{V}_{\mathrm{R}},\mathbb{V}_{\mathrm{C}}$ ,and 1, (b) Relation between thephasors $\mathbb{V}_{\mathrm{L}},\;\mathbb{V}_{\mathrm{R}}$ , and $(\mathbb{V}_{\mathrm{L}}+\mathbb{V}_{\mathrm{C}})$ for the circuit in Fig. 7.10.</div>


opposite i thy an  mid i  igle hasor $(\mathbf{V_{c}}+\mathbf{V_{r}})$ which has a magnitude $|v_{Cm}-v_{Lm}|$ . Since V is represented as the hypotenuse of a right-triangle whose sides are $\mathbf{v}_{\mathbf{R}}$ and $(\mathbf{v_{c}}+\mathbf{v_{r}})$ _|,the pythagorean theorem gives:

$$v_{m}^{2}=v_{Rm}^{2}+\left(v_{Cm}-v_{Lm}\right)^{2}$$

Substituting the values of $v_{Rm},v_{Cm}$ and $v_{Lm}$ from Eq. (7.22) into the above equation, we have 



$$\left\{\begin{aligned}v_{m}^{2}&=\left(i_{m}R\right)^{2}+\left(i_{m}X_{C}-i_{m}X_{L}\right)^{2}\\ &=i_{m}^{2}\left[R^{2}+\left(X_{C}-X_{L}\right)^{2}\right]\end{aligned}\right.$$

By analogy to the resistance in a circuit, we introduce the impedance Z in an ac circuit:

$$\begin{aligned}i_{m}&=\frac{v_{m}}{Z}\\ where&Z=\sqrt{R^{2}+\left(X_{C}-X_{L}\right)^{2}}\end{aligned}$$

<div style="text-align: center;"><img src="imgs/img_in_image_box_59_148_381_425.jpg" alt="Image" width="26%" /></div>


<div style="text-align: center;">FIGURE 7.12Impedance diagram.</div>


Since phasor I is always parallel to phasor $\mathbf{v_{R}}$ , the phase angle φis the angle between $\mathbf{v}_{\mathbf{R}}$ and v and can be determined from Fig. 7.12:

$$\tan\phi=\frac{v_{Cm}-v_{Lm}}{v_{Rm}}$$

Using Eq. (7.22), we have 

$$\tan\phi=\frac{X_{C}-X_{L}}{R}$$

Equations (7.26) and (7.27) are graphically shown in Fig. (7.12).This is called Impedance diagram which is a right-triangle with Zas its hypotenuse.



Equation 7.25(a) gives the amplitude of the current and Eq. (7.27)gives the phase angle. With these, Eq. (7.21) is completely specified.

If $X_{C}>X_{L}$ ,  is positive and the circuit is predominantly capacitive.Consequently, the current in the circuit leads the source voltage. If $X_{C}<X_{L}$ , is negative and the circuit is predominantly inductive.Consequently, the current in the circuit lags the source voltage.

.for the case $X_{C}>X_{L}$ Ta 

<div style="text-align: center;"><img src="imgs/img_in_image_box_83_740_627_1030.jpg" alt="Image" width="44%" /></div>


<div style="text-align: center;">FIGURE 7.13 (a) Phasor diagram of V and 1.(b) Graphs of v and i versus ω t for a series LCR EY circuit where b $X_{c}>X_{L}$ </div>


Thus, we have obtained the amplitude and phase of current for an LCR series circuit using the technique of phasors. But this method of analysing ac circuits suffers from certain disadvantages. First, the phasor diagram say nothing about the initial condition. One can take any arbitrary value of t(say,$t_{1}$ , as done throughout this chapter)and draw different phasors which show the relative angle between different phasors.The solution so obtained is called the steady-state solution. This is not a general solution. Additionally,we do havea transient solution which exists even for $v=0$ . The general solution is the sum of the die out and the behaviour of the circuit is described by the steady-state solution.



### 7.6 

of resonance. The phenomenon of resonance is common among systems is called the system's natural frequency.If such a system is driven by an energy source at a frequency that is near the natural frequency, the for swining back and orthlikea pendulum.f thechild pullso th 

rope at regular intervals and the frequency of the pulls is almost the same as the frequency of swinging, the amplitude of the swinging will be large.添司

 $$ and frequency ω, we found that the current amplitude is given by 

$$i_{m}=\frac{v_{m}}{Z}=\frac{v_{m}}{\sqrt{R^{2}+\left(X_{C}-X_{L}\right)^{2}}}$$

with $X_{c}=1/\omega C\mathrm{and}X_{L}=\omega L$ .So if ω is varied, then at a particular frequency $\omega_{0},X_{c}=X_{L}$ ,and the impedance is minimum $\left|\left(Z={\sqrt{R^{2}+0^{2}}}=R\right)\right|$ . This frequency is called the resonant frequency:

$$X_{c}=X_{L}\quad or\quad\frac{1}{\omega_{0}C}=\omega_{0}L $$

or $\omega_{0}=\frac{1}{\sqrt{LC}}$ 

At resonant frequency, the current amplitude is maximum;$i_{m}=v_{m}/R.$ 



Figure 7.16 shows the variation of $i_{m}$ with in a RLC series circuit with $L=1.00\ \mathrm{mH},\ C=$ 1.00 nF for two values of R: (i)$R=100$ C and (ii)$R=200\Omega$ . For the source applied $V_{m}\equiv$ $100\mathrm{~V~}\omega_{0}$ for this case is $\frac{1}{\sqrt{LC}}=1.00\times10^{6}$ rad $1/\mathbf{s}$ .



We see that the current amplitudeis maximum at the resonant frequency. Since $i_{m}=$ $V_{m}/$ Rat resonance, the current amplitude for case (i) is twice to that for case (ii).

<div style="text-align: center;"><img src="imgs/img_in_chart_box_656_560_1135_883.jpg" alt="Image" width="39%" /></div>


<div style="text-align: center;">FIGURE 7.14 Variation of $\dot{I}_{m}$ with ω for two  cases: (i)$R=100\Omega$ , (ii)$R=200\Omega$   $L=1.00\ mH.$   </div>


Resonant circuits have a variety of applications, for example, in the tuning mechanism of a radio or a TV set. The antenna of a radio accepts signals from many broadcasting stations. The signals picked up in the antenna acts as a source in the tuning circuit of the radio, so the circuit can be driven at many frequencies. But to hear one particular radio station, we tune the radio. In tuning, we vary the capacitance of a capacitor in the tuning circuit such that the resonant frequency of the circuit becomes nearly equal to the frequency of the radio signal received.When this happens, the amplitude of the current with the frequency of It is im    d circuit only if both L and C are present in the circuit. Only then do the voltages across L and C cancel each other (both being out of phase)and the current amplitude is $v_{m}/R,$ , the total source voltage appearing across R. This means that we cannot have resonance in a RL or RC circuit.



Example 7.6 A resistor of 200Ω and a capacitor of 15.0 μFare connected in series toa 220V,50 Hz ac source.(a) Calculate the current in the circuit;(b) Calculate the voltage (rms) across the resistor and the capacitor. Is the algebraic sum of these voltages more than the source voltage? If yes, resolve the paradox.

## Solution 

Given 

$$R=200\Omega,C=15.0\mu\mathrm{F}=15.0\times10^{-6}\mathrm{F}$$

$$V=220V,v=50Hz $$

(a)Inorder to calculate the current,we need the impedanceof thecircuit. It is ned 

$$\begin{aligned}Z&=\sqrt{R^{2}+X_{C}^{2}}=\sqrt{R^{2}+\left(2\pi\nu C\right)^{-2}}\\&=\sqrt{\left(200\Omega\right)^{2}+\left(2\times3.14\times50\times15.0\times10^{-6}\mathrm{F}\right)^{-2}}\\&=\sqrt{\left(200\Omega\right)^{2}+\left(212.3\Omega\right)^{2}}\\&=291.67\Omega\\ \end{aligned} ned $$

Therefore,the current in the circuit is 

$$I=\frac{V}{Z}=\frac{220V}{291.5\Omega}=0.755A $$

(b)Since the current is the same throughout the circuit, we have 

$V_{R}=IR=(0.755\mathrm{A})(200\Omega)=151\mathrm{V}$ 



$$V_{R}=IR=(0.755\mathrm{A})(200\Omega)=151\mathrm{V}$$

The algebraic sum of the two voltages,$V_{R}$ and $V_{c}$ is311.3Vwhich is more than the source voltage of 22o V. How to resolvethis paradox? As you have learnt in the text, the two voltages are not in the same phase. Therefore, they cannot be added like ordinary numbers. The two voltages are out of phase by ninety degrees.Therefore,the total of these voltages must be obtained using the Pythagorean theorem:

$$V_{R+C}=\sqrt{V_R^2+V_C^2}$$

Thus,if the phase difference between two voltages is properly taken into account, the total voltage across the resistor and the capacitor is equal to the voltage of the source.



### 7.7 PowER In AC CIrcuIT: THE PowER FaCTor 

We have seen that a voltage $v=v_{m}$ sinωt applied to a series RLC circuit drives a current in the circuit given by $i=i_{m}\sin(\omega t+\phi)$ where 

$$i_{m}=\frac{v_{m}}{Z}\quad and\quad\phi=\tan^{-1}\left(\frac{X_{C}-X_{L}}{R}\right)$$

Therefore, the instantaneous power p supplied by the source is 

$$\begin{aligned}&p=v i=(v_m\sin\omega t)\times[i_m\sin(\omega t+\phi)]\\ &=\frac{v_m i_m}{2}[\cos\phi-\cos(2\omega t+\phi)]\\ \end{aligned}$$

The average power over a cycle is given by the average of the two terms in R.H.S. .. ent.Its average is zero the positive half of the cosine cancels the negative half). Therefore,

$$P=\frac{v_m i_m}{2}\cos\phi=\frac{v_m}{\sqrt{2}}\frac{i_m}{\sqrt{2}}\cos\phi $$

$$=V I\cos\phi $$

This can also be written as,

$$P=I^{2}Z\cos\phi $$

quantity cos is called the power factor. Let us discuss the folowing So, the average power dissipated depends not only on the voltae and current but also on the cosine of the phase angle φ between them. The cases:a 

Case (1) Resistive circuit: If the circuit contains only pure R, it is called resistive. In that case $\phi=0,\cos\phi=1$ . There is maximum power dissipation.Case (ii) Purely inductive or capacitive circuit: If the circuit contains only an inductor or capacitor, we know that the phase diference between voltage and current is $\pi/2$ . Therefore, cos $\phi=0$ , and no power is dissipated evenimes referred to as wattless current.



Case (il) LCR series circuit: In an LCR series circuit, power dissipated is given by Eq. (7.30) where $\phi=\tan^{-1}\left(X_c-X_L\right)/R\mathrm{So}$ 1, may be non-zero in a RL or RC or RCL circuit. Even in such cases, power is dissipated only in the resistor.



Case (iv) Power dissipated at resonance in LCR circuit: At resonance $X_{c}-X_{L}=0$ ,and $\phi=0$ $\bar{\cos}\phi=1$ and $P=I^{2}Z=I^{2}$ R. That is,maximum power is dissipated in a circuit (through R) at resonance.

Example 7.7 (a) For circuits used for transporting electric power,a low power factor implies large power loss in transmission. Explain.

(b) Power factor can often be improved by the use ofa capacitor of appropriate capacitance in the circuit. Explain.



Solution (a) We know that $P=I\;V\cos\phi$ where cos is the power factor.To supply a given power at a given voltage, if cos is small, we have to increase current accordingly. But this will lead to large power loss $(I^{2}R)$ in transmission.



(b)Suppose in a circuit, current I lags the voltage by an angle . Then power factor cos $\scriptstyle\phi=R/Z.$ 



We can improve the power factor (tending to l) by making Ztend to R. Let us understand, with the help of a phasor diagram (Fig. 7.15)

<div style="text-align: center;"><img src="imgs/img_in_image_box_549_161_999_526.jpg" alt="Image" width="36%" /></div>


<div style="text-align: center;">FIGURE 7.15</div>


how this can be achieved. Let us resolve I into two components.$\mathbf{I}_{p}$ alongthe applied voltage V and $\mathbf{I}_{q}$ perpendicular to the applied voltage.$\mathbf{I}_{q}$ as you have learnt in Section 7.7, is called the wattless component since corresponding to this component of current, there is no power loss.$\mathbf{I}_{\mathrm{p}}$ is known as the power component because it is in phase with the voltage and corresponds to power loss in the circuit.It's clear from this analysis that if we want to improve power factor,we must completely neutralize the lagging wattless current $\mathbf{I}_{\mathrm{q}}$ by an equal leading wattless current $\mathbf{I}_{\mathrm{q}}^{\prime}.$ This can be done byconnecting a capacitor of appropriate value in parallel so that $\mathbf{I}_{\mathrm{q}}$ and $\mathbf{I}_{\mathrm{~q~}}^{\prime}$ cancel each other and P is effectively $I_{\mathrm{p}}\;V.$ 



Example 7.8 A sinusoidal voltage of peak value 283 V and frequency 50 Hz is applied to a series LCR circuit in which $R=3\Omega,L=25.48\mathrm{mH}$ $\mathrm{C}=796~\mu\mathrm{F}$ .Find (a) the impedance of the circuit; (b) the phase difference between the voltage across the source and the current;(c)the power dissipated in the circuit; and(d)the power factor.



## Solution 

(a) To find the impedance of the circuit, we first calculate $X_{\mathrm{L}}$ and $X_{\mathrm{c}}$ 

$\begin{cases}X_{L}=2\pi\mathrm{v}L\\\quad=2\times3.14\times50\times25.48\times10^{-3}\Omega=8\Omega\\\quad X_{C}=\displaystyle\frac{1}{2\pi\gamma C}\end{cases}$ 

$$(a) To find the impedance of the circuit, we first calculate \begin{cases}X_{L}=2\pi\mathrm{v}L\\\quad=2\times3.14\times50\times25.48\times10^{-3}\Omega=8\Omega\\\quad X_{C}=\displaystyle\frac{1}{2\pi\gamma C}\end{cases}$$

$$\frac{1}{1}=\frac{1}{2\times3.14\times50\times796\times10^{-6}}=4\Omega $$

Therefore,

$$\left\{\begin{aligned}Z=\sqrt{R^{2}+\left(X_{L}-X_{C}\right)^{2}}=\sqrt{3^{2}+\left(8-4\right)^{2}}\\ =5\Omega\end{aligned}\right.$$

(b) Phase difference,$\phi=\tan^{-1}\frac{X_{C}-X_{L}}{R}$ 

$$=\tan^{-1}\left({\frac{4-8}{3}}\right)=-53.1^{\circ}$$

Since φis negative,the current in the circuit lags the voltage across the source.



(c) The power dissipated in the circuit is 

$$P=I^{2}R $$

$$\mathrm{NOW},I=\frac{i_m}{\sqrt{2}}=\frac{1}{\sqrt{2}}\left(\frac{283}{5}\right)=40\mathrm{A}$$

$$P=(40\mathrm{A})^2\times3\Omega=4800\mathrm{W}$$

(d) Power $\mathrm{factor}=\cos\phi=\cos(-53.1^{\circ})=0.6$ 

Example 7.9 Suppose the frequency of the source in the previous example can be varied.(a) What is the frequencyof the source at which resonance occurs?(b) Calculate the impedance, the current,and the power dissipated at the resonant condition.

## Solution 

(a) The frequency at which the resonance occurs is ERT 

$$\omega_{0}=\frac{1}{\sqrt{LC}}=\frac{1}{\sqrt{25.48\times10^{-3}\times796\times10^{-6}}}$$

(b) The impedance Z at resonant condition is equal to the resistance:

$$Z=R=3\Omega $$

The rms current at resonance is 

$$\frac{V}{Z}=\frac{V}{R}=\left(\frac{283}{\sqrt{2}}\right)\frac{1}{3}=66.7A $$

The power dissipated at resonance is 

$$P=I^{2}\times R=(66.7)^{2}\times3=13.35kW $$

You can see that in the present case, power dissipated at resonance is more than the power dissipated in Example7.8.

Example 7.10 At an airport, a person is made to walk through the doorway of a metal detector,for security reasons.If she/he is carrying anything made of metal, the metal detector emits a sound. On what principle does this detector work?



Solution The metal detector works on the principle of resonance in ac circuits. When you walk through a metal detector,you are,in fact, walking through a coill of many turns. The coil is connected to a capacitor tuned so that the circuit is in resonance. When you walk through with metal in your pocket,the impedance of the circuit changes–resultinin significantchange incurrentin the circuit. This changeincurrent isdetected and thelectronicircuitry causes a sound to be emitted as an alarm.



$$^{s}{a}=\begin{aligned}{}&{{}^{s}{}^{}{}^{}{3}}\\ \end{aligned}$$

c 

   a r  r cr  r e e  c e r  $r^{d}\dot{\boldsymbol{\alpha}}=\dot{\boldsymbol{\alpha}}^{d}\boldsymbol{\beta}$ If this were not so, the primary current would be infinite But 

$$If this were not so, the primary current would be infinite 
\frac{\mathrm{i}\mathrm{p}}{\phi\mathrm{p}}^{d}N^{-}={}^{d}\mathcal{S}$$

s s 

L 

$\frac{\mathrm{i}\mathrm{p}}{\phi\mathrm{p}}^{s}N^{-}={}^{s3}$ 

$$L \frac{\mathrm{i}\mathrm{p}}{\phi\mathrm{p}}^{s}N^{-}={}^{s3}$$

i $\overset{s}{N}$ p $^{d}_{\alpha}$     $*^{s}{}_{3}$ e        e m primary and secondary windings. Let  be the flux in each turn in the core primary has negligible resistance and all the flux in the core links both consider an ideal transformer in which the $\alpha\Lambda$ turns in the secondary.and induces an emf in it. The value of this emf depends on the number of current produces an alternating magnetic flux which links the secondary When an altrnating voltage is applied to the primary, the resulting 

(a) two coils on topofeach other,(b) two coils on separate limbsof the core.

<div style="text-align: center;"><img src="imgs/img_in_image_box_146_690_1152_1064.jpg" alt="Image" width="82%" /></div>


e      e   

  a $$ turns. The other coil is called the coils called the primary coil has $^d N$ 

7.16(b). One of the $\widehat{\boldsymbol{\mathcal{B}}}_{\mathrm{I,I}}$ Fig. 7.16(a) or on separate limbs of the core as in  e             d a device called transformer using the principle of mutual induction.voltage from one to another of greater or smaller value. This is done with For many purposes, it is necessary to change (or transform) an alternating 

### 7.8 TRANSFORMERS 

where (7.32)$v_{s}$  



$$v_{s}=-N_{s}\frac{\;d\phi}{\;d t}$$

$$v_{p}=-N_{p}\frac{d\phi}{dt}$$

From Eqs. [7.31 (a)] and [7.32 (a)], we have 

$$\frac{v_{s}}{v_{p}}=\frac{N_{s}}{N_{p}}$$

assumptions: (i) the primary resistance and current are small; (ii) the same flux links both the primary and the secondary as very little flux Note that the above relation has been obtained using three Fesnoitrooore,aia(n tiicSccoindarycuiTemtissmall.e 

the power input is equal to the power output, and since      $p=i v,$  s ),es),

$$i_{p}v_{p}=i_{s}v_{s}$$

ion,since a well designed transformer may have an efficiency of more than 95%. Combining Eqs. (7.33) and (7.34), we have 

$$\cfrac{i_{p}}{i_{s}}=\cfrac{v_{s}}{v_{p}}=\cfrac{N_{s}}{N_{p}}.$$

Since i and v both oscillate with the same frequency as the ac source,Eq. (7.35) also gives the ratio of the amplitudes or rms values of corresponding quantities.



Now, we can see how a transformer affects the voltage and current.We have:

$$V_{s}=\left(\frac{N_{s}}{N_{p}}\right)V_{p}\quad and\quad I_{s}=\left(\frac{N_{p}}{N_{s}}\right)I_{p}$$

That is, if the secondary coil has a greater number of turns than the primary $\left(N_{s}>N_{p}\right)$ , the voltage is stepped up $(V_{s}>V_{p})$ . This type of arrangemet is alld a p-up tanrmer.Hoever, in tis rngement,there is less current in the secondary than in the primary $\{N_{p}/N_{s}\bar{<1}$ .and $I_{s}$ $<I_{p}$ .For example, if the primary coil of a tanformer has 0 turns and the secondary has 20o turns,$N_{s}/N_{p}=2\mathrm{~a n d~}N_{p}/N_{s}{=}1/2$ . Thus, a 220V 

If the secondary coil has less turns than the primary $\left(N_{s}<N_{p}\right)$ we have a step-down transformer. In this case,$V_{s}<V_{p}$ and $I_{s}>\mathring{I}_{p}$ That is, the voltage is stepped down, or reduced, and the current is increased.

The quans aed ave aply  a tarmrs (ithout any energy losses). But in actual transformers, small energy losses do occur due to the following reasons:

(i) Flux Leakage: There is always some flux leakage; that is, not all of the flux due to primary passes through the secondary due to poor 

design of the core or the air gaps in the core. It can be reduced by W 

(ii) i  :       resistance and so, energy is lost due to heat produced in the wire $(I^{2}R)$ . In high current, low voltage windings, these are minimised by 0AC using thick wire.



(i) 

in the iron core and causes heating. The effect is reduced by using a 

a：laminated core.



) 

the alternating magnetic field. The resulting expenditure of energy in the core appears as heat and is kept to a minimum by using a magnetic material which has a low hysteresis loss.C00Wo 

The large scae transmisin and itibution of crica nery over long distances is done with the use of transformers. The voltage output of the generator is stepped-up (so that current is reduced and consequently, the $I^{2}R$ loss is cut down). It is then transmitted over long distances to an area sub-station near the consumers. There the voltage is stepped down. It is further stepped down at distributing sub-stations and utility poles before a power supply of 240 V reaches our homes.

## SUMMARY 

1. Analternating voltage $v=v_{\mathrm{m}}$ sinωt appliedto a resistor Rdrives a current $i=i_{m}$ sinωt in the resistor,$i_{m}=\frac{v_{m}}{R}$ . The current is in phase with the applied voltage.Y 2For an alternating current $i=i_{m}$ sin ωt passing through a resistor R, the average power loss P(averaged over a cycle) due to joule heating is $(1/2)i_{m}^{2}R$ To express it in the same form as the dc power $\{P=I^{2}\bar{R}\}$ a special value ofcurrent is used. It is called root mean square (rms)current and is donoted by I:

$$I=\frac{i_{m}}{\sqrt{2}}=0.707i_{m}$$

Similarly, the rms voltage is defined by 

$$V=\frac{v_{m}}{\sqrt{2}}=0.707v_{m}$$

We have $P=I V=I^{2}R$ 

3.An ac voltage $v=v_{m}$ sin ωt applied to a pure inductor $L,$ drives a current in the inductor $i=\hat{i}_{m}\mathrm{sin}\left(\omega t-\pi/2\right)$ where $i_{m}=v_{m}/X_{L}.X_{L}=\omega L$ iscalled inductiue reactance."The current in the inductor lags the voltage by $\pi/2$ The average power supplied to an inductor over one complete cycle is zero.



4.An ac voltage $v=v_{m}$ sinωt applied to a capacitor drives a current in the capacitor:$\widetilde{i=i_{m}\sin^{m}\left(\omega t+\pi/2\right)}$ 



$$
\begin{aligned}
i&=i_{m}\sin\!\left(\omega t+\frac{\pi}{2}\right),\\[4pt]
i_{m}&=\frac{v_{m}}{X_{C}},\\[4pt]
X_{C}&=\frac{1}{\omega C},
\end{aligned}
$$

where $X_C$ is called the **capacitive reactance**.

The current through the capacitor is $\pi/2$ ahead of the applied voltage.As in the case of inductor, the average power supplied to a capacitor over one complete cycle is zero.



5.For a series RLC circuit driven by voltage $v=v_{m}$ sinωt, thecurrent is given by $i=i_{m}\sin\left(\omega t+\phi\right)$ 



where 

$$i_{m}=\frac{v_{m}}{\sqrt{R^{2}+\left(X_{C}-X_{L}\right)^{2}}}$$

and $\phi=\tan^{-1}\frac{X_{C}-X_{L}}{R}$ 

$Z=\sqrt{{R^{2}}+{\left({{X_{C}}-{X_{L}}}\right)^{2}}}$ is called the impedance of the circuit.

The average power loss over a complete cycle is given by 

$$P=V I\cos\phi $$

The term cos is called the power factor.

6.In a purely inductive or capacitive circuit,$\cos\phi=0$ and no power is dissipated even though a current is flowing in the circuit. In such cases,current is referred to as a wattless current.



7.The phase relationship between current and voltage in an ac circuit can be shown conveniently by representing voltage and current by rotating vectors called phasors. A phasor is a vector which rotates about the origin with angular speed ω. The magnitude of a phasor represents the amplitude or peak value of the quantity (voltage or current) represented by the phasor.



The analysis of an ac circuit is facilitated by the use of a phasor diagram.



8.A transformer consists ofan iron core on which are bound a primary coil of $N_{p}$ turns and a secondary coil of $\bar{N}_{s}$ turns. If the primary coil is connected to an ac source,the primary and secondary voltages are related by 



$$V_{s}=\left(\frac{N_{s}}{N_{\frac{p}{2}}}\right)_{\frac{p}{2}}$$

and the currents are related by 

$$I_{s}=\left(\frac{N_{p}}{N_{s}}\right)I_{p}$$

If the secondary coil has a greater number of turns than the primary, the voltage is stepped-up $(V_{s}>V_{p})$ .This type of arrangement is called a stepup transformer. If the secondary coil has turns less than the primary, we have a step-down transformer.




<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>Dimensions</td><td>Dimensions [A] $[\mathrm{M}\mathrm{L}^{2}\mathrm{T}^{-3}\mathrm{A}^{-1}]$ $[\mathrm{M}\mathrm{L}^{2}\mathrm{T}^{-3}\mathrm{A}^{-2}]$ $[\mathrm{T}^{-1}]$ $\begin{array}{r}{[\mathrm{M}\mathrm{L}^{2}\mathrm{T}^{-3}\mathrm{A}^{-2}]}\\ {[\mathrm{M}\mathrm{L}^{2}\mathrm{T}^{-3}\mathrm{A}^{-2}]}\end{array}$</td><td>Unit</td><td>Remarks</td><td></td></tr><tr><td>Physical quantity</td><td>Symbol V I Z $\omega_{\mathrm{r}}\;\mathrm{or}\;\omega_{0}$ $\begin{array}{r}{X_{\mathrm{L}}}\\ {X_{\mathrm{C}}}\end{array}$</td><td>Symbol</td><td>Unit V A $\mathrm{Hz}$</td><td>Remarks the amplitude of the ac voltage. is the amplitude of the ac current. pa Depends elements present in the circuit. for a series RLC circuit for a series RLC circuit. 一 cosφ, φ is the phase difference between voltage applied and current in the circuit. $I=\frac{i_{m}}{\sqrt{2}},\;i_{m}$ $Q=\frac{\omega_{0}L}{R}=\frac{1}{\omega_{0}CR}$ $\omega_{0}=\frac{1}{\sqrt{LC}}$ $\begin{array}{l}{{X_{\mathrm{_L}}={\dot{\mathrm{~}}}\omega\mathrm{~}L}}\\ {{X_{\mathrm{_c}}=1/\mathrm{~}\omega\mathrm{~}C}}\end{array}$ $V\quad=\quad\frac{v_{m}}{\sqrt{2}}\quad,\quad v_{m}\quad\mathrm{is}.$</td></tr><tr><td>rms voltage rms current Reactance: Inductive Capacitive Impedance Resonant frequency Quality factor Power factor</td><td>V</td><td>rms voltage</td><td>the $V\quad=\quad\frac{v_{m}}{\sqrt{2}}\quad,\quad v_{m}\quad\mathrm{is}.$</td><td></td></tr><tr><td></td><td></td><td>amplitude of the ac voltage.</td><td></td><td></td></tr><tr><td>rms current</td><td>I</td><td>[A]</td><td>A</td><td>is the amplitude of $I=\frac{i_{m}}{\sqrt{2}},\;i_{m}$</td></tr><tr><td>Reactance: Inductive Capacitive Impedance</td><td>Z $\begin{array}{r}{X_{\mathrm{L}}}\\ {X_{\mathrm{C}}}\end{array}$</td><td>$\begin{array}{l}{{X_{\mathrm{_L}}={\dot{\mathrm{~}}}\omega\mathrm{~}L}}\\ {{X_{\mathrm{_c}}=1/\mathrm{~}\omega\mathrm{~}C}}\end{array}$</td><td>Depends elements present in the circuit.</td><td>$[\mathrm{M}\mathrm{L}^{2}\mathrm{T}^{-3}\mathrm{A}^{-2}]$</td></tr><tr><td>Resonant frequency</td><td>$\omega_{\mathrm{r}}\;\mathrm{or}\;\omega_{0}$</td><td>$\mathrm{Hz}$</td><td>for a $\omega_{0}=\frac{1}{\sqrt{LC}}$</td><td>$[\mathrm{T}^{-1}]$</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Quality factor</td><td></td><td></td><td></td><td>for a series $Q=\frac{\omega_{0}L}{R}=\frac{1}{\omega_{0}CR}$</td></tr></tbody></table></body></html></div>


'When a value is given for ac voltage or current, it is ordinarily the rms value. The voltage across the terminals of an outlet in your room is normally 240 V. This refers to the rms value of the voltage. The amplitude of this voltage is 



<div style="text-align: center;"><img src="imgs/img_in_image_box_218_1149_349_1306.jpg" alt="Image" width="10%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_355_1064_473_1147.jpg" alt="Image" width="9%" /></div>


## POINTS TO PONDER 

$$v_{m}=\sqrt{2}V=\sqrt{2}(240)=340V $$

e 2.The power rating of an element used in ac circuits refers to its average power rating.



3.The power consumed in an ac circuit is never negative.

4.Both alternating current and direct current are measured in amperes.But how is the ampere defined for an alternating current? It cannot be 

with the source frequency and the attractive force would average to zero.Thus, the ac ampere must be defined in terms of some property that is independent of the direction of the current. Joule heating is such a property,and there is one ampere of rms value of alternating current in a circuit if the current produces the same average heating effect as one ampere of dc current would produce under the same conditions.



5.In an ac circuit, while adding voltages across different elements, one should take care of their phases properly. For example, if $V_{R}$ and $V_{c}$ $V_{R}+V_{C}$ 人,since $V_{c}$ 人人is 传$\pi/2$ C c out of phase of s $V_{R^{\prime}}$ $V_{RC}=\sqrt{V_{R}^{2}+V_{C}^{2}}$ an RC circuit,thenth an RC circuit, then the andn 6.Though in a phasor diagram, voltage and current are represented by vectors, these quantities are not really vectors themselves. They are harmonically varying scalars combine mathematically in the same way as do the projections of rotating vectors of corresponding magnitudes and directions. The 'rotating vectors' that represent harmonically varying scalar quantities are introduced only to provide us with a simple way of adding these quantities using a rule that we already know as the law of vector addition.scalar quantities. It so happens that the amplitudes and phases of 

7.There are no power losses associated with pure capacitances and pure inductances in an ac circuit. The only element that dissipates energy in an ac circuit is the resistive element.



8. In a RLC circuit, resonance phenomenon occur when $X_{L}=X_{C}$ or $\omega_{0}=\frac{1}{\sqrt{LC}}$ .For resonance to occur, the presence of both L and C 

elements in the circuit is a must. With only one of these (Lor C)elements, there is no possibility of voltage cancellation and hence,no resonance is possible.



9.The power factor in a RLC circuit is a measure of how closethe circuit is to expending the maximum power.

10.In generators and motors, the roles of input and output are reversed. In a motor, electric energy is the input and mechanical energy is the output. In a generator, mechanical energy isthe input and electric energy is the output. Both devices simply transform energy from one form to another.

ll.A transformer (step-up) changes a low-voltage into a high-voltage.This does not violate the law of conservation of energy. The current is reduced by the same proportion.



## Physics 

## EXERCISES 

7.1AT002TCSStOr10C0e 

a) What is the rms value of current in the circuit?

(a)what is uc Tis veaseenemedeuorafull cc 中

7.2 e              (b) The rms value of current in an ac circuit is 10 A. What is the aetmi peak current?



7.3A44H inu icdt22V,0Hulyrmie 

the rms value of the current in the circuit.7.4A0F  .rmie the rms value of the current in the circuit.a 7.5In Exercises 7.3 and 7.4, what is the net power absorbed by each circuit over a complete cycle. Explain your answer.7.6Acharged 30F capaci is ncd toa27 mH inductor.What is the angular fequency of fee oscillationsof the crcuit?Ta 7.7A series LCR circuit with $R=20\Omega$ T]$L=1.5\ H$ Iand $C=35~\mu\mathrm{F}$ 'is connected −to a variable-frequency 200 V ac supply. When the frequency of the supply equals the natural frequency of the circuit, what is the average powertransierredtotiecncuitnronesoiproteeyeoe 7.8Figure7.17showsseieLCRcicutconnctedtoaiable frequency 230 V source.suucc.$L=5.0\ H,\ C=80\mu F,\ R=40\ \Omega$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_306_910_392_991.jpg" alt="Image" width="7%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_527_763_878_968.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;">FIGURE 7.17</div>


(a) D resonance.TeSOaCC：

(b) O Obtain ao  amtuf urrent annca at the resonating frequency.



(cD Derm      e the circuit. Show that the potential drop across the LC combination is zero at the resonating frequency.

