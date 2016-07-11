#include <iostream>

using namespace std;

//��ɸѡ����
//��֪H[start~end]�г���start֮�������ѵĶ���
//���������е�����ʹH[start~end]��Ϊһ���󶥶�
typedef int ElemType;
void HeapAdjust(ElemType H[], int start, int end)
{

    ElemType temp = H[start];

    for(int i = 2*start + 1; i<=end; i*=2)
    {
        //��Ϊ������������Ϊ0������1������i������Ӻ��Һ��ӷֱ�Ϊ2i+1��2i+2
        if(i<end && H[i]<H[i+1])//���Һ��ӵıȽ�
        {
            ++i;//iΪ�ϴ�ļ�¼���±�
        }

        if(temp > H[i])//���Һ����л�ʤ���븸�׵ıȽ�
        {
            break;
        }

        //�����ӽ����λ�����Ժ��ӽ���λ�ý�����һ�ֵ�ɸѡ
        H[start]= H[i];
        start = i;

    }

    H[start]= temp; //�����ʼ����г��Ԫ��
}

void HeapSort(ElemType A[], int n)
{
    //�Ƚ����󶥶�
    for(int i=n/2; i>=0; --i)
    {
        HeapAdjust(A,i,n);
    }
    //��������
    for(int i=n-1; i>0; --i)
    {
        //���һ��Ԫ�غ͵�һԪ�ؽ��н���
        ElemType temp=A[i];
        A[i] = A[0];
        A[0] = temp;

        //Ȼ��ʣ�µ�����Ԫ�ؼ�������Ϊ�󶥶�
        HeapAdjust(A,0,i-1);
    }

}
