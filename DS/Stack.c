#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#define MAX_SIZE 100

typedef struct
{
    int arr[MAX_SIZE];    
    int head;

} MyStack;

MyStack *myStackCreate()
{
    MyStack *stack = (MyStack *)malloc(sizeof(MyStack));
    if(stack == NULL) {
        printf("Memmory allocation fail\n");
    }
    stack->head = -1;
    return stack;
}

bool myStackEmpty(MyStack *obj)
{
   return obj->head == -1; 
}

int myStackIsFull(MyStack *obj)
{
    return obj->head == MAX_SIZE - 1;
}


void myStackPush(MyStack *obj, int x)
{
    if(myStackIsFull(obj)) 
    {
        printf("The stack is already full\n");
        return;
    }
    obj->arr[++obj->head] = x;
   
    // printf("item pushed to the stack\n");
}

int myStackPop(MyStack *obj)
{
    if(myStackEmpty(obj)) {
        printf("Stack it is already empty");
        return -1;
    }
    int pooped = obj->arr[obj->head];
    obj->head--;
    printf("Object %d popped sucessfully", pooped);
    return pooped;
}

int myStackTop(MyStack *obj)
{
    if(myStackEmpty(obj)) {
        printf("Stack it is already empty");
        return -1;
    }
    return obj->arr[obj->head];
}


void myStackFree(MyStack *obj)
{
    free(obj);
}

int main()
{
    MyStack *stack = myStackCreate();
    myStackPush(stack, 3);
    myStackPush(stack, 2);
    myStackPush(stack, 2);
    myStackPush(stack, 2);
    myStackPush(stack, 2);
    for(int i = 0; i < 10; i ++) {
        printf("%d\n", stack->arr[i]);
    }
    // printf("Top element: %d\n", myStackTop(stack)); // Should print 2

    // myStackPop(stack); // Pops 2
    // printf("Top element after pop: %d\n", myStackTop(stack)); // Should print 3

    // printf("Is stack empty? %s\n", myStackEmpty(stack) ? "Yes" : "No");

    // myStackPop(stack); // Pops 3
    // printf("Is stack empty after popping all? %s\n", myStackEmpty(stack) ? "Yes" : "No");

    myStackFree(stack);
    return 0;
}