using System;
using System.Collections.Generic;

public static class ResistorColor
{
    private static String[] color_map = new String[] {"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};

    public static int ColorCode(string color)
    {
        return Array.IndexOf(color_map, color);
    }
    public static string[] Colors()
    {
        return color_map;
    }
}

// String[] stringarr = new String[] {"Geeks", "GFG", "Noida"};