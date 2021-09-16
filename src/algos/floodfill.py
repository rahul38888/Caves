import queue
import itertools


def flood_fill(arr: list, x_cord, y_cord, visited: list = None) -> set:
    if visited is None:
        visited = [[False for x in y] for y in arr]

    q = queue.Queue()
    q.put((x_cord, y_cord))
    matching_val = arr[y_cord][x_cord]

    result = set()
    result.add((x_cord, y_cord))
    while not q.empty():
        x, y = q.get()
        visited[y][x] = True
        for i, j in itertools.product(range(-1, 2), range(-1, 2)):
            if 0 <= x + i < len(arr[0]) and 0 <= y + j < len(arr):
                if (i != 0 or j != 0) and arr[y + j][x + i] == matching_val and not visited[y + j][x + i]:
                    result.add((x + i, y + j))
                    q.put((x + i, y + j))
    return result


if __name__ == '__main__':
    arr = [[1, 0, 1, 1, 1, 1],
           [1, 0, 0, 0, 1, 1],
           [1, 1, 0, 0, 0, 1],
           [0, 0, 1, 1, 1, 1]]

    visited = [[False for x in y] for y in arr]
    print(flood_fill(arr, 1, 1, visited))
