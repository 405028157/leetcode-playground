```java
package lc;

import java.util.*;


class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;
  TreeNode() {}
  TreeNode(int val) { this.val = val; }
  TreeNode(int val, TreeNode left, TreeNode right) {
      this.val = val;
      this.left = left;
      this.right = right;
  }
}


public class Solution {
    int maxDepth = 0;
    List<Integer> res = new ArrayList<>();

    public List<Integer> rightSideView(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        if (root == null) {
            return res;
        }

        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }

                if (i == size - 1) {
                    res.add(node.val);
                }
            }
        }

        return res;
    }
}
```

#### 快排

```java
public class Solution {
    public void myQuickSort(int[] array) {
        int n = array.length;
        quickSort(array, 0, n - 1);
    }

    public void quickSort(int[] array, int left, int right) {
        if (left < right) {
            int index = partition(array, left, right);
            quickSort(array, left, index - 1);
            quickSort(array, index + 1, right);
        }
    }

    public int partition(int[] array, int left, int right) {
        int temp = array[left];
        int i = left, j = right;
        while (i < j) {
            while (i < j && array[j] >= temp) j--;
            while (i < j && array[i] <= temp) i++;

            int s = array[i];
            array[i] = array[j];
            array[j] = s;
        }

        array[left] = array[i];
        array[i] = temp;
        return i;
    }

    public static void main(String[] args) {
        int[] array = {4,1,3,2,10};
        Solution s = new Solution();
        s.myQuickSort(array);

        for (int ele : array) {
            System.out.print(ele + " ");
        }
    }
}
```

#### **poj 滑雪 http://poj.org/problem?id=1088**

```java
// 记忆化递归
import java.util.Scanner;

public class Solution {
    static int[][] dp;
    static int[][] height;
    static int[][] move = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    static int ans;
    static int R, C;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        R = sc.nextInt();
        C = sc.nextInt();
        height = new int[R][C];
        dp = new int[R][C];
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                height[i][j] = sc.nextInt();
            }
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                int cur = dfs(i, j);
                ans = Math.max(ans, cur);
            }
        }

        System.out.println(ans);
    }

    public static int dfs(int i, int j) {
        if (dp[i][j] > 0) {
            return dp[i][j];
        }

        int max = 0;
        if (i - 1 >= 0 && height[i][j] > height[i - 1][j]) {
            max = Math.max(max, dfs(i - 1, j));
        }
        if (j - 1 >= 0 && height[i][j] > height[i][j - 1]) {
            max = Math.max(max, dfs(i, j - 1));
        }
        if (i + 1 < R && height[i][j] > height[i + 1][j]) {
            max = Math.max(max, dfs(i + 1, j));
        }
        if (j + 1 < C && height[i][j] > height[i][j + 1]) {
            max = Math.max(max, dfs(i, j + 1));
        }

        dp[i][j] = max + 1;
        return dp[i][j];
    }

}
```

#### 快速指数

```java
package lc;


public class Solution {
    static int mod = 1000000007;
    static long ans = 1;

    public static void main(String[] args) {
        System.out.println(fast_power(6, 1000));
    }

    /*
    * base 底数
    * n 指数
    */
    public static long fast_power(long base, int n) {
        // n = 7, 111
        while (n != 0) {
            if ((n & 1) != 0) {
                ans = (ans % mod) * base;
            }
            base = (base * base) % mod;
//            base = (base % mod) * (base % mod); 错误
            n >>= 1;
        }

        return ans % mod;
    }
}
```

#### 并查集

```java
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static int n, m;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLine()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            Relation[] relations = new Relation[m];
            for (int i = 0; i < m; i++) {
                relations[i] = new Relation(sc.nextInt(), sc.nextInt(), sc.nextInt() == 1);
            }

            Union uf = new Union(n);
            for (int i = 0; i < m; i++) {
                Relation relation = relations[i];
                if (relation.isSameCity) {
                    uf.union(relation.a, relation.b);
                }
            }

            System.out.println(uf.count());
        }
    }

    static class Relation {
        int a;
        int b;
        boolean isSameCity;

        Relation(int a, int b, Boolean isSameCity) {
            this.a = a;
            this.b = b;
            this.isSameCity = isSameCity;
        }
    }

    static class Union {
        public int[] parents;
        public int[] ranks;
        public int n;
        public Union(int n) {
            this.n = n;
            parents = new int[n + 1];
            for (int i = 1; i <= n; i++) {
                parents[i] = i;
            }
            ranks = new int[n + 1];
        }

        public int findParent(int x) {
            if (parents[x] == x) {
                return x;
            }
            parents[x] = findParent(parents[x]);
            return parents[x];
        }

        public void union(int x, int y) {
            int rootx = findParent(x);
            int rooty = findParent(y);

            if (rootx == rooty) {
                return;
            }

            if (ranks[rootx] < ranks[rooty]) {
                int temp = rootx;
                rootx = rooty;
                rooty = temp;
            }

            parents[rooty] = rootx;
            if (ranks[rooty] == ranks[rootx]) {
                ranks[rootx]++;
            }
        }

        public int count() {
            int count = 0;
            int parent = parents[1];

            for (int i = 2; i <= n; i++) {
                if (parents[i] == parent) {
                    count++;
                }
            }

            return count;
        }
    }
}
```

##### [105. 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    Map<Integer, Integer> map = new HashMap<>();
    int[] preorder, inorder;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        this.inorder = inorder;
        int n = preorder.length;
        for (int i = 0; i < inorder.length; i++) {
            map.put(inorder[i], i);
        }

        return build(0, n - 1, 0, n - 1);
    }

    public TreeNode build(int preleft, int preright, int inleft, int inright) {
        if (preleft > preright) {
            return null;
        }

        int root = map.get(preorder[preleft]);
        // [inleft, root - 1] 左子树
        TreeNode node = new TreeNode(preorder[preleft]);
        // x = root - inleft + preleft
        node.left = build(preleft + 1, root - inleft + preleft, inleft, root - 1);
        node.right = build(root - inleft + preleft + 1, preright, root + 1, inright);
        return node;
    }
}
```

##### [剑指 Offer 34. 二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> res = new ArrayList<>();
    public Deque<Integer> combination = new LinkedList<>();
    public List<List<Integer>> pathSum(TreeNode root, int target) {
        dfs(root, target);
        return res;
    }

    public void dfs(TreeNode curNode, int curSum) {
        if (curNode == null) {
            return;
        }

        if (curNode.left == null && curNode.right == null) {
            if (curSum == curNode.val) {
                combination.offerLast(curNode.val);
                res.add(new ArrayList<Integer>(combination));
                combination.pollLast();
            }
            return;
        }

        combination.offerLast(curNode.val);
        dfs(curNode.left, curSum - curNode.val);
        dfs(curNode.right, curSum - curNode.val);
        combination.pollLast();
    }
}
```

#### [22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/)

```java
class Solution {
    Deque<String> combination = new LinkedList<String>();
    List<String> res = new ArrayList<>();
    int n;
    public List<String> generateParenthesis(int n) {
        this.n = n;
        dfs(0);
        return res;
    }

    public void dfs(int num) {
        if (num == n * 2) {
            if (judge()) {
                res.add(String.join("", combination));
            }
            return;
        }

        combination.offerLast("(");
        dfs(num + 1);
        combination.pollLast();
        combination.offerLast(")");
        dfs(num + 1);
        combination.pollLast();
    }

    public boolean judge() {
        int bal = 0;
        for (String c : combination) {
            if (c == "(") {
                bal++;
            }
            else {
                bal--;
            }

            if (bal < 0) {
                return false;
            }
        }

        return bal == 0;
    }
}
```

#### [72. 编辑距离](https://leetcode-cn.com/problems/edit-distance/)

```java
/*
dp[i][j] = dp[i - 1][j - 1], word1[i] == word2[j]
dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1 word1[i] != word2[j]

horss, ros
*/

class Solution {
    public int minDistance(String word1, String word2) {
        int n1 = word1.length();
        int n2 = word2.length();
        int dp[][] = new int[n1 + 1][n2 + 1];

        for (int i = 1; i <= n1; i++) {
            dp[i][0] = i;
        }

        for (int i = 1; i <= n2; i++) {
            dp[0][i] = i;
        }

        for (int i = 1; i <= n1; i++) {
            for (int j = 1; j <= n2; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                }
                else {
                    dp[i][j] = Math.min(Math.min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1;
                }
            }
        }

        return dp[n1][n2];
    }
}
```

#### Map排序

```java
public class Solution {
    public static void main(String[] args) {
        Map<Integer, String> map = new TreeMap<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o1 - o2;
            }
        });

        map.put(5, "asldkf");
        map.put(4, "clsss");
        map.put(10, "bdsklfsda");

        for (Map.Entry<Integer, String> entry : map.entrySet()) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }

        Set<Map.Entry<Integer, String>> set = new TreeSet<>(new Comparator<Map.Entry<Integer, String>>() {
            @Override
            public int compare(Map.Entry<Integer, String> o1, Map.Entry<Integer, String> o2) {
                return o1.getValue().compareTo(o2.getValue());
            }
        });

        set.addAll(map.entrySet());
        for (Map.Entry<Integer, String> entry : set) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }
}
```

#### [24. 两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

 /*
one -> two -> three
one->  three -> two ->
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode one = new ListNode(0, head), two, three, four;
        ListNode dummyHead = one;

        two = one.next;
        three = two == null ? null : two.next;

        if (two == null || three == null) {
            return head;
        }

        while (two != null && three != null) {
            four = three.next;

            one.next = three;
            three.next = two;
            two.next = four;

            one = two;
            two = two.next;
            three = two == null ? null : two.next;
        }

        return dummyHead.next;
    }
}
```

#### [剑指 Offer 18. 删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/)

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode deleteNode(ListNode head, int val) {
        ListNode pre = new ListNode(-1, head), cur = head;
        ListNode dummyHead = pre;

        while (cur.val != val) {
            pre = cur;
            cur = cur.next;
        }

        pre.next = cur.next;
        cur.next = null;

        return dummyHead.next;
    }
}
```

#### [剑指 Offer 55 - II. 平衡二叉树](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/)

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        return height(root) != -1;
    }

    public int height(TreeNode node) {
        if (node == null) {
            return 0;
        }

        int left = height(node.left);
        int right = height(node.right);

        if (left == -1 || right == -1 || Math.abs(left - right) > 1) {
            return -1;
        }

        return Math.max(left, right) + 1;
    }
}
```

#### [109. 有序链表转换二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/)

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    List<Integer> list = new ArrayList<>();
    public TreeNode sortedListToBST(ListNode head) {
        ListNode cur = head;
        while (cur != null) {
            list.add(cur.val);
            cur = cur.next;
        }

        return buildTree(0, list.size() - 1);
    }

    public TreeNode buildTree(int left, int right) {
        if (left > right) {
            return null;
        }

        int mid = left + (right - left) / 2;
        TreeNode root = new TreeNode(list.get(mid));
        root.left = buildTree(left, mid - 1);
        root.right = buildTree(mid + 1, right);
        return root;
    }
}
```

#### [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

```java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return new int[]{-1, -1};
        }
        int[] res = new int[2];
        res[0] = findFirst(nums, target);
        res[1] = findLast(nums, target);

        return res;
    }

    public int findFirst(int[] nums, int target) {
        int n = nums.length;
        // [l, r]
        int l = 0, r = n - 1;
        while (l <= r) {
            int mid = (l + r) >> 1;
            if (nums[mid] == target) {
                r = mid - 1;
            }
            else if (nums[mid] < target) {
                l = mid + 1;
            }
            else {
                r = mid - 1;
            }
        }

        if (l == n || nums[l] != target) {
            return -1;
        }

        return l;
    }

    public int findLast(int[] nums, int target) {
        int n = nums.length;
        int l = 0, r = n - 1;
        while (l <= r) {
            int mid = (l + r) >> 1;
            if (nums[mid] <= target) {
                l = mid + 1;
            }
            else {
                r = mid - 1;
            }
        }

        if (r == -1 || nums[r] != target) {
            return -1;
        }

        return r;
    }
}
```

#### [69. x 的平方根](https://leetcode-cn.com/problems/sqrtx/)

```java
class Solution {
    public int mySqrt(int x) {
        if (x < 0) {
            return -1;
        }
        int l = 0, r = x;
        // [l, r]
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if ((long) mid * mid <= x) {
                l = mid + 1;
            }
            else {
                r = mid - 1;
            }
        }

        return r;
    }
}
```

#### [239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)

```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> queue = new LinkedList<>();
        List<Integer> res = new ArrayList<>();
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (!queue.isEmpty() && queue.peekFirst() < i - 2) {
                queue.pollFirst();
            }

            // System.out.println(queue.peekLast());
            while (!queue.isEmpty() && nums[queue.peekLast()] < nums[i]) {
                queue.pollLast();
            }

            queue.offerLast(i);

            if (i >= 2) {
                res.add(nums[queue.peekFirst()]);
            }
        }

        int[] ret = new int[n - 2];
        int index = 0;
        for (Integer i : res) {
            ret[index++] = i;
        }

        return ret;
        // System.out.println(res);
        // return new int[10];
    }
}
```

#### [剑指 Offer II 076. 数组中的第 k 大的数字](https://leetcode-cn.com/problems/xx4gT2/)

```java
// 快排
class Solution {
    public int findKthLargest(int[] nums, int k) {
        // 3,2,3,1,2,4,5,5,6
        // 1 2 2 3 3 4 5 5 6
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int pIndex = partition(nums, left, right);
            if (pIndex == k - 1) {
                return nums[pIndex];
            }
            else if (pIndex < k - 1) {
                left = pIndex + 1;
            }
            else {
                right = pIndex - 1;
            }
        }
        
        return -1;
    }

    public int partition(int[] nums, int left, int right) {
        int temp = nums[left], l = left, r = right;
        while (l < r) {
            while (l < r && nums[r] <= temp) r--;
            while (l < r && nums[l] >= temp) l++;
            int t = nums[l];
            nums[l] = nums[r];
            nums[r] = t;
        }
        
        nums[left] = nums[l];
        nums[l] = temp;

        return l;
    }
}

// 优先队列（堆）
class Solution {
    public int findKthLargest(int[] nums, int k) {
        Queue<Integer> queue = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2 - o1;
            }
        });

        for (int i = 0; i < nums.length; i++) {
            queue.offer(nums[i]);
        }

        for (int i = 0; i < k; i++) {
            if (i == k - 1) {
                return queue.poll();
            }

            queue.poll();
        }

        return -1;
    }
}
```

#### 堆基本操作

```java
package lc;

import java.util.ArrayList;
import java.util.List;

public class HeapDemo {
    public static void main(String[] args) throws Exception{
        HeapDemo h = new HeapDemo();
        h.insert(300);
        h.insert(2);
        h.insert(10);
        h.insert(12);
        h.insert(112);
        h.insert(-1);

        for (int i = 0; i < 3; i++) {
            System.out.println(h.delete());
        }
    }

    public List<Integer> heap = new ArrayList<>();
    public int size = 0;

    public HeapDemo() {
        // 大顶堆，放最大的值当哨兵
        heap.add(Integer.MAX_VALUE);
    }

    // 先再最后放节点，然后下滤。 一直和新放入节点比较
    public void insert(int element) {
        heap.add(element);
        size++;
        int child = size;
        int parent = size / 2;
        while (heap.get(parent) < element) {
            heap.set(child, heap.get(parent));
            child = parent;
            parent = child / 2;
        }

        heap.set(child, element);
    }

    // 把最后一个节点替换掉堆顶，然后上滤。 一直和最后一个节点比较。
    public int delete() throws Exception {
        if (size < 0) {
            throw new Exception();
        }
        int ret = heap.get(1);
        int temp = heap.get(size);
        heap.set(1, temp);
//        heap.remove(size);
        size--;

        int parent = 1;
        while (parent * 2 <= size) {
            int child = parent * 2;
            if (child + 1 <= size && heap.get(child + 1) > heap.get(child)) {
                child += 1;
            }

            if (temp > heap.get(child)) {
                break;
            }

            heap.set(parent, heap.get(child));
            parent = child;
        }

        heap.set(parent, temp);
        heap.remove(heap.size() - 1);
//        int child = parent * 2;
//        if (child + 1 <= size && heap.get(child) < heap.get(child + 1)) {
//            child = child + 1;
//        }
//
//        while (child <= size && heap.get(child) > heap.get(parent)) {
//            heap.set(parent, heap.get(child));
//            parent = child;
//            child = parent * 2;
//            if (child + 1 <= size && heap.get(child) < heap.get(child + 1)) {
//                child = child + 1;
//            }
//        }

        return ret;
    }
}
```

#### [23. 合并K个升序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists/)

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

// 分治
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        int n = lists.length;
        return merge(lists, 0, n - 1);
    }

    public ListNode merge(ListNode[] lists, int l, int r) {
        if (l > r) {
            return null;
        }

        if (l == r) {
            return lists[l];
        }

        int mid = l + (r - r) / 2;
        return mergeTwoLists(merge(lists, l, mid), merge(lists, mid + 1, r));
    }

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null || l2 == null) {
            return l1 == null ? l2 : l1;
        }

        ListNode dummyHead = new ListNode(), tail = dummyHead;
        ListNode ptr1 = l1, ptr2 = l2;

        while (ptr1 != null && ptr2 != null) {
            if (ptr1.val < ptr2.val) {
                tail.next = ptr1;
                ptr1 = ptr1.next;
            }
            else {
                tail.next = ptr2;
                ptr2 = ptr2.next;
            }
            tail = tail.next;
        }

        if (ptr1 != null) {
            tail.next = ptr1;
        }

        if (ptr2 != null) {
            tail.next = ptr2;
        }

        return dummyHead.next;
    }
}

// 优先队列
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        Queue<ListNode> queue = new PriorityQueue<>(new Comparator<ListNode>() {
            @Override
            public int compare(ListNode o1, ListNode o2) {
                return o1.val - o2.val;
            }
        });

        for (ListNode head : lists) {
            if (head != null) {
                queue.offer(head);
            }
        }

        ListNode dummyHead = new ListNode(), tail = dummyHead;
        while (!queue.isEmpty()) {
            ListNode node = queue.poll();
            tail.next = node;
            tail = tail.next;
            if (node.next != null) {
                queue.offer(node.next);
            }
        }

        return dummyHead.next;
    }
}
```

#### [3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

```java
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> occ = new HashSet<Character>();
        int n = s.length();
        
        int right = 0, ans = 0;
        for (int left = 0; left < n; left++) {
            if (left != 0) {
                occ.remove(s.charAt(left - 1));
            }
            
            while (right < n && !occ.contains(s.charAt(right))) {
                occ.add(s.charAt(right));
                right++;
            }
            
            // [left, right)
            ans = Math.max(ans, right - left);
        }
        
        return ans;
    }
}
```

#### 全排列

```java
import javax.swing.*;
import java.util.*;

/*
当list中有重复数字时，不会产生重复的全排列
*/
public class Main4 {
    public static List<Integer> list = new LinkedList<>();
    public static Deque<Integer> combination = new LinkedList<>();
    public static List<List<Integer>> res = new ArrayList<>();
    public static int num;
    public static int n;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            list.add(sc.nextInt());
        }
        Collections.sort(list);
        dfs();
        System.out.println(num);
        for (List<Integer> l : res) {
            for (int i = 0; i < l.size(); i++) {
                System.out.print(l.get(i));
                if (i < l.size() - 1) {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }

    }

    public static void dfs() {
        if (list.isEmpty()) {
            num++;
            res.add(new ArrayList<>(combination));
            return;
        }

        for (int i = 0; i < list.size(); i++) {
            if (i != 0 && list.get(i) == list.get(i - 1)) {
                continue;
            }

            int temp = list.get(i);
            combination.offerLast(temp);
            list.remove(i);
            dfs();
            combination.pollLast();
            list.add(i, temp);
        }
    }
}
```

### O(logn)求因子

```java
package lc;

import java.util.ArrayList;
import java.util.List;

public class QuickFactor {
    public static void main(String[] args) {
        System.out.println(calculate(32));
    }

    public static List<Integer> calculate(int n) {
        List<Integer> list = new ArrayList<>();
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                list.add(i);
                if (n / i != i) {
                    list.add(n / i);
                }
            }
        }
        return list;
    }
}
```

### 单调栈 [496. 下一个更大元素 I](https://leetcode-cn.com/problems/next-greater-element-i/)

https://github.com/labuladong/fucking-algorithm/blob/master/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E7%B3%BB%E5%88%97/%E5%8D%95%E8%B0%83%E6%A0%88.md

```java
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int len1 = nums1.length;
        int len2 = nums2.length;

        Deque<Integer> stack = new ArrayDeque<>();
        Map<Integer, Integer> map = new HashMap<>();
        // 先处理 nums2，把对应关系存入哈希表
        for (int i = 0; i < len2; i++) {
            while (!stack.isEmpty() && stack.peekLast() < nums2[i]) {
                map.put(stack.removeLast(), nums2[i]);
            }
            stack.addLast(nums2[i]);
        }

        // 遍历 nums1 得到结果集
        int[] res = new int[len1];
        for (int i = 0; i < len1; i++) {
            res[i] = map.getOrDefault(nums1[i], -1);
        }
        return res;
    }
}
```

### 归并排序

```java
package lc;

import java.util.Arrays;

public class MergeSort {
    public static void main(String[] args) {
        MergeSort m = new MergeSort();
        int[] nums = {5,3,1,3,5,6,7};
        m.mergeSort(nums, 0, nums.length - 1);
        System.out.println(Arrays.toString(nums));
    }

    public void mergeSort(int[] nums, int left, int right) {
        if (left >= right) {
            return;
        }

        int mid = left + (right - left) / 2;
        mergeSort(nums, left, mid);
        mergeSort(nums, mid + 1, right);
        merge(nums, left, mid, right);
    }

    // [left, mid]
    // [mid + 1, right]
    public void merge(int[] nums, int left, int mid, int right) {
        int[] temp = new int[right - left + 1];
        int index = 0;

        int l = left, r = mid + 1;
        while (l <= mid && r <= right) {
            if (nums[l] <= nums[r]) {
                temp[index++] = nums[l];
                l++;
            }
            else {
                temp[index++] = nums[r];
                r++;
            }
        }

        while (l <= mid) {
            temp[index++] = nums[l];
            l++;
        }

        while (r <= right) {
            temp[index++] = nums[r];
            r++;
        }

        for (int i = left; i <= right; i++) {
            nums[i] = temp[i - left];
        }
    }
}
```

### 冒泡排序

```java
package lc;

import java.util.Arrays;

public class BubbleSort {
    public static void main(String[] args) {
        int[] nums = new int[]{3,1,2,5,1,2,5,6,3,2};
        bubbleSort(nums);
        System.out.println(Arrays.toString(nums));
    }

    public static void bubbleSort(int[] nums) {
        int n = nums.length;

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                if (nums[j] > nums[j + 1]) {
                    int temp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = temp;
                }
            }
        }
    }
}
```

### 冒泡排序链表，归并排序链表

```java
package lc;

public class ListSort {
    public static class ListNode {
        int val;
        ListNode next = null;
        public ListNode() {

        }
        public ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }

        @Override
        public String toString() {
            return "ListNode{" +
                    "val=" + val +
                    ", next=" + next +
                    '}';
        }
    }

    public static void main(String[] args) {
        ListNode l1 = new ListNode(3, null);
        ListNode l2 = new ListNode(4, l1);
        ListNode l3 = new ListNode(1, l2);
        ListNode l4 = new ListNode(6, l3);

//        ListNode head = bubbleSort(l4);
        ListNode head = mergeSort(l4);
        ListNode curNode = head;
        while (curNode != null) {
            System.out.println(curNode.val);
            curNode = curNode.next;
        }
    }


    /*
    如果发生交换，pre，cur，next的更新：
    dummyHead -> A -> B -> C -> D -> E
      pre      cur  next nextNext

    dummyHead -> B -> A -> C -> D -> E

      nextNext = next.next;
      pre.next = next;
      next.next = cur;
      cur.next = nextNext;

      pre = next;
      next = nextNext;
    */
    public static ListNode bubbleSort(ListNode head) {
        if (head == null) {
            return null;
        }

        ListNode dummyHead = new ListNode(0, head);
        ListNode tempNode = head;
        int n = 0;
        while (tempNode != null) {
            n++;
            tempNode = tempNode.next;
        }

        ListNode pre, cur, next, nextNext;
        for (int i = 0; i < n - 1; i++) {
            pre = dummyHead;
            cur = pre.next;
            next = cur.next;
            for (int j = 0; j < n - 1 - i; j++) {
                nextNext = next.next;
                if (cur.val > next.val) {
                    pre.next = next;
                    next.next = cur;
                    cur.next = nextNext;

                    pre = next;
                    next = nextNext;
                }
                else {
                    pre = cur;
                    cur = next;
                    next = nextNext;
                }
            }
        }

        return dummyHead.next;
    }

    // 确定中间节点
    //   A ->  B  -> C -> D
    // slow  fast
    //       slow       fast
    //            second
    public static ListNode split(ListNode head) {
        ListNode slow = head, fast = slow.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode retNode = slow.next;
        slow.next = null;
        return retNode;
    }

    public static ListNode mergeSort(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode head1 = head;
        ListNode head2 = split(head);
        return merge(mergeSort(head1), mergeSort(head2));
    }

    public static ListNode merge(ListNode head1, ListNode head2) {
        ListNode dummyHead = new ListNode(), tail = dummyHead;

        while (head1 != null && head2 != null) {
            if (head1.val <= head2.val) {
                tail.next = head1;
                head1 = head1.next;
            }
            else {
                tail.next = head2;
                head2 = head2.next;
            }
            tail = tail.next;
        }

        tail.next = head1 != null ? head1 : head2;
        return dummyHead.next;
    }
}
```

