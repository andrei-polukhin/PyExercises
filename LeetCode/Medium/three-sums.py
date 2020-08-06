def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    from itertools import combinations
    """
    Using the itertools library is the fastest
    way to retrieve all triplets.
    """

    solutions = []
    triplets = list(combinations(nums, 3))
    for triplet in triplets:
        if sum(triplet) == 0:
            """
            Appending only those triplets
            which in sum give 0.
            """
            solutions.append(list(triplet))

    """
    Regrettably, we can get de-facto duplicate triplets
    like [-1, 0, 1] and [0,-1,1].
    Even more, applying set() is impossible as in-list
    tuples are NOT immutable and we will get TypeError!
    """

    solutions = list(set(tuple(sorted(sub)) for sub in solutions))
    """
    A workaround, though memory-consuming which finally
    allows to apply set() after sorting and transferring
    to tuples.
    """
    solutions = [list(s) for s in solutions]
    # -- Create lists from in-list tuples, as required.
    return solutions


print(threeSum([13,-14,-10,-4,4,4,0,-14,5,-9,-3,-10,14,7,-3,-4,-3,12,-14,2,-11,-6,0,-7,13,-2,-7,-11,-14,-13,5,14,-12,11,-13,-1,-8,2,0,4,1,4,10,-8,-11,-8,3,1,11,4,-12,8,5,-4,-14,-4,9,-13,-8,2,-11,12,-7,14,0,-5,-2,7,5,5,-3,13,-6,-8,-10,-10,-9,0,6,-12,11,2,11,1,13,4,12,-1,6,-11,-14,2,9,-6,1,-6,-4,14,-13,8,4,-1,6,6,-2,11,11,4,-4,-5,-1,-8,12,-13,1,10,7,-10,-14,-10,-5,-13,0,11]))
print("\n\n", threeSum([0,0,0,0]))
print("\n\n", threeSum([-1,0,1,-2,2,1]))

"""
Unfortunately, memory limit exceeded! But as for an aspiring
Junior Python developer - this is a decent solution for a task
of the Medium difficulty."""
