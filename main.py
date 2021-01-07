import montecarlo_method as mm
from multiprocessing import Pool
from tabulate import tabulate
import simulation_cup as sc

if __name__ == '__main__':

	pool = Pool()
	n_runs = 10000
	#print(mm.simulation_league(n_runs))
	"""print("Simulación desde el inicio del torneo")
	[a_1, b_1, c_1, d_1, a_1_second, b_1_second, c_1_second, d_1_second, l_1], [a_2, b_2, c_2, d_2, a_2_second, b_2_second, c_2_second, d_2_second, l_2], [a_3, b_3, c_3, d_3, a_3_second, b_3_second, c_3_second, d_3_second, l_3], [a_4, b_4, c_4, d_4, a_4_second, b_4_second, c_4_second, d_4_second, l_4]= pool.map(mm.simulation_league, (int(n_runs / 4), int(n_runs / 4), int(n_runs / 4), int(n_runs / 4)))
	
	#APERTURA
	table_a = []
	table_b = []
	table_points = []
	table_position = []
	last_team = []
	
	for iter in range(len(c_1)):
		table_points.append([iter + 20])
		for verify in range(1, len(c_1[0])):
			table_points[iter].append(c_1[iter][verify] + c_2[iter][verify] + c_3[iter][verify] + c_4[iter][verify])
	for iter in range(len(table_points)):
		for verify in range(1, len(table_points[0])):
			table_points[iter][verify] = (table_points[iter][verify] / (6 * n_runs)) * 100
	
	for iter in range(len(d_1)):
		table_position.append([d_1[iter][0]])
		for verify in range(1, len(d_1[0])):
			table_position[iter].append(d_1[iter][verify] + d_2[iter][verify] + d_3[iter][verify] + d_4[iter][verify])
	for iter in range(len(table_position)):
		for verify in range(1, len(table_position[0])):
			table_position[iter][verify] = table_position[iter][verify] / n_runs

	for iter in range(len(a_1)):
		table_a.append([a_1[iter][0]])
		table_b.append([b_1[iter][0]])
		for verify in range(1, 5):
			table_a[iter].append(a_1[iter][verify] + a_2[iter][verify] + a_3[iter][verify] + a_4[iter][verify])
			table_b[iter].append(b_1[iter][verify] + b_2[iter][verify] + b_3[iter][verify] + b_4[iter][verify])
	for iter in range(len(table_a)):
		for verify in range(1, 5):
			table_a[iter][verify] = table_a[iter][verify] / n_runs
			table_b[iter][verify] = table_b[iter][verify] / n_runs
	
	print(tabulate(table_a))
	print(tabulate(table_b))
	print(tabulate(table_points))
	print(tabulate(table_position))


	#CLAUSURA
	table_a_second = []
	table_b_second = []
	table_points_second = []
	table_position_second = []
	
	for iter in range(len(c_1_second)):
		table_points_second.append([iter + 20])
		for verify in range(1, len(c_1_second[0])):
			table_points_second[iter].append(c_1_second[iter][verify] + c_2_second[iter][verify] + c_3_second[iter][verify] + c_4_second[iter][verify])
	for iter in range(len(table_points_second)):
		for verify in range(1, len(table_points_second[0])):
			table_points_second[iter][verify] = (table_points_second[iter][verify] / (6 * n_runs)) * 100
	
	for iter in range(len(d_1_second)):
		table_position_second.append([d_1_second[iter][0]])
		for verify in range(1, len(d_1_second[0])):
			table_position_second[iter].append(d_1_second[iter][verify] + d_2_second[iter][verify] + d_3_second[iter][verify] + d_4_second[iter][verify])
	for iter in range(len(table_position_second)):
		for verify in range(1, len(table_position_second[0])):
			table_position_second[iter][verify] = table_position_second[iter][verify] / n_runs

	for iter in range(len(a_1_second)):
		table_a_second.append([a_1_second[iter][0]])
		table_b_second.append([b_1_second[iter][0]])
		for verify in range(1, 5):
			table_a_second[iter].append(a_1_second[iter][verify] + a_2_second[iter][verify] + a_3_second[iter][verify] + a_4_second[iter][verify])
			table_b_second[iter].append(b_1_second[iter][verify] + b_2_second[iter][verify] + b_3_second[iter][verify] + b_4_second[iter][verify])
	for iter in range(len(table_a_second)):
		for verify in range(1, 5):
			table_a_second[iter][verify] = table_a_second[iter][verify] / n_runs
			table_b_second[iter][verify] = table_b_second[iter][verify] / n_runs

	for iter in range(len(l_1)):
		last_team.append([l_1[iter][0]])
		for verify in range(1, len(l_1[0])):
			last_team[iter].append(l_1[iter][verify] + l_2[iter][verify] + l_3[iter][verify] + l_4[iter][verify])
	for iter in range(len(last_team)):
		for verify in range(1, len(last_team[0])):
			last_team[iter][verify] = last_team[iter][verify] / n_runs



	print(tabulate(table_a_second))
	print(tabulate(table_b_second))
	print(tabulate(table_points_second))
	print(tabulate(table_position_second))
	print(tabulate(last_team))

	print("Simulación desde la jornada 9 del torneo")
	[a_1, b_1, c_1, d_1, a_1_second, b_1_second, c_1_second, d_1_second, l_1], [a_2, b_2, c_2, d_2, a_2_second, b_2_second, c_2_second, d_2_second, l_2], [a_3, b_3, c_3, d_3, a_3_second, b_3_second, c_3_second, d_3_second, l_3], [a_4, b_4, c_4, d_4, a_4_second, b_4_second, c_4_second, d_4_second, l_4]= pool.map(mm.simulation_league_init, (int(n_runs / 4), int(n_runs / 4), int(n_runs / 4), int(n_runs / 4)))
	
	#APERTURA
	table_a = []
	table_b = []
	table_points = []
	table_position = []
	last_team = []
	
	for iter in range(len(c_1)):
		table_points.append([iter + 20])
		for verify in range(1, len(c_1[0])):
			table_points[iter].append(c_1[iter][verify] + c_2[iter][verify] + c_3[iter][verify] + c_4[iter][verify])
	for iter in range(len(table_points)):
		for verify in range(1, len(table_points[0])):
			table_points[iter][verify] = (table_points[iter][verify] / (6 * n_runs)) * 100
	
	for iter in range(len(d_1)):
		table_position.append([d_1[iter][0]])
		for verify in range(1, len(d_1[0])):
			table_position[iter].append(d_1[iter][verify] + d_2[iter][verify] + d_3[iter][verify] + d_4[iter][verify])
	for iter in range(len(table_position)):
		for verify in range(1, len(table_position[0])):
			table_position[iter][verify] = table_position[iter][verify] / n_runs

	for iter in range(len(a_1)):
		table_a.append([a_1[iter][0]])
		table_b.append([b_1[iter][0]])
		for verify in range(1, 5):
			table_a[iter].append(a_1[iter][verify] + a_2[iter][verify] + a_3[iter][verify] + a_4[iter][verify])
			table_b[iter].append(b_1[iter][verify] + b_2[iter][verify] + b_3[iter][verify] + b_4[iter][verify])
	for iter in range(len(table_a)):
		for verify in range(1, 5):
			table_a[iter][verify] = table_a[iter][verify] / n_runs
			table_b[iter][verify] = table_b[iter][verify] / n_runs
	
	print(tabulate(table_a))
	print(tabulate(table_b))
	print(tabulate(table_points))
	print(tabulate(table_position))


	#CLAUSURA
	table_a_second = []
	table_b_second = []
	table_points_second = []
	table_position_second = []
	
	for iter in range(len(c_1_second)):
		table_points_second.append([iter + 20])
		for verify in range(1, len(c_1_second[0])):
			table_points_second[iter].append(c_1_second[iter][verify] + c_2_second[iter][verify] + c_3_second[iter][verify] + c_4_second[iter][verify])
	for iter in range(len(table_points_second)):
		for verify in range(1, len(table_points_second[0])):
			table_points_second[iter][verify] = (table_points_second[iter][verify] / (6 * n_runs)) * 100
	
	for iter in range(len(d_1_second)):
		table_position_second.append([d_1_second[iter][0]])
		for verify in range(1, len(d_1_second[0])):
			table_position_second[iter].append(d_1_second[iter][verify] + d_2_second[iter][verify] + d_3_second[iter][verify] + d_4_second[iter][verify])
	for iter in range(len(table_position_second)):
		for verify in range(1, len(table_position_second[0])):
			table_position_second[iter][verify] = table_position_second[iter][verify] / n_runs

	for iter in range(len(a_1_second)):
		table_a_second.append([a_1_second[iter][0]])
		table_b_second.append([b_1_second[iter][0]])
		for verify in range(1, 5):
			table_a_second[iter].append(a_1_second[iter][verify] + a_2_second[iter][verify] + a_3_second[iter][verify] + a_4_second[iter][verify])
			table_b_second[iter].append(b_1_second[iter][verify] + b_2_second[iter][verify] + b_3_second[iter][verify] + b_4_second[iter][verify])
	for iter in range(len(table_a_second)):
		for verify in range(1, 5):
			table_a_second[iter][verify] = table_a_second[iter][verify] / n_runs
			table_b_second[iter][verify] = table_b_second[iter][verify] / n_runs

	for iter in range(len(l_1)):
		last_team.append([l_1[iter][0]])
		for verify in range(1, len(l_1[0])):
			last_team[iter].append(l_1[iter][verify] + l_2[iter][verify] + l_3[iter][verify] + l_4[iter][verify])
	for iter in range(len(last_team)):
		for verify in range(1, len(last_team[0])):
			last_team[iter][verify] = last_team[iter][verify] / n_runs



	print(tabulate(table_a_second))
	print(tabulate(table_b_second))
	print(tabulate(table_points_second))
	print(tabulate(table_position_second))
	print(tabulate(last_team))
"""
	print("Simulación desde la jornada 13 del torneo")
	[a_1, b_1, c_1, d_1, a_1_second, b_1_second, c_1_second, d_1_second, l_1], [a_2, b_2, c_2, d_2, a_2_second, b_2_second, c_2_second, d_2_second, l_2], [a_3, b_3, c_3, d_3, a_3_second, b_3_second, c_3_second, d_3_second, l_3], [a_4, b_4, c_4, d_4, a_4_second, b_4_second, c_4_second, d_4_second, l_4]= pool.map(mm.simulation_league_init_twelve, (int(n_runs / 4), int(n_runs / 4), int(n_runs / 4), int(n_runs / 4)))
	
	#APERTURA
	table_a = []
	table_b = []
	table_points = []
	table_position = []
	last_team = []
	
	for iter in range(len(c_1)):
		table_points.append([iter + 20])
		for verify in range(1, len(c_1[0])):
			table_points[iter].append(c_1[iter][verify] + c_2[iter][verify] + c_3[iter][verify] + c_4[iter][verify])
	for iter in range(len(table_points)):
		for verify in range(1, len(table_points[0])):
			table_points[iter][verify] = (table_points[iter][verify] / (6 * n_runs)) * 100
	
	for iter in range(len(d_1)):
		table_position.append([d_1[iter][0]])
		for verify in range(1, len(d_1[0])):
			table_position[iter].append(d_1[iter][verify] + d_2[iter][verify] + d_3[iter][verify] + d_4[iter][verify])
	for iter in range(len(table_position)):
		for verify in range(1, len(table_position[0])):
			table_position[iter][verify] = table_position[iter][verify] / n_runs

	for iter in range(len(a_1)):
		table_a.append([a_1[iter][0]])
		table_b.append([b_1[iter][0]])
		for verify in range(1, 5):
			table_a[iter].append(a_1[iter][verify] + a_2[iter][verify] + a_3[iter][verify] + a_4[iter][verify])
			table_b[iter].append(b_1[iter][verify] + b_2[iter][verify] + b_3[iter][verify] + b_4[iter][verify])
	for iter in range(len(table_a)):
		for verify in range(1, 5):
			table_a[iter][verify] = table_a[iter][verify] / n_runs
			table_b[iter][verify] = table_b[iter][verify] / n_runs
	
	print(tabulate(table_a))
	print(tabulate(table_b))
	print(tabulate(table_points))
	print(tabulate(table_position))


	#CLAUSURA
	table_a_second = []
	table_b_second = []
	table_points_second = []
	table_position_second = []
	
	for iter in range(len(c_1_second)):
		table_points_second.append([iter + 20])
		for verify in range(1, len(c_1_second[0])):
			table_points_second[iter].append(c_1_second[iter][verify] + c_2_second[iter][verify] + c_3_second[iter][verify] + c_4_second[iter][verify])
	for iter in range(len(table_points_second)):
		for verify in range(1, len(table_points_second[0])):
			table_points_second[iter][verify] = (table_points_second[iter][verify] / (6 * n_runs)) * 100
	
	for iter in range(len(d_1_second)):
		table_position_second.append([d_1_second[iter][0]])
		for verify in range(1, len(d_1_second[0])):
			table_position_second[iter].append(d_1_second[iter][verify] + d_2_second[iter][verify] + d_3_second[iter][verify] + d_4_second[iter][verify])
	for iter in range(len(table_position_second)):
		for verify in range(1, len(table_position_second[0])):
			table_position_second[iter][verify] = table_position_second[iter][verify] / n_runs

	for iter in range(len(a_1_second)):
		table_a_second.append([a_1_second[iter][0]])
		table_b_second.append([b_1_second[iter][0]])
		for verify in range(1, 5):
			table_a_second[iter].append(a_1_second[iter][verify] + a_2_second[iter][verify] + a_3_second[iter][verify] + a_4_second[iter][verify])
			table_b_second[iter].append(b_1_second[iter][verify] + b_2_second[iter][verify] + b_3_second[iter][verify] + b_4_second[iter][verify])
	for iter in range(len(table_a_second)):
		for verify in range(1, 5):
			table_a_second[iter][verify] = table_a_second[iter][verify] / n_runs
			table_b_second[iter][verify] = table_b_second[iter][verify] / n_runs

	for iter in range(len(l_1)):
		last_team.append([l_1[iter][0]])
		for verify in range(1, len(l_1[0])):
			last_team[iter].append(l_1[iter][verify] + l_2[iter][verify] + l_3[iter][verify] + l_4[iter][verify])
	for iter in range(len(last_team)):
		for verify in range(1, len(last_team[0])):
			last_team[iter][verify] = last_team[iter][verify] / n_runs



	print(tabulate(table_a_second))
	print(tabulate(table_b_second))
	print(tabulate(table_points_second))
	print(tabulate(table_position_second))
	print(tabulate(last_team))
	"""

	doce = [["Posicion", "Equipo", "Total", "Ganes", "Empates", "Perdidas", "Puntos", "Favor", "Contra"],  [1, 'Alajuelense', 12, 9, 1, 2, 28, 25, 13], [2, 'Perez Zeledon', 12, 4, 2, 6, 14, 17, 22], #Santos y saprissa 
					[3, 'Grecia', 12, 1, 3, 8, 13, 22, 6], [4, 'Santos', 12, 2, 5, 5, 11, 10, 18], [5, 'Herediano', 12, 5, 4, 3, 19, 20, 15], [6, 'Guadalupe', 12, 5, 2, 5, 17, 18, 18],
					[7, 'Jicaral', 12, 3, 3, 6, 12, 11, 13], [8, 'San Carlos', 12, 4, 5, 3, 17, 10, 10], [9, 'Sporting', 12, 4, 1, 7, 13, 13, 18], [10, 'Saprissa', 12, 6, 2, 4, 20, 15, 13], 
					[11, 'Limon', 12, 5, 4, 3, 19, 11, 15], [12, 'Cartagines', 12, 7, 2, 3, 23, 24, 10]]

	ocho = [["Posicion", "Equipo", "Total", "Ganes", "Empates", "Perdidas", "Puntos", "Favor", "Contra"],  [1, 'Alajuelense', 8, 7, 0, 1, 21, 18, 6], [2, 'Perez Zeledon', 8, 3, 0, 5, 9, 11, 16], 
					[3, 'Grecia', 8, 1, 1, 6, 4, 7, 14], [4, 'Santos', 8, 2, 3, 3, 9, 9, 14], [5, 'Herediano', 8, 4, 1, 3, 13, 13, 10], [6, 'Guadalupe', 8, 4, 1, 3, 13, 14, 12],
					[7, 'Jicaral', 8, 1, 1, 6, 4, 5, 10], [8, 'San Carlos', 8, 3, 2, 3, 11, 7, 9], [9, 'Sporting', 8, 3, 1, 4, 10, 9, 11], [10, 'Saprissa', 8, 5, 1, 2, 16, 12, 9], 
					[11, 'Limon', 8, 2, 3, 3, 9, 7, 14], [12, 'Cartagines', 8, 5, 2, 1, 17, 20, 7]]

	print(tabulate(ocho))
	print(tabulate(doce))"""