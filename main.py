from visualizer import Visualizer
import sorters

vis = Visualizer(title = "Sorterings-test", size=(1200, 400))

# vis.bar_animation(algorithm = bubble_sort, data = generate_linear_data(150), title = "Bubble sort", time_interval = 0)
# vis.await_press(key = "c")
vis.bar_animation(algorithm = sorters.shell_sort, data = sorters.generate_linear_data(600), title = "Shell sort", time_interval = 0)
# vis.bar_animation(algorithm = selection_sort, data = generate_linear_data(1200), title = "Selection sort", time_interval = 0)
# vis.bar_animation(algorithm = insertion_sort, data = generate_linear_data(1200), title = "Insertion sort", time_interval = 0)
# vis.bar_animation(algorithm = sorters.mergeSort, data = sorters.generate_linear_data(600), title = "Merge sort", time_interval = 0)
# vis.await_press(key = "c")
# vis.bar_animation(algorithm = selection_sort, data = generate_linear_data(150), title = "Selection sort", time_interval = 0.05)
# vis.await_press(key = "c")
# vis.bar_animation(algorithm = insertion_sort, data = generate_linear_data(150), title = "Insertion sort", time_interval = 0.05)
# vis.await_press(key = "c")
# vis.bar_animation(algorithm = stalin_sort, data = generate_data_biased(50), title = "Stalin sort", time_interval = 0.1)
vis.halt()

vis.quit()
