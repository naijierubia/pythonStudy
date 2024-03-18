class IterableHelper:
    @staticmethod
    def find_all(iterable, func_condition):
        for item in iterable:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(iterable, func_first):
        for item in iterable:
            if func_first(iterable):
                return item

    @staticmethod
    def get_count(iterable, func_count):
        count = 0
        for item in iterable:
            if func_count(item):
                count += 1
        return count

    @staticmethod
    def print_all(iterable, func_format):
        for item in iterable:
            yield func_format(item)

    @staticmethod
    def is_exist(iterable, func):
        for item in iterable:
            if func(item):
                return True
        return False

    @staticmethod
    def sum_item(iterable, func):
        sum = 0
        for item in iterable:
            sum += func(item)
        return sum

    @staticmethod
    def find_max(iterable, func):
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if func(iterable[i]) > func(max_value):
                max_value = iterable[i]
        return max_value

    @staticmethod
    def find_min(iterable, func):
        min_value = iterable[0]
        for i in range(1, len(iterable)):
            if func(iterable[i]) < func(min_value):
                min_value = iterable[i]
        return min_value

    @staticmethod
    def delete_all(iterable, func):
        """
        删除要倒着删
        """
        count = 0
        for i in range(len(iterable) - 1, -1, -1):
            if func(iterable[i]):
                del iterable[i]
                count += 1
        return count

    @staticmethod
    def order_by(iterable, func):
        for x in range(len(iterable) - 1):
            for y in range(x + 1, len(iterable)):
                if func(iterable[y]) < func(iterable[x]):
                    iterable[y], iterable[x] = iterable[x], iterable[y]
        return iterable

    @classmethod
    def down_by(cls, iterable, func):
        for x in range(len(iterable) - 1):
            for y in range(x + 1, len(iterable)):
                if func(iterable[y]) > func(iterable[x]):
                    iterable[y], iterable[x] = iterable[x], iterable[y]
        return iterable

