#include <stdio.h>
#include <stdlib.h>

#define SIZE 1000

int top = -1, box[SIZE];
void push();

void push(int element)
{
	top = top + 1;
	box[top] = element;
}
