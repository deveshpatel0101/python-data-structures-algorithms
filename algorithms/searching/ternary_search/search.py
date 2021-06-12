class TernarySearch:
    def search(self, arr, key):
        low = 0
        high = len(arr)-1

        while high >= low:
            mid1 = low + int((high-low)/3)
            mid2 = high - int((high-low)/3)

            if arr[mid1] == key:
                return True, mid1
            elif arr[mid2] == key:
                return True, mid2
            elif key < arr[mid1]:
                high = mid1-1
            elif key > arr[mid1] and key < arr[mid2]:
                low = mid1+1
                high = mid2-2
            elif key > arr[mid2]:
                low = mid2+1

        return False, None


test = TernarySearch()
print(test.search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))
print(test.search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
print(test.search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
print(test.search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
print(test.search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
print(test.search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))
print(test.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1))
print(test.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))
print(test.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
print(test.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))
print(test.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 7))
print(test.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
print(test.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
print(test.search([1, 2, 3, 4, 5, 6, 7, 8, 9], -1))
print(test.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5.5))
