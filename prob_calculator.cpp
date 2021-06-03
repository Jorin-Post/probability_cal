#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <ctime>
#include <cstdarg>

using namespace std;
class Hat{
private:
vector<string>balls;
vector<int>random_vec;
int Random(int max, int draw, int t){
    int rand_val;
    random_vec.clear();
    srand(time(0));
    for(int i = 0; i< draw; i++){  
        random_vec.push_back((rand()% max));
        max -= 1;
    } 
}
void Balls_in (string bal){  
    if (bal.back() != '-'){
        bal += '-';
    }
    while (bal.size() > 1)
    {
        int ballnumer = bal.find('=');
        string numstr = bal.substr(ballnumer +1);
        string balstr = bal.substr(0, ballnumer);
        int balln = stoi(numstr);
        for (int i=0; i < balln; i++){
            balls.push_back(balstr);
        }
        int erasenum = bal.find('-');
        bal.erase(0, erasenum +1);
    }
}
void experiment(string expec_balls, int balls_drown, int exper_times){
    vector<string>expec_balls_vec;
    vector<string>balls_random;
        //// placing a - at the end of the string
    if (expec_balls.back() != '-'){
            expec_balls += '-';
        }
        //// make a vector of the string
    while (expec_balls.size() > 1)
        {
            int ballnumer = expec_balls.find('=');
            string numstr = expec_balls.substr(ballnumer +1);
            string balstr = expec_balls.substr(0, ballnumer);
            int balln = stoi(numstr);
            for (int i=0; i < balln; i++){
                expec_balls_vec.push_back(balstr);
            }
            int erasenum = expec_balls.find('-');
            expec_balls.erase(0, erasenum +1);
        }
        //// when balls expected exets balls drawn
    if (balls_drown > balls.size()){
            balls_drown = balls.size();
        }
        int BINGO =0;
    for(int t =0; t < exper_times; t++){  
        int count = 0;
        vector<string>list_expec_balls = expec_balls_vec;
        vector<string>balls_erase = balls;

            //// cals random fuction in class
        Random(balls.size(), balls_drown, t);

            //// makes vector random balls
        for(int i=0; i < random_vec.size(); i++){
            balls_random.push_back(balls_erase[random_vec[i]]); 
            balls_erase[random_vec[i]].erase();
            vector<string>balls_temp {};
                //// cleans out vector balls_erase
            for(int i1 =0; i1 < balls_erase.size(); i1++){
                if (balls_erase[i1] != ""){
                    balls_temp.push_back(balls_erase[i1]);
                }
            }
            balls_erase.clear();
            balls_erase = balls_temp;      
        }

           //// count how match expected is in the vectors
        for(int i=0; i < list_expec_balls.size(); i++){
            for(int r=0; r < balls_random.size(); r++){
                if (list_expec_balls[i] == balls_random[r]){
                    balls_random[r].erase();
                    count ++;
                    break;
                }
            }
        }    

        for(int i =0; i < balls_random.size(); i++){
            cout<< balls_random[i]<< '\t';
        }       
        cout << endl;
        for(int i =0; i < list_expec_balls.size(); i++){
            cout<< list_expec_balls[i]<< '\t';
        }
        cout << endl;
        balls_random.clear();

            /// keep count
        if ( count >= list_expec_balls.size()){
            BINGO ++;
        }
    }
    cout << BINGO << endl;
}  
public:
void Run(string start_balls, string want_balls, int Draw, int times){
    Balls_in(start_balls);
    experiment(want_balls, Draw, times);
}
};

int main(){
    Hat hat1, hat2, hat3;
    
    hat1.Run("green=3-blue=2-red=2-yellow=2","red=2", 5, 2);
}