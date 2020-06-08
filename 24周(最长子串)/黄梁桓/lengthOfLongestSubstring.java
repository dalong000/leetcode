class Solution {
    public int lengthOfLongestSubstring(String s) {
        int right = 0,max = 0;
		HashSet<Character> set = new HashSet<Character>();
		for (int i = 0; i < s.length(); i++) {
			if (i == 0) {
				set.add(s.charAt(i));
			} else {
				set.remove(s.charAt(i-1));
			}
			
			while ((right + 1) < s.length() && !set.contains(s.charAt(right+1))) {
				set.add(s.charAt(right+1));
				right++;
			}
			
			max = max > (right-i+1) ? max : right-i+1;
		}
		return max;
    }
}