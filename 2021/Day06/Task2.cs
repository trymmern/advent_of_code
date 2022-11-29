using System;
using System.Collections.Specialized;
using AdventOfCode.Common;

namespace AdventOfCode.Day06
{
    /// <summary>
    /// --- Part Two ---
    /// 
    /// Suppose the lanternfish live forever and have unlimited food and space.
    /// Would they take over the entire ocean?
    /// 
    /// After 256 days in the example above, there would be a total of 26984457539 lanternfish!
    /// 
    /// How many lanternfish would there be after 256 days?
    /// </summary>
    public static class Task2
    {
        public static long GetLanternfishPopulation(int days)
        {
            var pop0 = CommonHelpers.ReadInstructions("Day06\\input.txt")[0].Split(',').Select(int.Parse).ToList();
            
            Console.WriteLine("\nInitial state: ");
            pop0.ForEach(f => Console.Write($"{f}, "));
            
            var pop = GroupPopulation(pop0);
            
            Console.WriteLine("\n\nInitial ordered state: ");
            foreach (var amountOfAge in pop)
            {
                Console.WriteLine($"Days: {pop.IndexOf(amountOfAge)} Amount: {amountOfAge}");
            }

            for (var i = 0; i < days; i++)
            {
                IterateDayAndSpawnFish(pop, out pop);

                Console.WriteLine($"\nAfter day {(i+1).ToString().PadLeft(2, '0')}: ");
                foreach (var amountOfAge in pop)
                {
                    Console.WriteLine($"Days: {pop.IndexOf(amountOfAge)} Amount: {amountOfAge}");
                }
            }

            return GetFinalPopulation(pop);
        }

        private static long GetFinalPopulation(List<long> pop)
        {
            return pop.Sum(i => i);
        }

        private static void IterateDayAndSpawnFish(List<long> pop, out List<long> newPop)
        {
            newPop = new List<long> { 0, 0, 0, 0, 0, 0, 0, 0, 0 };
            for (var i = 0; i < pop.Count; i++)
            {
                if (i == 0) // zero days until reproduction
                {
                    newPop[8] += pop[i]; // New spawns
                    newPop[6] += pop[i]; // Parents reset to 6 days
                }
                else
                { 
                    newPop[i - 1] += pop[i];
                }
            }
        }

        private static List<long> GroupPopulation(List<int> pop0)
        {
            var pop = new List<long> { 0, 0, 0, 0, 0, 0, 0, 0, 0 };
            foreach (var t in pop0)
            {
                pop[t]++;
            }

            return pop;
        }
    }
}
