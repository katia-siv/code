# code
You may not use Pandas or NumPy on this homework, as we’re building/reinforcing our foundational programming skills.
For each state and month, the data has:
Number of borrowers to-date who have had some or all of their student loans forgiven through the Public Service Loan Forgiveness program.
Outstanding balance to-date of those borrowers.

Recall that the data is cumulative! So the number of borrowers listed for September 2022 is everyone who had their loans forgiven up to and including that month.

Part 1 - Questions about the Data 

This part of your solution will be auto-graded. When you find this assignment on gradescope, the first part will ask you the following questions; type or select your answers. You must compute the answers to these questions programmatically. Gradescope will confirm your answers are correct/incorrect. 

Check the output! Gradescope can be a little picky about formatting, and we don’t want you to lose points for putting extra characters or whitespace in an answer. Make sure you’ve got the correct answer to each question for full credit. Note that the original dataset has monetary values in millions (e.g., $100 == $100 million), but the homework questions want the “real” values ($100 million == $100 million).

Answer these questions (make sure you compute these answers in your Python solution):
How many total borrowers had their PSLF application discharged as of March 2023? 
What is the total outstanding balance for all students as of March 2023?
What is the average outstanding balance per student as of March 2023?
Which state had the greatest increase in outstanding balance from May 2022 to March 2023?
How much did that state's outstanding balance increase during that timeframe?
Which state had the SMALLEST increase in outstanding balance from May 2022 to March 2023?
How much did that state’s outstanding balance increase during that timeframe?
On average, how much did the outstanding balance in a given state increase per month? (Prompt the user for the state. Assume that, in the first month, the outstanding balance did not change. Compute your first value as the change from May to June 2022.)


Part 2 - Visualization

Create two Python plots.

Plot #1: A histogram showing the average outstanding balance per borrower in each state, in November 2022.

Plot #2: A line chart showing how the average outstanding balance per borrowing changed over time. This chart should have two lines, comparing any two states you choose.
