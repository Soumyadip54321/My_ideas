#include <stdio.h>
#define Row 4
#define Col 4
 
void spiralPrint(int m, int n, int a[Row][Col])
{
    int i, k = 0, l = 0;
    //Here we put pointers on 1st and last rows in conjunction to 1st and last columns resp.k,l,m,n.
    while (k < m && l < n) {
        //Print the first row from the remaining rows 
        for (i = l; i < n; ++i) {
            printf("%d ", a[k][i]);
        }
        k++;
 
        //Print the last column from the remaining columns
        for (i = k; i < m; ++i) {
            printf("%d ", a[i][n - 1]);
        }
        n--;
 
        //Print the last row from the remaining rows */
        if (k<m) {
            for (i = n - 1; i >= l; --i) {
                printf("%d ", a[m - 1][i]);
            }
            m--;
        }
 
        //Printing the first column from the remaining columns
        if (l < n) {
            for (i = m - 1; i >= k; --i) {
                printf("%d ", a[i][l]);
            }
            l++;
        }
    }
}
int main()
{
    int M[Row][Col] = { { 5, 6, 7, 8 },
                    { 9, 10, 11, 12 },
                    { 13, 14, 15, 16 },
                    { 17, 18, 19, 20 } };
 
    spiralPrint(Row, Col, M);
    return 0;
}