#include <cs50.h>
#include <stdio.h>
#include < string.h>


int main(void)
{
    string = get_string("Text: ");

    int letters = 0;
    for(int i = 0; i < strlen(text); i++)
    {
        if((text[i] >= 'a' && text[i] <= 'z') ||
            (text[i] >= 'A' && text[i] <= 'Z'))
        letters++;
    }

    int words = 1;
    for(int i = 0; i <strlen(text); i++)
    {
        if(text[i] == '  ')
        words++;
    }

    int sentences = 0;
    for(int i = 0; i < strlen(text); i++)
    {
        if(text[i] == '.' || text[i] == '!' ||
            text[i] == '?')
        sentences++;
    }

    float calculation = (0.0588 * letters / words * 100) - (0.296 * sentences / words * 100) - 25.8;

    int index = round(calculation);

    if(index < 1);
    {
        printf("Before Grade 1\n");
        returm 0;
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
        return 0;
    }
    else
    {
        printf("Grade %i\n", index);
    }
}
