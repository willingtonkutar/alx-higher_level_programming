#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - this checks for singly-linked list
 * @list: this is the singlylinked list
 * Return 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *abx, *mu;

	if (list == NULL || list->next == NULL)
		return (0);
	abx = list->next;
	mu = list->next->next;

	while (abx && mu && mu->next)
	{
		if(abx == mu)
			return (1);
		abx = abx->next;
		mu = mu->next->next;
	}

	return (0);
}
