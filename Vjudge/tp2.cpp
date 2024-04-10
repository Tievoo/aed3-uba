#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int casos;
    cin >> casos;

    for (int caso = 1; caso <= casos; caso++) {
        int n;
        cin >> n;
        
        vector<int> altos(n);
        vector<int> anchos(n);
        
        for (int i = 0; i < n; i++) {
            cin >> altos[i];
            printf("elemento %d", altos[i]);
        }
        
        for (int i = 0; i < n; i++) {
            cin >> anchos[i];
            printf("elemento %d", anchos[i]);
        }

        printf("Case %d: ", caso);
        printf("%d\n", n);
    }
}