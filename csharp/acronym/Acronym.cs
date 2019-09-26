using System;

public static class Acronym
{
    public static string Abbreviate(string phrase)
    {
        string acronym = "";
        phrase = phrase.Replace("-", " ").Replace("_", " ");
        string[] words = phrase.Split(' ', StringSplitOptions.RemoveEmptyEntries);

        foreach (var word in words) 
        {
            acronym += word.ToUpper()[0];
        }
        return acronym;
    }
}

