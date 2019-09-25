using System;
using System.Linq;

public static class Pangram
{
    private static String alphabet = "abcdefghijklmnopqrstuvwxyz";
    public static bool IsPangram(string input)
    {
        foreach(char c in alphabet) {
            if (!input.ToLower().Contains(c)) {
                return false;
            }
        }
        return true; 
    }
}

