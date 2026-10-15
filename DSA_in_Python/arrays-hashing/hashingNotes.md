# Hashing: 
Hashing is a process that takes an input and transforms it into a value using a function called a hash function.

Example: (hash set)
    numbers = [10, 42, 7, 18, 25]

    number_set = set(numbers)

    print(42 in number_set)  # True
    print(99 in number_set)  # False

A set uses hashing to support efficient membership checks on average.

**Interview takeaway: When a problem repeatedly asks you to check whether something exists, hashing should be one of the first techniques you consider.**

## What is a hash function?
A hash function takes a key and produces a hash value.

A good hash function should distribute keys reasonably well across the available storage, rather than sending too many keys to the same location.

## What is a hash collision?
A hash collision occurs when two different keys map to the same hash table location.

Ex: 
    hash_f(k) = k mod 5
    h(12) = 2
    h(17) = 2
    // collision

# Hash tables, hash maps, and dictionaries
* A hash table is a data structure that uses hashing to organize stored information.
* A hash map stores associations between keys and values using a hash table.
* Example: 
    student_grades = {
        "Alice": 90,
        "Bob": 85,
        "Charlie": 94
    }

    print(student_grades["Bob"])  # 85

* Common dict operations: 

        grades = {"Alice": 90, "Bob": 85}
        # Access a value
        print(grades["Alice"])  # 90

        # Add a new key-value pair
        grades["Charlie"] = 94

        # Update an existing value
        grades["Alice"] = 95

        # Check whether a key exists
        print("Bob" in grades)  # True

        # Remove a key-value pair
        del grades["Bob"]

        # Safely retrieve a value, with a default if missing
        print(grades.get("David", 0))  # 0


# What is a set?
A set is a collection of unique elements. Python's built-in set uses hashing to support efficient membership checking.

Example: 
    numbers = {10, 20, 30} // defines by {}

    numbers.add(40)
    numbers.add(20)

    print(numbers)        # Contains 10, 20, 30, 40
    print(20 in numbers)  # True

**Need to remember whether an element has appeared? Use a set.**

# The three most important hashing patterns for interviews
1. Pattern A: Duplicate detection
    * Problem: Determine whether an array contains any duplicate values.

    def contains_duplicate(nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False


    print(contains_duplicate([4, 2, 7, 2]))  # True
    print(contains_duplicate([4, 2, 7, 9]))  # False

2. Pattern B: Frequency counting
    * Problem: Count how many times each number appears.

    def count_frequencies(nums):
        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        return counts

    print(count_frequencies([2, 3, 2, 5, 3, 2]))
    # {2: 3, 3: 2, 5: 1}

    * A shorter way: 
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

    * `counts.get(num, 0)` retrieves the current count, or 0 if the number has not appeared before.

3. Pattern C: Fast lookup and the Two Sum problem
    * **This is the most important question on leetcode**
    * Problem: Given an array of integers and a target, return the indices of two numbers that add up to the target. Assume exactly one solution exists and you cannot use the same element twice.

    def two_sum(nums, target):
        seen = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], i]

            seen[num] = i

        return []
        
        print(two_sum([2, 7, 11, 15], 9)) # [0, 1]
