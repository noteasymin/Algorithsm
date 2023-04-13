import java.util.*;

class Solution {
    public int[] solution(String[][] folders, String[][] files, String[] selected, String[] excepted) {
        int[] answer = new int[2];
        Set<String> exceptedSet = new HashSet<>(Arrays.asList(excepted));

        // 하위 폴더 정보를 상위 폴더에 저장하는 Map 생성
        Map<String, List<String>> folderMap = new HashMap<>();
        for (String[] folder : folders) {
            String child = folder[0];
            String parent = folder[1];
            folderMap.computeIfAbsent(parent, k -> new ArrayList<>()).add(child);
        }

        // 검사 대상 파일 크기와 개수 계산
        for (String folder : selected) {
            calculate(folder, folderMap, files, exceptedSet, answer);
        }

        return answer;
    }

    private void calculate(String folder, Map<String, List<String>> folderMap, String[][] files,
                           Set<String> exceptedSet, int[] answer) {
        List<String> subFolders = folderMap.get(folder);
        if (subFolders == null) { // 하위 폴더가 없는 경우
            for (String[] file : files) {
                if (!exceptedSet.contains(file[0]) && file[2].equals(folder)) { // 제외할 파일이 아니고 검사 대상인 파일인 경우
                    String sizeString = file[1];
                    int size;
                    if (sizeString.endsWith("KB")) { // KB 단위의 경우
                        sizeString = sizeString.substring(0, sizeString.length() - 2); // "KB"를 제거
                        size = Integer.parseInt(sizeString) * 1024; // KB를 B로 변환하여 계산
                    } else { // B 단위의 경우
                        sizeString = sizeString.substring(0, sizeString.length() - 1); // "B"를 제거
                        size = Integer.parseInt(sizeString);
                    }
                    answer[0] += size; // 파일 크기 추가
                    answer[1]++; // 파일 개수 추가
                }
            }
        } else { // 하위 폴더가 있는 경우
            for (String subFolder : subFolders) {
                calculate(subFolder, folderMap, files, exceptedSet, answer); // 하위 폴더에서 계산
            }
        }
    }
}