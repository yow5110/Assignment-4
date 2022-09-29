# Week 5 Task 2

Similar to Task 1, another method of numerical integration is the trapezoid rule, where the area below the function within each interval [x1,x2] is estimated from a trapezoid with its two unequal sides being f(x1) and f(x2).

<a href="https://www.codecogs.com/eqnedit.php?latex=\int_a^bf(x)dx\approx&space;\frac{b-a}{n}\sum&space;_{i=0}^{n-1}f\left(a&plus;\left(i&plus;\frac{1}{2}\right)\frac{b-a}{n}&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int_a^bf(x)dx\approx&space;\frac{b-a}{n}\sum&space;_{i=0}^{n-1}f\left(a&plus;\left(i&plus;\frac{1}{2}\right)\frac{b-a}{n}&space;\right&space;)" title="\int_a^bf(x)dx\approx \frac{b-a}{n}\sum _{i=0}^{n-1}f\left(a+\left(i+\frac{1}{2}\right)\frac{b-a}{n} \right )" /></a>

Here's a visual representation 
<img src="ftrapezoid.png" alt="hi" class="inline"/>


TASK: In the trapezoid.py program you can find the basic loop to perform trapezoid integration of a generic function f from a to b, using a large number of small intervals. Modify the code to compute the integral of:
 
1. the sine function between 0 and pi, and
2. the cosine function between 0 and pi.

In each case, write out the error, i.e., the difference between the exact integral and the numerical result. Make the following comparisons:

Within the trapzoid method here, which of the two numerical integrals has a much smaller error than the other. Why?
For the sine case, how does the error from the trapezoid method compare with the error from the midpoint method using the same number of intervals?  Make your own rough sketches of the trapezoids and rectangles for the sine integral and comment on how to understand this.

