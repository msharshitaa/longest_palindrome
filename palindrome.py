def longest_palindromic_substring(A):
    def ex(left, right):
        while left >= 0 and right < len(A) and A[left] == A[right]:
            left -= 1
            right += 1
        return A[left + 1:right]
    longest = ""
    for i in range(len(A)):
        palindrome1 = ex(i, i)
        palindrome2 = ex(i, i + 1)
        if len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) > len(longest):
            longest = palindrome2
    return longest
A = input()
print(longest_palindromic_substring(A))
