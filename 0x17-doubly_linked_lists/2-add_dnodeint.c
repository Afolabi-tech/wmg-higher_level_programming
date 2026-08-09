#include "lists.h"

/**
*add_dnotint - function that adds a new node at the beginning of a dlistint_t list
*@head: pointer to the head of the list
*@n: value to store in the new node
*
*Return: address of the new element, or NULL if it fails
*/

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
    dlistint_t *temp, *node = malloc(sizeof(dlistint_t));

    if (node == NULL) {
        return NULL;
    }
    node->n = n;
    node->prev = NULL;
    node->next = NULL;

    if (*head == NULL) {
        node->next = NULL;
        *head = node;
        return (*head);
    }

    temp = *head;
    node->next = temp;
    temp->prev = node;
    *head = node;

    return (node);
}
