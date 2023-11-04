from visualizer import Visualizer
import sorters

visualizer = Visualizer(title="Sorterings algoritmer", size=(1200, 400))

# Bubble sort
visualizer.bar_animation(algorithm=sorters.bubble_sort, data=sorters.generate_linear_data(50), time_interval=0.005, title="Bubble sort", expected_big_o="O(n²)")
visualizer.sleep(0.6)
visualizer.box_animation(algorithm=sorters.bubble_sort, data=sorters.generate_linear_ints(5), title="Bubble sort")
visualizer.sleep(0.6)
visualizer.bar_animation(algorithm=sorters.bubble_sort, data=sorters.generate_linear_data(120), time_interval=0, title="Bubble sort", expected_big_o="O(n²)")
visualizer.sleep(0.6)
# Selection sort
visualizer.bar_animation(algorithm=sorters.selection_sort, data=sorters.generate_linear_data(50), time_interval=0.2, title="Selection sort", expected_big_o="O(n²)")
visualizer.sleep(0.6)
visualizer.box_animation(algorithm=sorters.selection_sort, data=sorters.generate_linear_ints(8), title="Selection sort")
visualizer.sleep(0.6)
visualizer.bar_animation(algorithm=sorters.selection_sort, data=sorters.generate_linear_data(600), time_interval=0.008, title="Selection sort", expected_big_o="O(n²)")
visualizer.sleep(0.6)
# Insertion sort
visualizer.bar_animation(algorithm=sorters.insertion_sort, data=sorters.generate_linear_data(50), time_interval=0.3, title="Insertion sort", expected_big_o="O(n²)")
visualizer.sleep(0.6)
visualizer.bar_animation(algorithm=sorters.insertion_sort, data=sorters.generate_linear_data(600), time_interval=0.008, title="Insertion sort", expected_big_o="O(n²)")
visualizer.sleep(0.6)
# Merge sort
visualizer.bar_animation(algorithm=sorters.merge_sort, data=sorters.generate_linear_data(50), time_interval=0.04, title="Merge sort", expected_big_o="O(n log(n))")
visualizer.sleep(0.6)
visualizer.bar_animation(algorithm=sorters.merge_sort, data=sorters.generate_linear_data(600), time_interval=0, title="Merge sort", expected_big_o="O(n log(n))")
visualizer.sleep(0.6)
# Shell sort
visualizer.bar_animation(algorithm=sorters.shell_sort, data=sorters.generate_linear_data(50), time_interval=0.2, title="Shell sort", expected_big_o="O(n log(n)²)")
visualizer.sleep(0.6)
visualizer.box_animation(algorithm=sorters.shell_sort, data=sorters.generate_linear_ints(8), title="Shell sort")
visualizer.sleep(0.6)
visualizer.bar_animation(algorithm=sorters.shell_sort, data=sorters.generate_linear_data(600), time_interval=0, title="Shell sort", expected_big_o="O(n log(n)²)")
visualizer.halt()

visualizer.quit()
