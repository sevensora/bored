#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x;
    do
    {
        x = get_int("Please enter height: ");
    }
    while (x < 1 || x > 8);
}