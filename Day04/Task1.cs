using AdventOfCode.Common;

namespace AdventOfCode.Day04
{
    /// <summary>
    /// --- Day 4: Giant Squid ---
    /// 
    /// You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight.
    /// What you can see, however, is a giant squid that has attached itself to the outside of your submarine.
    /// 
    /// Maybe it wants to play bingo?
    /// 
    /// Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. 
    /// (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)
    /// 
    /// The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time.
    /// It automatically generates a random order in which to draw numbers and a random set of boards(your puzzle input). For example:
    /// 
    /// 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
    /// 
    /// 22 13 17 11  0
    ///  8  2 23  4 24
    /// 21  9 14 16  7
    ///  6 10  3 18  5
    ///  1 12 20 15 19
    /// 
    ///  3 15  0  2 22
    ///  9 18 13 17  5
    /// 19  8  7 25 23
    /// 20 11 10 24  4
    /// 14 21 16 12  6
    /// 
    /// 14 21 17 24  4
    /// 10 16 15  9 19
    /// 18  8 23 26 20
    /// 22 11 13  6  5
    ///  2  0 12  3  7
    /// 
    /// After the first five numbers are drawn(7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows(shown here adjacent to each other to save space) :
    /// 
    /// 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
    ///  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
    /// 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
    ///  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
    ///  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
    /// 
    /// After the next six numbers are drawn(17, 23, 2, 0, 14, and 21), there are still no winners:
    /// 
    /// 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
    ///  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
    /// 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
    ///  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
    ///  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
    /// 
    /// Finally, 24 is drawn:
    /// 
    /// 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
    ///  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
    /// 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
    ///  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
    ///  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
    /// 
    /// At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).
    /// 
    /// The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. 
    /// Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.
    /// 
    /// To guarantee victory against the giant squid, figure out which board will win first.What will your final score be if you choose that board ?
    /// </summary>
    public static class Task1
    {
        public static int GetFinalBingoScore()
        {
            var inputs = CommonHelpers.ReadBingoNumbers("Day04\\input.txt");
            var boards = CommonHelpers.GetBingoBoards("Day04\\input.txt");
            CommonHelpers.ExpandedInt[,]? winningBoard = null;
            var currentNum = inputs[0];

            foreach (var input in inputs)
            {
                currentNum = input;

                foreach (var board in boards)
                {
                    for (var i = 0; i < board.GetLength(0); i++)
                    {
                        for (var j = 0; j < board.GetLength(1); j++)
                        {
                            if (board[i, j].num == input && !board[i, j].marked)
                            {
                                board[i, j].marked = true;
                            }
                        }
                    }

                    if (CheckHorizontals(board) || CheckVerticals(board))
                    {
                        winningBoard = board;
                        break;
                    }
                }

                if (winningBoard != null) break;
            }

            if (winningBoard != null)
                return CalculateFinalScore(winningBoard, currentNum);
            else
                return 0;
        }

        private static bool CheckHorizontals(CommonHelpers.ExpandedInt[,] board)
        {
            var isFullRow = false;
            for (var i = 0; i < board.GetLength(0); i++)
            {
                var row = GetRow(board, i);

                if (row.All(x => x.marked))
                {
                    Console.WriteLine($"We have a winner row:");
                    row.ToList().ForEach(n => Console.WriteLine(n.num));
                    isFullRow = true;
                    break;
                }
            }

            return isFullRow;
        }

        private static bool CheckVerticals(CommonHelpers.ExpandedInt[,] board)
        {
            var isFullColumn = false;
            for (var i = 0; i < board.GetLength(1); i++)
            {
                var column = GetColumn(board, i);

                if (column.All(x => x.marked))
                {
                    Console.WriteLine($"We have a winner column:");
                    column.ToList().ForEach(n => Console.WriteLine(n.num));
                    isFullColumn = true;
                    break;
                }
            }

            return isFullColumn;
        }

        public static CommonHelpers.ExpandedInt[] GetColumn(CommonHelpers.ExpandedInt[,] matrix, int columnNumber)
        {
            return Enumerable.Range(0, matrix.GetLength(0))
                    .Select(x => matrix[x, columnNumber])
                    .ToArray();
        }

        public static CommonHelpers.ExpandedInt[] GetRow(CommonHelpers.ExpandedInt[,] matrix, int rowNumber)
        {
            return Enumerable.Range(0, matrix.GetLength(1))
                    .Select(x => matrix[rowNumber, x])
                    .ToArray();
        }

        private static int CalculateFinalScore(CommonHelpers.ExpandedInt[,] board, int currentNum)
        {
            var sumOfUnmarked = 0;

            foreach (var elem in board)
            {
                if (!elem.marked) 
                    sumOfUnmarked += elem.num;
            }

            return sumOfUnmarked * currentNum;
        }
    }
}
