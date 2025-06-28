def is_palindrome(s):
    return s == s[::-1]

def test_is_palindrome():
    assert is_palindrome("level")