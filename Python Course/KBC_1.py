print('''Welcome to Kaun Banega Crorepati !

You have to answer 5 questions.
Every right answer will give you 100 Rs. 
Before going further in this game. Make sure your Caps lock is ON.
''')

print('''Give Answer in the form of A, B, C or D.

So, Are you ready for questions ?
YES or NO''')
x = input('-->:')
while True:
  if (x=='YES'):
    print('\nSo, Your first question is :')

  else :
    print('Thank you, Come back later')
    break

  #1
  print('\n1. What is 01 + 0 ?')
  print('''  A. 11              B. 7
  C. 22              D. 1''')
  x = (input(':> '))
  if (x=='D'):
    print('''   \nYour ans is right. You win 100 Rs.''')
  else :
    print('   Your ans is wrong. Total Winning : 0 Rs.')
    break

  #2
  print('\n2. Who is the father of Python ?\n')
  print('''  A. Tim berners lee     B. Bill Gates
  C. Guido Van Rossum    D. Mark Zuckerberg''')
  x = (input(':> '))
  if (x=='C'):
    print('''   \nYour ans is right. You win 200 Rs.''')
  else :
    print('   Your ans is wrong. Total Winning : 100 Rs.')
    break

  #3
  print('\n3. What is the colour of Sky ?\n')
  print('''  A. Orange          B. Red
  C. Blue            D. Black''')
  x = (input(':> '))
  if (x=='C'):
    print('''   \nYour ans is right. You win 300 Rs.''')
  else :
    print('   Your ans is wrong. Total Winning : 200 Rs.')
    break

  #4
  print('\n4. Which is programing language?\n')
  print('''  A. Python          B. Rabbit
  C. Replit          D. English''')
  x = (input(':> '))
  if (x=='A'):
    print('''   \nYour ans is right. You win 400 Rs.''')
  else :
    print('   Your ans is wrong. Total Winning : 300 Rs.')
    break

  #5
  print('\n5. How many Years in One Century ?\n')
  print('''  A. 120              B. 12
  C. 60              D. 100''')
  x = (input(':> '))
  if (x=='D'):
    print('''   \nYour ans is right. 
    
  CONGRATULATION !!! You won the Grand Price of 500 Rs.''')
  else :
    print('   Your ans is wrong. Total Winning : 400 Rs.')
  break
