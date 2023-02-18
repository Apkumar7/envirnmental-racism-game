import random
import time
time.sleep(2)
job= random.choice(['Janitor','truck driver','Techniction','user','docter', 'bioligist'])
trash_saftey = random.choice
health = 100
happyness = 100
keep_playing = ''
trash = ["hazardous", "safe"]
names = ["John Doe (father - one child)", "Jane Doe (mother - one child)",'Jackson Doe (child)']
money = [100,300,500,1000,550,3000,3012]
character = random.choice(names)
money_amount = random.choice(money)
print(f'Welcome to the adventure game where you will experience the stark contrast between what it is like for many people of color on a daily basis VS. those who do not have to face enviornmental racism. You will be walking in the shoes of {character} today.')
time.sleep(2)

print(f'\nCharater Stats:\nYou have ${money_amount} and your health is at {health}. Happyness is currently at {happyness}. Good luck. We hope that your empathy increases and your become more informed of the ongoing issue of environemntal racism.\n')
time.sleep(2)
while keep_playing.lower() != 'no':
  answer = input("\nYou wake up as a sweaty mess, your throat is dry. In the dark you get out of bed and head to the kitchen. You find that you are all out of clean water. Do you want to DRINK the water that you have, or go FIND some clean water? ")
  print()
  time.sleep(2)
  if answer.capitalize() == 'Find':
    print('You check on your siblngs and then head out to the nearest fresh water source carrying buckets. They will be thirsty as well. You walk 4 miles and it takes you an hour to get their. You take big gulps of water and fill up your buckets. You start the long trek home sloshing water as you go. Your arms tire and you take frequent breaks. The sun is starting to rise, you will be back in time to start on some breakfast. \n')
    time.sleep(2)
    health += 20
    happyness += 20
    print(f"\nHealth: {health}\nHappyness:{happyness}\nMoney:${money_amount}")
    break
    time.sleep(2)
  elif answer.capitalize() == 'Drink':
    print('You drink the mirkey polluted water knowing that you will most likely get sick, but you do not want to have to walk all the way to the fresh water source. You go back to sleep so at least you get to sleep in. ')
    time.sleep(2)
    health -= 5
    happyness -= 2
    print(f"\nHealth: {health}\nHappyness:{happyness}\nMoney:${money_amount}")
    time.sleep(2)
    answer_drink = input(f"\nYou wake up with a terrible belly ache, the water DID make you ill. You do not have access to health care but you do have ${money_amount} money to spend. You still need to buy food for the week. Would you like to buy MEDICINE or FOOD? ")
    time.sleep(2)
    if answer_drink.capitalize() == "Food":
      print("\nYou are able to buy some food for you and your siblings, but you are still sick. At least your stomach is full.")
      time.sleep(2)
      happyness -= 2
      health -= 3
      print(f"\nHealth: {health}\nHappyness:{happyness}\nMoney:${money_amount}")
      time.sleep(2)
      answer_food = input('\nYou were walking back home and you found some trash lying on the floor, do you want to PICK it up or do you want to LEAVE it alone? ')
      time.sleep(2)
      if answer_food.capatalize() == 'Pick': 
        trash_saftey = random.choice(trash)
        print(f'\nThe trash you picked up was {trash_saftey}!')
      elif answer_food.capitalize() == 'Leave':
        print("\nYou left the trash where it was. Who knows if it was hazardous or safe. ")
        break
        time.sleep(2)
    elif answer_drink.capitalize() == "Medicine" :
      print("\nYou choose to buy some medicine. As you travel to get the medicine you need, you encounter air pollution. You inhale harmful things that are detrimental to your health. Since you spent most of your money on medicine, you and your family will only have a little food to share.")
      time.sleep(2)
      answer_medicine = input("\nDo you want to BUY a mask to help the air polution or you can CONTINUE to breath in the air? ")
      time.sleep(2)
      if answer_medicine.capitalize() == 'BUY':
        print('\nYou see a store in front of you so you walk inside, you buy a mask and continue walking.')
        time.sleep(2)
        break
      if answer_medicine.capitalize() == 'continue':
        happyness +=0
        health -=2
        money -=3
        breakpoint
      print(f"\nHealth: {health}\nHappyness:{happyness}\nMoney:${money_amount}")
      break
time.sleep(2)
print("\nEnvironmental Racism:Environmental racism, a form of systemic racism whereby communities of colour are disproportionately burdened with health hazards through policies and practices that force them to live in proximity to sources of toxic waste such as sewage works, mines, landfills, power stations, major roads and emitters of airborne particulate matter. As a result, these communities suffer greater rates of health problems attendant on hazardous pollutants. ")
time.sleep(5)
print("Thanks for playing.Goodbye!")
        
        
 
    
      
      
        