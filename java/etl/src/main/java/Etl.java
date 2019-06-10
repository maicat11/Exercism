import java.util.*;

class Etl {
    // transform method
    Map<String, Integer> transform(Map<Integer, List<String>> old) {
        Map<String, Integer> newMap = new HashMap();

        for (Map.Entry<Integer, List<String>> entry : old.entrySet()) {
            for (String letter : entry.getValue()) {
                newMap.put(letter.toLowerCase(), entry.getKey());
            }
        }
        return newMap;
    }
}