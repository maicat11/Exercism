using System;
using System.Collections.Generic;
using System.Linq;

public enum Classification
{
    Perfect,
    Abundant,
    Deficient
}

public static class PerfectNumbers
{
    public static Classification Classify(int number)
    {
        if (number < 1) {
            throw new System.ArgumentOutOfRangeException("Not a natural number.");
        }

        List<int> factors = new List<int>();
        for (int i = 1; i < number; i++) {
            if (number % i == 0) {
                factors.Add(i);
            }
        }

        int aliquotSum = factors.Take(factors.Count()).Sum();

        return aliquotSum < number ? Classification.Deficient 
            : aliquotSum > number ? Classification.Abundant
            : Classification.Perfect;
    }
}


