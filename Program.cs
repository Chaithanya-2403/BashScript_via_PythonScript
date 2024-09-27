using System;

public class Program
{
    static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.WriteLine("No arguments provided.");
            return;
        }

        Console.WriteLine("Arguments received:");

        foreach (string arg in args)
        {
            Console.WriteLine(arg);
        }
    }
}