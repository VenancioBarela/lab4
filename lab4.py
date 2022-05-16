"""
This program allos a user three tries to guess the correct answer to the question
question (q) = "what is the capital of california". The answer (a) is "Sacramento".

we first set the max tries = 3. Then we create a loop to iterate three times. For each iteration, we ask the user for the answer (user input). 
Then based on the answer given we check to see if the user input matches the answer.
If so, print "Correct!", then terminate the loop with a break statement.

If the user could not answer the question with the max attempts, then print "You have used up your allotment of guesses.", 
then print "The correct answer is "Sacramento".

"""

"""
main
  question = "What is the capital of California"
  Answer = "Sacramento"
  ask(question,answer)

ask 
    tries = 0
    loop three times
        increment tries by 1
        ask user input()
        check to see if user input is equal to answer
            if so, print "Correct" then exit the loop
    if not correct
        print to the user "You have used up your allotment of guesses." 
        print the correct answer "The correct answer is 'Sacramento'"
 
main
"""
