#1. Gaussian error

At the fundamental internship physics at my university, it is often necessary to calculate the Gaussian error of a math expression, when the single errors of the contained measures are known. 
For example: I know I can measure the length with a deviation of 1mm, using a ruler. Then I measure the time with a stopwatch, assuming a reaction time of 0.5s. Then I calculate the speed v = s/t
To determine the deviation of my calculated v, I can use the linear Gaussian error function. This can't be done by hand on big scales. 
The method "gauss" is fast to use: You just copy the string of the expression, for example

sigma_v = gauss("s/t")

That requires the existence of sigma_s and sigma_t, with that very name convention (Could be changed in the corresponding method)
The main file contains an example.
To achieve such a simple usage, the gauss method must be defined in the same file.

#2. LaTeX table

Once calculated, a numpy array can be exported to a table. The method "latexTable" creates the surrounding syntax for a table. It accepts any number of string arrays, that will be written as cols. To create these, there are several options. 
You could use unitCol, to add a unit string to your number in an array.
More advanced is the option roundCol, or its overlay RC.
It takes an array of measures and an array of the same length with the corresponding errors. Optional a unit String, and a stretching factor.
The result will be a string array, that is rounded according to the standards. 

#3. Matlab:

I implemented a similar functionality in Matlab, however the gauss function requires the connection of Matlab and Maple, to calculate the symbolic derivatives.

