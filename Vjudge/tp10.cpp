#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <climits>

using namespace std;

#define MAX_FLOOR 100
#define MAX_ELEVATORS 5

struct Node {
    int floor;
    int elevator;
    int T;

    int dist(const Node& other) const {
        
        if (elevator != other.elevator && floor == other.floor) {
            return 60;
        } else if (elevator == other.elevator) {
            return abs(floor - other.floor) * T;
        } else {
            return INT_MAX;
        }
    }

    Node(int floor, int elevator, int T) : floor(floor), elevator(elevator), T(T) {}

    bool operator<(const Node& other) const {
        return dist(other) < 0;
    }
};

struct NodeComparator {
    bool operator()(const Node& a, const Node& b) const {
        return a.dist(b) > 0; // Using '>' to create a min-heap
    }
};

#define Graph vector<vector<Node>>



int dijkstra(Graph& graph, int n, int floor, Node& start) {
    vector<int> dist((MAX_FLOOR + 1) * MAX_ELEVATORS, INT_MAX);
    priority_queue<Node, vector<Node>, NodeComparator> pq;

    pq.push(start);
    dist[start.floor * MAX_ELEVATORS + start.elevator] = 0;

    while (!pq.empty()) {
        Node u = pq.top();
        pq.pop();

        int uIndex = u.floor * MAX_ELEVATORS + u.elevator;

        for (Node v : graph[uIndex]) {
            
            int alt = dist[uIndex] + u.dist(v);
            int vIndex = v.floor * MAX_ELEVATORS + v.elevator;
            if (alt < dist[vIndex]) {
                dist[vIndex] = alt;
                pq.push(v);
            }
        }
    }

    int minDist = INT_MAX;
    for (int i = 0; i < n; i++) {
        minDist = min(minDist, dist[floor * MAX_ELEVATORS + i]);
    }

    return minDist;
}

int elevatorIn0(vector<vector<int>>& elevators) {
    for (int i = 0; i < elevators.size(); i++) {
        if (elevators[i][0] == 0) {
            return i;
        }
    }
    return -1;
}

Graph buildGraph(vector<vector<int>>& elevators, int n, vector<int> T) {
    Graph graph((MAX_FLOOR + 1) * MAX_ELEVATORS);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < elevators[i].size(); j++) {
            // Add same elevator connections
            for (int k = j + 1; k < elevators[i].size(); k++) {
                Node a(elevators[i][k], i, T[i]);
                Node b(elevators[i][j], i, T[i]);
                
                graph[elevators[i][j] * MAX_ELEVATORS + i].push_back(a);
                graph[elevators[i][k] * MAX_ELEVATORS + i].push_back(b);
            }

            // Add same floor connections
            for (int k = 0; k < n; k++) {
                for (int l = 0; l < elevators[k].size(); l++) {
                    if (elevators[i][j] == elevators[k][l] && k != i) {
                        Node a(elevators[k][l], k, T[k]);
                        Node b(elevators[i][j], i, T[i]);

                        graph[elevators[i][j] * MAX_ELEVATORS + i].push_back(a);
                        graph[elevators[k][l] * MAX_ELEVATORS + k].push_back(b);
                    }
                }
            }
        }
    }

    return graph;
}

int main() {
    string line;

    while (getline(cin, line)) {
        if (line.empty()) {
            break;
        }
        istringstream ssnk(line);
        int n, k;
        ssnk >> n >> k;
        
        getline(cin, line);

        istringstream sst(line);
        vector<int> T(n);
        
        int T_i;
        for (int i = 0; i < n; ++i) {
            sst >> T_i;
            T[i] = T_i;
        }
        
        vector<vector<int>> elevators(n);

        for (int i = 0; i < n; ++i) {
            int current_floor;
            getline(cin, line);
            if (line.empty()) {
                getline(cin, line);
            }

            istringstream sselv(line);
            
            while (sselv >> current_floor) {
                elevators[i].push_back(current_floor);
            }
        }
        
        int startIdx = elevatorIn0(elevators);
        if (startIdx == -1) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        Node start(0, startIdx, T[startIdx]);

        Graph graph = buildGraph(elevators, n, T);

        int result = dijkstra(graph, n, k, start);

        if (result == INT_MAX) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << result << endl;
        }
        
    }

    return 0;
}
