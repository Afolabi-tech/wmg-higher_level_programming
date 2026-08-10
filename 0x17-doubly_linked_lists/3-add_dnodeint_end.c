#include "lists.h"

/**
*add_dnodeint_end - function that adds new node at the end of a dlistint_t list
*@head: a pointer to the first node
*@n: the new node to be added
*
*Return: the address of the new element, or NULL if it failed
*/

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
    dlistint_t *current, *new = malloc(sizeof(dlistint_t));

    if (new == NULL)
        return NULL;

    new->n = n;
    new->prev = NULL;
    new->next = NULL;

    if (*head == NULL)
    {
        *head = new;
        return (new);
    }

    current = *head;

    while (current->next != NULL)
        current = current->next;

    current->next = new;
    new->prev = current;

    return (new);

}
