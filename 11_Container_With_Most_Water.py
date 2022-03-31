### [11\. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

Difficulty: **Medium**  

Related Topics: [Array](https://leetcode.com/tag/array/), [Two Pointers](https://leetcode.com/tag/two-pointers/), [Greedy](https://leetcode.com/tag/greedy/)


You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i<sup>th</sup>` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return _the maximum amount of water a container can store_.

**Notice** that you may not slant the container.

**Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

**Example 2:**

```
Input: height = [1,1]
Output: 1
```

**Constraints:**

*   `n == height.length`
*   `2 <= n <= 10<sup>5</sup>`
*   `0 <= height[i] <= 10<sup>4</sup>`


#### Solution

Language: **Python3**

```python3
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(height)-1
        while l < r:
            if height[l] < height[r]:
                max_area = max(max_area, height[l]*(r-l))
                l+=1
            else:
                max_area = max(max_area, height[r]*(r-l))
                r-=1
        return max_area
```
