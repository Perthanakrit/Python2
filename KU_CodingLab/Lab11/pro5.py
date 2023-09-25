result_elab = input()
corrent_input = input()

corrent_result = []
for c in corrent_input:
    if c not in corrent_result:
        corrent_result.append(c)

passed = 0
for c in corrent_result:
    for re in result_elab:
        if (c == re):
            passed += 1

total_case = len(result_elab) - 2 if len(result_elab) - 2 != 0 else 1
persent = (passed / total_case) * 100
print(passed)
print(f"{persent:.2f}")