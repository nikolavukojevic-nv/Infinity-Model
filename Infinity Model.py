# Infinity Model

## 1. Introduction

state1 = 1
while state1 > 0:
	

	state2 = input('do you want to let me on or shut me off? [on/off] ')
	
	if state2 == 'on':
		print('\n')
		## 2. Independent Variables
		observable = input('describe observation: ')
		mass = float(input('enter mass of the observation [g]: '))
		position = float(input('enter position of the observation [m]: '))
		time = float(input('enter time of the observation [s]: '))
		'''
		time_2 = float(input('enter another time of the observation [s]: ')) 
		'''
		money = float(input('enter money of the observation [M or local currency e.g. €]: '))
	
		print('\n--------------\n > observation: ',observable,
		'\n-----',
		'\n > mass: ',mass,'g',
		'\n > position: ',position,'m',
		'\n > time: ',time,'s',
		'\n > money: ',money,'M',
		'\n--------------')
	
		## 3. Model
		
		### 3.1 Calculations
		
		velocity = position / time
		acceleration = velocity / time
		force = mass * acceleration
		work = force * position
		power = work / time
		robustness = power / time
		
		simple_strength = robustness / money
		simple_weakness = robustness / ((-1) * money)
		
		true_strength = simple_strength / simple_weakness
		true_weakness = simple_weakness / simple_strength
		
		realness = true_strength / true_weakness
		perfect = true_weakness / true_strength
		
		everything = realness / perfect
		nothing = perfect / realness
		
		wholeness = ((everything + nothing)/2) * 2
		halfeness = ((everything + nothing)/2)
		
		realistic = wholeness / money
		utility = realistic / money
		practicality = utility / simple_strength
		
		fun = practicality * time
		seriousness = practicality / time
		
		humbleness = fun / seriousness
		marginalism = seriousness / fun
		
		strongholding = humbleness / marginalism
		strongholding_attack = strongholding * simple_strength
		strongholding_defense = strongholding / simple_strength
		
		honor = strongholding_attack / strongholding_defense
		pride = strongholding * honor
		practical_strength = pride / work
		best = practical_strength * money
		very_best = best * 1.2   # increasing factor is set intuitively 
		maximum_black = very_best * 85000   # large jump; increasing factor is set intuitively 
		
		#### 3.1.1 Outputs
		
		print(' • simple strength: ',simple_strength)
		print(' • utility: ',utility)
		print(' >> maximum black: ',maximum_black,'\n--------------')
		print('\n----------------\n> the one which has the most of it!\n----------------\n')
		
		### 3.3 Model Performance
		'''Calculating the performance of the model, which is equal to the amount of variables or observations.
		'''
	
	else:
		print('\noff ...')

		
	state1 = state1 + 1
	

