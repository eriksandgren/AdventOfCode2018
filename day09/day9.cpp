#include <iostream>
#include <list>

int main ()
{   
    int numPlayers = 446;
    long int lastMarble = 71522 * 100;
    int percent = 71522;
    long int current_idx = 0;
    long int numMarbles = 1;
    std::list<int> marbles_l;
    marbles_l.push_back(0);
    std::list<int>::iterator it = marbles_l.begin();
    long int points_marble;
    for (int i = 0; i < lastMarble + 1; i++)
    {
       if (i % 23 == 0)
       {
           current_idx = (current_idx - 7) % numMarbles;
           it = marbles_l.begin();
           std::advance(it, current_idx);
           points_marble = i + *it;
           marbles_l.erase(it++);
           numMarbles--;
       } 
       else
       {
            current_idx = 1 + (current_idx + 1) % numMarbles;
            it = marbles_l.begin();
            std::advance(it, current_idx);
            it = marbles_l.insert(it, i);
            numMarbles++;
       }
       if (i % 71522 == 0)
       {
          std::cout << "Percent " << i / 71522 << std::endl; 
       }
    }
    return 0;
}