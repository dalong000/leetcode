class Solution {
    public int reverse(int x) {
        long x2 = (long)x;
        long res = 0,ret = 0;
        while (x2!=0) {
            res = x2 % 10;
             x2 = x2/10;
             ret = ret*10 + res;
             if (ret > 2147483647 || ret < -2147483648) {
                    return 0;
                }
        }
        return (int)ret;
    }
}