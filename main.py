def is_eligible_for_discount(age: int) -> bool:
    """
    Determines if a customer is eligible for a senior discount.
    Original logic: age is 65 or older.
    """
    return age >= 65 # Original code

def test_original_function_weak():
    """
    A weak test for is_eligible_for_discount.
    It only checks one case that should be true.
    """
    print("\n--- Running WEAK test on ORIGINAL code ---")
    try:
        assert is_eligible_for_discount(70) is True, "Test Failed: 70 should be eligible"
        print("WEAK test PASSED for age 70.")
    except AssertionError as e:
        print(f"WEAK test FAILED: {e}")
    # This test is weak because it doesn't check the boundary condition (65)
    # or cases that should be false (e.g., 64).

def is_eligible_for_discount_mutated(age: int) -> bool:
    """
    A mutated version of is_eligible_for_discount.
    The operator `>=` is changed to `>`.
    This mutation means 65-year-olds are no longer eligible.
    """
    return age > 65 # MUTATION: changed >= to >

def demonstrate_weak_test_and_mutation():
    """
    Shows how a weak test fails to detect a code mutation.
    """
    print("\n--- Demonstrating WEAK test vs. MUTATED code ---")
    print("Applying a mutation: `age >= 65` changed to `age > 65`.")
    try:
        # We're running the WEAK test logic against the MUTATED function
        assert is_eligible_for_discount_mutated(70) is True, "Mutated Test Failed: 70 should be eligible"
        print("WEAK test PASSED against mutated code. (MUTANT SURVIVED!)")
        print("  Explanation: The weak test did not cover the edge case affected by the mutation.")
    except AssertionError as e:
        print(f"WEAK test FAILED against mutated code. (MUTANT KILLED!) - {e}")
        print("  Explanation: This should not happen with this specific weak test and mutation.")


def test_original_function_strong():
    """
    A stronger test for is_eligible_for_discount.
    It checks boundary conditions and negative cases.
    """
    print("\n--- Running STRONG test on ORIGINAL code ---")
    try:
        assert is_eligible_for_discount(65) is True, "Test Failed: 65 should be eligible (boundary)"
        print("STRONG test PASSED for age 65 (boundary).")
        assert is_eligible_for_discount(70) is True, "Test Failed: 70 should be eligible"
        print("STRONG test PASSED for age 70 (above boundary).")
        assert is_eligible_for_discount(64) is False, "Test Failed: 64 should not be eligible"
        print("STRONG test PASSED for age 64 (below boundary).")
    except AssertionError as e:
        print(f"STRONG test FAILED: {e}")


def demonstrate_strong_test_and_mutation():
    """
    Shows how a strong test successfully detects a code mutation.
    """
    print("\n--- Demonstrating STRONG test vs. MUTATED code ---")
    print("Applying the same mutation: `age >= 65` changed to `age > 65`.")
    try:
        # We're running the STRONG test logic against the MUTATED function
        # The first assertion (age 65) is expected to fail with the mutation.
        assert is_eligible_for_discount_mutated(65) is True, "Mutated Test Failed: 65 should be eligible"
        print("STRONG test PASSED against mutated code. (MUTANT SURVIVED!)")
        # If it reaches here, it means the mutation was not caught, which is unexpected for a strong test.
    except AssertionError as e:
        print(f"STRONG test FAILED against mutated code. (MUTANT KILLED!) - {e}")
        print("  Explanation: The strong test detected the mutation by failing on the boundary case (age 65).")


if __name__ == "__main__":
    print("--- Mutation Testing Concept Example ---")

    print("\n" + "="*60)
    print("Scenario 1: Weak Test Suite")
    print("="*60)
    test_original_function_weak()
    demonstrate_weak_test_and_mutation()

    print("\n" + "="*60)
    print("Scenario 2: Strong Test Suite")
    print("="*60)
    test_original_function_strong()
    demonstrate_strong_test_and_mutation()

    print("\n" + "="*60)
    print("Summary:")
    print("A weak test (Scenario 1) failed to detect a subtle code change (mutant survived).")
    print("A strong test (Scenario 2) successfully detected the same code change (mutant killed).")
    print("Mutation testing helps identify gaps in your test suite that traditional coverage metrics might miss.")
    print("="*60)
