#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#define MAX_SIZE 100

typedef struct
{
    int arr[MAX_SIZE];
    int top;

} MyStack;

MyStack *myStackCreate()
{
    MyStack *stack = (MyStack *)malloc(sizeof(MyStack));
    if(stack == NULL) {
        printf("Memory fail\n");
        exit(1);
    }
    stack->top = -1; 
    return stack;
}

void myStackPush(MyStack *obj, int x)
{
    if (obj->top == MAX_SIZE -1)
    {
        printf("Stack overflow\n");
        return;
    }
    obj->arr[++obj->top] = x;
    printf("Pushed %d onto the stack\n", x);
}

bool myStackEmpty(MyStack *obj)
{
    return obj->top = -1;
}

int myStackPop(MyStack *obj)
{
    if (myStackEmpty(obj))
    {
        printf("Stack is already empty\n");
        return -1;
    }
    int popped = obj->arr[obj->top];
    obj->top--;
    printf("Popped %d from the stack\n", popped);
    return popped;
}

int myStackTop(MyStack *obj)
{
    if(myStackEmpty(obj)) {
        printf("My stack is empty\n");
        return - 1;
    }
    return obj->arr[obj->top];
}

int myStackIsFull(MyStack *obj)
{
    return obj->top == MAX_SIZE - 1;
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

    printf("Top element: %d\n", myStackTop(stack)); // Should print 2

    myStackPop(stack); // Pops 2
    printf("Top element after pop: %d\n", myStackTop(stack)); // Should print 3

    printf("Is stack empty? %s\n", myStackEmpty(stack) ? "Yes" : "No");

    myStackPop(stack); // Pops 3
    printf("Is stack empty after popping all? %s\n", myStackEmpty(stack) ? "Yes" : "No");

    myStackFree(stack);
    return 0;
}