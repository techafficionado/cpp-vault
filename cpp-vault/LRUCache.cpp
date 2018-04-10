#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <list>
class LRUCache {
public:
    std::unordered_map<int,int> m_lmap;//(capacity); // <int key, int value>
    std::list<int> m_ll;//(capacity); // <int key>
    int m_cap;
    LRUCache(int capacity) {
        m_cap = capacity;
        //m_lmap.resize(capacity); // <int key, int value>
        m_ll.resize(capacity); // <int key>
        
    }
    
    int get(int key) {
        //if (std::find(m_lmap.begin(),m_lmap.end(),key) != m_lmap.end()){
        if(m_lmap.find(key) != m_lmap.end()){
            // update ll to put key at the end
            int key = m_ll.front();
            m_ll.pop_front();
            m_ll.push_back(key);
            return m_lmap[key];
        }
        else
            return -1;
    }
    
    void put(int key, int value) {
        // if element is new
        //if (std::find_if(m_lmap.begin(),m_lmap.end(),key) != m_lmap.end()){
        if(m_lmap.find(key) == m_lmap.end()){
            if (m_ll.size() == m_cap)
            {
                // list is full, need eviction
                evict();                
            }
        }
        m_lmap[key] = value;
        m_ll.push_back(key);
    }
    
    void evict(){
        //evict should delete both m_lmap and m_ll
        int key = m_ll.front();
        m_ll.pop_front();
        // remove key from m_lmap
        //m_ll.erase(std::remove_if(m_ll.begin(),m_ll.end(),key),m_ll.end());
        m_lmap.erase(key);
    }
};

int main(){
    //LRUCache obj = new LRUCache(2);
    int cap = 2;
    LRUCache l = new LRUCache(cap);
    //obj.put(1,1);
    //obj.put(2,2);
    //std::cout << "obj get" << obj.get(1) << std::endl;
}
