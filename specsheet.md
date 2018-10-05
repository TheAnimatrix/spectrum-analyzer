**SPECIFICATION DETAILS OF SPECTRUM ANALYZER**
----------------------------------------------

1. Bit Depth of ADC
2. Frequency Range
3. Sampling rate of ADC
4. Noise Level Management
5. POI ?
6. Sweep Rate
7. Real time bandwidth



**MAIN DETAILS**
-----------------
__*1. Bit depth*__ -> Bit depth is the amount of bits you're willing to use to represent an instant of the signal. It's like the scale of a graph. Taking a broader scale gives you less resolution of
what you're willing to graphically visualize. Same thing here. If i use 2 bits to represent my signal at any instant. It can only make a square wave. 0 and 1 right ?. Lets increase this to 4bits. thats 2^4 combinations (or) 16 possible combinations. 16 different values can be used to represent my signal at an instant. That's not bad , a fair representation can be made with that. However do keep in mind most audio signals are represented in 16bit formats and colors on your display upto 10 bits. That's 2^10 (to) 2^16 possible combinations and provides amazing resolution on data. There appears to be some relationship between bit depth and the signal to be analyzed and more thought needs to be given to this to find out what bit depth is appropriate for our project.

__*2. Sampling rate*__ -> I don't need to explain this , anyways for the sake of the detail sheet here it goes. Sampling rate is the rate at  which you're going to look at the signal and pick it's constituent data up. Imagine this in terms of a non-spurious judge in a dance  show. This particular judge looks at the dance and makes a judgement by writing it down once each second (yeah he's fast, it's an   example!!). This puts his sampling rate at 1hz. Similarly if he noted 5 times in a second it would be 5hz. Sample applies to a circuit which processes some data n times a second. 

   Now sampling rate is directly proportional to what frequency we're going to measure. Example : Imagine yourself trying to sample an      oscillating pendulum. The pendulum is oscillating at 1khz , 1000 oscillations in a second. And yourself are sampling at 1hz , 1 time    a second you're going to look at the pendulum and note it's position. There exist 1000ms in 1 second. With the pendulum oscillating      that fast , you're probably going to measure it at the same instant of it's movement every cycle . You will obtain a straight line .    Therefore it's best practice to have a greater sample rate than the the frequency you are measuring by an order of magnitude.

   To put it into perspective measurement of a 20khz signal would only require .. what ? 44.1 khz (standard for audio) 
   but the frequency of light is 430-750 Thz and sampling that would take ... you guessed it PRETTY DAMN HIGH!! which is probably why      those spectrographs begin at about an arm's worth.

   Question i still haven't answered relating to this : IF You're going to feed the light into a ccd and measure how much light exists      in each band isn't that spectrum analysis ? and how does that pertain to the whole sample rate situation . Confused!!

__*3. Quantization*__ : (Enter: Noise) :=> Well this is basically intrinsic to the ADC AFAIK. This process is just simple rounding off to a level that our bit depth can match. Example : Take a normal sinusoidal signal with values upto 5V(Amplitude.) , When i sample it i'm going to end up with values like 4.2451 V or 1.12415 V. This requires quantization. Essentially splitting a signal into levels, 1 bit quantization results in 2^1=2 levels therefore i'm going to do something like all values 2.5-5V are rounded to 1 and all values from 0-2.49 are rounded to 0. Similarly 10 bit quantization will split the signal and round to 2^10 levels. This is part of sampling and like all sampling methods. It's mapping a lot of data into a small set (-∞,∞) to (-512,512) levels for 10 bit quantization. 

__*4. Aliasing*__ , Part of the whole sampling process. This is when we are unable to construct an approximation of the original signal by sampling, Due to lack in bit depth. For audio, it's temporal aliasing and for video it's spatial aliasing. Wiki link.

How the spectrum analyzer would work :
---------------------------------------

1. Take analog input signal 
2. Push it through an ADC of appropriate bit depth
	This would involve sampling the signal 
	and quantizing it , both of which are pretty heavy tasks
3. Now the data is ready
4. Perform any function on it .. this could be done onboard or on the server. Data is usually bigger than a few megabytes which might pose a problem . Depends on bit depth and sample rate.
5. Display the transformed data

NOTE:-
------

1. How will the input signal be taken ? How will the frequencies of these inputs influence our circuitry and frequency range of the analyzer ? 
2. Using a relatively lower sampling rate induces a distortion called aliasing , need to learn more about that.
3. Understand limitations of various hardware arduino , nodemcu , arm etc.. and what are the features lost / cost saved / portability . Find a good ratio .

TO BE INCLUDED:-
-----------------
More technical analysis with respect to part usage and how each part chosen increases the reliability/availability/usability/range of this analyzer. Every Problem encountered must be detailed in Errors.md regardless of it's doltishness.

Technical Roadmap. Prototype parts. Product parts, etc. must be analyzed and mentioned



MAINLY
======

NO ASSUMPTIONS MUST BE MADE AT ANY POINT IN THIS PROJECT AND EACH QUESTION MUST BE ANSWERED AS TECHNICALLY AS POSSIBLE.
POWER MANAGEMENT, LOGIC EFFICIENCY, WHAT BIT DEPTH WAS CHOSEN AND WHY, etci.
