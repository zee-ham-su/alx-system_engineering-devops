#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>


/**
 * infinite_while - A function that enters an infinite loop
 * to keep the program running.
 * it is  used to keep the parent process alive after creating
 * the zombie child processes.
 * It uses the sleep() function to introduce a 1-second delay in
 * each iteration of the loop.
 * Return: Always returns 0.
 */

int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}

/**
 * main - The entry point of the program.
 * This function creates 5 zombie child processes and uses
 * the infinite_while() function to keep the parent process running.
 * Return: Always returns 0.
 */

int main(void)
{
pid_t child_pid;
int i;
for (i = 0; i < 5; i++)
{
child_pid = fork();

if (child_pid > 0)
{
printf("Zombie process created, PID: %d\n", child_pid);
}
else if (child_pid == 0)
{
exit(0);
}
else
{
perror("fork");
return (1);
}
}

    infinite_while();
   return (0);
}
