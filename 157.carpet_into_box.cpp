class Solution{
    public:
    int carpetBox(int A, int B, int C, int D){
        int op1 = 0, op2 = 0;
        int a = A, b = B, c = C, d = D;
        while(a > c or b > d){
            if(a > c) op1++, a /= 2;
            if(b > d) op1++, b /= 2;
        }
        a = A, b = B, c = C, d = D;
        while(a > d or b > c){
            if(a > d) op2++, a /= 2;
            if(b > c) op2++, b /= 2;
        }
        return min(op1,op2);
    }
};
