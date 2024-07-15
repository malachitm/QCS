def check_cnf_formula(formula: list[tuple], interpretation: list[bool]) -> bool:
	print(formula)
	print(interpretation)
	def check_clause(disjunct: tuple) -> bool:
		temp = [interpretation[abs(disjunct[i]) - 1] for i in range(3)]
		print(temp)
		print("end of temp")
		clause = [atom if disjunct[i] > 0 else not atom for atom, i in enumerate(temp)]
		print(clause)
		print("end of clause")
		print("any -> " + str(any(clause)))
		return any(clause)

	print(list(map(check_clause, formula)))
	print("end of check")
	return all(list(map(check_clause, formula)))

print(check_cnf_formula([(-1, -2, -3), (1, 2, -3)], [False, True, True]))