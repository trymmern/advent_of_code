namespace AdventOfCode.Common
{
    public static class CommonHelpers
    {
        public static List<string> ReadInstructions(string path)
        {
            return File.ReadAllLines($"{AppContext.BaseDirectory}..\\..\\..\\{path}").ToList();
        }

        public static List<int> ReadBingoNumbers(string path)
        {
            var numbers = File.ReadAllLines($"{AppContext.BaseDirectory}..\\..\\..\\{path}").Skip(0).Take(1).First();
            return numbers.Split(',').Select(int.Parse).ToList();
        }

        public static List<ExpandedInt[,]> GetBingoBoards(string path)
        {
            var rowCount = 0;
            var boards = new List<ExpandedInt[,]>();
            var board = new ExpandedInt[5,5];
            foreach (var line in File.ReadAllLines($"{AppContext.BaseDirectory}..\\..\\..\\{path}").Skip(2))
            {
                var row = line.Split(' ', StringSplitOptions.RemoveEmptyEntries).Select(int.Parse).ToArray();

                if (row.Length < 1)
                    continue;

                AddRowToBoard(board, row, rowCount);

                if (board[4,4].num != 0)
                {
                    rowCount = 0;
                    boards.Add(board);
                    board = new ExpandedInt[5,5];
                }
                rowCount++;
            }

            return boards;
        }

        private static void AddRowToBoard(ExpandedInt[,] board, int[] row, int rowNum)
        {
            for (var i = 0; i < row.Length; i++)
            {
                board[rowNum, i].num = row[i];
            }
        }

        public struct ExpandedInt
        {
            public int num;
            public bool marked = false;
        }
    }
}
