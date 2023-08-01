#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x;
    do
    {
        int x = get_int("What's the start size of the population?: ");
    }
    while (x < 9);

    int y;
    do
    {
        int y = get_int("What's the end size of the population?: ");
    }
    while (y < x);

    int years = 0;
    do
    {
        x = x + (x / 3) - (x / 4);
        years++;
    }
    while (x < y);

    printf("Years: %i\n", years);
}