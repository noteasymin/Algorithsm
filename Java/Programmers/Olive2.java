import java.util.*;

class Solution {
    public int solution(String[] kor, String[] usa, String[] incs) {
        Set<String> korSet = new HashSet<>(Arrays.asList(kor)); // 한국 주식 종목 집합으로 변환
        Set<String> usaSet = new HashSet<>(Arrays.asList(usa)); // 미국 주식 종목 집합으로 변환

        int maxCount = 0; // 함께 상승한 날이 가장 많은 종목의 수
        for (String inc : incs) {
            String[] incArr = inc.split(" "); // 상승한 종목들을 공백을 기준으로 분리하여 배열로 변환
            Set<String> incSet = new HashSet<>(Arrays.asList(incArr)); // 상승한 종목 집합으로 변환

            int korCount = 0; // 한국 주식이 함께 상승한 종목의 수
            int usaCount = 0; // 미국 주식이 함께 상승한 종목의 수
            for (String incItem : incSet) {
                if (korSet.contains(incItem)) {
                    korCount++;
                }
                if (usaSet.contains(incItem)) {
                    usaCount++;
                }
            }

            if (korCount > 0 && usaCount > 0) { // 한국 주식과 미국 주식이 함께 상승한 종목이 있을 때
                int count = Math.min(korCount, usaCount); // 함께 상승한 종목 수 중에서 작은 값이 두 종목이 함께 상승한 날의 수
                if (count > maxCount) { // 최대값 갱신
                    maxCount = count;
                }
            }
        }
        return maxCount;
    }
}