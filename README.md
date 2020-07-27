# minimalSubsetSumAlgo


Given an array of positive integers, divide the array into two subsets such that the difference between the sum of the subsets is as small as possible.

For example, given `[5, 10, 15, 20, 25]`, return the sets `{10, 25}` and `{5, 15, 20}`, which has a difference of 5, which is the smallest possible difference.

I used dynamic programming to solve this problem in O(Sn) time, where S is the sum of elements in the array

    1. Sub-prob: x(i,s): divide array A[i:] into two subsets so that the 
        difference between the subsets is as small as possible and return this 
        smallest difference where s is the pre-existing sum. We can create a 
        sum by labeling one subset as positive and another as negativen and 
        taking the absolute value
    2. Relation: x(i,s) = min(x(i + 1, s + A[i]),x(i + 1, s - A[i]))
    3. Topological order: always increase i
    4. Base: x(n,s) = s
    5. Original: x(0,0)
    6. Time: O(Sn)
