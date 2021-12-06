namespace AdventOfCode.Common
{
    public static class CommonHelpers
    {
        public static List<string> ReadInstructions(string path)
        {
            return File.ReadAllLines($"{AppContext.BaseDirectory}\\..\\..\\..\\{path}").ToList();
        }

        public static List<int> ReadBingoNumbers(string path)
        {
            return File.ReadLines(path).Select(x => int.Parse(x)).ToList();
        }

        public static List<int[,]> GetBingoBoards(string path)
        {
            var counter = 0;
            var rowCount = 0;
            var boards = new List<int[,]>();
            var board = new int[,] { };
            foreach (string line in File.ReadLines($"{AppContext.BaseDirectory}\\..\\..\\..\\{path}"))
            {
                if (counter > 0)
                    continue;

                var row = line.Split(' ').Select(x => int.Parse(x)).ToArray();

                if (row.Length < 1)
                    continue;

                board[rowCount, ] = ;
                
                if (rows.Count == 5)
                {
                    boards.Add(new Board { Rows = rows});
                    rows.Clear();
                }

                counter++;
            }

            return boards;
        }

        public struct Board
        {
            public List<Row> Rows;
        }

        public struct Row
        {
            public List<{}> Numbers;
        }
    }
}
