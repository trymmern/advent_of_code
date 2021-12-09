using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using AdventOfCode.Common;

namespace AdventOfCode.Day05
{
    /// <summary>
    /// --- Part Two ---
    /// 
    /// Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.
    /// 
    /// Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees.In other words:
    /// 
    /// An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
    /// An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
    /// 
    /// Considering all lines from the above example would now produce the following diagram:
    /// 
    /// 1.1....11.
    /// .111...2..
    /// ..2.1.111.
    /// ...1.2.2..
    /// .112313211
    /// ...1.2....
    /// ..1...1...
    /// .1.....1..
    /// 1.......1.
    /// 222111....
    /// 
    /// You still need to determine the number of points where at least two lines overlap.In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.
    /// 
    /// Consider all of the lines.At how many points do at least two lines overlap?
    /// </summary>
    public static class Task2
    {
        public static int GetNumberOfOverlappingPoints()
        {
            var rawLines = CommonHelpers.ReadInstructions("Day05\\input.txt");
            var lines = rawLines.Select(Task1.ConvertRawLine).ToList();
            var pointCount = new Dictionary<(int x, int y), bool?>();

            foreach (var line in lines)
            {
                var len = 0;
                if (line.A.X == line.B.X) // Vertical lines
                {
                    Console.WriteLine("* Vertical");

                    if (line.A.Y < line.B.Y) // A is before B
                    {
                        len = line.B.Y - line.A.Y + 1;
                        Task1.AddAllToPointCount(pointCount, len, line.A, Task1.Direction.VERTICAL);
                    }
                    else if (line.A.Y > line.B.Y) // B is before A
                    {
                        len = line.A.Y - line.B.Y + 1;
                        Task1.AddAllToPointCount(pointCount, len, line.B, Task1.Direction.VERTICAL);
                    }
                    else // If A == B
                    {
                        Task1.AddAllToPointCount(pointCount, len, line.A, Task1.Direction.VERTICAL);
                    }
                }
                else if (line.A.Y == line.B.Y) // Horizontal lines
                {
                    Console.WriteLine("* Horizontal");
                    
                    if (line.A.X < line.B.X) // A is before B
                    {
                        len = line.B.X - line.A.X + 1;
                        Task1.AddAllToPointCount(pointCount, len, line.A, Task1.Direction.HORIZONTAL);
                    }
                    else if (line.A.X > line.B.X) // B is before A
                    {
                        len = line.A.X - line.B.X + 1;
                        Task1.AddAllToPointCount(pointCount, len, line.B, Task1.Direction.HORIZONTAL);
                    }
                    else // If A == B
                    {
                        Task1.AddAllToPointCount(pointCount, len, line.A, Task1.Direction.HORIZONTAL);
                    }
                }
                else // Diagonal 45deg lines
                {
                    if (line.A.X < line.B.X) // positive x
                    {
                        len = line.B.X - line.A.X + 1;
                        if (line.A.Y < line.B.Y) // positive y
                            Task1.AddAllToPointCount(pointCount, len, line.A, Task1.Direction.DIAGONAL_POS_Y);
                        else if (line.A.Y > line.B.Y) // negative y
                            Task1.AddAllToPointCount(pointCount, len, line.A, Task1.Direction.DIAGONAL_NEG_Y);
                    }
                    else // negative x
                    {
                        len = line.A.X - line.B.X + 1;
                        if (line.B.Y < line.A.Y) // positive y
                            Task1.AddAllToPointCount(pointCount, len, line.B, Task1.Direction.DIAGONAL_POS_Y);
                        else if (line.B.Y > line.A.Y) // negative y
                            Task1.AddAllToPointCount(pointCount, len, line.B, Task1.Direction.DIAGONAL_NEG_Y);
                    }
                }
            }

            return Task1.GetOverlapAmount(pointCount);
        }
    }
}
