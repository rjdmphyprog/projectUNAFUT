import simulation_cup as sc
import pylab
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class montecarlo_method:

	global simulation_league
	global simulation_league_init
	global simulation_league_init_twelve

	def simulation_league(n_runs):
		table_percentage_a = [['Alajuelense', 0, 0, 0, 0], ['Guadalupe', 0, 0, 0, 0], ['Perez Zeledon', 0, 0, 0, 0], ['Herediano', 0, 0, 0, 0], ['Santos', 0, 0, 0, 0], ['Grecia', 0, 0, 0, 0]]
		table_percentage_b = [['Jicaral', 0, 0, 0, 0], ['Limon', 0, 0, 0, 0], ['Sporting', 0, 0, 0, 0], ['Saprissa', 0, 0, 0, 0], ['San Carlos', 0, 0, 0, 0], ['Cartagines', 0, 0, 0, 0]]
		table_points = []
		table_verifying_position = [['Alajuelense', 0, 0, 0, 0, 0, 0], ['Guadalupe', 0, 0, 0, 0, 0, 0], ['Perez Zeledon', 0, 0, 0, 0, 0, 0],
									 ['Herediano', 0, 0, 0, 0, 0, 0], ['Santos', 0, 0, 0, 0, 0, 0], ['Grecia', 0, 0, 0, 0, 0, 0], 
									['Jicaral', 0, 0, 0, 0, 0, 0], ['Limon', 0, 0, 0, 0, 0, 0], ['Sporting', 0, 0, 0, 0, 0, 0], 
									['Saprissa', 0, 0, 0, 0, 0, 0], ['San Carlos', 0, 0, 0, 0, 0, 0], ['Cartagines', 0, 0, 0, 0, 0, 0]]
		table_percentage_a_second = [['Alajuelense', 0, 0, 0, 0], ['Guadalupe', 0, 0, 0, 0], ['Perez Zeledon', 0, 0, 0, 0], ['Herediano', 0, 0, 0, 0], ['Santos', 0, 0, 0, 0], ['Grecia', 0, 0, 0, 0]]
		table_percentage_b_second = [['Jicaral', 0, 0, 0, 0], ['Limon', 0, 0, 0, 0], ['Sporting', 0, 0, 0, 0], ['Saprissa', 0, 0, 0, 0], ['San Carlos', 0, 0, 0, 0], ['Cartagines', 0, 0, 0, 0]]
		table_points_second = []
		table_verifying_position_second = [['Alajuelense', 0, 0, 0, 0, 0, 0], ['Guadalupe', 0, 0, 0, 0, 0, 0], ['Perez Zeledon', 0, 0, 0, 0, 0, 0],
									 ['Herediano', 0, 0, 0, 0, 0, 0], ['Santos', 0, 0, 0, 0, 0, 0], ['Grecia', 0, 0, 0, 0, 0, 0], 
									['Jicaral', 0, 0, 0, 0, 0, 0], ['Limon', 0, 0, 0, 0, 0, 0], ['Sporting', 0, 0, 0, 0, 0, 0], 
									['Saprissa', 0, 0, 0, 0, 0, 0], ['San Carlos', 0, 0, 0, 0, 0, 0], ['Cartagines', 0, 0, 0, 0, 0, 0]]							
		last_team = [['Alajuelense', 0], ['Guadalupe', 0], ['Perez Zeledon', 0],
									 ['Herediano', 0], ['Santos', 0], ['Grecia', 0], 
									['Jicaral', 0], ['Limon', 0], ['Sporting', 0], 
									['Saprissa', 0], ['San Carlos', 0], ['Cartagines', 0]]
		for iter in range(29):
			table_points.append([iter + 20, 0, 0])
		for iter in range(29):
			table_points_second.append([iter + 20, 0, 0])
		#count_a = [0 for values in range(10, 49)]
		#count_b = [0 for values in range(10, 49)]
		iteration = []
		sumar=0
		suma = []

		for run in range(n_runs):
			first_a, second_a, first_b, second_b, final, champion, first_all, third_a, third_b, table_position, first_a_second, second_a_second, first_b_second, second_b_second, final_second, champion_second, first_all_second, third_a_second, third_b_second, table_position_second, table_general= sc.league()
			#AOERTURA
			for verify in range (len(table_percentage_a)):
				if first_a[1] == table_percentage_a[verify][0] or second_a[1] == table_percentage_a[verify][0]:
					table_percentage_a[verify][1] += 1
				if first_b[1] == table_percentage_b[verify][0] or second_b[1] == table_percentage_b[verify][0]:
					table_percentage_b[verify][1] += 1
				if champion == table_percentage_a[verify][0]:
					table_percentage_a[verify][4] += 1
				if champion == table_percentage_b[verify][0]:
					table_percentage_b[verify][4] += 1
				if first_all == table_percentage_b[verify][0]:
					table_percentage_b[verify][2] += 1
				elif first_all == table_percentage_a[verify][0]:
					table_percentage_a[verify][2] += 1
				for iter in range(2):
					if final[iter] == table_percentage_a[verify][0]:
						table_percentage_a[verify][3] += 1
					if final[iter] == table_percentage_b[verify][0]:
						table_percentage_b[verify][3] += 1
				
				for iter in range(len(table_points)):
					if table_points[iter][0] > third_a[6]:
						table_points[iter][1] += 1
					if table_points[iter][0] > third_b[6]:
						table_points[iter][2] += 1
			for verify in range (1, len(table_percentage_a) + 1):
				for iter in range(len(table_verifying_position)):
					if table_position[verify][1] == table_verifying_position[iter][0] or table_position[verify + 6][1] == table_verifying_position[iter][0]:
						table_verifying_position[iter][verify] += 1
			#CLAUSURA
			for verify in range (len(table_percentage_a_second)):
				if first_a_second[1] == table_percentage_a_second[verify][0] or second_a_second[1] == table_percentage_a_second[verify][0]:
					table_percentage_a_second[verify][1] += 1
				if first_b_second[1] == table_percentage_b_second[verify][0] or second_b_second[1] == table_percentage_b_second[verify][0]:
					table_percentage_b_second[verify][1] += 1
				if champion_second == table_percentage_a_second[verify][0]:
					table_percentage_a_second[verify][4] += 1
				if champion_second == table_percentage_b_second[verify][0]:
					table_percentage_b_second[verify][4] += 1
				if first_all_second == table_percentage_b_second[verify][0]:
					table_percentage_b_second[verify][2] += 1
				elif first_all_second == table_percentage_a_second[verify][0]:
					table_percentage_a_second[verify][2] += 1
				for iter in range(2):
					if final_second[iter] == table_percentage_a_second[verify][0]:
						table_percentage_a_second[verify][3] += 1
					if final_second[iter] == table_percentage_b_second[verify][0]:
						table_percentage_b_second[verify][3] += 1
				
				for iter in range(len(table_points_second)):
					if table_points_second[iter][0] > third_a_second[6]:
						table_points_second[iter][1] += 1
					if table_points_second[iter][0] > third_b_second[6]:
						table_points_second[iter][2] += 1
			for verify in range (1, len(table_percentage_a_second) + 1):
				for iter in range(len(table_verifying_position_second)):
					if table_position_second[verify][1] == table_verifying_position_second[iter][0] or table_position_second[verify + 6][1] == table_verifying_position_second[iter][0]:
						table_verifying_position_second[iter][verify] += 1
			for iter in range(len(last_team)):
				if last_team[iter][0] == table_general[12][1]:
					last_team[iter][1] += 1			
			"""sumar = table_percentage_a[1][1] / float(run + 1)
			iteration.append(run + 1)
			suma.append(sumar)
		fig = plt.figure()  
		axis = plt.axes(xlim =(0, n_runs), 
		                ylim =(0, 1.0))  
		  
		line, = axis.plot([], [], lw = 2)  
		   
		# what will our line dataset 
		# contain? 
		def init():  
		    line.set_data([], [])  
		    return line,  
		   
		# initializing empty values 
		# for x and y co-ordinates 
		xdata, ydata = [], []  
		   
		# animation function  
		def animate(i):  
		    # t is a parameter which varies 
		    # with the frame number 
		    # x, y values to be plotted  
		    x = iteration[i]
		    y = suma [i] 
		       
		    # appending values to the previously  
		    # empty x and y data holders  
		    xdata.append(x)  
		    ydata.append(y)  
		    line.set_data(xdata, ydata)  
		      
		    return line, 
		   
		# calling the animation function      
		anim = animation.FuncAnimation(fig, animate, init_func = init,  
		                               frames = int(n_runs), interval = 20000, blit = True)  
		   
		# saves the animation in our desktop 
		anim.save('animation.gif', writer='PillowWriter', fps=240)"""


		#pylab.plot (iteration, suma, 'o')                          #grafica de convergencia de los resultados conforme a las veces iteradas
		#pylab.show()
				#count_a[first_a[6] - 10] += 1
				#count_a[second_a[6] - 10] += 1
				#count_b[first_b[6] - 10] += 1
				#count_b[second_b[6] - 10] += 1"""
		return table_percentage_a, table_percentage_b, table_points, table_verifying_position, table_percentage_a_second, table_percentage_b_second, table_points_second, table_verifying_position_second, last_team

	def simulation_league_init(n_runs):
		table_percentage_a = [['Alajuelense', 0, 0, 0, 0], ['Guadalupe', 0, 0, 0, 0], ['Perez Zeledon', 0, 0, 0, 0], ['Herediano', 0, 0, 0, 0], ['Santos', 0, 0, 0, 0], ['Grecia', 0, 0, 0, 0]]
		table_percentage_b = [['Jicaral', 0, 0, 0, 0], ['Limon', 0, 0, 0, 0], ['Sporting', 0, 0, 0, 0], ['Saprissa', 0, 0, 0, 0], ['San Carlos', 0, 0, 0, 0], ['Cartagines', 0, 0, 0, 0]]
		table_points = []
		table_verifying_position = [['Alajuelense', 0, 0, 0, 0, 0, 0], ['Guadalupe', 0, 0, 0, 0, 0, 0], ['Perez Zeledon', 0, 0, 0, 0, 0, 0],
									 ['Herediano', 0, 0, 0, 0, 0, 0], ['Santos', 0, 0, 0, 0, 0, 0], ['Grecia', 0, 0, 0, 0, 0, 0], 
									['Jicaral', 0, 0, 0, 0, 0, 0], ['Limon', 0, 0, 0, 0, 0, 0], ['Sporting', 0, 0, 0, 0, 0, 0], 
									['Saprissa', 0, 0, 0, 0, 0, 0], ['San Carlos', 0, 0, 0, 0, 0, 0], ['Cartagines', 0, 0, 0, 0, 0, 0]]
		table_percentage_a_second = [['Alajuelense', 0, 0, 0, 0], ['Guadalupe', 0, 0, 0, 0], ['Perez Zeledon', 0, 0, 0, 0], ['Herediano', 0, 0, 0, 0], ['Santos', 0, 0, 0, 0], ['Grecia', 0, 0, 0, 0]]
		table_percentage_b_second = [['Jicaral', 0, 0, 0, 0], ['Limon', 0, 0, 0, 0], ['Sporting', 0, 0, 0, 0], ['Saprissa', 0, 0, 0, 0], ['San Carlos', 0, 0, 0, 0], ['Cartagines', 0, 0, 0, 0]]
		table_points_second = []
		table_verifying_position_second = [['Alajuelense', 0, 0, 0, 0, 0, 0], ['Guadalupe', 0, 0, 0, 0, 0, 0], ['Perez Zeledon', 0, 0, 0, 0, 0, 0],
									 ['Herediano', 0, 0, 0, 0, 0, 0], ['Santos', 0, 0, 0, 0, 0, 0], ['Grecia', 0, 0, 0, 0, 0, 0], 
									['Jicaral', 0, 0, 0, 0, 0, 0], ['Limon', 0, 0, 0, 0, 0, 0], ['Sporting', 0, 0, 0, 0, 0, 0], 
									['Saprissa', 0, 0, 0, 0, 0, 0], ['San Carlos', 0, 0, 0, 0, 0, 0], ['Cartagines', 0, 0, 0, 0, 0, 0]]							
		last_team = [['Alajuelense', 0], ['Guadalupe', 0], ['Perez Zeledon', 0],
									 ['Herediano', 0], ['Santos', 0], ['Grecia', 0], 
									['Jicaral', 0], ['Limon', 0], ['Sporting', 0], 
									['Saprissa', 0], ['San Carlos', 0], ['Cartagines', 0]]
		for iter in range(29):
			table_points.append([iter + 20, 0, 0])
		for iter in range(29):
			table_points_second.append([iter + 20, 0, 0])
		#count_a = [0 for values in range(10, 49)]
		#count_b = [0 for values in range(10, 49)]
		iteration = []
		sumar=0
		suma = []

		for run in range(n_runs):
			first_a, second_a, first_b, second_b, final, champion, first_all, third_a, third_b, table_position, first_a_second, second_a_second, first_b_second, second_b_second, final_second, champion_second, first_all_second, third_a_second, third_b_second, table_position_second, table_general= sc.league_init(9)
			#AOERTURA
			for verify in range (len(table_percentage_a)):
				if first_a[1] == table_percentage_a[verify][0] or second_a[1] == table_percentage_a[verify][0]:
					table_percentage_a[verify][1] += 1
				if first_b[1] == table_percentage_b[verify][0] or second_b[1] == table_percentage_b[verify][0]:
					table_percentage_b[verify][1] += 1
				if champion == table_percentage_a[verify][0]:
					table_percentage_a[verify][4] += 1
				if champion == table_percentage_b[verify][0]:
					table_percentage_b[verify][4] += 1
				if first_all == table_percentage_b[verify][0]:
					table_percentage_b[verify][2] += 1
				elif first_all == table_percentage_a[verify][0]:
					table_percentage_a[verify][2] += 1
				for iter in range(2):
					if final[iter] == table_percentage_a[verify][0]:
						table_percentage_a[verify][3] += 1
					if final[iter] == table_percentage_b[verify][0]:
						table_percentage_b[verify][3] += 1
				
				for iter in range(len(table_points)):
					if table_points[iter][0] > third_a[6]:
						table_points[iter][1] += 1
					if table_points[iter][0] > third_b[6]:
						table_points[iter][2] += 1
			for verify in range (1, len(table_percentage_a) + 1):
				for iter in range(len(table_verifying_position)):
					if table_position[verify][1] == table_verifying_position[iter][0] or table_position[verify + 6][1] == table_verifying_position[iter][0]:
						table_verifying_position[iter][verify] += 1
			#CLAUSURA
			for verify in range (len(table_percentage_a_second)):
				if first_a_second[1] == table_percentage_a_second[verify][0] or second_a_second[1] == table_percentage_a_second[verify][0]:
					table_percentage_a_second[verify][1] += 1
				if first_b_second[1] == table_percentage_b_second[verify][0] or second_b_second[1] == table_percentage_b_second[verify][0]:
					table_percentage_b_second[verify][1] += 1
				if champion_second == table_percentage_a_second[verify][0]:
					table_percentage_a_second[verify][4] += 1
				if champion_second == table_percentage_b_second[verify][0]:
					table_percentage_b_second[verify][4] += 1
				if first_all_second == table_percentage_b_second[verify][0]:
					table_percentage_b_second[verify][2] += 1
				elif first_all_second == table_percentage_a_second[verify][0]:
					table_percentage_a_second[verify][2] += 1
				for iter in range(2):
					if final_second[iter] == table_percentage_a_second[verify][0]:
						table_percentage_a_second[verify][3] += 1
					if final_second[iter] == table_percentage_b_second[verify][0]:
						table_percentage_b_second[verify][3] += 1
				
				for iter in range(len(table_points_second)):
					if table_points_second[iter][0] > third_a_second[6]:
						table_points_second[iter][1] += 1
					if table_points_second[iter][0] > third_b_second[6]:
						table_points_second[iter][2] += 1
			for verify in range (1, len(table_percentage_a_second) + 1):
				for iter in range(len(table_verifying_position_second)):
					if table_position_second[verify][1] == table_verifying_position_second[iter][0] or table_position_second[verify + 6][1] == table_verifying_position_second[iter][0]:
						table_verifying_position_second[iter][verify] += 1
			for iter in range(len(last_team)):
				if last_team[iter][0] == table_general[12][1]:
					last_team[iter][1] += 1			
			"""sumar = table_percentage_a[1][1] / float(run + 1)
			iteration.append(run + 1)
			suma.append(sumar)"""
		"""fig = plt.figure()  
		axis = plt.axes(xlim =(0, n_runs), 
		                ylim =(0, 1.0))  
		  
		line, = axis.plot([], [], lw = 2)  
		   
		# what will our line dataset 
		# contain? 
		def init():  
		    line.set_data([], [])  
		    return line,  
		   
		# initializing empty values 
		# for x and y co-ordinates 
		xdata, ydata = [], []  
		   
		# animation function  
		def animate(i):  
		    # t is a parameter which varies 
		    # with the frame number 
		    # x, y values to be plotted  
		    x = iteration[i]
		    y = suma [i] 
		       
		    # appending values to the previously  
		    # empty x and y data holders  
		    xdata.append(x)  
		    ydata.append(y)  
		    line.set_data(xdata, ydata)  
		      
		    return line, 
		   
		# calling the animation function      
		anim = animation.FuncAnimation(fig, animate, init_func = init,  
		                               frames = int(n_runs), interval = 20000, blit = True)  
		   
		# saves the animation in our desktop 
		anim.save('animation.gif', writer='PillowWriter', fps=240)


		#pylab.plot (iteration, suma, 'o')                          #grafica de convergencia de los resultados conforme a las veces iteradas
		#pylab.show()
				#count_a[first_a[6] - 10] += 1
				#count_a[second_a[6] - 10] += 1
				#count_b[first_b[6] - 10] += 1
				#count_b[second_b[6] - 10] += 1"""
		return table_percentage_a, table_percentage_b, table_points, table_verifying_position, table_percentage_a_second, table_percentage_b_second, table_points_second, table_verifying_position_second, last_team

	def simulation_league_init_twelve(n_runs):
		table_percentage_a = [['Alajuelense', 0, 0, 0, 0], ['Guadalupe', 0, 0, 0, 0], ['Perez Zeledon', 0, 0, 0, 0], ['Herediano', 0, 0, 0, 0], ['Santos', 0, 0, 0, 0], ['Grecia', 0, 0, 0, 0]]
		table_percentage_b = [['Jicaral', 0, 0, 0, 0], ['Limon', 0, 0, 0, 0], ['Sporting', 0, 0, 0, 0], ['Saprissa', 0, 0, 0, 0], ['San Carlos', 0, 0, 0, 0], ['Cartagines', 0, 0, 0, 0]]
		table_points = []
		table_verifying_position = [['Alajuelense', 0, 0, 0, 0, 0, 0], ['Guadalupe', 0, 0, 0, 0, 0, 0], ['Perez Zeledon', 0, 0, 0, 0, 0, 0],
									 ['Herediano', 0, 0, 0, 0, 0, 0], ['Santos', 0, 0, 0, 0, 0, 0], ['Grecia', 0, 0, 0, 0, 0, 0], 
									['Jicaral', 0, 0, 0, 0, 0, 0], ['Limon', 0, 0, 0, 0, 0, 0], ['Sporting', 0, 0, 0, 0, 0, 0], 
									['Saprissa', 0, 0, 0, 0, 0, 0], ['San Carlos', 0, 0, 0, 0, 0, 0], ['Cartagines', 0, 0, 0, 0, 0, 0]]
		table_percentage_a_second = [['Alajuelense', 0, 0, 0, 0], ['Guadalupe', 0, 0, 0, 0], ['Perez Zeledon', 0, 0, 0, 0], ['Herediano', 0, 0, 0, 0], ['Santos', 0, 0, 0, 0], ['Grecia', 0, 0, 0, 0]]
		table_percentage_b_second = [['Jicaral', 0, 0, 0, 0], ['Limon', 0, 0, 0, 0], ['Sporting', 0, 0, 0, 0], ['Saprissa', 0, 0, 0, 0], ['San Carlos', 0, 0, 0, 0], ['Cartagines', 0, 0, 0, 0]]
		table_points_second = []
		table_verifying_position_second = [['Alajuelense', 0, 0, 0, 0, 0, 0], ['Guadalupe', 0, 0, 0, 0, 0, 0], ['Perez Zeledon', 0, 0, 0, 0, 0, 0],
									 ['Herediano', 0, 0, 0, 0, 0, 0], ['Santos', 0, 0, 0, 0, 0, 0], ['Grecia', 0, 0, 0, 0, 0, 0], 
									['Jicaral', 0, 0, 0, 0, 0, 0], ['Limon', 0, 0, 0, 0, 0, 0], ['Sporting', 0, 0, 0, 0, 0, 0], 
									['Saprissa', 0, 0, 0, 0, 0, 0], ['San Carlos', 0, 0, 0, 0, 0, 0], ['Cartagines', 0, 0, 0, 0, 0, 0]]							
		last_team = [['Alajuelense', 0], ['Guadalupe', 0], ['Perez Zeledon', 0],
									 ['Herediano', 0], ['Santos', 0], ['Grecia', 0], 
									['Jicaral', 0], ['Limon', 0], ['Sporting', 0], 
									['Saprissa', 0], ['San Carlos', 0], ['Cartagines', 0]]
		for iter in range(29):
			table_points.append([iter + 20, 0, 0])
		for iter in range(29):
			table_points_second.append([iter + 20, 0, 0])
		#count_a = [0 for values in range(10, 49)]
		#count_b = [0 for values in range(10, 49)]
		iteration = []
		sumar=0
		suma = []

		for run in range(n_runs):
			first_a, second_a, first_b, second_b, final, champion, first_all, third_a, third_b, table_position, first_a_second, second_a_second, first_b_second, second_b_second, final_second, champion_second, first_all_second, third_a_second, third_b_second, table_position_second, table_general= sc.league_init_twelve(16)
			#AOERTURA
			for verify in range (len(table_percentage_a)):
				if first_a[1] == table_percentage_a[verify][0] or second_a[1] == table_percentage_a[verify][0]:
					table_percentage_a[verify][1] += 1
				if first_b[1] == table_percentage_b[verify][0] or second_b[1] == table_percentage_b[verify][0]:
					table_percentage_b[verify][1] += 1
				if champion == table_percentage_a[verify][0]:
					table_percentage_a[verify][4] += 1
				if champion == table_percentage_b[verify][0]:
					table_percentage_b[verify][4] += 1
				if first_all == table_percentage_b[verify][0]:
					table_percentage_b[verify][2] += 1
				elif first_all == table_percentage_a[verify][0]:
					table_percentage_a[verify][2] += 1
				for iter in range(2):
					if final[iter] == table_percentage_a[verify][0]:
						table_percentage_a[verify][3] += 1
					if final[iter] == table_percentage_b[verify][0]:
						table_percentage_b[verify][3] += 1
				
				for iter in range(len(table_points)):
					if table_points[iter][0] > third_a[6]:
						table_points[iter][1] += 1
					if table_points[iter][0] > third_b[6]:
						table_points[iter][2] += 1
			for verify in range (1, len(table_percentage_a) + 1):
				for iter in range(len(table_verifying_position)):
					if table_position[verify][1] == table_verifying_position[iter][0] or table_position[verify + 6][1] == table_verifying_position[iter][0]:
						table_verifying_position[iter][verify] += 1
			#CLAUSURA
			for verify in range (len(table_percentage_a_second)):
				if first_a_second[1] == table_percentage_a_second[verify][0] or second_a_second[1] == table_percentage_a_second[verify][0]:
					table_percentage_a_second[verify][1] += 1
				if first_b_second[1] == table_percentage_b_second[verify][0] or second_b_second[1] == table_percentage_b_second[verify][0]:
					table_percentage_b_second[verify][1] += 1
				if champion_second == table_percentage_a_second[verify][0]:
					table_percentage_a_second[verify][4] += 1
				if champion_second == table_percentage_b_second[verify][0]:
					table_percentage_b_second[verify][4] += 1
				if first_all_second == table_percentage_b_second[verify][0]:
					table_percentage_b_second[verify][2] += 1
				elif first_all_second == table_percentage_a_second[verify][0]:
					table_percentage_a_second[verify][2] += 1
				for iter in range(2):
					if final_second[iter] == table_percentage_a_second[verify][0]:
						table_percentage_a_second[verify][3] += 1
					if final_second[iter] == table_percentage_b_second[verify][0]:
						table_percentage_b_second[verify][3] += 1
				
				for iter in range(len(table_points_second)):
					if table_points_second[iter][0] > third_a_second[6]:
						table_points_second[iter][1] += 1
					if table_points_second[iter][0] > third_b_second[6]:
						table_points_second[iter][2] += 1
			for verify in range (1, len(table_percentage_a_second) + 1):
				for iter in range(len(table_verifying_position_second)):
					if table_position_second[verify][1] == table_verifying_position_second[iter][0] or table_position_second[verify + 6][1] == table_verifying_position_second[iter][0]:
						table_verifying_position_second[iter][verify] += 1
			for iter in range(len(last_team)):
				if last_team[iter][0] == table_general[12][1]:
					last_team[iter][1] += 1			
			"""sumar = table_percentage_a[1][1] / float(run + 1)
			iteration.append(run + 1)
			suma.append(sumar)"""
		"""fig = plt.figure()  
		axis = plt.axes(xlim =(0, n_runs), 
		                ylim =(0, 1.0))  
		  
		line, = axis.plot([], [], lw = 2)  
		   
		# what will our line dataset 
		# contain? 
		def init():  
		    line.set_data([], [])  
		    return line,  
		   
		# initializing empty values 
		# for x and y co-ordinates 
		xdata, ydata = [], []  
		   
		# animation function  
		def animate(i):  
		    # t is a parameter which varies 
		    # with the frame number 
		    # x, y values to be plotted  
		    x = iteration[i]
		    y = suma [i] 
		       
		    # appending values to the previously  
		    # empty x and y data holders  
		    xdata.append(x)  
		    ydata.append(y)  
		    line.set_data(xdata, ydata)  
		      
		    return line, 
		   
		# calling the animation function      
		anim = animation.FuncAnimation(fig, animate, init_func = init,  
		                               frames = int(n_runs), interval = 20000, blit = True)  
		   
		# saves the animation in our desktop 
		anim.save('animation.gif', writer='PillowWriter', fps=240)


		#pylab.plot (iteration, suma, 'o')                          #grafica de convergencia de los resultados conforme a las veces iteradas
		#pylab.show()
				#count_a[first_a[6] - 10] += 1
				#count_a[second_a[6] - 10] += 1
				#count_b[first_b[6] - 10] += 1
				#count_b[second_b[6] - 10] += 1"""
		return table_percentage_a, table_percentage_b, table_points, table_verifying_position, table_percentage_a_second, table_percentage_b_second, table_points_second, table_verifying_position_second, last_team