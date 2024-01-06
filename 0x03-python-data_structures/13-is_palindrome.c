#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

/**
  *is_palindrome - checks if linked list is a palindromw
  *@head: linked list
  *
  *Return: 1 if palindrome, 0 if not
  */
int is_palindrome(listint_t **head)
{
	listint_t **prev, *start = *head;
	int i = 0, list_count;

	if (*head == NULL)
		return (1);

	list_count = list_len(head);
	prev = malloc(list_count * sizeof(listint_t));

	while (i < list_count)
	{
		if ((*head)->next)
		{
			prev[i] = *head;
			*head = (*head)->next;
			i++;
		}
		else
			break;
	}

	for (i = i; start->next; i--)
	{
		if (start->n == (*head)->n)
		{
			*head = prev[i - 1];
			if (start == *head)
				return (1);
			start = start->next;
		}
		else
			break;
	}
	free(prev);
	return (0);
}
/**
  *list_len - Counts number of nodes in the list
  *@head: linked list
  *
  *Return: count
*/
int list_len(listint_t **head)
{
	listint_t *trav = *head;
	int i = 0;

	while (trav)
	{
		i++;
		trav = trav->next;
	}

	return (i);
}
