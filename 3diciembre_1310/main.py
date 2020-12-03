from backtracking import laberintoADT

pasillos_inicial= ((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
lab = laberintoADT( 6, 6, pasillos_inicial, (5,2), (2,5))
lab.to_string()
"""
sigue el metodo de resolver() que revisa sialrededor hay donde ir si ya paso por un lado hace ignore
si en pos no hay nada hace backtracking
"""