﻿namespace AdventOfCode
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Choose day to run (add flag '-a' to run both tasks for that day): ");
            var day = Console.ReadLine();
            string? task;

            switch (day)
            {
                case "1":
                    Console.WriteLine("Choose task (type '1' or '2')");
                    task = Console.ReadLine();
                    if (task == "1")
                        Console.WriteLine($"Result: {Day01.Task1.GetIncreasedDepthCount()} \n\n");
                    if (task == "2") 
                        Console.WriteLine($"Result: {Day01.Task2.GetIncreasedDepthValueAmountX3()} \n\n");
                    break;
                case "1 -a":
                    Console.WriteLine($"Result: {Day01.Task1.GetIncreasedDepthCount()} \n\n");
                    Console.WriteLine($"Result: {Day01.Task2.GetIncreasedDepthValueAmountX3()} \n\n");
                    break;
                case "2":
                    Console.WriteLine("Choose task (type '1' or '2')");
                    task = Console.ReadLine();
                    if (task == "1")
                        Console.WriteLine($"Result: {Day02.Task1.GetFinalPosition()} \n\n");
                    if (task == "2")
                        Console.WriteLine($"Result: {Day02.Task2.GetFinalPosition()} \n\n");
                    break;
                case "2 -a":
                    Console.WriteLine($"Result: {Day02.Task1.GetFinalPosition()} \n\n");
                    Console.WriteLine($"Result: {Day02.Task2.GetFinalPosition()} \n\n");
                    break;
                case "3":
                    Console.WriteLine("Choose task (type '1' or '2')");
                    task = Console.ReadLine();
                    if (task == "1")
                        Console.WriteLine($"Result: {Day03.Task1.GetPowerConsumption()} \n\n");
                    if (task == "2")
                        Console.WriteLine($"Result: {Day03.Task2.GetLifeSupportRating()} \n\n");
                    break;
                case "3 -a":
                    Console.WriteLine($"Result: {Day03.Task1.GetPowerConsumption()} \n\n");
                    Console.WriteLine($"Result: {Day03.Task2.GetLifeSupportRating()} \n\n");
                    break;
                default:
                    throw new InvalidOperationException("Not a valid input");
            }
        }
    }
}