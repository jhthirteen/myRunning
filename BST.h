#ifndef BST_H
#define BST_H

#include "workout.h"
#include <string>
using namespace std;

class BST{
    public:
        BST();
        workout* find(int id);
        void insert(workout* toInsert);
        void remove(workout* toRemove);
        workout* getRoot();

    private:
        workout* root;
};
#endif