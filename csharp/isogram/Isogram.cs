using System;
using System.Text.RegularExpressions;
using System.Collections.Generic;

public static class Isogram
{
    public static bool IsIsogram(string word)
    {
        Regex rgx = new Regex("[^a-zA-Z]");
        word = rgx.Replace(word, "").ToLower();
        
        HashSet<char> charSet = new HashSet<char>();
        foreach(char c in word) {
            if (charSet.Contains(c)) {
                return false;
            }
            charSet.Add(c);
        }
        return true;
    }
}

