class Solution:
    def merge(self, arr, l, m, r):
        # Create temp arrays for left and right subarrays
        left = arr[l:m+1]   # arr[l..m]
        right = arr[m+1:r+1] # arr[m+1..r]

        # Initial indexes for left, right and merged arrays
        i = 0  # Initial index of left subarray
        j = 0  # Initial index of right subarray
        k = l  # Initial index of merged array

        # Merge the temp arrays back into arr[l..r]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy the remaining elements of left[], if any
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy the remaining elements of right[], if any
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def mergeSort(self, arr, l, r):
        # Base case: if there's only one element, do nothing
        if l < r:
            # Find the middle point
            m = (l + r) // 2

            # Recursively sort the first and second halves
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)

            # Merge the sorted halves
            self.merge(arr, l, m, r)


# Example usage:
arr_test = [4, 1, 3, 9, 7]
solution = Solution()
solution.mergeSort(arr_test, 0, len(arr_test) - 1)
print(arr_test)  # Expected output: [1, 3, 4, 7, 9]
