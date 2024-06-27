#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

#define Graph vector<vector<int>>

long long int dantzig(Graph &matrix, int n) {
    long long int res = 0;
    for (int k = 1; k < n; k++) {
        for (int i = 0; i < k; i++) {
            int ItoK = INT_MAX;
            int KtoI = INT_MAX;
            
            for (int j = 0; j < k; j++) {
                ItoK = min(ItoK, matrix[i][j] + matrix[j][k]);
                KtoI = min(KtoI, matrix[k][j] + matrix[j][i]);
            }
            
            matrix[i][k] = ItoK;
            matrix[k][i] = KtoI;
        }
        
        for (int i = 0; i <= k; i++) {
            for (int j = 0; j <= k; j++) {
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j]);
                res += matrix[i][j];
            }
        }
    }
    return res;
}

void reorder(Graph &matrix, vector<int> order, int n)
{
    reverse(order.begin(), order.end());
    Graph newMatrix(n, vector<int>(n,0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            newMatrix[i][j] = matrix[order[i]][order[j]];
        }
    }

    matrix = newMatrix;
}

int main()
{
    int tests;
    cin >> tests;

    while (tests--) {
        int tw;
        cin >> tw;

        Graph matrix(tw, vector<int>(tw, 0));

        for (int i = 0; i < tw; i++) {
            for (int j = 0; j < tw; j++) {
                cin >> matrix[i][j];
            }
        }

        vector<int> order(tw);

        for (int i = 0; i < tw; i++) {
            cin >> order[i];
        }
        reorder(matrix, order, tw);
        long long int r = dantzig(matrix, tw);
        
        cout << r << endl;
    }
}