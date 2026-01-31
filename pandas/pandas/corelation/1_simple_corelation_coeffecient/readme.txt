**********************
General
**********************
1) A great aspect of the Pandas module is the corr() method.

2) The corr() method calculates the relationship between each column in your data set.



**********************
simple_data.csv
**********************
Manual way to find corelation coeffecient (for simple_data.csv)
-------------------------------------------------------------------------

1) Find the MEAN of X and Y (sample_data.csv)

Mean of X = (1 + 2 + 3 + 4 + 5) / 5 = 3
Mean of Y = (6 + 4 + 5 + 3 + 2) / 5 = 4

2) Calculate the DEVIATION SCORES of each value.
Deviation Scores indicate how far each value deviates (or departs) from the mean.

X   Y   Deviation_Score_X      Deviation_Score_Y
X   Y   (X  - MEAN_OF_X)      (Y - MEAN_OF_Y)
------------------------------------------------------
1   6   1-3=-2                  6-2=2
2   4   2-3=-1                  4-4=0
3   5   3-3=0                   5-4=1
4   3   4-3=1                   3-4=-1
5   2   5-3=2                   2-4=-2

Note:
    - The deviation scores should always add upto ZERO.
    - e.g. Deviation Scores for X = -2 + -1 + 0 + 1 + 2 =  0

3) SQUARE the DEVIATION SCORES, to get rid of the negative values

X   Y        Square_Deviation_Score_X                   Squre_Deviation_Score_Y
X   Y       SS(X) = (X  - MEAN_OF_X)^2                SS(Y) = (Y - MEAN_OF_Y)^2
----------------------------------------------------------------------------------
1   6       -2^2 = 4                                     2^2 = 4
2   4       -1^2 = 1                                     0^2 = 0
3   5       0^2 = 0                                      1^2 = 1
4   3       1^2 = 1                                      -1^2 = 1
5   2       2^2 = 4                                      -2^2=4

5) Calculate the SUM of  SQUARED DEVIATION SCORES (SS)

Sum of SS(X) = 4 + 1 + 0 + 1 + 4 = 10
Sum of SS(Y) = 4 + 0 + 1 + 1 + 4 = 10


6) Calculate the CROSS PRODUCTS
Cross_Product_X =  Deviation_Score_X * Deviation_Score_Y

X   Y   Deviation_Score_X      Deviation_Score_Y       Sum_of_Cross_Products (SP)
X   Y   (X  - MEAN_OF_X)      (Y - MEAN_OF_Y)       (X  - MEAN_OF_X)  * (Y - MEAN_OF_Y)
--------------------------------------------------------------------------------------------
1   6   1-3=-2                  6-2=2                   2 * -2 = -4
2   4   2-3=-1                  4-4=0                   -1 * 0 = 0
3   5   3-3=0                   5-4=1                   0 * 1 = 0
4   3   4-3=1                   3-4=-1                  -1 * 1 = -1
5   2   5-3=2                   2-4=-2                  2 * -2 = -4

SP = -4 + 0 + 0 + -1 + -4 = -9

7) Finally, calculate the CORELATION_COEFFICIENT

CORELATION_COEFFECIENT (r) =     SP (from step (6))
                            ------------------------------
                                Sqrt(SS(X)) * Sqrt(SS(Y))

                                       -9
                           =  -----------------------
                                Sqrt(10) * Sqrt(10)

                           r = 0.9

Reference: https://www.youtube.com/watch?v=lVOzlHx_15s





Results (Corelation coeffecient / Pierson's r for simple_data.csv) as calculated by 'Pythons dataFrame.corr()'
------------------------------------------------------------------------------------------------------------------
     x    y
x  1.0 -0.9
y -0.9  1.0

Note:
    1) X and X have the co-relation coefficient = 1 because X will always have a perfect relationship with itself, same is true for Y.
    2) X and Y have a co-relation coeffecient = -0.9 (as calculated manually above)

**********************
complex_data.csv
**********************
Results (Corelation coeffecient / Pierson's r for complex_data.csv)
------------------------------------------------------------------------
          Duration     Pulse  Maxpulse  Calories
Duration  1.000000 -0.155408  0.009403  0.922721
Pulse    -0.155408  1.000000  0.786535  0.025120
Maxpulse  0.009403  0.786535  1.000000  0.203814
Calories  0.922721  0.025120  0.203814  1.000000

Explanation of Results (for complex_data.csv)
------------------------------------------------------
The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.

The number varies from -1 to 1.

1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.

0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.

-0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.

0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.

What is a good corelation
-----------------------------
It is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation.

Perfect Correlation:
-----------------------
We can see that "Duration" and "Duration" got the number 1.000000, which makes sense, each column always has a perfect relationship with itself.

Good Correlation:
-----------------------
"Duration" and "Calories" got a 0.922721 correlation, which is a very good correlation, and we can predict that the longer you work out, the more calories you burn, and the other way around: if you burned a lot of calories, you probably had a long work out.

Bad Correlation:
-----------------------
"Duration" and "Maxpulse" got a 0.009403 correlation, which is a very bad correlation, meaning that we can not predict the max pulse by just looking at the duration of the work out, and vice versa.
