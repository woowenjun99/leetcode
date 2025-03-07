#include <vector>

void merge(std::vector<int> &nums, int low, int mid, int high) {
    int n = high - low + 1;
    std::vector<int> util{n};
    int left = low, right = mid + 1, bIdx = 0;
    while (left <= mid and right <= high) {
        if (nums[left] <= nums[right]) util[bIdx++] = nums[left++];
        else util[bIdx++] = nums[right++];
    }
    while (left <= mid) util[bIdx++] = nums[left++];
    while (right <= high) util[bIdx++] = nums[right++];
    for (int k = 0; k < n; ++k) nums[low + k] = util[k];
}

void merge_sort(std::vector<int> &nums, int low, int high) {
    if (low >= high) return;
    int mid = (low + high) / 2;
    merge_sort(nums, low, mid);
    merge_sort(nums, mid + 1, high);
    merge(nums, low, mid, high);
}