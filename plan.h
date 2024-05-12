#ifndef PLAN_H
#define PLAN_H

#include <string>
#include <stdlib.h>
using namespace std;

class plan{
    public:
        plan();
        
    private:
        int lengthDays;
        int lengthWeeks;
        string race;
        string raceLocation;
        int raceMonth;
        int raceDay;
        int raceYear;
        int currentWeek;
};
#endif