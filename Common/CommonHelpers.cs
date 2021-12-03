namespace AdventOfCode.Common
{
    public static class CommonHelpers
    {
        public static List<string> ReadInstructions(string path)
        {
            return File.ReadAllLines($"{AppContext.BaseDirectory}\\..\\..\\..\\{path}").ToList();
        }
    }
}
