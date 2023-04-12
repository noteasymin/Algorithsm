class Solution {
    public int solution(int[] common) {
        int n = common.length;
        int nextNumber = 0;
        if (n > 2) {
            // 등차수열인 경우
            if (common[1] - common[0] == common[2] - common[1]) {
                int d = common[1] - common[0];
                nextNumber = common[n-1] + d;
            }
            // 등비수열인 경우
            else if (common[1] / common[0] == common[2] / common[1]) {
                int r = common[1] / common[0];
                nextNumber = common[n-1] * r;
            }
        }
        return nextNumber;
    }
}