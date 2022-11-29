using System;
using AdventOfCode.Common;

namespace AdventOfCode.Day05
{
    /// <summary>
    /// --- Day 5: Hydrothermal Venture ---
    /// 
    /// You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.
    /// 
    /// They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents(your puzzle input) for you to review.For example:
    /// 
    /// 0,9 -> 5,9
    /// 8,0 -> 0,8
    /// 9,4 -> 3,4
    /// 2,2 -> 2,1
    /// 7,0 -> 7,4
    /// 6,4 -> 2,0
    /// 0,9 -> 2,9
    /// 3,4 -> 1,4
    /// 0,0 -> 8,8
    /// 5,5 -> 8,2
    /// 
    /// Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2, y2 are the coordinates of the other end.
    /// These line segments include the points at both ends.In other words:
    /// 
    ///     An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
    ///     An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
    /// 
    /// For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.
    /// 
    /// So, the horizontal and vertical lines from the above list would produce the following diagram:
    /// 
    /// .......1..
    /// ..1....1..
    /// ..1....1..
    /// .......1..
    /// .112111211
    /// ..........
    /// ..........
    /// ..........
    /// ..........
    /// 222111....
    /// 
    /// In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or
    /// if no line covers that point.The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.
    /// 
    /// To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. 
    /// In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.
    /// 
    /// Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
    /// </summary>
    public static class Task1
    {
        public static int GetNumberOfOverlappingPoints()
        {
            var rawLines = CommonHelpers.ReadInstructions("Day05\\input.txt");
            var lines = rawLines.Select(ConvertRawLine).ToList();
            var pointCount = new Dictionary<(int x, int y), bool?>();
            FilterDiagonalLines(lines);

            foreach (var line in lines)
            {
                if (line.A.X == line.B.X) // Vertical lines
                {
                    Console.WriteLine("* Vertical");
                    var len = 0;
                    if (line.A.Y < line.B.Y) // A is before B
                    {
                        len = line.B.Y - line.A.Y + 1;
                        AddAllToPointCount(pointCount, len, line.A, Direction.VERTICAL);
                    }
                    else if (line.A.Y > line.B.Y) // B is before A
                    {
                        len = line.A.Y - line.B.Y + 1;
                        AddAllToPointCount(pointCount, len, line.B, Direction.VERTICAL);
                    }
                    else // If A == B
                    {
                        AddAllToPointCount(pointCount, len, line.A, Direction.VERTICAL);
                    }
                }
                else if (line.A.Y == line.B.Y) // Horizontal lines
                {
                    Console.WriteLine("* Horizontal");
                    var len = 0;
                    if (line.A.X < line.B.X) // A is before B
                    {
                        len = line.B.X - line.A.X + 1;
                        AddAllToPointCount(pointCount, len, line.A, Direction.HORIZONTAL);
                    }
                    else if (line.A.X > line.B.X) // B is before A
                    {
                        len = line.A.X - line.B.X + 1;
                        AddAllToPointCount(pointCount, len, line.B, Direction.HORIZONTAL);
                    }
                    else // If A == B
                    {
                        AddAllToPointCount(pointCount, len, line.A, Direction.HORIZONTAL);
                    }
                }
            }

            return GetOverlapAmount(pointCount);
        }

        public static int GetOverlapAmount(Dictionary<(int x, int y), bool?> pointCount)
        {
            return pointCount.Count(x => (bool) x.Value);
        }

        public static void AddAllToPointCount(Dictionary<(int x, int y), bool?> pointCount, int len, Coordinate start, Direction direction)
        {
            switch (direction)
            {
                case Direction.VERTICAL:
                    for (var i = 0; i < len; i++)
                    {
                        AddToPointCount(pointCount, new Coordinate { X = start.X, Y = start.Y + i });
                    }

                    break;
                case Direction.HORIZONTAL:
                    for (var i = 0; i < len; i++)
                    {
                        AddToPointCount(pointCount, new Coordinate { X = start.X + i, Y = start.Y });
                    }

                    break;
                case Direction.DIAGONAL_POS_Y:
                    for (var i = 0; i < len; i++)
                    {
                        AddToPointCount(pointCount, new Coordinate { X = start.X + i, Y = start.Y + i });
                    }
                    break;
                case Direction.DIAGONAL_NEG_Y:
                    for (var i = 0; i < len; i++)
                    {
                        AddToPointCount(pointCount, new Coordinate { X = start.X + i, Y = start.Y - i });
                    }
                    break;
            }
        }

        private static void AddToPointCount(Dictionary<(int x, int y), bool?> pointCount, Coordinate point)
        {
            var countedPoint = pointCount.FirstOrDefault(p => p.Key.x == point.X && p.Key.y == point.Y);

            if (countedPoint.Value == null) // First time for point
                pointCount.Add((point.X, point.Y), false);
            
            else if (countedPoint.Value == true) // Already intersected
                return;
            
            else // Registered once but not intersected until now
                pointCount[(countedPoint.Key.x, countedPoint.Key.y)] = true;
        }

        public static Line ConvertRawLine(string rawLine)
        {
            var coordinates = rawLine.Split(" -> ");
            return new Line
            {
                A = new Coordinate
                {
                    X = int.Parse(coordinates[0].Split(",")[0]),
                    Y = int.Parse(coordinates[0].Split(",")[1])
                },
                B = new Coordinate
                {
                    X = int.Parse(coordinates[1].Split(",")[0]),
                    Y = int.Parse(coordinates[1].Split(",")[1])
                }
            };
        }

        private static void FilterDiagonalLines(List<Line> lines)
        {
            lines.RemoveAll(l => l.A.X != l.B.X && l.A.Y != l.B.Y);
        }

        public struct Line
        {
            public Coordinate A { get; set; }
            public Coordinate B { get; set; }
        }

        public struct Coordinate
        {
            public int X { get; set; }
            public int Y { get; set; }
        }

        public enum Direction
        {
            HORIZONTAL,
            VERTICAL,
            DIAGONAL_POS_Y, // Growing Y
            DIAGONAL_NEG_Y // Shrinking Y
        }
    }
}
