using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Prime_in_Parallel
{
    class Program
    {
        static void Main(string[] args)
        {
            Program.GetPrimeNumbers(1000000);
          
       }

        static void GetPrimeNumbers(int max)
        {

            var isPrime = new bool[max + 1];
            for (int i = 0; i <= max; i++)
                isPrime[i] = true;

            Parallel.For(3, max, x =>
            {
                for (int y = 2; y < x; y++)
                {
                    if((x % y) == 0)
                    {
                        isPrime[x] = false;
                        y = x + 1;
                    }
                }
            });

            Console.WriteLine("2");
            Console.WriteLine("3");
            for (int n = 5; n <= max; n++)
            {
                if (isPrime[n])
                {
                    Console.WriteLine(n);
                }
            }
            Console.WriteLine("Einde..");
        }
    }
}
