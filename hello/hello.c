#include <stdio.h>

int main()
{
    int height;

    do
    {
        printf("Height: ");
        scanf("%i", &height);
    } while (height <= 0);

    for (int row = 0; row < height; row++)
    {
        // Spaces
        for (int j = 0; j < height - row; j++)
        {
            printf(" ");
        }

        // First hashes
        for (int j = 0; j < row; j++)
        {
            printf("#");
        }

        printf("  ");

        // Second hashes
        for (int j = 0; j < row; j++)
        {
            printf("#");
        }

        printf("\n");
    }
}