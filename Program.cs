namespace AdventOfCode
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
                case "2":
                    Console.WriteLine("Choose task (type '1' or '2')");
                    task = Console.ReadLine();
                    if (task == "1")
                        Console.WriteLine($"\nResult: {Day02.Task1.GetFinalPosition()} \n\n");
                    if (task == "2")
                        Console.WriteLine($"\nResult: {Day02.Task2.GetFinalPosition()} \n\n");
                    break;
                case "3":
                    Console.WriteLine("Choose task (type '1' or '2')");
                    task = Console.ReadLine();
                    if (task == "1")
                        Console.WriteLine($"\nResult: {Day03.Task1.GetPowerConsumption()} \n\n");
                    if (task == "2")
                        Console.WriteLine($"\nResult: {Day03.Task2.GetLifeSupportRating()} \n\n");
                    break;
                case "4":
                    Console.WriteLine("Choose task (type '1' or '2')");
                    task = Console.ReadLine();
                    if (task == "1")
                        Console.WriteLine($"\nResult: {Day04.Task1.GetFinalBingoScore()} \n\n");
                    if (task == "2")
                        Console.WriteLine($"\nResult: {Day04.Task2.GetFinalScoreOfLastWinningBoard()} \n\n");
                    break;
                case "5":
                    Console.WriteLine("Choose task (type '1' or '2')");
                    task = Console.ReadLine();
                    if (task == "1")
                        Console.WriteLine($"\nResult: {Day05.Task1.GetNumberOfOverlappingPoints()} \n\n");
                    if (task == "2")
                        Console.WriteLine($"\nResult: {Day05.Task2.GetNumberOfOverlappingPoints()} \n\n");
                    break;
                case "6":
                    Console.WriteLine("Choose task (type '1' or '2')");
                    task = Console.ReadLine();
                    if (task == "1")
                        Console.WriteLine($"\nResult: {Day06.Task1.GetLanternfishPopulation(80)} \n\n");
                    if (task == "2")
                        Console.WriteLine($"\nResult: {Day06.Task2.GetLanternfishPopulation(256)} \n\n");
                    break;
                case "7":
                    Console.WriteLine("Choose task (type '1' or '2')");
                    task = Console.ReadLine();
                    if (task == "1")
                        Console.WriteLine($"\nResult: {Day07.Task1.GetFuelConsumption()} \n\n");
                    if (task == "2")
                        Console.WriteLine($"\nResult: {Day07.Task2.GetFuelConsumption()} \n\n");
                    break;
                default:
                    throw new InvalidOperationException("Not a valid input");
            }
        }
    }
}