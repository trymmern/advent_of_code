using System;
using AdventOfCode.Common;

namespace AdventOfCode.Day05
{
    public static class Task1
    {
        public static int GetNumberOfOverlappingPoints()
        {
            var rawLines = CommonHelpers.ReadInstructions("Day05\\input.txt");
            var lines = rawLines.Select(ConvertRawLine).ToList();
            var pointCount = new List<PointCount>();
            FilterDiagonalLines(lines);

            foreach (var line in lines)
            {
                if (line.A.X == line.B.X)
                {
                    var len = 0;
                    if (line.A.Y < line.B.Y) // A is before B
                    {
                        len = line.B.Y - line.A.Y;

                        for (var i = 0; i < len; i++)
                        {
                            AddToPointCount(pointCount, new Coordinate { X = line.A.X, Y = line.A.Y + i });
                        }
                    }
                    else if (line.A.Y > line.B.Y) // B is before A
                    {
                        len = line.A.Y - line.B.Y;
                    }
                    else // If A == B
                    {
                        AddToPointCount(pointCount, new Coordinate { X = line.A.X, Y = line.A.Y });
                    }
                    
                }
                else if (line.A.Y == line.B.Y)
                {

                }
            }
        }

        private static Line ConvertRawLine(string rawLine)
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

        private static void AddToPointCount(List<PointCount> pointCount, Coordinate point)
        {
            var countedPoint = pointCount.FirstOrDefault(p => p.Coordinate.Equals(point));
            if (countedPoint.Count == 0) // Default
            {
                pointCount.Add(new PointCount
                {
                    Coordinate = point,
                    Count = 1
                });
            }
            else
            {
                countedPoint.Count++;
            }
        }


        public struct Line
        {
            public Coordinate A { get; set; }
            public Coordinate B { get; set; }
        }

        public struct PointCount
        {
            public Coordinate Coordinate { get; set; }
            public int Count { get; set; }
        }

        public struct Coordinate
        {
            public int X { get; set; }
            public int Y { get; set; }
        }
    }
}
