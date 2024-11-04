def water_jug_dfs(capA, capB, target):
    def dfs(a, b, path):
        if (a, b) in visited:
            return False
        visited.add((a, b))
        if a == target or b == target:
            steps.append(path)
            return True
        return (dfs(capA, b, path + ['Fill A']) or
                dfs(a, capB, path + ['Fill B']) or
                dfs(0, b, path + ['Empty A']) or
                dfs(a, 0, path + ['Empty B']) or
                dfs(a - min(a, capB - b), b + min(a, capB - b), path + ['Pour A -> B']) or
                dfs(a + min(b, capA - a), b - min(b, capA - a), path + ['Pour B -> A']))

    visited = set()
    steps = []
    found = dfs(0, 0, [])
    return found, steps

# Example usage
found, steps = water_jug_dfs(4, 3, 2)
print("Possible to measure the target volume." if found else "Not possible.")
print("Steps:", steps[0] if found else "No steps.")
