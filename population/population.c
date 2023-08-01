#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x;
    do
    {
        x = get_int("What is the starting size of the population?: ");
    }
    while (x < 9);

    int y;
    do
    {
        y = get_int("What is the ending size of the population?: ");
    }
    while (y < x);

    int years = 0;
    while (x < y)
    {
        x = x + (x / 3) - (x / 4);
        years++;
    }

    printf("Years: %i\n", years);
}