# DAY 1 - 10/6/26

# D1P1
# Hash Map: Target Complement Search
# Original Pattern: Two Sum

# Scenario
# An API rate-limiting proxy tracks incoming network requests by their response latency in milliseconds. To optimize multi-threading, the system needs to pair two requests whose combined latencies equal a fixed total quota target_latency.

# Write a function find_latency_pair(latencies: list[int], target_latency: int) -> list[int] that returns the 0-based indices of the two requests that sum to target_latency. Return [] if no valid pair exists.

def find_latency_pair(latencies: list[int], target_latency: int) -> list[int]: 
    seen = {}

    for i, latency in enumerate(latencies): 
        Complement = target_latency - latency

        if Complement in seen: 
            return [seen[Complement], i]

        seen[latency] = i
    
    return []

# D1P2
# Hash Map + Categorization: Signature Keys
# Original Pattern: Group Anagrams

# Scenario
# A log processing system ingests query parameters from web traffic. Parameter strings that contain the exact same character counts belong to the same route pattern, regardless of key ordering.

# Write a function group_query_signatures(queries: list[str]) -> list[list[str]] that groups parameter strings sharing identical character frequencies.
from collections import defaultdict 

def group_query_signatures(queries: list[str]) -> list[list[str]]: 
    anagram_map = defaultdict(list)

    for query in queries:
        sorted_key = "".join(sorted(query))

        anagram_map[sorted_key].append(query)
    
    return list(anagram_map.values())

# D1P3
# Min-Heap: Priority Threshold
# Original Pattern: Top K Frequent Words / K Closest Points

# Scenario
# A datacenter server monitor tracks running background tasks by their memory consumption (in megabytes). When memory spikes occur, the supervisor process needs to terminate the k tasks using the most memory.

# Write a function top_k_memory_tasks(tasks: list[tuple[str, int]], k: int) -> list[str] where each task is a tuple of (task_name, memory_mb). Return the names of the k largest memory consumers.

def op_k_memory_tasks(tasks: list[tuple[str, int]], k: int) -> list[str]:
    min_heap = []

    for task_name. memory_mb in task: 
        heapq.heappush(min_heap, (memory_mb, task_name))

        if len(min_heap) > k: 
            heapq.heappop(min_heap)
    
    return [task_name for memory_mb, task_name in min_heap]

# D1P4
# Dynamic Sliding Window: Variable Length Tracking
# Original Pattern: Longest Substring Without Repeating Characters

# Scenario
# An IoT sensor records a stream of status codes over time represented by characters in a string status_stream. System diagnostics need to calculate the duration of the longest continuous run of status events that contains no repeated codes.

# Write a function longest_unique_status_run(status_stream: str) -> int.

def longest_unique_status_run(status_stream: str) -> int: 
    seen = {}

    left = 0
    max_length = 0

    for right, char in enumerate(status_stream):
        if char in seen and seen[char] >= left: 
            left = seen[char] + 1

        seen[char] = right 
        max_length = max(max_length, right - left + 1)
    
    return max_length

# D1P5
# Dynamic Sliding Window: Subarray Target Condition
# Original Pattern: Minimum Size Subarray Sum

# Scenario
# A payment gateway receives a sequential array of transaction amounts transactions. A risk monitor needs to find the shortest continuous sequence of transactions whose total value reaches or exceeds a alert threshold threshold.

# Write a function min_transactions_for_threshold(threshold: int, transactions: list[int]) -> int. Return 0 if no contiguous subarray satisfies the threshold.

def min_transactions_for_threshold(threshold: int, transactions: list[int]) -> int: 
    left = 0
    current_sum = 0
    min_len = float("inf")

    for right in range(len(transactions)): 
        current_sum += transactions[right]

        while current_sum >= threshold: 
            min_len = min(min_len, right - left + 1)

            current_sum -= transactions[left] 
            left += 1

    return min_len if min_len != float("inf") else 0 

# D1P6
