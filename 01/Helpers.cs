using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode._01
{
    public static class Helpers
    {
        public static List<string> ReadFile()
        {
            return File.ReadAllLines("C:\\dev\\AdventOfCode\\01\\input.txt").ToList();
        }
    }
}
