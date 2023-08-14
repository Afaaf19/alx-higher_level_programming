#include "lists.h"
/**
 * is_palindrome - function that checks if the list is palindrome
 * @head: list's header
 * Return: 1 if success, 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *palin = *head;
	int cnt = 0, i = 0, j = 0;

	if (!*head)
		return (1);

	while (current)
	{
		current = current->next;
		cnt++;
	}
	current = *head;
	for (i = 1; i <= cnt; i++)
	{
		for (j = i; j <= cnt - i; j++)
			palin = palin->next;
		if (current->n != palin->n)
			return (0);
		current = current->next;
		palin = current;
	}
	return (1);
}
