using System;
using System.Collections.Generic;

public static class ResistorColor
{
    private static String[] colorMap = new String[] {"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};

    public static int ColorCode(string color)
    {
        return Array.IndexOf(colorMap, color);
    }
    public static string[] Colors()
    {
        return colorMap;
    }
}

