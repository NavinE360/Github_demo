def test_addition(a, b):
    return a + b

# This test will pass
assert test_addition(1, 3) == 4  # Passes, since 1 + 3 == 4

# This test will fail (intentionally)
try:
    assert test_addition(1, 3) == 5  # Raises AssertionError
except AssertionError:
    print("Test failed: test_addition(1, 3) != 5")
