#include "lists.h"

/**
 * check_cycle _ checks if a list has a cycle
 * @list: linked list
 * @Return: 0 for no cycle and 1 for cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	if (!list || !list->next)
		return(0);
	fast = list;
	slow = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return(1);
		}
	}
	return (0);
}
