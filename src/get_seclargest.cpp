#include <iostream>
#include <vector>
#include <climits>

int secondLargest(const std::vector<int>& arr) {
    int largest = INT_MIN;
    int second = INT_MIN;

    for (int num : arr) {
        if (num > largest) {
            second = largest;
            largest = num;
        } else if (num > second && num != largest) {
            second = num;
        }
    }

    return second == INT_MIN ? -1 : second;
}

int main() {
    int n;
    std::cin >> n;

    std::vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }

    std::cout << secondLargest(arr);
    return 0;
}