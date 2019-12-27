class IntersectionAlgorithms:
    @staticmethod
    def linear_intersection(list_1, list_2) -> list:
        def intersect(l1, l2):
            answer = []
            walker_1 = 0
            walker_2 = 0
            while len(l1) > walker_1 and len(l2) > walker_2:
                if l1[walker_1] == l2[walker_2]:
                    answer.append(l1[walker_1])
                    walker_1 += 1
                    walker_2 += 1
                elif l1[walker_1] < l2[walker_2]:
                    walker_1 += 1
                else:
                    walker_2 += 1
            return answer

        return intersect(list_1, list_2) if len(list_1) < len(list_2) else intersect(list_2, list_1)

    @staticmethod
    def binary_intersection(list_1, list_2) -> list:
        def binary_search(needle, haystack) -> int:
            def search(arr, left, right, value) -> int:
                if right >= left:
                    mid = left + (right - left) // 2
                    if arr[mid] == value:
                        return mid
                    elif arr[mid] > value:
                        return search(arr, left, mid - 1, value)
                    else:
                        return search(arr, mid + 1, right, value)
                else:
                    return -1
            return search(haystack, 0, len(haystack) - 1, needle)

        def intersect(l1, l2) -> list:
            answer = []
            for i in l1:
                search_result = binary_search(i, l2)
                if search_result != -1:
                    answer.append(i)
            return answer

        return intersect(list_1, list_2) if len(list_1) < len(list_2) else intersect(list_2, list_1)

    @staticmethod
    def builtin_intersection(set1, iterable) -> set:
        return set1.intersection(iterable)
