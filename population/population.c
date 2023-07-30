#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x, y, years = 0;

    do
    {
       int x = get_int("What's the start size of the population? ");
    }
    while (x < 9);

    do
    {
        int y = get_int("What's the end size of the population?")
    }
    while (y < x);

    while (start < end)
    {
        x = x + (x / 3) - (x / 4);
        years++;
    }

    printf("Years: %i\n", years);
    return 0;
}
