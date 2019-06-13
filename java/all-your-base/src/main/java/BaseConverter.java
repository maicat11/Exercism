import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class BaseConverter {
    private int baseTen = 0;

    BaseConverter(int inputBase, int[] digits) {

        if (inputBase < 2) {
            throw new IllegalArgumentException("Bases must be at least 2.");
        }

        int exp = 0;
        for (int i = digits.length - 1; i >= 0; --i) {
            if (digits[i] < 0) {
                throw new IllegalArgumentException("Digits may not be negative.");
            }
            if (digits[i] >= inputBase) {
                throw new IllegalArgumentException("All digits must be strictly less than the base.");
            }
            baseTen += (Math.pow(inputBase, exp) * digits[i]);
            exp++;
        }
    }

    int[] convertToBase(int outputBase) {

        if (outputBase < 2) {
            throw new IllegalArgumentException("Bases must be at least 2.");
        }

        if (baseTen == 0) {
            return new int[]{0};
        }
        List<Integer> convertDigits = new ArrayList<>();

        while (baseTen > 0) {
            convertDigits.add(baseTen % outputBase);
            baseTen /= outputBase;
        }
        Collections.reverse(convertDigits);

        int[] output = new int[convertDigits.size()];
        for(int i = 0; i < convertDigits.size(); i++) {
            output[i] = convertDigits.get(i);
        }
        return output;
    }
}
