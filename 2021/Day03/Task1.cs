using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using AdventOfCode.Common;

namespace AdventOfCode.Day03
{
    /// <summary>
    /// --- Day 3: Binary Diagnostic ---
    /// 
    /// The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.
    ///
    /// The diagnostic report(your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine.
    /// The first parameter to check is the power consumption.
    ///
    /// You need to use the binary numbers in the diagnostic report to generate two new binary numbers(called the gamma rate and the epsilon rate).
    /// The power consumption can then be found by multiplying the gamma rate by the epsilon rate.
    ///
    /// Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report.For example, given the following diagnostic report:
    ///
    /// 00100
    /// 11110
    /// 10110
    /// 10111
    /// 10101
    /// 01111
    /// 00111
    /// 11100
    /// 10000
    /// 11001
    /// 00010
    /// 01010
    /// 
    /// 
    /// Considering only the first bit of each number, there are five 0 bits and seven 1 bits.Since the most common bit is 1, the first bit of the gamma rate is 1.
    /// 
    /// 
    /// The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.
    /// 
    /// 
    /// The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.
    /// 
    /// 
    /// So, the gamma rate is the binary number 10110, or 22 in decimal.
    /// 
    /// 
    /// The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used.
    /// So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate(22) by the epsilon rate(9) produces the power consumption, 198.
    /// 
    /// Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together.
    /// What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)
    /// </summary>
    public static class Task1
    {
        public static int GetPowerConsumption()
        {
            const int bits = 12;
            var binaryValues = CommonHelpers.ReadInstructions("Day03\\input.txt");
            var gammaBinary = "";
            var epsilonBinary = "";

            for (var b = 0; b < bits; b++)
            {
                Console.WriteLine($"\nChecking most common value for bit {b}");

                var mostCommonBitAtIndex = GetMostOrLeastCommonBitValueAtIndex(binaryValues, b);

                

                if (mostCommonBitAtIndex == "0")
                {
                    gammaBinary += "0";
                    epsilonBinary += "1";
                }
                else if (mostCommonBitAtIndex == "1")
                {
                    gammaBinary += "1";
                    epsilonBinary += "0";
                }
                else
                {
                    Console.WriteLine($"Most common value for bit {b} could not be found as they are equally present");
                }
            }

            Console.WriteLine($"\n\nGamma binary: {gammaBinary}\nEpsilon binary: {epsilonBinary}");

            var gamma = Convert.ToInt32(gammaBinary, 2);
            var epsilon = Convert.ToInt32(epsilonBinary, 2);

            Console.WriteLine($"\n\nGamma decimal: {gamma}\nEpsilon decimal: {epsilon}");

            return gamma * epsilon;
        }

        public static string GetMostOrLeastCommonBitValueAtIndex(List<string> values, int bitIndex, bool getMostCommon = true, PreferredBit preferredBit = PreferredBit.NONE)
        {
            var count0 = 0;
            var count1 = 0;
            foreach (var bit in values.Select(value => value.Substring(bitIndex, 1)))
            {
                if (bit == "0") count0++;
                if (bit == "1") count1++;
            }

            if (count0 > count1)
            {
                return getMostCommon ? "0" : "1";
            }

            if (count0 < count1)
            {
                return getMostCommon ? "1" : "0";
            }

            Console.WriteLine($"The count is even for both 0 and 1 for this bit. Using preferredBit {(int)preferredBit}");
            return ((int)preferredBit).ToString();
        }

        public enum PreferredBit
        {
            ZERO,
            ONE,
            NONE
        }
    }
}
