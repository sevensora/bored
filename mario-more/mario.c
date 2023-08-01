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
}