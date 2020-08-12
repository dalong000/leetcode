class Solution {
    public int myAtoi(String str) {
        int i = 0, n = str.length();
        while (i < n && str.charAt(i) == ' ')
            i++;
        if (i == n)
            return 0;
        int flag = 1;
        if (str.charAt(i) == '+' || str.charAt(i) == '-') {
            if (str.charAt(i) == '-')
                flag = -1;
            i++;
        }
        int num = 0;
        while (i < n && Character.isDigit(str.charAt(i))) {
            int temp = str.charAt(i) - '0';
            if (flag == 1 && (num > 214748364 || (num == 214748364 && temp > 7 )))
                return Integer.MAX_VALUE ;
            if (flag == -1 && (num > 214748364 || (num == 214748364 && temp > 8)))
                return Integer.MIN_VALUE;
            num = num * 10 + temp;
            i++;
        }
        return num * flag;
    }
}