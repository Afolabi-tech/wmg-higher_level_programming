#include "lists.h"


/**
 * reverse_list - reverses a singly linked list
 * @head: pointer to the head of the list
 *
 * Return: pointer to the new head
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 *
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;
	listint_t *second_half;
	listint_t *copy_second;
	listint_t *first_half;
	int palindrome = 1;

	if (head == NULL || 
            *head == NULL || 
            (*head)->next == NULL)
		return (1);

	slow = *head;
	fast = *head;

	/* Find the middle of the list */
	while (fast != NULL && 
            fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/* Reverse the second half */
	second_half = reverse_list(slow);
	copy_second = second_half;

	first_half = *head;

	/* Compare both halves */
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			palindrome = 0;
			break;
		}

		first_half = first_half->next;
		second_half = second_half->next;
	}

	/* Restore the original list */
	reverse_list(copy_second);

	return (palindrome);
}
