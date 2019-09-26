using System;

public class SpaceAge
{
    private static double earthTime;
    public SpaceAge(int seconds)
    {
        earthTime = seconds / 31557600.0;
    }

    public double OnEarth()
    {
        return Math.Round(earthTime, 2);
    }

    public double OnMercury()
    {
        return Math.Round(earthTime / 0.2408467, 2);
    }

    public double OnVenus()
    {
        return Math.Round(earthTime / 0.61519726, 2);
    }

    public double OnMars()
    {
        return Math.Round(earthTime / 1.8808158, 2);
    }

    public double OnJupiter()
    {
        return Math.Round(earthTime / 11.862615, 2);
    }

    public double OnSaturn()
    {
        return Math.Round(earthTime / 29.447498, 2);
    }

    public double OnUranus()
    {
        return Math.Round(earthTime / 84.016846, 2);
    }

    public double OnNeptune()
    {
        return Math.Round(earthTime / 164.79132, 2);
    }
}