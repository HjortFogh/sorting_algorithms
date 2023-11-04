from typing import Callable, Tuple, List

# Liste af værdier som kan sorters
Data = List[float | int]
# En permutation af et datasæt dvs. datasættet efter et sorterings-step, samt en liste af indekser som skal fremhæves (f.eks. hvis to elementer byttes rundt bliver disse fremhævet)
DataPermutation = Tuple[Data, List[int]]
# Generator-funktion som tager et datasæt og giver (yields) en 'DataPermutation' efter hvert sorterings-step
DataSorter = Callable[[Data], DataPermutation]
# Størrelse af et vindue
Size = Tuple[int, int]
