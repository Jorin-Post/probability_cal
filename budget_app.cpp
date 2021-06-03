#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;
using std::to_string;

class Category { // Main class
string category_name; float chash = 0;
vector <string> d_from; vector<float> d_amount;
vector <string> w_product; vector <float> w_amount{}; 

public:
void info(string ca_na){
    category_name = ca_na;
}
void diposit(string d_pr, float d_am){
    d_from.push_back(d_pr); d_amount.push_back(d_am);
    int i = d_amount.size() -1;
    chash+= d_amount[i];
}
void withdraw(string w_pr, float w_am){
    w_product.push_back(w_pr); 
    w_am += - w_am - w_am;    
    w_amount.push_back(w_am);
    int i = w_amount.size() -1 ;
    if (chash >= w_amount[i]){
        chash+= w_amount[i];
    }
    else{
        cout<< "To low on chash." << endl;
    }   
}
string TITLE(){
    string title; string title1; string title2;
    int title_num = (30 - category_name.size())/2;
    for (int i = 0; i < title_num; i++){
        title1 += "*";
    }
    for (int i = 0; i < title_num; i++){
        title2 += "*";
    }
    title = title1 + category_name + title2;
    if (title.size() < 30){
        title += "*";
    }
    return title;    
}
string MONEY(int i){
    string money; string space; string str_d_amount;
    str_d_amount = to_string(d_amount[i]);
    int money_num = 30 - (d_from[i].size() + str_d_amount.size());
        
    for (int i1 = 0; i1 < 4; i1++){
        str_d_amount.pop_back();
        money_num += 1;
    }
    for (int i2 = 0; i2 < money_num; i2++){
        space += " ";
    }
        money += d_from[i] + space + str_d_amount + '\n';

    return money;
}
string STUF(int i){
    string stuf; string space; string str_w_amount;
    str_w_amount = to_string(w_amount[i]);
    int stuf_num = 30 - (w_product[i].size() + str_w_amount.size());
        
    for (int i1 = 0; i1 < 4; i1++){
        str_w_amount.pop_back();
        stuf_num += 1;
    }
    for (int i2 = 0; i2 < stuf_num; i2++){
        space += " ";
    }
        stuf += w_product[i] + space + str_w_amount + '\n';

    return stuf;
}
string TOTAL(){
    string total = "Total:";
    string str_chash = to_string(chash);
    int total_num = 30 - (total.size() + str_chash.size());
    for (int i1 = 0; i1 < 4; i1++){
        str_chash.pop_back();
        total_num += 1;
    }
    for (int i=0; i < total_num; i++){
        total += " ";
    }
    total += str_chash;
    return total;
}
string CHECK(){
    string check;
    check = TITLE() +'\n';
    for (int i = 0; i < d_amount.size(); i++){
        check += MONEY(i);
    }
    for (int i = 0; i < w_amount.size(); i++){
        check += STUF(i);
    }
    check += '\n' + TOTAL() + '\n';
    return check;
}
};

int main(){
Category food, car;
food.info("FOOD");
car.info("CAR");
food.diposit("Bank", 100);
food.withdraw("Bread", 10);
food.withdraw("Beef", 17);
food.withdraw("chicken", 5.7);
cout << food.CHECK() << endl;

car.diposit("Bank", 1000);
car.withdraw("Tiers", 124);
cout << car.CHECK() << endl;
}