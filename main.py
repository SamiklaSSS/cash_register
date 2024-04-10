#
# Kases aparāts
#
# 0.5pt pievienot jaunu preci - nosaukumu un cenu 
#     0.5pt preces nosaukumam jābūt no 2 līdz 120 simboliem (jābūt validācijai, rādīt paziņojumu ja neder)
#     0.5pt preces cenai jābūt veselam skaitlim vai daļskaitlim ar vērtību no 0 līdz 9999 (jābūt validācijai, rādīt paziņojumu ja neder)
# 0.5pt dzēst preci pēc kārtas numura 
# 0.5pt atcelt ievadu / iztukšot preču sarakstu
# 0.5pt piemērot atlaidi, ievadīt summu procentos
# 0.5pt samaksāt, ja iedota lielāka summa - izdrukāt atlikumu
# 0.5pt izdrukāt čeku uz ekrāna - preces nosaukumus un summas
#     0.5pt izdrukāt piemēroto atlaidi (ja ir)
#     0.5pt izdrukāt kopējo summu

# 1pt programmas stāvoklis tiek glabāts JSON faila un programmas sākumā tiek ielasīts un beigās saglabāts 
# 1pt kodam ir jēdzīgi komentāri, pirms "if, for, while" koda konstrukcijam 
# 1pt koda palaišanas brīdī nerādās kļūdas 
# 1pt mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā 
# 1pt izmaiņas saglabātas versiju vadības sistēmā Git, savs fork 
#
# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git
#

import json
 
f = open('CR.json')
f.close()


import json

print("Hello!")

while True:                                                                      # Chance to buy items, you can buy only one item
    choice = input("Do you want to buy something?(Answer yes/no)")

    Operation = []

    if choice == 'yes':
       print("Let's start!")
       a = input(print("What is a name of what you want to buy?"))               # a is a name of yhing that we want to buy
       Operation.append(a)
       b = input(print("What is this item's price?"))                            # b is price of the item
       Operation.append(b)
       choice2 = input(print("Is there discount on this item?(Answer yes/no)"))  # c is discount in procents
       if choice2 == 'yes':
          c = input(print("How big is discount?(Write without %)"))              # d is discount as a number
          Operation.append(c)  
          d = int(c)/100                                                         # e is final price
          h = int(b)*int(d)
          e = int(b) - int(h)                                                    # h is discount as a number(second)
          Operation.append(e)
       elif choice2 == 'no':
          print("That's sad.")
          c = 0
          Operation.append(c)
          e = b
          Operation.append(e)
       else:
          ("Error")
       print("name, price, discount in procents, final price")
       print(Operation)
       choice4 = print(input("How do you want to pay?(cash/card)"))
#       if choice4 == 'cash':                                                     # Choose how to pay
#          Alt = -2
#          while Alt !=2:
#             Alt = Alt + 1
#             g = print(input("How much will you pay?"))                             # g is payd cash
#             if g > b:
#                 print("Everything is allright!")
#                 m = g - b                                                           # m is everything that is left of payd
#             else:
#                 print("That's not enough!")
#       elif choice4 == 'card':
#          g = b
#          print("Everything is allright!")
#       else:
#          print("Error!")




       choice3 = input(print("Is everything correct?(Answer yes/no)"))
       if choice3 == 'yes':
         print("That's great!")
         print("Give us some time to print to print out check!")                 # Showing the check,only one item, so it show items separated
         print("               ")
         print("               ")
         print("     Check     ")
         print("               ")
         print(a)               
         print("Price:          ",  b )
         print("Discount(%):    ",  c )
         print("===================")
         print("Total:          ",  e )
#         print("Payd:           ",  g )
#         print("                ",  m )
         print("     Thanks!     ")


         with open('CR.json') as file:                                          # Adding operation to Json file
           json.dump = json.dumps(Operation)
         f.close()


       elif choice3 == 'no':
         print("Well, that's okay, let's start from begining!")
       else:
          print("Error")
    pass


    if choice == 'no':
       print("Goodbye! Hope see you later!")
       break
