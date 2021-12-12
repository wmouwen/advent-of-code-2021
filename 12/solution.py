import sys


def traverse(graph: dict, source: str, sink: str, revisits: int, current: str = None, visited: list = None) -> int:
    current = current if current is not None else source
    visited = visited if visited is not None else []

    if current == sink:
        return 1

    if current in visited:
        if current != source and revisits:
            revisits -= 1
        else:
            return 0

    if current.islower():
        visited.append(current)

    paths = sum(traverse(graph, source, sink, revisits, target, visited) for target in graph[current])

    if current in visited:
        visited.remove(current)

    return paths


graph = {}
for line in sys.stdin:
    source, target = line.strip().split('-')

    if source not in graph:
        graph[source] = []
    if target not in graph:
        graph[target] = []

    graph[source].append(target)
    graph[target].append(source)

print(traverse(graph, 'start', 'end', 0))
print(traverse(graph, 'start', 'end', 1))
