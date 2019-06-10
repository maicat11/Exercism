import java.util.HashMap;
import java.util.Map;

class Scrabble {
    private String word;

    static Map<String, Integer> letterValues = new HashMap<String, Integer>();
    static {
        String[] letters = {"AEIOULNRST", "DG", "BCMP", "FHVWY", "K", "JX", "QZ"};
        int[] values = {1, 2, 3, 4, 5, 8, 10};
        for (int i = 0; i < letters.length; i++) {
            for (String letter : letters[i].split("")){
                letterValues.put(letter, values[i]);
            }
        }
    }

    Scrabble(String word) {
        this.word = word;
    }

    int getScore() {
        int wordScore = 0;
        if (!word.equals("")) {
            for(String letter : word.split("")) {
                wordScore += letterValues.get(letter.toUpperCase());
            }
        }
        return wordScore;
    }
}
