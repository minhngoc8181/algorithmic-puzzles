"""Exact checks and certificates for the authored teaching instances.

These small-instance solvers verify answers; they are not suggested to students
as efficient algorithms for every large input mentioned in a question.
"""
from collections import Counter
from functools import lru_cache
import heapq
import itertools
import math


def rope_cost(values):
    heap = list(values)
    heapq.heapify(heap)
    cost, steps = 0, []
    while len(heap) > 1:
        a, b = heapq.heappop(heap), heapq.heappop(heap)
        steps.append([a, b, a + b])
        cost += a + b
        heapq.heappush(heap, a + b)
    return cost, steps


def adjacent_merge(values):
    prefix = [0]
    for value in values:
        prefix.append(prefix[-1] + value)
    @lru_cache(None)
    def cost(i, j):
        if i == j:
            return 0, str(i + 1)
        value, k = min((cost(i, k)[0] + cost(k + 1, j)[0], k) for k in range(i, j))
        return value + prefix[j + 1] - prefix[i], f'({cost(i,k)[1]}+{cost(k+1,j)[1]})'
    return cost(0, len(values) - 1)


def coin_game(values):
    @lru_cache(None)
    def difference(i, j):
        if i > j:
            return 0
        return max(values[i] - difference(i + 1, j), values[j] - difference(i, j - 1))
    return (sum(values) + difference(0, len(values) - 1)) // 2


def strange_printer(text):
    text = ''.join(c for i, c in enumerate(text) if i == 0 or c != text[i-1])
    @lru_cache(None)
    def cost(i, j):
        if i > j:
            return 0
        return min([1 + cost(i + 1, j)] +
                   [cost(i + 1, k - 1) + cost(k, j) for k in range(i + 1, j + 1) if text[k] == text[i]])
    return cost(0, len(text) - 1)


def grundy_split(n):
    values = [0] * (n + 1)
    for size in range(3, n + 1):
        reachable = {values[a] ^ values[size - a] for a in range(1, (size + 1) // 2)}
        while values[size] in reachable:
            values[size] += 1
    return values[n], [a for a in range(1, (n + 1) // 2) if values[a] == values[n - a]]


def kayles(segments):
    g = [0] * (max(segments, default=0) + 1)
    for n in range(1, len(g)):
        reachable = {g[i] ^ g[n-i-1] for i in range(n)} | {g[i] ^ g[n-i-2] for i in range(n-1)}
        while g[n] in reachable:
            g[n] += 1
    total = 0
    for n in segments:
        total ^= g[n]
    moves = [(j + 1, i + 1, take) for j, n in enumerate(segments) for take in (1, 2)
             for i in range(n - take + 1) if total ^ g[n] ^ g[i] ^ g[n - i - take] == 0]
    return total, moves


def skyline(records):
    result, previous = [], 0
    for x in sorted({r[key] for r in records for key in ('left', 'right')}):
        height = max((r['height'] for r in records if r['left'] <= x < r['right']), default=0)
        if height != previous:
            result.append([x, height])
            previous = height
    return result


def closest_pairs(records):
    pairs = [(sum((a[key]-b[key])**2 for key in ('x','y')), a['id'], b['id'])
             for a,b in itertools.combinations(records,2)]
    minimum = min(p[0] for p in pairs)
    return minimum, [[a,b] for distance,a,b in pairs if distance == minimum]


def inversions(records):
    first = {r['first']: i for i, r in enumerate(records)}
    permutation = [first[r['second']] for r in records]
    return sum(permutation[i] > permutation[j] for i in range(len(records)) for j in range(i+1,len(records)))


def gas_starts(records):
    answer = []
    for start in range(len(records)):
        fuel = 0
        for step in range(len(records)):
            row = records[(start + step) % len(records)]
            fuel += row['fuel'] - row['cost']
            if fuel < 0:
                break
        else:
            answer.append(start + 1)
    return answer


def stabbing(records):
    points, certificate = [], []
    for row in sorted(records, key=lambda r: r['right']):
        if not points or points[-1] < row['left']:
            points.append(row['right'])
            certificate.append(row['id'])
    return points, certificate


def weighted_schedule(records):
    jobs = sorted(records, key=lambda r: (r['end'], r['start'], r['id']))
    best = [(0, [])]
    for i, job in enumerate(jobs):
        compatible = max((j+1 for j in range(i) if jobs[j]['end'] <= job['start']), default=0)
        take = (best[compatible][0] + job['reward'], best[compatible][1] + [job['id']])
        best.append(max(best[-1], take))
    return best[-1]


def partition(records):
    half = len(records) // 2
    def sums(rows):
        answer = [(0, [])]
        for row in rows:
            answer += [(total+row['strength'], chosen+[row['id']]) for total,chosen in answer]
        return answer
    left, right = sums(records[:half]), sorted(sums(records[half:]))
    import bisect
    total = sum(r['strength'] for r in records)
    result = (total, [])
    for value, selected in left:
        i = bisect.bisect_left(right, ((total/2)-value, []))
        for j in (i-1, i):
            if 0 <= j < len(right):
                result = min(result, (abs(total-2*(value+right[j][0])), selected+right[j][1]))
    return result


def bin_packing(records, capacity):
    n = len(records)
    dp, previous = [(n+1, capacity+1)] * (1 << n), [None] * (1 << n)
    dp[0] = (1, 0)
    for mask in range(1, 1 << n):
        bits = mask
        while bits:
            bit = bits & -bits
            i = bit.bit_length() - 1
            trips, load = dp[mask ^ bit]
            weight = records[i]['weight']
            candidate = (trips, load+weight) if load+weight <= capacity else (trips+1, weight)
            if candidate < dp[mask]:
                dp[mask], previous[mask] = candidate, i
            bits ^= bit
    mask, order = (1 << n)-1, []
    while mask:
        i = previous[mask]
        order.append(i)
        mask ^= 1 << i
    groups, load = [[]], 0
    for i in reversed(order):
        if load+records[i]['weight'] > capacity:
            groups.append([])
            load = 0
        groups[-1].append(records[i]['id'])
        load += records[i]['weight']
    return dp[-1][0], groups


def matching(records):
    assigned = {}
    def augment(row, visited):
        for position in row['accepts']:
            if position in visited:
                continue
            visited.add(position)
            if position not in assigned or augment(assigned[position], visited):
                assigned[position] = row
                return True
        return False
    for row in records:
        augment(row, set())
    return {row['id']: position for position,row in assigned.items()}


def set_cover(records, universe):
    target = set(universe)
    for count in range(len(records)+1):
        for group in itertools.combinations(records, count):
            if set().union(*(set(r['covers']) for r in group)) >= target:
                return [r['id'] for r in group]
    return None


def deadlines(records):
    schedule = {}
    for row in sorted(records, key=lambda r: (-r['reward'], r['id'])):
        for slot in range(row['deadline'], 0, -1):
            if slot not in schedule:
                schedule[slot] = row['id']
                break
    by_id = {r['id']: r for r in records}
    return sum(by_id[i]['reward'] for i in schedule.values()), schedule


def parallel_cooking(records, machines):
    """Binary search with an exact capacity feasibility certificate."""
    jobs = sorted(records, key=lambda r: -r['duration'])
    lower = max(jobs[0]['duration'], math.ceil(sum(r['duration'] for r in jobs)/machines))
    upper = sum(r['duration'] for r in jobs)
    def feasible(limit):
        loads, groups = [0]*machines, [[] for _ in range(machines)]
        failed = set()
        def place(index):
            if index == len(jobs):
                return [group[:] for group in groups]
            state = index, tuple(sorted(loads))
            if state in failed:
                return None
            seen = set()
            for stove in sorted(range(machines), key=lambda j: loads[j]):
                if loads[stove] in seen or loads[stove]+jobs[index]['duration'] > limit:
                    continue
                seen.add(loads[stove])
                loads[stove] += jobs[index]['duration']
                groups[stove].append(jobs[index]['id'])
                answer = place(index+1)
                if answer is not None:
                    return answer
                groups[stove].pop()
                loads[stove] -= jobs[index]['duration']
            failed.add(state)
            return None
        return place(0)
    while lower < upper:
        mid = (lower+upper)//2
        if feasible(mid) is None:
            lower = mid+1
        else:
            upper = mid
    return lower, feasible(lower)


def flowshop(records, no_wait=False):
    """Subset DP, independent of Johnson's sorting rule."""
    n = len(records)
    if not no_wait:
        totals = [0]*(1 << n)
        dp, predecessor = [0] + [math.inf]*((1 << n)-1), [None]*(1 << n)
        for mask in range(1, 1 << n):
            bit = mask & -mask
            totals[mask] = totals[mask ^ bit] + records[bit.bit_length()-1]['wash']
            for j in range(n):
                if mask >> j & 1:
                    value = max(totals[mask], dp[mask ^ (1 << j)]) + records[j]['dry']
                    if value < dp[mask]:
                        dp[mask], predecessor[mask] = value, j
        sequence, mask = [], (1 << n)-1
        while mask:
            j = predecessor[mask]
            sequence.append(records[j]['id'])
            mask ^= 1 << j
        return dp[-1], list(reversed(sequence))
    dp, parent = {}, {}
    for j in range(n):
        dp[1 << j, j], parent[1 << j, j] = 0, None
    for mask in range(1, 1 << n):
        for j in range(n):
            if (mask, j) not in dp:
                continue
            for k in range(n):
                if mask >> k & 1:
                    continue
                row, nxt = records[j], records[k]
                delay = max(row['wash'], row['wash'] + row['dry'] - nxt['wash'])
                key, value = (mask | (1 << k), k), dp[mask, j] + delay
                if value < dp.get(key, math.inf):
                    dp[key], parent[key] = value, j
    mask = (1 << n)-1
    value, j = min((dp[mask,j]+records[j]['wash']+records[j]['dry'], j) for j in range(n))
    sequence = []
    while j is not None:
        sequence.append(records[j]['id'])
        previous = parent[mask,j]
        mask, j = mask ^ (1 << j), previous
    return value, list(reversed(sequence))


def johnson(records):
    first = sorted((r for r in records if r['wash'] < r['dry']), key=lambda r: (r['wash'], r['id']))
    last = sorted((r for r in records if r['wash'] >= r['dry']), key=lambda r: (-r['dry'], r['id']))
    washer, dryer, trace = 0, 0, []
    for row in first + last:
        start = washer
        washer += row['wash']
        dry_start = max(washer, dryer)
        dryer = dry_start + row['dry']
        trace.append([row['id'], start, washer, dry_start, dryer])
    return dryer, trace


def sum_product(limit=100):
    original = [(x,y) for x in range(2,limit) for y in range(x+1,limit) if x+y <= limit]
    products = Counter(x*y for x,y in original)
    sums = {x+y for x,y in original if all(products[a*b] > 1 for a,b in original if a+b == x+y)}
    after_s = [(x,y) for x,y in original if x+y in sums]
    counts = Counter(x*y for x,y in after_s)
    after_p = [(x,y) for x,y in after_s if counts[x*y] == 1]
    counts = Counter(x+y for x,y in after_p)
    return [(x,y) for x,y in after_p if counts[x+y] == 1]


def birthday(records):
    days = Counter(r['day'] for r in records)
    months = {r['month'] for r in records if all(days[x['day']] > 1 for x in records if x['month'] == r['month'])}
    first = [r for r in records if r['month'] in months]
    day_counts = Counter(r['day'] for r in first)
    second = [r for r in first if day_counts[r['day']] == 1]
    month_counts = Counter(r['month'] for r in second)
    third = [r for r in second if month_counts[r['month']] == 1]
    return third, [len(records), len(first), len(second), len(third)]


def bridge(times):
    n, initial = len(times), ((1 << len(times))-1, 0)
    queue, distances = [(0, *initial)], {initial: 0}
    while queue:
        cost, mask, side = heapq.heappop(queue)
        if cost != distances[mask,side]:
            continue
        if mask == 0 and side == 1:
            return cost
        available = [i for i in range(n) if bool(mask >> i & 1) != bool(side)]
        for number in (1,2):
            for people in itertools.combinations(available,number):
                next_mask = mask
                for i in people:
                    next_mask ^= 1 << i
                key, value = (next_mask, 1-side), cost+max(times[i] for i in people)
                if value < distances.get(key, math.inf):
                    distances[key] = value
                    heapq.heappush(queue, (value, *key))


def lights(grid):
    n, size = len(grid), len(grid)**2
    rows = []
    for r in range(n):
        for c in range(n):
            mask = sum(1 << (rr*n+cc) for rr,cc in ((r,c),(r-1,c),(r+1,c),(r,c-1),(r,c+1))
                       if 0 <= rr < n and 0 <= cc < n)
            rows.append(mask | (grid[r][c] << size))
    pivots, rank = [], 0
    for column in range(size):
        selected = next((i for i in range(rank,size) if rows[i] >> column & 1), None)
        if selected is None:
            continue
        rows[rank], rows[selected] = rows[selected], rows[rank]
        for i in range(size):
            if i != rank and rows[i] >> column & 1:
                rows[i] ^= rows[rank]
        pivots.append(column)
        rank += 1
    if any(row == 1 << size for row in rows[rank:]):
        return []
    free = [column for column in range(size) if column not in pivots]
    solutions = []
    for choice in range(1 << len(free)):
        value = sum(1 << column for i,column in enumerate(free) if choice >> i & 1)
        for i,column in enumerate(pivots):
            if (rows[i] >> size & 1) ^ ((rows[i] & value).bit_count() & 1):
                value |= 1 << column
        solutions.append(value)
    return solutions
