#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#define MAX_SIZE 100

typedef struct
{

    int arr[MAX_SIZE];
    int head;
    int tail;
} MyQueue;

MyQueue *myQueueCreate()
{
    MyQueue *queue = (MyQueue *)malloc(sizeof(MyQueue));
    if (queue == NULL)
    {
        printf("Memmory allocation fail\n");
    }
    queue->head = 0;
    queue->tail = 0;
    return queue;
}

bool myQueueEmpty(MyQueue *obj)
{
    return obj->head == obj->tail;
}

bool myQueueFull(MyQueue *obj)
{
    return obj->tail == MAX_SIZE;
}

void myQueuePush(MyQueue *obj, int x)
{
    if (myQueueFull(obj))
    {
        printf("Queue is already full cannot add\n");
        return;
    }
    obj->arr[obj->tail++] = x;
}

int myQueuePop(MyQueue *obj)
{
    if (myQueueEmpty(obj))
    {
        printf("Obj is empty");
        return -1;
    }
    return obj->arr[obj->head++];
}

int myQueuePeek(MyQueue *obj)
{
    if (myQueueEmpty(obj))
    {
        printf("Obj is empty");
        return -1;
    }
    int p = obj->arr[obj->head];
    printf("PEAK -> %d\n", p);
    return p;
}

void printQueue(MyQueue *obj)
{
    if (myQueueEmpty(obj))
    {
        printf("Queue is empty\n");
        return;
    }

    for (int i = obj->head; i < obj->tail; i++)
    {
        printf("%d ", obj->arr[i]);
    }
    printf("\n");
}

void myQueueFree(MyQueue *obj)
{
    free(obj);
}

int main()
{
    MyQueue *queue = myQueueCreate();
    myQueuePush(queue, 11);
    myQueuePush(queue, 3);
    myQueuePush(queue, 1);
    myQueuePush(queue, 4);
    myQueuePush(queue, 5);
    myQueuePush(queue, 28);
    myQueuePush(queue, 123);
    myQueuePeek(queue);
    printQueue(queue);
    myQueuePop(queue);
    printQueue(queue);
    return 0;
    myQueueFree(queue);
}

/**
 * Your MyQueue struct will be instantiated and called as such:
 * MyQueue* obj = myQueueCreate();
 * myQueuePush(obj, x);

 * int param_2 = myQueuePop(obj);

 * int param_3 = myQueuePeek(obj);

 * bool param_4 = myQueueEmpty(obj);

 * myQueueFree(obj);
*/