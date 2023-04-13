import java.util.*;

class Solution {
    public int solution(String number) {
        int count = 0;
        String temp = "";

        for (int i = 0; i < number.length(); i++) {
            char c = number.charAt(i);
            if (c == '0') {
                temp += "0";
                continue;
            }
            while (i < number.length() && number.charAt(i) == c) {
                temp += c;
                i++;
            }
            i--;
        }

        for (int i = 0; i < temp.length(); i++) {
            count += Math.min(temp.charAt(i) - '0', 10 - (temp.charAt(i) - '0'));
        }

        return count;
    }
}
