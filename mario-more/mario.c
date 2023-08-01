#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x;
    do
    {
        x = get_int("Please enter height: ");
    }
    while (0 < x < 9);

    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < x; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}