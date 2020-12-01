from backtracking import laberintoADT

pasillos_inicial= ((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
lab = laberintoADT(6,6,pasillos_inicial)
lab.to_string()