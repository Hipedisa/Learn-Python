#include <stdio.h>

int cents;
int calc_quarters(int cents);
int calc_dimes(int cents);
int calc_nickels(int cents);
int calc_pennies(int cents);

int main()

{
    do
    {
        printf("Enter amount of cents owed: ");
        scanf("%i", &cents);
    } while (cents < 0);

    int quarters = calc_quarters(cents);
    cents -= quarters * 25;

    int dimes = calc_dimes(cents);
    cents -= dimes * 10;

    int nickels = calc_nickels(cents);
    cents -= nickels * 5;

    int pennies = calc_pennies(cents);
    cents -= pennies * 1;

    int total_coins = quarters + dimes + nickels + pennies;

    printf("Total coins: %i", total_coins);
}

int calc_quarters(int cents)
{

    int quarters = 0;
    while (cents >= 25)
    {
        cents -= 25;
        quarters++;
    }
    return quarters;
}

int calc_dimes(int cents)
{

    int dimes = 0;
    while (cents >= 10)
    {
        cents -= 10;
        dimes++;
    }
    return dimes;
}

int calc_nickels(int cents)
{

    int nickels = 0;
    while (cents >= 5)
    {
        cents -= 5;
        nickels++;
    }
    return nickels;
}

int calc_pennies(int cents)
{

    int pennies = 0;
    while (cents >= 1)
    {
        cents -= 1;
        pennies++;
    }
    return pennies;
}