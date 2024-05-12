#ifndef WORKOUT_H
#define WORKOUT_H

#include <string>
#include <stdlib.h>
using namespace std;

class workout{
    public:
        workout();
        workout(int distance1, int distance2, int time, int sec, int paceTime, int paceSeconds, int id, string notes);
        
        void setDistance(string mileage);
        void setTime(string time);
        void setPace(string pace);
        void recordNotes(string info);
        
    private:
        int distance;
        int distanceDig;
        int mins;
        int seconds;
        int paceMins;
        int paceSec;
        int workoutId;
        string notes;
};
#endif