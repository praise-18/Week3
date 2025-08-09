#include <stdio.h>
#include <stdlib.h>
struct Node { int data; struct Node* next; };
void deleteNode(struct Node** head, int value) {
    struct Node* temp = *head, *prev = NULL;
    if (temp && temp->data == value) {
        *head = temp->next; free(temp); return;
    }
    while (temp && temp->data != value) {
        prev = temp; temp = temp->next;
    }
    if (!temp) return;
    prev->next = temp->next; free(temp);
}
struct Node* createNode(int x) {
    struct Node* newNode
        = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = x;
    newNode->next = NULL;
    return newNode;
}
void printList(struct Node* head) {
    while (head) { printf("%d -> ", head->data); head = head->next; }
    printf("NULL\n");
}
int main() {
    struct Node* head = createNode(10);
    head->next = createNode(20);
    head->next->next = createNode(30);
    deleteNode(&head, 10);
    printList(head);
    return 0;
}
