#include <stdio.h>
#include <stdlib.h>
struct Node { int data; struct Node* next; };
int search(struct Node* head, int key) {
    while (head) {
        if (head->data == key) return 1;
        head = head->next;
    }
    return 0;
}
struct Node* createNode(int x) {
    struct Node* newNode
        = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = x;
    newNode->next = NULL;
    return newNode;
}
int main() {
    struct Node* head = createNode(10);
    head->next = createNode(20);
    head->next->next = createNode(30);
    printf("%s\n", search(head, 20) ? "Found" : "Not Found");
    return 0;
}
