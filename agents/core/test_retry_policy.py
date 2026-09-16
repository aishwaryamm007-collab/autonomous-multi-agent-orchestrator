from agents.core.retry_policy import RetryPolicy


print("\n========== RETRY POLICY TEST ==========")


# Test 1: Default retry policy
policy = RetryPolicy()

print(f"Max retries: {policy.max_retries}")
print(f"Total attempts: {policy.total_attempts()}")

print(
    f"Should retry after 1 attempt: "
    f"{policy.should_retry(1)}"
)

print(
    f"Should retry after 3 attempts: "
    f"{policy.should_retry(3)}"
)


# Test 2: Custom retry policy
custom_policy = RetryPolicy(max_retries=1)

print("\nCustom policy:")
print(f"Max retries: {custom_policy.max_retries}")
print(
    f"Total attempts: "
    f"{custom_policy.total_attempts()}"
)

print(
    f"Should retry after 1 attempt: "
    f"{custom_policy.should_retry(1)}"
)

print(
    f"Should retry after 2 attempts: "
    f"{custom_policy.should_retry(2)}"
)


# Test 3: Negative retry count
print("\nNegative retry test:")

try:
    RetryPolicy(max_retries=-1)
except ValueError as error:
    print(f"Correctly rejected: {error}")


print("\n========== TEST COMPLETE ==========")