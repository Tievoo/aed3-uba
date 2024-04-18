#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int acorn(vector<vector<int>>& arboles, int t, int h, int f) {
    vector<int> max_per_h(h + 1, 0);
    
    for (int i = 1; i <= h; i++) {
      for (int j = 0; j < t; j++) {
        int jump = 0;
        if (i - f >= 0) {
          jump = max_per_h[i - f];
        }
        arboles[j][i] = arboles[j][i] + max(arboles[j][i - 1], jump);
        max_per_h[i] = max(max_per_h[i], arboles[j][i]);
      }
    }

    return max_per_h[h];
} 

int main() {
    int casos;
    cin >> casos;

    for (int caso = 0; caso < casos; caso++) {
        int t, h, f;
        cin >> t >> h >> f;

        vector<vector<int>> arboles(t, vector<int>(h + 1, 0));

        for (int i = 0; i < t; i++) {
          int amount;
          cin >> amount;

          for (int j = 0; j < amount; j++) {
            int acorn;
            cin >> acorn;

            arboles[i][acorn]++;
          }

        }
        int acorns = acorn(arboles, t, h, f);
        printf("%d\n", acorns);
    }
}