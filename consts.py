from typing import Callable, Tuple, List

Data = List[float]
DataHighlight = Tuple[Data, List[int]]
DataSorter = Callable[[Data], DataHighlight]
Size = Tuple[int, int]
