using System;

public static class CollatzConjecture
{
    public static int Steps(int number)
    {
        int result = number;
        int count = 0;

        if (number < 1) {
            throw new ArgumentException("Number must exceed zero.");
        }

        while (result > 1) {
            if (result % 2 == 0) {
                result = result / 2;
            }
            else {
                result = 3 * result + 1;
            }
            count++;
        }

        return count;
    }
}