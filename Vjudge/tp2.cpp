#include <iostream>
#include <vector>
#include <string>
using namespace std;

int lds(vector<int>& h, vector<int>& w, int lng) {
    vector<int> m(lng, -1);
    int maxD = 0;
    for (int i = 0; i < lng; i++) {
        m[i] = w[i];
        for (int j = 0; j < i; j++) {
            if (h[i] < h[j]) {
                m[i] = max(m[i], w[i] + m[j]);
            }
        }
        maxD = max(m[i], maxD);
    }
    
    return maxD;
}

int lis(vector<int>& h, vector<int>& w, int lng) {
    vector<int> m(lng, -1);
    int maxI = 0;
    for (int i = 0; i < lng; i++) {
        m[i] = w[i];
        for (int j = 0; j < i; j++) {
            if (h[i] > h[j]) {
                m[i] = max(m[i], w[i] + m[j]);
            }
        }
        maxI = max(m[i], maxI);
    }
    return maxI;
}

int main() {
    int n;
    cin >> n;

    for (int k = 1; k <= n; k++) {
        int lng;
        cin >> lng;
        
        vector<int> h(lng);
        vector<int> w(lng);
        
        for (int i = 0; i < lng; i++) {
            cin >> h[i];
        }
        
        for (int i = 0; i < lng; i++) {
            cin >> w[i];
        }
        
        int inc = lis(h, w, lng);
        int dec = lds(h, w, lng);
        
        string res;
        
        if (inc >= dec) {
            res = "Increasing (" + to_string(inc) + "). Decreasing (" + to_string(dec) + ").";
        } else {
             res = "Decreasing (" + to_string(dec) + "). Increasing (" + to_string(inc) + ").";
        }
        
        
        cout << "Case " << k << ". " << res << endl;
        
    }
}