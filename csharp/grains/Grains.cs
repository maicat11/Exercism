using System;

public static class Grains
{
    public static ulong Square(int n)
    {
        if (n <= 0 || n > 64)
        {
            throw new System.ArgumentOutOfRangeException("Out of Range");
        }
        return (ulong)Math.Pow(2.0, n-1);
    }

    public static ulong Total()
    {
        ulong total = 0;
        for (int i = 0; i < 64; i++)
        {
            total += (ulong)Math.Pow(2, i);
        }
        return total;
    }
}