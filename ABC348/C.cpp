#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<long long > a(n);
    vector<long long> c(n);
    for (int i = 0; i < n; i++)
    {
        cin >> a.at(i);
        cin >> c.at(i);
    }
    vector<long long> min_scores(pow(10, 9), pow(10, 9) + 7);
    for (int i = 0; i < n; i++)
    {
        long long a_ = a.at(i);
        long long c_ = c.at(i);
        if (a_ < min_scores.at(c_ - 1))
        {
            min_scores.at(c_ - 1) = a_;
        }
    }
    long long max_scores = 0;
    for (int i = 0; i < n; i++)
    {
        if (a.at(i) > max_scores )
        {
            max_scores = a.at(i);
        }
    }
    cout << max_index << endl;
}