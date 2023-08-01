#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x;
    do
    {
        x = get_int ("Please enter height: ");
    }
    while (height < 1 || height > 8);

    for (int a = 0; a < x; a++)
    {
        for (int b = 0; b < x; b++)
        {
            if (a + b < x - 1)
                    print(" ");
                else
                    print("#")
        }
        print("\n");
    }
}