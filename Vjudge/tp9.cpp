#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

typedef vector<int> vi;
typedef vector<vector<int>> grafo;

int distancia(int a, int b) {
    // Busco la distancia entre los numeros de 4 digitos
    int dist = 0;
    for (int i = 0; i < 4; i++) {
        int ddist = abs(a % 10 - b % 10);
        dist += min(ddist, 10 - ddist);
        a /= 10;
        b /= 10;
    }

    return dist;
}

#define distancia_a_0(a) distancia(a, 0)

int prim(grafo G, vi passwords) {
    int n = G.size();
    vi dist(n, INT_MAX);
    vector<bool> visitado(n, false);

    int idx = 0;
    for (int i = 0; i < n; i++) {
        int dist1 = distancia_a_0(passwords[i]);
        int dist2 = distancia_a_0(passwords[idx]);
        if (dist1 < dist2) {
            idx = i;
        }
    }

    dist[idx] = 0;

    int res = distancia_a_0(passwords[idx]);
    for (int i = 0; i < n; i++) {
        int u = -1;
        for (int j = 0; j < n; j++) {
            if (!visitado[j] && (u == -1 || dist[j] < dist[u])) {
                u = j;
            }
        }
        visitado[u] = true;
        res += dist[u];
        for (int v = 0; v < n; v++) {
            if (G[u][v] < dist[v]) {
                dist[v] = G[u][v];
            }
        }
    }

    return res;
}

int main() {
    int cases;
    std::cin >> cases;

    for (int i = 0; i < cases; i++) {
        int length;
        std::cin >> length;
        vi passwords(length);
        grafo g(length, vi(length, 0));
        for (int j = 0; j < length; j++) {
            std::cin >> passwords[j];
        }
        for (int j = 0; j < length-1; j++) {
            for (int k = j+1; k < length; k++) {
                int dist = distancia(passwords[j], passwords[k]);
                g[j][k] = dist;
                g[k][j] = dist;
            }
        }
        int res = prim(g, passwords);
        std::cout << res << std::endl;
    }
}