#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>
/**
 * struct listint_s -a  singly linked list
 * @n: integer
 * @next: next node
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

#endif

