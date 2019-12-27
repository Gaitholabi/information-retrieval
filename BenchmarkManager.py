import timeit

from IntersectionAlgorithms import IntersectionAlgorithms


class BenchmarkManager:
    @staticmethod
    def benchmark_intersection_algorithms(list_1: list, list_2: list) -> dict:
        list_1 = sorted(set(list_1))
        list_2 = sorted(set(list_2))
        start = timeit.default_timer()
        IntersectionAlgorithms.linear_intersection(list_1, list_2)
        linear_intersect_time = timeit.default_timer() - start

        start = timeit.default_timer()
        IntersectionAlgorithms.binary_intersection(list_1, list_2)
        binary_intersect_time = timeit.default_timer() - start

        start = timeit.default_timer()
        IntersectionAlgorithms.builtin_intersection(set(list_1), list_2)
        python_builtin_intersect_time = timeit.default_timer() - start

        return {'linear': linear_intersect_time, 'binary': binary_intersect_time, 'builtin': python_builtin_intersect_time}
