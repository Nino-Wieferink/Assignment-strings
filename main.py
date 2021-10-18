# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#Part 1
#1
gullit = 'Ruud Gullit'
van_basten = 'Marco van Basten'
#2
goal_0 = 32
goal_1 = 54
#3
scorers = gullit + " " + str(goal_0) + ", " + van_basten + " " + str(goal_1)
#4
report = f"{gullit} scored in the {goal_0}nd minute\n{van_basten} scored in the {goal_1}th minute"
print(scorers)
print(report)

#Part 2
#1
player = 'Berry van Aerle'
#2
first_name = player[:5]
#3
last_name_start = player.find("v")
last_name = player[last_name_start:]
last_name_len = len(last_name)
print(last_name_len)
#4
initial_num = player.find("B")
initial_let = player[initial_num:1]
initial_capital = initial_let + ". "
name_short = initial_capital + last_name
print(name_short)
#5
first_name_num = player.find("B")
first_name = player[first_name_num:5]
chant =  f'{first_name}! ' * len(first_name)
chant = chant[:-1]
print(chant)
#6
good_chant = chant != " "
print(good_chant)