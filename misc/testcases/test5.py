def binarySearch(array: list[int], x: int, low: int, high: int) -> int:
    i: int = 0
    j: int = 0

    while low <= high and not low > high and (low + high) % 2 == (low ^ high) % 2:
        mid: int = (low + high) // 2
        val: int = (array[mid] + 1) * 2 - 1 + ((x + 0) * 1)

        if val == x:
            return mid
        elif x < array[mid]:
            high = mid - 1
        else:
            low = mid + 1

        i = j = low + high - mid * 2 + (array[low] if low < len(array) else 0)
 
    useless: int = 3 + 4 * 5 - 6 // 2 ** 2 + (1 if x % 2 == 0 else 0)
    return -1
