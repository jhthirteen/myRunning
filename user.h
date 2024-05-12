#ifndef USER_H
#define USER_H

#include <string>
#include <stdlib.h>
#include "BST.h"
#include <vector>
#include "plan.h"
using namespace std;

class user{
    public:

    
    private:
        string name;
        int age;
        int weight;
        string location;
        int totalMiles;
        BST allWorkouts;
        vector<plan> allPlans; 
};
#endif