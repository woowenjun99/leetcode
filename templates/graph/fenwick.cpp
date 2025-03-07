#define LSOne(S) (S & -(S))
#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;

class FenwickTree {
    private:
        vll ft;
    public:
        void build(const vll &f) {
            int m = (int) f.size() - 1;
            ft.assign(m + 1, 0);
            for (int i = 1; i <= m; ++i) {
                ft[i] += f[i];
                if (i + LSOne(i) <= m) ft[i + LSOne(i)] += ft[i];
            }
        }

        ll rsq(int j) {
            ll sum = 0;
            for (; j; j -= LSOne(j)) sum += ft[j];
            return sum; 
        }

        ll rsq(int i, int j) { return rsq(j) - rsq(1); }

        void update(int i, ll v) {
            for (; i < (int)ft.size(); i += LSOne(i)) ft[i] += v;
        }

        int select(ll k) {
            int low = 1;
            int high = ft.size() - 1;
            for (int i = 0; i < 30; ++i) {
                int mid = (low + high) / 2;
                (rsq(mid) < k) ? low = mid : high = mid;
            }
            return high;
        }

        FenwickTree(ll m) { ft.assign(m + 1, 0); }

        FenwickTree(const vll &f) { build(f); }

        FenwickTree(int m, const vi &s) {
            vll f(m + 1, 0);
            for (int i = 0; i < (int)s.size(); ++i) ++f[s[i]];
            build(f);
        }
};
