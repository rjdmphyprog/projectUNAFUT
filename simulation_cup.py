import random
import pandas as pd

class simulation_cup:

	global probability
	global detection_result
	global league
	global league_init
	global league_init_twelve
	global dataframe
	global detection_goals

	global table_teams
	global table_days
	global table_goals
	global table_draws
	global table_goals_loser
	global table_historical
	
	data_unafut = pd.ExcelFile("unafut.xlsx")
	table_teams = data_unafut.parse("unafut")
	table_days = data_unafut.parse("jornadas")
	table_goals = data_unafut.parse("wins")
	table_draws = data_unafut.parse("draws")
	table_goals_loser = data_unafut.parse("goals_loser")

	def dataframe():            #Crea una tabla con los equipos y sus pesos de ganar, perder o empatar
		teams=[["posicion", "Equipo", "Partidos", "Ganes", "Empate", "Perdidas"]]
		for row in range(1, table_teams.shape[0] + 1):
			for column in range(6):
				if column==0:
					teams.append([row])
				else:
					teams[row].append(table_teams.iloc[row-1][column])
		return teams

	def data_days():           #Crea una tabla con las jornadas
		days = [["day", "home", "visit", "home", "visit", "home", "visit", "home", "visit", "home", "visit", "home", "visit"]]
		for row in range (1, table_days.shape[0] + 1):
			for column in range (13):
				if column==0:
					days.append([row])
				else:
					days[row].append(table_days.iloc[row - 1][column])
		return days

	def data_goals():           #Crea una tabla con las jornadas
		goals_list = [["goals", "Percentage"],]
		for row in range (1, table_goals.shape[0] + 1):
			for column in range (len(goals_list[0])):
				if column == 0:
					goals_list.append([row])
				else:
					goals_list[row].append(table_goals.iloc[row - 1][column])
		return goals_list

	def data_draws():           #Crea una tabla con las jornadas
		draws_list = [["goals", "Percentage"],]
		for row in range (1, table_draws.shape[0] + 1):
			for column in range (len(draws_list[0])):
				if column == 0:
					draws_list.append([row - 1])
				else:
					draws_list[row].append(table_draws.iloc[row - 1][column])
		return draws_list

	def data_goals_loser():           #Crea una tabla con las jornadas
		goals_loser_list = [["goals", "Percentage"],]
		for row in range (1, table_goals_loser.shape[0] + 1):
			for column in range (len(goals_loser_list[0])):
				if column == 0:
					goals_loser_list.append([row - 1])
				else:
					goals_loser_list[row].append(table_goals_loser.iloc[row - 1][column])
		return goals_loser_list
	
	table_historical = tuple(dataframe())
	table_days = data_days()
	table_goals = data_goals()
	table_draws = data_draws()
	table_goals_loser = data_goals_loser()

	def probability(home, visit, table, n):
		percentage_home, percentage_draw = 0, 0
		sum_draw = 0
		for iter in range(1, len(table)):
			sum_draw = sum_draw + table[iter][4] / table[iter][2]
		percentage_draw = sum_draw/float(len(table) - 1)
		for iter in range(1, len(table)):
			if home == table[iter][1]:
				if table[iter][2] - table_historical[iter][2] == 0:
					percentage_home = (2 * max(0.5, n) + table_historical[iter][3] / table_historical[iter][2] + 2 * max((1- percentage_draw)/2, 0))/5
				else:	
					percentage_home = (2 * max(0.5, n) + table_historical[iter][3] / table_historical[iter][2] + 2 * max((1- percentage_draw)/2, (table[iter][3] - table_historical[iter][3]) / (table[iter][2] - table_historical[iter][2])))/5
		return percentage_home, percentage_home + percentage_draw, 1.0

	def detection_result(home, visit, table, n):
		limit_home_win, limit_draw, limit_visit_win = probability(home, visit, table, n)
		home_win, draw, visit_win = False, False, False
		result = random.random()
		if result < limit_home_win:
			home_win = True
		elif limit_home_win <= result < limit_draw:
			draw = True
		else:
			visit_win = True
		return home_win, draw, visit_win

	def detection_goals(home_win, draw, visit_win):
		arr_loser = [0.0, table_goals_loser[1][1], table_goals_loser[1][1] + table_goals_loser[2][1], 
					table_goals_loser[1][1] + table_goals_loser[2][1] + table_goals_loser[3][1], 1.0]
		
		arr_draws = [0.0,table_draws[1][1], table_draws[1][1] + table_draws[2][1], 
					table_draws[1][1] + table_draws[2][1] + table_draws[3][1], 1.0]
		
		arr_goals = [0.0, table_goals[1][1], table_goals[1][1] + table_goals[2][1], 
					table_goals[1][1] + table_goals[2][1] + table_goals[3][1], 
					table_goals[1][1] + table_goals[2][1] + table_goals[3][1] + table_goals[4][1], 1.0]

		if home_win:
			criteria_loser = random.random()
			criteria_difference = random.random()
			for iter in range(len(arr_loser) - 1):
				if arr_loser[iter] <= criteria_loser < arr_loser[iter + 1]:
					visit_goal = table_goals_loser[iter + 1][0]
			for iter in range(len(arr_goals) - 1):
				if arr_goals[iter] <= criteria_difference < arr_goals[iter + 1]:
					home_goal = table_goals[iter + 1][0] + visit_goal
		elif visit_win:
			criteria_loser = random.random()
			criteria_difference = random.random()
			for iter in range(len(arr_loser) - 1):
				if arr_loser[iter] <= criteria_loser < arr_loser[iter + 1]:
					home_goal = table_goals_loser[iter + 1][0]
			for iter in range(len(arr_goals) - 1):
				if arr_goals[iter] <= criteria_difference < arr_goals[iter + 1]:
					visit_goal = table_goals[iter + 1][0] + home_goal
		elif draw:
			criteria_draw = random.random()
			for iter in range(len(arr_draws) - 1):
				if arr_draws[iter] <= criteria_draw < arr_draws[iter + 1]:
					home_goal = table_draws[iter + 1][0]
					visit_goal = home_goal
		return home_goal, visit_goal
	
	def league( ):
		#TORNEO DE APERTURA 2020-2021
		table_position = [["Posicion", "Equipo", "Total", "Ganes", "Empates", "Perdidas", "Puntos", "Favor", "Contra"],  [1, 'Alajuelense', 0, 0, 0, 0, 0, 0, 0], [2, 'Perez Zeledon', 0, 0, 0, 0, 0, 0, 0], 
					[3, 'Grecia', 0, 0, 0, 0, 0, 0, 0], [4, 'Santos', 0, 0, 0, 0, 0, 0, 0], [5, 'Herediano', 0, 0, 0, 0, 0, 0, 0], [6, 'Guadalupe', 0, 0, 0, 0, 0, 0, 0],
					[7, 'Jicaral', 0, 0, 0, 0, 0, 0, 0], [8, 'San Carlos', 0, 0, 0, 0, 0, 0, 0], [9, 'Sporting', 0, 0, 0, 0, 0, 0, 0], [10, 'Saprissa', 0, 0, 0, 0, 0, 0, 0], 
					[11, 'Limon', 0, 0, 0, 0, 0, 0, 0], [12, 'Cartagines', 0, 0, 0, 0, 0, 0, 0]]
		count_home_win = 0
		table_teams_updating = dataframe()
		limit_iter = int((len(table_days[0]) + 1) / 2)
		for day in range(1, len(table_days)):
			for iter in range(1, limit_iter):
				n = count_home_win/((day -1) * (limit_iter - 1) + iter)
				home_win, draw, visit_win = detection_result(table_days[day][2 * iter - 1], table_days[day][2 * iter], table_teams_updating, n) #Itera los partidos
				home_goal, visit_goal = detection_goals(home_win, draw, visit_win,)
				for verify in range (1, 13):
					for verify_b in range(1, len(table_teams_updating )):
						if table_days[day][2 * iter - 1] == table_position[verify][1] and table_days[day][2 * iter - 1] == table_teams_updating[verify_b][1]:   #Cada if me calcula lo necesario cuando gana, empata o piede alguien
							table_position[verify][7] += home_goal
							table_position[verify][8] += visit_goal
							if home_win:
								table_position[verify][2] += 1
								table_position[verify][3] += 1
								table_position[verify][6] += 3
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][3] += 1
								count_home_win +=1
							elif draw:
								table_position[verify][2] += 1
								table_position[verify][4] += 1
								table_position[verify][6] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][4] += 1
							elif visit_win:
								table_position[verify][2] += 1
								table_position[verify][5] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][5] += 1
				for verify in range (1, 13):
					for verify_b in range(1, len(table_teams_updating)):
						if table_days[day][2 * iter] == table_position[verify][1] and table_days[day][2 * iter] == table_teams_updating[verify_b][1]:
							table_position[verify][8] += home_goal
							table_position[verify][7] += visit_goal
							if home_win:
								table_position[verify][2] += 1
								table_position[verify][5] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][5] += 1
								home_win = False
							if draw:
								table_position[verify][2] += 1
								table_position[verify][4] += 1
								table_position[verify][6] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][4] += 1
								draw = False
							if visit_win:
								table_position[verify][2] += 1
								table_position[verify][3] += 1
								table_position[verify][6] += 3
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][3] += 1
								visit_win = False
		change_factor_a = [0, "", 0, 0, 0, 0, 0] 
		change_factor_b = [0, "", 0, 0, 0, 0, 0]                       #Esta parte me ordena de mayo a menor, criterio puntos
		for serie in range (5):
			for change in range(1, 6):
				if table_position[change][6] < table_position[change + 1][6]:
					change_factor_a[1:9] = table_position[change][1:9]
					table_position[change][1:9] = table_position[change + 1][1:9]
					table_position[change + 1][1:9] = change_factor_a[1:9]
				elif table_position[change][6] == table_position[change + 1][6]:
					if table_position[change][7] - table_position[change][8] < table_position[change + 1][7] - table_position[change + 1][8]:
						change_factor_a[1:9] = table_position[change][1:9]
						table_position[change][1:9] = table_position[change + 1][1:9]
						table_position[change + 1][1:9] = change_factor_a[1:9]
					elif table_position[change][7] - table_position[change][8] == table_position[change + 1][7] - table_position[change + 1][8]:
						if table_position[change][7] < table_position[change + 1][7]:
							change_factor_a[1:9] = table_position[change][1:9]
							table_position[change][1:9] = table_position[change + 1][1:9]
							table_position[change + 1][1:9] = change_factor_a[1:9]


				if table_position[change + 6][6] < table_position[change + 7][6]:
					change_factor_b[1:9] = table_position[change + 6][1:9]
					table_position[change + 6][1:9] = table_position[change + 7][1:9]
					table_position[change + 7][1:9] = change_factor_b[1:9]
				elif table_position[change + 6][6] == table_position[change + 7][6]:
					if table_position[change + 6][7] - table_position[change + 6][8] < table_position[change + 7][7] - table_position[change + 7][8]:
						change_factor_b[1:9] = table_position[change + 6][1:9]
						table_position[change + 6][1:9] = table_position[change + 7][1:9]
						table_position[change + 7][1:9] = change_factor_b[1:9]
					elif table_position[change + 6][7] - table_position[change + 6][8] == table_position[change + 7][7] - table_position[change + 7][8]:
						if table_position[change + 6][7] < table_position[change + 7][7]:
							change_factor_b[1:9] = table_position[change + 6][1:9]
							table_position[change + 6][1:9] = table_position[change + 7][1:9]
							table_position[change + 7][1:9] = change_factor_b[1:9]

		if table_position[1][6] >= table_position[7][6]:
			first_all = table_position[1][1]
			second_all = table_position[7][1]
		else:
			first_all = table_position[7][1]
			second_all = table_position[1][1]

		if table_position[2][6] >= table_position[8][6]:
			third_all = table_position[2][1]
			fourth_all = table_position[8][1]
		else:
			third_all = table_position[8][1]
			fourth_all = table_position[2][1]

		finalist = [first_all, second_all, third_all, fourth_all]
		#SEMI-FINALS
		final = ["", ""]
		for iter in range(1, 3):
			#FIRST LEG
			home_win, draw, visit_win = detection_result(table_position[iter][1], table_position[9 - iter][1], table_teams_updating, n)
			home_goal_first, visit_goal_first = detection_goals(home_win, draw, visit_win)
			#SECOND LEG
			home_win, draw, visit_win = detection_result(table_position[9 - iter][1], table_position[iter][1], table_teams_updating, n)
			home_goal_second, visit_goal_second = detection_goals(home_win, draw, visit_win)
			
			if home_goal_first + visit_goal_second > visit_goal_first + home_goal_second:
				final[iter - 1] = table_position[iter][1]
			elif home_goal_first + visit_goal_second < visit_goal_first + home_goal_second:
				final[iter - 1] = table_position[9 - iter][1]
			else:
				if  home_goal_first + 2 * visit_goal_second > 2 * visit_goal_first + home_goal_second:
					final[iter - 1] = table_position[iter][1]
				elif home_goal_first + 2 * visit_goal_second < 2 * visit_goal_first + home_goal_second:
					final[iter - 1] = table_position[9 - iter][1]
				else:
					verify = 0
					while verify < 1:
						if iter == 1:
							home_win, draw, visit_win = detection_result(table_position[iter][1], table_position[9 - iter][1], table_teams_updating, n)
							if home_win:
								final[0] = table_position[iter][1]
								verify = verify + 1
							elif visit_win:
								final[0] = table_position[9 - iter][1]
								verify = verify + 1
							elif draw:
								draw = False
								pass
						else:
							home_win, draw, visit_win = detection_result(table_position[9 - iter][1], table_position[iter][1], table_teams_updating, n)
							if home_win:
								final[1] = table_position[9 - iter][1]
								verify = verify + 1
							elif visit_win:
								final[1] = table_position[iter][1]
								verify = verify + 1
							elif draw:
								draw = False
								pass	

		#FINAL
		for iter in range(len(finalist)):
			for verify in range (len(finalist)):
				if final[0] == finalist[iter] and final[1] == finalist[verify]:
					if iter > verify:
						home_win, draw, visit_win = detection_result(final[0], final[1], table_teams_updating, n)
						home_goal_first, visit_goal_first = detection_goals(home_win, draw, visit_win)
							#SECOND LEG
						home_win, draw, visit_win = detection_result(final[1], final[0], table_teams_updating, n)
						home_goal_second, visit_goal_second = detection_goals(home_win, draw, visit_win)

						if home_goal_first + visit_goal_second > visit_goal_first + home_goal_second:
							champion = final[0]
						elif home_goal_first + visit_goal_second < visit_goal_first + home_goal_second:
							champion = final[1]
						else:
							rolo = 0
							while rolo < 1:
								home_win, draw, visit_win = detection_result(final[1], final[0], table_teams_updating, n)
								if home_win:
									champion = final[1]
									rolo = rolo + 1
								elif visit_win:
									champion = final[0]
									rolo = rolo + 1
								elif draw:
									draw = False
									pass

					if iter < verify:
						home_win, draw, visit_win = detection_result(final[1], final[0], table_teams_updating, n)
						home_goal_first, visit_goal_first = detection_goals(home_win, draw, visit_win)
							#SECOND LEG
						home_win, draw, visit_win = detection_result(final[0], final[1], table_teams_updating, n)
						home_goal_second, visit_goal_second = detection_goals(home_win, draw, visit_win)

						if home_goal_first + visit_goal_second > visit_goal_first + home_goal_second:
							champion = final[1]
						elif home_goal_first + visit_goal_second < visit_goal_first + home_goal_second:
							champion = final[0]
						else:
							rolo = 0
							while rolo < 1:
								home_win, draw, visit_win = detection_result(final[0], final[1], table_teams_updating, n)
								if home_win:
									champion = final[0]
									rolo = rolo + 1
								elif visit_win:
									champion = final[1]
									rolo = rolo + 1
								elif draw:
									draw = False
									pass
									
		#TORNEO DE CLAUSURA 2020-2021
		table_position_second = [["Posicion", "Equipo", "Total", "Ganes", "Empates", "Perdidas", "Puntos", "Favor", "Contra"],  [1, 'Alajuelense', 0, 0, 0, 0, 0, 0, 0], [2, 'Perez Zeledon', 0, 0, 0, 0, 0, 0, 0], 
					[3, 'Grecia', 0, 0, 0, 0, 0, 0, 0], [4, 'Santos', 0, 0, 0, 0, 0, 0, 0], [5, 'Herediano', 0, 0, 0, 0, 0, 0, 0], [6, 'Guadalupe', 0, 0, 0, 0, 0, 0, 0],
					[7, 'Jicaral', 0, 0, 0, 0, 0, 0, 0], [8, 'San Carlos', 0, 0, 0, 0, 0, 0, 0], [9, 'Sporting', 0, 0, 0, 0, 0, 0, 0], [10, 'Saprissa', 0, 0, 0, 0, 0, 0, 0], 
					[11, 'Limon', 0, 0, 0, 0, 0, 0, 0], [12, 'Cartagines', 0, 0, 0, 0, 0, 0, 0]]
		#TORNEO DE APERTURA 
		count_home_win_second = 0
		for day in range(1, len(table_days)):
			for iter in range(1, limit_iter):
				n = count_home_win_second/((day -1) * (limit_iter - 1) + iter)
				home_win, draw, visit_win = detection_result(table_days[day][len(table_days[0]) - 2 * iter + 1], table_days[day][len(table_days[0]) - 2 * iter], table_teams_updating, n) #Itera los partidos
				home_goal, visit_goal = detection_goals(home_win, draw, visit_win,)
				for verify in range (1, 13):
					for verify_b in range(1, len(table_teams_updating )):
						if table_days[day][len(table_days[0]) - 2 * iter + 1] == table_position_second[verify][1] and table_days[day][len(table_days[0]) - 2 * iter + 1] == table_teams_updating[verify_b][1]:   #Cada if me calcula lo necesario cuando gana, empata o piede alguien
							table_position_second[verify][7] += home_goal
							table_position_second[verify][8] += visit_goal
							if home_win:
								table_position_second[verify][2] += 1
								table_position_second[verify][3] += 1
								table_position_second[verify][6] += 3
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][3] += 1
								count_home_win +=1
							elif draw:
								table_position_second[verify][2] += 1
								table_position_second[verify][4] += 1
								table_position_second[verify][6] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][4] += 1
							elif visit_win:
								table_position_second[verify][2] += 1
								table_position_second[verify][5] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][5] += 1
				for verify in range (1, 13):
					for verify_b in range(1, len(table_teams_updating)):
						if table_days[day][len(table_days[0]) - 2 * iter] == table_position_second[verify][1] and table_days[day][len(table_days[0]) - 2 * iter] == table_teams_updating[verify_b][1]:
							table_position_second[verify][8] += home_goal
							table_position_second[verify][7] += visit_goal
							if home_win:
								table_position_second[verify][2] += 1
								table_position_second[verify][5] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][5] += 1
								home_win = False
							if draw:
								table_position_second[verify][2] += 1
								table_position_second[verify][4] += 1
								table_position_second[verify][6] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][4] += 1
								draw = False
							if visit_win:
								table_position_second[verify][2] += 1
								table_position_second[verify][3] += 1
								table_position_second[verify][6] += 3
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][3] += 1
								visit_win = False
		change_factor_a = [0, "", 0, 0, 0, 0, 0] 
		change_factor_b = [0, "", 0, 0, 0, 0, 0]                       #Esta parte me ordena de mayo a menor, criterio puntos
		for serie in range (5):
			for change in range(1, 6):
				if table_position_second[change][6] < table_position_second[change + 1][6]:
					change_factor_a[1:9] = table_position_second[change][1:9]
					table_position_second[change][1:9] = table_position_second[change + 1][1:9]
					table_position_second[change + 1][1:9] = change_factor_a[1:9]
				elif table_position_second[change][6] == table_position_second[change + 1][6]:
					if table_position_second[change][7] - table_position_second[change][8] < table_position_second[change + 1][7] - table_position_second[change + 1][8]:
						change_factor_a[1:9] = table_position_second[change][1:9]
						table_position_second[change][1:9] = table_position_second[change + 1][1:9]
						table_position_second[change + 1][1:9] = change_factor_a[1:9]
					elif table_position_second[change][7] - table_position_second[change][8] == table_position_second[change + 1][7] - table_position_second[change + 1][8]:
						if table_position_second[change][7] < table_position_second[change + 1][7]:
							change_factor_a[1:9] = table_position_second[change][1:9]
							table_position_second[change][1:9] = table_position_second[change + 1][1:9]
							table_position_second[change + 1][1:9] = change_factor_a[1:9]


				if table_position_second[change + 6][6] < table_position_second[change + 7][6]:
					change_factor_b[1:9] = table_position_second[change + 6][1:9]
					table_position_second[change + 6][1:9] = table_position_second[change + 7][1:9]
					table_position_second[change + 7][1:9] = change_factor_b[1:9]
				elif table_position_second[change + 6][6] == table_position_second[change + 7][6]:
					if table_position_second[change + 6][7] - table_position_second[change + 6][8] < table_position_second[change + 7][7] - table_position_second[change + 7][8]:
						change_factor_b[1:9] = table_position_second[change + 6][1:9]
						table_position_second[change + 6][1:9] = table_position_second[change + 7][1:9]
						table_position_second[change + 7][1:9] = change_factor_b[1:9]
					elif table_position_second[change + 6][7] - table_position_second[change + 6][8] == table_position_second[change + 7][7] - table_position_second[change + 7][8]:
						if table_position_second[change + 6][7] < table_position_second[change + 7][7]:
							change_factor_b[1:9] = table_position_second[change + 6][1:9]
							table_position_second[change + 6][1:9] = table_position_second[change + 7][1:9]
							table_position_second[change + 7][1:9] = change_factor_b[1:9]

		if table_position_second[1][6] >= table_position_second[7][6]:
			first_all_second = table_position_second[1][1]
			second_all_second = table_position_second[7][1]
		else:
			first_all_second = table_position_second[7][1]
			second_all_second = table_position_second[1][1]

		if table_position_second[2][6] >= table_position_second[8][6]:
			third_all_second = table_position_second[2][1]
			fourth_all_second = table_position_second[8][1]
		else:
			third_all_second = table_position_second[8][1]
			fourth_all_second = table_position_second[2][1]

		finalist_second = [first_all_second, second_all_second, third_all_second, fourth_all_second]
		#SEMI-FINALS
		final_second = ["", ""]
		for iter in range(1, 3):
			#FIRST LEG
			home_win, draw, visit_win = detection_result(table_position_second[iter][1], table_position_second[9 - iter][1], table_teams_updating, n)
			home_goal_first, visit_goal_first = detection_goals(home_win, draw, visit_win)
			#SECOND LEG
			home_win, draw, visit_win = detection_result(table_position_second[9 - iter][1], table_position_second[iter][1], table_teams_updating, n)
			home_goal_second, visit_goal_second = detection_goals(home_win, draw, visit_win)
			
			if home_goal_first + visit_goal_second > visit_goal_first + home_goal_second:
				final_second[iter - 1] = table_position_second[iter][1]
			elif home_goal_first + visit_goal_second < visit_goal_first + home_goal_second:
				final_second[iter - 1] = table_position_second[9 - iter][1]
			else:
				if  home_goal_first + 2 * visit_goal_second > 2 * visit_goal_first + home_goal_second:
					final_second[iter - 1] = table_position_second[iter][1]
				elif home_goal_first + 2 * visit_goal_second < 2 * visit_goal_first + home_goal_second:
					final_second[iter - 1] = table_position_second[9 - iter][1]
				else:
					verify = 0
					while verify < 1:
						if iter == 1:
							home_win, draw, visit_win = detection_result(table_position_second[iter][1], table_position_second[9 - iter][1], table_teams_updating, n)
							if home_win:
								final_second[0] = table_position_second[iter][1]
								verify = verify + 1
							elif visit_win:
								final_second[0] = table_position_second[9 - iter][1]
								verify = verify + 1
							elif draw:
								draw = False
								pass
						else:
							home_win, draw, visit_win = detection_result(table_position_second[9 - iter][1], table_position_second[iter][1], table_teams_updating, n)
							if home_win:
								final_second[1] = table_position_second[9 - iter][1]
								verify = verify + 1
							elif visit_win:
								final_second[1] = table_position_second[iter][1]
								verify = verify + 1
							elif draw:
								draw = False
								pass	

		#FINAL
		for iter in range(len(finalist_second)):
			for verify in range (len(finalist_second)):
				if final_second[0] == finalist_second[iter] and final_second[1] == finalist_second[verify]:
					if iter > verify:
						home_win, draw, visit_win = detection_result(final_second[0], final_second[1], table_teams_updating, n)
						home_goal_first, visit_goal_first = detection_goals(home_win, draw, visit_win)
							#SECOND LEG
						home_win, draw, visit_win = detection_result(final_second[1], final_second[0], table_teams_updating, n)
						home_goal_second, visit_goal_second = detection_goals(home_win, draw, visit_win)

						if home_goal_first + visit_goal_second > visit_goal_first + home_goal_second:
							champion_second = final_second[0]
						elif home_goal_first + visit_goal_second < visit_goal_first + home_goal_second:
							champion_second = final_second[1]
						else:
							rolo = 0
							while rolo < 1:
								home_win, draw, visit_win = detection_result(final_second[1], final_second[0], table_teams_updating, n)
								if home_win:
									champion_second = final_second[1]
									rolo = rolo + 1
								elif visit_win:
									champion_second = final_second[0]
									rolo = rolo + 1
								elif draw:
									draw = False
									pass

					if iter < verify:
						home_win, draw, visit_win = detection_result(final_second[1], final_second[0], table_teams_updating, n)
						home_goal_first, visit_goal_first = detection_goals(home_win, draw, visit_win)
							#SECOND LEG
						home_win, draw, visit_win = detection_result(final_second[0], final_second[1], table_teams_updating, n)
						home_goal_second, visit_goal_second = detection_goals(home_win, draw, visit_win)

						if home_goal_first + visit_goal_second > visit_goal_first + home_goal_second:
							champion_second = final_second[1]
						elif home_goal_first + visit_goal_second < visit_goal_first + home_goal_second:
							champion_second = final_second[0]
						else:
							rolo = 0
							while rolo < 1:
								home_win, draw, visit_win = detection_result(final_second[0], final_second[1], table_teams_updating, n)
								if home_win:
									champion_second = final_second[0]
									rolo = rolo + 1
								elif visit_win:
									champion_second = final_second[1]
									rolo = rolo + 1
								elif draw:
									draw = False
									pass	
		
		change_factor_a = [0, "", 0, 0, 0, 0, 0] 
		table_general = [["Posicion", "Equipo", "Total", "Ganes", "Empates", "Perdidas", "Puntos", "Favor", "Contra"],  [1, 'Alajuelense', 0, 0, 0, 0, 0, 0, 0], [2, 'Perez Zeledon', 0, 0, 0, 0, 0, 0, 0], 
					[3, 'Grecia', 0, 0, 0, 0, 0, 0, 0], [4, 'Santos', 0, 0, 0, 0, 0, 0, 0], [5, 'Herediano', 0, 0, 0, 0, 0, 0, 0], [6, 'Guadalupe', 0, 0, 0, 0, 0, 0, 0],
					[7, 'Jicaral', 0, 0, 0, 0, 0, 0, 0], [8, 'San Carlos', 0, 0, 0, 0, 0, 0, 0], [9, 'Sporting', 0, 0, 0, 0, 0, 0, 0], [10, 'Saprissa', 0, 0, 0, 0, 0, 0, 0], 
					[11, 'Limon', 0, 0, 0, 0, 0, 0, 0], [12, 'Cartagines', 0, 0, 0, 0, 0, 0, 0]]
		for iter in range(1, len(table_general)):
			for verify_first in range(1, len(table_position)):
				for verify_second in range(1, len(table_position_second)):
					for column in range(2, len(table_general[0])):
						if table_general[iter][1] == table_position[verify_first][1] and table_general[iter][1] == table_position_second[verify_second][1]:
							table_general[iter][column] = table_position[verify_first][column] + table_position_second[verify_second][column]

		for serie in range (len(table_general)):
			for change in range(1, len(table_general) - 1):
				if table_general[change][6] < table_general[change + 1][6]:
					change_factor_a[1:9] = table_general[change][1:9]
					table_general[change][1:9] = table_general[change + 1][1:9]
					table_general[change + 1][1:9] = change_factor_a[1:9]
				elif table_general[change][6] == table_general[change + 1][6]:
					if table_general[change][7] - table_general[change][8] < table_general[change + 1][7] - table_general[change + 1][8]:
						change_factor_a[1:9] = table_general[change][1:9]
						table_general[change][1:9] = table_general[change + 1][1:9]
						table_general[change + 1][1:9] = change_factor_a[1:9]
					elif table_general[change][7] - table_general[change][8] == table_general[change + 1][7] - table_general[change + 1][8]:
						if table_general[change][7] < table_general[change + 1][7]:
							change_factor_a[1:9] = table_general[change][1:9]
							table_general[change][1:9] = table_general[change + 1][1:9]
							table_general[change + 1][1:9] = change_factor_a[1:9]


		return table_position[1], table_position[2], table_position[7], table_position[8], final, champion, first_all , table_position[3], table_position[9], table_position, table_position_second[1], table_position_second[2], table_position_second[7], table_position_second[8], final_second, champion_second, first_all_second , table_position_second[3], table_position_second[9], table_position_second, table_general

	def league_init(init_day):
		#TORNEO DE APERTURA 2020-2021
		table_position = [["Posicion", "Equipo", "Total", "Ganes", "Empates", "Perdidas", "Puntos", "Favor", "Contra"],  [1, 'Alajuelense', 8, 7, 0, 1, 21, 18, 6], [2, 'Perez Zeledon', 8, 3, 0, 5, 9, 11, 16], 
					[3, 'Grecia', 8, 1, 1, 6, 4, 7, 14], [4, 'Santos', 8, 2, 3, 3, 9, 9, 14], [5, 'Herediano', 8, 4, 1, 3, 13, 13, 10], [6, 'Guadalupe', 8, 4, 1, 3, 13, 14, 12],
					[7, 'Jicaral', 8, 1, 1, 6, 4, 5, 10], [8, 'San Carlos', 8, 3, 2, 3, 11, 7, 9], [9, 'Sporting', 8, 3, 1, 4, 10, 9, 11], [10, 'Saprissa', 8, 5, 1, 2, 16, 12, 9], 
					[11, 'Limon', 8, 2, 3, 3, 9, 7, 14], [12, 'Cartagines', 8, 5, 2, 1, 17, 20, 7]]
		count_home_win = 21
		table_teams_updating = dataframe()
		limit_iter = int((len(table_days[0]) + 1) / 2)
		for day in range(init_day, len(table_days)):
			for iter in range(1, limit_iter):
				n = count_home_win/((day -1) * (limit_iter - 1) + iter)
				home_win, draw, visit_win = detection_result(table_days[day][2 * iter - 1], table_days[day][2 * iter], table_teams_updating, n) #Itera los partidos
				home_goal, visit_goal = detection_goals(home_win, draw, visit_win,)
				for verify in range (1, 13):
					for verify_b in range(1, len(table_teams_updating )):
						if table_days[day][2 * iter - 1] == table_position[verify][1] and table_days[day][2 * iter - 1] == table_teams_updating[verify_b][1]:   #Cada if me calcula lo necesario cuando gana, empata o piede alguien
							table_position[verify][7] += home_goal
							table_position[verify][8] += visit_goal
							if home_win:
								table_position[verify][2] += 1
								table_position[verify][3] += 1
								table_position[verify][6] += 3
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][3] += 1
								count_home_win +=1
							elif draw:
								table_position[verify][2] += 1
								table_position[verify][4] += 1
								table_position[verify][6] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][4] += 1
							elif visit_win:
								table_position[verify][2] += 1
								table_position[verify][5] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][5] += 1
				for verify in range (1, 13):
					for verify_b in range(1, len(table_teams_updating)):
						if table_days[day][2 * iter] == table_position[verify][1] and table_days[day][2 * iter] == table_teams_updating[verify_b][1]:
							table_position[verify][8] += home_goal
							table_position[verify][7] += visit_goal
							if home_win:
								table_position[verify][2] += 1
								table_position[verify][5] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][5] += 1
								home_win = False
							if draw:
								table_position[verify][2] += 1
								table_position[verify][4] += 1
								table_position[verify][6] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][4] += 1
								draw = False
							if visit_win:
								table_position[verify][2] += 1
								table_position[verify][3] += 1
								table_position[verify][6] += 3
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][3] += 1
								visit_win = False
		change_factor_a = [0, "", 0, 0, 0, 0, 0] 
		change_factor_b = [0, "", 0, 0, 0, 0, 0]                       #Esta parte me ordena de mayo a menor, criterio puntos
		for serie in range (5):
			for change in range(1, 6):
				if table_position[change][6] < table_position[change + 1][6]:
					change_factor_a[1:9] = table_position[change][1:9]
					table_position[change][1:9] = table_position[change + 1][1:9]
					table_position[change + 1][1:9] = change_factor_a[1:9]
				elif table_position[change][6] == table_position[change + 1][6]:
					if table_position[change][7] - table_position[change][8] < table_position[change + 1][7] - table_position[change + 1][8]:
						change_factor_a[1:9] = table_position[change][1:9]
						table_position[change][1:9] = table_position[change + 1][1:9]
						table_position[change + 1][1:9] = change_factor_a[1:9]
					elif table_position[change][7] - table_position[change][8] == table_position[change + 1][7] - table_position[change + 1][8]:
						if table_position[change][7] < table_position[change + 1][7]:
							change_factor_a[1:9] = table_position[change][1:9]
							table_position[change][1:9] = table_position[change + 1][1:9]
							table_position[change + 1][1:9] = change_factor_a[1:9]


				if table_position[change + 6][6] < table_position[change + 7][6]:
					change_factor_b[1:9] = table_position[change + 6][1:9]
					table_position[change + 6][1:9] = table_position[change + 7][1:9]
					table_position[change + 7][1:9] = change_factor_b[1:9]
				elif table_position[change + 6][6] == table_position[change + 7][6]:
					if table_position[change + 6][7] - table_position[change + 6][8] < table_position[change + 7][7] - table_position[change + 7][8]:
						change_factor_b[1:9] = table_position[change + 6][1:9]
						table_position[change + 6][1:9] = table_position[change + 7][1:9]
						table_position[change + 7][1:9] = change_factor_b[1:9]
					elif table_position[change + 6][7] - table_position[change + 6][8] == table_position[change + 7][7] - table_position[change + 7][8]:
						if table_position[change + 6][7] < table_position[change + 7][7]:
							change_factor_b[1:9] = table_position[change + 6][1:9]
							table_position[change + 6][1:9] = table_position[change + 7][1:9]
							table_position[change + 7][1:9] = change_factor_b[1:9]

		if table_position[1][6] >= table_position[7][6]:
			first_all = table_position[1][1]
			second_all = table_position[7][1]
		else:
			first_all = table_position[7][1]
			second_all = table_position[1][1]

		if table_position[2][6] >= table_position[8][6]:
			third_all = table_position[2][1]
			fourth_all = table_position[8][1]
		else:
			third_all = table_position[8][1]
			fourth_all = table_position[2][1]

		finalist = [first_all, second_all, third_all, fourth_all]
		#SEMI-FINALS
		final = ["", ""]
		for iter in range(1, 3):
			#FIRST LEG
			home_win, draw, visit_win = detection_result(table_position[iter][1], table_position[9 - iter][1], table_teams_updating, n)
			home_goal_first, visit_goal_first = detection_goals(home_win, draw, visit_win)
			#SECOND LEG
			home_win, draw, visit_win = detection_result(table_position[9 - iter][1], table_position[iter][1], table_teams_updating, n)
			home_goal_second, visit_goal_second = detection_goals(home_win, draw, visit_win)
			
			if home_goal_first + visit_goal_second > visit_goal_first + home_goal_second:
				final[iter - 1] = table_position[iter][1]
			elif home_goal_first + visit_goal_second < visit_goal_first + home_goal_second:
				final[iter - 1] = table_position[9 - iter][1]
			else:
				if  home_goal_first + 2 * visit_goal_second > 2 * visit_goal_first + home_goal_second:
					final[iter - 1] = table_position[iter][1]
				elif home_goal_first + 2 * visit_goal_second < 2 * visit_goal_first + home_goal_second:
					final[iter - 1] = table_position[9 - iter][1]
				else:
					verify = 0
					while verify < 1:
						if iter == 1:
							home_win, draw, visit_win = detection_result(table_position[iter][1], table_position[9 - iter][1], table_teams_updating, n)
							if home_win:
								final[0] = table_position[iter][1]
								verify = verify + 1
							elif visit_win:
								final[0] = table_position[9 - iter][1]
								verify = verify + 1
							elif draw:
								draw = False
								pass
						else:
							home_win, draw, visit_win = detection_result(table_position[9 - iter][1], table_position[iter][1], table_teams_updating, n)
							if home_win:
								final[1] = table_position[9 - iter][1]
								verify = verify + 1
							elif visit_win:
								final[1] = table_position[iter][1]
								verify = verify + 1
							elif draw:
								draw = False
								pass	

		#FINAL
		for iter in range(len(finalist)):
			for verify in range (len(finalist)):
				if final[0] == finalist[iter] and final[1] == finalist[verify]:
					if iter > verify:
						home_win, draw, visit_win = detection_result(final[0], final[1], table_teams_updating, n)
						home_goal_first, visit_goal_first = detection_goals(home_win, draw, visit_win)
							#SECOND LEG
						home_win, draw, visit_win = detection_result(final[1], final[0], table_teams_updating, n)
						home_goal_second, visit_goal_second = detection_goals(home_win, draw, visit_win)

						if home_goal_first + visit_goal_second > visit_goal_first + home_goal_second:
							champion = final[0]
						elif home_goal_first + visit_goal_second < visit_goal_first + home_goal_second:
							champion = final[1]
						else:
							rolo = 0
							while rolo < 1:
								home_win, draw, visit_win = detection_result(final[1], final[0], table_teams_updating, n)
								if home_win:
									champion = final[1]
									rolo = rolo + 1
								elif visit_win:
									champion = final[0]
									rolo = rolo + 1
								elif draw:
									draw = False
									pass

					if iter < verify:
						home_win, draw, visit_win = detection_result(final[1], final[0], table_teams_updating, n)
						home_goal_first, visit_goal_first = detection_goals(home_win, draw, visit_win)
							#SECOND LEG
						home_win, draw, visit_win = detection_result(final[0], final[1], table_teams_updating, n)
						home_goal_second, visit_goal_second = detection_goals(home_win, draw, visit_win)

						if home_goal_first + visit_goal_second > visit_goal_first + home_goal_second:
							champion = final[1]
						elif home_goal_first + visit_goal_second < visit_goal_first + home_goal_second:
							champion = final[0]
						else:
							rolo = 0
							while rolo < 1:
								home_win, draw, visit_win = detection_result(final[0], final[1], table_teams_updating, n)
								if home_win:
									champion = final[0]
									rolo = rolo + 1
								elif visit_win:
									champion = final[1]
									rolo = rolo + 1
								elif draw:
									draw = False
									pass
									
		#TORNEO DE CLAUSURA 2020-2021
		table_position_second = [["Posicion", "Equipo", "Total", "Ganes", "Empates", "Perdidas", "Puntos", "Favor", "Contra"],  [1, 'Alajuelense', 0, 0, 0, 0, 0, 0, 0], [2, 'Perez Zeledon', 0, 0, 0, 0, 0, 0, 0], 
					[3, 'Grecia', 0, 0, 0, 0, 0, 0, 0], [4, 'Santos', 0, 0, 0, 0, 0, 0, 0], [5, 'Herediano', 0, 0, 0, 0, 0, 0, 0], [6, 'Guadalupe', 0, 0, 0, 0, 0, 0, 0],
					[7, 'Jicaral', 0, 0, 0, 0, 0, 0, 0], [8, 'San Carlos', 0, 0, 0, 0, 0, 0, 0], [9, 'Sporting', 0, 0, 0, 0, 0, 0, 0], [10, 'Saprissa', 0, 0, 0, 0, 0, 0, 0], 
					[11, 'Limon', 0, 0, 0, 0, 0, 0, 0], [12, 'Cartagines', 0, 0, 0, 0, 0, 0, 0]]
		#TORNEO DE APERTURA 
		count_home_win_second = 0
		for day in range(1, len(table_days)):
			for iter in range(1, limit_iter):
				n = count_home_win_second/((day -1) * (limit_iter - 1) + iter)
				home_win, draw, visit_win = detection_result(table_days[day][len(table_days[0]) - 2 * iter + 1], table_days[day][len(table_days[0]) - 2 * iter], table_teams_updating, n) #Itera los partidos
				home_goal, visit_goal = detection_goals(home_win, draw, visit_win,)
				for verify in range (1, 13):
					for verify_b in range(1, len(table_teams_updating )):
						if table_days[day][len(table_days[0]) - 2 * iter + 1] == table_position_second[verify][1] and table_days[day][len(table_days[0]) - 2 * iter + 1] == table_teams_updating[verify_b][1]:   #Cada if me calcula lo necesario cuando gana, empata o piede alguien
							table_position_second[verify][7] += home_goal
							table_position_second[verify][8] += visit_goal
							if home_win:
								table_position_second[verify][2] += 1
								table_position_second[verify][3] += 1
								table_position_second[verify][6] += 3
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][3] += 1
								count_home_win +=1
							elif draw:
								table_position_second[verify][2] += 1
								table_position_second[verify][4] += 1
								table_position_second[verify][6] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][4] += 1
							elif visit_win:
								table_position_second[verify][2] += 1
								table_position_second[verify][5] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][5] += 1
				for verify in range (1, 13):
					for verify_b in range(1, len(table_teams_updating)):
						if table_days[day][len(table_days[0]) - 2 * iter] == table_position_second[verify][1] and table_days[day][len(table_days[0]) - 2 * iter] == table_teams_updating[verify_b][1]:
							table_position_second[verify][8] += home_goal
							table_position_second[verify][7] += visit_goal
							if home_win:
								table_position_second[verify][2] += 1
								table_position_second[verify][5] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][5] += 1
								home_win = False
							if draw:
								table_position_second[verify][2] += 1
								table_position_second[verify][4] += 1
								table_position_second[verify][6] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][4] += 1
								draw = False
							if visit_win:
								table_position_second[verify][2] += 1
								table_position_second[verify][3] += 1
								table_position_second[verify][6] += 3
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][3] += 1
								visit_win = False
		change_factor_a = [0, "", 0, 0, 0, 0, 0] 
		change_factor_b = [0, "", 0, 0, 0, 0, 0]                       #Esta parte me ordena de mayo a menor, criterio puntos
		for serie in range (5):
			for change in range(1, 6):
				if table_position_second[change][6] < table_position_second[change + 1][6]:
					change_factor_a[1:9] = table_position_second[change][1:9]
					table_position_second[change][1:9] = table_position_second[change + 1][1:9]
					table_position_second[change + 1][1:9] = change_factor_a[1:9]
				elif table_position_second[change][6] == table_position_second[change + 1][6]:
					if table_position_second[change][7] - table_position_second[change][8] < table_position_second[change + 1][7] - table_position_second[change + 1][8]:
						change_factor_a[1:9] = table_position_second[change][1:9]
						table_position_second[change][1:9] = table_position_second[change + 1][1:9]
						table_position_second[change + 1][1:9] = change_factor_a[1:9]
					elif table_position_second[change][7] - table_position_second[change][8] == table_position_second[change + 1][7] - table_position_second[change + 1][8]:
						if table_position_second[change][7] < table_position_second[change + 1][7]:
							change_factor_a[1:9] = table_position_second[change][1:9]
							table_position_second[change][1:9] = table_position_second[change + 1][1:9]
							table_position_second[change + 1][1:9] = change_factor_a[1:9]


				if table_position_second[change + 6][6] < table_position_second[change + 7][6]:
					change_factor_b[1:9] = table_position_second[change + 6][1:9]
					table_position_second[change + 6][1:9] = table_position_second[change + 7][1:9]
					table_position_second[change + 7][1:9] = change_factor_b[1:9]
				elif table_position_second[change + 6][6] == table_position_second[change + 7][6]:
					if table_position_second[change + 6][7] - table_position_second[change + 6][8] < table_position_second[change + 7][7] - table_position_second[change + 7][8]:
						change_factor_b[1:9] = table_position_second[change + 6][1:9]
						table_position_second[change + 6][1:9] = table_position_second[change + 7][1:9]
						table_position_second[change + 7][1:9] = change_factor_b[1:9]
					elif table_position_second[change + 6][7] - table_position_second[change + 6][8] == table_position_second[change + 7][7] - table_position_second[change + 7][8]:
						if table_position_second[change + 6][7] < table_position_second[change + 7][7]:
							change_factor_b[1:9] = table_position_second[change + 6][1:9]
							table_position_second[change + 6][1:9] = table_position_second[change + 7][1:9]
							table_position_second[change + 7][1:9] = change_factor_b[1:9]

		if table_position_second[1][6] >= table_position_second[7][6]:
			first_all_second = table_position_second[1][1]
			second_all_second = table_position_second[7][1]
		else:
			first_all_second = table_position_second[7][1]
			second_all_second = table_position_second[1][1]

		if table_position_second[2][6] >= table_position_second[8][6]:
			third_all_second = table_position_second[2][1]
			fourth_all_second = table_position_second[8][1]
		else:
			third_all_second = table_position_second[8][1]
			fourth_all_second = table_position_second[2][1]

		finalist_second = [first_all_second, second_all_second, third_all_second, fourth_all_second]
		#SEMI-FINALS
		final_second = ["", ""]
		for iter in range(1, 3):
			#FIRST LEG
			home_win, draw, visit_win = detection_result(table_position_second[iter][1], table_position_second[9 - iter][1], table_teams_updating, n)
			home_goal_first, visit_goal_first = detection_goals(home_win, draw, visit_win)
			#SECOND LEG
			home_win, draw, visit_win = detection_result(table_position_second[9 - iter][1], table_position_second[iter][1], table_teams_updating, n)
			home_goal_second, visit_goal_second = detection_goals(home_win, draw, visit_win)
			
			if home_goal_first + visit_goal_second > visit_goal_first + home_goal_second:
				final_second[iter - 1] = table_position_second[iter][1]
			elif home_goal_first + visit_goal_second < visit_goal_first + home_goal_second:
				final_second[iter - 1] = table_position_second[9 - iter][1]
			else:
				if  home_goal_first + 2 * visit_goal_second > 2 * visit_goal_first + home_goal_second:
					final_second[iter - 1] = table_position_second[iter][1]
				elif home_goal_first + 2 * visit_goal_second < 2 * visit_goal_first + home_goal_second:
					final_second[iter - 1] = table_position_second[9 - iter][1]
				else:
					verify = 0
					while verify < 1:
						if iter == 1:
							home_win, draw, visit_win = detection_result(table_position_second[iter][1], table_position_second[9 - iter][1], table_teams_updating, n)
							if home_win:
								final_second[0] = table_position_second[iter][1]
								verify = verify + 1
							elif visit_win:
								final_second[0] = table_position_second[9 - iter][1]
								verify = verify + 1
							elif draw:
								draw = False
								pass
						else:
							home_win, draw, visit_win = detection_result(table_position_second[9 - iter][1], table_position_second[iter][1], table_teams_updating, n)
							if home_win:
								final_second[1] = table_position_second[9 - iter][1]
								verify = verify + 1
							elif visit_win:
								final_second[1] = table_position_second[iter][1]
								verify = verify + 1
							elif draw:
								draw = False
								pass	

		#FINAL
		for iter in range(len(finalist_second)):
			for verify in range (len(finalist_second)):
				if final_second[0] == finalist_second[iter] and final_second[1] == finalist_second[verify]:
					if iter > verify:
						home_win, draw, visit_win = detection_result(final_second[0], final_second[1], table_teams_updating, n)
						home_goal_first, visit_goal_first = detection_goals(home_win, draw, visit_win)
							#SECOND LEG
						home_win, draw, visit_win = detection_result(final_second[1], final_second[0], table_teams_updating, n)
						home_goal_second, visit_goal_second = detection_goals(home_win, draw, visit_win)

						if home_goal_first + visit_goal_second > visit_goal_first + home_goal_second:
							champion_second = final_second[0]
						elif home_goal_first + visit_goal_second < visit_goal_first + home_goal_second:
							champion_second = final_second[1]
						else:
							rolo = 0
							while rolo < 1:
								home_win, draw, visit_win = detection_result(final_second[1], final_second[0], table_teams_updating, n)
								if home_win:
									champion_second = final_second[1]
									rolo = rolo + 1
								elif visit_win:
									champion_second = final_second[0]
									rolo = rolo + 1
								elif draw:
									draw = False
									pass

					if iter < verify:
						home_win, draw, visit_win = detection_result(final_second[1], final_second[0], table_teams_updating, n)
						home_goal_first, visit_goal_first = detection_goals(home_win, draw, visit_win)
							#SECOND LEG
						home_win, draw, visit_win = detection_result(final_second[0], final_second[1], table_teams_updating, n)
						home_goal_second, visit_goal_second = detection_goals(home_win, draw, visit_win)

						if home_goal_first + visit_goal_second > visit_goal_first + home_goal_second:
							champion_second = final_second[1]
						elif home_goal_first + visit_goal_second < visit_goal_first + home_goal_second:
							champion_second = final_second[0]
						else:
							rolo = 0
							while rolo < 1:
								home_win, draw, visit_win = detection_result(final_second[0], final_second[1], table_teams_updating, n)
								if home_win:
									champion_second = final_second[0]
									rolo = rolo + 1
								elif visit_win:
									champion_second = final_second[1]
									rolo = rolo + 1
								elif draw:
									draw = False
									pass	
		
		change_factor_a = [0, "", 0, 0, 0, 0, 0] 
		table_general = [["Posicion", "Equipo", "Total", "Ganes", "Empates", "Perdidas", "Puntos", "Favor", "Contra"],  [1, 'Alajuelense', 0, 0, 0, 0, 0, 0, 0], [2, 'Perez Zeledon', 0, 0, 0, 0, 0, 0, 0], 
					[3, 'Grecia', 0, 0, 0, 0, 0, 0, 0], [4, 'Santos', 0, 0, 0, 0, 0, 0, 0], [5, 'Herediano', 0, 0, 0, 0, 0, 0, 0], [6, 'Guadalupe', 0, 0, 0, 0, 0, 0, 0],
					[7, 'Jicaral', 0, 0, 0, 0, 0, 0, 0], [8, 'San Carlos', 0, 0, 0, 0, 0, 0, 0], [9, 'Sporting', 0, 0, 0, 0, 0, 0, 0], [10, 'Saprissa', 0, 0, 0, 0, 0, 0, 0], 
					[11, 'Limon', 0, 0, 0, 0, 0, 0, 0], [12, 'Cartagines', 0, 0, 0, 0, 0, 0, 0]]
		for iter in range(1, len(table_general)):
			for verify_first in range(1, len(table_position)):
				for verify_second in range(1, len(table_position_second)):
					for column in range(2, len(table_general[0])):
						if table_general[iter][1] == table_position[verify_first][1] and table_general[iter][1] == table_position_second[verify_second][1]:
							table_general[iter][column] = table_position[verify_first][column] + table_position_second[verify_second][column]

		for serie in range (len(table_general)):
			for change in range(1, len(table_general) - 1):
				if table_general[change][6] < table_general[change + 1][6]:
					change_factor_a[1:9] = table_general[change][1:9]
					table_general[change][1:9] = table_general[change + 1][1:9]
					table_general[change + 1][1:9] = change_factor_a[1:9]
				elif table_general[change][6] == table_general[change + 1][6]:
					if table_general[change][7] - table_general[change][8] < table_general[change + 1][7] - table_general[change + 1][8]:
						change_factor_a[1:9] = table_general[change][1:9]
						table_general[change][1:9] = table_general[change + 1][1:9]
						table_general[change + 1][1:9] = change_factor_a[1:9]
					elif table_general[change][7] - table_general[change][8] == table_general[change + 1][7] - table_general[change + 1][8]:
						if table_general[change][7] < table_general[change + 1][7]:
							change_factor_a[1:9] = table_general[change][1:9]
							table_general[change][1:9] = table_general[change + 1][1:9]
							table_general[change + 1][1:9] = change_factor_a[1:9]


		return table_position[1], table_position[2], table_position[7], table_position[8], final, champion, first_all , table_position[3], table_position[9], table_position, table_position_second[1], table_position_second[2], table_position_second[7], table_position_second[8], final_second, champion_second, first_all_second , table_position_second[3], table_position_second[9], table_position_second, table_general

	def league_init_twelve(init_day):
		#TORNEO DE APERTURA 2020-2021
		table_position = [["Posicion", "Equipo", "Total", "Ganes", "Empates", "Perdidas", "Puntos", "Favor", "Contra"],  [1, 'Alajuelense', 16, 12, 1, 3, 37, 36, 18], [2, 'Perez Zeledon', 16, 4, 3, 9, 15, 20, 34], #Santos y saprissa 
					[3, 'Grecia', 16, 2, 4, 10, 10, 14, 26], [4, 'Santos', 16, 2, 8, 6, 14, 12, 24], [5, 'Herediano', 16, 7, 5, 4, 26, 27, 19], [6, 'Guadalupe', 16, 6, 3, 7, 21, 25, 27],
					[7, 'Jicaral', 16, 4, 6, 6, 18, 14, 15], [8, 'San Carlos', 16, 5, 6, 5, 20, 12, 15], [9, 'Sporting', 16, 5, 3, 8, 18, 20, 24], [10, 'Saprissa', 16, 9, 3, 4, 30, 29, 16], 
					[11, 'Limon', 16, 6, 6, 4, 23, 15, 22], [12, 'Cartagines', 16, 9, 2, 5, 29, 32, 16]]
		count_home_win = 42
		table_teams_updating = dataframe()
		limit_iter = int((len(table_days[0]) + 1) / 2)
		for day in range(init_day, len(table_days)):
			for iter in range(1, limit_iter):
				n = count_home_win/((day -1) * (limit_iter - 1) + iter)
				home_win, draw, visit_win = detection_result(table_days[day][2 * iter - 1], table_days[day][2 * iter], table_teams_updating, n) #Itera los partidos
				home_goal, visit_goal = detection_goals(home_win, draw, visit_win,)
				for verify in range (1, 13):
					for verify_b in range(1, len(table_teams_updating )):
						if table_days[day][2 * iter - 1] == table_position[verify][1] and table_days[day][2 * iter - 1] == table_teams_updating[verify_b][1]:   #Cada if me calcula lo necesario cuando gana, empata o piede alguien
							table_position[verify][7] += home_goal
							table_position[verify][8] += visit_goal
							if home_win:
								table_position[verify][2] += 1
								table_position[verify][3] += 1
								table_position[verify][6] += 3
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][3] += 1
								count_home_win +=1
							elif draw:
								table_position[verify][2] += 1
								table_position[verify][4] += 1
								table_position[verify][6] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][4] += 1
							elif visit_win:
								table_position[verify][2] += 1
								table_position[verify][5] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][5] += 1
				for verify in range (1, 13):
					for verify_b in range(1, len(table_teams_updating)):
						if table_days[day][2 * iter] == table_position[verify][1] and table_days[day][2 * iter] == table_teams_updating[verify_b][1]:
							table_position[verify][8] += home_goal
							table_position[verify][7] += visit_goal
							if home_win:
								table_position[verify][2] += 1
								table_position[verify][5] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][5] += 1
								home_win = False
							if draw:
								table_position[verify][2] += 1
								table_position[verify][4] += 1
								table_position[verify][6] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][4] += 1
								draw = False
							if visit_win:
								table_position[verify][2] += 1
								table_position[verify][3] += 1
								table_position[verify][6] += 3
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][3] += 1
								visit_win = False
		change_factor_a = [0, "", 0, 0, 0, 0, 0] 
		change_factor_b = [0, "", 0, 0, 0, 0, 0]                       #Esta parte me ordena de mayo a menor, criterio puntos
		for serie in range (5):
			for change in range(1, 6):
				if table_position[change][6] < table_position[change + 1][6]:
					change_factor_a[1:9] = table_position[change][1:9]
					table_position[change][1:9] = table_position[change + 1][1:9]
					table_position[change + 1][1:9] = change_factor_a[1:9]
				elif table_position[change][6] == table_position[change + 1][6]:
					if table_position[change][7] - table_position[change][8] < table_position[change + 1][7] - table_position[change + 1][8]:
						change_factor_a[1:9] = table_position[change][1:9]
						table_position[change][1:9] = table_position[change + 1][1:9]
						table_position[change + 1][1:9] = change_factor_a[1:9]
					elif table_position[change][7] - table_position[change][8] == table_position[change + 1][7] - table_position[change + 1][8]:
						if table_position[change][7] < table_position[change + 1][7]:
							change_factor_a[1:9] = table_position[change][1:9]
							table_position[change][1:9] = table_position[change + 1][1:9]
							table_position[change + 1][1:9] = change_factor_a[1:9]


				if table_position[change + 6][6] < table_position[change + 7][6]:
					change_factor_b[1:9] = table_position[change + 6][1:9]
					table_position[change + 6][1:9] = table_position[change + 7][1:9]
					table_position[change + 7][1:9] = change_factor_b[1:9]
				elif table_position[change + 6][6] == table_position[change + 7][6]:
					if table_position[change + 6][7] - table_position[change + 6][8] < table_position[change + 7][7] - table_position[change + 7][8]:
						change_factor_b[1:9] = table_position[change + 6][1:9]
						table_position[change + 6][1:9] = table_position[change + 7][1:9]
						table_position[change + 7][1:9] = change_factor_b[1:9]
					elif table_position[change + 6][7] - table_position[change + 6][8] == table_position[change + 7][7] - table_position[change + 7][8]:
						if table_position[change + 6][7] < table_position[change + 7][7]:
							change_factor_b[1:9] = table_position[change + 6][1:9]
							table_position[change + 6][1:9] = table_position[change + 7][1:9]
							table_position[change + 7][1:9] = change_factor_b[1:9]

		if table_position[1][6] >= table_position[7][6]:
			first_all = table_position[1][1]
			second_all = table_position[7][1]
		else:
			first_all = table_position[7][1]
			second_all = table_position[1][1]

		if table_position[2][6] >= table_position[8][6]:
			third_all = table_position[2][1]
			fourth_all = table_position[8][1]
		else:
			third_all = table_position[8][1]
			fourth_all = table_position[2][1]

		finalist = [first_all, second_all, third_all, fourth_all]
		finalist = ['Alajuelense', 'Saprissa', 'Herediano', 'Cartagines']
		#SEMI-FINALS
		final = ["", ""]
		for iter in range(1, 3):
			#FIRST LEG
			home_win, draw, visit_win = detection_result(table_position[iter][1], table_position[9 - iter][1], table_teams_updating, n)
			home_goal_first, visit_goal_first = detection_goals(home_win, draw, visit_win)
			#SECOND LEG
			home_win, draw, visit_win = detection_result(table_position[9 - iter][1], table_position[iter][1], table_teams_updating, n)
			home_goal_second, visit_goal_second = detection_goals(home_win, draw, visit_win)
			
			if home_goal_first + visit_goal_second > visit_goal_first + home_goal_second:
				final[iter - 1] = table_position[iter][1]
			elif home_goal_first + visit_goal_second < visit_goal_first + home_goal_second:
				final[iter - 1] = table_position[9 - iter][1]
			else:
				if  home_goal_first + 2 * visit_goal_second > 2 * visit_goal_first + home_goal_second:
					final[iter - 1] = table_position[iter][1]
				elif home_goal_first + 2 * visit_goal_second < 2 * visit_goal_first + home_goal_second:
					final[iter - 1] = table_position[9 - iter][1]
				else:
					verify = 0
					while verify < 1:
						if iter == 1:
							home_win, draw, visit_win = detection_result(table_position[iter][1], table_position[9 - iter][1], table_teams_updating, n)
							if home_win:
								final[0] = table_position[iter][1]
								verify = verify + 1
							elif visit_win:
								final[0] = table_position[9 - iter][1]
								verify = verify + 1
							elif draw:
								draw = False
								pass
						else:
							home_win, draw, visit_win = detection_result(table_position[9 - iter][1], table_position[iter][1], table_teams_updating, n)
							if home_win:
								final[1] = table_position[9 - iter][1]
								verify = verify + 1
							elif visit_win:
								final[1] = table_position[iter][1]
								verify = verify + 1
							elif draw:
								draw = False
								pass	
		final = ['Alajuelense', 'Herediano']
		#FINAL
		for iter in range(len(finalist)):
			for verify in range (len(finalist)):
				if final[0] == finalist[iter] and final[1] == finalist[verify]:
					if iter > verify:
						home_win, draw, visit_win = detection_result(final[0], final[1], table_teams_updating, n)
						home_goal_first, visit_goal_first = detection_goals(home_win, draw, visit_win)
							#SECOND LEG
						home_win, draw, visit_win = detection_result(final[1], final[0], table_teams_updating, n)
						home_goal_second, visit_goal_second = detection_goals(home_win, draw, visit_win)

						if home_goal_first + visit_goal_second > visit_goal_first + home_goal_second:
							champion = final[0]
						elif home_goal_first + visit_goal_second < visit_goal_first + home_goal_second:
							champion = final[1]
						else:
							rolo = 0
							while rolo < 1:
								home_win, draw, visit_win = detection_result(final[1], final[0], table_teams_updating, n)
								if home_win:
									champion = final[1]
									rolo = rolo + 1
								elif visit_win:
									champion = final[0]
									rolo = rolo + 1
								elif draw:
									draw = False
									pass

					if iter < verify:
						home_win, draw, visit_win = detection_result(final[1], final[0], table_teams_updating, n)
						home_goal_first, visit_goal_first = detection_goals(home_win, draw, visit_win)
							#SECOND LEG
						home_win, draw, visit_win = detection_result(final[0], final[1], table_teams_updating, n)
						home_goal_second, visit_goal_second = detection_goals(home_win, draw, visit_win)

						if home_goal_first + visit_goal_second > visit_goal_first + home_goal_second:
							champion = final[1]
						elif home_goal_first + visit_goal_second < visit_goal_first + home_goal_second:
							champion = final[0]
						else:
							rolo = 0
							while rolo < 1:
								home_win, draw, visit_win = detection_result(final[0], final[1], table_teams_updating, n)
								if home_win:
									champion = final[0]
									rolo = rolo + 1
								elif visit_win:
									champion = final[1]
									rolo = rolo + 1
								elif draw:
									draw = False
									pass
									
		#TORNEO DE CLAUSURA 2020-2021
		table_position_second = [["Posicion", "Equipo", "Total", "Ganes", "Empates", "Perdidas", "Puntos", "Favor", "Contra"],  [1, 'Alajuelense', 0, 0, 0, 0, 0, 0, 0], [2, 'Perez Zeledon', 0, 0, 0, 0, 0, 0, 0], 
					[3, 'Grecia', 0, 0, 0, 0, 0, 0, 0], [4, 'Santos', 0, 0, 0, 0, 0, 0, 0], [5, 'Herediano', 0, 0, 0, 0, 0, 0, 0], [6, 'Guadalupe', 0, 0, 0, 0, 0, 0, 0],
					[7, 'Jicaral', 0, 0, 0, 0, 0, 0, 0], [8, 'San Carlos', 0, 0, 0, 0, 0, 0, 0], [9, 'Sporting', 0, 0, 0, 0, 0, 0, 0], [10, 'Saprissa', 0, 0, 0, 0, 0, 0, 0], 
					[11, 'Limon', 0, 0, 0, 0, 0, 0, 0], [12, 'Cartagines', 0, 0, 0, 0, 0, 0, 0]]
		#TORNEO DE APERTURA 
		count_home_win_second = 0
		for day in range(1, len(table_days)):
			for iter in range(1, limit_iter):
				n = count_home_win_second/((day -1) * (limit_iter - 1) + iter)
				home_win, draw, visit_win = detection_result(table_days[day][len(table_days[0]) - 2 * iter + 1], table_days[day][len(table_days[0]) - 2 * iter], table_teams_updating, n) #Itera los partidos
				home_goal, visit_goal = detection_goals(home_win, draw, visit_win,)
				for verify in range (1, 13):
					for verify_b in range(1, len(table_teams_updating )):
						if table_days[day][len(table_days[0]) - 2 * iter + 1] == table_position_second[verify][1] and table_days[day][len(table_days[0]) - 2 * iter + 1] == table_teams_updating[verify_b][1]:   #Cada if me calcula lo necesario cuando gana, empata o piede alguien
							table_position_second[verify][7] += home_goal
							table_position_second[verify][8] += visit_goal
							if home_win:
								table_position_second[verify][2] += 1
								table_position_second[verify][3] += 1
								table_position_second[verify][6] += 3
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][3] += 1
								count_home_win +=1
							elif draw:
								table_position_second[verify][2] += 1
								table_position_second[verify][4] += 1
								table_position_second[verify][6] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][4] += 1
							elif visit_win:
								table_position_second[verify][2] += 1
								table_position_second[verify][5] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][5] += 1
				for verify in range (1, 13):
					for verify_b in range(1, len(table_teams_updating)):
						if table_days[day][len(table_days[0]) - 2 * iter] == table_position_second[verify][1] and table_days[day][len(table_days[0]) - 2 * iter] == table_teams_updating[verify_b][1]:
							table_position_second[verify][8] += home_goal
							table_position_second[verify][7] += visit_goal
							if home_win:
								table_position_second[verify][2] += 1
								table_position_second[verify][5] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][5] += 1
								home_win = False
							if draw:
								table_position_second[verify][2] += 1
								table_position_second[verify][4] += 1
								table_position_second[verify][6] += 1
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][4] += 1
								draw = False
							if visit_win:
								table_position_second[verify][2] += 1
								table_position_second[verify][3] += 1
								table_position_second[verify][6] += 3
								table_teams_updating[verify_b][2] += 1
								table_teams_updating[verify_b][3] += 1
								visit_win = False
		change_factor_a = [0, "", 0, 0, 0, 0, 0] 
		change_factor_b = [0, "", 0, 0, 0, 0, 0]                       #Esta parte me ordena de mayo a menor, criterio puntos
		for serie in range (5):
			for change in range(1, 6):
				if table_position_second[change][6] < table_position_second[change + 1][6]:
					change_factor_a[1:9] = table_position_second[change][1:9]
					table_position_second[change][1:9] = table_position_second[change + 1][1:9]
					table_position_second[change + 1][1:9] = change_factor_a[1:9]
				elif table_position_second[change][6] == table_position_second[change + 1][6]:
					if table_position_second[change][7] - table_position_second[change][8] < table_position_second[change + 1][7] - table_position_second[change + 1][8]:
						change_factor_a[1:9] = table_position_second[change][1:9]
						table_position_second[change][1:9] = table_position_second[change + 1][1:9]
						table_position_second[change + 1][1:9] = change_factor_a[1:9]
					elif table_position_second[change][7] - table_position_second[change][8] == table_position_second[change + 1][7] - table_position_second[change + 1][8]:
						if table_position_second[change][7] < table_position_second[change + 1][7]:
							change_factor_a[1:9] = table_position_second[change][1:9]
							table_position_second[change][1:9] = table_position_second[change + 1][1:9]
							table_position_second[change + 1][1:9] = change_factor_a[1:9]


				if table_position_second[change + 6][6] < table_position_second[change + 7][6]:
					change_factor_b[1:9] = table_position_second[change + 6][1:9]
					table_position_second[change + 6][1:9] = table_position_second[change + 7][1:9]
					table_position_second[change + 7][1:9] = change_factor_b[1:9]
				elif table_position_second[change + 6][6] == table_position_second[change + 7][6]:
					if table_position_second[change + 6][7] - table_position_second[change + 6][8] < table_position_second[change + 7][7] - table_position_second[change + 7][8]:
						change_factor_b[1:9] = table_position_second[change + 6][1:9]
						table_position_second[change + 6][1:9] = table_position_second[change + 7][1:9]
						table_position_second[change + 7][1:9] = change_factor_b[1:9]
					elif table_position_second[change + 6][7] - table_position_second[change + 6][8] == table_position_second[change + 7][7] - table_position_second[change + 7][8]:
						if table_position_second[change + 6][7] < table_position_second[change + 7][7]:
							change_factor_b[1:9] = table_position_second[change + 6][1:9]
							table_position_second[change + 6][1:9] = table_position_second[change + 7][1:9]
							table_position_second[change + 7][1:9] = change_factor_b[1:9]

		if table_position_second[1][6] >= table_position_second[7][6]:
			first_all_second = table_position_second[1][1]
			second_all_second = table_position_second[7][1]
		else:
			first_all_second = table_position_second[7][1]
			second_all_second = table_position_second[1][1]

		if table_position_second[2][6] >= table_position_second[8][6]:
			third_all_second = table_position_second[2][1]
			fourth_all_second = table_position_second[8][1]
		else:
			third_all_second = table_position_second[8][1]
			fourth_all_second = table_position_second[2][1]

		finalist_second = [first_all_second, second_all_second, third_all_second, fourth_all_second]
		#SEMI-FINALS
		final_second = ["", ""]
		for iter in range(1, 3):
			#FIRST LEG
			home_win, draw, visit_win = detection_result(table_position_second[iter][1], table_position_second[9 - iter][1], table_teams_updating, n)
			home_goal_first, visit_goal_first = detection_goals(home_win, draw, visit_win)
			#SECOND LEG
			home_win, draw, visit_win = detection_result(table_position_second[9 - iter][1], table_position_second[iter][1], table_teams_updating, n)
			home_goal_second, visit_goal_second = detection_goals(home_win, draw, visit_win)
			
			if home_goal_first + visit_goal_second > visit_goal_first + home_goal_second:
				final_second[iter - 1] = table_position_second[iter][1]
			elif home_goal_first + visit_goal_second < visit_goal_first + home_goal_second:
				final_second[iter - 1] = table_position_second[9 - iter][1]
			else:
				if  home_goal_first + 2 * visit_goal_second > 2 * visit_goal_first + home_goal_second:
					final_second[iter - 1] = table_position_second[iter][1]
				elif home_goal_first + 2 * visit_goal_second < 2 * visit_goal_first + home_goal_second:
					final_second[iter - 1] = table_position_second[9 - iter][1]
				else:
					verify = 0
					while verify < 1:
						if iter == 1:
							home_win, draw, visit_win = detection_result(table_position_second[iter][1], table_position_second[9 - iter][1], table_teams_updating, n)
							if home_win:
								final_second[0] = table_position_second[iter][1]
								verify = verify + 1
							elif visit_win:
								final_second[0] = table_position_second[9 - iter][1]
								verify = verify + 1
							elif draw:
								draw = False
								pass
						else:
							home_win, draw, visit_win = detection_result(table_position_second[9 - iter][1], table_position_second[iter][1], table_teams_updating, n)
							if home_win:
								final_second[1] = table_position_second[9 - iter][1]
								verify = verify + 1
							elif visit_win:
								final_second[1] = table_position_second[iter][1]
								verify = verify + 1
							elif draw:
								draw = False
								pass	

		#FINAL
		for iter in range(len(finalist_second)):
			for verify in range (len(finalist_second)):
				if final_second[0] == finalist_second[iter] and final_second[1] == finalist_second[verify]:
					if iter > verify:
						home_win, draw, visit_win = detection_result(final_second[0], final_second[1], table_teams_updating, n)
						home_goal_first, visit_goal_first = detection_goals(home_win, draw, visit_win)
							#SECOND LEG
						home_win, draw, visit_win = detection_result(final_second[1], final_second[0], table_teams_updating, n)
						home_goal_second, visit_goal_second = detection_goals(home_win, draw, visit_win)

						if home_goal_first + visit_goal_second > visit_goal_first + home_goal_second:
							champion_second = final_second[0]
						elif home_goal_first + visit_goal_second < visit_goal_first + home_goal_second:
							champion_second = final_second[1]
						else:
							rolo = 0
							while rolo < 1:
								home_win, draw, visit_win = detection_result(final_second[1], final_second[0], table_teams_updating, n)
								if home_win:
									champion_second = final_second[1]
									rolo = rolo + 1
								elif visit_win:
									champion_second = final_second[0]
									rolo = rolo + 1
								elif draw:
									draw = False
									pass

					if iter < verify:
						home_win, draw, visit_win = detection_result(final_second[1], final_second[0], table_teams_updating, n)
						home_goal_first, visit_goal_first = detection_goals(home_win, draw, visit_win)
							#SECOND LEG
						home_win, draw, visit_win = detection_result(final_second[0], final_second[1], table_teams_updating, n)
						home_goal_second, visit_goal_second = detection_goals(home_win, draw, visit_win)

						if home_goal_first + visit_goal_second > visit_goal_first + home_goal_second:
							champion_second = final_second[1]
						elif home_goal_first + visit_goal_second < visit_goal_first + home_goal_second:
							champion_second = final_second[0]
						else:
							rolo = 0
							while rolo < 1:
								home_win, draw, visit_win = detection_result(final_second[0], final_second[1], table_teams_updating, n)
								if home_win:
									champion_second = final_second[0]
									rolo = rolo + 1
								elif visit_win:
									champion_second = final_second[1]
									rolo = rolo + 1
								elif draw:
									draw = False
									pass	
		
		change_factor_a = [0, "", 0, 0, 0, 0, 0] 
		table_general = [["Posicion", "Equipo", "Total", "Ganes", "Empates", "Perdidas", "Puntos", "Favor", "Contra"],  [1, 'Alajuelense', 0, 0, 0, 0, 0, 0, 0], [2, 'Perez Zeledon', 0, 0, 0, 0, 0, 0, 0], 
					[3, 'Grecia', 0, 0, 0, 0, 0, 0, 0], [4, 'Santos', 0, 0, 0, 0, 0, 0, 0], [5, 'Herediano', 0, 0, 0, 0, 0, 0, 0], [6, 'Guadalupe', 0, 0, 0, 0, 0, 0, 0],
					[7, 'Jicaral', 0, 0, 0, 0, 0, 0, 0], [8, 'San Carlos', 0, 0, 0, 0, 0, 0, 0], [9, 'Sporting', 0, 0, 0, 0, 0, 0, 0], [10, 'Saprissa', 0, 0, 0, 0, 0, 0, 0], 
					[11, 'Limon', 0, 0, 0, 0, 0, 0, 0], [12, 'Cartagines', 0, 0, 0, 0, 0, 0, 0]]
		for iter in range(1, len(table_general)):
			for verify_first in range(1, len(table_position)):
				for verify_second in range(1, len(table_position_second)):
					for column in range(2, len(table_general[0])):
						if table_general[iter][1] == table_position[verify_first][1] and table_general[iter][1] == table_position_second[verify_second][1]:
							table_general[iter][column] = table_position[verify_first][column] + table_position_second[verify_second][column]

		for serie in range (len(table_general)):
			for change in range(1, len(table_general) - 1):
				if table_general[change][6] < table_general[change + 1][6]:
					change_factor_a[1:9] = table_general[change][1:9]
					table_general[change][1:9] = table_general[change + 1][1:9]
					table_general[change + 1][1:9] = change_factor_a[1:9]
				elif table_general[change][6] == table_general[change + 1][6]:
					if table_general[change][7] - table_general[change][8] < table_general[change + 1][7] - table_general[change + 1][8]:
						change_factor_a[1:9] = table_general[change][1:9]
						table_general[change][1:9] = table_general[change + 1][1:9]
						table_general[change + 1][1:9] = change_factor_a[1:9]
					elif table_general[change][7] - table_general[change][8] == table_general[change + 1][7] - table_general[change + 1][8]:
						if table_general[change][7] < table_general[change + 1][7]:
							change_factor_a[1:9] = table_general[change][1:9]
							table_general[change][1:9] = table_general[change + 1][1:9]
							table_general[change + 1][1:9] = change_factor_a[1:9]


		return table_position[1], table_position[2], table_position[7], table_position[8], final, champion, first_all , table_position[3], table_position[9], table_position, table_position_second[1], table_position_second[2], table_position_second[7], table_position_second[8], final_second, champion_second, first_all_second , table_position_second[3], table_position_second[9], table_position_second, table_general