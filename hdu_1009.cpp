#include <iostream>
#include <stdio.h>
using namespace std;

struct Node{
    int quantity;
    double proportion;
    Node * next;
};

Node * addNode(Node * head, Node * node)
{
    if(head -> proportion < node -> proportion)
    {
        node -> next = head;
        return node;
    }
    Node * temp = head;
    while(temp)
    {
        if(temp -> next != NULL && temp -> proportion >= node -> proportion && node -> proportion > temp -> next -> proportion)
        {
            node -> next = temp -> next;
            temp -> next = node;
            break;
        }
        else if(temp -> next == NULL && temp -> proportion > node -> proportion)
        {
            temp -> next = node;
            break;
        }
        temp = temp -> next;
    }
    return head;
}

int main()
{
    int m, n;
    int j, f;
    double result;
    while(cin >> m >> n && m != -1 && n != -1)
    {
        result = 0.0;
        cin >> j >> f;
        Node * head = new Node;
        head -> quantity = f;
        head -> proportion = (double)j / f;
        head -> next = NULL;
        n--;
        while(n)
        {
            cin >> j >> f;
            Node * temp = new Node;
            temp -> quantity = f;
            temp -> proportion = (double)j/ f;
            temp -> next = NULL;
            head = addNode(head, temp);
            n--;
        }
        Node * temp = head;
        while(head)
        {
            if(m == 0)
                break;
            if(m >= head -> quantity)
            {
                m -= head -> quantity;
                result += head -> quantity * head -> proportion;
                head = head -> next;
            }
            else if(m < head -> quantity)
            {
                result += m * head -> proportion;
                m = 0;
                break;
            }
        }
        printf("%.3f\n",result);
    }
    return 0;
}
