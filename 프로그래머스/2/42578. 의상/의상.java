import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 0;
        HashMap<String,List<String>> clothesMap = new HashMap<>();
        for (String[] clothe : clothes) {
            if (clothesMap.containsKey(clothe[1])) {
                clothesMap.get(clothe[1]).add(clothe[0]);
            } else {
                clothesMap.put(clothe[1], new ArrayList(Arrays.asList(clothe[0])));
            }
        }
        return calculateCombinations(clothesMap);
    }
    
    public static int calculateCombinations(Map<String, List<String>> clothesMap) {
    int totalCombinations = 1;
    for (List<String> clothesList : clothesMap.values()) {
        totalCombinations *= (clothesList.size() + 1); // 아무것도 선택하지 않는 경우 포함
    }
    return totalCombinations - 1; // 모든 것을 선택하지 않는 경우 제외
}
}