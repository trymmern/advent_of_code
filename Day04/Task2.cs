using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using AdventOfCode.Common;

namespace AdventOfCode.Day04
{
    /// <summary>
    /// --- Part Two ---
    /// 
    /// On the other hand, it might be wise to try a different strategy: let the giant squid win.
    ///
    /// You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms,
    /// the safe thing to do is to figure out which board will win last and choose that one.
    /// That way, no matter which boards it picks, it will win for sure.
    ///
    /// In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked.
    /// If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.
    ///
    /// Figure out which board will win last. Once it wins, what would its final score be?
    ///
    /// </summary>
    public static class Task2
    {
        public static int GetFinalScoreOfLastWinningBoard()
        {
            var inputs = CommonHelpers.ReadBingoNumbers("Day04\\input.txt");
            var boards = CommonHelpers.GetBingoBoards("Day04\\input.txt");
            var winningNum = 0;
            var winningBoards = new List<CommonHelpers.ExpandedInt[,]>();
            CommonHelpers.ExpandedInt[,]? lastWinningBoard = null;

            foreach (var input in inputs)
            {
                foreach (var board in boards)
                {
                    if (winningBoards.Any(b => b == board))
                        continue;

                    for (var i = 0; i < board.GetLength(0); i++)
                    {
                        for (var j = 0; j < board.GetLength(1); j++)
                        {
                            Console.Write($"{board[i, j].num.ToString(), 2} ");

                            if (board[i, j].num == 48 && input == 48)
                            {
                                Console.WriteLine("test");
                            }

                            if (board[i, j].num == input)
                            {
                                board[i, j].marked = true;
                            }
                        }
                        Console.WriteLine("\n");
                    }

                    if (Task1.IsWinningBoard(board))
                    {
                        lastWinningBoard = board;
                        winningNum = input;
                        winningBoards.Add(board);
                    }

                    Console.WriteLine("\n\n");
                }
            }

            return lastWinningBoard != null ? Task1.CalculateFinalScore(lastWinningBoard, winningNum) : 0;
        }
    }
}
