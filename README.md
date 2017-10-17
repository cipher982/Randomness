# Randomness in all its wonderful forms!

Over the years I have fallen in love with the ideas of prediction, models, and
the tailwind of computer analytics that subsequently brought them all together.
It’s such a fascinating time to be an observer trying my best to keep up with
the steady flow of papers and talks, and the ever increasing amount of
open-source code that is becoming the norm for everything from academia to the
tech giants of Facebook and Google.

I wanted to be able to gather up all these scraps in my head and lay them back
out in an attempt to help both me and a whoever else that may come by and graze.
Most of these will focus on the general area of modeling and statistics from the
frame of modern machine learning, so it would be best to go ahead and explain
the foundations of *randomness.*

#### Random Walks of 1000 Steps

![](https://cdn-images-1.medium.com/max/1600/1*X6USvIfGlbW6_22mQrgfNg.gif)

> **Randomness: **the lack of [pattern](https://en.wikipedia.org/wiki/Pattern) or
> [predictability](https://en.wikipedia.org/wiki/Predictability) in events.

#### Some of the good

* It is a main component of modern cryptographic systems that power the digital
age, see [pseudorandom number
generators](https://en.wikipedia.org/wiki/Pseudorandom_number_generator).
* Simulating risk models or estimating areas using the [Monte Carlo
Method](http://mathonweb.com/entrtain/monte/t_monte.htm). *(See bottom of page
for example)*

![](https://cdn-images-1.medium.com/max/1600/1*8W-aBhlbaL16GqewPPnCyg.png)
<span class="figcaption_hack">Using random points to estimate area of a circle</span>

* [Statistical inference](https://en.wikipedia.org/wiki/Statistical_inference) and
how it enables the ideas of surveys and the scientific method to work.

#### Some of the annoying

* In the age of the computer and their
[Deterministic](https://en.wikipedia.org/wiki/Deterministic_algorithm) method of
operation, we have to ‘fake’ randomness using external sources or algorithms
that can be studied > modeled > predicted. This is the method a* *[Russian
hacker used to bilk casinos out of million of
dollars](https://www.wired.com/story/meet-alex-the-russian-casino-hacker-who-makes-millions-targeting-slot-machines/).
* Due to interactions going all the way down to the quantum level, many systems
can not be modeled past a certain preciseness due to ideas of
[Chaos](https://en.wikipedia.org/wiki/Chaos_theory) and divergence of systems
over time. On a most technical level they may actually be deterministic, but
pragmatically not in the ways we work with them.
* In relation to above, entire fields are dedicated to these ideas such as
[dynamical systems](https://en.wikipedia.org/wiki/Dynamical_system) and
[stochastic](https://en.wikipedia.org/wiki/Stochastic_system) processes that
underly them, in which something may be truly non-deterministic.

*****

### Modeling Random Motion in Nature

Below is a quick animation I put together with the magic of Python and
MatPlotLib *(annoyingly I can’t embed H.264 via HTML5 here, had to convert to
GIF)*

#### Random Travel in a 2D plane (Wiener Process)

*Github code below:*

### The Wiener Process, or Brownian Motion

As above and below, these motions are all related to the same idea of a
stochastic motion over time. The grid blow contains 25 simulations of random 2D
motion to give an idea of the varying types of outcomes. As the stocks charts
simulated at the top and the animation above as well illustrate, these are what
are referred to as a [Wiener
process](https://en.wikipedia.org/wiki/Wiener_process). A *continuous
time-series stochastic process *that has uses in numerous fields such as:
control theory, probability, quantum mechanics, and more.

Each plot below contains 1000 steps starting at 0,0 and going any direction from
there. It’s interesting so see how different these can end up. When looking at a
single image it may seem evident there are some clear patterns taking hold,
which dissolve with each subsequent image.

Now relate this back to events someone may observe in day to day life and you
can see why people may begin to see patterns where they don’t exist.

*Github code below:*

### Monte Carlo Estimation of Area

When attempting to find the area of any 2D or 3D shape you may realize there is
no obvious analytical solution, unless you know the function that created it.
One method that is quite simple with a computer is to simply brute force it.

![](https://cdn-images-1.medium.com/max/1600/1*fF2eJEgwj43KIBBdm4fePQ.png)

Monte Carlo methods, named after the casino in gambling mecca Monaco, came about
when Stanislaw Ulam looked to model the random processes that were the
foundation of many gambling style games, such as roulette, dice, and slot
machines. He initially theorized some of this work while performing nuclear
research at Los Alamos in the late 1940’s, it was soon picked up by [John von
Neumann](https://en.wikipedia.org/wiki/John_von_Neumann) who programmed some of
this into a computer to perform some calculations.

> This was already possible to envisage with the beginning of the new era of fast
> computers, and I immediately thought of problems of neutron diffusion and other
questions of mathematical physics, … Later [in 1946], I described the idea to
[John von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann), and we began
to plan actual
calculations.[[13]](https://en.wikipedia.org/wiki/Monte_Carlo_method#cite_note-13)
— Stanislaw Ulam

**Steps involved: *** Place image in a square grid<br> * Throw down a lot of
random points<br> * Measure ratio of points within to overall amount<br> *
Multiply by area of rectangle

*Here is an animated plot I created that iterates through 2000 steps of random
points in the box, and continually re-calculates the estimates area of the
circle: (Correct area is ~3.14)*

*GitHub code below:*


### [David Rose](https://medium.com/@david010)
