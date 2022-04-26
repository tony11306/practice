vector<vector<int>> getConvexHull(vector<vector<int>>& points) {
    int removeIndex = 0;
    // find lowest left point, which is definitely one point on the convex hull
    for(int i = 0; i < points.size(); ++i) {
        if(points[removeIndex][1] > points[i][1]) {
            removeIndex = i;
        } else if(points[removeIndex][1] == points[i][1] && points[removeIndex][0] > points[i][0]) {
            removeIndex = i;
        }
    }
    vector<int> start = points[removeIndex];
    points.erase(points.begin() + removeIndex);

    auto getQuadrant = [&](vector<int>& a) {
        if(a[0] - start[0] > 0 && a[1] - start[1] >= 0) {
            return 1;
        }

        if(a[0] - start[0] <= 0 && a[1] - start[1] > 0) {
            return 2;
        }

        if(a[0] - start[0] < 0 && a[1] - start[1] <= 0) {
            return 3;
        }
        return 4;
    };

    auto getCross = [&](int ax, int ay, int bx, int by) {
        return by * ax - bx * ay;
    };

    auto getNorm = [&](vector<int>& a) {
        return (a[0] - start[0]) * (a[0] - start[0]) + (a[1] - start[1]) * (a[1] - start[1]);
    };

    sort(points.begin(), points.end(), [&](vector<int>& a, vector<int>& b) {
        if(getQuadrant(a) == getQuadrant(b)) {
            int acb = getCross(a[0] - start[0], a[1] - start[1], b[0] - start[0], b[1] - start[1]);
            if(acb == 0) {
                return getNorm(a) < getNorm(b);
            }
            return acb > 0;
        }
        return getQuadrant(a) < getQuadrant(b);
    });

    // reverse last segment if there exist points on same line
    if(points.size() > 0) {
        int i = points.size() - 1;
        vector<int> d = {points.back()[0] - start[0], points.back()[1] - start[1]};

        while(i > 0) {
            if(getCross(d[0], d[1], points[i][0] - start[0], points[i][1] - start[1]) != 0) {
                break;
            }
            i--;
        }
        reverse(points.begin() + i + 1, points.end());
    }

    // graham scan
    vector<vector<int>> ans;
    ans.push_back(start);

    // using cross product, if a cross b is postive then a is on right hand side of b
    // vise versa
    auto isTurningLeft = [](vector<int>& a, vector<int>& b, vector<int>& c) {
        return (c[1] - b[1]) * (b[0] - a[0]) - (c[0] - b[0]) * (b[1] - a[1]) >= 0;
    };


    for(int i = 0; i < points.size(); ++i) {
        if(i == 0) {
            ans.push_back(points[i]);
        } else {
            while(!isTurningLeft(ans[ans.size() - 2], ans[ans.size() - 1], points[i])) {
                ans.pop_back();
            }
            ans.push_back(points[i]);

        }
    }

    return ans;
}
