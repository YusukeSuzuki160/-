#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int h, w;
    cin >> h >> w;
    vector<vector<string>> a(h, vector<string>(w));
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            cin >> a.at(i).at(j);
        }
    }
    int n;
    cin >> n;
    vector<int> r(n);
    vector<int> c(n);
    vector<int> e(n);
    for (int i = 0; i < n; i++)
    {
        cin >> r.at(i);
        cin >> c.at(i);
        cin >> e.at(i);
    }
}