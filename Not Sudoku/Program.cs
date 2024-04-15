using System;

namespace Program
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] nums = Console.ReadLine().Split(' ');
            byte rowNum = byte.Parse(nums[0]);
            byte colNum = byte.Parse(nums[1]);
            ushort[,] board = new ushort[rowNum, colNum];
            ushort[] pos = new ushort[2];
            for (byte y = 0; y < rowNum; y++)
            {
                string[] cells = Console.ReadLine().Split(' ');
                for (byte x = 0; x < colNum; x++)
                {
                    if (cells[x] == "x")
                    {
                        board[y, x] = 0;
                        pos[0] = y;
                        pos[1] = x;
                    } else
                    {
                        ushort n = ushort.Parse(cells[x]);
                        board[y, x] = n;
                    }
                }
            }
            ushort sum = 0;
            for (byte y = 0; y < rowNum; y++)
            {
                for (byte x = 0; x < colNum; x++)
                {
                    if (board[y, x] == 0)
                    {
                        for (byte i = 0; i < rowNum; i++)
                        {
                            sum += board[i, pos[1]];
                        }
                        ushort shit = (ushort)((double)rowNum / 2 * (rowNum + 1));
                        board[y, x] = (ushort)(shit - sum);
                    }
                    Console.Write(board[y, x]);
                    Console.Write(" ");
                }
                Console.Write("\n");
            }
        }
    }
}