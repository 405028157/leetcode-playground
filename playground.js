class Solutions {
    /**
     * 
     * @param work Array[]
     * @param gym Array[]
     */
    getDays(work, gym) {
        let n = work.length;
        
    }

    /**
     * 
     * @param A int升序数组
     * @param target 要找的值
     * 二分查找，有可能找不到
     */
    binarySearch(A, target) {
        let start = 0, end = A.length - 1;
        // 这里需要 start <= end，start === end，上一次循环，只能是 start = mid + 1 ，那时并没有查找到A[end]
        // 但是有个问题，如果start === end的时候，A[mid] < target, 那么下一步 end = mid, 会死循环
        while (start <= end) {
            mid = Math.floor((start + end) / 2);
            console.log('start, end' + start + ' ' + end);
            if (A[mid] > target) {
                end = mid;
            }
            else if (A[mid] < target) {
                start = mid + 1;
            }
            else {
                return mid;
            }
        }
        if (A[mid] === target) {
            return mid;
        }

        return -1;
    }
}