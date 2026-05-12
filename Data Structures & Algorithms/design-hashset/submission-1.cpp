class MyHashSet {
private:
    vector<int> set;

public:
    MyHashSet() {}
    
    void add(int key) {
        for(auto k : set) {
            if (k == key) {
                return;
            }
        }
        set.push_back(key);
    }
    
    void remove(int key) {
        bool pop_back = false;
        for(int i = 0; i<set.size(); ++i) {
            if (set[i] == key) {
                set[i] = set[set.size() - 1];
                pop_back = true;
                break;
            }
        }
        if(pop_back) {
            set.pop_back();
        }

    }
    
    bool contains(int key) {
        for(auto k : set) {
            if (k == key) {
                return true;
            }
        }
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */